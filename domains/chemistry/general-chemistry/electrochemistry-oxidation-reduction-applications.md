---
id: electrochemistry-oxidation-reduction-applications
title: Electrochemistry and Redox Reactions
domain: chemistry
course: general-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: oxidation-reduction-basics
  type: hard
- id: conservation-of-energy
  type: soft
builds-toward:
- electrochemical-cells
- galvanic-cells
tags:
- electrochemistry
- redox
- oxidation
- reduction
- electron-transfer
stage: advanced
status: draft
---

# Electrochemistry and Redox Reactions

## Core Idea
Electrochemistry involves the transfer of electrons between chemical species. In redox reactions, oxidation is loss of electrons and reduction is gain. Oxidation states track electron transfer and balance redox equations. Electrochemical cells harness electron flow to do work (galvanic cells) or use electrical energy to drive non-spontaneous reactions (electrolytic cells).

## Explainer

You already understand oxidation-reduction reactions as processes where electrons transfer between species, and you know the basics of electrochemistry — that electron flow can be harnessed in cells. This topic brings those ideas together by showing how redox chemistry becomes a practical tool when you separate the two half-reactions physically and force the electrons to travel through an external circuit.

In a **galvanic (voltaic) cell**, a spontaneous redox reaction is split into two half-cells connected by a wire and a salt bridge. The species that gets oxidized (loses electrons) does so at the **anode**, and the electrons travel through the wire to the **cathode**, where another species is reduced (gains electrons). The salt bridge completes the circuit by allowing ions to migrate between compartments, maintaining electrical neutrality. The key insight is that this is the *same* reaction that would occur if you mixed the reactants directly — but by forcing the electrons through a wire, you can extract electrical work from the chemical energy. A battery is simply a galvanic cell (or series of cells) packaged for practical use.

The driving force for electron flow is measured as **cell potential (E°cell)**, expressed in volts. You calculate it from standard reduction potentials: E°cell = E°cathode − E°anode. A positive E°cell means the reaction is spontaneous as written — it will produce electrical current without external input. This connects directly to thermodynamics through the relationship ΔG° = −nFE°cell, where n is the number of moles of electrons transferred and F is Faraday's constant (96,485 C/mol). A positive cell potential means negative free energy change, confirming spontaneity — which should feel consistent with what you learned about energy conservation.

An **electrolytic cell** runs the logic in reverse. By applying an external voltage greater than the cell potential of the reverse reaction, you force a non-spontaneous reaction to proceed. This is how aluminum is extracted from its ore, how copper is electroplated onto surfaces, and how water is split into hydrogen and oxygen. The same principles of half-reactions, oxidation states, and electron counting apply — the only difference is the energy source. In electrolysis, electrical energy drives the chemistry rather than chemistry producing the electricity. Understanding this symmetry — galvanic cells convert chemical energy to electrical energy, electrolytic cells convert electrical energy to chemical energy — unifies the entire field of electrochemistry around the single concept of controlled electron transfer.
