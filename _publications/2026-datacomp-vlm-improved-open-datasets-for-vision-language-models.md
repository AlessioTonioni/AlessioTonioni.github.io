---
title: 'DataComp-VLM: Improved Open Datasets for Vision-Language Models'
authors: "Matteo Farina, Vishaal Udandarao, Thao Nguyen, Selim Kuzucu, Maximilian B\xF6ther, Andreas Hochlehnert, Adhiraj Ghosh, Marianna Nezhurina, Karsten Roth, Joschka Struber, Yuhui Zhang, Sebastian Dziadzio, Elaine Sui, Soumya Jahagirdar, Dhruba Ghosh, Hasan Hammoud, Thomas De Min, Simone Caldarella, Jehanzeb Mirza, Sedrick Keh, Mehdi Cherti, Hilde Kuehne, Bernt Schiele, Serena Yeung-Levy, Muhammad Ferjad Naeem, Federico Tombari, Ana Klimovic, Elisa Ricci, Matthias Bethge, Sewoong Oh, Ameya Prabhu, Alessio Tonioni, Jenia Jitsev, Massimiliano Mancini, Ludwig Schmidt, Nikhil Parthasarathy"
collection: publications
permalink: /publication/datacomp-vlm-improved-open-datasets-for-vision-language-models
excerpt: Building performant Vision-Language Models (VLMs) requires carefully curating large-scale training datasets, yet the community lacks systematic benchm...
date: 2026-07-05
venue: ArXiv
paperurl: https://arxiv.org/pdf/2606.28551.pdf
citation: "Matteo Farina, Vishaal Udandarao, Thao Nguyen, Selim Kuzucu, Maximilian B\xF6ther, Andreas Hochlehnert, Adhiraj Ghosh, Marianna Nezhurina, Karsten Roth, Joschka Struber, Yuhui Zhang, Sebastian Dziadzio, Elaine Sui, Soumya Jahagirdar, Dhruba Ghosh, Hasan Hammoud, Thomas De Min, Simone Caldarella, Jehanzeb Mirza, Sedrick Keh, Mehdi Cherti, Hilde Kuehne, Bernt Schiele, Serena Yeung-Levy, Muhammad Ferjad Naeem, Federico Tombari, Ana Klimovic, Elisa Ricci, Matthias Bethge, Sewoong Oh, Ameya Prabhu, **Alessio Tonioni**, Jenia Jitsev, Massimiliano Mancini, Ludwig Schmidt, Nikhil Parthasarathy. \"DataComp-VLM: Improved Open Datasets for Vision-Language Models.\" ArXiv, 2026."
pubtype: review
---

## Abstract

Building performant Vision-Language Models (VLMs) requires carefully curating large-scale training datasets, yet the community lacks systematic benchmarks for evaluating such curation strategies. We introduce DataComp for VLMs (DCVLM), a benchmark for controlled data-centric experiments to improve VLM training. As part of DCVLM, we collect 160 datasets spanning four data types -- image-caption pairs, multimodal interleaved documents, text-only, and instruction-tuning data -- into a corpus of 6T multimodal tokens. DCVLM allows participants to test curation strategies (filtering, mixing, formatting, sampling) across 1B-8B models and 6.25B-200B token budgets. Models are then evaluated on a carefully selected suite of up to 52 downstream benchmarks across 9 domains. We conduct extensive experiments on DCVLM and find that data mixing, not filtering, is key to a high-quality training dataset: instruction-heavy mixtures scale better than caption-heavy ones, with gains widening at larger scales. The resulting dataset, DCVLM-Baseline, enables training an 8B VLM to 63.6% accuracy on our 33-task core suite with 200B training tokens. Compared to FineVision, the state-of-the-art open VLM training dataset, this represents an improvement of +5.4pp. DCVLM and all accompanying artifacts will be made publicly available at https://www.datacomp.ai/dcvlm/.

| [Paper](https://arxiv.org/pdf/2606.28551.pdf) |
