---
id: complex-ions-and-stability
title: Stability of Complex Ions and Formation Constants
domain: chemistry
course: general-chemistry
prerequisites:
- id: coordination-chemistry-basics
  type: hard
- id: chemical-equilibrium
  type: hard
builds-toward:
- complexometric-titration
- solubility-product-constant-ksp
tags:
- complex stability
- formation constant
- coordination equilibrium
stage: formal-systems
status: draft
---

# Stability of Complex Ions and Formation Constants

## Core Idea
Complex ion stability is measured by the formation constant Kf. Higher Kf values indicate more stable complexes. Equilibrium calculations for complex formation parallel those for other equilibrium systems.

## Explainer

From coordination chemistry basics, you know that a **complex ion** forms when a central metal ion bonds to surrounding molecules or ions called **ligands** through coordinate covalent bonds — bonds where the ligand donates both electrons. The question this topic addresses is: how tightly do those ligands hold on? Not all complex ions are created equal. Some fall apart readily when conditions change, while others are so stable they persist even in highly dilute solutions. The **formation constant (Kf)** quantifies this stability, and it works exactly like the equilibrium constants you already know from chemical equilibrium.

Consider copper(II) ions in water reacting with four ammonia molecules to form the deep blue tetraamminecopper(II) complex: Cu²⁺(aq) + 4NH₃(aq) ⇌ [Cu(NH₃)₄]²⁺(aq). The formation constant for this equilibrium is Kf = [Cu(NH₃)₄²⁺] / ([Cu²⁺][NH₃]⁴), and its value is approximately 1 × 10¹³. That enormous number tells you the equilibrium lies overwhelmingly to the right — once the complex forms, very little free Cu²⁺ remains in solution. Compare this to a complex with Kf = 10³, where appreciable amounts of free metal ion coexist with the complex at equilibrium. The magnitude of Kf directly indicates how completely the metal is "locked up" by its ligands.

In practice, complex formation often occurs in **stepwise** fashion rather than all at once. The four ammonia ligands in the copper example do not all attach simultaneously — they add one at a time, each step with its own equilibrium constant (K₁, K₂, K₃, K₄). The overall Kf is the product of these stepwise constants: Kf = K₁ × K₂ × K₃ × K₄. Typically, each successive constant is smaller than the previous one, because as more ligands crowd around the metal center, it becomes statistically and sterically harder to add the next one. Working with stepwise constants lets you predict the dominant species at any given ligand concentration — a skill that becomes essential for complexometric titrations.

The stability of a complex ion has real chemical consequences beyond the equilibrium calculation itself. A highly stable complex effectively removes free metal ions from solution, which can shift other equilibria. For example, adding ammonia to a solution containing insoluble AgCl dissolves the solid — not because ammonia attacks chloride, but because it forms the very stable [Ag(NH₃)₂]⁺ complex, pulling Ag⁺ out of solution and shifting the solubility equilibrium to produce more dissolved silver. This interplay between complex formation and solubility equilibria is a powerful analytical and synthetic tool, and it illustrates how Kf values connect to the broader framework of competing equilibria you have been building throughout general chemistry.
