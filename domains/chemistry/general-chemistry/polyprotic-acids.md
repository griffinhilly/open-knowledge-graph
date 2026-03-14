---
id: polyprotic-acids
title: Polyprotic Acids
domain: chemistry
course: general-chemistry
prerequisites:
- id: weak-acid-ionization
  type: hard
builds-toward:
- ph-and-acid-base-calculations
tags:
- diprotic
- triprotic
- Ka1
- Ka2
- Ka3
- sequential-ionization
- phosphoric-acid
- sulfuric-acid
stage: abstract-reasoning
status: draft
---
# Polyprotic Acids

## Core Idea
Polyprotic acids can donate more than one proton per molecule, ionizing in sequential steps. Each successive ionization has a smaller Ka (Ka₁ >> Ka₂ >> Ka₃) because removing a proton from an increasingly negative species requires more energy. For most polyprotic acids, the pH is determined almost entirely by the first ionization — the second and third contribute negligibly to [H⁺]. Sulfuric acid is a notable exception: its first ionization is strong (complete), so Ka₂ must be used for the second proton. Intermediate species (like HCO₃⁻ or H₂PO₄⁻) are amphoteric — they can act as either acid or base.

## How It's Best Learned
Solve the first ionization as a standard weak acid ICE table, then verify that the second ionization's contribution to [H⁺] is negligible (typically [H⁺] from Ka₂ ≈ Ka₂ itself when Ka₁ >> Ka₂). For the pH of an amphoteric intermediate, use the formula pH ≈ ½(pKa₁ + pKa₂).

## Common Misconceptions
- Students often try to solve all ionizations simultaneously. Because Ka₁ >> Ka₂, the ionizations can be treated as independent sequential equilibria — the first is solved, and its result becomes the initial condition for the second.
- The concentration of the doubly-deprotonated species is approximately equal to Ka₂ (not dependent on initial concentration), a counterintuitive result that follows directly from the algebra of sequential equilibria.
