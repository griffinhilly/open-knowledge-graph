---
id: entropy-intro
title: Entropy
domain: physics
course: thermodynamics
prerequisites:
- id: second-law-of-thermodynamics
  type: hard
- id: natural-logarithm-and-e
  type: soft
- id: logarithms-intro
  type: soft
builds-toward:
- entropy-in-thermodynamic-processes
- statistical-interpretation-of-entropy
tags:
- entropy
- disorder
- irreversibility
- state-function
- Clausius
stage: formal-systems
status: validated
---

# Entropy

## Core Idea
Entropy (S) is a state function that quantifies the degree of disorder or the number of available microstates in a system. For a reversible process, the change in entropy is dS = δQ_rev/T. Entropy is additive and extensive. For irreversible processes, the entropy generated is always positive (ΔS_universe > 0), making entropy increase the arrow of time. At equilibrium, entropy is maximized. The units of entropy are J/K.

## How It's Best Learned
Compute entropy changes for simple reversible processes: isothermal expansion, heating at constant pressure. Then verify that combining two irreversible processes (e.g., heat flow across a finite temperature difference) always yields ΔS_universe > 0.

## Common Misconceptions
- Entropy is not simply 'disorder' in a qualitative sense — it has a precise mathematical definition tied to heat exchange and temperature.
- Entropy can decrease in a subsystem (e.g., a refrigerator cools its interior); only the total entropy of system plus surroundings must increase.
- High entropy does not mean high energy — entropy and energy are independent state variables.

## Questions

```yaml
- question: "A gas expands isothermally and reversibly into a vacuum, doing no work and exchanging no heat. Which of the following best describes what happens to the entropy of the universe?"
  type: multiple-choice
  options: ["Entropy of the universe decreases", "Entropy of the universe stays the same", "Entropy of the universe increases", "Entropy of the gas decreases while the surroundings increase"]
  answer: 2
  explanation: "Irreversible free expansion into a vacuum increases the number of accessible microstates for the gas, so the entropy of the gas (and thus the universe) increases even though no heat is exchanged. ΔS_universe > 0 for all irreversible processes."

- question: "It is possible for the entropy of a system to decrease without violating the Second Law of Thermodynamics."
  type: true-false
  answer: true
  explanation: "A refrigerator decreases the entropy of its interior by removing heat. This is allowed because the entropy increase of the surroundings (heat dumped to the room) more than compensates. The Second Law only requires that ΔS_universe ≥ 0 — a subsystem can decrease in entropy at the expense of its environment."

- question: "Why is entropy described as the 'arrow of time' rather than just another state variable like pressure or volume?"
  type: short-answer
  answer: "Because entropy can only increase or stay constant for an isolated system — it never spontaneously decreases. This gives time a preferred direction: the past is the direction of lower entropy, and the future is the direction of higher entropy. Pressure and volume can reversibly return to prior values; entropy cannot."
  explanation: "All other classical thermodynamic state variables (pressure, volume, temperature, internal energy) can oscillate freely. Entropy's monotonic increase in isolated systems creates the thermodynamic asymmetry we experience as the flow of time from past to future."
```

## Explainer

Entropy entered physics through a practical engineering problem: why can't a steam engine convert all its heat into work? Rudolf Clausius found that some quantity — which he named entropy — always increases in any real process. That observation is now the Second Law of Thermodynamics. Entropy (S) is defined quantitatively as dS = δQ_rev/T: for a reversible process, the entropy change equals the heat exchanged divided by the temperature at which the exchange occurs. The units, J/K, reflect this definition.

The most important thing entropy tells you is the direction of spontaneous change. If you drop an ice cube into warm water, heat flows from warm to cold — never the reverse — because the entropy of the universe increases that way. The reverse process (heat spontaneously flowing from cold to warm) would not violate conservation of energy, but it would violate the Second Law. Entropy is what makes physics time-asymmetric even though Newton's laws are not.

A common shortcut is to call entropy "disorder," and the intuition is roughly correct: a gas spread throughout a room has more entropy than the same gas compressed into a corner, because there are more ways (more microstates) to arrange the molecules in the spread-out configuration. Ludwig Boltzmann formalized this: S = k_B ln(Ω), where Ω is the number of microstates consistent with the macroscopic state. But "disorder" is qualitative — the precise definition is always the heat-exchange formula or Boltzmann's count of microstates.

Two misconceptions trip up nearly every student. First, entropy can decrease locally: a refrigerator reduces the entropy of its interior. This is fine — the Second Law only forbids entropy decreases for the universe as a whole. The refrigerator increases the entropy of the room by more than it decreases the entropy inside. Second, high entropy does not mean high energy. A gas at high temperature has high energy but may have lower entropy than a cold gas spread over a larger volume. Entropy and energy are independent state variables; confusing them leads to systematic errors in free-energy calculations.

When computing entropy changes in practice, start by identifying whether the process is reversible. For reversible processes, integrate dS = δQ_rev/T. For irreversible processes, you cannot use this integral directly — instead, find a reversible path between the same initial and final states (entropy is a state function, so the answer is the same regardless of path) and integrate along that path. This is why entropy calculations often involve hypothetical reversible routes even when the actual process is irreversible.
