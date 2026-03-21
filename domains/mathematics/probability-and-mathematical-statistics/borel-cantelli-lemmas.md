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

## Questions

```yaml
- question: "Events A_n are independent and satisfy P(A_n) = 1/n for all n ≥ 1. What does the Borel-Cantelli theory predict about how often these events occur?"
  type: multiple-choice
  options:
    - "P(lim sup A_n) = 0, because each individual probability P(A_n) → 0"
    - "P(lim sup A_n) = 1/2, by the law of large numbers"
    - "P(lim sup A_n) = 1, because the A_n are independent and Σ P(A_n) = Σ 1/n diverges"
    - "P(lim sup A_n) cannot be determined without knowing the sample space"
  answer: 2
  explanation: "This is precisely the setup for the second Borel-Cantelli lemma: independence plus divergent sum. Even though P(A_n) → 0, the sum Σ 1/n is the harmonic series and diverges. With independence, the second lemma guarantees P(lim sup A_n) = 1 — the events occur infinitely often with probability 1. The common mistake is thinking that because individual probabilities go to zero, the events must eventually stop. The divergent sum overrides that intuition."

- question: "Events A_n are defined such that P(A_n) = 1/n, but they are NOT independent. What can be concluded about P(lim sup A_n)?"
  type: multiple-choice
  options:
    - "P(lim sup A_n) = 1, because the sum Σ P(A_n) diverges"
    - "P(lim sup A_n) = 0, because independence fails"
    - "The second Borel-Cantelli lemma does not apply; P(lim sup A_n) could be anywhere in [0, 1]"
    - "P(lim sup A_n) = 1/2, by symmetry of the non-independence"
  answer: 2
  explanation: "Independence is genuinely required by the second Borel-Cantelli lemma — it is not just a technical nicety. Without independence, a divergent sum does not guarantee P(lim sup A_n) = 1. For example, if all A_n are the same event (say, a coin lands heads), then P(A_n) = 1/2, the sum diverges, but P(lim sup A_n) = 1/2, not 1. The proof of the second lemma relies on the product structure that independence provides."

- question: "If Σ P(A_n) diverges and the events A_n are independent, then P(lim sup A_n) = 1, regardless of any other properties of the sequence."
  type: true-false
  answer: true
  explanation: "This is exactly the second Borel-Cantelli lemma. Independence plus a divergent sum is sufficient to guarantee that the lim sup has probability 1 — meaning the events recur infinitely often almost surely. The key conditions are independence and divergence of the sum; no other assumptions about the events are needed."

- question: "If Σ P(A_n) diverges, then P(lim sup A_n) = 1 regardless of whether the events are independent."
  type: true-false
  answer: false
  explanation: "This is the most common mistake when applying Borel-Cantelli. The second lemma requires independence — a divergent sum alone is not enough. Without independence, you cannot use the exponential product bound that drives the proof. There exist explicit counterexamples where Σ P(A_n) = ∞ but P(lim sup A_n) = 0 (e.g., if A_n = A for all n with P(A) > 0 but less than 1, the sum diverges yet the lim sup equals A, not the whole space). The first lemma (convergent sum → probability 0) needs no independence; the second does."

- question: "Explain why the independence assumption is essential for the second Borel-Cantelli lemma but is not needed for the first."
  type: short-answer
  answer: "The first lemma follows purely from the union bound (subadditivity of probability) and the assumption that series tail sums go to zero — no independence is needed. The second lemma requires independence because its proof multiplies individual non-occurrence probabilities across trials: P(none of A_{n+1},...,A_{n+k} occur) = ∏(1 − P(A_i)), which requires independence. This product is then bounded by exp(−Σ P(A_i)) → 0 when the sum diverges. Without independence, you cannot factor the joint probability this way, and the argument collapses."
  explanation: "Independence is a statement about the joint probability structure: it allows you to factor P(∩ A_i^c) = ∏ P(A_i^c). The exponential bound 1 − x ≤ e^{−x} then lets you show the probability of avoiding all events in a tail goes to zero. The first lemma is purely about marginal probabilities and their sum — subadditivity works event-by-event without needing to know how events relate to each other. This asymmetry is fundamental: ruling something out (first lemma) is easier than guaranteeing recurrence (second lemma)."
```

## Explainer

From your work on measure-theoretic probability spaces, you know that infinite sequences of events have well-defined limiting behavior. The expression **lim sup Aₙ** — read "A_n infinitely often" or abbreviated "A_n i.o." — is the event that infinitely many of the A_n occur. Formally it is ∩_{N=1}^∞ ∪_{n=N}^∞ Aₙ: an outcome ω is in lim sup Aₙ if for every N, there is some n ≥ N with ω ∈ Aₙ. Think of A_n as "a rare event happens on trial n." The lim sup is the event that this keeps happening forever — the sequence never fully stops.

The **first Borel-Cantelli lemma** says: if Σ P(Aₙ) < ∞, then P(lim sup Aₙ) = 0. No independence assumption is needed. The proof is direct: for any ε > 0, choose N large enough that Σ_{n>N} P(Aₙ) < ε. The probability that at least one A_n with n > N occurs is at most Σ_{n>N} P(Aₙ) < ε by the union bound. The set where infinitely many A_n occur is contained in this tail for every N, and the probabilities go to zero. Sending ε → 0 yields measure zero. This lemma captures a simple intuition: if the total expected number of occurrences is finite, then almost surely only finitely many can happen.

The **second Borel-Cantelli lemma** requires independence and reverses the conclusion: if the Aₙ are independent and Σ P(Aₙ) = ∞, then P(lim sup Aₙ) = 1. Independence is genuinely necessary — without it, the conclusion can fail. The proof uses the bound 1 − x ≤ e^{−x}: the probability that none of Aₙ₊₁, …, Aₙ₊ₖ occur is ∏(1 − P(Aₙ)) ≤ exp(−Σ P(Aₙ)), which tends to 0 as k → ∞ whenever the partial sums diverge. So A_n must occur infinitely often with probability 1. Together, the two lemmas give a sharp dichotomy: convergent sum → eventually stops almost surely; divergent sum plus independence → recurs infinitely often almost surely.

These lemmas are the standard tool for proving almost sure convergence results, including the strong law of large numbers. In practice, to prove that some "bad event" happens only finitely often almost surely, you define Aₙ as the event that the bad thing occurs on trial n, compute P(Aₙ) (often something like 1/n²), show the series converges, and invoke the first lemma. To prove that something recurs forever almost surely, you exhibit independence and a divergent sum and invoke the second. The lemmas translate an analytic question (does Σ P(Aₙ) converge?) into a probability statement (does the event recur infinitely often?) — a clean bridge between series analysis and probabilistic behavior.
