---
id: no-false-lemmas-condition
title: The No False Lemmas Condition
domain: philosophy
course: epistemology
prerequisites:
- id: gettier-cases-formal-analysis
  type: hard
builds-toward:
- defeasibility-conditions-knowledge
tags:
- gettier
- responses
- knowledge
- false-lemmas
stage: formal-systems
status: draft
---

# The No False Lemmas Condition

## Core Idea
The no false lemmas condition, developed by Lehrer and others, proposes that knowledge requires not only justified true belief but also that the belief not be based on any false lemmas or false intermediate steps. This condition aims to eliminate Gettier cases by excluding inferences that depend crucially on falsehoods, even if those falsehoods don't directly appear in the justification.

## Explainer

From your formal analysis of Gettier cases, you know the problem: there are situations where a person has a true, justified belief that nonetheless seems not to count as knowledge, because the route from justification to truth runs through luck. The challenge is to identify exactly what extra ingredient knowledge requires beyond JTB. The **no false lemmas condition** is one of the earliest and most intuitive proposals: knowledge fails whenever the inferential path from justification to belief passes through a false intermediate step, even if the final belief is true.

Consider the canonical Gettier-style case. Smith justifiably believes "Jones owns a Ford" (perhaps Jones drives one, has always owned one, etc.). From this, Smith infers "Either Jones owns a Ford, or Brown is in Barcelona" — a true disjunction, formed by adding a random second disjunct. As it happens, Jones does not own a Ford, but Brown genuinely is in Barcelona. So Smith has a justified true belief in the disjunction, but it seems wrong to say he *knows* it. The no false lemmas diagnosis: Smith's inference ran through the false lemma "Jones owns a Ford." Because that lemma is false, the epistemic connection between Smith's justification and the true conclusion is broken — the truth of the conclusion is accidental relative to his evidence.

The condition can be stated formally: S knows that p if and only if (i) p is true, (ii) S believes that p, (iii) S is justified in believing p, and (iv) S's justification does not essentially depend on any **false lemma** — that is, there is no false proposition q such that S's belief that p is inferred (explicitly or implicitly) from q. Condition (iv) is the addition. It targets the structure of inferential chains: even if the final product is true, if the chain passed through a falsehood, the inference is epistemically tainted.

The condition handles many Gettier cases cleanly and has a strong intuitive motivation: falsehoods in an inference are like forged links in a chain — the chain still holds the weight, but by luck rather than by its actual structure. However, the condition runs into **counterexamples from the other direction**. Some Gettier cases appear not to involve any false lemma: perception-based cases where you form a belief directly from a reliable perceptual process, without any inferential chain at all, can still generate Gettier-like luck. If you perceive a barn while driving through a region full of convincing barn facades (and you happen to be looking at the one real barn), your perceptual belief has no inferential lemmas — yet many philosophers judge it not to count as knowledge. No false lemmas cannot diagnose this case, because there are no lemmas at all.

This limitation motivates the move to **defeasibility conditions** — the next development in this line of thought. Instead of asking whether the inferential chain contains falsehoods, defeasibility approaches ask whether the justification would survive the addition of true information. The no false lemmas condition is, in effect, a special case of defeasibility: a false lemma is one salient way a justification can be defeated. But not all defeaters are false lemmas, and tracking that fuller space of potential defeaters requires a more general framework.
