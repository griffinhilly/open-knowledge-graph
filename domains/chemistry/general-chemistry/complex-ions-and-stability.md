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

## Questions

```yaml
- question: "A saturated solution of AgCl (Ksp ≈ 1.8 × 10⁻¹⁰) has very low [Ag⁺]. Excess aqueous ammonia is added and AgCl begins to dissolve. Why?"
  type: multiple-choice
  options:
    - "Ammonia reacts with Cl⁻ to form NH₄Cl, removing chloride and pulling the equilibrium toward dissolution"
    - "Ammonia forms [Ag(NH₃)₂]⁺, a stable complex with large Kf, drastically lowering [Ag⁺] and shifting the solubility equilibrium toward more dissolved AgCl"
    - "Ammonia raises pH, which generally increases the solubility of ionic compounds"
    - "Ammonia increases ionic strength, raising the activity of Ag⁺ and pulling more Cl⁻ into solution"
  answer: 1
  explanation: "This is competing equilibria in action. AgCl dissolves according to AgCl(s) ⇌ Ag⁺ + Cl⁻ (Ksp very small). Ammonia forms [Ag(NH₃)₂]⁺ with a large Kf ≈ 1.7 × 10⁷. Complex formation removes free Ag⁺ from solution, dropping [Ag⁺] below the value consistent with the solubility equilibrium. Le Chatelier's principle drives AgCl to dissolve further to replenish Ag⁺ — which is immediately complexed again. This continuous removal of Ag⁺ by complexation drives dissolution far beyond what Ksp alone would allow. Ammonia is not reacting with Cl⁻ (option A), and the pH and ionic-strength effects (options C and D) are not the operative mechanism here."

- question: "Complex A has Kf = 1 × 10²⁰ and Complex B has Kf = 1 × 10⁵. Equal concentrations of both metal ions compete for a limiting amount of ligand. Which complex forms predominantly?"
  type: multiple-choice
  options:
    - "Complex B, because less stable complexes form faster kinetically"
    - "Equal amounts, because Kf only describes equilibrium ratios, not competition between different metals"
    - "Complex A, because the larger Kf means its equilibrium position strongly favors complex over free metal, out-competing B for the available ligand"
    - "Neither predominates — Kf values describe different reactions and cannot be directly compared"
  answer: 2
  explanation: "Kf is an equilibrium constant that directly compares how completely different metal ions are complexed at equilibrium. Complex A's Kf is 10¹⁵ times larger than B's, meaning A's equilibrium lies overwhelmingly further toward the complex. With limiting ligand, both reactions compete for the same resource, and the reaction with the vastly larger Kf captures essentially all available ligand. Option A incorrectly conflates thermodynamics with kinetics — Kf describes where equilibrium lies, not how fast it is reached. Option B is wrong because Kf values for reactions using the same ligand can absolutely be compared to predict selectivity."

- question: "The overall formation constant Kf for a complex that forms in n stepwise stages equals the product of all n stepwise formation constants."
  type: true-false
  answer: true
  explanation: "This follows from the standard rule for combining equilibrium constants: when successive reactions are summed to give an overall reaction, their equilibrium constants multiply. Each stepwise constant Ki describes one ligand addition: [MLᵢ]/([MLᵢ₋₁][L]). Summing all n steps to give M + nL ⇌ MLn produces an overall Kf = K₁ × K₂ × ⋯ × Kn. This is why Kf values for complexes with many ligands can reach astronomically large numbers — multiplying several successive stepwise constants compounds the effect even if each individual step is modest."

- question: "A complex ion with a large Kf will be present in appreciable concentration only at high ligand concentrations, because most of the metal remains as the free aquo complex at lower ligand levels."
  type: true-false
  answer: false
  explanation: "This reverses the meaning of Kf. A large Kf means the equilibrium lies far toward the complex — at equilibrium, essentially all metal is complexed and very little remains as free ion, even at moderate ligand concentrations. For [Cu(NH₃)₄]²⁺ with Kf ≈ 10¹³, even modest NH₃ concentrations lock up virtually all Cu²⁺. A small Kf would indicate a weak complex requiring high ligand concentrations to form appreciably. Since Kf = [complex]/([free metal][ligand]ⁿ), a large Kf means a large numerator and tiny denominator at equilibrium."

- question: "Explain how the formation constant Kf connects to competing equilibria, using the dissolution of an insoluble metal salt in the presence of a complexing ligand as your example."
  type: short-answer
  answer: "Kf quantifies how completely complexation proceeds at equilibrium. When a complexing ligand is added to a solution in contact with an insoluble salt (e.g., AgCl + NH₃), two equilibria operate through a shared species (Ag⁺): dissolution (AgCl ⇌ Ag⁺ + Cl⁻, governed by Ksp) and complexation (Ag⁺ + 2NH₃ ⇌ [Ag(NH₃)₂]⁺, governed by Kf). A large Kf means complexation removes free Ag⁺ rapidly and nearly completely, driving [Ag⁺] far below the value consistent with the solubility equilibrium. Le Chatelier's principle pushes the dissolution equilibrium right to replenish Ag⁺, which is immediately re-complexed. The overall process couples both equilibria: the net equilibrium constant for AgCl dissolving into the complex equals Ksp × Kf, and when Kf is large enough, this product makes the overall process thermodynamically favorable."
  explanation: "The key is coupling through a shared species: when Kf effectively eliminates free Ag⁺, the solubility equilibrium is forced right to compensate, dissolving an otherwise insoluble solid."
```

## Explainer

From coordination chemistry basics, you know that a **complex ion** forms when a central metal ion bonds to surrounding molecules or ions called **ligands** through coordinate covalent bonds — bonds where the ligand donates both electrons. The question this topic addresses is: how tightly do those ligands hold on? Not all complex ions are created equal. Some fall apart readily when conditions change, while others are so stable they persist even in highly dilute solutions. The **formation constant (Kf)** quantifies this stability, and it works exactly like the equilibrium constants you already know from chemical equilibrium.

Consider copper(II) ions in water reacting with four ammonia molecules to form the deep blue tetraamminecopper(II) complex: Cu²⁺(aq) + 4NH₃(aq) ⇌ [Cu(NH₃)₄]²⁺(aq). The formation constant for this equilibrium is Kf = [Cu(NH₃)₄²⁺] / ([Cu²⁺][NH₃]⁴), and its value is approximately 1 × 10¹³. That enormous number tells you the equilibrium lies overwhelmingly to the right — once the complex forms, very little free Cu²⁺ remains in solution. Compare this to a complex with Kf = 10³, where appreciable amounts of free metal ion coexist with the complex at equilibrium. The magnitude of Kf directly indicates how completely the metal is "locked up" by its ligands.

In practice, complex formation often occurs in **stepwise** fashion rather than all at once. The four ammonia ligands in the copper example do not all attach simultaneously — they add one at a time, each step with its own equilibrium constant (K₁, K₂, K₃, K₄). The overall Kf is the product of these stepwise constants: Kf = K₁ × K₂ × K₃ × K₄. Typically, each successive constant is smaller than the previous one, because as more ligands crowd around the metal center, it becomes statistically and sterically harder to add the next one. Working with stepwise constants lets you predict the dominant species at any given ligand concentration — a skill that becomes essential for complexometric titrations.

The stability of a complex ion has real chemical consequences beyond the equilibrium calculation itself. A highly stable complex effectively removes free metal ions from solution, which can shift other equilibria. For example, adding ammonia to a solution containing insoluble AgCl dissolves the solid — not because ammonia attacks chloride, but because it forms the very stable [Ag(NH₃)₂]⁺ complex, pulling Ag⁺ out of solution and shifting the solubility equilibrium to produce more dissolved silver. This interplay between complex formation and solubility equilibria is a powerful analytical and synthetic tool, and it illustrates how Kf values connect to the broader framework of competing equilibria you have been building throughout general chemistry.
