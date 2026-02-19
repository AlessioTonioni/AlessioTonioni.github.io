---
title: Shifting the Breaking Point of Flow Matching for Multi-Instance Editing
authors: "Carmine Zaccagnino, Fabio Quattrini, Enis Simsar, Marta Tintor\xE9 Gazulla, Rita Cucchiara, Alessio Tonioni, Silvia Cascianelli"
collection: publications
permalink: /publication/shifting-the-breaking-point-of-flow-matching-for-multi-instance-editing
excerpt: Flow matching models have recently emerged as an efficient alternative to diffusion, especially for text-guided image generation and editing, offering...
date: 2026-02-19
venue: ArXiv
paperurl: https://arxiv.org/pdf/2602.08749.pdf
citation: "Carmine Zaccagnino, Fabio Quattrini, Enis Simsar, Marta Tintor\xE9 Gazulla, Rita Cucchiara, **Alessio Tonioni**, Silvia Cascianelli. \"Shifting the Breaking Point of Flow Matching for Multi-Instance Editing.\" ArXiv, 2026."
pubtype: review
---

## Abstract

Flow matching models have recently emerged as an efficient alternative to diffusion, especially for text-guided image generation and editing, offering faster inference through continuous-time dynamics. However, existing flow-based editors predominantly support global or single-instruction edits and struggle with multi-instance scenarios, where multiple parts of a reference input must be edited independently without semantic interference. We identify this limitation as a consequence of globally conditioned velocity fields and joint attention mechanisms, which entangle concurrent edits. To address this issue, we introduce Instance-Disentangled Attention, a mechanism that partitions joint attention operations, enforcing binding between instance-specific textual instructions and spatial regions during velocity field estimation. We evaluate our approach on both natural image editing and a newly introduced benchmark of text-dense infographics with region-level editing instructions. Experimental results demonstrate that our approach promotes edit disentanglement and locality while preserving global output coherence, enabling single-pass, instance-level editing.

| [Paper](https://arxiv.org/pdf/2602.08749.pdf) |
