---
id: heat-transfer-conduction
title: 'Heat Transfer: Conduction'
domain: physics
course: thermodynamics
prerequisites:
- id: temperature-and-thermal-equilibrium
  type: hard
- id: thermal-expansion
  type: soft
- id: heat-conduction-basics
  type: soft
- id: thermal-energy-transfer-mechanisms
  type: soft
builds-toward:
- heat-transfer-convection
- heat-transfer-radiation
tags:
- conduction
- heat-transfer
- thermal-conductivity
- fourier-law
stage: formal-systems
status: validated
---
# Heat Transfer: Conduction

## Core Idea
Conduction is the transfer of heat through direct molecular collisions without bulk movement of matter. The rate of heat flow is given by Fourier's law: P = kA(ΔT/L), where k is the thermal conductivity of the material, A is cross-sectional area, ΔT is the temperature difference, and L is thickness. Metals are excellent conductors because free electrons transport energy efficiently; insulators like wood and fiberglass have low k values.

## How It's Best Learned
Compare thermal conductivities of materials and interpret why a metal doorknob feels colder than a wooden door at the same room temperature. Solve steady-state conduction problems in layered materials (R-value problems) by analogy with electrical resistance in series.

## Common Misconceptions
- A metal object does not have a lower temperature than a wooden one at the same room temperature — it just conducts heat away from your hand faster, making it feel colder.
- Thermal conductivity and electrical conductivity are correlated in metals but not identical.

## Questions

```yaml
- question: "You simultaneously touch a metal frying pan and a wooden cutting board that have both been sitting in a 22°C kitchen. The metal feels much colder. What explains this?"
  type: multiple-choice
  options:
    - "The metal is actually at a lower temperature than the wood — metal loses heat to the air faster"
    - "Metal has higher thermal conductivity, so it draws heat away from your hand faster, making it feel colder"
    - "Your hand heats the wood, raising its temperature, while metal remains cold"
    - "Metal has a lower heat capacity, so it absorbs less total energy from your hand"
  answer: 1
  explanation: "Both objects are at 22°C — the same temperature. 'Feeling cold' reflects the rate at which heat leaves your hand, not the object's temperature. Metal's high thermal conductivity (k) means it transfers heat away from your hand very rapidly, signaling coldness to your nerves. Wood's low k means heat flows slowly, so your hand doesn't cool quickly. The temperature is identical; the sensation differs entirely because k differs."

- question: "A wall is 10 cm thick. If the thickness is doubled to 20 cm while everything else stays the same, what happens to the rate of heat conduction through it?"
  type: multiple-choice
  options:
    - "The rate doubles — more material provides more pathways for heat"
    - "The rate stays the same — thickness does not affect heat flow"
    - "The rate is halved — thickness L is in the denominator of Fourier's Law"
    - "The rate is quartered — the effect compounds with the area"
  answer: 2
  explanation: "Fourier's Law: P = kA(ΔT/L). Thickness L is in the denominator, so doubling L halves P. More thickness means heat must travel farther through the material, increasing thermal resistance R = L/(kA) and proportionally reducing the flow rate. This is the physical principle behind thick insulation."

- question: "Two objects at exactly the same temperature can feel different temperatures when touched."
  type: true-false
  answer: true
  explanation: "True — and this is the central insight of conduction. What you feel as 'cold' or 'warm' is not the object's temperature but the rate of heat flow between the object and your skin. A metal and a wooden object at the same temperature feel different because their thermal conductivities differ by orders of magnitude."

- question: "Adding thicker insulation to a wall reduces heat loss mainly because the insulation is colder than the outside air."
  type: true-false
  answer: false
  explanation: "False. Insulation works because of its low thermal conductivity (k) and because increasing thickness (L) raises thermal resistance R = L/(kA), reducing heat flow P = kA(ΔT/L). The temperature of the insulation is not the cause — what matters are the material property k and the thickness L. A thicker wall of any material reduces heat loss, regardless of the insulation's temperature."

- question: "Why does doubling the thickness of an insulating wall reduce heat loss, and how does Fourier's Law explain this?"
  type: short-answer
  answer: "Fourier's Law states P = kA(ΔT/L). Thickness L appears in the denominator, so doubling L doubles the thermal resistance (R = L/kA) and halves the heat flow rate P. Physically, heat must travel a longer path through more material, slowing the transfer of energy."
  explanation: "Thermal resistance R = L/(kA) works like electrical resistance: more resistance means less current (heat flow). Doubling L doubles R, halving P. This is why building codes specify minimum insulation thickness — each added inch meaningfully reduces energy loss in winter."
```

## Explainer

You know from thermal equilibrium that heat flows from hot regions to cold regions until temperatures equalize. Conduction is the microscopic mechanism by which this happens inside a solid or stationary fluid: energetic molecules collide with their neighbors and pass kinetic energy along, without any bulk flow of matter. The quantitative description is **Fourier's Law**: the rate of heat flow P (in watts) through a material is proportional to the temperature difference, the cross-sectional area, and the inverse of the thickness — P = kA(ΔT/L), where k is the **thermal conductivity** of the material.

The factor k is a material property that varies enormously: copper has k ≈ 400 W/m·K, while air has k ≈ 0.025 W/m·K — a factor of 16,000. This explains why a metal doorknob at 20°C feels cold while a wooden door at the same temperature feels neutral. Your hand is at 37°C; both objects are at 20°C and will extract heat from your hand. But copper extracts it 1,000× faster than wood, so your hand cools rapidly — which your nervous system interprets as "cold." The temperature is the same; the sensation is different because k is different.

Fourier's Law has a direct analogy with Ohm's Law for electricity: P (heat flow rate) corresponds to current I, temperature difference ΔT corresponds to voltage ΔV, and the **thermal resistance** R_th = L/(kA) corresponds to electrical resistance. For composite materials — like a wall made of plaster, insulation, and brick — thermal resistances in series simply add: R_total = R₁ + R₂ + R₃. This is the basis of **R-values** in building insulation: a higher R-value means higher thermal resistance, so less heat escapes in winter. Doubling the thickness doubles R; using a material with half the k also doubles R.

In steady state, the heat current is the same through every layer of a composite wall — just as current is the same through resistors in series. The temperature drops across each layer proportionally to its thermal resistance: most of the temperature drop occurs across the most resistive layer. This is exactly why adding a thin air gap (very low k but also very thin) contributes some insulation, while thick fiberglass batting (low k, large L) contributes much more. Understanding this layered resistance framework lets you design thermal systems — from building envelopes to heat sinks in electronics — using the same intuition you would apply to a resistor network.
