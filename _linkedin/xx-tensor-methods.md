---
layout: post
title: "Why Tensor Methods Matter (and Why Nobody Talks About Them)"
picture: /assets/images/projects/conference.webp
category: research
publish: True
date: 2025-02-12
---

Quick question: when you record brain activity, you get a 3D structure—electrodes × time × frequency.

So why do most researchers flatten it into a 2D matrix (or worse, a 1D vector) before analyzing it?

Answer: Because that's what the standard machine learning tools expect.

But here's the problem: you just threw away the multilinear structure of your data.

Let me explain why this matters, why almost nobody talks about it, and why tensor methods might be the most underappreciated tool in biomedical machine learning.

What's a tensor? (Non-scary version)

A tensor is just a multi-dimensional array:

1D array = vector (e.g., one patient's age, weight, height)
2D array = matrix (e.g., multiple patients × multiple features)
3D array = tensor (e.g., patients × features × time)
And so on...
Brain signals are naturally tensors: electrodes × time × trials. Or electrodes × time × frequency. Or subjects × electrodes × time. You get the idea.

Medical imaging? Tensors. Longitudinal health records? Tensors. Genomic data across tissues and conditions? You guessed it—tensors.

Why flattening is a problem

Imagine you have ECoG recordings: 64 electrodes, 1000 time points, 5 frequency bands.

Standard approach: flatten it to a 320,000-element vector, feed it to a neural network or SVM.

What you just lost:

The spatial relationship between electrodes
The temporal dynamics within each electrode
The frequency-specific patterns
The interactions between these dimensions
It's like taking a color photograph, converting it to text pixel-by-pixel, and then trying to recognize faces. You can do it, but you're making it way harder than it needs to be.

Enter: Block-Term Tensor Regression (BTTR)

This is the method I've been developing and refining since my PhD. Here's the idea:

Instead of flattening your 3D brain activity into a vector, keep it as a tensor. Then, decompose it into a small number of "blocks"—each capturing a different pattern in the data.

Think of it like finding the key themes in your data while preserving how those themes play out across electrodes, time, and frequency simultaneously.

The math is based on Tucker decomposition, but we do it recursively (deflation-based) to find one component at a time. This makes it:

Computationally efficient (trains in minutes, not hours)
Interpretable (each block corresponds to a neural pattern)
Accurate (consistently beats matrix-based methods in our benchmarks)
Real results:

Finger movement decoding from ECoG:

BTTR: 0.82 correlation with true finger trajectories
Standard regression: 0.72 correlation
Deep learning baseline: 0.75 correlation
Federated learning for heart disease prediction:

Federated BTTR (FBTTR): 0.872 AUC-ROC
Centralized standard model: 0.812 AUC-ROC
Standard federated learning: ~0.84 AUC-ROC
Sign language alphabet decoding:

Go-BTTR (graph-optimized version): 0.82 correlation for complex gestures
Previous methods: 0.72 for simpler tasks
Arrhythmia detection (Dries Cornelissen's thesis, under review):

BTTR on sinus rhythms: predicts arrhythmia onset before standard ECG markers
So why doesn't everyone use tensor methods?

1. Unfamiliarity Most ML courses teach matrices. CNNs handle images (2D-ish). Transformers work on sequences (1D-ish). Tensor algebra is niche.

2. Perceived complexity The math looks scary. Tucker decomposition, CP decomposition, tensor trains—it sounds like you need a PhD in applied mathematics. (Spoiler: you don't. The concepts are intuitive once you see them.)

3. Lack of accessible tools Scikit-learn doesn't have it. PyTorch tensors are not the same as tensor decomposition. Until recently, you had to implement it yourself or use academic code with terrible documentation.

(That's why I open-sourced BTTR. To fix this.)

4. "Good enough" syndrome Standard methods work okay. Why bother learning something new?

When should you use tensor methods?

Use tensors when:

Your data has clear multi-way structure (space × time, patients × visits × biomarkers, etc.)
You care about interpretability (tensor components often correspond to real patterns)
You have limited data (tensor methods are sample-efficient because they exploit structure)
You need computational efficiency (BTTR trains faster than most deep learning approaches)
Stick with standard methods when:

Your data is genuinely flat (single time point, single measurement per patient)
You have massive datasets and don't care about interpretability (deep learning can brute-force patterns)
You're doing a quick proof-of-concept and don't want to learn new tools
Where tensor methods are heading:

Federated tensor regression (my current focus): Bringing BTTR to multi-institutional healthcare data while preserving privacy. We've shown it works for brain-computer interfaces and clinical prediction. Next: longitudinal imaging for cancer detection.

Tensor methods + foundation models: Can we combine the interpretability of tensor decomposition with the representation learning of transformers? My new postdoc at University of Twente will explore this for multi-modal cancer detection.

Tensor methods for real-world evidence: Healthcare data is messy, heterogeneous, and multi-dimensional. Tensor methods handle this naturally. I'm working with the FAIR program to deploy this at scale.

The bottom line:

If you're working with multi-dimensional biomedical data and you're flattening it before analysis, you're probably losing information.

Tensor methods preserve the structure that matters. They're not magic, and they're not always the answer. But they're underutilized, misunderstood, and deserve more attention.

Want to try BTTR? It's open-source on GitHub: https://github.com/TheAxeC/block-term-tensor-regression

Want to learn more? My papers on BTTR are linked in the comments. Start with the IEEE TNNLS paper—it's the most accessible.

Questions? Drop them below. I love talking about this stuff (clearly).

#MachineLearning #TensorDecomposition #BiomedicalAI #BrainComputerInterface #DataScience #MethodsMatters

