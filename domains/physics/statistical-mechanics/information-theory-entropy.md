---
id: information-theory-entropy
title: Information Theory and Entropy
domain: physics
course: statistical-mechanics
prerequisites:
- id: entropy-intro
  type: hard
- id: probability-axioms
  type: hard
tags:
- information
- entropy
- statistical-foundations
stage: advanced
status: draft
---

# Information Theory and Entropy

## Core Idea
Shannon entropy S = −k Σ p_i ln p_i quantifies the information content of a probability distribution {p_i}. It is maximized when the distribution is uniform. Statistical mechanical entropy is the Shannon entropy of the microstate distribution; the second law reflects the tendency toward maximum entropy (maximum ignorance consistent with constraints). This connection unifies thermodynamic and information-theoretic entropy.

## Explainer

You already know thermodynamic entropy from its macroscopic definition (dS = δQ_rev/T) and its statistical mechanical interpretation via Boltzmann's formula S = k ln Ω, where Ω counts accessible microstates. The information-theoretic approach, due to Claude Shannon, takes a different starting point: given a probability distribution over outcomes, how much uncertainty does it describe? The answer is the **Shannon entropy** H = −Σ p_i log p_i (using natural logs and writing S = kH to match thermodynamic units). This formula can be derived from first principles by asking what function of a probability distribution correctly captures "uncertainty" — the answer is unique up to a constant.

To build intuition, consider two extreme cases. If one outcome has probability 1 and all others have probability 0, then H = 0: there is no uncertainty, and knowing the distribution tells you exactly what will happen. If all N outcomes are equally likely (p_i = 1/N for all i), then H = ln N — the uncertainty is maximized and equals Boltzmann's formula S = k ln Ω when Ω = N. The Shannon entropy is a maximum when ignorance is maximal (uniform distribution) and zero when knowledge is complete. It measures not the outcomes themselves but how much information is required to specify them.

The connection to statistical mechanics is deep. In the microcanonical ensemble, all microstates are equally likely, so S = k ln Ω is exactly the Shannon entropy of that distribution — consistent with both formulas. In the canonical ensemble, the Boltzmann distribution p_i = e^{−βE_i}/Z is not uniform, but computing −k Σ p_i ln p_i returns the thermodynamic entropy S = (U − F)/T, which is again consistent. This is not a coincidence: **Jaynes' maximum entropy principle** states that the correct statistical mechanical ensemble is the one that maximizes Shannon entropy subject to whatever macroscopic constraints you impose. Microcanonical → fix energy; canonical → fix mean energy; grand canonical → fix mean energy and particle number. Each ensemble arises from entropy maximization with different Lagrange constraints.

The unification has a profound implication for the second law. "Entropy increases" is not merely a statement about heat flow — it is a statement about information loss. When a gas expands into a vacuum, the number of accessible microstates grows, and our knowledge of which microstate the system occupies decreases. Entropy measures our ignorance. The second law, reread in information-theoretic terms, says that isolated systems evolve toward states of maximum uncertainty — not because nature "wants" disorder, but because there are vastly more high-entropy microstates than low-entropy ones, so random evolution almost surely increases Ω. The arrow of time is the direction in which our knowledge of the microstate decreases.


