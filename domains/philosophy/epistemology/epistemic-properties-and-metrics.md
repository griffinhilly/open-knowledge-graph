---
id: epistemic-properties-and-metrics
title: Epistemic Properties and Metrics
domain: philosophy
course: epistemology
prerequisites:
- id: formal-epistemology-introduction
  type: hard
tags:
- properties
- measurement
- coherence
- reliability
stage: formal-systems
status: draft
---

# Epistemic Properties and Metrics

## Core Idea
Formal epistemology quantifies epistemic properties: coherence as a measure of mutual support among beliefs, reliability as the frequency of true outputs, epistemic utility as a function mapping belief-states to numbers, informativeness as variance in posterior distributions. These metrics enable precise comparison of theories and discovery of trade-offs. For instance, maximizing coherence may lower reliability; balancing these trade-offs requires explicit utility functions.

## Explainer

From your introduction to formal epistemology, you are already comfortable using probability theory to represent degrees of belief and Bayesian updating to revise beliefs in response to evidence. Now we are extending that framework to ask a more evaluative question: not just "how should I update?" but "how good is my epistemic state, and how can we measure it?"

**Coherence** is the first major metric. Intuitively, a coherent set of beliefs mutually support each other — believing P is more plausible given the rest of your beliefs than it would be in isolation. Formal measures of coherence (such as Shogenji's measure or Olsson's average pairwise confirmation) capture this as ratios of joint probabilities to products of individual probabilities. A perfectly incoherent set of beliefs is one where each belief is independent of all the others; a highly coherent set is one where each belief raises the probability of the others. Coherence is attractive as an epistemic goal because it reflects a kind of internal rationality — your beliefs fit together. But here is the first trade-off: a body of beliefs can be highly coherent while being systematically false. A conspiracy theory can be remarkably coherent while being disconnected from reality.

This is where **reliability** enters as a competing metric. A belief-forming process is reliable if it tends to produce true beliefs — its track record of accuracy is high. A highly coherent but unreliable system (think: a very internally consistent but empirically false worldview) fails the reliability test. Conversely, a reliable process might produce individual beliefs that don't hang together neatly. The tension between coherentist and reliabilist ideals is not merely theoretical — it maps onto the practical question of whether to trust a source that is consistent but unchecked versus one that is accurate but unsystematic.

**Epistemic utility functions** generalize this further. A utility function assigns a numerical score to any belief-state — not just "true" or "false" but a graded measure of how good the state is, combining accuracy, calibration, and informativeness. The most widely studied class is **strictly proper scoring rules**: scoring rules where the strategy that maximizes expected utility is always to report your true credences, not to hedge or overstate confidence. The **Brier score** and **logarithmic scoring rule** are examples. These tools matter because they make it possible to formally compare epistemic theories — if theory A consistently achieves higher expected utility than theory B under a proper scoring rule, that is a precise argument in its favor. The trade-off structure becomes explicit: **informativeness** (a tightly peaked posterior that commits to a specific prediction) and **calibration** (being right at the stated confidence level) can pull in opposite directions, and epistemic utility functions let us quantify exactly how to balance them.


