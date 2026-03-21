---
id: electrochemistry-intro
title: 'Electrochemistry: Galvanic Cells and Electron Flow'
domain: chemistry
course: general-chemistry
prerequisites:
- id: oxidation-reduction-reactions
  type: hard
tags:
- electrochemistry
- galvanic cells
- anode
- cathode
- electron flow
stage: advanced
status: draft
---

# Electrochemistry: Galvanic Cells and Electron Flow

## Core Idea
Galvanic (voltaic) cells produce electricity from redox reactions. Oxidation occurs at the anode (negative terminal); reduction at the cathode (positive terminal). Electrons flow from anode to cathode through an external circuit, creating electric current. The voltage (cell potential) depends on the specific redox reaction. Electrochemistry is fundamental to batteries and corrosion.

## Questions

```yaml
- question: "In a zinc-copper galvanic cell, zinc is oxidized and copper ions are reduced. Through which path do electrons travel, and in which direction?"
  type: multiple-choice
  options:
    - "Through the salt bridge, from the copper half-cell to the zinc half-cell"
    - "Through the external wire, from the zinc electrode (anode) to the copper electrode (cathode)"
    - "Through the external wire, from the copper electrode (cathode) to the zinc electrode (anode)"
    - "Through the solution, from the zinc half-cell to the copper half-cell"
  answer: 1
  explanation: "Electrons are produced at the anode (where oxidation occurs — the zinc strip loses electrons) and consumed at the cathode (where reduction occurs — Cu²⁺ gains electrons). They flow through the external wire from anode to cathode, i.e., from zinc to copper. The salt bridge carries ions (not electrons) to balance charge buildup in each half-cell. Option C is the common error: conventional current flows from positive to negative, but electron flow is the reverse — from negative (anode) to positive (cathode)."

- question: "A student sets up a galvanic cell and notices that the copper electrode gradually gains mass over time while the zinc electrode loses mass. Which statement best explains both observations together?"
  type: multiple-choice
  options:
    - "Copper is being oxidized at the cathode, releasing Cu²⁺ ions into solution"
    - "Both electrodes are simultaneously acting as anodes in parallel circuits"
    - "Zinc is being oxidized at the anode and Cu²⁺ ions are being reduced and deposited at the cathode"
    - "The salt bridge is transferring metal atoms from the zinc half-cell to the copper half-cell"
  answer: 2
  explanation: "Zinc undergoes oxidation (Zn → Zn²⁺ + 2e⁻) at the anode, dissolving the zinc strip. Those electrons travel to the cathode, where Cu²⁺ ions from solution are reduced (Cu²⁺ + 2e⁻ → Cu) and plate out as solid copper, increasing the electrode's mass. This is the core operation of a galvanic cell: spontaneous redox chemistry converts chemical energy into electrical work."

- question: "In a galvanic cell, the anode is the negative terminal because it is the source of electrons."
  type: true-false
  answer: true
  explanation: "The anode is where oxidation occurs — the species being oxidized releases electrons into the external circuit. Because electrons accumulate there before flowing outward, the anode is electron-rich and therefore the negative terminal. Many students memorize that batteries have a positive terminal as the 'active' one, but in a galvanic cell the cathode is positive because it attracts electrons from the circuit. The mnemonic AnOx (anode = oxidation) and RedCat (cathode = reduction) anchors both processes."

- question: "In a galvanic cell, ions flow through the external wire to complete the electrical circuit."
  type: true-false
  answer: false
  explanation: "Electrons — not ions — flow through the external wire. Ions carry charge through the solution and the salt bridge. The salt bridge provides an ionic pathway that completes the internal circuit by allowing ions to migrate between half-cells, balancing the charge buildup that would otherwise halt the reaction. Without the salt bridge, the half-cells would quickly develop prohibitive charge separation and the cell would stop working — but it is always electrons in the wire, never ions."

- question: "Why is the salt bridge essential to a galvanic cell, and what would happen if it were removed?"
  type: short-answer
  answer: "The salt bridge provides an ionic pathway between the two half-cells, allowing ions to migrate and maintain electrical neutrality in each solution. Without it, the half-cell producing cations (the anode, where oxidation dissolves metal into solution as positive ions) would build up positive charge, while the half-cell consuming cations (the cathode, where positive ions plate out) would build up negative charge. This charge imbalance would create an opposing electric potential that rapidly stops electron flow — the cell would die almost immediately even though the chemical driving force remains."
  explanation: "The external wire carries electron current; the internal solution-and-salt-bridge pathway carries ionic current. Both pathways must be complete for sustained current flow. Real batteries solve this problem internally with a porous separator or gel electrolyte that allows ion migration between anode and cathode compartments."
```

## Explainer

From your study of oxidation-reduction reactions, you know that redox processes involve electron transfer — one species loses electrons (oxidation) while another gains them (reduction). In a beaker, this transfer happens directly when the reactants touch. The brilliant idea behind a **galvanic cell** is to physically separate the two half-reactions so that electrons must travel through an external wire to get from the species being oxidized to the species being reduced. That flow of electrons through the wire is electric current — and that is how a battery works.

Picture a classic zinc-copper galvanic cell. A strip of zinc metal sits in a solution of Zn²⁺ ions (one **half-cell**), and a strip of copper metal sits in a solution of Cu²⁺ ions (the other half-cell). The two solutions are connected by a **salt bridge** — a tube filled with an inert electrolyte like KNO₃ — and the two metal strips are connected by a wire. Zinc is more easily oxidized than copper (it is higher in the activity series), so zinc atoms on the strip spontaneously lose electrons: Zn(s) → Zn²⁺(aq) + 2e⁻. Those electrons flow through the wire to the copper strip, where Cu²⁺ ions in solution grab them: Cu²⁺(aq) + 2e⁻ → Cu(s). The zinc strip slowly dissolves while copper plates out on the copper strip. The salt bridge completes the circuit by allowing ions to migrate and balance the charges building up in each half-cell.

The terminology follows a simple mnemonic: **an**ode = **ox**idation (both start with vowels), **c**athode = **r**eduction (both start with consonants). In a galvanic cell, the anode is the negative terminal because it is the source of electrons, and the cathode is the positive terminal because electrons flow toward it. The **cell potential** (E°cell) measures how strongly the cell pushes electrons through the wire and is calculated as E°cathode − E°anode using standard reduction potentials. A positive cell potential means the reaction is spontaneous — it will generate current without any external energy input.

Every battery you use — from AA alkaline cells to lithium-ion phone batteries — is a galvanic cell using this same principle. The specific metals and electrolytes differ, but the architecture is identical: two half-reactions separated so that electron transfer is forced through a circuit. When you connect a galvanic cell to a light bulb or motor, the spontaneous redox reaction does work. Understanding this foundation prepares you for electrolytic cells (where you reverse the process by pushing current *into* a non-spontaneous reaction), the Nernst equation (which accounts for non-standard conditions), and the electrochemistry of corrosion, electroplating, and fuel cells.
