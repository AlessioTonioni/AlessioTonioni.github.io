---
title: "Real-Time Highly Accurate Dense Depth on a Power Budget using an FPGA-CPU Hybrid SoC"
collection: 'Depth Estimation'
permalink: /publication/FPGA
excerpt: 'In this paper, we leverage a FPGA-CPU chip to propose a novel, sophisticated, stereo approach that combines the best features of SGM and ELAS-based methods to compute highly accurate dense depth in real time.'
date: 2019-04-03
venue: ' IEEE Transactions on Circuits and Systems II: Express Briefs '
paperurl: 'https://ieeexplore.ieee.org/document/8681073'
citation: 'O. Rahnama et al., "Real-Time Highly Accurate Dense Depth on a Power Budget using an FPGA-CPU Hybrid SoC," in IEEE Transactions on Circuits and Systems II: Express Briefs.'
---
## Abstract

Obtaining highly accurate depth from stereo images in real time has many applications across computer vision and robotics, but in some contexts, upper bounds on power consumption constrain the feasible hardware to embedded platforms such as FPGAs. Whilst various stereo algorithms have been deployed on these platforms, usually cut down to better match the embedded architecture, certain key parts of the more advanced algorithms, e.g. those that rely on unpredictable access to memory or are highly iterative in nature, are difficult to deploy efficiently on FPGAs, and thus the depth quality that can be achieved is limited. In this paper, we leverage a FPGA-CPU chip to propose a novel, sophisticated, stereo approach that combines the best features of SGM and ELAS-based methods to compute highly accurate dense depth in real time. Our approach achieves an 8.7% error rate on the challenging KITTI 2015 dataset at over 50 FPS, with a power consumption of only 5W.

[Paper](https://ieeexplore.ieee.org/document/8681073)

## BibTex
```
@ARTICLE{8681073,
author={O. {Rahnama} and T. {Cavallari} and S. {Golodetz} and A. {Tonioni} and T. {Joy} and L. {Di Stefano} and S. {Walker} and P. H. S. {Torr}},
journal={IEEE Transactions on Circuits and Systems II: Express Briefs},
title={Real-Time Highly Accurate Dense Depth on a Power Budget using an FPGA-CPU Hybrid SoC},
year={2019},
volume={},
number={},
pages={1-1},
keywords={Field programmable gate arrays;Pipelines;Real-time systems;Optimization;Random access memory;Reliability;Central Processing Unit;Heterogeneous;FPGA;real-time;stereo;depth.},
doi={10.1109/TCSII.2019.2909169},
ISSN={1549-7747},
month={},}

```