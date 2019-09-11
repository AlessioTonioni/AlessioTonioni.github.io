---
title: "Unsupervised Domain Adaptation for Depth Prediction from Images"
authors: 'Alessio Tonioni, Matteo Poggi, Stefano Mattoccia and Luigi Di Stefano'
collection: 'Depth Estimation'
permalink: /publication/AdaptationJournal
excerpt: 'In this paper we extend our previous unsupervised adaptation approach to fine-tune a deep learning stereo or mono model without any ground-truth information.'
venue: 'IEEE Transactions on Pattern Analysis and Machine Intelligence'
paperurl: 'https://arxiv.org/abs/1909.03943'
date: 2019-12-31
citation: 'Tonioni, A., Poggi, M., Mattoccia, S., & Di Stefano, L. (2019). Unsupervised Domain Adaptation for Depth Prediction from Images. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2019'
pubtype: 'journal'
---
## Abstract

State-of-the-art approaches to infer dense depth measurements from images rely on CNNs trained end-to-end on a vast amount of data. However, these approaches suffer a drastic drop in accuracy when dealing with environments much different in appearance and/or context from those observed at training time. This domain shift issue is usually addressed by fine-tuning on smaller sets of images from the target domain annotated with depth labels. Unfortunately, relying on such supervised labeling is seldom feasible in most practical settings. 
Therefore, we propose an unsupervised domain adaptation technique which does not require groundtruth labels. Our method relies only on image pairs and leverages on classical stereo algorithms to produce disparity measurements alongside with confidence estimators to assess upon their reliability.
We propose to fine-tune both depth-from-stereo as well as depth-from-mono architectures by a novel confidence-guided loss function that handles the measured disparities as noisy labels weighted according to the estimated confidence.  
Extensive experimental results based on standard datasets and evaluation protocols prove that our technique can address effectively the domain shift issue with both  stereo and monocular depth prediction architectures  and  outperforms  other state-of-the-art unsupervised loss functions that may be alternatively deployed to pursue domain adaptation.

[Paper](https://arxiv.org/abs/1909.03943) 

## BibTex
```
@artcile{tonioni2019unsupervised,
  title={Unsupervised Domain Adaptation for Depth Prediction from Images},
  author={Tonioni, Alessio and Poggi, Matteo and Mattoccia, Stefano and Di Stefano, Luigi},
  booktitle={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2019}
}
```
