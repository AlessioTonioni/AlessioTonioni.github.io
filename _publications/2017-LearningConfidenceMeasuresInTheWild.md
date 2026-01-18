---
title: "Learning confidence measures in the wild"
authors: 'Fabio Tosi, Matteo Poggi, Alessio Tonioni, Luigi Di Stefano, & Stefano Mattoccia'
collection: 'Depth Estimation'
permalink: /publication/confidenceWild
excerpt: 'In this paper we propose a methodology suited for training a confidence measure for stereo in a self-supervised manner.'
date: 2017-09-04
venue: 'BMVC'
paperurl: 'https://www.bmva-archive.org.uk/bmvc/2017/papers/paper133/paper133.pdf'
citation: 'Tosi, F., Poggi, M., Tonioni, A., Di Stefano, L., & Mattoccia, S. (2017, September). Learning confidence measures in the wild. In 28th British Machine Vision Conference (BMVC 2017) (Vol. 2, No. 4).'
pubtype: 'conference'
---

## Abstract 

Confidence measures for stereo earned increasing popularity in most recent works concerning stereo, being effectively deployed to improve its accuracy. While most measures are obtained by processing cues from the cost volume, top-performing ones usually leverage on random-forests or CNNs to predict match reliability. Therefore, a proper amount of labeled data is required to effectively train such confidence measures. Being such ground-truth labels not always available in practical applications, in this paper we propose a methodology suited for training confidence measures in a self-supervised manner. Leveraging on a pool of properly selected conventional measures, we automatically detect a subset of very reliable pixels as well as a subset of erroneous samples from the output of a stereo algorithm. This strategy provides labels for training confidence measures based on machine-learning technique without ground-truth labels. Compared to state-of-the-art, our method is neither constrained to image sequences nor to image content. Experimental results on three challenging datasets with three stereo algorithms and three state-of-the-art confidence measures based on machine-learning techniques confirm the effectiveness of our proposal for self-supervised training.

| [Paper](https://www.bmva-archive.org.uk/bmvc/2017/papers/paper133/paper133.pdf) | [Code](https://github.com/fabiotosi92/Unsupervised-Confidence-Measures) | 

## BibTex 
```
@inproceedings{tosi2017learning,
  title={Learning confidence measures in the wild},
  author={Tosi, Fabio and Poggi, Matteo and Tonioni, Alessio and Di Stefano, Luigi and Mattoccia, Stefano},
  booktitle={28th British Machine Vision Conference (BMVC 2017)},
  volume={2},
  number={4},
  year={2017}
}

```]