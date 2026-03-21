---
id: interpretations-quantum-mechanics
title: Interpretations of Quantum Mechanics
domain: physics
course: quantum-mechanics
prerequisites:
- id: measurement-problem-quantum
  type: hard
tags:
- interpretations
- foundations
stage: advanced
status: draft
---

# Interpretations of Quantum Mechanics

## Core Idea
Major interpretations address the measurement problem differently: Copenhagen (subjective ψ), many-worlds (all branches), objective collapse (physical collapse), Bohmian (deterministic trajectories), relational (relative properties). All reproduce empirical predictions.

## Questions

```yaml
- question: "A physicist says: 'Many-worlds is obviously wrong because it predicts we should observe all quantum outcomes, but we only ever see one.' What is the error in this reasoning?"
  type: multiple-choice
  options:
    - "Many-worlds does not actually say all outcomes occur — only the most probable outcome happens"
    - "Many-worlds predicts that each observer in each branch sees exactly one outcome, consistent with experience; the challenge is explaining Born rule probabilities, not the singularity of outcomes"
    - "The physicist is correct — many-worlds is empirically distinguishable from Copenhagen because it predicts outcome multiplicity"
    - "Many-worlds applies only to microscopic systems and not to macroscopic measurement devices"
  answer: 1
  explanation: "Many-worlds does not predict that any single observer sees multiple outcomes. Upon measurement, the universe branches — each branch contains an observer who sees exactly one definite result, consistent with experience. The genuine challenge for many-worlds is not singularity of outcomes but explaining *why* branches occur with Born rule frequencies rather than just being equally probable. The physicist's objection confuses the global structure (all branches exist) with the local experience of an observer within a branch (one outcome, always)."

- question: "Which feature distinguishes Bohmian mechanics (pilot-wave theory) from all other major interpretations of quantum mechanics?"
  type: multiple-choice
  options:
    - "It denies that the wavefunction is real — only particle positions are physically meaningful"
    - "It modifies the Schrödinger equation by adding small random collapse terms"
    - "Particles always have definite positions and follow deterministic trajectories guided by a real pilot wave, making quantum randomness purely epistemic"
    - "Quantum states are defined only relative to observers, not as absolute properties of systems"
  answer: 2
  explanation: "Bohmian mechanics restores full determinism: particles have definite positions at all times, guided by the pilot wave (which satisfies the Schrödinger equation). The apparent randomness of quantum mechanics is epistemic — we don't know the exact initial particle positions, so outcomes appear random. This distinguishes it from Copenhagen (randomness is fundamental), many-worlds (all outcomes occur), and objective collapse theories (randomness is physical). Note that Bohmian mechanics is empirically equivalent to standard quantum mechanics but requires nonlocal guidance: a particle's velocity depends instantaneously on all other particles' positions."

- question: "All major interpretations of quantum mechanics — Copenhagen, many-worlds, Bohmian mechanics, objective collapse, and relational QM — make identical predictions for every possible experiment."
  type: true-false
  answer: true
  explanation: "This is one of the most important facts about the interpretation debate: it is not empirically decidable by any currently feasible experiment. All interpretations reproduce the Born rule predictions and agree on every observable outcome. The disagreement is about what is 'really happening' — whether collapse is physical (objective collapse theories, which are in principle distinguishable but extremely difficult to test), what the wavefunction represents, and whether there is a fact about particle positions before measurement. The choice among interpretations is currently philosophical, not scientific."

- question: "The Copenhagen interpretation holds that the wavefunction describes the objective physical state of a quantum system between measurements."
  type: true-false
  answer: false
  explanation: "Copenhagen takes a deliberately agnostic or instrumentalist stance: the wavefunction is a calculational tool for predicting probabilities of measurement outcomes, not a description of an objective physical reality that exists between measurements. This is precisely what Copenhagen refuses to say: the question 'what is the particle doing before measurement?' is treated as meaningless or unanswerable within Copenhagen. This agnosticism is what other interpretations reject — many-worlds, Bohmian mechanics, and objective collapse theories all insist on providing an ontological account of what is happening between measurements."

- question: "What is the measurement problem, and why does it motivate the proliferation of interpretations of quantum mechanics?"
  type: short-answer
  answer: "The measurement problem is the conflict between two aspects of quantum mechanics: (1) the Schrödinger equation, which evolves the wavefunction deterministically and produces superpositions of multiple states, and (2) the fact that every measurement yields a single definite outcome rather than a superposition. The equation alone cannot explain why measurements give definite results. Each interpretation resolves this differently: Copenhagen treats the wavefunction as merely a probability tool and collapse as a probability update; many-worlds says all outcomes occur in branching universes; objective collapse theories modify the Schrödinger equation; Bohmian mechanics adds definite particle positions guided by the wave. Since all interpretations reproduce the same predictions, the measurement problem is not resolved by data alone but requires a philosophical choice about what the formalism means."
  explanation: "The key insight is that quantum mechanics is empirically complete — it predicts everything we can measure — but interpretively incomplete: the formalism underdetermines what is physically happening. The measurement problem makes this underdetermination sharp. Knowing that interpretations are empirically equivalent should produce humility: anyone claiming the interpretation question is 'settled' by physics is confused about the nature of the problem."
```

## Explainer

You've encountered the **measurement problem**: quantum mechanics assigns a wavefunction that evolves deterministically via the Schrödinger equation, producing superpositions — yet every measurement yields a single definite outcome, not a superposition. Something not contained in the Schrödinger equation must be happening during measurement. Every interpretation of quantum mechanics is an attempt to make sense of this apparent collapse, and they differ fundamentally on whether collapse is real, what the wavefunction represents, and whether quantum mechanics is complete.

The **Copenhagen interpretation**, the default in most textbooks, takes a deliberately agnostic stance: the wavefunction is a tool for predicting probabilities, not a description of an objective physical reality. Collapse is simply the update of probabilities upon getting a result. The quantum-classical boundary is drawn pragmatically — the measuring apparatus is treated classically. This works perfectly for calculations but leaves open what is "really happening" before measurement, which many physicists consider an unacceptable silence about fundamental ontology.

**Many-worlds** (Everett) takes the wavefunction at full face value: it is real, and the Schrödinger equation is exact and universal. When a measurement occurs, the universe branches — all outcomes happen, in different branches of a vast universal wavefunction. There is no collapse and no special role for observers. The difficulty is explaining why we experience probability at all: why do we observe outcomes with Born rule frequencies rather than just finding ourselves in arbitrary branches? This is the "preferred basis problem" and the "probability problem," both active areas of debate. **Objective collapse** theories (GRW, CSL) modify the Schrödinger equation itself by adding small random collapse terms that are negligible for single particles but cumulative for large systems, causing macroscopic superpositions to collapse in microseconds. These are empirically distinguishable in principle, though extremely difficult to test in practice.

**Bohmian mechanics** (pilot-wave theory) restores determinism entirely: particles always have definite positions, guided by a real pilot wave that satisfies the Schrödinger equation. The apparent randomness of quantum mechanics is purely epistemic — we don't know the exact initial positions. This interpretation is empirically equivalent to standard quantum mechanics, but the guiding equation is nonlocal: the velocity of a particle depends instantaneously on the configuration of all other particles, no matter how distant. **Relational quantum mechanics** takes yet another path: quantum states are not absolute properties of systems but are relative to observers, and different observers may legitimately assign different wavefunctions to the same system. Choosing among these interpretations is currently a philosophical question, not an empirical one — and knowing that all of them reproduce the same predictions should give you healthy skepticism toward anyone who claims the question is already settled.
