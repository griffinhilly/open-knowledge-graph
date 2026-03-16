---
id: hydroboration-oxidation-alkenes
title: 'Hydroboration-Oxidation: Anti-Markovnikov Hydration'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: electrophilic-addition-to-alkenes
  type: hard
- id: markovnikov-rule-regioselectivity
  type: hard
builds-toward:
- alcohol-oxidation-to-carbonyls
tags:
- addition
- hydroboration
- alcohol-synthesis
- non-markovnikov
stage: formal-systems
status: draft
---

# Hydroboration-Oxidation: Anti-Markovnikov Hydration

## Core Idea
Hydroboration-oxidation converts alkenes to primary alcohols (or secondary from internal alkenes) with anti-Markovnikov regiochemistry and syn stereochemistry. Borane (BH₃) adds to the alkene such that hydride goes to the more substituted carbon and boron to the less substituted carbon; oxidation with H₂O₂/OH⁻ replaces B with OH while inverting the stereochemistry of that position.

## How It's Best Learned
Draw the borane addition, hydride migration, and oxidation steps. Compare the overall regiochemistry and stereochemistry to standard HX addition and understand why hydroboration is synthetically valuable for anti-Markovnikov products.

## Common Misconceptions
- Confusing which carbon receives B vs. H; boron attaches to the less substituted carbon (opposite of H in Markovnikov additions).
- Forgetting the inverting nature of the oxidation step after the initial syn addition of borane.

## Explainer

You know from electrophilic addition that when HX adds to an unsymmetrical alkene, Markovnikov's rule places the hydrogen on the carbon with more hydrogens and the halide on the more substituted carbon. **Hydroboration-oxidation** is the essential complement to this reaction: it achieves the *opposite* regiochemistry, placing the hydroxyl group on the less substituted carbon to give an **anti-Markovnikov alcohol**. This makes it one of the most synthetically valuable reactions in the alkene toolkit — it gives you the product that acid-catalyzed hydration cannot.

The reaction proceeds in two distinct stages. In the **hydroboration step**, borane (BH₃, typically used as the THF complex) adds across the double bond in a single concerted step — no carbocation intermediate is formed. Boron is electrophilic (it has an empty p orbital) and the alkene's pi electrons attack it, while simultaneously a hydrogen transfers from boron to the adjacent carbon. Because both the B–C and H–C bonds form on the same face of the double bond in this four-centered transition state, the addition is **syn** (both groups add to the same side). Crucially, boron ends up on the **less substituted carbon** and hydrogen on the more substituted carbon. This regiochemistry arises because boron, the larger atom, preferentially goes to the less sterically hindered position, and because the transition state has partial negative charge on the carbon receiving boron — the more substituted carbon better stabilizes the partial positive charge on the other carbon.

Since BH₃ has three B–H bonds, it can add across three equivalents of alkene, producing a **trialkylborane** (R₃B). The second stage is **oxidation**: treating the trialkylborane with hydrogen peroxide (H₂O₂) in aqueous base (NaOH). This replaces each B–C bond with a HO–C bond. The mechanism involves nucleophilic attack of the hydroperoxide anion (HOO⁻) on boron, followed by a 1,2-alkyl migration from boron to oxygen — critically, this migration occurs with **retention of configuration** at the carbon that migrates. Since the boron was originally placed by syn addition, and the oxidation retains the configuration at that carbon, the net result is that OH replaces B in exactly the same position and on the same face.

The overall outcome — anti-Markovnikov regiochemistry and syn stereochemistry — is unique to hydroboration-oxidation. Contrast this with acid-catalyzed hydration (Markovnikov, no stereochemical control because of the planar carbocation) and oxymercuration (Markovnikov, anti addition). By choosing among these three methods, you can place a hydroxyl group on either carbon of an unsymmetrical alkene with predictable stereochemistry. This is the kind of reagent-controlled selectivity that makes retrosynthetic planning possible.
