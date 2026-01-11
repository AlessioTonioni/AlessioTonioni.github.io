---
title: "Training-free Online Video Step Grounding"
authors: "Luca Zanella, Massimiliano Mancini, Yiming Wang, Alessio Tonioni, Elisa Ricci"
collection: "Multimodal Models"
permalink: "/publication/baglm"
excerpt: 'Online video step grounding'
date: 2025-10-19
venue: 'Neurips'
paperurl: 'https://arxiv.org/abs/2510.16989'
citation: 'Zanella, L., Mancini, M., Wang, Y., Tonioni, A., & Ricci, E. (2025). Training-free Online Video Step Grounding. arXiv preprint arXiv:2510.16989.'
pubtype: 'conference'
---

## Abstract

Given a task and a set of steps composing it, Video Step Grounding (VSG) aims to detect which steps are performed in a video. Standard approaches for this task require a labeled training set (e.g., with step-level annotations or narrations), which may be costly to collect. Moreover, they process the full video offline, limiting their applications for scenarios requiring online decisions. Thus, in this work, we explore how to perform VSG online and without training. We achieve this by exploiting the zero-shot capabilities of recent Large Multimodal Models (LMMs). In particular, we use LMMs to predict the step associated with a restricted set of frames, without access to the whole video. We show that this online strategy without task-specific tuning outperforms offline and training-based models. Motivated by this finding, we develop Bayesian Grounding with Large Multimodal Models (BaGLM), further injecting knowledge of past frames into the LMM-based predictions. BaGLM exploits Bayesian filtering principles, modeling step transitions via (i) a dependency matrix extracted through large language models and (ii) an estimation of step progress. Experiments on three datasets show superior performance of BaGLM over state-of-the-art training-based offline methods.

| [Paper](https://arxiv.org/pdf/2510.16989) | [Project Page](https://lucazanella.github.io/baglm/) |  

## BibTex 

```
@article{zanella2025training,
  title={Training-free Online Video Step Grounding},
  author={Zanella, Luca and Mancini, Massimiliano and Wang, Yiming and Tonioni, Alessio and Ricci, Elisa},
  journal={arXiv preprint arXiv:2510.16989},
  year={2025}
}
```