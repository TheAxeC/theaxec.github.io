---
layout: post
title:  "Prompts and Spells"
category: research
publish: True
date: 2026-10-26
---

A phrase added to a prompt can move a model's score by tens of points, and the effect belongs to the model and the questions it was measured on. A prompt is the text a user gives a language model, and the model is the trained program that answers it. In May 2022 Takeshi Kojima and colleagues [posted a paper](https://arxiv.org/abs/2205.11916) in which the phrase "Let's think step by step.", placed before the answer, raised the accuracy of the GPT-3 model text-davinci-002 on the MultiArith arithmetic problems from 17.7 to 78.7 percent.

The wording decided how much gain appeared. Of sixteen phrases tried on the same model and problems, "Let's think about this logically." scored 74.5 and "Abrakadabra!" 15.5, below the 17.7 of the question with no phrase. A phrase that asked for reasoning helped, and a nonsense word did not.

The comparison of a prompt with a spell holds in four documented ways. This post follows [post 1]({{ '/blog/ai-and-alchemy/' | relative_url }}), on AI as alchemy, and [post 2]({{ '/blog/ai-culture-and-magic/' | relative_url }}), on belief in magic among the people who build AI. The four ways are:

- A phrase can move a single answer by tens of points.
- Recipes circulate as texts, a recipe being a phrase or prompt text that is copied and handed on.
- The value of a recipe changes with the model version, the dated release of a model that a vendor serves.
- Results vary with the format of a prompt and with the model, which is variation of outcome, one of the two conditions of Malinowski's test for magic. The other condition is danger, and the post covers variation of outcome.

The comparison fails where the field averages over a whole benchmark, a fixed set of questions with known answers, and where automatic search for prompts, with a score for each candidate, has begun to replace the recipe.

## The marks of magic

Four marks of magic in Bronislaw Malinowski's essay [Magic, Science and Religion](https://archive.org/details/dli.ernet.476121), first published in 1925 and reprinted in 1948, have counterparts to look for in prompt practice. Post 2 introduced them, and in his words they are:

- the spell
- tradition, the handing on of magic
- the belief "that hope cannot fail nor desire deceive" (p. 67)
- the way failures are accounted for

Prompt practice uses the vocabulary of the spell, though the evidence here is one lecture title: Charles Frye called a 2023 bootcamp lecture [Learn to Spell](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/prompt-engineering/), which can also be read as a pun on spelling. For Malinowski's islanders "knowledge of magic means knowledge of spell" (p. 54).

Among the sources read, the one scholarly version of the claim that a prompt is a spell is an essay by Timothy de Waal Malefyt and Matt Artz in the [Journal of Business Anthropology](https://doi.org/10.22439/jba.v15i1.7813) of 2026. They compare the exact wording of a prompt with "the correctness of a spoken chant" and limit the magic to skill "rather than belief". Their evidence is two tools from Artz's own toolkit, and they score no model output, so the essay describes practice without measuring it.

Magic, for Malinowski, is handed on and changed on the way, and prompt recipes travel as texts copied with changes. The sentence that magic is "made by tradition" is, on page 3, his summary of Preuss, Marett, Hubert and Mauss. His own words are that magic is "handed over in direct filiation from generation to generation" (p. 68), and that "a magical formula is in reality constantly being re-shaped as it passes from one generation to another" ([Argonauts of the Western Pacific](https://www.gutenberg.org/ebooks/55822), 1922). The phrase "made by tradition" names the second mark, and the next paragraphs look for it in prompt practice.

Prompt recipes are collected and handed on in online prompt libraries. The prompt library now called [prompts.chat](https://github.com/f/prompts.chat), created as Awesome ChatGPT Prompts on 5 December 2022, had 174,545 stars, the bookmarks users give a project on GitHub, on 25 October 2026. Its README says that its prompts "work great with any modern AI assistant", a claim it does not test.

In the data of Shen and colleagues, a jailbreak prompt, a text written to make a model answer what it was trained to refuse, reached other sites in variant form within about a month. Xinyue Shen and colleagues [collected](https://arxiv.org/abs/2308.03825) 1,405 jailbreak prompts posted from December 2022 to December 2023. They scored the similarity of each pair of prompts by Levenshtein distance, the number of single-character edits that turn one text into the other, linked pairs with a similarity score above 0.5, and grouped the linked prompts into 131 communities with the Louvain algorithm, a method that finds densely connected groups. The first prompt of the "Do Anything Now" (DAN) community they call "Basic" was observed on r/ChatGPTPromptGenius on 8 January 2023, and its variants reached other subreddits and Discord about a month later, on 9 February.

Anthropic, one of the vendors, publishes its own prompts too. It posts the [system prompt](https://platform.claude.com/docs/en/release-notes/system-prompts/overview) of claude.ai, the text placed before every conversation, on one page per model, and the Claude Sonnet 3.5 page holds four versions dated from 12 July to 22 November 2024, so the system prompt of one model changed three times in about four months.

People have extracted and published the system prompts of AI assistants, as with Bing Chat. Kevin Liu, a Stanford student, got its prompt by a prompt injection, an input that overrides a model's instructions, asking it to "Ignore previous instructions" and to write out what is at the "beginning of the document above" ([Ars Technica](https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-spills-its-secrets-via-prompt-injection-attack/), 10 February 2023; [The Verge](https://www.theverge.com/23599441/microsoft-bing-ai-sydney-secret-rules), 14 February 2023). The Verge wrote that Microsoft, when asked, "confirmed that the secret rules are genuine". Caitlin Roulston of Microsoft said Sydney was an internal code name.

Studies measure how easily system prompts are extracted. Perez and Ribeiro (2022) [define](https://arxiv.org/abs/2211.09527) prompt leaking as printing part or all of the original prompt and name the motive "copying the prompt for a specific application". Zhang, Carlini and Ippolito (COLM 2024) [report](https://arxiv.org/abs/2307.06865) that for all eleven models over 50% of prompts could be approximately extracted, about 87% for GPT-3.5 and 86.0% for GPT-4.

Zhang, Carlini and Ippolito call earlier reports of extracted Bing Chat and GitHub Copilot Chat prompts anecdotal, since such efforts rarely have access to the actual prompt. The extraction rates mean, in my reading, that a system prompt can circulate outside its vendor, while the fidelity of a single leaked copy is rarely checked.

Public repositories collect the texts. On 26 October 2026 [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) had 70,224 stars, and its README calls its contents "The full verbatim system prompts"; the README of [jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) (14,978 stars) requires "sources that I can verify or reproducible prompts". Patsakis, Argyropoulos and Alepis write in a 2026 [paper on arXiv](https://arxiv.org/abs/2609.31575) that they "cannot verify their fidelity, completeness, or dating", but for five Anthropic prompts a mean of 76% of the published text appears inside the leaked file (38% to 94%), in files 6.6 times longer.

A repository adapts a system prompt: [KinetiNode/claude-fable-5-system-prompt-clean](https://github.com/KinetiNode/claude-fable-5-system-prompt-clean) is described as a "token-efficient version of the leaked ... system prompt" (a token is a word or piece of a word that a model reads as a unit), while its README calls the source "Anthropic's publicly available" prompt. It is not research and shows only that the practice exists. I found no study of whether prompt writers reuse leaked system prompt text in their own prompts; the overlap scores of Patsakis and colleagues "describe document relationships, not whether any organization copied from or collaborated with another".

My reading is that leaked and published prompts both circulate as texts, and the one repository I found that adapts such a prompt copies it with changes, which is what the mark of tradition describes.

Malinowski explains why failure never counts against magic: "the failures of magic can be always accounted for by the slip of memory, by slovenliness in performance or in observance of a taboo", or by "counter-magic" (p. 66). Prompt practice has wording close to the accounts that put the failure in the performer, the slip of memory and slovenliness in performance.

Advice from two sources places the cause of a failure in the person who wrote or used the prompt. Anthropic's [prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) asks the writer to show the prompt to a colleague, because "If they'd be confused, Claude will be too." Jim Nielsen [describes](https://blog.jim-nielsen.com/2026/skill-issue/) "skill issue" as a common reply to a failed prompt.

Prompt practice shows three of the four marks, the spell, tradition, and failure put on the performer. The advice to show a prompt to a colleague can also be read as plain advice on writing clearly, a reading that the guide's "If they'd be confused, Claude will be too." supports.

## Ritual where the outcome varies

Malinowski's test for where magic appears has two conditions, danger and variation of outcome, which he also calls "chance" ("Myth in Primitive Psychology", p. 116). In the Trobriand Islands, lagoon fishing by poison gave "abundant results without danger and uncertainty" and had no magic, while open-sea fishing, with danger and a yield that "greatly varies", had "extensive magical ritual" (p. 14). The passage joins danger and variation of outcome. House-building was "technically quite as difficult a pursuit, but involving neither danger, nor chance", and had no magic (["Myth in Primitive Psychology"](https://archive.org/details/dli.ernet.476121), p. 115), which separates technical difficulty from variation of outcome.

He gave magic a function: "The function of magic is to ritualize man's optimism, to enhance his faith in the victory of hope over fear" (p. 70). This connects to the mark "that hope cannot fail nor desire deceive". He ties the function of magic to the places where outcomes are uncertain, which is the condition of variation of outcome, so the paragraph bears on prompts through that condition. His evidence is an anthropologist's report and not a count.

B. F. Skinner [reported](https://psychclassics.yorku.ca/Skinner/Pigeon/) in 1948 on eight pigeons fed by a clock at regular intervals, and six showed responses "so clearly defined that two observers could agree perfectly in counting instances" (p. 168). He compared them to "Rituals for changing one's luck at cards" (p. 171). The pigeons were fed on a fixed timetable, so the link to variation of outcome is his analogy.

Two later abstracts describe the behaviour as a response to the periodic delivery of food. The abstract of [Staddon and Simmelhag](https://fds.duke.edu/db/aas/Biology/faculty/staddon/publications/288054) (1971) describes "interim activities" just after food delivery and "the terminal response" toward the end of the interval. The abstract of [Timberlake and Lucas](https://pmc.ncbi.nlm.nih.gov/articles/PMC1348192/) (1985) concludes that the behaviour "probably develops from components of species-typical patterns of appetitive behavior related to feeding", appetitive behaviour being behaviour directed toward food.

In the human studies read here, ritual goes with anxiety under conditions the person cannot control. Sosis and Handwerker [studied](https://doi.org/10.1111/j.1548-1433.2010.01305.x) 115 Israeli women during the 2006 Lebanon War, 33 who stayed in Tzfat, in northern Israel, and 82 who left. "Psalms had no effect on the anxiety of those who left Tzfat but had a significant effect on those who remained" (p. 47).

Two abstracts report the same link. [Keinan's](https://doi.org/10.1177/0146167202281009) (2002) abstract reports that in 108 participants, high stress widened the difference in knocks on wood between people high and low in desirability of control. [Lang and colleagues](https://doi.org/10.1016/j.cub.2015.05.049) (2015) report in their abstract that "induced anxiety led to an increase in repetitiveness and rigidity, but not redundancy" in spontaneous ritualized behavior.

For prompting, the sources report variation of outcome. [Sclar and colleagues](https://arxiv.org/abs/2310.11324) reported "up to 76 accuracy points" of difference after subtle changes in prompt formatting. [Battle and Gollapudi](https://arxiv.org/abs/2402.10949) tested 60 combinations of system message snippets and found in the abstract that "results do not universally generalize across models".

[Berry's](https://doi.org/10.1007/s00146-026-03093-8) 2026 article argues that prompt engineering "resembles the psychological and temporal structures that Walter Benjamin identified in gambling behaviour". Its abstract adds that "Analysis through LLMbench demonstrates that the uncertainty users experience corresponds to measurable variation in model confidence across the generated text", LLMbench being a tool the author built. The article is a humanities argument, and its abstract reports no study of how users write prompts.

Prompt writers describe outcomes as hard to predict, and one participant, P19, uses the language of magic. Inie and colleagues held [28 interviews](https://arxiv.org/abs/2311.06237) with "people purposefully generating adversarial content from LLMs", short for large language models, and P19 uses magic talk as "a trivial fun kind of layer" to "keep yourself honest". [Liang and colleagues](https://arxiv.org/abs/2409.12447) interviewed 20 developers who write prompts, and their abstract reports that prompt programmers "still struggle to develop reliable mental models".

The sources, in my reading, show variation of outcome in prompting, one of the two conditions of Malinowski's test. Danger, the other condition, goes unmeasured in them. In jailbreaks, agents (models that work on tasks by themselves) and production applications, the sources do not measure what a failed prompt costs. The comparison with the spell rests on variation of outcome and on the circulation of recipes.

I found no measured study of whether prompt writers respond to variation of outcome with ritual, such as fixed openers or polite phrases. Such a study would test whether the comparison extends from the condition to the response.

## Effects of a phrase

On a single question a phrase can decide the answer. Wharton's [Prompting Science Report 1](https://arxiv.org/abs/2503.04818) asked GPT-4o each of the 198 questions of GPQA Diamond, a benchmark of difficult science questions, 100 times per prompt.

Which phrase was better depended on the question. GPT-4o answered question 158 correctly 0.610 more often with "Please answer the following question." before it than with "I order you to answer the following question.", and on question 105 the "I order" phrase scored 0.633 higher. The authors call these differences uncorrected, meaning not adjusted for the number of comparisons made, and note that they "disappear when aggregating across all questions".

Changes of layout that keep the meaning can move a score as far, and the best layout differs between models. Melanie Sclar and colleagues [varied](https://arxiv.org/abs/2310.11324) separators, spaces and capitals across 53 tasks and reported "performance differences of up to 76 accuracy points when evaluated using LLaMA-2-13B". When one format beat another on one model, the order held on another model with a probability below 0.62, against 0.5 for chance, so the ranking of layouts carried over only weakly.

Averaged over all 198 questions, the two phrases of Report 1 differed little, since in the authors' words prompt variations "are dwarfed by overall model characteristics." A difference is significant when it is unlikely to be a chance result, which here means that its 95 percent confidence interval, given in brackets as the range that plausibly holds the true difference, excludes zero. Only the difference for GPT-4o-mini was significant, when a question counted as solved if 51 of its 100 trials were right: "I order" minus "Please" was -0.066 [-0.111, -0.020]. For GPT-4o it was 0.040 [-0.000, 0.081], the other direction.

Rudeness is the clearest exception among the studies read. Yin and colleagues [wrote prompts](https://arxiv.org/abs/2402.14531) at eight levels of politeness, and the rudest English one begins "Answer these question you scum bag!" At that level, whose prompt also carries a threat, Llama2-70B scored 28.44 on MMLU, a benchmark of 17,844 four-option multiple-choice questions in 57 tasks, against 55.26 at its best level. The paper attributes the difference to politeness and does not separate the insult from the rest of the wording.

Emotional appeals gave mixed results in the paper that proposed them. In 2023 Li and colleagues [reported](https://arxiv.org/abs/2307.11760) that "This is very important to my career." gave the best results on the Instruction Induction tasks, which were run zero-shot, without worked examples in the prompt. Averaged over their 11 appended phrases, GPT-4's score on those tasks fell from 80.75 to 78.96.

Wharton's [Report 3](https://arxiv.org/abs/2508.00614) tested "This is very important to my career!" in 2025 on five models, 25 trials per question, and found no significant gain for any of them and a loss of 0.040 [-0.065, -0.014] for Gemini 2.0 Flash on GPQA Diamond. The phrase that helped in one study gave no significant gain across five models in another.

Every significant difference from the baseline, the condition with no added phrase, on GPQA Diamond in Report 3 was a loss. Of the 40 comparisons of prompt conditions with the baseline, 8 conditions for each of 5 models, five were significant without correction, and all five lowered the score. This runs against a remark that the report attributes to Sergey Brin on the All-In podcast in May 2025, that "models tend to do better if you threaten them".

A tip raised the score of one model and lowered that of another. In Report 3, on 100 engineering questions from MMLU-Pro, a benchmark of multiple-choice questions with 10 options each, "I'll tip you a $1000 dollars if you answer this question correctly." lowered Gemini 1.5 Flash by 0.055 and raised Gemini 2.0 Flash by 0.053.

## Recipes and model versions

The value of a recipe changed with the model version in one task on two versions of one model, as Chen and colleagues [showed](https://arxiv.org/abs/2307.09009) by comparing the March 2023 and June 2023 versions of GPT-4 on deciding whether a number is prime. The chain-of-thought request, which asks for a written sequence of reasoning steps before the answer, added 24.4 points in March and 0.1 points in June.

Jailbreak prompts lost most of their success on a later version of ChatGPT, and altered copies regained much of it. Shen and colleagues ran their jailbreak prompts on three versions of ChatGPT, and their attack success rate is the share of forbidden questions the model answered rather than refused or only described. For the major communities it was 0.685 on 1 March 2023, 0.671 on 13 June and 0.103 on 6 November. Typos in 10 percent of the words of the best prompts raised the best rate on the November version from 0.477 to 0.857.

The gain from asking for chain of thought depends on the kind of model. Wharton's [Report 2](https://arxiv.org/abs/2506.07142) (2025) divided models into reasoning models, which engage in an initial reasoning process before answering, and non-reasoning models, which do not. Adding the chain-of-thought request "Think step by step" to a plain question raised GPQA Diamond accuracy by 0.062 for Gemini 2.0 Flash and 0.069 for GPT-4o, with no significant change for Sonnet 3.5 or GPT-4o-mini.

The authors of Report 2 attribute the modest gains to models that "perform some form of CoT reasoning even if not asked", CoT standing for chain of thought. For reasoning models the request gave "only marginal, if any, gains", and against a prompt asking for the answer alone Gemini Flash 2.5 lost 0.033.

Anthropic's prompting guide, which carries no date and was read on 25 October 2026, attaches model versions to its advice. Claude Opus 4.5 and Claude Opus 4.6 "are also more responsive to the system prompt than previous models", and "Where you might have said 'CRITICAL: You MUST use this tool when...,' you can use more normal prompting such as 'Use this tool when...' instead." Emphasis written for earlier versions can be, for these two, too strong.

Anthropic's page ties a measured result to one model version: it tells developers to treat a technique that names a model "as measured on that model and re-check it against your own evals before applying it to another". OpenAI's [evaluation guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices) defines evals as "structured tests for measuring a model's performance".

My reading is that a prompt recipe has the structure of the alchemical recipes of post 1: it works with an ingredient its writer does not know is there, the model version it was tried on. Post 1 cited a reconstruction by Principe, reported by [Anft (2011)](https://web.archive.org/web/2023/https://magazine.jhu.edu/2011/06/01/in-alchemys-defense/), of the glassy substance alchemists derived from antimony. It failed with antimony bought from a chemical company and worked with antimony ore from Eastern Europe, which contained about 0.5 percent quartz.

## Capital letters

Some recipes quoted below write instructions in capitals, as in "You MUST", and capitals change the text the model reads. A model reads text as tokens, the words and pieces of words its tokenizer cuts the text into. The tables of a 2026 preprint by Dillitzer and colleagues, [Attention is Case-Sensitive](https://arxiv.org/abs/2608.03711), show that LLaMA-3's tokenizer makes "running" one token and "RUNNING" two, and splits "UNBELIEVABLY" into six tokens and "unbelievably" into three.

In RoBERTa's standard tokenizer "other", "Other" and "OTHER" are three separate vocabulary entries, as Powalski and Stanislawek [showed](https://arxiv.org/abs/2010.11936) in 2020.

The test model of Powalski and Stanislawek was a RoBERTa-base model trained from scratch, that is starting from random weights, with a 32k tokenizer, one with a vocabulary of 32,000 entries.

In this one model, capitals lowered the score. Fine-tuned on each task of the GLUE benchmark, that is trained further on the task's own examples, it averaged 82.87 on the development sets, the held-out examples used for scoring, without the WNLI task, which the authors exclude as problematic. With the task text in capitals it averaged 77.19. The authors read this as a model trained mostly on normal casing handling capitals worse.

Capitals also moved a model's attention toward the text they marked, in one preprint covering 13 models. Attention is the set of weights by which a model mixes the tokens it has read when it produces the next one. Dillitzer and colleagues measured it. In Qwen2.5-7B-Instruct, writing a span in capitals with the rest of the input unchanged moved attention toward it by 2.06 percentage points, and alternating case by up to 2.77.

The span they changed was the correct answer inside the input, so accuracy gains such as LLaMA-3.1-8B rising from 29.59 to 44.39 on MMLU-Pro come from marking the answer. The authors manipulated the casing as a causal variable, so the shift of attention followed from the capitals. Whether that shift causes the change in accuracy is untested: they list causal mediation analysis, a test of whether one measured change causes another, as future work.

The capital-letters recipe has a published form, principle 9 of the 26 that Bsharat and colleagues [published](https://arxiv.org/abs/2312.16171) in December 2023: "Incorporate the following phrases: "Your task is" and "You MUST"." The paper tested the two phrases together, on 20 questions with one answer each judged by human raters, with no lowercase version, so its results belong to the pair as a whole.

OpenAI's [GPT-4.1 prompting guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide) advises against capitals and uses them in its own agent prompt. The guide, of April 2025 and now marked archived, says "It's generally not necessary to use all-caps or other incentives like bribes or tips." Its agent prompt, the instructions given to a model that works on tasks by itself, says "You MUST plan extensively before each function call", a function call being a request by the model to run a tool. The guide's advice and its own agent prompt, in my reading, point in opposite directions, so the guide does not settle what capitals do.

The guide credits three reminders of this kind, capitals and content together, with raising OpenAI's internal score "by close to 20%" on SWE-bench Verified, whose tasks ask a model to fix an issue from an open-source code repository.

Anthropic's guide gives "NEVER use ellipses" as the less effective form of an instruction and a version with the reason as the more effective one, because "Claude can generalize from the explanation." My reading is that the quoted contrast concerns the reason, so it leaves the effect of capitals alone untested.

For "MUST" against "must", the sources give two findings and one gap:

- In the tokenizers of two papers, capitals change the tokens of listed words such as "UNBELIEVABLY" and "OTHER", and "must" is not among them.
- Capitals on a span move attention toward it, in the 13 models of one preprint.
- These sources include no controlled variation of capitals inside an instruction that holds the rest fixed and measures whether an instruction-tuned model, one trained further to follow instructions, complies.

In the sources, the effect of capitals is documented for tokens and, in one preprint, for attention, and untested for instructions, which in my reading is variation of outcome measured piece by piece.

## Measurement

The field has begun to find prompts by automatic search, in which a model writes candidate prompts and a score picks among them. In [OPRO](https://arxiv.org/abs/2309.03409), Yang and colleagues let PaLM 2-L-IT, the instruction-tuned version of PaLM 2-L, write candidate prompts, scored on training questions answered by the pre-trained PaLM 2-L, a model trained only on text. At step 107 the search found "Take a deep breath and work on this problem step-by-step.", which scored 80.2 on the 1,319 questions of the GSM8K math test set against 71.8 for "Let's think step by step." The authors scored it only with PaLM 2-L and write that "the optimal prompt formats can be model-specific and task-specific".

Automatic search beat human-written instructions in [APE](https://arxiv.org/abs/2211.01910), the system of Zhou and colleagues. On InstructGPT the interquartile mean across 24 tasks, the mean of the middle half of the scores, was 0.810 against 0.749 for human instructions.

On a rhyming task the search found what the score rewarded. Four of the five instructions the search kept asked the model to echo the input word. They scored 0.99 to 1 on the zero-shot test, because "every word rhymes with itself", and so were selected.

In APE, the instructions the search found for InstructGPT "work best for the InstructGPT itself but do not transfer well".

Khattab and colleagues built [DSPy](https://arxiv.org/abs/2310.03714) to replace "lengthy strings discovered via trial and error" with programs, and compiled programs scored higher than a plain program. A DSPy pipeline is a chain of language-model calls, and compiling it lets DSPy collect the worked examples its prompts use so as to maximize a metric.

Compiling a program raised GPT-3.5's score on the GSM8K test set from 25.2 percent, with a plain program and no compilation, to 72.4 for a chain-of-thought program compiled with hand-written examples and 81.6 for the best compiled program. That program adds bootstrapped examples, example traces that the compiler collects by running the program on training inputs, and an ensemble, which runs several copies of the program and combines their predictions.

Testing a prompt means repeated trials on a fixed model version. The Wharton reports replace one run with 100 trials per question (Report 1) or 25 (Reports 2 and 3). OpenAI's evaluation guide lists "Vibe-based evals" among the practices to avoid, and its [prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering) recommends "Pinning your production applications to specific model snapshots".

Measuring a recipe has a dated precedent in chymistry, the early modern discipline of post 1, when weighing became the rule of an experiment. In 1789 Antoine Lavoisier wrote in the work translated as [Elements of Chemistry](https://www.gutenberg.org/ebooks/30775) that "nothing is created; an equal quantity of matter exists both before and after the experiment".

Lavoisier applied the rule to fermentation, a recipe "well known to every one". His tables account for "510 libs. of fermentable liquor" going in and every product coming out, and both sides balance at 510 libs. The experiments "were made only with a few pounds of sugar", and he scaled the results to "the quintal or imaginary hundred pounds" of sugar.

In Paris, on Principe's account, chrysopoeia, the search for gold, left the Académie through the professionalisation of chymistry. Principe's account has four points:

- Principe [finds](https://www.euchems.eu/wp-content/uploads/2015/08/03-Principe_.pdf) "no evidence that new theoretical structures or experiments dealt a death-blow to chrysopoeia".
- He suggests that it "fell at the hands of a movement intended to domesticate chymistry into a respectible professionalised discipline".
- He notes that John Law's bank collapse of 1720 and a rumour about the Regent gave the Académie's paper of 1722 on cheats a public-relations motive.
- He claims no single cause.

The prompt studies, in my reading, follow the weighing route of Lavoisier's tables. Those tables are a different route from the professionalisation Principe describes: they account for the weight of everything that went in and came out. Wharton's trials, OPRO, APE, DSPy and vendor evals count a prompt's effect run by run on a fixed model version.

How an eval scores answers can change its result as much as a phrase can. In Report 1, removing an instruction about the answer format lowered GPT-4o's score by 0.086 [0.040, 0.136] when a question counted as solved only if all 100 trials were right, and by 0.015 (p=0.590, the probability of a difference at least that large if the instruction had no effect) at the 51 percent threshold. Report 1 draws the lesson that "how we measure performance greatly influences our interpretations of LLM capabilities".

Grader prompts, which ask one model to score another model's output, are sensitive to wording in the same way as any prompt, so they need the same checking. Shankar and colleagues [state](https://arxiv.org/abs/2404.12272) in their introduction, citing Sclar and colleagues, that such prompts "are unintuitively sensitive to seemingly minor changes in wording or structure". From think-aloud sessions, in which participants speak their thoughts while working, with nine practitioners they concluded that "it is impossible to completely determine evaluation criteria prior to human judging of LLM outputs".

## Conclusion

On the documented evidence, in my reading, a prompt shows three of the four marks of magic and the condition of variation of outcome, and the sources do not show the belief that hope cannot fail.

In the Wharton reports, averaging over a benchmark leaves few effects of a phrase. On GPQA Diamond, Report 3 found five significant effects in 40 comparisons of threats, tips and appeals with the baseline, and all five were losses. Report 1 found over the whole benchmark one significant difference between a polite and a commanding phrase, for one model at one threshold.

Results that vary with prompt format (Sclar and colleagues) and with the model (Battle and Gollapudi) show the condition of variation of outcome in Malinowski's test. Whether prompt writers answer it with ritual is untested in the sources read.

A phrase that worked on your question is evidence about that question and that model version, and weak evidence about other questions and versions. A winning layout kept its rank on another model with a probability below 0.62, against 0.5 for chance. In Report 2 the chain-of-thought request helped two of four non-reasoning models and gave reasoning models "only marginal, if any, gains".

The sources point to one practice:

- Keep a set of your own questions.
- Run each prompt on each question 25 to 100 times (the Wharton reports used 100 in Report 1 and 25 in Reports 2 and 3).
- Anthropic advises writing the plain instruction with its reason.
- OpenAI advises pinning the model version; run the set again when it changes, which Mollick, in a [post of November 2025](https://www.oneusefulthing.org/p/giving-your-ai-a-job-interview), expects "multiple times a year".

## References

- Anft, M., "In alchemy's defense", Johns Hopkins Magazine, 1 June 2011. https://web.archive.org/web/2023/https://magazine.jhu.edu/2011/06/01/in-alchemys-defense/
- Anthropic, "Prompting best practices", undated, read on 25 October 2026. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, "System prompts", release notes, undated, read on 25 October 2026. https://platform.claude.com/docs/en/release-notes/system-prompts/overview
- asgeirtj/system_prompts_leaks, GitHub repository, created 2025, read on 26 October 2026. https://github.com/asgeirtj/system_prompts_leaks
- Battle, R. and Gollapudi, T., "The Unreasonable Effectiveness of Eccentric Automatic Prompts", arXiv 2402.10949, 2024. https://arxiv.org/abs/2402.10949
- Berry, D. M., "Prompt anxiety and the algorithmic politics of uncertainty", AI and Society 41, 2026. https://doi.org/10.1007/s00146-026-03093-8
- Bsharat, S. M., Myrzakhan, A. and Shen, Z., "Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4", arXiv 2312.16171, 2023. https://arxiv.org/abs/2312.16171
- Chen, L., Zaharia, M. and Zou, J., "How Is ChatGPT's Behavior Changing over Time?", arXiv 2307.09009, 2023. https://arxiv.org/abs/2307.09009
- Dillitzer, Sohn, Corso and Auerbach, "Attention is Case-Sensitive", arXiv 2608.03711, preprint, 2026. https://arxiv.org/abs/2608.03711
- Edwards, B., "AI-powered Bing Chat spills its secrets via prompt injection attack [Updated]", Ars Technica, 10 February 2023, read on 26 October 2026. https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-spills-its-secrets-via-prompt-injection-attack/
- f/prompts.chat (formerly Awesome ChatGPT Prompts), GitHub repository, created 2022, read on 25 October 2026. https://github.com/f/prompts.chat
- Frye, C., "Learn to Spell: Prompt Engineering", Full Stack Deep Learning LLM Bootcamp, 9 May 2023. https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/prompt-engineering/
- Inie, N., Stray, J. and Derczynski, L., "Summon a Demon and Bind It: A Grounded Theory of LLM Red Teaming", arXiv 2311.06237. https://arxiv.org/abs/2311.06237
- jujumilk3/leaked-system-prompts, GitHub repository, created 2023, read on 26 October 2026. https://github.com/jujumilk3/leaked-system-prompts
- Keinan, G., "The Effects of Stress and Desire for Control on Superstitious Behavior", Personality and Social Psychology Bulletin 28: 102-108, 2002. https://doi.org/10.1177/0146167202281009
- Khattab and others, "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines", arXiv 2310.03714, 2023. https://arxiv.org/abs/2310.03714
- KinetiNode/claude-fable-5-system-prompt-clean, GitHub repository, created 2026, read on 26 October 2026. https://github.com/KinetiNode/claude-fable-5-system-prompt-clean
- Kojima, T., Gu, S. S., Reid, M., Matsuo, Y. and Iwasawa, Y., "Large Language Models are Zero-Shot Reasoners", arXiv 2205.11916, NeurIPS 2022. https://arxiv.org/abs/2205.11916
- Lang, M., Krátký, J., Shaver, J. H., Jerotijević, D. and Xygalatas, D., "Effects of Anxiety on Spontaneous Ritualized Behavior", Current Biology 25(14): 1892-1897, 2015. https://doi.org/10.1016/j.cub.2015.05.049
- Lavoisier, A., Elements of Chemistry, trans. R. Kerr, Edinburgh, 1790 (Paris, 1789), Project Gutenberg #30775. https://www.gutenberg.org/ebooks/30775
- Li and others, "Large Language Models Understand and Can Be Enhanced by Emotional Stimuli", arXiv 2307.11760, 2023. https://arxiv.org/abs/2307.11760
- Liang, J. T., Lin, M., Rao, N. and Myers, B., "Prompts Are Programs Too! Understanding How Developers Build Software Containing Prompts", Proceedings of the ACM on Software Engineering 2(FSE), 2025, arXiv 2409.12447. https://arxiv.org/abs/2409.12447
- Malefyt, T. de W. and Artz, M., "The Magical Power of Words in Large Language Models: Prompt Engineering as Ritual Magic", Journal of Business Anthropology 15(1), 2026. https://doi.org/10.22439/jba.v15i1.7813
- Malinowski, B., Argonauts of the Western Pacific, 1922, Project Gutenberg #55822. https://www.gutenberg.org/ebooks/55822
- Malinowski, B., "Magic, Science and Religion", in Magic, Science and Religion and Other Essays, 1948. https://archive.org/details/dli.ernet.476121
- Malinowski, B., "Myth in Primitive Psychology", in Magic, Science and Religion and Other Essays, 1948. https://archive.org/details/dli.ernet.476121
- Meincke, Mollick, E., Mollick, L. and Shapiro, "Prompting Science Report 1: Prompt Engineering is Complicated and Contingent", arXiv 2503.04818, 2025. https://arxiv.org/abs/2503.04818
- Meincke, Mollick, E., Mollick, L. and Shapiro, "Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting", arXiv 2506.07142, 2025. https://arxiv.org/abs/2506.07142
- Meincke, Mollick, E., Mollick, L. and Shapiro, "Prompting Science Report 3: I'll pay you or I'll kill you, but will you care?", arXiv 2508.00614, 2025. https://arxiv.org/abs/2508.00614
- Mollick, E., "Giving your AI a Job Interview", One Useful Thing, 12 November 2025. https://www.oneusefulthing.org/p/giving-your-ai-a-job-interview
- Nielsen, J., "That's a Skill Issue", 12 April 2026. https://blog.jim-nielsen.com/2026/skill-issue/
- OpenAI, "Evaluation best practices", undated, read on 25 October 2026. https://developers.openai.com/api/docs/guides/evaluation-best-practices
- OpenAI, "GPT-4.1 Prompting Guide", OpenAI cookbook, 2025, marked archived. https://cookbook.openai.com/examples/gpt4-1_prompting_guide
- OpenAI, "Prompt engineering", undated, read on 25 October 2026. https://developers.openai.com/api/docs/guides/prompt-engineering
- Patsakis, C., Argyropoulos, V. and Alepis, E., "Configuration, Not Conscience: A Large-Scale Empirical Study of LLM System Prompts", arXiv 2609.31575, 2026. https://arxiv.org/abs/2609.31575
- Perez, F. and Ribeiro, I., "Ignore Previous Prompt: Attack Techniques For Language Models", arXiv 2211.09527, 2022. https://arxiv.org/abs/2211.09527
- Powalski, R. and Stanislawek, T., "UniCase: Rethinking Casing in Language Models", arXiv 2010.11936, 2020. https://arxiv.org/abs/2010.11936
- Principe, L. M., "Transmuting Chymistry into Chemistry: Eighteenth-Century Chrysopoeia and Its Repudiation", plenary lecture, 6th International Conference on the History of Chemistry (EuCheMS), pp. 21-32. https://www.euchems.eu/wp-content/uploads/2015/08/03-Principe_.pdf
- Sclar, M., Choi, Y., Tsvetkov, Y. and Suhr, A., "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting", ICLR 2024, arXiv 2310.11324. https://arxiv.org/abs/2310.11324
- Shankar, Zamfirescu-Pereira, Hartmann, Parameswaran and Arawjo, "Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences", arXiv 2404.12272, 2024. https://arxiv.org/abs/2404.12272
- Shen, X., Chen, Z., Backes, M., Shen, Y. and Zhang, Y., "'Do Anything Now': Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models", ACM CCS 2024, arXiv 2308.03825. https://arxiv.org/abs/2308.03825
- Skinner, B. F., "'Superstition' in the pigeon", Journal of Experimental Psychology 38(2): 168-172, 1948. https://psychclassics.yorku.ca/Skinner/Pigeon/
- Sosis, R. and Handwerker, W. P., "Psalms and Coping with Uncertainty: Religious Israeli Women's Responses to the 2006 Lebanon War", American Anthropologist 113(1): 40-55, 2011. https://doi.org/10.1111/j.1548-1433.2010.01305.x
- Staddon, J. E. R. and Simmelhag, V. L., "The 'superstition' experiment: A reexamination of its implications for the principles of adaptive behavior", Psychological Review 78(1): 3-43, 1971. https://fds.duke.edu/db/aas/Biology/faculty/staddon/publications/288054
- Timberlake, W. and Lucas, G. A., "The basis of superstitious behavior: chance contingency, stimulus substitution, or appetitive behavior?", Journal of the Experimental Analysis of Behavior 44(3): 279-299, 1985. https://pmc.ncbi.nlm.nih.gov/articles/PMC1348192/
- Warren, T., "These are Microsoft's Bing AI secret rules and why it says it's named Sydney", The Verge, 14 February 2023, read on 26 October 2026. https://www.theverge.com/23599441/microsoft-bing-ai-sydney-secret-rules
- Yang, C. and others, "Large Language Models as Optimizers", arXiv 2309.03409, ICLR 2024. https://arxiv.org/abs/2309.03409
- Yin, Wang, Horio, Kawahara and Sekine, "Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance", arXiv 2402.14531, 2024. https://arxiv.org/abs/2402.14531
- Zhang, Y., Carlini, N. and Ippolito, D., "Effective Prompt Extraction from Language Models", COLM 2024, arXiv 2307.06865. https://arxiv.org/abs/2307.06865
- Zhou and others, "Large Language Models Are Human-Level Prompt Engineers", arXiv 2211.01910, ICLR 2023. https://arxiv.org/abs/2211.01910
