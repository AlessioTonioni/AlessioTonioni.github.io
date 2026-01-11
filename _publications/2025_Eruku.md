---
title: "Autoregressive Styled Text Image Generation, but Make it Reliable"
authors: "Carmine Zaccagnino, Fabio Quattrini, Vittorio Pippi, Silvia Cascianelli, Alessio Tonioni, Rita Cucchiara"
collection: "Multimodal Models"
permalink: "/publication/eruku"
excerpt: 'Better autoregressive handwriting generation'
date: 2025-10-27
venue: 'WACV'
paperurl: 'https://arxiv.org/abs/2510.23240'
citation: 'Zaccagnino, C., Quattrini, F., Pippi, V., Cascianelli, S., Tonioni, A., & Cucchiara, R. (2025). Autoregressive Styled Text Image Generation, but Make it Reliable. arXiv preprint arXiv:2510.23240.'
pubtype: 'conference'
---

## Abstract

Generating faithful and readable styled text images (especially for Styled Handwritten Text generation - HTG) is an open problem with several possible applications across graphic design, document understanding, and image editing. A lot of research effort in this task is dedicated to developing strategies that reproduce the stylistic characteristics of a given writer, with promising results in terms of style fidelity and generalization achieved by the recently proposed Autoregressive Transformer paradigm for HTG. However, this method requires additional inputs, lacks a proper stop mechanism, and might end up in repetition loops, generating visual artifacts. In this work, we rethink the autoregressive formulation by framing HTG as a multimodal prompt-conditioned generation task, and tackle the content controllability issues by introducing special textual input tokens for better alignment with the visual ones. Moreover, we devise a Classifier-Free-Guidance-based strategy for our autoregressive model. Through extensive experimental validation, we demonstrate that our approach, dubbed Eruku, compared to previous solutions requires fewer inputs, generalizes better to unseen styles, and follows more faithfully the textual prompt, improving content adherence.

| [Paper](https://arxiv.org/pdf/2510.23240) | [Code](https://huggingface.co/blowing-up-groundhogs/eruku) |  

## BibTex 

```
@article{zaccagnino2025autoregressive,
  title={Autoregressive Styled Text Image Generation, but Make it Reliable},
  author={Zaccagnino, Carmine and Quattrini, Fabio and Pippi, Vittorio and Cascianelli, Silvia and Tonioni, Alessio and Cucchiara, Rita},
  journal={arXiv preprint arXiv:2510.23240},
  year={2025}
}
```