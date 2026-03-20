---
id: electrolytic-cells-and-electrolysis
title: Electrolytic Cells and Non-Spontaneous Redox
domain: chemistry
course: general-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: oxidation-reduction-basics
  type: hard
builds-toward:
- faraday-laws-electrolysis
- coulometry
tags:
- electrolysis
- electrolytic cells
- non-spontaneous
stage: advanced
status: draft
---

# Electrolytic Cells and Non-Spontaneous Redox

## Core Idea
Electrolytic cells use an external electrical source to drive non-spontaneous redox reactions. Unlike galvanic cells, electrons are forced into the cathode (reduction site) from an external power source.

## Explainer

In your study of electrochemistry and redox reactions, you saw how galvanic (voltaic) cells harness spontaneous redox reactions to produce electrical energy — the reaction "wants" to happen, and we capture the electron flow as useful current. An **electrolytic cell** does the opposite: it uses an external power supply to force a reaction that would not occur on its own. Think of it as pushing water uphill — the reaction is thermodynamically unfavorable (positive ΔG), but by supplying enough electrical energy, we can make it proceed anyway.

The physical setup looks deceptively similar to a galvanic cell: two electrodes immersed in an electrolyte solution, connected by a circuit. The critical difference is that external battery or power supply in the circuit. At the **cathode**, the power source pumps electrons into the electrode, forcing cations in solution to accept them (reduction). At the **anode**, the power source pulls electrons away from the electrode, forcing anions or the electrode material to lose electrons (oxidation). Note that the electrode sign conventions flip compared to a galvanic cell: in electrolysis the cathode is connected to the negative terminal of the battery and the anode to the positive terminal, whereas in a galvanic cell those polarities are reversed.

A classic example is the electrolysis of molten sodium chloride. Sodium ions (Na⁺) are reduced to sodium metal at the cathode, and chloride ions (Cl⁻) are oxidized to chlorine gas at the anode. Neither of these half-reactions occurs spontaneously — metallic sodium reacts violently with chlorine in the forward direction, so reversing that reaction requires energy input. The minimum voltage needed to drive electrolysis equals the magnitude of the cell's standard potential for the reverse (non-spontaneous) direction, though in practice additional voltage called **overpotential** is required to overcome kinetic barriers at electrode surfaces.

Electrolysis has enormous industrial importance. It produces aluminum from bauxite ore (the Hall-Héroult process), refines copper to high purity, generates chlorine and sodium hydroxide from brine, and **electroplates** metals onto surfaces for corrosion protection or decoration. In each case, the principle is the same: electrical energy drives a thermodynamically uphill redox reaction. Understanding the relationship between the applied voltage, the cell potential, and Faraday's laws of electrolysis (which you will encounter next) lets you predict how much product forms for a given amount of charge passed through the cell.
