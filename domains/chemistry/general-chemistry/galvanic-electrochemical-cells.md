---
id: galvanic-electrochemical-cells
title: Galvanic Cells and Spontaneous Redox Reactions
domain: chemistry
course: general-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: oxidation-reduction-basics
  type: hard
builds-toward:
- electrolytic-cells
- electrochemical-kinetics
tags:
- galvanic cells
- spontaneous
- redox
stage: advanced
status: draft
---

# Galvanic Cells and Spontaneous Redox Reactions

## Core Idea
Galvanic cells harness spontaneous redox reactions to generate electrical current. Electrons flow from the oxidation half-reaction (anode) through an external circuit to the reduction half-reaction (cathode).

## How It's Best Learned
Draw cell diagrams and identify which half-reaction occurs at each electrode.

## Explainer

You already know that oxidation-reduction reactions involve electron transfer — one species loses electrons (oxidation) while another gains them (reduction). In a beaker, this transfer happens directly when the two reactants meet, and the energy is released as heat. A **galvanic cell** (also called a voltaic cell) is a device that forces this electron transfer to happen through an external wire instead of by direct contact, converting the chemical energy of a spontaneous redox reaction into electrical energy. This is the principle behind every battery you have ever used.

The design of a galvanic cell separates the two half-reactions into two compartments called **half-cells**. In one half-cell, oxidation occurs at the electrode called the **anode** — this is where a metal like zinc dissolves into solution as Zn²⁺ ions, releasing two electrons into the metal electrode. In the other half-cell, reduction occurs at the electrode called the **cathode** — this is where ions like Cu²⁺ from solution gain electrons from the electrode and deposit as solid copper. The electrons released at the anode travel through the external wire to the cathode, and this flow of electrons is the electrical current that can power a device. A helpful mnemonic: **an**ode = **ox**idation (both start with vowels); **c**athode = **r**eduction (both start with consonants).

There is one critical problem this design must solve: as oxidation proceeds at the anode, positive ions accumulate in that half-cell's solution, while at the cathode, positive ions are consumed, leaving excess negative ions. This charge imbalance would quickly halt the reaction. The **salt bridge** (or porous membrane) solves this by allowing ions to migrate between the two half-cells, maintaining electrical neutrality. Typically, anions flow toward the anode solution and cations flow toward the cathode solution. Without the salt bridge, a galvanic cell stops working almost immediately.

The **cell potential** (E°cell) measures the driving force of the overall reaction, reported in volts. You calculate it from the standard reduction potentials of the two half-reactions: E°cell = E°cathode − E°anode. A positive E°cell means the reaction is spontaneous as written — this is the defining feature of a galvanic cell. The more positive the cell potential, the more energy is available per electron transferred. For the classic zinc-copper cell, E°cell = +0.34 V − (−0.76 V) = +1.10 V. This quantitative connection between reduction potentials and cell voltage is what allows you to predict whether any given pair of half-reactions will produce a working galvanic cell and how much voltage it will generate.
