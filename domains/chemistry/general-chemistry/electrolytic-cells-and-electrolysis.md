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

## Questions

```yaml
- question: "You want to electroplate copper onto a metal object using a copper sulfate solution. The object is placed in the solution as one electrode. Which role does the object play, and what occurs there?"
  type: multiple-choice
  options:
    - "Anode — copper from the object dissolves into solution"
    - "Cathode — copper ions from solution are reduced and deposited onto the object"
    - "Cathode — the object loses mass as electrons are pulled away by the power supply"
    - "Anode — copper ions are oxidized and plated onto the object"
  answer: 1
  explanation: "In electrolysis, the cathode is where reduction occurs: cations in solution gain electrons and deposit as metal. The object to be plated is connected to the negative terminal of the power supply (cathode), so Cu²⁺ ions are reduced onto its surface. The common confusion is thinking the anode receives material — it is the anode (connected to the positive terminal) where oxidation occurs, dissolving the copper metal electrode to replenish the solution."

- question: "The standard cell potential for a galvanic cell is +0.80 V. You want to run the reverse reaction in an electrolytic cell. What is the minimum applied voltage required (ignoring overpotential)?"
  type: multiple-choice
  options:
    - "0 V — the reaction will proceed spontaneously once current begins to flow"
    - "0.40 V — half the galvanic potential because the cell is split into two half-reactions"
    - "0.80 V — you must supply at least the magnitude of the reversed cell potential"
    - "1.60 V — twice the galvanic potential to overcome thermodynamic barriers"
  answer: 2
  explanation: "The non-spontaneous (electrolytic) direction has ΔG > 0 equal in magnitude to the spontaneous direction. The minimum voltage to drive it equals the magnitude of the original cell potential, here 0.80 V. In practice, additional 'overpotential' is needed to overcome electrode kinetic barriers, but the thermodynamic minimum is the reverse cell potential. Applying less voltage simply fails to drive the reaction."

- question: "In an electrolytic cell, the cathode is connected to the negative terminal of the external power supply."
  type: true-false
  answer: true
  explanation: "This is the opposite convention from a galvanic cell, where the anode is the negative terminal. In electrolysis, the power supply forces electrons into the cathode (negative terminal), driving reduction of cations in solution. The anode is connected to the positive terminal, which pulls electrons away, forcing oxidation. Confusing the two conventions is the most common error when comparing galvanic and electrolytic cells."

- question: "Electrolysis of molten sodium chloride and electrolysis of aqueous sodium chloride produce the same products at the cathode."
  type: true-false
  answer: false
  explanation: "In molten NaCl, the only cations present are Na⁺, so sodium metal is produced at the cathode. In aqueous NaCl, water is also present, and H₂O is reduced preferentially at the cathode (lower overpotential), producing H₂ gas and OH⁻ rather than sodium metal. The competition between water and Na⁺ reduction in aqueous solution changes the product entirely — this is why the chlor-alkali industrial process (aqueous) produces H₂ and NaOH, not sodium metal."

- question: "Why does an electrolytic cell require an external power source, and what thermodynamic condition distinguishes an electrolytic reaction from a galvanic one?"
  type: short-answer
  answer: "An electrolytic cell drives a non-spontaneous redox reaction — one with ΔG > 0 and a negative standard cell potential. Because the reaction will not proceed on its own, energy must be supplied externally. A galvanic cell harnesses a spontaneous reaction (ΔG < 0, positive cell potential) to produce electrical energy. The external power supply in electrolysis does the reverse: it converts electrical energy into chemical energy, pushing electrons against the thermodynamically favored direction."
  explanation: "The key distinction is the sign of ΔG. Galvanic: ΔG < 0 (spontaneous, releases energy). Electrolytic: ΔG > 0 (non-spontaneous, requires energy input equal to at least |ΔG|). The minimum applied voltage corresponds to ΔG = −nFE, where E is the reverse cell potential. Understanding this thermodynamic framing makes sense of why industrial electrolysis (aluminum smelting, chlor-alkali, electroplating) is energy-intensive."
```

## Explainer

In your study of electrochemistry and redox reactions, you saw how galvanic (voltaic) cells harness spontaneous redox reactions to produce electrical energy — the reaction "wants" to happen, and we capture the electron flow as useful current. An **electrolytic cell** does the opposite: it uses an external power supply to force a reaction that would not occur on its own. Think of it as pushing water uphill — the reaction is thermodynamically unfavorable (positive ΔG), but by supplying enough electrical energy, we can make it proceed anyway.

The physical setup looks deceptively similar to a galvanic cell: two electrodes immersed in an electrolyte solution, connected by a circuit. The critical difference is that external battery or power supply in the circuit. At the **cathode**, the power source pumps electrons into the electrode, forcing cations in solution to accept them (reduction). At the **anode**, the power source pulls electrons away from the electrode, forcing anions or the electrode material to lose electrons (oxidation). Note that the electrode sign conventions flip compared to a galvanic cell: in electrolysis the cathode is connected to the negative terminal of the battery and the anode to the positive terminal, whereas in a galvanic cell those polarities are reversed.

A classic example is the electrolysis of molten sodium chloride. Sodium ions (Na⁺) are reduced to sodium metal at the cathode, and chloride ions (Cl⁻) are oxidized to chlorine gas at the anode. Neither of these half-reactions occurs spontaneously — metallic sodium reacts violently with chlorine in the forward direction, so reversing that reaction requires energy input. The minimum voltage needed to drive electrolysis equals the magnitude of the cell's standard potential for the reverse (non-spontaneous) direction, though in practice additional voltage called **overpotential** is required to overcome kinetic barriers at electrode surfaces.

Electrolysis has enormous industrial importance. It produces aluminum from bauxite ore (the Hall-Héroult process), refines copper to high purity, generates chlorine and sodium hydroxide from brine, and **electroplates** metals onto surfaces for corrosion protection or decoration. In each case, the principle is the same: electrical energy drives a thermodynamically uphill redox reaction. Understanding the relationship between the applied voltage, the cell potential, and Faraday's laws of electrolysis (which you will encounter next) lets you predict how much product forms for a given amount of charge passed through the cell.
