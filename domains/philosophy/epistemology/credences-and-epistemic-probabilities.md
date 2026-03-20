---
id: credences-and-epistemic-probabilities
title: Credences and Epistemic Probabilities
domain: philosophy
course: epistemology
prerequisites:
- id: what-is-knowledge
  type: soft
- id: probabilistic-reasoning
  type: soft
- id: probabilistic-computation
  type: soft
builds-toward:
- conditionalization-and-bayesian-updating
- evidential-support-formalization
- permissible-probability-distributions
tags:
- degrees-of-belief
- probability
- bayesian
stage: advanced
status: draft
---

# Credences and Epistemic Probabilities

## Core Idea
A credence is a numerical degree of belief: a real number between 0 and 1 representing how strongly an agent believes a proposition. Rather than all-or-nothing knowledge and belief, credences model rational partial belief and uncertainty. They are subject to coherence constraints (probability axioms): P(p) ≥ 0, P(tautology) = 1, and P(p ∨ q) = P(p) + P(q) when p and q are incompatible.

## Explainer

From your study of knowledge and probabilistic reasoning, you already have two familiar frameworks for thinking about belief. The epistemological tradition treats belief as binary: you either believe something or you don't, and knowledge adds justification and truth to that belief. The mathematical tradition of probability theory treats uncertainty quantitatively. Credence theory is the proposal that we should combine these frameworks — that belief itself admits of degrees, and that rationality constrains what those degrees can be.

The core insight is that ordinary language already implicitly uses degrees of belief. When you say "I'm pretty sure it will rain," "I doubt she'll arrive on time," or "I'm certain this is correct," you're not just reporting a binary attitude — you're reporting something more like a probability estimate. **Credences** make this precise: your credence in a proposition is a number from 0 (complete disbelief) to 1 (complete certainty). A credence of 0.9 in "it will rain tomorrow" means you believe it quite strongly but not with certainty. A credence of 0.5 is genuine uncertainty, equivalent to a coin flip.

What makes credence theory epistemically interesting — and not merely descriptive — is that credences are subject to rational constraints. These constraints are exactly the **probability axioms** you know from probabilistic reasoning. A tautology must receive credence 1 (you can't rationally be uncertain about something necessarily true). The credences of mutually exclusive possibilities must sum to at most 1. Most importantly, your credence in a disjunction P(A or B) = P(A) + P(B) when A and B can't both be true. A rational agent whose credences violate these axioms is **incoherent** — they can be shown to accept a series of bets that guarantee a loss regardless of what happens, a result called a **Dutch Book**. Coherence is the minimum rationality requirement; it's the credence analog of logical consistency.

The move from binary belief to credences has far-reaching consequences. Questions in epistemology that seemed simple become more nuanced: Does justification come in degrees? Can you know something you're not certain of? How should you update your credences when you get new evidence? Credences build toward **Bayesian updating**, which gives a precise rule (Bayes' theorem) for how rational credences should change in light of evidence. This framework has become central not just to philosophy but to statistics, artificial intelligence, and decision theory — anywhere that rational reasoning under uncertainty is needed.
