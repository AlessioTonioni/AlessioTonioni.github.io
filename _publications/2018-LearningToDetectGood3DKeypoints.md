---
title: "Learning to detect good 3D keypoints"
collection: "3D Computer Vision"
permalink: /publication/kpl
excerpt: 'In this paper we learn a descriptor-specific 3D keypoint detector so as to optimize the end-to-end performance of a feature matching pipeline'
date: 2018-01-01
venue: 'International Journal of Computer Vision'
paperurl: 'https://link.springer.com/epdf/10.1007/s11263-017-1037-3?author_access_token=A6mZlEoOjxZGyCHCohv2S_e4RwlQNchNByi7wbcMAY6YMRbUoetNXq7aaaAeIQvsChPHezwOevTcWH93kQ_Yjjv2XMTn9nAxPBQNdENkj7GMNBAtgtyEM5XnOFDXn4M5rzzUKa_cxrklnPH7XFDXQg%3D%3D'
citation: 'Tonioni, A., Salti, S., Tombari, F., Spezialetti, R., & Di Stefano, L. (2018). Learning to detect good 3D keypoints. International Journal of Computer Vision, 126(1), 1-20.'
pubtype: 'journal'
---
## Abstract
The established approach to 3D keypoint detection consists in defining effective handcrafted saliency functions based on geometric cues with the aim of maximizing keypoint repeatability. Differently, the idea behind our work is to learn a descriptor-specific keypoint detector so as to optimize the end-to-end performance of the feature matching pipeline. Accordingly, we cast 3D keypoint detection as a classification problem between surface patches that can or cannot be matched correctly by a given 3D descriptor, i.e. those either good or not in respect to that descriptor. We propose a machine learning framework that allows for defining examples of good surface patches from the training data and leverages Random Forest classifiers to realize both fixed-scale and adaptive-scale 3D keypoint detectors. Through extensive experiments on standard datasets, we show how feature matching performance improves significantly by deploying 3D descriptors together with companion detectors learned by our methodology with respect to the adoption of established state-of-the-art 3D detectors based on hand-crafted saliency functions.

| [Paper](https://link.springer.com/epdf/10.1007/s11263-017-1037-3?author_access_token=A6mZlEoOjxZGyCHCohv2S_e4RwlQNchNByi7wbcMAY6YMRbUoetNXq7aaaAeIQvsChPHezwOevTcWH93kQ_Yjjv2XMTn9nAxPBQNdENkj7GMNBAtgtyEM5XnOFDXn4M5rzzUKa_cxrklnPH7XFDXQg%3D%3D) | [Code](https://github.com/CVLAB-Unibo/Keypoint-Learning) |

## BibTex
```
@article{tonioni2018learning,
  title={Learning to detect good 3D keypoints},
  author={Tonioni, Alessio and Salti, Samuele and Tombari, Federico and Spezialetti, Riccardo and Di Stefano, Luigi},
  journal={International Journal of Computer Vision},
  volume={126},
  number={1},
  pages={1--20},
  year={2018},
  publisher={Springer}
}
```