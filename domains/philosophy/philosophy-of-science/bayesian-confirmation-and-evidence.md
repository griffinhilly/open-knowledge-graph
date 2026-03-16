---
id: bayesian-confirmation-and-evidence
title: Bayesian Confirmation Theory
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: bayesian-epistemology
  type: hard
- id: probabilistic-reasoning
  type: soft
builds-toward:
- theoretical-virtues-in-theory-choice
tags:
- confirmation
- bayesian
- evidence
stage: advanced
status: draft
---

# Bayesian Confirmation Theory

## Core Idea
Bayesian confirmation theory treats evidential support probabilistically: evidence confirms a hypothesis when observing it raises the hypothesis's probability. This formalizes the intuitive idea that evidence must be more likely given the theory than it would be otherwise, providing a quantitative measure of confirmation.

## How It's Best Learned
Learn Bayes' theorem and apply it to simple scientific examples. Study how it handles problems like old evidence and the ravens paradox that troubled earlier confirmation theories.

## Explainer

You already know Bayes' theorem from your study of Bayesian epistemology: P(H|E) = P(E|H) × P(H) / P(E). Bayesian confirmation theory applies this machinery to the philosophy of science. The central claim is simple: **evidence E confirms hypothesis H** if observing E raises the probability of H — formally, if P(H|E) > P(H). Evidence that leaves H's probability unchanged is irrelevant, and evidence that lowers H's probability disconfirms it. This gives us a quantitative framework for the qualitative intuition that data should update our confidence in theories.

The key ratio that drives confirmation is P(E|H) / P(E|¬H) — the **likelihood ratio**. Evidence confirms H strongly when it is much more likely if H is true than if H is false. If you observe a raven and it is black, this confirms the hypothesis "all ravens are black" — but only weakly, because black ravens are common anyway. If you observe a raven and it is *white*, this strongly disconfirms the hypothesis, because the hypothesis makes white ravens strictly impossible while the alternative does not. The asymmetry between confirmation and disconfirmation here reflects a real structural feature: a single counterexample defeats a universal claim decisively, while confirming instances raise the probability by only a small amount.

Bayesian confirmation handles several puzzles that troubled earlier theories. The **ravens paradox** (Hempel's paradox): "All ravens are black" is logically equivalent to "All non-black things are non-ravens," which seems to be confirmed by observing a green apple. Bayesian analysis shows this is technically correct — a green apple does raise the probability of "all ravens are black" — but only infinitesimally, because the sample space of non-black things is enormous. The Bayesian framework dissolves the paradox by showing the confirmation is real but negligible. The **problem of old evidence** is harder: if you already know E with certainty (P(E) = 1), then E cannot raise the probability of H because the math yields P(H|E) = P(H). Bayesians address this by imagining a counterfactual prior probability before learning E, though this remains contested.

The philosophical significance of Bayesian confirmation is that it grounds scientific rationality in the mathematics of probability. Scientific reasoning is not a mysterious faculty — it is Bayes' theorem applied to theories and evidence. Each observation updates your credences by a definite amount. Theories with high prior probability (from simplicity, coherence with known science, etc.) require less confirming evidence; theories that make bold predictions require that those predictions come true to earn high probability. The framework also clarifies what it means to have evidence *for* a theory at all: evidence is only evidence relative to alternatives. Data that confirms one hypothesis always implicitly compares it to competing hypotheses through the denominator P(E).
