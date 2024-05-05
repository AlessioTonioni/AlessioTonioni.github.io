---
title: "NeRF-Supervised Deep Stereo"
authors: 'Fabio Tosi, Alessio Tonioni, Daniele De Gregorio, Matteo Poggi'
collection: "Depth Estimation"
permalink: /publication/NerfStereo
excerpt: 'NeRF makes great groundtruth for stereo systems.'
date: 2023-03-30
venue: 'CVPR23'
paperurl: 'https://arxiv.org/pdf/2303.17603'
citation: 'Tosi, Fabio, et al. "NeRF-Supervised Deep Stereo." arXiv preprint arXiv:2303.17603 (2023).'
pubtype: 'conference'
---

## Abstract

We introduce a novel framework for training deep stereo networks effortlessly and without any ground-truth. By leveraging state-of-the-art neural rendering solutions, we generate stereo training data from image sequences collected with a single handheld camera. On top of them, a NeRF-supervised training procedure is carried out, from which we exploit rendered stereo triplets to compensate for occlusions and depth maps as proxy labels. This results in stereo networks capable of predicting sharp and detailed disparity maps. Experimental results show that models trained under this regime yield a 30-40% improvement over existing self-supervised methods on the challenging Middlebury dataset, filling the gap to supervised models and, most times, outperforming them at zero-shot generalization.
| [Paper](https://arxiv.org/pdf/2303.17603) | [Project Page](https://nerfstereo.github.io/) | [Code](https://github.com/fabiotosi92/NeRF-Supervised-Deep-Stereo) |

## BibTex 

```
@article{tosi2023nerf,
  title={NeRF-Supervised Deep Stereo},
  author={Tosi, Fabio and Tonioni, Alessio and De Gregorio, Daniele and Poggi, Matteo},
  journal={arXiv preprint arXiv:2303.17603},
  year={2023}
}
```
