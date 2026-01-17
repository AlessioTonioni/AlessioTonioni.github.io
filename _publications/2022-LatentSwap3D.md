---
title: "LatentSwap3D: Semantic Edits on 3D Image GANs"
authors: 'Enis Simsar, Alessio Tonioni, Evin Pınar Örnek, Federico Tombari'
collection: "3D Computer Vision"
permalink: /publication/LS3D
excerpt: 'Semantic edits in the latent space of Nerf based gan.'
date: 2022-12-02
venue: 'ICCV-W'
paperurl: 'https://arxiv.org/pdf/2212.01381'
citation: 'Simsar, Enis, et al. "LatentSwap3D: Semantic Edits on 3D Image GANs." arXiv preprint arXiv:2212.01381 (2022).'
pubtype: 'conference'
---

## Abstract

Recent 3D-aware GANs rely on volumetric rendering techniques to disentangle the pose and appearance of objects, de facto generating entire 3D volumes rather than single-view 2D images from a latent code. Complex image editing tasks can be performed in standard 2D-based GANs (e.g., StyleGAN models) as manipulation of latent dimensions. However, to the best of our knowledge, similar properties have only been partially explored for 3D-aware GAN models. This work aims to fill this gap by showing the limitations of existing methods and proposing LatentSwap3D, a model-agnostic approach designed to enable attribute editing in the latent space of pre-trained 3D-aware GANs. We first identify the most relevant dimensions in the latent space of the model controlling the targeted attribute by relying on the feature importance ranking of a random forest classifier. Then, to apply the transformation, we swap the top-K most relevant latent dimensions of the image being edited with an image exhibiting the desired attribute. Despite its simplicity, LatentSwap3D provides remarkable semantic edits in a disentangled manner and outperforms alternative approaches both qualitatively and quantitatively. We demonstrate our semantic edit approach on various 3D-aware generative models such as pi-GAN, GIRAFFE, StyleSDF, MVCGAN, EG3D and VolumeGAN, and on diverse datasets, such as FFHQ, AFHQ, Cats, MetFaces, and CompCars. 
| [Paper](https://arxiv.org/pdf/2212.01381) | [Project Page](https://enisimsar.github.io/latentswap3d/)

## BibTex 

```
@article{simsar2022latentswap3d,
  title={LatentSwap3D: Semantic Edits on 3D Image GANs},
  author={Simsar, Enis and Tonioni, Alessio and {\"O}rnek, Evin P{\i}nar and Tombari, Federico},
  journal={arXiv preprint arXiv:2212.01381},
  year={2022}
}
```
