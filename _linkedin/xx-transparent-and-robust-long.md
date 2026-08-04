---
layout: post
title: "Transparent and robust: interpretable models degrade more gracefully than foundation models"
category: research
publish: False
date: 2026-08-11
---

There is an assumption built into a lot of enterprise AI right now, and it usually goes unstated: the foundation model is the ROBUST choice, and losing transparency is the price you pay for that robustness.

We tested that assumption on a mission-critical clinical decision task. On this task, it is false.

The setup

Case study: predict 1-year all-cause mortality from a single 12-lead ECG. Two cohorts, MIMIC-IV-ECG (n = 14,000, 12.9% mortality) and the Brazilian CODE-15 (n = 65,000, 4.3%).

The transparent model: gradient boosting on 165 named ECG features plus age. 166 inputs, every one of them something you can point at and explain.

The black boxes: six open ECG foundation models.

Then the part that usually gets skipped. Instead of only testing on clean data, we ran the whole comparison through the conditions a deployed model actually meets: six kinds of signal corruption at increasing severity, and cross-site transfer between the two cohorts.

On clean data, it is a draw

MIMIC: 0.757 for the transparent model against 0.761 for the best foundation model. CODE-15: 0.804 against 0.812. Confidence intervals overlap in both cohorts, so this is parity, honestly stated, and not a win.

If the story ended there you would reasonably pick the foundation model and accept the opacity.

Under degradation, the gap opens the other way

At severe EMG noise, the best foundation model collapses from 0.812 to 0.614. The transparent model goes from 0.804 to 0.754. The intervals do not overlap. Same picture for combined bad-recording conditions.

Now put the two together, which is what deployment actually looks like: move the model to another site AND degrade the signal. Transporting from MIMIC to CODE-15, the transparent model beats all six foundation models, and its margin GROWS from +0.017 on clean data to +0.066 under severe noise. The worse the conditions, the bigger the advantage of the model you can read.

Where the foundation models win, and why

They win under lead dropout, by a clear margin. That is the honest counterweight and it points straight at the mechanism.

Additive noise favours the glass box, because age is a strong predictor that noise cannot touch and named measurements are stable across sites. Structural loss favours the black box, because the encoders have seen missing leads in pretraining, while zeroing out a named per-lead feature is genuinely destructive to a feature table.

So this is not a blanket ranking. It is a decision rule: know which failure mode your pipeline actually faces, and pick accordingly. If your ECGs are noisy and come from multiple sites, the transparent model is the robust option AND the auditable one. If leads drop out, that flips.

The other honest caveat: transporting in the reverse direction, CODE-15 to MIMIC, the transparent model trails the single best foundation model by 0.02 to 0.06. It beats ECGFounder both ways, but the reverse direction is not a clean sweep and the paper says so.

Why I think this matters for governance

The usual framing is a tradeoff: you can have performance or you can have transparency. That framing lets an organisation treat opacity as a cost of doing business, something to be managed with documentation rather than avoided.

On this task, there was no tradeoff to make. Transparency came for free on clean data and paid a dividend exactly where robustness matters most, under degraded inputs and site shift. That is a governance argument, not only a modelling one: the model you can inspect is also the one that holds up when the input quality drops at 3am in a different hospital.

I want to be careful about scope. This is one clinical task, one endpoint, six encoders, one evaluation protocol. It is an applied rigor result, not a law of nature. What I would push for is that "we used a foundation model, therefore it is robust" stops being an assumption anyone gets to make for free. Test it under degradation. It is cheap, and the answer is not obvious in advance.

One footnote that I enjoyed

When I rebuilt this study from scratch to check reproducibility, the transparent model came back BIT-IDENTICAL everywhere, because its features are computed on CPU with deterministic code. The foundation model baselines wobbled at the fourth decimal from ordinary GPU kernel nondeterminism, amplified by a discontinuous boosting head. Every claim in the paper survived, with zero sign flips.

Even the reproduction was more graceful on the transparent side.

The paper has been ACCEPTED at the XAI-EADM workshop at IEEE CBI/EDOC 2026, which happens to be here in Enschede, 15-18 September. I will be presenting it there.

If you work on model governance, clinical deployment, or robustness evaluation, come find me, or tell me here how you test for this in your own pipelines. My honest suspicion is that most deployed systems have never been evaluated under the conditions they will actually meet.

#ExplainableAI #FoundationModels #Robustness #HealthcareAI #AIGovernance #MachineLearning #InterpretableAI
