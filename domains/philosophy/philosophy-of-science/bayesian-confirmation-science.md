---
id: bayesian-confirmation-science
title: Bayesian Approaches to Confirmation
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: bayesian-epistemology
  type: hard
- id: confirmation-theory-science
  type: hard
- id: probabilistic-reasoning
  type: hard
- id: probabilistic-computation
  type: soft
- id: bayesian-confirmation-and-evidence
  type: soft
builds-toward:
- scientific-realism
- causal-explanation-science
tags:
- bayesian
- probability
- likelihood
- posterior
stage: advanced
status: draft
---

# Bayesian Approaches to Confirmation

## Core Idea
Bayesian confirmation theory applies Bayes' theorem to understand how evidence confirms or disconfirms hypotheses. Your degree of belief in a hypothesis should be updated by evidence using P(H|E) = P(E|H) × P(H) / P(E). Evidence confirms H if it is more likely given H than given its negation. Bayesian approaches provide a mathematically rigorous account of rational belief revision and offer responses to problems of induction and underdetermination.

## Explainer

From your study of **Bayesian epistemology**, you know that beliefs can be represented as degrees of credence — real numbers between 0 and 1 — and that rational agents update them by conditionalization: when you learn E, your new credence in H becomes P(H|E), your prior conditional probability. Bayesian confirmation theory applies this framework specifically to the scientific context, asking: when does evidence *confirm* a hypothesis, and by how much? The answer is elegantly simple: evidence E **confirms** hypothesis H if and only if P(H|E) > P(H) — that is, learning E raises your credence in H above where it started.

Expanding via Bayes' theorem — P(H|E) = P(E|H) × P(H) / P(E) — makes the structure visible. The key term is **P(E|H)**, the **likelihood**: how probable would the evidence be if H were true? A high likelihood means the hypothesis predicts the evidence well, so observing it strongly supports H. Compare this to **P(E|¬H)**, the probability of the evidence if H is false. The ratio P(E|H)/P(E|¬H) is the **Bayes factor**, measuring the evidence's force. If a hypothesis predicts the evidence far better than its competitors, the evidence is strong confirmation. If both H and ¬H predict E equally, E is neutral — this is why trivially predictable results are weak evidence.

This framework handles several problems that troubled earlier confirmation theories. The **raven paradox** (from your confirmation theory study) noted that classical accounts made it mysterious why observing a green apple could confirm "all ravens are black." Bayesianism dissolves this: observing a non-black non-raven does confirm the hypothesis, but only infinitesimally — because such observations are almost equally likely whether the hypothesis is true or false. The Bayes factor is barely above 1. The paradox arose from treating confirmation as binary; Bayesianism restores the quantitative difference between weak and strong confirmation.

The most contested element is the **prior**: P(H) before any evidence. Bayesians are divided between **objectivists**, who think there are uniquely rational priors determined by logic or symmetry, and **subjectivists**, who accept that priors vary among agents and is acceptable so long as updating is rational. The subjectivist position raises a worry: if two scientists begin with very different priors, will they ever converge on the same hypothesis? The good news is that, under mild conditions, Bayesian agents who share evidence will eventually converge regardless of starting priors — evidence eventually overwhelms the prior. This makes Bayesianism a strong response to **underdetermination**: even if data alone cannot force a unique theory, iterative Bayesian updating across a scientific community tends toward agreement.

The framework also illuminates **old evidence** problems. If E was observed before H was proposed, then P(E) ≈ 1, making the update trivial — E cannot raise P(H) because E is already certain. Yet intuitively, explaining long-known phenomena is genuine confirmation (Einstein's general relativity explaining Mercury's perihelion advance). Addressing this requires treating confirmation as what P(E|H) tells us relative to the theoretical alternatives available, not just the raw update. These subtleties show that while Bayesianism gives the most mathematically precise theory of confirmation in science, applying it to real scientific practice requires careful handling of priors, likelihoods, and the background context in which evidence is acquired.
