---
id: bell-inequalities
title: Bell Inequalities and Their Violation
domain: physics
course: quantum-mechanics
prerequisites:
- id: bell-theorem
  type: hard
tags:
- bell-inequalities
- quantum-nonlocality
stage: formal-systems
status: draft
---

# Bell Inequalities and Their Violation

## Core Idea
CHSH inequality: |⟨AB⟩ + ⟨AB'⟩ + ⟨A'B⟩ − ⟨A'B'⟩| ≤ 2 in local hidden-variable theories. Quantum mechanics allows ≤ 2√2 for entangled states.

## Questions

```yaml
- question: "An experiment measures a CHSH value of 2.7. What does this result demonstrate?"
  type: multiple-choice
  options:
    - "The particles must have communicated faster than light during measurement"
    - "The correlations cannot be explained by any local hidden-variable theory"
    - "The experiment has violated Heisenberg's uncertainty principle"
    - "Quantum mechanics predicts a CHSH maximum of 2.7, so this result is expected classically"
  answer: 1
  explanation: "The CHSH bound for any local hidden-variable theory is ≤2. A measured value of 2.7 exceeds this bound, which rules out local realism — there is no way to assign pre-set hidden variables to the particles that would reproduce such correlations. Importantly, this does NOT imply faster-than-light communication; the correlations arise from entanglement but cannot be used to transmit information."

- question: "What is the significance of the Tsirelson bound (2√2 ≈ 2.83) in quantum mechanics?"
  type: multiple-choice
  options:
    - "It is the maximum CHSH value achievable by any physical system, including hypothetical post-quantum theories"
    - "It is the classical upper bound that local hidden-variable theories must respect"
    - "It is the maximum CHSH value that any quantum state can achieve — the ceiling of quantum correlations"
    - "It is the exact correlation value that a maximally entangled state always produces regardless of measurement angles"
  answer: 2
  explanation: "The Tsirelson bound is the maximum CHSH value quantum mechanics permits, achieved by maximally entangled qubits at optimal measurement angles. It is not a universal limit for all conceivable physical theories — some mathematical frameworks exceed it — but no quantum state can. Option B confuses it with the local hidden-variable bound of 2, which is the lower benchmark. Option D is wrong because the Tsirelson bound is a maximum, not a fixed output: sub-optimal measurement angles yield lower values."

- question: "Experimental violation of the CHSH inequality proves that entangled particles communicate faster than light at the moment of measurement."
  type: true-false
  answer: false
  explanation: "This is the most common misreading of Bell test results. Violating the CHSH inequality rules out local hidden-variable explanations, but it does NOT imply faster-than-light communication. The correlations cannot be used to send any signal — Alice's outcomes appear random to her, and she learns nothing about Bob's setting until they compare notes classically. The 2015 loophole-free Bell experiments confirmed non-local correlations without enabling superluminal information transfer."

- question: "Bell test experiments are agnostic about which interpretation of quantum mechanics is correct — they rule out local realism but do not distinguish between Copenhagen, many-worlds, or other interpretations."
  type: true-false
  answer: true
  explanation: "Bell inequality violations establish that no local hidden-variable theory can reproduce all quantum predictions — but this constraint is compatible with multiple interpretations. Copenhagen (wave function collapse), many-worlds (branching), pilot-wave theory (non-local hidden variables), and others all reproduce the quantum predictions and therefore all violate the CHSH bound in the way experiments observe. The experiments close off local determinism, not the broader interpretation question."

- question: "Why can a CHSH value greater than 2 not be explained by particles carrying 'pre-set instructions' from their shared source?"
  type: short-answer
  answer: "If each particle carried predetermined answers to both possible measurement settings (A or A′, B or B′), a simple algebraic argument shows the CHSH combination |⟨AB⟩ + ⟨AB′⟩ + ⟨A′B⟩ − ⟨A′B′⟩| can never exceed 2, no matter what the pre-set values are. The bound follows from the constraint that each variable is ±1 and assignments are fixed at emission, independent of the other particle's measurement. A measured value above 2 therefore means the outcomes cannot have been pre-determined locally — the correlations must arise from the quantum state itself."
  explanation: "The CHSH derivation is essentially a constraint on products of ±1 variables. If A, A′, B, B′ are all ±1 and locally fixed, then AB + AB′ + A′B − A′B′ = A(B + B′) + A′(B − B′). Since B and B′ are ±1, either B + B′ = ±2 and B − B′ = 0, or vice versa. In either case the expression equals ±2. Averaging over many trials cannot exceed 2. Quantum correlations violate this because the outcomes are not locally pre-set — they are generated by the measurement process acting on a non-separable joint state."
```

## Explainer

Bell's theorem, which you have already studied, establishes that no local hidden-variable (LHV) theory can reproduce all predictions of quantum mechanics. But a theorem is only as strong as what you can test. The **Bell inequalities** — and in particular the **CHSH inequality** (named for Clauser, Horne, Shimony, and Holt) — translate Bell's abstract argument into a precise, experimentally measurable bound. They give you a number: if nature obeys local realism, certain correlation measurements must stay within a hard limit. Quantum mechanics predicts that entangled states can violate that limit. Experiments have confirmed the violation. The inequalities are the instrument that turned a philosophical debate into a laboratory result.

To understand the CHSH inequality, imagine two distant parties, Alice and Bob, each receiving one particle from an entangled pair. Alice can choose between two measurement settings, call them A and A′, each returning outcome ±1. Bob can choose between B and B′, also returning ±1. They repeat the experiment many times and compute the four correlation values ⟨AB⟩, ⟨AB′⟩, ⟨A′B⟩, and ⟨A′B′⟩ — each is the average of the product of their outcomes when that pair of settings is used. In any local hidden-variable theory, each particle carries pre-determined instructions for how to respond to each measurement. A simple algebraic argument (the CHSH derivation) then shows that the combination |⟨AB⟩ + ⟨AB′⟩ + ⟨A′B⟩ − ⟨A′B′⟩| cannot exceed 2. This is the **CHSH bound** for classical local realism.

Quantum mechanics breaks through this bound. For two qubits in a maximally entangled (singlet) state and optimally chosen measurement angles, quantum theory predicts the combination reaches 2√2 ≈ 2.83 — the **Tsirelson bound**, which is the maximum any quantum state can achieve. The reason is that quantum correlations are not carried by hidden variables pre-assigned at emission; they arise from the entangled state itself, which does not factor into independent particle states. When Alice measures, her outcome is genuinely random — but it is **correlated** with Bob's outcome in a way that cannot be explained by any shared classical information. The correlations are "spookier" than any classical mechanism can produce.

Experiments by Aspect (1982), and more recently loophole-free experiments by groups in Delft, Vienna, and NIST (2015), have measured CHSH values above 2 with high statistical confidence, closing detector and locality loopholes simultaneously. These results rule out all local hidden-variable theories as complete descriptions of nature. What they do *not* do is require a particular interpretation of quantum mechanics — they are silent on whether collapse is real, whether many-worlds is correct, or what the wavefunction "is." But they firmly establish that if a deeper theory underlies quantum mechanics, it cannot be both local and deterministic in the classical sense. The CHSH inequality is the quantitative scar left by Bell's theorem on the surface of experimental physics.
