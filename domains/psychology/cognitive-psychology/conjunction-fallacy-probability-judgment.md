---
id: conjunction-fallacy-probability-judgment
title: Conjunction Fallacy and Probability Judgment Errors
domain: psychology
course: cognitive-psychology
prerequisites:
- id: heuristics-and-judgment
  type: hard
- id: reasoning-biases-and-errors
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- base-rate-integration-probability
tags:
- probability
- judgment
- fallacy
- logic
stage: formal-systems
status: draft
---

# Conjunction Fallacy and Probability Judgment Errors

## Core Idea
People often judge the probability of a conjunction (A and B) as higher than one of its constituents (A alone), violating probability axioms where P(A and B) ≤ P(A). This conjunction fallacy is especially pronounced when the conjunction is vivid, narrative, or representative of a stereotyped group (e.g., a person described as having feminist interests being rated as more likely to be a feminist bank teller than simply a bank teller). The fallacy reflects substitution of representativeness—how well the description matches the category—for probability.

## How It's Best Learned
Present the classic Linda problem and variations, showing persistent conjunction fallacy even with explicit instructions. Demonstrate how relative likelihood judgments (ordinal comparisons) avoid the fallacy while probability judgments do not.

## Common Misconceptions
- Assuming the fallacy reflects mathematical ignorance; even trained statisticians show it on realistic scenarios.
- Treating representativeness and probability as independent; when narrative details make a conjunction more representative, the fallacy emerges.

## Explainer

From your prerequisites in heuristics and reasoning biases, you understand that human judgment uses mental shortcuts that are fast and often useful but systematically fail in predictable ways. The **conjunction fallacy** is perhaps the cleanest demonstration of this failure: people judge the probability of a conjunction (A and B) to be *higher* than the probability of one of its components (A alone) — which is logically impossible, since any conjunction is a subset of each of its components.

The classic demonstration is the **Linda problem** (Tversky & Kahneman, 1983). Linda is described as 31 years old, bright, outspoken, and deeply concerned with social justice — she majored in philosophy and participated in antinuclear demonstrations. Participants are asked: which is more probable — that Linda is a bank teller, or that Linda is a feminist bank teller? The majority rate the conjunction (feminist bank teller) as more likely. From your probability axioms prerequisite, you can see why this is a mathematical impossibility: every feminist bank teller is also a bank teller, so the set of feminist bank tellers is a strict subset of bank tellers. P(feminist bank teller) ≤ P(bank teller) by the axiom that the probability of an intersection cannot exceed the probability of either component.

The fallacy occurs because participants are not computing probabilities — they are evaluating **representativeness**, a heuristic that asks "how well does this description match this category?" The feminist bank teller is more *representative* of Linda's description than the bank teller alone, so it *feels* more probable. This is **heuristic substitution**: the mind replaces a hard question (what is the probability?) with an easier one (how well does this match?) and uses the answer to the easy question as its response to the hard one. The substitution is automatic and remarkably persistent — it occurs even when the mathematical error is pointed out, and even in trained statisticians encountering realistic vignettes where the narrative pull of representativeness is strong.

The broader lesson is that the conjunction fallacy is not a statistical mistake driven by ignorance of the rules. It reflects a deep feature of how human cognition is organized: we are **narrative thinkers** who evaluate coherence and fit, not frequency-counting machines that naturally track base rates. Adding vivid details to a description makes a scenario feel *more* probable and credible, not less — even though every additional detail mathematically constrains (reduces) the probability of the conjunction. This is why con artists, political rhetoric, and legal arguments exploit rich detail: a vivid, coherent account feels more believable than a sparse accurate one. Understanding this fallacy is understanding a core tension between narrative cognition and statistical reasoning that pervades judgment under uncertainty.
