---
layout: cards
title: Research
navbar_name: Research
permalink: /research
description: "Research statement of Dr. Axel Faes - self-explaining, interpretable AI and privacy-preserving federated learning that travels between hospitals, for precision oncology and trustworthy clinical decision support."
keywords: "Axel Faes research, self-explaining AI, interpretable machine learning, federated learning, block-term tensor regression, precision oncology, hepatocellular carcinoma, trustworthy clinical AI, healthcare"
---

# Research

I build clinical AI with two properties most systems lack: it can **explain its own reasoning** to the clinician using it, and it can be **trained across hospitals without any of them giving up their data**. I think of the goal as **the self-explaining hospital**, care supported by models that are interpretable by design and that travel between institutions instead of forcing the data to travel to them. Three lines of work converge on it: **interpretable, self-explaining models**, **federated learning across real institutions**, and **multi-modal precision oncology**. What ties them together is a methodological signature: **multiway (block-term tensor) models whose structure *is* the explanation**, rather than something reconstructed after the fact.

<!-- card -->

## Research themes

### 1. Interpretable, self-explaining models

Clinical machine learning is full of models that are accurate and unaccountable, they return a number, not a reason. I design models that are interpretable *by construction*. My **block-term tensor networks** decompose a signal into components that line up with structure a clinician already reasons about, regions, rhythms, time windows, modalities, so the explanation is read directly off the model rather than approximated afterwards by a separate tool. The aim is to make interpretability a **first-class design objective and a guarantee**, not a disclaimer bolted on at the end. This matters most exactly where AI is hardest to trust: high-stakes, low-data clinical decisions, where a plausible-but-wrong answer is worse than no answer at all.

### 2. Federated learning that travels between institutions

The most informative clinical data is fragmented across hospitals and walled off by privacy law, which is precisely why so much of it stays unused. I build **federated learning** methods that let institutions train shared models **without raw data ever leaving their walls**, including the hard, realistic case where different sites hold **different modalities and incomplete records**. As Technical Machine Learning Lead and Scientific Coordinator of the **Flanders AI Research Program's Real-World Evidence use case** at UHasselt, I built these systems across multiple institutions for cardiovascular risk prediction and population health management. Federation is what turns locked, scattered data into something a model can learn from in the first place.

### 3. Multi-modal precision oncology

Within the **AI-HCC (ZonMw)** project at the University of Twente and Medisch Spectrum Twente, I develop models that integrate **longitudinal MRI, multi-omics, and clinical variables** for the early detection and risk stratification of hepatocellular carcinoma. The signal is spread across imaging, molecular, and clinical timelines that are each noisy and rarely aligned, so I work on **self-supervised backbones for longitudinal medical imaging** that learn from unlabelled scans, and on architectures that model these timelines jointly. This is where the other two threads meet: a model that flags rising cancer risk has to **say why**, and has to learn from cohorts **no single hospital holds on its own**.

### Where the methods came from

The spine of this programme was forged in **neural decoding**. During my PhD and early postdoctoral work I decoded finger movements and sign-language gestures from high-density intracranial (ECoG) recordings, and to capture the spatiotemporal structure of neural signals I developed **block-term tensor regression**. Those methods, multiway, structured, interpretable, turned out to be exactly what trustworthy federated clinical modelling needs. Brain-computer interfacing is where my methodological core was built; precision medicine is where it now does its work.

<!-- card -->

## Research agenda (next 3-5 years)

As an independent investigator, I want to build a group around the self-explaining hospital. Concretely, I aim to:

- **Make interpretability a guarantee, not a hope.** Develop self-explaining multiway architectures whose explanations are **faithful by construction** and stand up to clinical and regulatory scrutiny, so "interpretable" is a property you can verify, not a claim you take on trust.
- **Federate across real, uneven hospitals.** Build methods that let institutions holding **different modalities and incomplete data** train models which genuinely travel between them, moving from simulated silos to prospective, cross-border deployment.
- **Carry multi-modal oncology to the clinic.** Extend the HCC work from retrospective benchmarks to **prospective, clinically embedded validation**, and to further oncological and cardiovascular indications, in direct partnership with hospitals.
- **Sustain open, reusable infrastructure.** Keep building the open-source tooling (below) that lets life scientists and clinicians actually use these methods, because reproducible infrastructure is how a method reaches the bedside.

<!-- card -->

## Funding, projects & open science

**Grants and projects.** My research has been supported by, and I have contributed to, competitively funded programmes including an **FWO Fundamental Research grant** (doctoral project on finger-movement decoding), the **Flanders AI Research Program - Real-World Evidence use case** (Scientific Coordinator, ~10 researchers across 4 institutions), **ELIXIR Belgium** (consortium partner, federated health-data re-use), and the **AI-HCC (ZonMw)** project at the University of Twente. I was also selected, ranked 4th among international contractors, for the **European Food Safety Authority (EFSA) Framework Contract** in statistical and epidemiological analysis.

**Open-source software.** I believe methods should ship as usable tools. I author or contribute to:

- **[FLkit](https://github.com/UHasselt-BiomedicalDataSciences/federated-learning-toolkit)**, a community federated-learning toolkit helping life scientists apply privacy-preserving methods to decentralised, sensitive data (contributor).
- **[Block-Term Tensor Regression (BTTR)](https://github.com/TheAxeC/block-term-tensor-regression)**, a documented Python package making interpretable tensor regression reproducible for neuroscience and beyond.
- **[Federated Learning Tutorial](https://github.com/TheAxeC/federated-learning-tutorial)**, a step-by-step research tutorial lowering the entry barrier for newcomers.

**Collaborations.** My work is inherently multi-institutional, spanning the University of Twente, UHasselt, KU Leuven, Medisch Spectrum Twente, the University of Antwerp, and VIB.

<a href="/publications" class="btn btn-outline-primary mt-3">Browse publications <i class="fas fa-angle-double-right"></i></a>
<a href="/cv.pdf" class="btn btn-outline-primary mt-3">View full CV <i class="fas fa-angle-double-right"></i></a>
