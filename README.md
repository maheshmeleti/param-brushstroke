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

This video demonstrates the application of the parameterized brush strokes optimization using content and style transfer.

### Image Results

<span style="color: blue;">Click on the image to zoom</span>

<div id="image-gallery" style="position: relative; width: 720px; height: 360px;">
  <img id="gallery-image" src="images/bridge.png" alt="Result 1" width="720" height="360" style="transition: transform 0.25s ease;">
  <button id="prev-button" style="position: absolute; top: 50%; left: 0; transform: translateY(-50%); background: rgba(128, 128, 128, 0.9); border: none; font-size: 2em; cursor: pointer;">&#9664;</button>
  <button id="next-button" style="position: absolute; top: 50%; right: 0; transform: translateY(-50%); background: rgba(128, 128, 128, 0.9); border: none; font-size: 2em; cursor: pointer;">&#9654;</button>
</div>
<p id="image-description" style="text-align: center; color: white; background: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 5px; width: 720px; margin: 0 auto; position: relative; top: -20px;">
  This image shows the result of applying the style transfer technique to a bridge scene. Notice the intricate brush strokes and the overall artistic transformation.
</p>

<script>
  const images = [
    { src: 'images/bridge.png', description: 'This image shows the result of applying the style transfer technique to content image - Golden Gate Bridge and Style image Van Gogh\'s Starry Night. Notice the intricate brush strokes and the overall artistic transformation.' },
    { src: 'images/strokes_zoomed.png', description: 'Zoomed in view of brush strokes and texture after pixel optimization' },
    { src: 'images/me.png', description: 'Style transfer applied on human (It\'s me in the photo :) )' },
    { src: 'images/Olive_tree_garden.png', description: 'The style transfer is applied to Olive garden with stylization using the famous The stone Bench in the Garden of Saint-Paul Hospital by Van Gogh' }
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
    const caption = document.getElementById('image-description');
    if (img.style.transform === 'scale(1.5)') {
      img.style.transform = 'scale(1)';
      prevButton.style.left = '0';
      nextButton.style.right = '0';
      caption.style.top = '0px';
    } else {
      img.style.transform = 'scale(1.5)';
      prevButton.style.left = '-30%';
      nextButton.style.right = '-30%';
      caption.style.top = '40px'; // Move the caption down when zoomed
    }
  });

  function updateGallery() {
    const img = document.getElementById('gallery-image');
    const caption = document.getElementById('image-description');
    img.src = images[currentIndex].src;
    img.alt = `Result ${currentIndex + 1}`;
    caption.textContent = images[currentIndex].description;
  }

  // Initialize the gallery with the first image description
  updateGallery();
</script>

## Social and Other Links

<div style="display: flex; gap: 10px;">
  <a href="https://github.com/maheshmeleti/brushstroke-parameterized-style-transfer-pytorch">
    <img src="https://img.shields.io/badge/GitHub-Repository-blue?logo=github" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/mahesh-meleti/">
    <img src="https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin" alt="LinkedIn">
  </a>
  <a href="paper/BrushStroke_StyleTransfer.pdf">
    <img src="https://img.shields.io/badge/Project%20Paper-3a3e51" alt="Paper">
  </a>
  <a href="paper/final_project_presentation.pdf">
    <img src="https://img.shields.io/badge/Course-Presentation-blue" alt="Presentation">
  </a>
  <a href="https://sites.google.com/view/cpsc8810-2024fall/home">
    <img src="https://img.shields.io/badge/Course-page-blue" alt="course-link">
  </a>
</div>

## References

@article{kotovenko_cvpr_2021,
    title={Rethinking Style Transfer: From Pixels to Parameterized Brushstrokes},
    author={Dmytro Kotovenko and Matthias Wright and Arthur Heimbrecht and Bj{\"o}rn Ommer},
    journal={CVPR},
    year={2021}
}

## Citation

@misc{meleti2024brushstroke, title={Brush Stroke Parameterized Style Transfer}, author={Uma Maheswara R Meleti}, year={2024}, url={https://github.com/maheshmeleti/brushstroke-parameterized-style-transfer-pytorch}, }