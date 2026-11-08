---
layout: post
title: "The big model collapses, sixteen numbers bend"
category: research
publish: True
date: 2026-11-08
---

The big model collapses. Sixteen numbers bend.

ECGFounder, a foundation model pretrained on over 10 million recordings, clusters heart rhythms best on balanced data held in one place. Change those two conditions and it falls to or near chance, while 16 hand-crafted features lose ground and stay well above it.

Our new paper in Biomedical Signal Processing and Control asks which ECG representation lets clustering find arrhythmia groups without labels. We compared raw signals, an autoencoder, the 16 features, ECGFounder and HuBERT-ECG on PTB-XL recordings of sinus rhythm and atrial fibrillation.

The score is the adjusted Rand index (ARI): 0 is chance, 1 is perfect agreement with the true labels. With k-means on balanced data, ECGFounder reaches 0.885 and the 16 features 0.644. At one atrial fibrillation recording in ten, ECGFounder drops to 0.063 and the features to 0.265.

Across ten simulated hospitals with very different atrial fibrillation rates, the averages are close: 0.612 for ECGFounder, 0.591 for the features. Over ten random splits the features never go below 0.455, while ECGFounder lands at 0.132 or lower three times, once at chance. The features also take 15 times less computing time per record.

These are two-class tasks with two foundation models, and the hospitals are simulated from one dataset.

Dongho Chun led this work, and I am proud that it is the first paper with my name in last place.

Free to read until 27 December: https://authors.elsevier.com/a/1o3zB6DBR3L1G2

Code: https://github.com/TheAxeC/ecg-representation-clustering

When you test a model for deployment, do you report its average or its worst case?

#ECG #FoundationModels #Clustering #HealthcareAI
