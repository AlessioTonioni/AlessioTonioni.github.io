---
title: "BRAVE: Broadening the visual encoding of vision-language models"
authors: "Oğuzhan Fatih Kar, Alessio Tonioni, Petra Poklukar, Achin Kulshrestha, Amir Zamir, Federico Tombari"
collection: "Multimodal Models"
permalink: "/publication/Brave"
excerpt: 'Ensembling for LMM'
date: 2024-04-10
venue: 'Arxive'
paperurl: 'https://arxiv.org/pdf/2404.07204'
citation: 'Kar, Oğuzhan Fatih, et al. "BRAVE: Broadening the visual encoding of vision-language models." arXiv preprint arXiv:2404.07204 (2024).'
pubtype: 'conference'
---

## Abstract

Vision-language models (VLMs) are typically composed of a vision encoder, e.g. CLIP, and a language model (LM) that interprets the encoded features to solve downstream tasks. Despite remarkable progress, VLMs are subject to several shortcomings due to the limited capabilities of vision encoders, e.g. "blindness" to certain image features, visual hallucination, etc. To address these issues, we study broadening the visual encoding capabilities of VLMs. We first comprehensively benchmark several vision encoders with different inductive biases for solving VLM tasks. We observe that there is no single encoding configuration that consistently achieves top performance across different tasks, and encoders with different biases can perform surprisingly similarly. Motivated by this, we introduce a method, named BRAVE, that consolidates features from multiple frozen encoders into a more versatile representation that can be directly fed as the input to a frozen LM. BRAVE achieves state-of-the-art performance on a broad range of captioning and VQA benchmarks and significantly reduces the aforementioned issues of VLMs, while requiring a smaller number of trainable parameters than existing methods and having a more compressed representation. Our results highlight the potential of incorporating different visual biases for a more broad and contextualized visual understanding of VLMs.

| [Paper](https://arxiv.org/pdf/2404.07204) | [Project Page](https://brave-vlms.epfl.ch/) |

## BibTex 

```
@article{kar2024brave,
  title={BRAVE: Broadening the visual encoding of vision-language models},
  author={Kar, O{\u{g}}uzhan Fatih and Tonioni, Alessio and Poklukar, Petra and Kulshrestha, Achin and Zamir, Amir and Tombari, Federico},
  journal={arXiv preprint arXiv:2404.07204},
  year={2024}
}
```
