---
layout: post
title: "Removing a patient from a model does not stick"
category: research
publish: True
date: 2026-09-05
---

🔐 A hospital can delete a patient's record. Three months, no reason needed. That part works.

Ask what happened to the model that trained on that record, and there is no good answer.

The record is out of the database. The model still has whatever it picked up. There are methods for taking it back out and people work on them, but the removals do not hold. Fine-tune the model on unrelated data and what was taken out comes back. Sometimes compressing it for deployment is enough.

We also cannot say where in a model one patient's record ends up, so there is nothing precise to aim at. Regulators have not settled whether the weights count as personal data at all, so there is not much of a rule to comply with either.

That is some of what I work on now. Where does one record sit in the weights, and can you cut it out with the model still working afterwards.

Until that is solved, hospitals should say so out loud. Put it in the information patients get: the model keeps something of your record, and we cannot currently undo that. It beats claiming a deletion that did not happen.

If you train on patient data or any other kind of personal data, what does your deletion procedure actually promise?

#HealthcareAI #Privacy #LLM #MachineLearning
