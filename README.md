## Abstract

This project, titled "Brush Stroke Parameterized Style Transfer," explores the application of parameterized brush stroke techniques in the field of style transfer. By leveraging advanced algorithms and machine learning models, the project aims to achieve high-quality artistic transformations of images. The implementation is designed to be efficient and user-friendly, providing customizable parameters to control the style transfer process. This work has potential applications in digital art, graphic design, and other creative industries.

## Methodology

![Methodology](images/Method.png)

## Results

### Video Result

<video width="700" height="480" controls>
  <source src="videos/clemson.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

 video demonstrates the application of the parameterized brush strokes optimizatoin using content and  style transfer .

### Image Results

<div id="image-gallery" style="position: relative; width: 720px; height: 360px;">
  <img id="gallery-image" src="images/bridge.png" alt="Result 1" width="720" height="360" style="transition: transform 0.25s ease;">
  <button id="prev-button" style="position: absolute; top: 50%; left: 0; transform: translateY(-50%); background: rgba(128, 128, 128, 0.9); border: none; font-size: 2em; cursor: pointer;">&#9664;</button>
  <button id="next-button" style="position: absolute; top: 50%; right: 0; transform: translateY(-50%); background: rgba(128, 128, 128, 0.9); border: none; font-size: 2em; cursor: pointer;">&#9654;</button>
</div>
<!-- <p id="image-description">This image shows the result of applying the style transfer technique to a bridge scene. Notice the intricate brush strokes and the overall artistic transformation.</p> -->

<script>
  const images = [
    { src: 'images/bridge.png', description: 'This image shows the result of applying the style transfer technique to content image - Golden Gate Bridge and Style image Van Gogh\'s Starry Night. Notice the intricate brush strokes and the overall artistic transformation.' },
    { src: 'images/strokes_zoomed.png', description: 'Zoomed in view of brush strokes and texture after pixel optimization' },
    { src: 'images/me.png', description: 'Style transfer applied on human (It\'s me in the photo :) )' },
    { src: 'images/Olive_tree_garden.png', description: 'The style transfer is applied to Olive garden with stylization using the famous painting - The stone Bench in the Garden of Saint-Paul Hospital by Van Gogh' }
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

## Social and Other Links

[![Website](https://img.shields.io/badge/Website-Portfolio-blue?logo=google-chrome)](https://maheshmeleti.github.io/)

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/maheshmeleti/brushstroke-parameterized-style-transfer-pytorch)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/mahesh-meleti/)

[![Paper](https://img.shields.io/badge/Course-Paper-blue)](paper/BrushStroke_StyleTransfer.pdf)

[![Presentation](https://img.shields.io/badge/Course-Presentation-blue)](paper/final_project presentation.pdf)

[![Course-homepage](https://img.shields.io/badge/Course-Page-blue)](https://sites.google.com/view/cpsc8810-2024fall/home)




## References

@article{kotovenko_cvpr_2021,
    title={Rethinking Style Transfer: From Pixels to Parameterized Brushstrokes},
    author={Dmytro Kotovenko and Matthias Wright and Arthur Heimbrecht and Bj{\"o}rn Ommer},
    journal={CVPR},
    year={2021}
}

## Citation

@misc{meleti2024brushstroke, title={Brush Stroke Parameterized Style Transfer}, author={Uma Maheswara R Meleti}, year={2024}, url={https://github.com/maheshmeleti/brushstroke-parameterized-style-transfer-pytorch}, }