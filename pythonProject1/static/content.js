document.addEventListener('click', (event) => {
  if (event.target.tagName === 'IMG') {
    const imgSrc = event.target.src;
    chrome.storage.local.set({ selectedImage: imgSrc });
    alert('Image selected! You can now process it in the extension.');
  }
});
