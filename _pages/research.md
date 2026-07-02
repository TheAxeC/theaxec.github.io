---
layout: page
title: Research
navbar_name: Research
permalink: /research
body_class: pubpage statement
description: "Research statement of Dr. Axel Faes - self-explaining, interpretable AI and privacy-preserving federated learning that travels between hospitals, for precision oncology and trustworthy clinical decision support."
keywords: "Axel Faes research, self-explaining AI, interpretable machine learning, federated learning, block-term tensor regression, precision oncology, hepatocellular carcinoma, trustworthy clinical AI, healthcare"
---

<h1>Research</h1>

<p class="stmt-lede">I build clinical AI with two properties most systems lack: it can <strong>explain its own reasoning</strong> to the clinician using it, and it can be <strong>trained across hospitals without any of them giving up their data</strong>. I think of the goal as <strong>the self-explaining hospital</strong> - care supported by models that are interpretable by design and that travel between institutions instead of forcing the data to travel to them.</p>

<section class="stmt-sec">
  <h2 class="psec-h">Research themes</h2>
  <p>Three lines of work converge on the self-explaining hospital. What ties them together is a methodological signature: <strong>multiway (block-term tensor) models whose structure <em>is</em> the explanation</strong>, rather than something reconstructed after the fact.</p>

  <article class="stmt-theme pcol pcol-tensor">
    <div class="pdia">{% include site/program-diagram.html key='tensor' %}</div>
    <div>
      <h3><span class="n">01</span> Interpretable, self-explaining models</h3>
      <p>Clinical machine learning is full of models that are accurate and unaccountable - they return a number, not a reason. I design models that are interpretable <em>by construction</em>. My <strong>block-term tensor networks</strong> decompose a signal into components that line up with structure a clinician already reasons about - regions, rhythms, time windows, modalities - so the explanation is read directly off the model rather than approximated afterwards by a separate tool. My flagship cardiology result does exactly this: a block-term tensor model that identifies <strong>atrial-fibrillation substrate from routine sinus-rhythm ECG</strong>, with components a cardiologist can read as time-by-lead signatures, and that holds its own against deep and foundation-model baselines. The aim is to make interpretability a <strong>first-class design objective and a guarantee</strong>, not a disclaimer bolted on at the end. This matters most exactly where AI is hardest to trust: high-stakes, low-data clinical decisions, where a plausible-but-wrong answer is worse than no answer at all.</p>
    </div>
  </article>

  <article class="stmt-theme pcol pcol-federated">
    <div class="pdia">{% include site/program-diagram.html key='federated' %}</div>
    <div>
      <h3><span class="n">02</span> Federated learning that travels between institutions</h3>
      <p>The most informative clinical data is fragmented across hospitals and walled off by privacy law, which is precisely why so much of it stays unused. I build <strong>federated learning</strong> methods that let institutions train shared models <strong>without raw data ever leaving their walls</strong>, including the hard, realistic case where different sites hold <strong>different modalities and incomplete records</strong>. As Technical Machine Learning Lead and Scientific Coordinator of the <strong>Flanders AI Research Program's Real-World Evidence use case</strong> at UHasselt, I built these systems across multiple institutions for cardiovascular risk prediction and population health management. Federation is what turns locked, scattered data into something a model can learn from in the first place.</p>
    </div>
  </article>

  <article class="stmt-theme pcol pcol-hcc">
    <div class="pdia">{% include site/program-diagram.html key='hcc' %}</div>
    <div>
      <h3><span class="n">03</span> Multi-modal precision oncology</h3>
      <p>Within the <strong>AI-HCC (ZonMw)</strong> project at the University of Twente and Medisch Spectrum Twente, I develop models that integrate <strong>longitudinal MRI, multi-omics, and clinical variables</strong> for the early detection and risk stratification of hepatocellular carcinoma. The signal is spread across imaging, molecular, and clinical timelines that are each noisy and rarely aligned, so I work on <strong>self-supervised backbones for longitudinal medical imaging</strong> that learn from unlabelled scans, and on architectures that model these timelines jointly. This is where the other two threads meet: a model that flags rising cancer risk has to <strong>say why</strong>, and has to learn from cohorts <strong>no single hospital holds on its own</strong>.</p>
    </div>
  </article>

  <div class="stmt-origin pcol">
    <div class="pdia">{% include site/program-diagram.html key='eeg' %}</div>
    <div>
      <h3>Where the methods came from</h3>
      <p>The spine of this programme was forged in <strong>neural decoding</strong>. During my PhD and early postdoctoral work I decoded finger movements and sign-language gestures from high-density intracranial (ECoG) recordings, and to capture the spatiotemporal structure of neural signals I developed <strong>block-term tensor regression</strong>. Those methods - multiway, structured, interpretable - turned out to be exactly what trustworthy federated clinical modelling needs. Brain-computer interfacing is where my methodological core was built; precision medicine is where it now does its work.</p>
    </div>
  </div>
</section>

<section class="stmt-sec">
  <h2 class="psec-h">Research agenda (next 3-5 years)</h2>
  <p>As an independent investigator, I want to build a group around the self-explaining hospital. Concretely, I aim to:</p>
  <ul class="stmt-agenda">
    <li><strong>Make interpretability a guarantee, not a hope.</strong> Develop self-explaining multiway architectures whose explanations are <strong>faithful by construction</strong> and stand up to clinical and regulatory scrutiny, so "interpretable" is a property you can verify, not a claim you take on trust.</li>
    <li><strong>Federate across real, uneven hospitals.</strong> Build methods that let institutions holding <strong>different modalities and incomplete data</strong> train models which genuinely travel between them, moving from simulated silos to prospective, cross-border deployment.</li>
    <li><strong>Carry multi-modal oncology to the clinic.</strong> Extend the HCC work from retrospective benchmarks to <strong>prospective, clinically embedded validation</strong>, and to further oncological and cardiovascular indications, in direct partnership with hospitals.</li>
    <li><strong>Sustain open, reusable infrastructure.</strong> Keep building the open-source tooling (below) that lets life scientists and clinicians actually use these methods, because reproducible infrastructure is how a method reaches the bedside.</li>
  </ul>
</section>

<section class="stmt-sec">
  <h2 class="psec-h">Funding, projects &amp; open science</h2>
  <p><strong>Grants and projects.</strong> My research has been supported by, and I have contributed to, competitively funded programmes including an <strong>FWO Fundamental Research grant</strong> (doctoral project on finger-movement decoding), the <strong>Flanders AI Research Program - Real-World Evidence use case</strong> (Scientific Coordinator, ~10 researchers across 4 institutions), <strong>ELIXIR Belgium</strong> (consortium partner, federated health-data re-use), and the <strong>AI-HCC (ZonMw)</strong> project at the University of Twente. I was also selected, ranked 4th among international contractors, for the <strong>European Food Safety Authority (EFSA) Framework Contract</strong> in statistical and epidemiological analysis.</p>

  <div class="stmt-sub">Open-source software</div>
  <p>I believe methods should ship as usable tools. I author or contribute to:</p>
  <ul class="stmt-list">
    <li><strong><a href="https://github.com/UHasselt-BiomedicalDataSciences/federated-learning-toolkit" target="_blank" rel="noopener">FLkit</a></strong> - a community federated-learning toolkit helping life scientists apply privacy-preserving methods to decentralised, sensitive data (contributor).</li>
    <li><strong><a href="https://github.com/TheAxeC/block-term-tensor-regression" target="_blank" rel="noopener">Block-Term Tensor Regression (BTTR)</a></strong> - a documented Python package making interpretable tensor regression reproducible for neuroscience and beyond.</li>
    <li><strong><a href="https://github.com/TheAxeC/federated-learning-tutorial" target="_blank" rel="noopener">Federated Learning Tutorial</a></strong> - a step-by-step research tutorial lowering the entry barrier for newcomers.</li>
  </ul>

  <div class="stmt-sub">Collaborations</div>
  <p>My work is inherently multi-institutional, spanning the University of Twente, UHasselt, KU Leuven, Medisch Spectrum Twente, the University of Antwerp, and VIB.</p>
</section>

<div class="stmt-cta">
  <a class="btn" href="{{ '/publications' | relative_url }}">Browse publications &rarr;</a>
  <a class="btn" href="{{ '/cv.pdf' | relative_url }}" target="_blank" rel="noopener">View full CV &rarr;</a>
</div>
