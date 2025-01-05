import cv2
import numpy as np
from flask import Flask, request, jsonify
import mediapipe as mp
from rembg import remove
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

# Initialize Mediapipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def remove_background(image):
    """Removes background from the outfit image."""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for rembg
    image_no_bg = remove(image)
    return cv2.cvtColor(np.array(image_no_bg), cv2.COLOR_RGB2BGR)  # Back to BGR

def overlay_outfit(user_image, outfit_image):
    """Aligns the outfit with user's pose and overlays it."""
    # Detect pose landmarks
    user_image_rgb = cv2.cvtColor(user_image, cv2.COLOR_BGR2RGB)
    results = pose.process(user_image_rgb)

    if not results.pose_landmarks:
        raise ValueError("No pose landmarks detected. Ensure a full-body image.")

    # Extract key landmarks
    landmarks = results.pose_landmarks.landmark

    def get_landmark_coords(landmark):
        """Convert normalized landmarks to pixel coordinates."""
        x = int(landmark.x * user_image.shape[1])
        y = int(landmark.y * user_image.shape[0])
        return max(0, min(user_image.shape[1] - 1, x)), max(0, min(user_image.shape[0] - 1, y))

    # Key landmarks: shoulders, hips, etc.
    left_shoulder = get_landmark_coords(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER])
    right_shoulder = get_landmark_coords(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER])
    left_hip = get_landmark_coords(landmarks[mp_pose.PoseLandmark.LEFT_HIP])
    right_hip = get_landmark_coords(landmarks[mp_pose.PoseLandmark.RIGHT_HIP])

    # Calculate outfit width and height
    outfit_width = abs(left_shoulder[0] - right_shoulder[0])
    outfit_height = abs(left_hip[1] - left_shoulder[1])

    if outfit_width == 0 or outfit_height == 0:
        raise ValueError("Invalid pose landmarks detected. Try another image.")

    # Resize the outfit image
    outfit_image = cv2.resize(outfit_image, (outfit_width, outfit_height))

    # Positioning of outfit on the user image
    x_offset = min(left_shoulder[0], right_shoulder[0])
    y_offset = left_shoulder[1]  # Adjust this if you want to tweak the vertical position

    # Overlay the outfit onto the user image
    for i in range(outfit_image.shape[0]):
        for j in range(outfit_image.shape[1]):
            if np.any(outfit_image[i, j] > 0):  # Check if the pixel is not transparent
                y, x = y_offset + i, x_offset + j
                if 0 <= y < user_image.shape[0] and 0 <= x < user_image.shape[1]:
                    user_image[y, x] = outfit_image[i, j]

    return user_image

@app.route('/tryon', methods=['POST'])
def try_on_outfit():
    """Endpoint to handle outfit try-on."""
    try:
        # Get user image and outfit image from request
        user_image_file = request.files['user_image']
        outfit_image_file = request.files['outfit_image']

        # Read images
        user_image = cv2.imdecode(np.frombuffer(user_image_file.read(), np.uint8), cv2.IMREAD_COLOR)
        outfit_image = cv2.imdecode(np.frombuffer(outfit_image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Validate image dimensions
        if user_image is None or outfit_image is None:
            raise ValueError("Invalid image(s) uploaded. Please check the files.")

        # Remove background from the outfit image
        outfit_image = remove_background(outfit_image)

        # Overlay outfit onto user image
        output_image = overlay_outfit(user_image, outfit_image)

        # Encode output image to Base64
        _, buffer = cv2.imencode('.png', output_image)
        base64_image = base64.b64encode(buffer).decode('utf-8')

        return jsonify({'processed_image': base64_image})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
