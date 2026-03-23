---
id: bell-theorem-inequalities
title: Bell Theorem and Bell Inequalities
domain: physics
course: quantum-mechanics
prerequisites:
- id: entanglement-quantum
  type: hard
tags:
- bell-theorem
- non-locality
- foundations
stage: advanced
status: validated
---

# Bell Theorem and Bell Inequalities

## Core Idea
Bell's theorem proves that no local hidden variable theory can reproduce quantum mechanical predictions for entangled states. Bell inequalities give bounds on correlations in any local realistic theory; quantum mechanics violates these bounds. Experiments have confirmed quantum predictions, ruling out local hidden variables. This settles the foundational debate about completeness of quantum mechanics.

## Questions

```yaml
- question: "Two entangled particles are separated to distant detectors, and their measurement outcomes are found to violate the Bell inequality. The 'matched gloves' explanation — particles carry pre-set correlated values from preparation — predicts:"
  type: multiple-choice
  options:
    - "Correlations that exactly match quantum mechanics, since pre-set values correctly describe quantum entanglement"
    - "Correlations that satisfy the Bell inequality, which quantum mechanics exceeds"
    - "Stronger correlations than quantum mechanics, since pre-set values would determine outcomes with certainty"
    - "No correlations at all, since the particles are no longer in contact at the time of measurement"
  answer: 1
  explanation: "Any local hidden variable theory — including the pre-set gloves model — must produce correlations satisfying the Bell inequalities. Quantum mechanics violates these bounds for certain measurement angle combinations. The gloves model handles the aligned-detector case correctly (100% correlation) but fails at intermediate angles, where quantum correlations are roughly 40% stronger than any local pre-shared information can produce."

- question: "Bell's theorem establishes that quantum mechanics cannot be explained by any theory that assumes both:"
  type: multiple-choice
  options:
    - "Superposition and unitarity"
    - "Determinism and time-reversal symmetry"
    - "Locality and realism (particles have definite properties prior to and independent of measurement)"
    - "Completeness and consistency of the wave function"
  answer: 2
  explanation: "Bell's argument requires exactly two assumptions: (1) locality — the measurement choice at one detector cannot influence the outcome at the other; (2) realism — particles have definite values for observable properties before measurement. Together these imply the Bell inequalities. QM violates them. So at least one assumption must fail — no theory can be simultaneously local and realistic while reproducing quantum predictions."

- question: "Experiments that confirm violations of Bell inequalities prove that no local hidden variable theory can explain the observed quantum correlations."
  type: true-false
  answer: true
  explanation: "This is the empirical upshot of Bell's theorem. Bell showed that local hidden variable theories are constrained by his inequalities. Experiments from Clauser and Freedman (1972) through loophole-free tests in 2015 confirm correlations that violate Bell inequalities and match quantum predictions. The violations are not subtle. Local hidden variable theories are empirically ruled out — the strangeness of quantum entanglement is a feature of the world, not a failure of imagination."

- question: "Bell's theorem proves that quantum mechanics is non-local — measurements on entangled particles involve faster-than-light causal influences between the detectors."
  type: true-false
  answer: false
  explanation: "Bell's theorem proves that at least one of {locality, realism} must fail — it does not specify which. Many physicists respond by abandoning realism (particles lack definite values before measurement) while maintaining a form of locality. Even in explicitly non-local interpretations like Bohmian mechanics, the non-local influences cannot be used to transmit information faster than light — the no-signaling theorem holds in all empirically adequate interpretations. Bell's theorem rules out LOCAL REALISM, not locality alone."

- question: "What are the two assumptions Bell's argument makes, and what follows if experiments confirm that Bell inequalities are violated?"
  type: short-answer
  answer: "Bell's argument assumes (1) locality: the measurement setting at one detector cannot causally influence the outcome at the other; (2) realism: each particle possesses definite values for the measured observable prior to and independent of measurement. Together these constrain the correlations any such theory can produce — the Bell inequalities. Quantum mechanics predicts correlations that violate these bounds for certain angle combinations. Loophole-free experiments confirm the violations. The logical consequence: at least one assumption must be false. Either nature is non-local (measurement choices or outcomes at one detector affect the other in some sense) or realism fails (particles do not have pre-existing definite values). Bell's theorem does not determine which must be abandoned — that requires additional interpretational choices — but it proves no theory maintaining both can match the data."
  explanation: "The philosophical depth of this result cannot be overstated: the pre-quantum intuition that correlations must arise from either direct causation or common causes (local hidden variables) is empirically refuted. The correlations between entangled particles are irreducibly non-classical."
```

## Explainer

The central mystery of quantum entanglement is that two particles can remain correlated even when separated by large distances — measuring one instantly determines something about the other. Before Bell's work, the natural skeptical response was: perhaps the particles simply carry predetermined "hidden" answers with them from the moment they were created, like two gloves placed in separate boxes. Before opening either box you don't know which is left and which is right, but nothing spooky is happening; the information was always there. This is the **local hidden variable** hypothesis: each particle carries complete information about what outcomes it will produce for any measurement, determined locally without any faster-than-light influence.

Bell's genius was to show that this seemingly reasonable hypothesis makes a testable prediction. Consider measuring spin components of two entangled particles along different angles. A local hidden variable theory must assign each particle definite (hidden) values for every possible measurement direction. The correlations that result from combining those answers must satisfy certain algebraic bounds — these are the **Bell inequalities**. Quantum mechanics, on the other hand, predicts correlations that violate these bounds for certain measurement choices. The violation is not subtle: quantum mechanics predicts correlations roughly 40% stronger than any local hidden variable theory can produce.

The brilliant simplicity of Bell's argument is that it requires only two assumptions: **locality** (the measurement choice at one detector doesn't affect the outcome at the other) and **realism** (particles have definite properties before measurement). Both assumptions together imply the Bell inequalities. Quantum mechanics violates those inequalities, so at least one assumption must fail. You cannot have a theory that is simultaneously local and realistic — hence the phrase "no local hidden variable theory."

Experiments beginning with Clauser and Freedman (1972) and culminating in loophole-free tests in 2015 have confirmed quantum predictions to high precision. The violations are real. The philosophical implication is profound: the correlations between entangled particles are not explained by pre-shared information. Either locality fails (the measurement choice at one end somehow influences the other) or realism fails (particles don't have definite properties before measurement). Bell's theorem ensures that no comfortable hidden-variable escape route exists — the strangeness of quantum mechanics is not a failure of our imagination but a feature of the world.
