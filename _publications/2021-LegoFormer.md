---
title: "LegoFormer: Transformers for Block-by-Block Multi-view 3D Reconstruction"
authors: 'Farid Yagubbayli, Alessio Tonioni and Federico Tombari'
collection: "3D Computer Vision"
permalink: /publication/LegoFormer
excerpt: 'Transformers for voxel based 3D reconstruction.'
date: 2021-07-06
venue: 'Arxive'
paperurl: 'https://arxiv.org/abs/2106.12102'
citation: 'Yagubbayli, Farid, Alessio Tonioni, and Federico Tombari. "LegoFormer: Transformers for Block-by-Block Multi-view 3D Reconstruction." arXiv preprint arXiv:2106.12102 (2021).'
pubtype: 'conference'
---

## Abstract

Most modern deep learning-based multi-view 3D reconstruction techniques use RNNs or fusion modules to combine information from multiple images after encoding them. These two separate steps have loose connections and do not consider all available information while encoding each view. We propose LegoFormer, a transformer-based model that unifies object reconstruction under a single framework and parametrizes the reconstructed occupancy grid by its decomposition factors. This reformulation allows the prediction of an object as a set of independent structures then aggregated to obtain the final reconstruction. Experiments conducted on ShapeNet display the competitive performance of our network with respect to the state-of-the-art methods. We also demonstrate how the use of self-attention leads to increased interpretability of the model output.
| [Paper](https://arxiv.org/abs/2106.12102) | [Code](https://github.com/faridyagubbayli/LegoFormer)

## BibTex 

```
@article{yagubbayli2021legoformer,
  title={LegoFormer: Transformers for Block-by-Block Multi-view 3D Reconstruction},
  author={Yagubbayli, Farid and Tonioni, Alessio and Tombari, Federico},
  journal={arXiv preprint arXiv:2106.12102},
  year={2021}
}
```
