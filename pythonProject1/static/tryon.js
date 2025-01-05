document.getElementById("tryOnButton").addEventListener("click", async () => {
  const userImageInput = document.getElementById("userImage");
  const outfitImageInput = document.getElementById("outfitImage");

  if (!userImageInput.files[0] || !outfitImageInput.files[0]) {
    alert("Please upload both user and outfit images.");
    return;
  }

  const formData = new FormData();
  formData.append("user_image", userImageInput.files[0]);
  formData.append("outfit_image", outfitImageInput.files[0]);

  try {
    const response = await fetch("http://127.0.0.1:5000/tryon", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errorData = await response.json();
      alert("Error: " + errorData.error);
      return;
    }

    const result = await response.json();
    const outputImage = document.getElementById("outputImage");
    outputImage.src = "data:image/png;base64," + result.processed_image;
  } catch (error) {
    console.error("Error:", error);
    alert("An unexpected error occurred. Please try again.");
  }
});
