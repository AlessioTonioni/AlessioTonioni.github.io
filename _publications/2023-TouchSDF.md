---
title: "TouchSDF: A DeepSDF Approach for 3D Shape Reconstruction using Vision-Based Tactile Sensing"
authors: "Mauro Comi, Yijiong Lin, Alex Church, Alessio Tonioni, Laurence Aitchison, Nathan F Lepora"
collection: "Generative Models"
permalink: "/publication/TouchSDF"
excerpt: 'Touch sensors meet 3D computer vision'
date: 2023-11-21
venue: 'RAL'
paperurl: 'https://arxiv.org/pdf/2311.12602'
citation: 'Comi, Mauro, et al. "Touchsdf: A deepsdf approach for 3d shape reconstruction using vision-based tactile sensing." IEEE Robotics and Automation Letters (2024).'
pubtype: 'journal'
---

## Abstract

Humans rely on their visual and tactile senses to develop a comprehensive 3D understanding of their physical environment. Recently, there has been a growing interest in exploring and manipulating objects using data-driven approaches that utilise high-resolution vision-based tactile sensors. However, 3D shape reconstruction using tactile sensing has lagged behind visual shape reconstruction because of limitations in existing techniques, including the inability to generalise over unseen shapes, the absence of real-world testing, and limited expressive capacity imposed by discrete representations. To address these challenges, we propose TouchSDF, a Deep Learning approach for tactile 3D shape reconstruction that leverages the rich information provided by a vision-based tactile sensor and the expressivity of the implicit neural representation DeepSDF. Our technique consists of two components: (1) a Convolutional Neural Network that maps tactile images into local meshes representing the surface at the touch location, and (2) an implicit neural function that predicts a signed distance function to extract the desired 3D shape. This combination allows TouchSDF to reconstruct smooth and continuous 3D shapes from tactile inputs in simulation and realworld settings, opening up research avenues for robust 3Daware representations and improved multimodal perception in robotics. 

| [Paper](https://arxiv.org/pdf/2311.12602) | [Project Page](https://touchsdf.github.io/) | 

## BibTex 

```
@article{comi2024touchsdf,
  title={Touchsdf: A deepsdf approach for 3d shape reconstruction using vision-based tactile sensing},
  author={Comi, Mauro and Lin, Yijiong and Church, Alex and Tonioni, Alessio and Aitchison, Laurence and Lepora, Nathan F},
  journal={IEEE Robotics and Automation Letters},
  year={2024},
  publisher={IEEE}
}
```
