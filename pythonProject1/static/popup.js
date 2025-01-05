document.getElementById('try-on-button').addEventListener('click', async () => {
  const userImage = document.getElementById('user-image').files[0];
  const outfitImage = document.getElementById('outfit-image').files[0];

  if (!userImage || !outfitImage) {
    alert('Please upload both images!');
    return;
  }

  const formData = new FormData();
  formData.append('user_image', userImage);
  formData.append('outfit_image', outfitImage);

  try {
    const response = await fetch('http://127.0.0.1:5000/tryon', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    const data = await response.json();
    const outputImage = document.getElementById('output-image');
    outputImage.src = `data:image/png;base64,${data.processed_image}`;
  } catch (error) {
    console.error('Error:', error);
    alert('Failed to process the images.');
  }
});
