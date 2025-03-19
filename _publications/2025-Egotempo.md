---
title: "Omnia de EgoTempo: Benchmarking Temporal Understanding of Multi-Modal LLMs in Egocentric Videos"
authors: "Chiara Plizzari, Alessio Tonioni, Yongqin Xian, Achin Kulshrestha, Federico Tombari"
collection: "Multimodal Models"
permalink: "/publication/egotempo"
excerpt: 'New Egocentric video benchmark'
date: 2025-03-19
venue: 'CVPR'
paperurl: 'https://arxiv.org/abs/2503.13646'
citation: 'Plizzari, Chiara, et al. "Omnia de EgoTempo: Benchmarking Temporal Understanding of Multi-Modal LLMs in Egocentric Videos." CVPR (2025).'
pubtype: 'conference'
---

## Abstract

Understanding fine-grained temporal dynamics is crucial in egocentric videos, where continuous streams capture frequent, close-up interactions with objects. In this work, we bring to light that current egocentric video question-answering datasets often include questions that can be answered using only few frames or commonsense reasoning, without being necessarily grounded in the actual video. Our analysis shows that state-of-the-art Multi-Modal Large Language Models (MLLMs) on these benchmarks achieve remarkably high performance using just text or a single frame as input. To address these limitations, we introduce EgoTempo, a dataset specifically designed to evaluate temporal understanding in the egocentric domain. EgoTempo emphasizes tasks that require integrating information across the entire video, ensuring that models would need to rely on temporal patterns rather than static cues or pre-existing knowledge. Extensive experiments on EgoTempo show that current MLLMs still fall short in temporal reasoning on egocentric videos, and thus we hope EgoTempo will catalyze new research in the field and inspire models that better capture the complexity of temporal dynamics.

| [Paper](https://arxiv.org/pdf/2503.13646) | [Dataset](https://github.com/google-research-datasets/egotempo) |  

## BibTex 

```
@inproceedings{plizzari2025egptempo,
      title={Omnia de EgoTempo: Benchmarking Temporal Understanding of Multi-Modal LLMs in Egocentric Videos}, 
      author={Chiara Plizzari, Alessio Tonioni, Yongqin Xian, Ace Kulshrestha, Federico Tombari},
      booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
      year={2025},
}
```
