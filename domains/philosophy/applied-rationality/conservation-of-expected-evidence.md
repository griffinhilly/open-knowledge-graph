---
id: conservation-of-expected-evidence
title: "Conservation of Expected Evidence"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: bayesian-thinking-in-practice
    type: hard
  - id: conditionalization-and-bayesian-updating
    type: soft
  - id: expected-value
    type: soft
builds-toward:
  - absence-of-evidence
  - calibration-training
tags: ["bayesian", "evidence", "probability", "rationality"]
stage: advanced
status: draft
---

## Core Idea

Before you observe evidence, your expected posterior probability must equal your prior probability — averaged over all possible observations, weighted by their likelihood. This means you cannot rationally expect to be convinced of something you do not already believe: if you expect the evidence to support hypothesis H, then you should already believe H more strongly. Conservation of expected evidence is a powerful diagnostic for motivated reasoning: if you expect to find evidence confirming your current belief no matter what happens, something has gone wrong with your reasoning. Genuine inquiry must admit the possibility that evidence will push you in either direction.

## How It's Best Learned

Work through a concrete example: before flipping a coin you suspect is biased, write down how each possible sequence of outcomes would update your belief. Verify that the probability-weighted average of all possible posteriors equals your prior. Then apply this to real beliefs: before reading a study, ask what results would update you in each direction and by how much.

## Common Misconceptions

- This does not mean evidence is useless — it means that before seeing evidence, you cannot predict which direction it will push you, though it will push you somewhere specific once observed.
- Conservation of expected evidence does not prevent you from seeking confirming evidence — it says your expectation of what you will find must be calibrated.

## Questions

```yaml
- question: "Before running a clinical trial, a researcher thinks: 'If the trial shows a positive effect, the methodology was probably flawed; if it shows no effect, it confirms my belief that the drug is ineffective.' Conservation of expected evidence implies that:"
  type: multiple-choice
  options:
    - "Her reasoning is fine — healthy skepticism about positive results is scientifically appropriate"
    - "Her reasoning is subtly broken — if she assigns near-zero update probability to positive results, her expected posterior cannot equal her prior probability"
    - "She should only conduct the trial if she has no prior belief about the outcome"
    - "The principle only applies when both outcomes have equal prior probability"
  answer: 1
  explanation: "Conservation of expected evidence requires that the probability-weighted average of your posteriors across all possible observations equals your current prior. If the researcher assigns near-zero weight to positive results pushing her belief upward, and full weight to negative results confirming her belief, the weighted average will be lower than her prior — which is a mathematical impossibility for correct Bayesian reasoning. The tell-tale sign of motivated reasoning is exactly this: you've pre-interpreted every possible outcome as confirming your current belief, which means you've effectively already decided the answer."

- question: "A student says: 'I'm going to look up what experts say about this question, but I'm sure it will confirm what I already think.' Conservation of expected evidence implies that:"
  type: multiple-choice
  options:
    - "The student's confidence is well-placed — expert consensus usually aligns with common-sense priors"
    - "If the student genuinely expects the expert evidence to confirm their belief, they should already have updated toward that conclusion before looking"
    - "The student should not look up the expert opinion since doing so will bias their reasoning"
    - "Looking specifically for confirming evidence violates the principle of conservation of expected evidence"
  answer: 1
  explanation: "This is the core operational implication of the principle: if you can predict before seeing evidence that it will push you in a specific direction, that expected update should already be incorporated into your current belief. 'I expect to find X' and 'I believe X more strongly' should be the same epistemic state. If the student genuinely expects experts to agree with them, they should have already raised their credence — not wait for the evidence to do what they've already predicted it will do."

- question: "If you genuinely don't know the outcome of a coin flip, then before flipping, the probability-weighted average of your posterior beliefs (after seeing heads vs. tails) must equal your current prior belief about the coin's bias."
  type: true-false
  answer: true
  explanation: "This is the direct mathematical content of conservation of expected evidence. Let P(H) be your prior and p(heads), p(tails) be the likelihoods. Then E[posterior] = p(heads)·P(H|heads) + p(tails)·P(H|tails) = P(H). This is a consequence of the law of total probability and is not optional for a coherent Bayesian reasoner. If your weighted average posterior would differ from your prior, your probabilities are internally inconsistent."

- question: "The principle 'absence of evidence is not evidence of absence' contradicts conservation of expected evidence, because the latter implies that failing to find evidence should leave your belief unchanged."
  type: true-false
  answer: false
  explanation: "These two claims do not contradict each other — in fact, conservation of expected evidence implies that absence of evidence IS evidence of absence (when the evidence was likely to be found if the hypothesis were true). Conservation of expected evidence says: if finding evidence would raise your credence, then NOT finding it must lower your credence by the compensating amount, to keep the weighted average at your prior. 'Absence of evidence is not evidence of absence' is only valid when absence was likely regardless of the hypothesis — when the evidence wouldn't be there either way."

- question: "How does conservation of expected evidence diagnose motivated reasoning? Give an example of a belief pattern that violates it."
  type: short-answer
  answer: "Conservation of expected evidence diagnoses motivated reasoning by checking whether a person's anticipated responses to different evidence outcomes are probability-weighted consistent with their prior. If someone's expected posterior (averaged over all possible observations) would differ from their prior, their updating procedure is not Bayesian — they are treating evidence asymmetrically. Example: a person who believes a controversial claim and says 'studies supporting it are rigorous; studies against it are methodologically flawed' is assigning near-zero update probability to disconfirming evidence. Since the weighted average of their posteriors cannot equal their prior under this scheme, they are not reasoning with genuine openness to evidence — they have pre-committed to the conclusion."
  explanation: "The practical diagnostic is to ask: before looking at the evidence, what would move you in each direction, and by how much? If you cannot identify any possible observation that would lower your credence — or if disconfirming evidence always gets reinterpreted as neutral — conservation of expected evidence is violated and motivated reasoning is the likely culprit."
```
