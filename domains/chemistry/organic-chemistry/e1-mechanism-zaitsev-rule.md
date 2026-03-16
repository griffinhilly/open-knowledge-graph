---
id: e1-mechanism-zaitsev-rule
title: E1 Elimination Mechanism and Zaitsev's Rule
domain: chemistry
course: organic-chemistry
prerequisites:
- id: e1-elimination
  type: hard
- id: carbocation-stability-rearrangement
  type: hard
- id: alkene-structure-and-nomenclature
  type: hard
builds-toward:
- competing-substitution-and-elimination
tags:
- e1
- elimination
- unimolecular
- zaitsev
- carbocation
stage: formal-systems
status: draft
---

# E1 Elimination Mechanism and Zaitsev's Rule

## Core Idea
E1 is a unimolecular elimination reaction that proceeds through a carbocation intermediate in a two-step process. Zaitsev's rule states that the major product is the alkene with the most substituted double bond (most stable alkene). E1 is favored under conditions similar to SN1: tertiary substrates, polar protic solvents, and high temperatures.

## Explainer

You know from studying E1 elimination that the mechanism has two discrete steps and that it passes through a carbocation intermediate. The first step — the **rate-determining step** — is ionization: the leaving group departs from the substrate, generating a carbocation. This is unimolecular, meaning only the substrate is involved in the slow step (hence "E1" — elimination, unimolecular). The second step is deprotonation: a base removes a proton from a carbon adjacent to the carbocation, and the electrons from that C–H bond form the new π bond of the alkene. Because the carbocation must form first, E1 is strongly favored at tertiary carbons, where the resulting carbocation is most stable — exactly the same reasoning that governs SN1 reactivity.

**Zaitsev's rule** addresses a question that arises when the carbocation intermediate has protons on more than one adjacent carbon: which proton gets removed, and therefore which alkene forms? The answer is that the **more substituted alkene** is the major product. If a tertiary carbocation has β-hydrogens on both a –CH₃ group and a –CH₂– group, removing a proton from the –CH₂– side produces a trisubstituted alkene, while removing one from the –CH₃ side produces a disubstituted alkene. The trisubstituted product predominates. The thermodynamic basis is straightforward: more substituted alkenes are more stable because of hyperconjugation — the adjacent C–H and C–C σ bonds donate electron density into the π* orbital of the double bond, lowering its energy. More substituents mean more hyperconjugative donors.

Think of it this way: the carbocation intermediate sits at an energy hilltop, and it can "fall" toward several possible alkene products. Each possible product represents a different valley, and Zaitsev's rule says the carbocation preferentially falls toward the *deepest* valley — the most stable alkene. This thermodynamic control makes sense because E1 reactions are typically run at elevated temperatures in polar protic solvents, conditions that favor equilibrium-like product distributions. The transition state for forming the more substituted alkene is lower in energy (by Hammond's postulate, it resembles the more stable product), so both kinetics and thermodynamics point in the same direction.

E1 competes with SN1 because both reactions share the same rate-determining step — carbocation formation. Once the carbocation forms, it can either be captured by a nucleophile (SN1) or lose a proton to form an alkene (E1). Higher temperature favors elimination because the ΔS term is more favorable (two molecules — alkene plus HB — form from one), and weaker, bulkier bases that are poor nucleophiles tip the balance toward E1. Recognizing that E1 and SN1 are parallel pathways from the same intermediate is essential for predicting product mixtures in real reactions, which rarely give 100% of one pathway.
