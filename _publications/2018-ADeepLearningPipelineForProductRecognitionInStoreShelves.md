---
title: "A deep learning pipeline for product recognition in store shelves"
collection: 'Product Detection and Recognition'
permalink: /publication/deepProduct
excerpt: 'In this paper, we propose a deep learning pipeline to recognize products on grocery shelves that can scale effortlessly to thousand of different products to recognize.'
date: 2018-12-12
venue: 'International Conference on Image Processing, Applications and Systems'
paperurl: 'https://arxiv.org/pdf/1810.01733'
citation: 'Tonioni, Alessio, Eugenio Serra, and Luigi Di Stefano. "A deep learning pipeline for product recognition in store shelves." In International Conference on Image Processing, Applications and Systems, 2018'
pubtype: 'conference'
---

## Abstract

Recognition of grocery products in store shelves poses peculiar challenges. Firstly, the task mandates the recognition of an extremely high number of different items, in the order of several thousands for medium-small shops, with many of them featuring small inter and intra class variability. Then, available product databases usually include just one or a few studio-quality images per product (refereed to here as reference images), whilst at test time recognition is performed on pictures displaying a portion of a shelf containing several products and taken in the store by cheap cameras (refereed to as query images). Moreover, as the items on sale in a store as well as their appearance change frequently overtime, a practical recognition system should handle seamlessly new products/packages. Inspired by recent advances in object detection and image retrieval, we propose to leverage on state of the art object detectors based on deep learning to obtain an initial product-agnostic item detection. Then, we pursue product recognition through similarity search between global descriptors computed on reference and cropped query images. To maximize performance, we learn an ad-hoc global descriptor by a CNN trained on reference images based on an image embedding loss. Our system is computationally expensive at training time, but can perform recognition rapidly and accurately at test time.

| [Paper](https://arxiv.org/pdf/1810.01733) | [Dataset](https://drive.google.com/open?id=1vvB1hvKhr4pE8zUpPImlogA6kof-kLVN) |

## BibTex
```
@inproceedings{tonioni2019product,
  title={A deep learning pipeline for fine-grained products recognition on store shelves},
  author={Tonioni, Alessio and Serra, Eugenio and Di Stefano, Luigi},
  booktitle={International Conference on Image Processing, Applications and Systems},
  year={2018}
}
```