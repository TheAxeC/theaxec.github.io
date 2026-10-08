---
layout: post
title: "Federate what transfers: component-aware federation at FLTA 2026"
category: research
publish: True
date: 2026-10-08
---

🎤 I will present our paper on federated learning for longitudinal 3D MRI at IEEE FLTA 2026 in Paris (27-30 October). The idea: federate only the part of the model that transfers.

The setting is liver cancer (HCC) surveillance in cirrhosis. Each hospital has few patients and few positives, and cannot share scans.

In our earlier model, HCCNet, most of the predictive gain comes from self-supervised pre-training of the convolutional backbone, which needs no labels. The temporal Transformer on top depends on how often a hospital screens its patients.

So component-aware federation (CAF) federates only the label-free backbone pre-training. The temporal Transformer stays at each hospital, and every label stays local. In the figure, blue is shared and orange stays local.

We split one cirrhosis cohort into five simulated hospitals. CAF reaches an AUPRC (a score that suits rare positives) of 0.713, against 0.677 for the best federated baseline and 0.744 for centralised training on pooled data. Each hospital uploads 55.2 MB per round instead of 88.0 MB.

It also holds up when some hospitals have no positive cases at all, because those hospitals still strengthen the shared backbone.

The hospitals are simulated from one cohort, so this shows the design rule works under controlled differences between hospitals. Real cross-hospital data is the test it has not yet had.

With Maureen Guichelaar, Donald Bouman, Stéphanie van den Berg and Maryam Amir Haeri.

If you federate a model, how do you decide which parts to share?

#FederatedLearning #MedicalImaging #HealthcareAI #HCC
