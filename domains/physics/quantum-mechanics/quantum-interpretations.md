---
id: quantum-interpretations
title: Interpretations of Quantum Mechanics
domain: physics
course: quantum-mechanics
prerequisites:
- id: measurement-problem
  type: hard
tags:
- interpretation
- foundations
stage: advanced
status: draft
---

# Interpretations of Quantum Mechanics

## Core Idea
Multiple interpretations agree on quantum predictions but differ philosophically: Copenhagen (wavefunction is knowledge, collapse is real), Many-Worlds (all outcomes occur in different branches), Bohmian mechanics (particles guided by pilot wave), Objective Collapse (collapse is physical). None is empirically proven; all remain viable.

## Questions

```yaml
- question: "A student argues: 'I prefer the Copenhagen interpretation because it predicts quantum interference patterns more accurately than Many-Worlds.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Copenhagen actually predicts weaker interference patterns because wavefunction collapse destroys superposition"
    - "All major interpretations make identical empirical predictions for every experiment performed to date — no experiment distinguishes them, so the preference cannot be based on predictive accuracy"
    - "Copenhagen has been empirically falsified and is no longer accepted by physicists"
    - "Many-Worlds is the only interpretation that has been tested in a controlled laboratory setting"
  answer: 1
  explanation: "This is the central fact about quantum interpretations: they are empirically equivalent. Copenhagen, Many-Worlds, Bohmian mechanics, and GRW all reproduce the same predictions for every experiment we can currently perform. (GRW is the partial exception — it makes slightly different predictions in principle, but beyond current experimental sensitivity.) Preferring one interpretation on predictive grounds misunderstands what an interpretation is: it is a philosophical account of what the formalism means, not a different physical theory."

- question: "The 'Heisenberg cut' problem is a recognized weakness of the Copenhagen interpretation. What does it refer to?"
  type: multiple-choice
  options:
    - "The mathematical limit at which the uncertainty principle prevents simultaneous position and momentum measurement"
    - "The energy threshold separating quantum behavior from relativistic behavior"
    - "The unspecified boundary between the quantum system and the classical measuring apparatus, which Copenhagen treats as a primitive without defining"
    - "The point in a calculation where the wavefunction transitions from complex to real values"
  answer: 2
  explanation: "Copenhagen says the wavefunction collapses upon measurement, but it does not specify what counts as a 'measurement' or where to draw the boundary between the quantum system (which obeys the Schrödinger equation) and the classical apparatus (which produces definite outcomes). This boundary — the Heisenberg cut — is assumed rather than derived. For practical calculations this is fine, but as a fundamental account of nature it leaves the most important question (what makes something a measurement?) unanswered. Many-Worlds and Bohmian mechanics avoid this by never invoking a special measurement process."

- question: "The Many-Worlds interpretation adds extra equations or physical mechanisms beyond standard quantum mechanics to explain why we observe definite outcomes rather than superpositions."
  type: true-false
  answer: false
  explanation: "The opposite is true: Many-Worlds is precisely the interpretation that adds nothing to the formalism. It takes the Schrödinger equation seriously for all scales, including macroscopic objects and observers, without any collapse postulate. When measurement occurs, the observer becomes entangled with the system — both the 'particle-detected-left, observer-saw-left' branch and the 'particle-detected-right, observer-saw-right' branch exist in the universal wavefunction. Decoherence explains why these branches don't interfere. Many-Worlds is mathematically minimal, even if ontologically extravagant."

- question: "Bohmian mechanics (de Broglie–Bohm pilot wave theory) is a hidden-variable theory that was ruled out by Bell's theorem because it requires faster-than-light signaling."
  type: true-false
  answer: false
  explanation: "Bell's theorem rules out local hidden-variable theories — those in which each particle carries predetermined answers to measurement questions independently of distant events. Bohmian mechanics is a hidden-variable theory (particles always have definite positions), but it is explicitly nonlocal: the pilot wave connects distant particles instantaneously in the sense that the guidance equation depends on the global wavefunction. It is therefore not ruled out by Bell's theorem, only constrained to be nonlocal. It cannot be used to send faster-than-light signals (due to the measurement statistics), but it is nonlocal in its ontology."

- question: "What does it mean to say that quantum interpretations 'underdetermine the physics'? Why can't we simply run an experiment to determine which interpretation is correct?"
  type: short-answer
  answer: "Underdetermination means that the mathematical formalism of quantum mechanics — the Schrödinger equation, the Born rule, the algebra of observables — does not uniquely specify what physically exists or what processes actually occur. Multiple incompatible interpretations (Copenhagen: no collapse is real; Many-Worlds: all branches exist; Bohmian: particles have definite positions guided by a pilot wave) are all consistent with the same mathematical structure and therefore predict the same experimental outcomes. Since interpretations agree on predictions, no experiment can currently distinguish them — the disagreement is about the underlying ontology, not the observable physics."
  explanation: "This situation is unusual in physics, where theoretical differences typically imply different predictions. The hard problem of quantum mechanics is that the measurement problem admits multiple self-consistent solutions at the philosophical level, and the solutions diverge on questions (Does the wavefunction represent reality or knowledge? Do unmeasured branches exist?) that have no direct empirical signature. GRW objective collapse is a partial exception — it modifies the Schrödinger equation slightly, making predictions that differ from standard QM in principle, just not detectably with current technology."
```

## Explainer

From studying the measurement problem, you know that quantum mechanics presents a paradox: the Schrödinger equation evolves wavefunctions smoothly and deterministically, yet measurement produces a single definite outcome rather than a superposition. The wavefunction of a particle in a double-slit experiment genuinely passes through both slits — the interference pattern proves it. But when you look, the particle is always at one place. Something breaks the superposition. An interpretation of quantum mechanics is a consistent story about what that "something" is, and what the wavefunction represents in the first place. Critically, all major interpretations make identical predictions for every experiment performed to date, so the choice between them is currently a matter of philosophy, not physics.

The **Copenhagen interpretation**, developed by Bohr and Heisenberg, holds that the wavefunction is not a description of physical reality but a tool for calculating probabilities. "What is the electron doing before measurement?" is, on this view, a meaningless question. The wavefunction **collapses** upon measurement: the quantum system transitions abruptly from superposition to a definite state, and this collapse is a fundamental feature of nature. Copenhagen is pragmatically comfortable and experimentally sufficient, which is why most physicists use it in practice. Its weakness is that it treats "measurement" as a primitive term without defining where the quantum-classical boundary lies — the so-called **Heisenberg cut** is not specified.

The **Many-Worlds interpretation** (Everett, 1957) denies that collapse happens at all. The Schrödinger equation is always valid, even for macroscopic systems and observers. When you measure a particle, you become entangled with it: both the "particle-went-left, you-saw-left" branch and the "particle-went-right, you-saw-right" branch exist — in separate, non-interacting branches of a vast universal wavefunction. You experience only one branch because quantum interference between branches vanishes for macroscopic objects (**decoherence**). Many-Worlds is mathematically the most parsimonious interpretation — it adds nothing to the formalism — but raises deep questions about how probabilities arise from deterministic branching and what it means for "you" to persist across branches.

**Bohmian mechanics** (de Broglie–Bohm theory) takes a radically different approach: particles always have definite positions, and the wavefunction is a real physical field — the **pilot wave** — that guides them. The apparent randomness of quantum mechanics arises because we have incomplete knowledge of the particle's initial position, which is hidden from us. This is a **hidden-variable theory**, and it is fully deterministic. Bell's theorem rules out local hidden-variable theories, but Bohmian mechanics is explicitly non-local (the pilot wave connects distant particles instantaneously), satisfying the letter but not the spirit of locality. **Objective collapse** theories like GRW (Ghirardi-Rimini-Weber) modify the Schrödinger equation itself, adding a small spontaneous collapse term that is negligible for microscopic systems but effectively instantaneous for macroscopic ones. These theories are, in principle, empirically distinguishable from standard quantum mechanics — just beyond current experimental sensitivity. The interpretations collectively reveal that the formalism of quantum mechanics underdetermines the physics: the mathematics alone does not tell us what exists.
