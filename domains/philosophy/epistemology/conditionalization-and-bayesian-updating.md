---
id: conditionalization-and-bayesian-updating
title: Conditionalization and Bayesian Updating
domain: philosophy
course: epistemology
prerequisites:
- id: credences-and-epistemic-probabilities
  type: hard
- id: probabilistic-computation
  type: soft
- id: probabilistic-reasoning
  type: soft
builds-toward:
- evidential-support-formalization
tags:
- bayesian-updating
- evidence
- learning
stage: advanced
status: draft
---

# Conditionalization and Bayesian Updating

## Core Idea
Conditionalization is the rule by which rational agents update credences in response to evidence: P_new(p) = P_old(p|e), where e is the agent's total evidence. The posterior probability of p given e equals the prior probability of p conditional on e. This rule ensures that repeated updating leads to convergence on the truth given enough evidence, and formalizes the intuition that learning should shift belief toward propositions consistent with observed evidence.

## Questions

```yaml
- question: "An agent assigns prior credences: P(rain) = 0.3, P(cloudy|rain) = 0.9, P(cloudy|no rain) = 0.2. She then observes that it is cloudy. What should her new credence in rain be?"
  type: multiple-choice
  options:
    - "0.9 — because it is almost always cloudy when it rains"
    - "0.3 — a single observation shouldn't change her prior"
    - "Approximately 0.66 — computed via Bayes' theorem as P_old(rain|cloudy)"
    - "0.27 — the joint probability P(rain ∧ cloudy)"
  answer: 2
  explanation: "Conditionalization says P_new(rain) = P_old(rain|cloudy). By Bayes' theorem: P(rain|cloudy) = P(cloudy|rain)·P(rain)/P(cloudy) = (0.9×0.3)/(0.9×0.3 + 0.2×0.7) = 0.27/0.41 ≈ 0.659. Option A confuses the likelihood P(cloudy|rain) with the posterior — the likelihood is an input to the update, not the result. Option B incorrectly treats the prior as fixed against evidence. Option D gives the joint probability, the numerator before normalizing — not the conditional."

- question: "Two agents disagree: P₁(H) = 0.1 and P₂(H) = 0.9. Both conditionalize faithfully on the same stream of shared evidence. What will happen to their credences over time?"
  type: multiple-choice
  options:
    - "Their posteriors will immediately agree after the first piece of evidence"
    - "Their posteriors will never converge because their priors are so far apart"
    - "Their posteriors will tend to converge as the amount of shared evidence grows"
    - "Conditionalization cannot be applied when agents have such different priors"
  answer: 2
  explanation: "The convergence property of Bayesian updating states that agents who start with different priors but observe the same evidence and conditionalize faithfully will converge in credence, given sufficient evidence. The convergence is asymptotic — not immediate (option A) and not impossible (option B). The exception: if either agent assigns prior probability exactly 0 to H, no amount of evidence can move that credence, since conditionalizing on any evidence always multiplies a zero prior by a finite likelihood ratio and returns zero."

- question: "Under conditionalization, if P(p | e) = P(p), then learning e with certainty leaves your credence in p unchanged."
  type: true-false
  answer: true
  explanation: "If P(p|e) = P(p), then p and e are probabilistically independent in the prior — knowing e tells you nothing new about p. The conditionalization rule sets P_new(p) = P_old(p|e) = P_old(p), so credence is unchanged. This is not a pathological case — it is the correct behavior. For example, learning that it rained in Tokyo should not change your credence that Shakespeare wrote Hamlet; they are independent, and rational updating reflects that."

- question: "The problem of old evidence shows that conditionalization is fundamentally flawed and should be abandoned as a model of rational belief updating."
  type: true-false
  answer: false
  explanation: "The problem of old evidence identifies a genuine scope limitation: if you already assign certainty to e (P(e) = 1), then conditionalizing on e leaves all credences unchanged — which seems wrong when you later realize e bears on a new hypothesis you just formulated. But most Bayesian epistemologists treat this as a problem requiring refinement or supplementation of the framework (e.g., counterfactual priors), not as a refutation. The conditionalization rule is well-supported as the correct update when you learn genuinely new information with certainty. The old evidence problem applies only in the specific case of hypothesis formation after the evidence is already known."

- question: "Explain the 'renormalization' picture of conditionalization: what does it mean to say you eliminate impossible worlds and redistribute probability mass?"
  type: short-answer
  answer: "Your prior is a probability distribution across all logically possible worlds — each world gets some credence that reflects how likely you think that world is actual. When you learn that e is true, you know you are not in any world where e is false, so you set those worlds' probabilities to zero (eliminate them). The remaining worlds — those where e holds — now sum to P(e) < 1, not 1. To restore a valid probability distribution summing to 1, you divide each remaining world's probability by P(e) (renormalize). After this operation, a world w gets probability P_old(w)/P(e) if e holds in w, and 0 otherwise. Your credence in any proposition p then equals the sum of these rescaled probabilities for worlds where p holds — which is exactly P_old(p|e), confirming that conditionalization is precisely this elimination-and-rescaling procedure."
```

## Explainer

You have learned that **credences** are degrees of belief — numbers between 0 and 1 representing how confident an agent is in a proposition. A credence of 1 is certainty, 0 is certainty of falsity, and 0.5 is maximum uncertainty. But credences are not static; rational agents receive evidence and must update their beliefs in light of it. The question is: what is the right rule for updating? Conditionalization provides a precise answer.

If your current credence in proposition *p* is P(p), and you then learn evidence *e* with certainty, your new credence in *p* should be P(p | e) — your old conditional probability of p given e. Formally: P_new(p) = P_old(p | e). This formula follows from the definition of conditional probability: P(p | e) = P(p ∧ e) / P(e). The numerator is the prior probability you assigned to worlds where both p and e are true; the denominator is the prior probability you assigned to e being true at all. The ratio tells you how much of e's prior probability-mass came from worlds where p also holds. If e is strongly correlated with p in your prior, then learning e raises your credence in p substantially.

The intuitive picture is illuminating. Imagine your beliefs as a probability distribution spread across many possible worlds. Before observing evidence, you distribute credence across those worlds according to your prior. When you learn that e is true, you eliminate all worlds where e is false and renormalize — redistributing the remaining probability mass proportionally among worlds where e holds. Propositions correlated with e become more credible; those anti-correlated become less credible. This is exactly what the conditionalization formula computes. The rule has a powerful **convergence property**: two rational agents who start with different priors but share evidence and conditionalize faithfully will, given enough evidence, converge on very similar credences. Evidence is the great leveler of disagreement. One important philosophical challenge is the **problem of old evidence**: conditionalization implies that learning something you already knew with certainty cannot change your beliefs. But it sometimes seems that recognizing old evidence bears on a new hypothesis should update you. This tension motivates ongoing Bayesian epistemology research into how to handle evidence and hypothesis formation in tandem.

