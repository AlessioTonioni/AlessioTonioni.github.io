---
title: "A Divide et Impera Approach for 3D Shape Reconstruction from Multiple Views"
authors: 'Riccardo Spezialetti, David Joseph Tan, Alessio Tonioni, Keisuke Tateno and Federico Tombari'
collection: "3D Computer Vision"
permalink: /publication/DivideEtImpera
excerpt: 'A deep learning pipeline for multi view reconstruction.'
date: 2020-11-25
venue: '3DV'
paperurl: 'https://arxiv.org/pdf/2011.08534.pdf'
citation: 'Spezialetti, R., Tan, D.J., Tonioni, A., Tateno, K. and Tombari, F., 2020. A Divide et Impera Approach for 3D Shape Reconstruction from Multiple Views. 3DV20.'
pubtype: 'conference'
---

## Abstract

Estimating the 3D shape of an object from a single or
multiple images has gained popularity thanks to the recent
breakthroughs powered by deep learning. Most approaches
regress the full object shape in a canonical pose, possibly
extrapolating the occluded parts based on the learned priors. 
However, their viewpoint invariant technique often discards 
the unique structures visible from the input images.
In contrast, this paper proposes to rely on viewpoint variant 
reconstructions by merging the visible information from
the given views. Our approach is divided into three steps.
Starting from the sparse views of the object, we first align
them into a common coordinate system by estimating the
relative pose between all the pairs. Then, inspired by the
traditional voxel carving, we generate an occupancy grid
of the object taken from the silhouette on the images and
their relative poses. Finally, we refine the initial reconstruction to build a clean 3D model which preserves the details
from each viewpoint. To validate the proposed method, we
perform a comprehensive evaluation on the ShapeNet reference benchmark in terms of relative pose estimation and
3D shape reconstruction.

| [Paper](https://arxiv.org/pdf/2011.08534.pdf) | 

## BibTex 

```
@article{spezialetti2020divide,
  title={A Divide et Impera Approach for 3D Shape Reconstruction from Multiple Views},
  author={Spezialetti, Riccardo and Tan, David Joseph and Tonioni, Alessio and Tateno, Keisuke and Tombari, Federico},
  journal={International Conference on 3D Vision},
  year={2020}
}

```
