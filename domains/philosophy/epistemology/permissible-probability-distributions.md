---
id: permissible-probability-distributions
title: Permissible Probability Distributions
domain: philosophy
course: epistemology
prerequisites:
- id: credences-and-epistemic-probabilities
  type: hard
- id: probabilistic-reasoning
  type: soft
builds-toward:
- bayesian-epistemology
tags:
- rationality-constraints
- probability-assignments
- prior-belief
stage: advanced
status: draft
---

# Permissible Probability Distributions

## Core Idea
The Bayesian requires that degrees of belief obey the probability axioms (non-negativity, normalization, additivity). But which probability distributions are rationally permissible? Some epistemologists require all credences to be equal (maximum entropy); others allow any prior satisfying the axioms (subjective Bayesianism). Still others impose additional constraints: principle of indifference for equivalent cases, updating by conditionalization, or domination (avoiding strictly dominated strategies). These constraints formalize the idea that some belief-states are rationally better than others.

## Questions

```yaml
- question: "An agent assigns credence 0.95 to 'the next flip of this coin will land heads' with no reason to believe the coin is biased. Their credences are coherent (they sum to 1 and satisfy the axioms). A subjective Bayesian says this prior is permissible; an objective Bayesian disagrees. What is the objective Bayesian's objection?"
  type: multiple-choice
  options:
    - "The credences violate the normalization axiom, since 0.95 + 0.05 ≠ 1 under the correct reckoning"
    - "The credences are coherent but violate the principle of indifference, which requires equal probabilities when there is no evidence favoring one outcome"
    - "The credences are incoherent because Dutch book arguments apply whenever any credence exceeds 0.5"
    - "Credences about future events are never permissible because future states are not yet part of the evidence"
  answer: 1
  explanation: "The objective Bayesian holds that in cases of symmetrical ignorance — no reason to favor heads over tails — the principle of indifference mandates assigning equal probabilities (0.5 each). Assigning 0.95/0.05 is coherent in the technical sense (satisfies the axioms and cannot be Dutch-booked) but violates the additional rationality constraint that ignorance should be represented by equal distributions. This is precisely the debate: subjective Bayesians say any coherent prior is permissible; objective Bayesians say some coherent priors are nonetheless irrational."

- question: "The principle of indifference and the maximum entropy principle both face which major philosophical challenge?"
  type: multiple-choice
  options:
    - "They violate the probability axioms, making them logically self-defeating"
    - "They require knowing the actual truth before assigning priors, creating circularity"
    - "They yield different probability assignments depending on how the possibility space is partitioned or described (Bertrand's paradox)"
    - "They are equivalent to subjective Bayesianism and add no genuinely new constraints"
  answer: 2
  explanation: "Bertrand's paradox demonstrates the problem: if you are ignorant about a random chord in a circle, should you uniformize over chord endpoints, chord midpoints, or chord lengths? Each partition gives a different 'ignorance prior' for whether the chord is longer than the inscribed triangle's side. The principle of indifference and maximum entropy both depend on a choice of parameterization that is not fixed by the evidence alone — the 'ignorance' they encode is relative to a description, not absolute."

- question: "According to subjective Bayesianism, an agent who assigns credence 0.99 to 'the moon is made of cheese' is irrational, because this violates the principle of indifference."
  type: true-false
  answer: false
  explanation: "Subjective Bayesianism imposes only two rationality requirements: (1) credences must satisfy the probability axioms (coherence), and (2) agents must update by conditionalization when new evidence arrives. Any prior satisfying the axioms is permissible — including bizarre ones like 0.99 on a cheese moon. The principle of indifference is an objective Bayesian constraint that subjective Bayesians reject. From the subjective view, what makes an agent irrational is not a wrong starting point but incorrect updating."

- question: "An agent whose credences satisfy the probability axioms (coherence) cannot be made to accept a set of bets that guarantees a net loss."
  type: true-false
  answer: true
  explanation: "This is the Dutch book theorem: coherence (satisfying the probability axioms) is necessary and sufficient to avoid Dutch books. An agent with incoherent credences can always be offered a combination of individually acceptable bets that guarantee a loss. Conversely, a coherent agent has no such vulnerability. This is the primary Bayesian argument for why the probability axioms are rationality requirements — not just convenient mathematics."

- question: "Why do subjective Bayesians hold that different people can rationally start with different priors, and what constraint does rationality actually impose on them?"
  type: short-answer
  answer: "Subjective Bayesians argue that rationality is procedural, not about correct starting points. Any prior that satisfies the probability axioms is permissible. The constraint rationality imposes is on updating: when evidence E arrives, agents must update by conditionalization — the posterior probability of hypothesis H is proportional to the prior times the likelihood of E given H. Given enough evidence, agents who began with different (but coherent) priors will converge toward the same posteriors. Rationality lives in the method of updating, not in the initial distribution."
  explanation: "This view prioritizes convergence under evidence: diverse priors are fine because good evidence eventually washes them out. Critics (objective Bayesians) argue that 'enough evidence' may never arrive, making the starting point matter practically even if it doesn't matter in the limit."
```

## Explainer

You already know that **credences** — degrees of belief — must satisfy the probability axioms to be coherent: they must be non-negative, they must sum to 1 across mutually exclusive and exhaustive possibilities, and they must respect the additivity rule for disjunctions. Satisfying these axioms rules out incoherence: an agent with incoherent credences can be Dutch-booked (offered a set of bets they accept individually but that guarantee a loss). But the axioms alone place very weak constraints on what you believe before any evidence arrives. You could assign credence 0.99 to "the moon is made of cheese" and credence 0.01 to the negation, and while this is bizarre, it is technically **coherent** — it satisfies the axioms. The question of *permissible prior distributions* asks: is any coherent prior rationally acceptable, or does rationality impose additional constraints on where you start?

**Subjective Bayesianism** gives the most permissive answer: any prior satisfying the probability axioms is permissible. What rationality requires is not a specific starting point but a specific *method of updating* — **conditionalization** (updating on evidence E by multiplying each prior probability by the likelihood of E given that hypothesis and renormalizing). Given enough evidence, agents with different priors will converge toward the same posterior, regardless of where they started. This view prioritizes procedural rationality: rationality is about updating correctly, not having the "right" initial beliefs.

**Objective Bayesianism** imposes stronger constraints, arguing that certain priors are rationally mandated by the evidence situation before any data arrives. The **principle of indifference** says: when you have no evidence favoring any outcome over any other, assign equal probabilities. If you're about to roll a die and have no reason to think it's biased, assign 1/6 to each face. The **maximum entropy principle** generalizes this: from among all distributions consistent with your constraints, choose the one with the highest entropy (the most spread out, least committal distribution). Both principles attempt to formalize "ignorance" as a rational state, encoding the intuition that you should not believe something without reason. But both generate famous paradoxes: the principle of indifference gives different answers depending on how you partition the possibility space (Bertrand's paradox), and maximum entropy can yield counterintuitive results when the problem is described differently.

A third constraint, **dominance**, forbids adopting a credence function that is *strictly dominated* — meaning there exists an alternative distribution that is guaranteed to do better no matter what the world turns out to be. This is weaker than maximum entropy but rules out obviously irrational priors like assigning probability 0 to a proposition that will certainly be true (if you already know this). Together, these constraints map a spectrum from the maximally permissive (anything coherent goes) to the maximally constrained (there is a unique rationally required prior for each evidence situation). Most working epistemologists occupy positions somewhere in between, accepting some additional constraints beyond bare coherence while resisting the strong uniqueness claims of full objective Bayesianism.
