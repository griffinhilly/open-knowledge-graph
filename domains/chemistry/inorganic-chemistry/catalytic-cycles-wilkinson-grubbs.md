---
id: catalytic-cycles-wilkinson-grubbs
title: Catalytic Cycles (Wilkinson's Catalyst, Grubbs)
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: organometallic-chemistry-fundamentals
  type: hard
- id: metal-carbonyls
  type: soft
builds-toward:
- homogeneous-catalysis-mechanisms
tags:
- Wilkinson's catalyst
- Grubbs catalyst
- hydrogenation
- olefin metathesis
- catalytic cycle
stage: advanced
status: validated
---

# Catalytic Cycles (Wilkinson's Catalyst, Grubbs)

## Core Idea
Homogeneous transition metal catalysis proceeds through catalytic cycles — closed sequences of elementary organometallic reactions (oxidative addition, migratory insertion, reductive elimination, beta-hydride elimination) that convert substrates to products while regenerating the active catalyst. Wilkinson's catalyst [RhCl(PPh₃)₃] for alkene hydrogenation and Grubbs' catalyst for olefin metathesis are landmark examples that illustrate how understanding each elementary step enables rational catalyst design.

## Questions

```yaml
- question: "In the catalytic cycle of Wilkinson's catalyst for hydrogenation of an alkene, what is the first step after dissociation of one PPh₃ ligand to generate the active 14-electron species?"
  type: multiple-choice
  options:
    - "Migratory insertion of the alkene into a Rh-H bond"
    - "Oxidative addition of H₂ to the rhodium center, forming a dihydride complex and increasing the oxidation state from Rh(I) to Rh(III)"
    - "Beta-hydride elimination from a coordinated alkane"
    - "Reductive elimination of HCl to generate a more reactive Rh(0) species"
  answer: 1
  explanation: "After PPh₃ dissociation, the active species [RhCl(PPh₃)₂] (14e, Rh⁺) undergoes oxidative addition of H₂. The H-H bond breaks, and both hydrogen atoms bond to rhodium, forming [RhH₂Cl(PPh₃)₂] (Rh³⁺, 16e). This is followed by alkene coordination, migratory insertion of the alkene into one Rh-H bond (forming a Rh-alkyl species), and finally reductive elimination to release the alkane product and regenerate the active catalyst. Each step follows the rules of organometallic elementary reactions, and the overall cycle returns the catalyst to its original state."

- question: "Grubbs' catalyst accomplishes olefin metathesis — the exchange of substituents between two alkenes — through a mechanism involving a metal carbene intermediate (a M=CHR double bond)."
  type: true-false
  answer: true
  explanation: "The Chauvin mechanism for olefin metathesis involves a [2+2] cycloaddition between the metal carbene (Ru=CHR in Grubbs' catalyst) and an alkene substrate, forming a metallacyclobutane intermediate. This intermediate then undergoes a retro-[2+2] cycloreversion in the other direction, releasing a new alkene and regenerating a metal carbene with a different substituent. The cycle repeats, redistributing the substituents among alkene partners. Grubbs' ruthenium carbene catalysts are air-tolerant and functional-group tolerant, making them practical for organic synthesis — earning Grubbs the 2005 Nobel Prize."

- question: "A good homogeneous catalyst must bind substrates strongly enough to activate them but weakly enough to release products. This balance is described as the Sabatier principle."
  type: true-false
  answer: true
  explanation: "The Sabatier principle states that optimal catalytic activity requires intermediate binding strength between catalyst and substrate. If binding is too weak, the substrate cannot be activated (no reaction). If binding is too strong, the product cannot dissociate (catalyst poisoning). Wilkinson's catalyst illustrates this: PPh₃ dissociation creates a coordinatively unsaturated site for substrate binding, but the remaining ligands keep the metal center electron-rich enough to undergo oxidative addition of H₂. After hydrogenation, reductive elimination releases the product because the thermodynamic driving force of alkane formation exceeds the binding energy."

- question: "Trace the complete catalytic cycle for hydrogenation of ethylene by Wilkinson's catalyst, identifying each elementary step and the electron count at each stage."
  type: short-answer
  answer: "1) [RhCl(PPh₃)₃] (16e, Rh⁺) loses one PPh₃ to form [RhCl(PPh₃)₂] (14e, Rh⁺). 2) Oxidative addition of H₂: [RhH₂Cl(PPh₃)₂] (16e, Rh³⁺). 3) Coordination of ethylene: [RhH₂Cl(C₂H₄)(PPh₃)₂] (18e, Rh³⁺). 4) Migratory insertion: ethylene inserts into one Rh-H bond to form [Rh(C₂H₅)HCl(PPh₃)₂] (16e, Rh³⁺). 5) Reductive elimination: C₂H₅ and H couple to release C₂H₆, regenerating [RhCl(PPh₃)₂] (14e, Rh⁺). The PPh₃ re-coordinates to reform the resting state. Each step alternates the electron count between 14-18 electrons, and the oxidation state cycles between Rh(I) and Rh(III)."
  explanation: "The elegance of this cycle is that every step is a well-understood elementary reaction. No new chemistry is invented — the catalyst simply orchestrates a sequence of oxidative additions, insertions, and eliminations in the correct order. Understanding the elementary steps enables modification: changing ligands tunes selectivity, changing the metal can change which substrates are activated."
```

## Explainer

A catalyst accelerates a reaction by providing an alternative pathway with a lower activation energy, and it is regenerated at the end of each cycle. In homogeneous transition metal catalysis, the catalyst is a soluble organometallic complex that cycles through a series of well-defined elementary reactions, each changing the metal's oxidation state, coordination number, or both. The beauty of this field is that each elementary step — oxidative addition, reductive elimination, migratory insertion, beta-hydride elimination — is independently understood, and catalytic cycles are constructed by assembling these steps in sequence.

Wilkinson's catalyst, RhCl(PPh₃)₃, catalyzes the hydrogenation of alkenes under mild conditions (ambient temperature, 1 atm H₂). The resting state is a 16-electron square planar Rh(I) complex. One PPh₃ dissociates to create a coordinatively unsaturated 14-electron species. Oxidative addition of H₂ forms a Rh(III) dihydride. Ethylene coordinates, then undergoes migratory insertion into one Rh-H bond to form a rhodium-ethyl species. Reductive elimination couples the ethyl and remaining hydride to release ethane, regenerating the Rh(I) catalyst. The cycle repeats thousands of times per second, each turnover converting one alkene molecule to an alkane.

Grubbs' catalyst represents a different paradigm: olefin metathesis, where two alkenes exchange their substituents through a mechanism involving metal carbene (M=CHR) intermediates. The Chauvin mechanism proceeds through [2+2] cycloaddition between the metal carbene and an alkene, forming a metallacyclobutane, followed by retro-[2+2] cycloreversion to release a new alkene. Grubbs' ruthenium-based catalysts are remarkably tolerant of air, moisture, and diverse functional groups — a dramatic advantage over earlier molybdenum and tungsten catalysts that required rigorous exclusion of air and water. The practical utility earned the 2005 Nobel Prize in Chemistry (shared with Schrock and Chauvin).

These examples illustrate a general principle: understanding mechanisms enables rational catalyst design. Want faster turnover? Modify ligands to lower the barrier for the rate-limiting step. Want different selectivity? Change the steric environment to favor one substrate orientation over another. Want to prevent catalyst decomposition? Identify the deactivation pathway and block it. The transition from empirical catalyst screening to mechanism-guided design is one of the major intellectual achievements of organometallic chemistry, and it continues to drive the development of new catalytic reactions for pharmaceutical synthesis, polymer production, and energy conversion.
