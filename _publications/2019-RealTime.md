---
title: "Real-time self-adaptive deep stereo"
collection: 'Depth Estimation'
permalink: /publication/realTime
excerpt: 'In this paper we propose a real-time self adaptive deep stereo system.'
date: 2019-06-16
venue: 'Conference on Computer Vision and Pattern Recognition'
paperurl: 'https://arxiv.org/pdf/1810.05424'
citation: 'Tonioni, A., Tosi, F., Poggi, M., Mattoccia, S., & Di Stefano, L. (2019). The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2019'
---

## Abstract

Deep convolutional neural networks trained end-to-end are the undisputed state-of-the-art methods to regress dense disparity maps directly from stereo pairs. However, such methods suffer from notable accuracy drops when exposed to scenarios significantly different from those seen in the training phase (eg real vs synthetic images, indoor vs outdoor, etc). As it is unlikely to be able to gather enough samples to achieve effective training/tuning in any target domain, we propose to perform unsupervised and continuous online adaptation of a deep stereo network in order to preserve its accuracy independently of the sensed environment. However, such a strategy can be extremely demanding regarding computational resources and thus not enabling real-time performance. Therefore, we address this side effect by introducing a new lightweight, yet effective, deep stereo architecture Modularly ADaptive Network (MADNet) and by developing Modular ADaptation (MAD), an algorithm to train independently only sub-portions of our model. By deploying MADNet together with MAD we propose the first ever realtime self-adaptive deep stereo system.

| [Paper](https://arxiv.org/pdf/1810.05424) |
[Code](https://github.com/CVLAB-Unibo/Real-time-self-adaptive-deep-stereo) |
[Video](https://www.youtube.com/watch?v=7SjyzDxmCY4) |

## BibTex 

```
@InProceedings{Tonioni_2019_CVPR,
    author = {Tonioni, Alessio and Tosi, Fabio and Poggi, Matteo and Mattoccia, Stefano and Di Stefano, Luigi},
    title = {Real-time self-adaptive deep stereo},
    booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2019}    
}
```