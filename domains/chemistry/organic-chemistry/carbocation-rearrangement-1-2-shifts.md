---
id: carbocation-rearrangement-1-2-shifts
title: 'Carbocation Rearrangement: 1,2-Hydride and 1,2-Alkyl Shifts'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carbocation-stability-rearrangement
  type: soft
- id: e1-elimination
  type: soft
- id: addition-to-alkynes
  type: soft
builds-toward:
- oxymercuration-mechanism
tags:
- mechanism
- rearrangement
- carbocation
- hydride-shift
- alkyl-shift
stage: formal-systems
status: draft
---

# Carbocation Rearrangement: 1,2-Hydride and 1,2-Alkyl Shifts

## Core Idea
Carbocations can undergo 1,2-hydride or 1,2-alkyl shifts from an adjacent carbon to form more stable carbocations. These rearrangements occur when a secondary carbocation can rearrange to a tertiary (more stable) one. The migrating group moves with its bonding electrons toward the carbocation center.

## How It's Best Learned
Identify secondary vs. tertiary carbocations and predict which rearrangements increase stability. Draw electron flow diagrams for hydride and alkyl shifts.

## Common Misconceptions
- Assuming all carbocations rearrange; rearrangement only occurs if it leads to a more stable carbocation.
- Misunderstanding the electron flow; the migrating group's bonding electrons move toward the positive charge, not away.

## Explainer

You already know that carbocations are classified by substitution — primary, secondary, tertiary — and that more substituted carbocations are more stable due to hyperconjugation and inductive effects. **Carbocation rearrangement** is the direct consequence of this stability hierarchy: if a reaction generates a less stable carbocation and a more stable one is just one bond-shift away, the rearrangement will happen, often faster than any competing reaction. This is not an optional side reaction — it is a thermodynamic imperative that the mechanism follows automatically.

A **1,2-hydride shift** is the most common rearrangement. Imagine a secondary carbocation on carbon-2 of a chain, with a tertiary carbon adjacent at carbon-3 bearing a hydrogen. The hydrogen on carbon-3 migrates *with its bonding electrons* to the positively charged carbon-2. The result: the positive charge has moved from carbon-2 (secondary) to carbon-3 (now tertiary, because the hydrogen left). Crucially, what migrates is not a bare proton (H⁺) — it is a hydride (H:⁻), carrying the bonding pair. The electron flow arrow points from the C–H bond toward the empty p orbital of the carbocation. This is why the shift is drawn as a curved arrow from the adjacent C–H bond to the cation center.

A **1,2-alkyl shift** (also called a 1,2-methyl shift when the migrating group is –CH₃) works identically, except an entire alkyl group migrates with its bonding electrons instead of a hydrogen. This occurs when no hydride shift can improve stability, but moving an alkyl group can. For example, a secondary carbocation adjacent to a quaternary carbon (which has no hydrogen to shift) can rearrange via methyl migration to form a tertiary carbocation. The principle is the same: the group moves toward the positive charge, carrying its electrons with it.

Not every carbocation rearranges. The shift only occurs if it leads to a *more stable* carbocation — secondary to tertiary, or secondary to a resonance-stabilized cation. A tertiary carbocation adjacent to another tertiary carbon has no driving force to rearrange and will proceed directly to product. When predicting products, always check: does the initially formed carbocation have a neighboring carbon that could donate a hydride or alkyl group to produce a more substituted cation? If yes, draw the rearranged intermediate *before* predicting the final product. Failing to check for rearrangement is one of the most common mistakes in organic mechanism problems, leading to incorrect regiochemistry in addition, substitution, and elimination products.
