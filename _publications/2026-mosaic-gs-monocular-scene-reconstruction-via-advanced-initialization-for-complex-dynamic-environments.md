---
title: 'MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for
  Complex Dynamic Environments'
authors: Svitlana Morkva, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh
  Patil
collection: publications
permalink: /publication/mosaic-gs-monocular-scene-reconstruction-via-advanced-initialization-for-complex-dynamic-environments
excerpt: We present MOSAIC-GS, a novel, fully explicit, and computationally efficient
  approach for high-fidelity dynamic scene reconstruction from monocular vi...
date: 2026-01-18
venue: ArXiv
paperurl: https://arxiv.org/pdf/2601.05368.pdf
citation: 'Svitlana Morkva, Michael Oechsle, **Alessio Tonioni**, Marco Hutter, Vaishakh
  Patil. "MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for
  Complex Dynamic Environments." ArXiv, 2026.'
pubtype: review
---

## Abstract

We present MOSAIC-GS, a novel, fully explicit, and computationally efficient approach for high-fidelity dynamic scene reconstruction from monocular videos using Gaussian Splatting. Monocular reconstruction is inherently ill-posed due to the lack of sufficient multiview constraints, making accurate recovery of object geometry and temporal coherence particularly challenging. To address this, we leverage multiple geometric cues, such as depth, optical flow, dynamic object segmentation, and point tracking. Combined with rigidity-based motion constraints, these cues allow us to estimate preliminary 3D scene dynamics during an initialization stage. Recovering scene dynamics prior to the photometric optimization reduces reliance on motion inference from visual appearance alone, which is often ambiguous in monocular settings. To enable compact representations, fast training, and real-time rendering while supporting non-rigid deformations, the scene is decomposed into static and dynamic components. Each Gaussian in the dynamic part of the scene is assigned a trajectory represented as time-dependent Poly-Fourier curve for parameter-efficient motion encoding. We demonstrate that MOSAIC-GS achieves substantially faster optimization and rendering compared to existing methods, while maintaining reconstruction quality on par with state-of-the-art approaches across standard monocular dynamic scene benchmarks.

| [Paper](https://arxiv.org/pdf/2601.05368.pdf) |
