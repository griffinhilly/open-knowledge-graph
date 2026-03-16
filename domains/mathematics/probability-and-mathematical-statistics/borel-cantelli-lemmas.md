---
id: borel-cantelli-lemmas
title: Borel-Cantelli Lemmas
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: independence-sigma-algebras
  type: hard
- id: probability-spaces-measure-theoretic
  type: hard
builds-toward:
- almost-sure-convergence
- strong-law-of-large-numbers
tags:
- limit-theorems
- convergence
- probability
stage: advanced
status: draft
---

# Borel-Cantelli Lemmas

## Core Idea
If {Aₙ} are events with Σ P(Aₙ) < ∞, then P(lim sup Aₙ) = 0 (first Borel-Cantelli lemma). Conversely, if {Aₙ} are independent with Σ P(Aₙ) = ∞, then P(lim sup Aₙ) = 1 (second Borel-Cantelli lemma). These lemmas control the tail behavior of event sequences and are crucial for proving almost sure convergence.

## Explainer

From your work on measure-theoretic probability spaces, you know that infinite sequences of events have well-defined limiting behavior. The expression **lim sup Aₙ** — read "A_n infinitely often" or abbreviated "A_n i.o." — is the event that infinitely many of the A_n occur. Formally it is ∩_{N=1}^∞ ∪_{n=N}^∞ Aₙ: an outcome ω is in lim sup Aₙ if for every N, there is some n ≥ N with ω ∈ Aₙ. Think of A_n as "a rare event happens on trial n." The lim sup is the event that this keeps happening forever — the sequence never fully stops.

The **first Borel-Cantelli lemma** says: if Σ P(Aₙ) < ∞, then P(lim sup Aₙ) = 0. No independence assumption is needed. The proof is direct: for any ε > 0, choose N large enough that Σ_{n>N} P(Aₙ) < ε. The probability that at least one A_n with n > N occurs is at most Σ_{n>N} P(Aₙ) < ε by the union bound. The set where infinitely many A_n occur is contained in this tail for every N, and the probabilities go to zero. Sending ε → 0 yields measure zero. This lemma captures a simple intuition: if the total expected number of occurrences is finite, then almost surely only finitely many can happen.

The **second Borel-Cantelli lemma** requires independence and reverses the conclusion: if the Aₙ are independent and Σ P(Aₙ) = ∞, then P(lim sup Aₙ) = 1. Independence is genuinely necessary — without it, the conclusion can fail. The proof uses the bound 1 − x ≤ e^{−x}: the probability that none of Aₙ₊₁, …, Aₙ₊ₖ occur is ∏(1 − P(Aₙ)) ≤ exp(−Σ P(Aₙ)), which tends to 0 as k → ∞ whenever the partial sums diverge. So A_n must occur infinitely often with probability 1. Together, the two lemmas give a sharp dichotomy: convergent sum → eventually stops almost surely; divergent sum plus independence → recurs infinitely often almost surely.

These lemmas are the standard tool for proving almost sure convergence results, including the strong law of large numbers. In practice, to prove that some "bad event" happens only finitely often almost surely, you define Aₙ as the event that the bad thing occurs on trial n, compute P(Aₙ) (often something like 1/n²), show the series converges, and invoke the first lemma. To prove that something recurs forever almost surely, you exhibit independence and a divergent sum and invoke the second. The lemmas translate an analytic question (does Σ P(Aₙ) converge?) into a probability statement (does the event recur infinitely often?) — a clean bridge between series analysis and probabilistic behavior.
