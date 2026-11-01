---
layout: post
title:  "What Crosses the Hospital Wall"
category: research
publish: True
date: 2026-11-01
---

Federated learning trains a model across hospitals without pooling their records, so a hospital can join a study while its patient data stay on site. The hospitals still have to exchange something, or none would learn from the others, and that exchange can reveal information about patients. A privacy review therefore starts from what exactly leaves the building. It can be one of six objects:

- a gradient, the direction in which each weight of the model should change
- a set of model weights, the numbers a model learns
- a sum of updates under secure aggregation, a protocol that hides each site's own update
- part of a model
- a summary that compresses the data into a few components
- a score for each patient

For each object, the questions are what it reveals, who has to be watching and what else that person needs. I found published attacks on five of the six, and each attack depends on conditions that may not hold in a hospital.

Three of my own projects release part of a model, a summary and a patient score.

<figure class="chart">
<img class="only-light" src="{{ '/assets/images/what-crosses-the-hospital-wall/wall-objects-light.svg' | relative_url }}" alt="Six arrows cross the hospital boundary: gradient, model weights, sum under secure aggregation, part of a model, summary in a few components and score for each patient. A published attack was found on all but part of a model.">
<img class="only-dark" src="{{ '/assets/images/what-crosses-the-hospital-wall/wall-objects-dark.svg' | relative_url }}" alt="Six arrows cross the hospital boundary: gradient, model weights, sum under secure aggregation, part of a model, summary in a few components and score for each patient. A published attack was found on all but part of a model.">
<figcaption>The six objects that can leave a hospital, and whether I found a published attack on each.</figcaption>
</figure>

## Gradients

A gradient is computed on a batch of training examples. In the plainest federated learning, each site sends the server its gradient or its updated weights after each round.

Gradient inversion reconstructs the training images from a gradient. [Zhu and colleagues (2019)](https://arxiv.org/abs/1906.08935) recovered images from CIFAR, a benchmark of small photographs, within 270 attack iterations at batch size 1 and 2,711 at batch size 8. [Yin and colleagues (2021)](https://doi.org/10.1109/CVPR46437.2021.01607) reached 224 by 224 images and batches of up to 48, with the attacker given the batch-normalisation statistics, which are averages that a model stores about its training data.

The attack depended on those statistics. When the attacker had to infer them, the attack "fails to return a recognizable reconstruction" of a single image from ImageNet, a large photograph benchmark, according to [Huang and colleagues (2021)](https://proceedings.neurips.cc/paper/2021/hash/3b3fff6463464959dcd1b68d0320f781-Abstract.html).

A 2025 survey by [Du and colleagues](https://www.usenix.org/conference/usenixsecurity25/presentation/du) called gradient inversion "notably constrained, fragile, and easily defensible". In their tests, rounding each gradient value to 2 bits defended an image classifier at an accuracy cost of at most 5 percent.

The medical evidence I read comes from [Hatamizadeh and colleagues (2023)](https://doi.org/10.1109/TMI.2023.3239391). They tested chest X-rays and retinal photographs in a simulated federation with an honest server, which follows the protocol and studies what it receives. The one site that leaked held a single image, with a batch of 1 and one training step before sending. More images, larger batches and more local steps all hurt the attack.

All the authors work at NVIDIA, and the software tested is NVIDIA's own. This one simulated study suggests that the most exposed hospital is a small site training on one image at a time.

Gradient inversion research concentrates on image classification and overlooks tasks such as segmentation, the outlining of structures in an image, according to [Carletti and colleagues (2025)](https://www.usenix.org/conference/usenixsecurity25/presentation/carletti). They describe segmentation as "widely used in privacy-sensitive medical domains", so those medical tasks have had less testing.

## Weights and final models

Membership inference asks whether a person's record was in the training data. In a clinical cohort, membership can be the secret, because a diagnosis may define the cohort.

An overfitted model, one that fits its training records better than new ones, behaves differently on those records, which helps this attack. [Shokri and colleagues (2017)](https://doi.org/10.1109/SP.2017.41) exceeded 70 percent accuracy on a model trained on Texas hospital discharge data, using only a public prediction interface. That model scored 0.668 on its training data and 0.517 on test data.

[Nasr and colleagues (2019)](https://doi.org/10.1109/SP.2019.00065) found that more access gave a stronger attack on an image classifier trained on CIFAR-100, where 50 percent is chance:

- outputs only: 54.5 percent
- the weights: 74.3 percent
- an honest server watching a 4-site federation: 79.2 percent

The scoring rule also matters. [Carlini and colleagues (2022)](https://doi.org/10.1109/SP46214.2022.9833649) argued for counting members found while very few non-members are flagged, since a privacy failure is a confident hit on one person. Their attack, LiRA, found 0.1 to 10 percent of members with 0.001 percent of non-members flagged.

[Jebreel and colleagues (2026)](https://doi.org/10.56553/popets-2026-0105) retested LiRA with measures against overfitting and with thresholds that an attacker could set in practice. The share of claimed members who were members fell from 100 percent to about 80 to 90 percent with members at 10 percent of the population, and to about 60 to 70 percent at 1 percent. With transfer learning added it sometimes fell to 25 to 50 percent, and at those levels a flagged person can plausibly deny membership.

## Sums under secure aggregation

Secure aggregation shows the server only the sum of the site updates. The protocol of [Bonawitz and colleagues (2017)](https://doi.org/10.1145/3133956.3133982) comes with proofs against honest servers and against malicious ones, which break the protocol. It was designed for fleets of thousands of mobile phones, while the hospital federations below have tens of sites, so each sum mixes far fewer contributors.

Later attacks show that a malicious server can still extract data:

- **A planted layer:** in [Fowl and colleagues (2022)](https://arxiv.org/abs/2110.13057), the server added an extra layer to the model and recovered data verbatim. Secure aggregation "is reduced to only secure shuffling": the data comes out without the name of the site.
- **Different weights per site:** in [Pasquini and colleagues (2022)](https://doi.org/10.1145/3548606.3560557), the server sent each site different weights, which evaded the protocol "independently of the number of users". The authors named the cause as "incorrect usage of secure aggregation and lack of parameter validation", and showed that consistency checks can be added.
- **Fake sites:** in [Boenisch and colleagues (2023)](https://doi.org/10.1109/EuroSP57164.2023.00023), the server added sybils, fake sites under its control, and defeated secure aggregation combined with noise added at each site.

An honest server has a weaker attack. [Kariyappa and colleagues (2023)](https://arxiv.org/abs/2209.05578) treated summed gradients from part of a model as a mixture of signals and separated them, at batches up to 1,024, with degraded images at that size.

Whether malicious-server attacks matter to a hospital depends on who runs the server and on whether sites can check what they are sent. [Pati and colleagues (2022)](https://doi.org/10.1038/s41467-022-33407-5) described a federation built on trust between named sites. I found no study that measures how far such trust lowers this risk.

## Part of a model

A site can send less than the whole model. [Dayan and colleagues (2021)](https://doi.org/10.1038/s41591-021-01506-3) kept only updates above a percentile threshold and reported performance they called comparable at 25 percent of the updates. Sending less saves communication, and its effect on privacy has to be tested separately.

My paper *Federate What Transfers*, accepted at IEEE FLTA 2026, applies this idea to repeated liver MRI of one patient. Sites share only a backbone, the part of a model that turns an image into features, the numbers that later layers use. The backbone is pre-trained without labels, the outcomes a model learns to predict. Each site keeps its labels and its own model of change over time. On sites simulated from one cohort, the method beat the strongest federated baseline on AUPRC, the area under the precision-recall curve, a score suited to rare outcomes (0.713 against 0.677), with 37 to 55 percent less communication.

I found no attack on a shared backbone with local site layers, and I have not measured its resistance to membership inference against a full model.

## Summaries

A summary of many people can still reveal one of them. In 2008 [Homer and colleagues](https://doi.org/10.1371/journal.pgen.1000167) detected a person's presence in a DNA mixture at and below 1 percent of the mixture, given that person's genetic profile and a reference population. They concluded that composite statistics such as allele frequencies, the share of each gene variant in a group, "do not mask identity". The US National Institutes of Health (NIH) [removed these summary data from public sites](https://www.genome.gov/Pages/About/NACHGR/September2008Agenda/ProjectingAggregateGenomicData.pdf) in response.

Later work limited that result in one setting and extended it in another. [Sankararaman (2010)](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2010/EECS-2010-51.pdf) derived an upper bound on the chance that any such test detects a member, and found for a pool of 1,000 people that this power "is in fact limited". [Dwork and colleagues (2015)](https://doi.org/10.1109/FOCS.2015.46) proved that detecting one person in released statistics still works after those statistics are distorted, when the data has about $n^2$ attributes for $n$ people. In 2018 the NIH [restored unrestricted access](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-19-023.html) to genomic summary results from most of the studies it supports and kept sensitive studies controlled.

Principal component analysis, which compresses data into a few components, has the same kind of exposure. [Zari and colleagues (2022)](https://doi.org/10.1007/978-3-031-13945-1_19) ran membership inference against it. AUC, the chance that the attack ranks a member above a non-member, reached 0.9 on image data and was much lower on census data with 13 or 14 attributes per record. It rose with the number of components and fell with the number of samples.

A federated version leaks in another way. [Hartebrodt and colleagues (2024)](https://doi.org/10.1007/s10618-023-00983-z) showed that in federated subspace iteration, which computes such components across sites, the server can compute how all variables vary together, given enough rounds. Secure multiparty computation, which hides each site's input, did not stop this, since the aggregated updates stay visible.

My [single-cell work]({{ '/publications/preprint/fed-multicellular-immune.pdf' | relative_url }}), under review, releases a summary of this kind. Sites recover disease programs, patterns of gene activity across cell types, and only a program subspace, a small set of directions in gene space, leaves each site. We tested one attack, which scores how well a subspace reconstructs a donor's data, on a lupus dataset of 261 donors. Attack AUC was 0.906 on the subspaces of individual sites and 0.609 on the merged subspace, which combines them into one.

On the same dataset, exposure varied with what was released and with site size. A score for each donor gave an attack AUC of 1.000. Site subspaces gave AUC that rose as sites shrank, from 0.61 at 130 donors per site to 0.98 at 20.

The program subspace also predicted self-reported ancestry at AUC 0.81. Ancestry may overlap with cohort or disease in this dataset, and the result still shows that a released subspace can carry information about a donor's population.

The gap between 0.906 and 0.609 is a difference between two released objects. Additive secure aggregation, which adds numbers, does not produce the merged subspace, so hiding the site subspaces would need a separate secure protocol, which we did not build. An [earlier arXiv version](https://arxiv.org/abs/2606.24938) of the paper described that contrast as a gain from secure aggregation, and the preprint linked above corrects it.

## Budgets

Differential privacy adds calibrated noise so that one record can change the output only by a bounded amount. It is the one defence here that states a number, the privacy budget $\varepsilon$, and that bound holds whatever attack is used. A smaller $\varepsilon$ means stronger protection.

The accuracy cost of differential privacy varied by task:

- **Pneumonia, outside a federation:** [Ziller and colleagues (2021)](https://doi.org/10.1038/s41598-021-93030-0) reported AUC of 0.848 at $\varepsilon = 0.52$ and 0.882 at $\varepsilon = 2.69$, against 0.960 without privacy.
- **Liver segmentation, outside a federation:** the same paper reported a Dice overlap, where 1 is a perfect match, of 0.943 at $\varepsilon = 0.12$ against 0.950.
- **Simulated federation:** [Adnan and colleagues (2022)](https://doi.org/10.1038/s41598-022-05539-7) found no loss in test accuracy at $\varepsilon = 2.90$, and a loss of 0.034 on external data against plain federated learning.

The large clinical federations I read gave no such number. [Dayan and colleagues (2021)](https://doi.org/10.1038/s41591-021-01506-3) ran 20 sites, and [Pati and colleagues (2022)](https://doi.org/10.1038/s41467-022-33407-5) ran 71 sites on six continents. Both said what was released, as did the multi-institution experiment of [Sheller and colleagues (2020)](https://doi.org/10.1038/s41598-020-69250-1). None stated an $\varepsilon$ in the text or in the supplements I could search.

Dayan and colleagues called their partial sharing a differential privacy technique, although they added no noise, and said that a quantifiable privacy measure would be needed. The federation of Pati and colleagues used encrypted transport and trust between named sites, and neither of these bounds what an update reveals.

## Scores in vertical federated learning

In vertical federated learning, the sites hold different variables for the same patients. One department has the ECG, another has the labs, and only one holds the outcome. What leaves is then a score indexed by patient, such as the output of the cut layer, the point where a split model is divided between sites.

These scores can leak outcomes, variables and whole inputs:

- **Outcomes:** [Fu and colleagues (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/fu-chong) recovered outcome labels from the sign of returned gradients at accuracy 1.0000 on six datasets, given per-sample gradients and no model split. With a split and 70 known labels, F1, a score where 1 is perfect, was 0.7614 on breast tissue images.
- **Outcomes:** [Li and colleagues (2022)](https://arxiv.org/abs/2102.08504) recovered labels through cut-layer gradients in two-party split learning, with an AUC of about 1 on unprotected skin lesion images throughout training.
- **Variables:** [Luo and colleagues (2021)](https://doi.org/10.1109/ICDE51399.2021.00023) showed that, for logistic regression, a linear classifier, one prediction reveals up to $c-1$ unknown variables exactly, where $c$ is the number of classes.
- **Inputs:** [Pasquini and colleagues (2021)](https://doi.org/10.1145/3460120.3485259) showed that a malicious server can steer a site's model into a form it can invert, given a public dataset similar to the site's data.

In *Private Coupled Descent*, a paper of mine under review at IEEE Transactions on Signal Processing, only a short shared score leaves each site. Differential privacy noise goes on that score, and the tables of variables stay local. The excess risk, the error added by privacy, then depends on the score length and the regression problem, and does not grow with the number of variables.

In a synthetic check, the excess risk stayed flat across a 100-fold increase in the number of variables. On well-conditioned problems, meaning numerically stable ones, a matching lower bound shows that this excess risk cannot be improved in its dependence on the privacy budget. I have not tested the method against the attacks listed above.

## European law

European law appears to be moving towards asking about the object and the recipient. The European Data Protection Board's [Opinion 28/2024](https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf) says personal data may remain "absorbed" in a model's weights, and that models trained on personal data "cannot, in all cases, be considered anonymous". In 2025 the Court of Justice held in [EDPS v SRB](https://publications.europa.eu/resource/celex/62023CJ0413) (C-413/23 P) that pseudonymised data, where names are replaced by codes, are not "in all cases and for every person" personal data, which ties the status of data to the party holding it.

The Board's opinion does not mention federated learning, and the judgment concerns pseudonymised comments under the regulation for EU bodies. Whether either applies to a model update in transit is a question for a lawyer.

## Questions for a hospital

The attacks above are research demonstrations. I found no documented attack on a live clinical federation, so I cannot say how large the risk is in practice. The best-supported leak differs by object:

| What leaves | Best-supported leak | What it needs | Where it weakens |
|---|---|---|---|
| Gradients | Image reconstruction | Small batch, batch-normalisation statistics | Large batches, inferred statistics, rounding |
| Weights | Membership | Access to the weights helps | Well-fitted model, few members |
| Secure sums | Verbatim recovery | A malicious server | Consistency checks |
| Part of a model | Not measured | | |
| Summaries | Membership | The target's record, more components | Large pools, fewer components |
| Patient-indexed scores | Outcomes, variables | Returned gradients or predictions | Not measured |

A hospital asked to join a federation can test the privacy claim against the object released:

1. What exactly leaves, in what shape, at each round?
2. Who sees it per site, and who sees only a sum?
3. How many patients stand behind it at the smallest site?
4. Is it indexed by patient?
5. What number, if any, bounds what it reveals, and against which attacker?

## References

- Adnan, M., Kalra, S., Cresswell, J. C., Taylor, G. W. and Tizhoosh, H. R., "Federated learning and differential privacy for medical image analysis", Scientific Reports 12, 2022. https://doi.org/10.1038/s41598-022-05539-7
- Boenisch, F. et al., "Reconstructing individual data points in federated learning hardened with differential privacy and secure aggregation", IEEE EuroS&P, 2023. https://doi.org/10.1109/EuroSP57164.2023.00023
- Bonawitz, K. et al., "Practical secure aggregation for privacy-preserving machine learning", ACM CCS, 2017. https://doi.org/10.1145/3133956.3133982
- Carletti, V., Foggia, P., Mazzocca, C., Parrella, G. and Vento, M., "SoK: Gradient inversion attacks in federated learning", USENIX Security, 2025.
- Carlini, N., Chien, S., Nasr, M., Song, S., Terzis, A. and Tramer, F., "Membership inference attacks from first principles", IEEE S&P, 2022. https://doi.org/10.1109/SP46214.2022.9833649
- Court of Justice of the European Union, C-413/23 P, EDPS v SRB, 4 September 2025, ECLI:EU:C:2025:645.
- Dayan, I. et al., "Federated learning for predicting clinical outcomes in patients with COVID-19", Nature Medicine 27, 2021. https://doi.org/10.1038/s41591-021-01506-3
- Du, J. et al., "SoK: On gradient leakage in federated learning", USENIX Security, 2025.
- Dwork, C., Smith, A., Steinke, T., Ullman, J. and Vadhan, S., "Robust traceability from trace amounts", IEEE FOCS, 2015. https://doi.org/10.1109/FOCS.2015.46
- European Data Protection Board, Opinion 28/2024, 17 December 2024.
- Fowl, L., Geiping, J., Czaja, W., Goldblum, M. and Goldstein, T., "Robbing the fed: Directly obtaining private data in federated learning with modified models", ICLR, 2022.
- Fu, C. et al., "Label inference attacks against vertical federated learning", USENIX Security, 2022.
- Hartebrodt, A., Rottger, R. and Blumenthal, D. B., "Federated singular value decomposition for high-dimensional data", Data Mining and Knowledge Discovery 38, 2024. https://doi.org/10.1007/s10618-023-00983-z
- Hatamizadeh, A. et al., "Do gradient inversion attacks make federated learning unsafe?", IEEE Transactions on Medical Imaging, 2023. https://doi.org/10.1109/TMI.2023.3239391
- Homer, N. et al., "Resolving individuals contributing trace amounts of DNA to highly complex mixtures using high-density SNP genotyping microarrays", PLoS Genetics, 2008. https://doi.org/10.1371/journal.pgen.1000167
- Huang, Y., Gupta, S., Song, Z., Li, K. and Arora, S., "Evaluating gradient inversion attacks and defenses in federated learning", NeurIPS, 2021.
- Jebreel, N., Khalil, M., Sanchez, D. and Domingo-Ferrer, J., "Revisiting the LiRA membership inference attack under realistic assumptions", Proceedings on Privacy Enhancing Technologies 2026(3). https://doi.org/10.56553/popets-2026-0105
- Kariyappa, S. et al., "Cocktail party attack: Breaking aggregation-based privacy in federated learning using independent component analysis", ICML, 2023.
- Li, O. et al., "Label leakage and protection in two-party split learning", ICLR, 2022.
- Luo, X., Wu, Y., Xiao, X. and Ooi, B. C., "Feature inference attack on model predictions in vertical federated learning", IEEE ICDE, 2021. https://doi.org/10.1109/ICDE51399.2021.00023
- Nasr, M., Shokri, R. and Houmansadr, A., "Comprehensive privacy analysis of deep learning", IEEE S&P, 2019. https://doi.org/10.1109/SP.2019.00065
- National Institutes of Health, NOT-OD-19-023, November 2018.
- Pasquini, D., Ateniese, G. and Bernaschi, M., "Unleashing the tiger: Inference attacks on split learning", ACM CCS, 2021. https://doi.org/10.1145/3460120.3485259
- Pasquini, D., Francati, D. and Ateniese, G., "Eluding secure aggregation in federated learning via model inconsistency", ACM CCS, 2022. https://doi.org/10.1145/3548606.3560557
- Pati, S. et al., "Federated learning enables big data for rare cancer boundary detection", Nature Communications 13, 2022. https://doi.org/10.1038/s41467-022-33407-5
- Sankararaman, S., Statistical models for analyzing human genetic variation, UC Berkeley EECS-2010-51, chapter 6, 2010.
- Sheller, M. J. et al., "Federated learning in medicine: Facilitating multi-institutional collaborations without sharing patient data", Scientific Reports 10, 2020. https://doi.org/10.1038/s41598-020-69250-1
- Shokri, R., Stronati, M., Song, C. and Shmatikov, V., "Membership inference attacks against machine learning models", IEEE S&P, 2017. https://doi.org/10.1109/SP.2017.41
- Yin, H. et al., "See through gradients: Image batch recovery via GradInversion", CVPR, 2021. https://doi.org/10.1109/CVPR46437.2021.01607
- Zari, O., Parra-Arnau, J., Unsal, A., Strufe, T. and Onen, M., "Membership inference attack against principal component analysis", Privacy in Statistical Databases, 2022. https://doi.org/10.1007/978-3-031-13945-1_19
- Zhu, L., Liu, Z. and Han, S., "Deep leakage from gradients", NeurIPS, 2019.
- Ziller, A. et al., "Medical imaging deep learning with differential privacy", Scientific Reports 11, 2021. https://doi.org/10.1038/s41598-021-93030-0
