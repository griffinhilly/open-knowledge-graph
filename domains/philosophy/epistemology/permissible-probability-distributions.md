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
stage: formal-systems
status: draft
---

# Permissible Probability Distributions

## Core Idea
The Bayesian requires that degrees of belief obey the probability axioms (non-negativity, normalization, additivity). But which probability distributions are rationally permissible? Some epistemologists require all credences to be equal (maximum entropy); others allow any prior satisfying the axioms (subjective Bayesianism). Still others impose additional constraints: principle of indifference for equivalent cases, updating by conditionalization, or domination (avoiding strictly dominated strategies). These constraints formalize the idea that some belief-states are rationally better than others.

## Explainer

You already know that **credences** — degrees of belief — must satisfy the probability axioms to be coherent: they must be non-negative, they must sum to 1 across mutually exclusive and exhaustive possibilities, and they must respect the additivity rule for disjunctions. Satisfying these axioms rules out incoherence: an agent with incoherent credences can be Dutch-booked (offered a set of bets they accept individually but that guarantee a loss). But the axioms alone place very weak constraints on what you believe before any evidence arrives. You could assign credence 0.99 to "the moon is made of cheese" and credence 0.01 to the negation, and while this is bizarre, it is technically **coherent** — it satisfies the axioms. The question of *permissible prior distributions* asks: is any coherent prior rationally acceptable, or does rationality impose additional constraints on where you start?

**Subjective Bayesianism** gives the most permissive answer: any prior satisfying the probability axioms is permissible. What rationality requires is not a specific starting point but a specific *method of updating* — **conditionalization** (updating on evidence E by multiplying each prior probability by the likelihood of E given that hypothesis and renormalizing). Given enough evidence, agents with different priors will converge toward the same posterior, regardless of where they started. This view prioritizes procedural rationality: rationality is about updating correctly, not having the "right" initial beliefs.

**Objective Bayesianism** imposes stronger constraints, arguing that certain priors are rationally mandated by the evidence situation before any data arrives. The **principle of indifference** says: when you have no evidence favoring any outcome over any other, assign equal probabilities. If you're about to roll a die and have no reason to think it's biased, assign 1/6 to each face. The **maximum entropy principle** generalizes this: from among all distributions consistent with your constraints, choose the one with the highest entropy (the most spread out, least committal distribution). Both principles attempt to formalize "ignorance" as a rational state, encoding the intuition that you should not believe something without reason. But both generate famous paradoxes: the principle of indifference gives different answers depending on how you partition the possibility space (Bertrand's paradox), and maximum entropy can yield counterintuitive results when the problem is described differently.

A third constraint, **dominance**, forbids adopting a credence function that is *strictly dominated* — meaning there exists an alternative distribution that is guaranteed to do better no matter what the world turns out to be. This is weaker than maximum entropy but rules out obviously irrational priors like assigning probability 0 to a proposition that will certainly be true (if you already know this). Together, these constraints map a spectrum from the maximally permissive (anything coherent goes) to the maximally constrained (there is a unique rationally required prior for each evidence situation). Most working epistemologists occupy positions somewhere in between, accepting some additional constraints beyond bare coherence while resisting the strong uniqueness claims of full objective Bayesianism.
