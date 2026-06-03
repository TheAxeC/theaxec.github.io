---
layout: default
title: Research
navbar_name: Research
permalink: /research
description: "Research statement of Dr. Axel Faes - multi-modal foundation models, privacy-preserving federated learning, and brain-computer interfaces for precision medicine and oncology."
keywords: "Axel Faes research, foundation models, federated learning, precision oncology, brain-computer interfaces, tensor regression, explainable AI, healthcare"
---

<div class="row mt-3 main_view">
    <div class="col">
        <div class="card border-0 shadow-sm bg-white">
            <div class="card-body p-4 p-md-5" markdown="1">

# Research

I build **AI systems that learn from sensitive, multi-modal biomedical data without compromising patient privacy**, and I translate them into tools clinicians can actually trust. My work sits at the intersection of three areas that have converged over the course of my career: **multi-modal foundation models**, **privacy-preserving federated learning**, and **neural decoding for brain-computer interfaces**. My current methodological focus is on **deep learning** and **explainable AI (XAI)** — designing architectures expressive enough to capture multi-modal biomedical signal, and interpretable enough for clinicians to trust. The connective tissue across all three areas is a single motivating question: *how do we turn high-dimensional, fragmented, privacy-constrained health data into clinically actionable insight?*

</div>
        </div>
    </div>
</div>

<div class="row mt-3 main_view">
    <div class="col">
        <div class="card border-0 shadow-sm bg-white">
            <div class="card-body p-4 p-md-5" markdown="1">

## Research themes

### 1. Multi-modal foundation models for precision oncology

At the University of Twente (CODE) and Medisch Spectrum Twente, within the **AI-HCC (ZonMw)** project, I develop foundation models and deep learning architectures that integrate **longitudinal MRI, multi-omics profiles, and clinical variables** for the early detection and risk stratification of hepatocellular carcinoma. The core challenge is temporal and cross-modal: disease signal is distributed across imaging, molecular, and clinical timelines that are individually noisy and rarely aligned. I work on transformer-based architectures that model these temporal dynamics jointly, and on explainable-AI frameworks that link imaging features and molecular markers back to clinically meaningful outcomes — a prerequisite for clinical translation in oncology.

### 2. Privacy-preserving federated learning for healthcare

As Scientific Coordinator of the **Flanders AI Research Program's Real-World Evidence use case** and Technical Machine Learning Lead of the Biomedical Data Sciences group at UHasselt, I built federated learning frameworks that let institutions collaborate on clinical research **without ever sharing raw patient data**. This line of work spans federated tensor regression for longitudinal health data, distributed architectures for heterogeneous clinical datasets, and the practical translation of these methods into cardiovascular disease prediction and population health management. Privacy-preserving collaboration is, to me, the central enabler of large-scale clinical AI — it is what makes the data accessible in the first place.

### 3. Brain-computer interfaces and neural decoding

My doctoral and postdoctoral research decoded **finger movements and sign-language gestures from high-density intracranial recordings (ECoG)**. I introduced **block-term tensor regression** methods that capture the spatiotemporal structure of neural signals more faithfully than conventional approaches, and I studied cross-subject generalisation for robust, deployable BCIs. This work advances both the fundamental understanding of how the motor cortex encodes movement and language, and the assistive communication technology that can restore function for people who have lost it.

### A cross-cutting methodological thread

These themes are not separate projects but one research programme. The tensor methods I developed for neural decoding became the basis for **federated** regression on clinical data; that foundation now drives my work on **deep learning architectures** and **explainable AI** for multi-modal precision medicine. The explainability demands of oncology echo the interpretability I need for BCIs to be clinically trusted. My contribution is to treat privacy, multi-modality, and interpretability not as constraints bolted on after the fact, but as first-class design objectives.

</div>
        </div>
    </div>
</div>

<div class="row mt-3 main_view">
    <div class="col">
        <div class="card border-0 shadow-sm bg-white">
            <div class="card-body p-4 p-md-5" markdown="1">

## Research agenda (next 3–5 years)

As an independent investigator, my goal is to establish a group at the convergence of my three themes: **federated foundation models for trustworthy precision medicine**. Concretely, I aim to:

- **Unify federated learning and foundation models.** Foundation models are data-hungry; the richest biomedical data is locked behind privacy and institutional boundaries. I will develop methods to *pre-train and adapt foundation models in a federated setting*, so that multi-institutional cohorts can power large models without centralising sensitive data.
- **Advance multi-modal clinical translation.** Building on AI-HCC, I will extend multi-modal integration (imaging + omics + clinical) to additional oncological and cardiovascular indications, working directly with hospital partners to move from retrospective benchmarks to prospective, clinically embedded validation.
- **Make trustworthy AI a deliverable, not a disclaimer.** I will continue to develop explainable-AI and uncertainty-quantification methods designed for the realities of clinical and regulatory acceptance, so that model outputs are interpretable and actionable for clinicians.
- **Sustain open, reusable infrastructure.** I will keep building the open-source tooling (below) that lowers the barrier for life scientists to apply these methods, because reproducible infrastructure is how methodological advances actually reach the clinic.

</div>
        </div>
    </div>
</div>

<div class="row mt-3 main_view">
    <div class="col">
        <div class="card border-0 shadow-sm bg-white">
            <div class="card-body p-4 p-md-5" markdown="1">

## Funding, projects & open science

**Grants and projects.** My research has been supported by, and I have contributed to, competitively funded programmes including an **FWO Fundamental Research grant** (doctoral project on finger-movement decoding), a **€1.15M FWO Senior Research Project, *Federated Learning for Population Health Management*** (co-supervisor; with Y. Moreau, L. Peeters, B. Vaes), the **Flanders AI Research Program – Real-World Evidence use case** (Scientific Coordinator, ~10 researchers across 4 institutions), **ELIXIR Belgium** (consortium partner, health-data re-use and federated analyses), and the **AI-HCC (ZonMw)** project at the University of Twente. I was also selected — ranked 4th among international contractors — for the **European Food Safety Authority (EFSA) Framework Contract** in statistical and epidemiological analysis.

**Open-source software.** I believe methods should ship as usable tools. I lead or author:

- **[FLkit](https://github.com/UHasselt-BiomedicalDataSciences/federated-learning-toolkit)** — a federated-learning toolkit helping life scientists apply privacy-preserving methods to decentralised, sensitive data.
- **[Block-Term Tensor Regression (BTTR)](https://github.com/TheAxeC/block-term-tensor-regression)** — a documented Python package making tensor regression reproducible for neuroscience and beyond.
- **[Federated Learning Tutorial](https://github.com/TheAxeC/federated-learning-tutorial)** — a step-by-step research tutorial lowering the entry barrier for newcomers.

**Collaborations.** My work is inherently multi-institutional, spanning the University of Twente, UHasselt, KU Leuven, Medisch Spectrum Twente, the University of Antwerp, and VIB.

<a href="/publications" class="btn btn-outline-primary mt-3">Browse publications <i class="fas fa-angle-double-right"></i></a>
<a href="/cv.html" class="btn btn-outline-primary mt-3">View full CV <i class="fas fa-angle-double-right"></i></a>

</div>
        </div>
    </div>
</div>
