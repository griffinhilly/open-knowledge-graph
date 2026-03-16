---
id: neuroeconomics-value-computation
title: Neuroeconomics and Value Computation
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: reward-dopamine-systems
  type: hard
- id: executive-control-networks
  type: soft
- id: expected-value-theory
  type: hard
- id: constrained-optimization
  type: soft
builds-toward:
- decision-making-neural-mechanisms
tags:
- decision-making
- value
- economics
stage: advanced
status: draft
---

# Neuroeconomics and Value Computation

## Core Idea
The brain computes subjective values—the desirability of options adjusted for personal preferences and probability—in ventromedial prefrontal cortex. This common currency representation allows comparing options across domains. Decision-making integrates value signals with temporal discounting (striatum), risk evaluation (insula), and goal representation (lateral prefrontal cortex). Neural value signals predict economic choices, while value computation failures in addiction and psychiatric illness explain maladaptive decisions.

## Explainer

From your expected-value theory prerequisite, you know the normative account of decision-making: the rational agent multiplies the probability of each outcome by its utility and chooses the option with the highest expected value. Real people deviate from this in systematic ways — they are risk-averse for gains, risk-seeking for losses (Kahneman and Tversky's prospect theory), they overweight immediate rewards relative to delayed ones, and they sometimes make inconsistent choices across framings. Neuroeconomics asks a different question: what are the *neural computations* that produce these choices, rational and irrational alike?

The central discovery of neuroeconomics is that the brain maintains a **common currency for value** — a single neural representation that allows comparing options across radically different domains (food, money, social approval, pain relief) on a single scale. This value signal is encoded in the **ventromedial prefrontal cortex (vmPFC)**. When participants in fMRI studies make choices between different types of rewards, vmPFC activity correlates with the *subjective value* of the chosen option — and this correlation predicts which option will be chosen even before a decision is consciously reported. The vmPFC does not encode objective reward magnitude; it encodes a personalized, experience-weighted utility that incorporates preference, satiety, and context. Without a common currency, the brain could not compare apples to oranges; vmPFC makes that comparison possible.

Your dopamine prerequisite is directly relevant here. Dopamine neurons in the ventral tegmental area (VTA) and substantia nigra signal **reward prediction errors** — the difference between expected and received reward. When a reward arrives unexpectedly, dopamine firing increases (positive prediction error); when an expected reward is omitted, dopamine firing decreases (negative prediction error). This prediction error signal is the learning signal that updates value representations in the striatum. The **striatum** (particularly the nucleus accumbens and ventral striatum) stores learned value associations and is heavily implicated in **temporal discounting** — the tendency to devalue delayed rewards. Striatal activity during anticipation of future rewards decreases with delay, which is part of why immediate rewards feel disproportionately compelling. Dysfunction in this system — either through abnormal dopamine signaling (as in addiction) or blunted value representation across all options (as in depression's anhedonia) — directly disrupts the quality of decision-making.

Risk and uncertainty add another layer. The **insula**, which processes interoceptive states and visceral emotional responses, is activated by risky choices and appears to represent the aversive uncertainty of unknown outcomes — its activity predicts risk aversion and contributes to loss aversion. The **lateral prefrontal cortex (lPFC)**, meanwhile, represents goal states and integrates value signals with longer-term plans, supporting the capacity to override immediate value signals in service of future goals. Decision-making is thus not a single computation but a competition between systems: the value-learning striatum and vmPFC signaling "this is desirable now," the insula signaling "this is risky and aversive," and lPFC representing "this does or does not fit my goals." **Self-control** in this framework is lPFC successfully modulating striatal/vmPFC signals — and failures of self-control in addiction are partially understood as pathological overvaluation of immediate reward coupled with a weakened top-down regulatory signal.
