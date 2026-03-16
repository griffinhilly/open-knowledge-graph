---
id: sn2-mechanism-kinetics-and-factors
title: SN2 Mechanism, Kinetics, and Factors Affecting Reactivity
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn2-reaction
  type: hard
- id: walden-inversion-sn2
  type: hard
- id: haloalkane-structure-nomenclature
  type: hard
builds-toward:
- competing-substitution-and-elimination
- williamson-ether-synthesis-sn2
tags:
- sn2
- bimolecular
- mechanism
- kinetics
- inversion
- primary
stage: formal-systems
status: draft
---

# SN2 Mechanism, Kinetics, and Factors Affecting Reactivity

## Core Idea
The SN2 reaction is a one-step bimolecular nucleophilic substitution occurring via a single transition state with inversion of stereochemistry. Second-order kinetics depend on both substrate and nucleophile concentrations. Factors favoring SN2 include primary carbon centers, polar aprotic solvents, strong nucleophiles, and good leaving groups.

## Explainer

You already know from the basic SN2 reaction and Walden inversion that the nucleophile attacks the electrophilic carbon from the back side, pushing out the leaving group in a single concerted step with complete inversion of stereochemistry. This topic zooms in on why the reaction behaves this way kinetically and what structural factors make it faster or slower.

The **rate law** is the defining fingerprint: rate = k[substrate][nucleophile]. Both species appear in the rate expression because both are present in the single transition state — that is what "bimolecular" means. Double the nucleophile concentration and the rate doubles. Double the substrate concentration and the rate doubles again. This second-order kinetics distinguishes SN2 from SN1, where only the substrate appears in the rate law. The practical consequence is immediate: if you want a faster SN2 reaction, increasing nucleophile concentration works, whereas it would have no effect on an SN1 reaction.

**Substrate structure** is the most powerful factor. The nucleophile must physically reach the electrophilic carbon, so anything that blocks the back side slows the reaction dramatically. Methyl substrates (CH₃-LG) are fastest because there are only hydrogen atoms flanking the carbon — essentially no steric obstruction. Primary substrates are nearly as good. Secondary substrates are much slower because two carbon-containing groups partially block approach. Tertiary substrates are essentially unreactive by SN2 — three bulky groups create a wall the nucleophile cannot penetrate. Think of it like trying to thread a needle: methyl is an open doorway, primary is a normal door, secondary is a narrow gap, and tertiary is a locked wall.

The remaining three factors fine-tune reactivity. A **strong nucleophile** (one with high nucleophilicity — recall that this is a kinetic property distinct from basicity) accelerates the reaction because it appears in the rate law. A **good leaving group** stabilizes the developing negative charge in the transition state; the better it departs, the lower the activation energy. And **solvent choice** matters enormously: polar aprotic solvents like DMSO and acetone do not solvate anions through hydrogen bonding, leaving the nucleophile's electron pair fully available for back-side attack. Switching from a protic solvent like methanol to an aprotic solvent like DMSO can increase SN2 rates by factors of a million. These four factors — substrate, nucleophile, leaving group, and solvent — form a checklist for predicting when an SN2 pathway will dominate over competing mechanisms.
