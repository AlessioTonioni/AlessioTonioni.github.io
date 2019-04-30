---
title: "Unsupervised Adaptation For Deep Stereo"
collection: 'Depth Estimation'
permalink: /publication/Adaptation
excerpt: 'In this paper we propose a novel unsupervised adaptation approach that enables to fine-tune a deep learning stereo model without any ground-truth information.'
date: 2017-10-22
venue: 'Proceedings of the IEEE International Conference on Computer Vision'
paperurl: 'http://openaccess.thecvf.com/content_ICCV_2017/papers/Tonioni_Unsupervised_Adaptation_for_ICCV_2017_paper.pdf'
citation: 'Tonioni, A., Poggi, M., Mattoccia, S., & Di Stefano, L. (2017). Unsupervised adaptation for deep stereo. In Proceedings of the IEEE International Conference on Computer Vision (pp. 1605-1613).'
pubtype: 'conference'
---

## Abstract

Recent ground-breaking works have shown that deep neural networks can be trained end-to-end to regress dense disparity maps directly from image pairs. Computer generated imagery is deployed to gather the large data corpus required to train such networks, an additional fine-tuning allowing to adapt the model to work well also on real and possibly diverse environments. Yet, besides a few public datasets such as Kitti, the ground-truth needed to adapt the network to a new scenario is hardly available in practice. In this paper we propose a novel unsupervised adaptation approach that enables to fine-tune a deep learning stereo model without any ground-truth information. We rely on off-the-shelf stereo algorithms together with state-of-the-art confidence measures, the latter able to ascertain upon correctness of the measurements yielded by former. Thus, we train the network based on a novel loss-function that penalizes predictions disagreeing with the highly confident disparities provided by the algorithm and enforces a smoothness constraint. Experiments on popular datasets (KITTI 2012, KITTI 2015 and Middlebury 2014) and other challenging test images demonstrate the effectiveness of our proposal.

| [Paper](http://openaccess.thecvf.com/content_ICCV_2017/papers/Tonioni_Unsupervised_Adaptation_for_ICCV_2017_paper.pdf) | [Code](https://github.com/CVLAB-Unibo/Unsupervised-Adaptation-for-Deep-Stereo) |

## BibTex
```
@inproceedings{tonioni2017unsupervised,
  title={Unsupervised adaptation for deep stereo},
  author={Tonioni, Alessio and Poggi, Matteo and Mattoccia, Stefano and Di Stefano, Luigi},
  booktitle={Proceedings of the IEEE International Conference on Computer Vision},
  pages={1605--1613},
  year={2017}
}
```