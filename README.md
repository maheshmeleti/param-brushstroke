## Abstract

Computer Vision-based Style Transfer techniques have been used for many years to represent artistic style. However, most contemporary methods have been restricted to the pixel domain; in other words, the style transfer approach has been modifying the image pixels to incorporate artistic style. However, real artistic work is made of brush strokes with different colors on a canvas. Pixel-based approaches are unnatural for representing these images. Hence, this paper discusses a style transfer method that represents the image in the brush stroke domain instead of the RGB domain, which has better visual improvement over pixel-based methods. 

## Methodology

![Methodology](images/Method.png)

## Results

### Video Result

<video width="700" height="480" controls>
  <source src="videos/clemson.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

This video demonstrates the application of the brush stroke parameterized style transfer technique on a sample video. The transformation showcases the effectiveness of the algorithm in maintaining high-quality artistic effects.

### Image Results

<div id="image-gallery" style="position: relative; width: 720px; height: 360px;">
  <img id="gallery-image" src="images/bridge.png" alt="Result 1" width="720" height="360" style="transition: transform 0.25s ease;">
  <button id="prev-button" style="position: absolute; top: 50%; left: 0; transform: translateY(-50%); background: rgba(128, 128, 128, 0.9); border: none; font-size: 2em; cursor: pointer;">&#9664;</button>
  <button id="next-button" style="position: absolute; top: 50%; right: 0; transform: translateY(-50%); background: rgba(128, 128, 128, 0.9); border: none; font-size: 2em; cursor: pointer;">&#9654;</button>
</div>
<p id="image-description">This image shows the result of applying the style transfer technique to a bridge scene. Notice the intricate brush strokes and the overall artistic transformation.</p>

<script>
  const images = [
    { src: 'images/bridge.png', description: 'This image shows the result of applying the style transfer technique to a bridge scene. Notice the intricate brush strokes and the overall artistic transformation.' },
    { src: 'images/strokes_zoomed.png', description: 'Here, we have a zoomed-in view of the brush strokes applied to a different scene. The details highlight the precision and customization capabilities of the algorithm.' },
    { src: 'images/me.png', description: 'This image demonstrates the style transfer applied to a portrait. The transformation retains the subject\'s features while adding an artistic flair.' },
    { src: 'images/Olive_tree_garden.png', description: 'In this example, the style transfer is applied to a garden scene. The brush strokes and color adjustments create a visually appealing artistic rendition.' }
  ];

  let currentIndex = 0;

  document.getElementById('prev-button').addEventListener('click', () => {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
    updateGallery();
  });

  document.getElementById('next-button').addEventListener('click', () => {
    currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
    updateGallery();
  });

  document.getElementById('gallery-image').addEventListener('click', () => {
    const img = document.getElementById('gallery-image');
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');
    if (img.style.transform === 'scale(1.5)') {
      img.style.transform = 'scale(1)';
      prevButton.style.left = '0';
      nextButton.style.right = '0';
    } else {
      img.style.transform = 'scale(1.5)';
      prevButton.style.left = '-30%';
      nextButton.style.right = '-30%';
    }
  });

  function updateGallery() {
    document.getElementById('gallery-image').src = images[currentIndex].src;
    document.getElementById('gallery-image').alt = `Result ${currentIndex + 1}`;
    document.getElementById('image-description').textContent = images[currentIndex].description;
  }
</script>

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/maheshmeleti/brushstroke-parameterized-style-transfer-pytorch)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/mahesh-meleti/)