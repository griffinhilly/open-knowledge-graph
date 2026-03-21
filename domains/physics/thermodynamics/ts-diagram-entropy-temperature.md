---
id: ts-diagram-entropy-temperature
title: 'T-S Diagrams: Temperature-Entropy Diagrams'
domain: physics
course: thermodynamics
prerequisites:
- id: entropy-intro
  type: hard
- id: second-law-of-thermodynamics
  type: hard
builds-toward:
  - brayton-cycle-gas-turbine
tags:
- visualization
- entropy
- heat-transfer
stage: formal-systems
status: draft
---
# T-S Diagrams: Temperature-Entropy Diagrams

## Core Idea
A T-S diagram (temperature vs. entropy) plots thermodynamic processes and cycles with temperature on the vertical axis and entropy on the horizontal; the area under a curve equals the heat transferred. For a reversible process, đQ_rev = T dS, so the area under a T-S curve directly gives heat transfer, making these diagrams particularly useful for steam cycles and heat engine analysis. T-S diagrams complement P-V diagrams in understanding thermodynamic cycles from different perspectives.

## How It's Best Learned
Plot ideal cycles on T-S diagrams. Calculate heat transfer from areas. Compare reversible and irreversible process paths.

## Common Misconceptions
- Thinking T-S and P-V diagrams show the same cycles (they look different but represent the same physics).
- Forgetting that only the area between the curve and the S-axis equals Q (not area between any reference line).
- Confusing entropy increase with heat transfer direction.

## Questions

```yaml
- question: "A reversible process traces a horizontal line on a T-S diagram from entropy S₁ to S₂ at constant temperature T. What does the area under this line represent?"
  type: multiple-choice
  options:
    - "The work done by the system during the process"
    - "The heat transferred during the process"
    - "The change in internal energy of the system"
    - "The change in enthalpy of the system"
  answer: 1
  explanation: "By δQ_rev = T dS, the area under a T-S curve is heat transfer. For an isothermal process, heat = T × ΔS, which equals the rectangular area under the horizontal line. This is the core utility of T-S diagrams: heat becomes geometrically legible."

- question: "A student claims: 'A vertical line on a T-S diagram represents an isothermal process because the temperature axis doesn't move.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — a vertical line does represent an isothermal process"
    - "A vertical line represents an isentropic (constant entropy) process — no heat is transferred, but temperature can change"
    - "Vertical lines cannot exist on a T-S diagram"
    - "Isothermal processes appear as curved lines, not vertical ones"
  answer: 1
  explanation: "A vertical line means entropy is constant (ΔS = 0), corresponding to a reversible adiabatic (isentropic) process — no heat flows, but temperature can rise or fall. An isothermal process (constant temperature) appears as a HORIZONTAL line, because temperature (the vertical axis) stays fixed while entropy changes as heat is absorbed or released."

- question: "The Carnot cycle appears as a perfect rectangle on a T-S diagram."
  type: true-false
  answer: true
  explanation: "The Carnot cycle consists of two isothermal processes (horizontal lines at T_H and T_C) connected by two isentropic processes (vertical lines at fixed entropy). These four segments form a rectangle. The efficiency η = (T_H − T_C)/T_H is directly visible as the ratio of the rectangle's height span to its maximum temperature — no algebra required."

- question: "The area enclosed by a complete thermodynamic cycle on a T-S diagram represents the total heat input to the system."
  type: true-false
  answer: false
  explanation: "The enclosed area represents the NET WORK output of the cycle — that is, heat absorbed minus heat rejected. Heat input alone is the area under the upper portion of the cycle curve (above the baseline); heat rejected is the area under the lower portion. Net work = heat in − heat out = the enclosed area. Confusing 'enclosed area' with 'heat in' is a common error."

- question: "Why is a T-S diagram more useful than a P-V diagram for analyzing a heat engine's thermal efficiency?"
  type: short-answer
  answer: "A T-S diagram represents heat transfer directly as a geometric area (δQ_rev = T dS), so heat input, heat rejection, and net work appear as readable areas without calculation. On a P-V diagram, the area represents work, but heat is not geometric — it requires knowing the process path and thermodynamic state functions. The T-S diagram makes thermal efficiency visible as the ratio of the enclosed area to the heat-input area."
  explanation: "The key insight is that heat and work play symmetric roles in different diagram spaces: P-V gives work as area, T-S gives heat as area. A Carnot cycle's efficiency η = 1 − T_C/T_H is immediately legible from the rectangle's proportions in T-S space, while extracting the same information from a P-V diagram requires integrating along curved paths."
```

## Explainer

The T-S diagram builds directly on your understanding of entropy as a state function and the second law. You know that entropy measures the dispersal of energy in a system, and that entropy cannot spontaneously decrease in an isolated system. The T-S diagram gives you a graphical language to reason about heat and thermodynamic cycles using these ideas directly — it is to heat what the P-V diagram is to work.

The key relationship is δQ_rev = T dS: for a reversible process, the infinitesimal heat transferred equals the absolute temperature multiplied by the change in entropy. On a T-S diagram, with temperature on the vertical axis and entropy on the horizontal, this expression becomes an area. Specifically, the heat transferred during any reversible process is the area under the curve traced on the T-S diagram. A reversible **isothermal** process (constant temperature) appears as a horizontal line — temperature is fixed, entropy increases as heat flows in. The heat absorbed is simply T × ΔS, readable directly as the rectangle under that line. A reversible **adiabatic** (isentropic) process appears as a vertical line: no heat flows, so entropy is constant, but temperature rises or falls.

When a complete thermodynamic cycle is plotted, it forms a closed loop. The area enclosed by the loop equals the net work output of the cycle — because net work equals heat in minus heat rejected, and each quantity is the area under its respective portion of the curve. The **Carnot cycle** is particularly elegant in T-S space: two horizontal isotherms (at T_H and T_C) connected by two vertical isentropes form a rectangle. The efficiency η = (T_H − T_C)/T_H is immediately visible as the ratio of the rectangle's height span to its top edge. No algebra required — the diagram makes the physics legible at a glance.

The T-S diagram does not replace the P-V diagram; the two represent the same physical processes from different perspectives. A P-V diagram emphasizes mechanical work; a T-S diagram emphasizes heat transfer and thermal efficiency. Using both together — plotting a cycle on each — gives you a complete picture of how a heat engine converts thermal energy into mechanical work and where the unavoidable losses to the cold reservoir appear. Real cycles (Rankine, Brayton) deviate from ideal rectangles in T-S space, and the shape of those deviations tells you precisely where irreversibility is eating into efficiency.
