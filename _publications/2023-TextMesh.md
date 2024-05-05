---
title: "TextMesh: Generation of Realistic 3D Meshes From Text Prompts"
authors: 'Christina Tsalicoglou, Fabian Manhardt, Alessio Tonioni, Michael Niemeyer, Federico Tombari'
collection: "Generative Models"
permalink: /publication/TextMesh
excerpt: 'Turning Tetx prompt into full 3D meshes'
date: 2023-04-24
venue: '3DV24'
paperurl: 'https://arxiv.org/pdf/2304.12439'
citation: 'Tsalicoglou, Christina, et al. "TextMesh: Generation of Realistic 3D Meshes From Text Prompts." arXiv preprint arXiv:2304.12439 (2023).'
pubtype: 'conference'
---

## Abstract

The ability to generate highly realistic 2D images from mere text prompts has recently made huge progress in terms of speed and quality, thanks to the advent of image diffusion models. Naturally, the question arises if this can be also achieved in the generation of 3D content from such text prompts. To this end, a new line of methods recently emerged trying to harness diffusion models, trained on 2D images, for supervision of 3D model generation using view dependent prompts. While achieving impressive results, these methods, however, have two major drawbacks. First, rather than commonly used 3D meshes, they instead generate neural radiance fields (NeRFs), making them impractical for most real applications. Second, these approaches tend to produce over-saturated models, giving the output a cartoonish looking effect. Therefore, in this work we propose a novel method for generation of highly realistic-looking 3D meshes. To this end, we extend NeRF to employ an SDF backbone, leading to improved 3D mesh extraction. In addition, we propose a novel way to finetune the mesh texture, removing the effect of high saturation and improving the details of the output 3D mesh.

| [Paper](https://arxiv.org/pdf/2304.12439) | [Project Page](https://fabi92.github.io/textmesh/) | 

## BibTex 

```
@article{tsalicoglou2023textmesh,
  title={TextMesh: Generation of Realistic 3D Meshes From Text Prompts},
  author={Tsalicoglou, Christina and Manhardt, Fabian and Tonioni, Alessio and Niemeyer, Michael and Tombari, Federico},
  journal={arXiv preprint arXiv:2304.12439},
  year={2023}
}
```
