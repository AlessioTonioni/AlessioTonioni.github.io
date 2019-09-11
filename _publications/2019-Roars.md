---
title: "Semi-Automatic Labeling for Deep Learning in Robotics"
authors: 'Daniele De Gregorio, Alessio Tonioni, Gianluca Palli and Luigi Di Stefano'
collection: 'Robotics'
permalink: /publication/ARS
excerpt: 'In this paper, we propose Augmented Reality Semi-automatic labeling (ARS), a semi-automatic method to create large labeled datasets with minimal human intervention'
date: 2019-08-11
venue: ' IEEE Transactions on Automation Science and Engineering  '
paperurl: 'https://arxiv.org/abs/1908.01862'
citation: 'Daniele De Gregorio, Alessio Tonioni, Gianluca Palli and Luigi Di Stefano, "Semi-Automatic Labeling for Deep Learning in Robotics," in IEEE Transactions on Automation Science and Engineering.'
pubtype: 'journal'
---
## Abstract
In this paper, we propose Augmented Reality Semi-automatic labeling (ARS), a semi-automatic method which leverages on moving a 2D camera by means of a robot, proving precise camera tracking, and an augmented reality pen to define initial object bounding box, to create large labeled datasets with minimal human intervention. By removing the burden of generating annotated data from humans, we make the Deep Learning technique applied to computer vision, that typically requires very large datasets, truly automated and reliable. With the ARS pipeline, we created effortlessly two novel datasets, one on electromechanical components (industrial scenario) and one on fruits (daily-living scenario), and trained robustly two state-of-the-art object detectors, based on convolutional neural networks, such as YOLO and SSD. With respect to the conventional manual annotation of 1000 frames that takes us slightly more than 10 hours, the proposed approach based on ARS allows annotating 9 sequences of about 35000 frames in less than one hour, with a gain factor of about 450. Moreover, both the precision and recall of object detection is increased by about 15\% with respect to manual labeling. All our software is available as a ROS package in a public repository alongside the novel annotated datasets.

[Paper](https://arxiv.org/abs/1908.01862) 
```
@article{de2019semi,
  title={Semi-Automatic Labeling for Deep Learning in Robotics},
  author={De Gregorio, Daniele and Tonioni, Alessio and Palli, Gianluca and Di Stefano, Luigi},
  journal={IEEE Transactions on Automation Science and Engineering},
  year={2019}
}


```
