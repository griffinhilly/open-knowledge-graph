---
id: hydroboration-oxidation-anti-markovnikov
title: 'Hydroboration-Oxidation: Anti-Markovnikov Addition'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: alkene-structure-and-nomenclature
  type: hard
builds-toward:
- catalytic-hydrogenation-lindlar-catalyst
tags:
- hydroboration
- oxidation
- anti-markovnikov
- syn-addition
- alcohols
stage: formal-systems
status: draft
---

# Hydroboration-Oxidation: Anti-Markovnikov Addition

## Core Idea
Hydroboration-oxidation is a two-step sequence: first, borane (BH₃) adds to the alkene in a syn manner (both atoms add from the same face) and anti-Markovnikov manner (B adds to the less substituted carbon); then, hydrogen peroxide oxidizes the C-B bond to C-OH, inverting stereochemistry at that center. This sequence provides primary alcohols from terminal alkenes and secondary alcohols from internal alkenes with predictable regioselectivity and stereochemistry.

## Explainer

From electrophilic addition to alkenes, you know that adding HBr or H₂O across a double bond typically follows Markovnikov's rule — the electrophile (H⁺) adds to the less substituted carbon, forming the more stable carbocation at the more substituted position, and the nucleophile (Br⁻ or OH⁻) ends up there. **Hydroboration-oxidation** achieves the opposite regiochemistry: the hydroxyl group ends up on the *less* substituted carbon, giving **anti-Markovnikov** addition. This complementary selectivity makes it one of the most important reactions in your synthetic toolkit.

The first step is **hydroboration**: borane (BH₃, often used as the THF complex BH₃·THF) adds across the double bond in a single concerted step — no carbocation intermediate forms. Boron is electron-deficient (it has an empty p orbital), so it acts as the electrophile, but because the addition is concerted rather than stepwise, both the B–H bond and the new C–B and C–H bonds form simultaneously through a four-membered transition state. Boron, being the larger atom, preferentially bonds to the **less sterically hindered** (less substituted) carbon. This steric preference is what produces anti-Markovnikov regiochemistry — it has nothing to do with carbocation stability because no carbocation ever forms. The concerted mechanism also ensures **syn addition**: boron and hydrogen both add from the same face of the double bond.

The second step is **oxidation**: treating the organoborane intermediate with hydrogen peroxide (H₂O₂) in aqueous NaOH replaces the C–B bond with a C–OH bond. The oxygen inserts between carbon and boron through a 1,2-migration with **retention of configuration** at the carbon that was bonded to boron. The net result is that the OH ends up exactly where the boron was — on the less substituted carbon, on the same face where addition occurred.

Consider 1-methylcyclohexene as a concrete example. Acid-catalyzed hydration (Markovnikov) would give 1-methylcyclohexanol — OH on the more substituted carbon. Hydroboration-oxidation gives *trans*-2-methylcyclohexanol — OH on the less substituted carbon, with syn stereochemistry. Having both reactions available means you can place the hydroxyl group on either carbon of an unsymmetrical alkene, choosing Markovnikov or anti-Markovnikov addition by choosing the appropriate reagent. This is the power of understanding mechanism over memorizing outcomes: the concerted, non-carbocation pathway of hydroboration is *why* it gives the "opposite" regiochemistry.
