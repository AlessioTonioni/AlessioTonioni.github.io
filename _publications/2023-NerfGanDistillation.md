---
title: "NeRF-GAN Distillation for Efficient 3D-Aware Generation with Convolutions"
authors: 'Mohamad Shahbazi, Evangelos Ntavelis, Alessio Tonioni, Edo Collins, Danda Pani Paudel, Martin Danelljan, Luc Van Gool'
collection: "Generative Models"
permalink: /publication/NerfGanDistillation
excerpt: 'StyleGan like network can approximate NerfGAN.'
date: 2023-03-22
venue: 'Arxive'
paperurl: 'https://arxiv.org/pdf/2303.12865'
citation: 'Shahbazi, Mohamad, et al. "NeRF-GAN Distillation for Efficient 3D-Aware Generation with Convolutions." arXiv preprint arXiv:2303.12865 (2023).'
pubtype: 'conference'
---

## Abstract

Pose-conditioned convolutional generative models struggle with high-quality 3D-consistent image generation from single-view datasets, due to their lack of sufficient 3D priors. Recently, the integration of Neural Radiance Fields (NeRFs) and generative models, such as Generative Adversarial Networks (GANs), has transformed 3D-aware generation from single-view images. NeRF-GANs exploit the strong inductive bias of 3D neural representations and volumetric rendering at the cost of higher computational complexity. This study aims at revisiting pose-conditioned 2D GANs for efficient 3D-aware generation at inference time by distilling 3D knowledge from pretrained NeRF-GANS. We propose a simple and effective method, based on re-using the well-disentangled latent space of a pre-trained NeRF-GAN in a pose-conditioned convolutional network to directly generate 3D-consistent images corresponding to the underlying 3D representations. Experiments on several datasets demonstrate that the proposed method obtains results comparable with volumetric rendering in terms of quality and 3D consistency while benefiting from the superior computational advantage of convolutional networks. 
| [Paper](https://arxiv.org/pdf/2303.12865) | [Code](https://github.com/mshahbazi72/NeRF-GAN-Distillation) |

## BibTex 

```
@article{shahbazi2023nerf,
  title={NeRF-GAN Distillation for Efficient 3D-Aware Generation with Convolutions},
  author={Shahbazi, Mohamad and Ntavelis, Evangelos and Tonioni, Alessio and Collins, Edo and Paudel, Danda Pani and Danelljan, Martin and Van Gool, Luc},
  journal={arXiv preprint arXiv:2303.12865},
  year={2023}
}
```
