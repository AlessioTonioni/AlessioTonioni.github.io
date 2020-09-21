---
title: "Continual Adaptation for Deep Stereo"
authors: ' Matteo Poggi, Alessio Tonioni, Fabio Tosi, Stefano Mattoccia and Luigi Di Stefano'
collection: 'Depth Estimation'
permalink: /publication/realTimII
excerpt: 'In this paper we propose an etension of our real-time self adaptive deep stereo system.'
date: 2020-07-14
venue: 'IEEE Transactions on Pattern Analysis and Machine Intelligence'
paperurl: 'https://arxiv.org/pdf/1810.05424'
citation: 'Poggi, M., Tonioni, A., Tosi, F., Mattoccia, S., & Di Stefano, L. (2019). IEEE Transactions on Pattern Analysis and Machine Intelligence, 2020'
pubtype: 'review'
---

## Abstract

Depth estimation from stereo images is carried out with unmatched results by convolutional neural networks trained end-to-end to regress dense disparities. Like for most tasks, this is possible if large amounts of labelled samples are available for training, possibly covering the whole data distribution encountered at deployment time. Being such an assumption systematically unmet in real applications, the capacity of adapting to any unseen setting becomes of paramount importance. Purposely, we propose a continual adaptation paradigm for deep stereo networks designed to deal with challenging and ever-changing environments. We design a lightweight and modular architecture, Modularly ADaptive Network (MADNet), and formulate Modular ADaptation algorithms (MAD, MAD++) which permit efficient optimization of independent sub-portions of the entire network. In our paradigm, the learning signals needed to continuously adapt models online can be sourced from self-supervision via right-to-left image warping or from traditional stereo algorithms. With both sources, no other data than the input images being gathered at deployment time are needed. Thus, our network architecture and adaptation algorithms realize the first real-time self-adaptive deep stereo system and pave the way for a new paradigm that can facilitate practical deployment of end-to-end architectures for dense disparity regression. 

| [Paper](https://arxiv.org/pdf/2007.05233.pdf) | [Code](https://github.com/CVLAB-Unibo/Real-time-self-adaptive-deep-stereo) | [Video](https://www.youtube.com/watch?v=YnPGbQE2dLQ) |

## BibTex 

```
@article{poggi2020continual,
  title={Continual Adaptation for Deep Stereo},
  author={Poggi, Matteo and Tonioni, Alessio and Tosi, Fabio and Mattoccia, Stefano and Di Stefano, Luigi},
  journal={arXiv preprint arXiv:2007.05233},
  year={2020}
}

```