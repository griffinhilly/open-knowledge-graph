---
id: electrochemical-cells
title: Electrochemical Cells
domain: chemistry
course: general-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: entropy-and-gibbs-free-energy
  type: soft
tags:
- galvanic-cell
- electrolytic-cell
- cell-potential
- Nernst-equation
- standard-reduction-potential
- Faraday
- electrolysis
stage: formal-systems
status: validated
---

# Electrochemical Cells

## Core Idea
Galvanic (voltaic) cells convert spontaneous redox reactions into electrical energy; electrolytic cells use electrical energy to drive non-spontaneous reactions. Standard cell potential E°cell = E°cathode − E°anode (from standard reduction potential tables) indicates spontaneity: E°cell > 0 means spontaneous. The thermodynamic connection is ΔG° = −nFE°cell, where n is moles of electrons transferred and F is Faraday's constant (96,485 C/mol). The Nernst equation E = E° − (RT/nF)ln Q adjusts cell potential for non-standard concentrations, explaining why batteries lose voltage as they discharge.

## How It's Best Learned
Draw and label galvanic cells: anode on left (oxidation), cathode on right (reduction), electrons flow through external circuit, ions migrate through salt bridge. Practice calculating E°cell from reduction potential tables and connecting to ΔG° and K through the ΔG° = −nFE° = −RT ln K triangle.

## Common Misconceptions
- Electrons flow from anode to cathode through the wire; cations in the salt bridge migrate toward the cathode — these are two different charge carriers, not the same.
- A positive E°cell means the reaction is spontaneous as written (ΔG° < 0), not that energy is required — it means the cell can do work, not that work must be done to it.

## Questions

```yaml
- question: "A galvanic cell is constructed from a Zn²⁺/Zn half-cell (E° = −0.76 V) and a Cu²⁺/Cu half-cell (E° = +0.34 V), with Zn as the anode. What is E°cell?"
  type: multiple-choice
  options:
    - "−1.10 V"
    - "−0.42 V"
    - "+0.42 V"
    - "+1.10 V"
  answer: 3
  explanation: "E°cell = E°cathode − E°anode = (+0.34) − (−0.76) = +1.10 V. The copper half-cell is the cathode (reduction) and zinc is the anode (oxidation). A common error is to simply add the two values algebraically without recognizing that the anode potential must be subtracted, and another is to reverse the cathode/anode assignment."

- question: "In a galvanic cell, both electrons in the external wire and cations in the salt bridge move toward the cathode, so they are doing the same job of carrying positive charge in the same direction."
  type: true-false
  answer: false
  explanation: "Electrons flow from anode to cathode through the external wire — they are negatively charged moving in one direction. Cations in the salt bridge migrate toward the cathode to maintain charge neutrality in the cathode compartment, which becomes depleted of positive ions as reduction consumes cations. These are two distinct charge carriers serving complementary roles; conflating them misrepresents how the circuit is completed."

- question: "Using the Nernst equation, explain why a battery's voltage decreases as it discharges."
  type: short-answer
  answer: "As a battery discharges, reactant concentrations fall and product concentrations rise, increasing the reaction quotient Q. The Nernst equation (E = E° − (RT/nF)ln Q) shows that as Q increases, cell potential E decreases below E°."
  explanation: "At standard conditions Q = 1 and E = E°. As the cell operates, it consumes reactants and generates products, so Q grows larger than 1. Because ln Q becomes a larger positive number, the term (RT/nF)ln Q subtracted from E° grows, lowering E. When Q equals the equilibrium constant K, E = 0 — the battery is dead and ΔG = 0."
```

## Explainer

You already know from electrochemistry basics that redox reactions involve electron transfer — one species is oxidized (loses electrons) and another is reduced (gains them). Electrochemical cells exploit this electron flow by physically separating the two half-reactions, forcing electrons to travel through an external wire rather than jumping directly between species. That moving charge is electrical current, and capturing it is how a battery works.

In a **galvanic (voltaic) cell**, the reaction is spontaneous — it releases free energy and the cell does work on the circuit. The standard convention is: **anode on the left, cathode on the right**. At the anode, oxidation occurs and electrons are released into the wire. At the cathode, those electrons arrive and drive reduction. A salt bridge (or porous membrane) connects the two solution compartments, allowing ions to migrate and maintain electrical neutrality without letting the solutions mix. Without the salt bridge, charge would build up and the reaction would stop almost immediately.

The cell's driving force is quantified by **standard cell potential**: E°cell = E°cathode − E°anode. Both values come from standard reduction potential tables, which list half-reactions written as reductions. To get the anode's contribution, you use the same table value but *subtract* it (because oxidation is the reverse). A positive E°cell tells you the reaction is spontaneous (ΔG° < 0); the thermodynamic link is ΔG° = −nFE°cell, where n is moles of electrons transferred and F = 96,485 C/mol. This triangle — E°cell, ΔG°, and the equilibrium constant K via ΔG° = −RT ln K — connects electrochemistry to thermodynamics.

An **electrolytic cell** reverses the situation: an external power source forces a non-spontaneous reaction to proceed (E°cell < 0, ΔG° > 0). Electrolysis is how aluminum is refined from bauxite, how chlorine gas is produced industrially, and how electroplating works. The anode/cathode labels still hold (anode = oxidation, cathode = reduction), but now the cathode is connected to the negative terminal of the power supply.

Real batteries operate under non-standard concentrations, which is where the **Nernst equation** becomes essential: E = E° − (RT/nF) ln Q. As the battery discharges, reactants are consumed and products accumulate, so Q increases, ln Q becomes positive, and E falls. This explains the gradual voltage drop you observe as a battery ages. When Q = K (equilibrium), E = 0 — the battery is fully discharged and incapable of doing further work. Rechargeable batteries reverse the process by applying an external voltage to regenerate the original reactants.
