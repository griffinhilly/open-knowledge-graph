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
stage: advanced
status: draft
---

# The Common Ion Effect

## Core Idea
The common ion effect occurs when a soluble salt sharing an ion with a sparingly soluble salt is added. The added ion shifts the dissolution equilibrium, decreasing the solubility of the sparingly soluble salt.

## Explainer

You already know from studying the solubility product constant (Ksp) that a sparingly soluble salt like silver chloride (AgCl) establishes an equilibrium between its solid form and its dissolved ions: AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq). The Ksp expression is Ksp = [Ag⁺][Cl⁻], and at a given temperature this product is a fixed number. In pure water, both ions dissolve in equal amounts until the ion product reaches Ksp — that defines the solubility.

Now imagine you dissolve the AgCl not in pure water, but in a solution that already contains chloride ions — say, a sodium chloride solution. NaCl is highly soluble and dissociates completely, flooding the solution with Cl⁻. This is the **common ion**: chloride is "common" to both the sparingly soluble salt (AgCl) and the added soluble salt (NaCl). Because the Ksp value cannot change at constant temperature, the equilibrium must adjust. With [Cl⁻] already elevated by the NaCl, the product [Ag⁺][Cl⁻] would exceed Ksp if AgCl tried to dissolve to the same extent as in pure water. So the equilibrium shifts to the left — less AgCl dissolves, and the concentration of Ag⁺ drops. The silver chloride becomes *less* soluble in the NaCl solution than in pure water.

Think of it like a room with a fixed capacity. If half the seats are already taken by chloride ions from NaCl, there is less room for the chloride ions that would come from dissolving AgCl, and consequently less Ag⁺ enters solution too. The Ksp acts as the fixed capacity — it sets the maximum ion product, and any ion already present from another source counts toward that limit. This is Le Chatelier's principle applied to dissolution equilibria: adding a product (the common ion) shifts the equilibrium back toward the reactant (the undissolved solid).

The common ion effect has direct practical applications. In qualitative analysis, adding HCl to a solution containing Ag⁺ exploits the common ion effect to precipitate AgCl more completely than pure water would allow. In buffer solutions — which you will study next — the common ion effect explains why adding a salt of a weak acid's conjugate base suppresses the acid's dissociation, stabilizing the pH. Whenever you see an equilibrium involving ions and want to push it in one direction, flooding the solution with one of those ions is a powerful and predictable tool.
