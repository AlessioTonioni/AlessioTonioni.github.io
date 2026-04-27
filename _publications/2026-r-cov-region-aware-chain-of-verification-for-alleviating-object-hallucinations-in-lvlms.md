---
title: 'R-CoV: Region-Aware Chain-of-Verification for Alleviating Object Hallucinations in LVLMs'
authors: Jiahao Xie, Alessio Tonioni, Nathalie Rauschmayr, Federico Tombari, Bernt Schiele
collection: publications
permalink: /publication/r-cov-region-aware-chain-of-verification-for-alleviating-object-hallucinations-in-lvlms
excerpt: Large vision-language models (LVLMs) have demonstrated impressive performance in various multimodal understanding and reasoning tasks. However, they s...
date: 2026-04-27
venue: ArXiv
paperurl: https://arxiv.org/pdf/2604.20696.pdf
citation: 'Jiahao Xie, **Alessio Tonioni**, Nathalie Rauschmayr, Federico Tombari, Bernt Schiele. "R-CoV: Region-Aware Chain-of-Verification for Alleviating Object Hallucinations in LVLMs." ArXiv, 2026.'
pubtype: review
---

## Abstract

Large vision-language models (LVLMs) have demonstrated impressive performance in various multimodal understanding and reasoning tasks. However, they still struggle with object hallucinations, i.e., the claim of nonexistent objects in the visual input. To address this challenge, we propose Region-aware Chain-of-Verification (R-CoV), a visual chain-of-verification method to alleviate object hallucinations in LVLMs in a post-hoc manner. Motivated by how humans comprehend intricate visual information -- often focusing on specific image regions or details within a given sample -- we elicit such region-level processing from LVLMs themselves and use it as a chaining cue to detect and alleviate their own object hallucinations. Specifically, our R-CoV consists of six steps: initial response generation, entity extraction, coordinate generation, region description, verification execution, and final response generation. As a simple yet effective method, R-CoV can be seamlessly integrated into various LVLMs in a training-free manner and without relying on external detection models. Extensive experiments on several widely used hallucination benchmarks across multiple LVLMs demonstrate that R-CoV can significantly alleviate object hallucinations in LVLMs. Project page: https://github.com/Jiahao000/R-CoV.

| [Paper](https://arxiv.org/pdf/2604.20696.pdf) |
