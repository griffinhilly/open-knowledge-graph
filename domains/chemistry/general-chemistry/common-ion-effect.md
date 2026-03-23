---
id: common-ion-effect
title: The Common Ion Effect
domain: chemistry
course: general-chemistry
prerequisites:
- id: solubility-product-constant-ksp
  type: hard
- id: ionic-bonding
  type: soft
builds-toward:
- buffer-solutions
- precipitation-titration
tags:
- common ion effect
- solubility reduction
- equilibrium
stage: formal-systems
status: validated
---

# The Common Ion Effect

## Core Idea
The common ion effect occurs when a soluble salt sharing an ion with a sparingly soluble salt is added. The added ion shifts the dissolution equilibrium, decreasing the solubility of the sparingly soluble salt.

## Questions

```yaml
- question: "Silver chloride (AgCl) has a fixed Ksp at a given temperature. When sodium chloride (NaCl) is dissolved in the same solution, what happens to the amount of AgCl that dissolves?"
  type: multiple-choice
  options:
    - "More AgCl dissolves because NaCl increases the overall ionic strength of the solution"
    - "Less AgCl dissolves because the added Cl⁻ shifts the dissolution equilibrium toward undissolved solid"
    - "The same amount dissolves because the Ksp value is unchanged"
    - "More AgCl dissolves because Na⁺ ions pair with Cl⁻, freeing up capacity for AgCl to dissolve"
  answer: 1
  explanation: "Ksp is fixed, so with [Cl⁻] already elevated by NaCl, the product [Ag⁺][Cl⁻] would exceed Ksp if AgCl dissolved to the same extent as in pure water. The equilibrium shifts left, reducing [Ag⁺] and therefore reducing AgCl solubility. Option C is the classic mistake: Ksp doesn't change, but solubility does — the pre-existing Cl⁻ uses up part of the ion-product 'budget.'"

- question: "In qualitative analysis, adding concentrated HCl to a solution is used to precipitate Ag⁺ as AgCl more completely than plain water would allow. Which principle best explains why HCl is more effective?"
  type: multiple-choice
  options:
    - "HCl lowers the pH, which destabilizes the Ag⁺ ion in solution"
    - "The common ion effect: excess Cl⁻ from HCl shifts the AgCl dissolution equilibrium toward the solid"
    - "HCl increases the Ksp of AgCl by changing the temperature of the solution"
    - "HCl reacts directly with Ag⁺ to form a covalent AgCl complex"
  answer: 1
  explanation: "HCl fully dissociates, flooding the solution with Cl⁻. This common ion (shared with AgCl) shifts the equilibrium AgCl(s) ⇌ Ag⁺ + Cl⁻ to the left, driving more AgCl to precipitate. The pH effect of HCl is irrelevant here; it is purely an application of Le Chatelier's principle to the dissolution equilibrium."

- question: "The common ion effect reduces solubility only when the added salt shares the cation with the sparingly soluble compound — a shared anion has no effect."
  type: true-false
  answer: false
  explanation: "The common ion effect works when EITHER the cation OR the anion is shared. Adding NaCl to AgCl(s) solution suppresses solubility through the common Cl⁻ anion; adding AgNO₃ would suppress it through the common Ag⁺ cation. Any ion that appears in the Ksp expression counts — the constraint is just that Ksp = [Ag⁺][Cl⁻] must not be exceeded."

- question: "Adding NaCl to a saturated AgCl solution causes the concentration of Ag⁺ to decrease, even though no Ag⁺ is added or removed directly."
  type: true-false
  answer: true
  explanation: "Because Ksp = [Ag⁺][Cl⁻] is fixed, increasing [Cl⁻] via NaCl forces [Ag⁺] to decrease proportionally. AgCl precipitates until the ion product falls back to Ksp at a lower [Ag⁺]. This is Le Chatelier's principle in action: adding a product (Cl⁻) drives the equilibrium toward the reactant (solid AgCl), reducing the concentration of the other product (Ag⁺)."

- question: "Explain why the solubility of a sparingly soluble salt decreases when a soluble salt sharing one of its ions is added, even though the Ksp value itself does not change."
  type: short-answer
  answer: "Ksp sets the maximum value of the ion-product at equilibrium. When a common ion is added from a separate soluble salt, the concentration of that ion rises immediately, pushing the ion product above Ksp. To restore equilibrium, the sparingly soluble salt precipitates — shifting the equilibrium left — until the ion product returns to Ksp. At this new equilibrium, the concentration of the other ion (not added externally) is lower than it was in pure water. Solubility is defined as how much of the sparingly soluble salt dissolves, and since less of it is in solution, its solubility has decreased — all while Ksp remains constant."
  explanation: "The key is that Ksp constrains the product of ion concentrations, not either concentration individually. A fixed product means the two concentrations trade off: raise one and the other must fall. The common ion effect is simply the practical consequence of this constraint when an outside source contributes one of the ions."
```

## Explainer

You already know from studying the solubility product constant (Ksp) that a sparingly soluble salt like silver chloride (AgCl) establishes an equilibrium between its solid form and its dissolved ions: AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq). The Ksp expression is Ksp = [Ag⁺][Cl⁻], and at a given temperature this product is a fixed number. In pure water, both ions dissolve in equal amounts until the ion product reaches Ksp — that defines the solubility.

Now imagine you dissolve the AgCl not in pure water, but in a solution that already contains chloride ions — say, a sodium chloride solution. NaCl is highly soluble and dissociates completely, flooding the solution with Cl⁻. This is the **common ion**: chloride is "common" to both the sparingly soluble salt (AgCl) and the added soluble salt (NaCl). Because the Ksp value cannot change at constant temperature, the equilibrium must adjust. With [Cl⁻] already elevated by the NaCl, the product [Ag⁺][Cl⁻] would exceed Ksp if AgCl tried to dissolve to the same extent as in pure water. So the equilibrium shifts to the left — less AgCl dissolves, and the concentration of Ag⁺ drops. The silver chloride becomes *less* soluble in the NaCl solution than in pure water.

Think of it like a room with a fixed capacity. If half the seats are already taken by chloride ions from NaCl, there is less room for the chloride ions that would come from dissolving AgCl, and consequently less Ag⁺ enters solution too. The Ksp acts as the fixed capacity — it sets the maximum ion product, and any ion already present from another source counts toward that limit. This is Le Chatelier's principle applied to dissolution equilibria: adding a product (the common ion) shifts the equilibrium back toward the reactant (the undissolved solid).

The common ion effect has direct practical applications. In qualitative analysis, adding HCl to a solution containing Ag⁺ exploits the common ion effect to precipitate AgCl more completely than pure water would allow. In buffer solutions — which you will study next — the common ion effect explains why adding a salt of a weak acid's conjugate base suppresses the acid's dissociation, stabilizing the pH. Whenever you see an equilibrium involving ions and want to push it in one direction, flooding the solution with one of those ions is a powerful and predictable tool.
