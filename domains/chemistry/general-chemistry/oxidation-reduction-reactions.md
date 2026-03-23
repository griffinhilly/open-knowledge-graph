---
id: oxidation-reduction-reactions
title: 'Oxidation-Reduction Reactions: Electron Transfer'
domain: chemistry
course: general-chemistry
prerequisites:
- id: ionic-bonding-formation
  type: hard
- id: chemical-equations-and-balancing
  type: hard
builds-toward:
- electrochemistry-intro
tags:
- redox reactions
- oxidation
- reduction
- electron transfer
stage: formal-systems
status: draft
---

# Oxidation-Reduction Reactions: Electron Transfer

## Core Idea
Redox reactions involve electron transfer: oxidation is losing electrons (increase in oxidation number), reduction is gaining electrons (decrease in oxidation number). An oxidizing agent causes oxidation (itself reduced); a reducing agent causes reduction (itself oxidized). Balancing redox equations requires matching electron loss and gain. Most acid-base and synthesis reactions are actually redox reactions.

## Questions

```yaml
- question: "In the reaction Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s), zinc is oxidized. Which species is the oxidizing agent?"
  type: multiple-choice
  options:
    - "Zinc (Zn), because it loses electrons"
    - "Zinc sulfate (ZnSO₄), because it is the ionic product"
    - "Copper(II) ion (Cu²⁺), because it gains the electrons that zinc loses"
    - "Sulfate ion (SO₄²⁻), because it stabilizes the zinc cation"
  answer: 2
  explanation: "The oxidizing agent is the species that causes oxidation in another substance — it does so by accepting electrons itself, and therefore gets reduced. Cu²⁺ gains two electrons (Cu²⁺ + 2e⁻ → Cu) and is therefore the oxidizing agent. Zinc loses electrons and is oxidized — making zinc the reducing agent. The agent and the species undergoing the change are always different."

- question: "The oxidizing agent in a redox reaction is the species that loses electrons."
  type: true-false
  answer: false
  explanation: "This is the single most common redox misconception. The oxidizing agent GAINS electrons (is itself reduced) — it causes oxidation in the other reactant by pulling away electrons. The REDUCING agent loses electrons (is itself oxidized). Memory device: OIL RIG — Oxidation Is Loss, Reduction Is Gain. The agent terminology always refers to what the species does TO the other reactant, not what happens to itself... except in reverse."

- question: "Assign oxidation numbers to all atoms in the reaction 2H₂ + O₂ → 2H₂O, and identify which element is oxidized and which is reduced."
  type: short-answer
  answer: "In H₂: H = 0. In O₂: O = 0. In H₂O: H = +1, O = -2. Hydrogen goes from 0 to +1 (loses electrons — oxidized). Oxygen goes from 0 to -2 (gains electrons — reduced). H₂ is the reducing agent; O₂ is the oxidizing agent."
  explanation: "Elements in their pure elemental form always have an oxidation number of 0. In H₂O, oxygen's oxidation number is -2 (its most common value) and hydrogen is +1. Tracking the change in oxidation number is how you identify oxidation (increase) and reduction (decrease) without explicitly tracking electron movement."
```

## Explainer

Redox reactions are everywhere — combustion, corrosion, photosynthesis, cellular respiration, batteries, and bleaching all involve the transfer of electrons between atoms. The core concept is deceptively simple: in any redox reaction, one species loses electrons (oxidation) and another gains them (reduction). These two half-processes always occur together — you cannot have one without the other. The word "redox" itself is a portmanteau of reduction-oxidation.

The easiest way to track electron transfer is through oxidation numbers (also called oxidation states). Oxidation numbers are a bookkeeping tool: they assign a hypothetical charge to each atom based on a set of rules (elements in elemental form = 0; oxygen is usually -2; hydrogen is usually +1 when bonded to nonmetals; etc.). Oxidation is defined as an *increase* in oxidation number (the atom is losing negative charge — electrons). Reduction is a *decrease* in oxidation number (the atom is gaining electrons). The mnemonic OIL RIG — Oxidation Is Loss, Reduction Is Gain — refers to the electrons themselves: oxidized species lose electrons, reduced species gain them.

The agent terminology trips up many students. The **oxidizing agent** causes oxidation in the other reactant — and does so by *accepting* electrons, meaning the oxidizing agent is itself reduced. The **reducing agent** causes reduction — and does so by *donating* electrons, meaning it is itself oxidized. The naming is from the perspective of what each species does to its reaction partner, not to itself. In the reaction between zinc and copper(II) sulfate: Zn gives up 2 electrons to Cu²⁺. Zinc is oxidized (and is the reducing agent); Cu²⁺ is reduced (and is the oxidizing agent).

Balancing redox equations requires that the total electrons lost equal the total electrons gained — charge must be conserved. For simple reactions, you can inspect oxidation number changes directly. For complex reactions in acidic or basic solution, the half-reaction method (splitting the equation into separate oxidation and reduction half-reactions, balancing each for atoms and charge, then combining) is the systematic approach. You will apply this extensively when you study electrochemistry, where oxidation and reduction are physically separated at different electrodes and the electron transfer is harnessed as electrical current.

A practical anchor: rusting is oxidation (iron goes from Fe⁰ to Fe²⁺/Fe³⁺, losing electrons to oxygen). Charging a battery is reversing a redox reaction by forcing electrons in the non-spontaneous direction. Bleach works by being a powerful oxidizing agent that destroys the chromophores in colored molecules by altering their electron configurations. Every one of these phenomena is the same underlying process — electron transfer — just operating in different chemical contexts.
