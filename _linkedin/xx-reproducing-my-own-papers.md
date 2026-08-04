---
layout: post
title: "I reproduced my own papers from scratch. Here is what broke."
category: research
publish: False
date: 2026-08-04
---

Every paper I have out there says the code is available. A few months ago I decided to find out what that sentence is actually worth.

So I set a rule, and I made it deliberately unforgiving.

Reproducible means: a stranger clones the repo, obtains the documented data, runs ONE command, and gets every number, every table and every figure back, starting from the raw inputs. No pre-built caches. No "just run this script first to generate the features". No reusing a checkpoint to save time. If they hit a single "file not found", it failed. Not their fault, mine.

I then held eight projects to that rule. Here is what fell out.

1. A pipeline that only worked because of a file nobody built

One merge step reconstructed the canonical record ordering by reading a cache file that had no builder anywhere in the repo. It had passed for months, because a stale copy of that file was sitting in my cache directory from an earlier version of the design. I emptied the cache, and the pipeline died on the first merge with FileNotFoundError.

That bug is invisible to code review. It is invisible to any run that starts from an existing cache. The only thing that finds it is a genuine from-scratch run.

2. Figures that were typed instead of computed

Some figure scripts had their numbers hardcoded. One had quietly drifted out of sync with the table it was illustrating. The fix was structural: every analysis script now writes its numbers to a json file, the figure scripts read that json, and one command regenerates both. Numbers get computed once and transcribed zero times.

3. An analysis script that was never in the pipeline

A draft quoted a +0.016 margin where the canonical pipeline produced +0.013. The script behind it used a slightly different feature bank and had never been wired into the entry point, so its number could not be regenerated at all. On another project, six generators had the same problem: they existed, they ran, they were simply not in the job graph. If it is not in the DAG, it is not reproducible, it is folklore.

4. A crash on a dash

One deposit script died on an em dash in a generated file. Completely trivial, and it would have hit the very first person who tried to run it.

5. A result that moved

Rebuilding one cohort from raw produced a deterministic patient subset, different from the development one. One head-to-head comparison with a +0.007 margin had its confidence interval cross zero, moving from a nominal win to a statistical tie. The headline was unchanged and the table is arguably cleaner now, since every remaining win survives Bonferroni correction.

I would much rather find that myself than have a reviewer find it. And I would never have found it by re-running from a saved cache.

What the discipline costs, and what it pays back

Reproducing from raw means reading everything again, every time. On one project that came to roughly 646 GB of network reads per full run, which is the kind of thing that makes an HPC admin write you an email. Chunking the job arrays and pre-slicing the test split brought it to about 83 GB and cut the number of submitted jobs from around 90 to 44. The reproducibility rule forced an engineering fix that made the pipeline about eight times cheaper to run. That was not the goal, it was the dividend.

Be honest about what does not come back byte-exact

GPU nondeterminism is real. On the ECoG project all 28 jobs re-ran and the headline came back at r 0.561 against the published 0.566. In band, not identical. That belongs in the repo notes, stated plainly, with the reason. The same for anything gated behind credentialed data or a specific cluster: say which numbers you re-ran and which you did not.

The check I now trust most

On one manuscript I verified all 77 numbers the text pulls from the pipeline against the values the pipeline actually emits. Zero mismatches. That took an afternoon, and it is the only reason I can say the paper matches the code rather than hoping it does.

The uncomfortable part

Every bug above lived in code I had already reviewed, in projects I already considered finished. None of them changed a scientific conclusion. All of them would have become the reader's problem.

So the takeaway is not "be more careful". It is that reproducibility is a TEST, and an untested claim of reproducibility is just a claim. One command, empty cache directory, from raw. Run it before a reviewer does.

Mine failed the first time. On every single project I pointed it at.

If you have run this test on your own work, I would genuinely like to hear what broke. My guess is it rhymes with mine.

#Reproducibility #OpenScience #ResearchSoftware #MachineLearning #HPC #ScientificComputing
