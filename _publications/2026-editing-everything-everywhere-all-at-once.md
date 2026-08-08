---
title: Editing Everything Everywhere All at Once
authors: "Fabio Quattrini, Carmine Zaccagnino, Enis Simsar, Marta Tintor\xE9 Gazulla, Rita Cucchiara, Alessio Tonioni, Silvia Cascianelli"
collection: publications
permalink: /publication/editing-everything-everywhere-all-at-once
excerpt: Editing multiple elements of an image in a single forward pass is a practical alternative to multi-turn image manipulation, offering improved efficien...
date: 2026-07-05
venue: 'ECCV'
paperurl: https://arxiv.org/pdf/2606.31278.pdf
citation: "Fabio Quattrini, Carmine Zaccagnino, Enis Simsar, Marta Tintor\xE9 Gazulla, Rita Cucchiara, **Alessio Tonioni**, Silvia Cascianelli. \"Editing Everything Everywhere All at Once.\" ArXiv, 2026."
pubtype: 'conference'
---

## Abstract

Editing multiple elements of an image in a single forward pass is a practical alternative to multi-turn image manipulation, offering improved efficiency and potentially better harmonization. However, when several instructions target different regions, semantic interference often leads to attribute leakage and poor edit disentanglement, especially as the number of edits increases. In this work, we propose MICE (Multi-Instance Concurrent Editing), a training-free strategy for scalable multi-instance image editing with Multimodal Diffusion Transformers. MICE modifies the additive bias of joint attention to regulate interactions between instance-specific edit instructions, latent, and context tokens identified via user-provided segmentation masks. Specifically, MICE allows intra-instance attention, penalizes interactions between neighboring region tokens, and suppresses unrelated cross-instance attention. As a result, our method enforces attribute binding while preserving global visual consistency. We evaluate MICE on LoMOE-Bench and introduce MICE-Bench, a more challenging benchmark with an average of 8.5 concurrent edits per image. The experiments demonstrate that our approach outperforms strong baselines and recent competitors in terms of visual quality preservation and faithfulness to the editing instructions.

| [Paper](https://arxiv.org/pdf/2606.31278.pdf) |
