---
title: 'RefAM: Attention Magnets for Zero-Shot Referral Segmentation'
authors: Anna Kukleva, Enis Simsar, Alessio Tonioni, Muhammad Ferjad Naeem, Federico Tombari, Jan Eric Lenssen, Bernt Schiele
collection: publications
permalink: /publication/refam-attention-magnets-for-zero-shot-referral-segmentation
excerpt: Most existing approaches to referring segmentation achieve strong performance only through fine-tuning or by composing multiple pre-trained models, of...
date: 2026-01-18
venue: ArXiv
paperurl: https://arxiv.org/pdf/2509.22650.pdf
citation: 'Anna Kukleva, Enis Simsar, **Alessio Tonioni**, Muhammad Ferjad Naeem, Federico Tombari, Jan Eric Lenssen, Bernt Schiele. "RefAM: Attention Magnets for Zero-Shot Referral Segmentation." ArXiv, 2025.'
pubtype: review
---

## Abstract

Most existing approaches to referring segmentation achieve strong performance only through fine-tuning or by composing multiple pre-trained models, often at the cost of additional training and architectural modifications. Meanwhile, large-scale generative diffusion models encode rich semantic information, making them attractive as general-purpose feature extractors. In this work, we introduce a new method that directly exploits features, attention scores, from diffusion transformers for downstream tasks, requiring neither architectural modifications nor additional training. To systematically evaluate these features, we extend benchmarks with vision-language grounding tasks spanning both images and videos. Our key insight is that stop words act as attention magnets: they accumulate surplus attention and can be filtered to reduce noise. Moreover, we identify global attention sinks (GAS) emerging in deeper layers and show that they can be safely suppressed or redirected onto auxiliary tokens, leading to sharper and more accurate grounding maps. We further propose an attention redistribution strategy, where appended stop words partition background activations into smaller clusters, yielding sharper and more localized heatmaps. Building on these findings, we develop RefAM, a simple training-free grounding framework that combines cross-attention maps, GAS handling, and redistribution. Across zero-shot referring image and video segmentation benchmarks, our approach consistently outperforms prior methods, establishing a new state of the art without fine-tuning or additional components.

| [Paper](https://arxiv.org/pdf/2509.22650.pdf) |
