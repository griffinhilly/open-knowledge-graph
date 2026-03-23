---
id: dilution-and-solution-preparation
title: Dilution Calculations and Solution Preparation
domain: chemistry
course: general-chemistry
prerequisites:
- id: concentration-and-molarity
  type: hard
- id: proportions
  type: hard
builds-toward:
- colligative-properties-solutions
tags:
- dilution
- M₁V₁ = M₂V₂
- concentration
stage: formal-systems
status: draft
---

# Dilution Calculations and Solution Preparation

## Core Idea
When a solution is diluted by adding solvent, the moles of solute remain constant while volume increases, decreasing molarity. The dilution equation M₁V₁ = M₂V₂ relates initial and final molarity and volume. Proper solution preparation involves dissolving a solute, then diluting to the mark in a volumetric flask to ensure accurate concentration.

## Questions

```yaml
- question: "A student needs to prepare 200 mL of 0.50 M NaCl from a 4.0 M stock solution. How many mL of stock should they use?"
  type: multiple-choice
  options:
    - "400 mL — calculated as (0.50 / 4.0) × 200"
    - "25 mL — calculated as M₁V₁ = M₂V₂: (4.0)(V₁) = (0.50)(200)"
    - "100 mL — calculated by dividing both concentrations"
    - "160 mL — the volume of water needed after taking stock solution"
  answer: 1
  explanation: "Applying M₁V₁ = M₂V₂: (4.0 M)(V₁) = (0.50 M)(200 mL), so V₁ = 25 mL. The student takes 25 mL of stock and dilutes it to a total volume of 200 mL (not adds 200 mL of water). Option D (160 mL) is a common error: it represents the volume of water to add (200 − 25 = 175 mL, though option D shows 160 suggesting an arithmetic error), confusing 'volume of solvent added' with 'final volume.' The equation always uses final total volume, not the volume of solvent added."

- question: "A student prepares a solution by dissolving the correct mass of solute in a beaker, then transfers it to a 500 mL graduated cylinder and adds water until the volume reads 500 mL. Another student uses a 500 mL volumetric flask and fills to the calibration mark. Whose preparation is more accurate, and why?"
  type: multiple-choice
  options:
    - "Both are equally accurate — graduated cylinders and volumetric flasks have the same precision"
    - "The volumetric flask method is more accurate because volumetric flasks are calibrated to contain an exact volume, while graduated cylinders have much wider tolerances"
    - "The graduated cylinder method is more accurate because graduated cylinders have finer graduations for reading small volume differences"
    - "Neither is accurate — accurate solutions must be prepared using a balance, not volumetric glassware"
  answer: 1
  explanation: "Volumetric flasks are calibrated to contain a single exact volume at a specific temperature, with tolerances of ±0.1–0.3 mL at 500 mL. Graduated cylinders are designed for approximate volume measurement, with tolerances of ±2–5 mL at the same scale. For a 500 mL solution, a 5 mL error translates to a ~1% concentration error — which matters significantly in quantitative chemistry. This is why the standard procedure specifies diluting 'to the mark' in a volumetric flask, not adding a measured volume of solvent to the dissolved solute."

- question: "When you dilute a solution by adding water, both the number of moles of solute and the molarity decrease."
  type: true-false
  answer: false
  explanation: "False — this is the central misconception that the dilution equation corrects. When you add water to a solution, the moles of solute do not change: all the solute molecules are still present, just distributed through a larger volume. Only the molarity decreases (because molarity = moles/volume, and volume increases while moles stay constant). This conservation of moles is the entire logical foundation of M₁V₁ = M₂V₂: since moles = M×V, and moles are conserved, M₁V₁ must equal M₂V₂."

- question: "The dilution equation M₁V₁ = M₂V₂ works with any volume unit (mL, L, etc.) as long as both V₁ and V₂ are expressed in the same unit."
  type: true-false
  answer: true
  explanation: "True. The equation comes from setting moles equal on both sides: n = M₁V₁ = M₂V₂. If you use liters, molarity cancels properly (mol/L × L = mol). If you use mL on both sides, the mL units cancel (mol/L × mL = mol/L × mL on both sides — and you can express M in mol/mL if you prefer, or simply note that the volume units cancel in the ratio). The key constraint is consistency: V₁ and V₂ must be in the same unit so that the volume units cancel correctly across the equation."

- question: "Explain why moles of solute are conserved during dilution, and show how this conservation leads directly to the equation M₁V₁ = M₂V₂."
  type: short-answer
  answer: "Dilution adds only solvent — no solute molecules are created or destroyed. Since the number of solute molecules is unchanged, the moles of solute before and after dilution are equal: n₁ = n₂. From the definition of molarity, moles = molarity × volume (in liters), so n = MV. Substituting: M₁V₁ = n₁ = n₂ = M₂V₂, giving M₁V₁ = M₂V₂. This equation is not a separate formula to memorize — it is simply the statement that moles are conserved, written in terms of the measurable quantities molarity and volume."
  explanation: "Understanding the derivation rather than memorizing the equation prevents common errors like using the volume of solvent added instead of the final total volume. If you know the equation comes from mole conservation, you can re-derive it on the fly and catch errors by checking whether the moles of solute are the same on both sides. The same reasoning applies to serial dilutions (each step conserves moles), aliquot calculations, and any other scenario involving changing volumes of a solution."
```

## Explainer

From your work with concentration and molarity, you know that molarity (M) equals moles of solute divided by liters of solution. Dilution is simply the act of adding more solvent to an existing solution — the solute molecules are still all there, just spread through a larger volume. This one insight — that **moles of solute do not change during dilution** — is the entire logical foundation of the dilution equation.

Since moles stay constant, and moles = molarity × volume, you can write: **M₁V₁ = M₂V₂**. The subscript 1 refers to the concentrated (initial) solution and subscript 2 to the dilute (final) solution. This equation works with any volume units as long as both sides use the same unit, because the conversion factor cancels. For example, if you have 50 mL of 6.0 M HCl and want to know the concentration after diluting to 300 mL: (6.0)(50) = M₂(300), giving M₂ = 1.0 M. You can also solve the equation in the other direction — "what volume of 12 M stock do I need to make 500 mL of 0.10 M solution?" — which is the question you face most often in lab preparation.

In practice, preparing a solution from a solid solute follows a specific procedure designed for accuracy. You calculate the required mass of solute using its molar mass, weigh it on an analytical balance, dissolve it in a beaker with less solvent than the final volume, transfer the solution quantitatively to a **volumetric flask** (rinsing the beaker to capture all solute), and then add solvent to the calibration mark. The volumetric flask is calibrated to contain an exact volume at a specific temperature — this is why you dilute *to the mark* rather than adding a measured volume of solvent to the solute. Using a graduated cylinder or beaker to measure the final volume would introduce significant error because their calibration tolerances are much wider.

The same proportional reasoning from your math background applies here: dilution is a direct application of the concept that when one factor in a product increases (volume), the other must decrease (concentration) to keep the product (moles) constant. This relationship extends beyond simple dilutions — whenever you pipette an aliquot, prepare a serial dilution series, or calculate how much reagent to add to achieve a target concentration, you are applying M₁V₁ = M₂V₂ in one form or another.
