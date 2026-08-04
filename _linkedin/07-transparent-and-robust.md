---
layout: post
title: "Transparent and robust: interpretable models degrade more gracefully than foundation models"
category: research
publish: True
date: 2026-08-04
---

Enterprises reach for the black-box foundation model because they assume it is the ROBUST choice, and treat the lost transparency as the price of that robustness.

We tested the assumption. On our task it runs the other way.

The setup: predict 1-year mortality from a single 12-lead ECG. A transparent gradient-boosted model on 165 named ECG features plus age, against six open ECG foundation models, on two cohorts.

On clean data it is a draw. 0.757 against 0.761 AUROC.

Then we degraded the signal, which is what deployment actually looks like. At severe muscle-noise contamination the best foundation model falls from 0.812 to 0.614. The transparent model holds at 0.754.

Move the model to another hospital as well and the gap widens rather than closes: its cross-site advantage grows from +0.017 on clean signals to +0.066 under severe noise.

The honest counterweight: foundation models win under whole-lead dropout, because they saw missing leads during pretraining while a named feature simply goes to zero.

The mechanism is unglamorous. Age is a strong predictor that noise cannot corrupt and the encoder never sees, and named measurements are stable across sites.

So on this task there was no transparency-versus-robustness trade to make. The model an overseer can read is also the one still standing when a bad recording arrives at 3am from a different hospital.

Accepted at the XAI-EADM workshop at IEEE CBI/EDOC 2026, here in Enschede this September. Come find me there.

How do you test your deployed models under degraded inputs?

#ExplainableAI #FoundationModels #Robustness #HealthcareAI #AIGovernance
