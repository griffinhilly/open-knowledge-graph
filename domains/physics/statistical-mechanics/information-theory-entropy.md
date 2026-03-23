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
stage: expert
status: validated
---

# Information Theory and Entropy

## Core Idea
Shannon entropy S = −k Σ p_i ln p_i quantifies the information content of a probability distribution {p_i}. It is maximized when the distribution is uniform. Statistical mechanical entropy is the Shannon entropy of the microstate distribution; the second law reflects the tendency toward maximum entropy (maximum ignorance consistent with constraints). This connection unifies thermodynamic and information-theoretic entropy.

## Questions

```yaml
- question: "A system has 100 possible microstates. A measurement reveals with certainty that it is in microstate #47. What is the Shannon entropy of this distribution?"
  type: multiple-choice
  options:
    - "ln 100 — because there are 100 possible states in the system"
    - "1/100 — the probability of any one state in the uniform distribution"
    - "0 — complete knowledge of the microstate means zero uncertainty"
    - "100 × (1/100) × ln 100 = ln 100 — by summing over all states"
  answer: 2
  explanation: "If the system is certainly in microstate #47, then p₄₇ = 1 and all other pᵢ = 0. Shannon entropy H = −Σ pᵢ ln pᵢ = −(1 × ln 1) − (99 × 0 × ln 0) = 0. (The 0 ln 0 terms are zero by convention.) Zero entropy means zero uncertainty — you know exactly which microstate the system occupies. Options A and D both give ln 100, which is the entropy of the *uniform* distribution over 100 states — the maximum-ignorance case. Option B gives a single probability value, not entropy."

- question: "Jaynes' maximum entropy principle says the correct statistical mechanical ensemble is the distribution that maximizes Shannon entropy subject to known constraints. For the canonical ensemble (fixed mean energy ⟨E⟩), this yields:"
  type: multiple-choice
  options:
    - "The uniform distribution over all microstates, because maximum entropy always means maximum uniformity"
    - "A distribution concentrated on the single lowest-energy microstate"
    - "The Boltzmann distribution pᵢ ∝ e^{−βEᵢ}, where β is a Lagrange multiplier enforcing the mean energy constraint"
    - "A distribution proportional to the energy of each microstate"
  answer: 2
  explanation: "When you maximize H = −Σ pᵢ ln pᵢ subject to the constraint Σ pᵢ Eᵢ = ⟨E⟩ (and normalization), the Lagrange multiplier method yields pᵢ ∝ e^{−βEᵢ} — the Boltzmann distribution. β = 1/kT is the Lagrange multiplier for the energy constraint. The uniform distribution (option A) is the maximum-entropy solution only when there are *no* constraints beyond normalization — the microcanonical case where all accessible states are equiprobable. Options B and D are incorrect; the Boltzmann distribution naturally weights lower-energy states more heavily but is not concentrated on any single state."

- question: "The statement 'entropy increases in an isolated system' is equivalent to saying that our knowledge of the system's precise microstate increases over time."
  type: true-false
  answer: false
  explanation: "This reverses the information-theoretic meaning. Entropy is a measure of *uncertainty* or *ignorance* — it is maximized when the distribution is most spread out (maximum uncertainty). 'Entropy increases' means our knowledge of the microstate *decreases* — the system evolves into a larger space of accessible microstates, and our information about which one it occupies diminishes. The correct restatement is: isolated systems evolve toward states of maximum uncertainty (maximum Shannon entropy), meaning minimal knowledge of the precise microstate."

- question: "Boltzmann's formula S = k ln Ω is a special case of Shannon entropy, arising when all accessible microstates are equally probable."
  type: true-false
  answer: true
  explanation: "If all Ω microstates are equally probable, then pᵢ = 1/Ω for all i. Shannon entropy H = −Σ pᵢ ln pᵢ = −Ω × (1/Ω) × ln(1/Ω) = ln Ω. Multiplying by Boltzmann's constant k gives S = k ln Ω — exactly Boltzmann's formula. This is the microcanonical ensemble result. The Shannon entropy formula is the general case; Boltzmann's formula applies when the system is isolated and all accessible microstates are equiprobable. This equivalence confirms that statistical mechanical and information-theoretic entropy are the same concept."

- question: "Why does 'entropy increases' mean the same thing as 'our knowledge of the microstate decreases,' and what does this imply about the direction of time?"
  type: short-answer
  answer: "Shannon entropy measures uncertainty — how spread out a probability distribution is. When entropy increases, the distribution over microstates becomes more spread out, meaning we know less about which specific microstate the system is in. A gas expanding into a vacuum has more accessible microstates; the same energy is consistent with exponentially more arrangements, so our knowledge of where the molecules are diminishes. This interpretation implies that the arrow of time is the direction in which information about the microstate is lost. We experience time as directed from past to future because high-entropy (high-ignorance) states vastly outnumber low-entropy ones, so random evolution almost always increases entropy — and thus decreases our knowledge."
  explanation: "This connection between time and information loss was developed by Maxwell, Boltzmann, and later Jaynes. The past feels different from the future because we retain memories (information) of past states but not future ones — and memories are low-entropy records. The second law says that isolated systems evolve toward maximum ignorance. The 'arrow of time' is not a feature of the fundamental laws (which are time-symmetric) but emerges from the statistical tendency toward higher entropy — toward states about which we know less."
```

## Explainer

You already know thermodynamic entropy from its macroscopic definition (dS = δQ_rev/T) and its statistical mechanical interpretation via Boltzmann's formula S = k ln Ω, where Ω counts accessible microstates. The information-theoretic approach, due to Claude Shannon, takes a different starting point: given a probability distribution over outcomes, how much uncertainty does it describe? The answer is the **Shannon entropy** H = −Σ p_i log p_i (using natural logs and writing S = kH to match thermodynamic units). This formula can be derived from first principles by asking what function of a probability distribution correctly captures "uncertainty" — the answer is unique up to a constant.

To build intuition, consider two extreme cases. If one outcome has probability 1 and all others have probability 0, then H = 0: there is no uncertainty, and knowing the distribution tells you exactly what will happen. If all N outcomes are equally likely (p_i = 1/N for all i), then H = ln N — the uncertainty is maximized and equals Boltzmann's formula S = k ln Ω when Ω = N. The Shannon entropy is a maximum when ignorance is maximal (uniform distribution) and zero when knowledge is complete. It measures not the outcomes themselves but how much information is required to specify them.

The connection to statistical mechanics is deep. In the microcanonical ensemble, all microstates are equally likely, so S = k ln Ω is exactly the Shannon entropy of that distribution — consistent with both formulas. In the canonical ensemble, the Boltzmann distribution p_i = e^{−βE_i}/Z is not uniform, but computing −k Σ p_i ln p_i returns the thermodynamic entropy S = (U − F)/T, which is again consistent. This is not a coincidence: **Jaynes' maximum entropy principle** states that the correct statistical mechanical ensemble is the one that maximizes Shannon entropy subject to whatever macroscopic constraints you impose. Microcanonical → fix energy; canonical → fix mean energy; grand canonical → fix mean energy and particle number. Each ensemble arises from entropy maximization with different Lagrange constraints.

The unification has a profound implication for the second law. "Entropy increases" is not merely a statement about heat flow — it is a statement about information loss. When a gas expands into a vacuum, the number of accessible microstates grows, and our knowledge of which microstate the system occupies decreases. Entropy measures our ignorance. The second law, reread in information-theoretic terms, says that isolated systems evolve toward states of maximum uncertainty — not because nature "wants" disorder, but because there are vastly more high-entropy microstates than low-entropy ones, so random evolution almost surely increases Ω. The arrow of time is the direction in which our knowledge of the microstate decreases.


