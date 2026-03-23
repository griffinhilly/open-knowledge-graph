---
id: concentration-and-molarity
title: Concentration Units and Molarity Calculations
domain: chemistry
course: general-chemistry
prerequisites:
- id: the-mole-concept-and-avogadro
  type: hard
- id: solution-properties
  type: hard
- id: ratios
  type: soft
builds-toward:
- dilution-and-solution-preparation
- colligative-properties-solutions
tags:
- molarity
- concentration
- M
- mol/L
stage: formal-systems
status: validated
---

# Concentration Units and Molarity Calculations

## Core Idea
Molarity (M) is moles of solute per liter of solution: M = n/V. It is the most common unit for solution concentration in chemistry. Other units include molality (moles per kg solvent), mass percent, and parts per million. Molarity allows chemists to calculate reactant amounts in solution-based reactions.

## Questions

```yaml
- question: "A student dissolves 0.50 mol of NaCl into 0.80 L of water. The resulting solution has a total volume of 1.00 L. What is the molarity of the solution?"
  type: multiple-choice
  options:
    - "0.625 M — calculated as 0.50 mol ÷ 0.80 L (liters of water used)"
    - "0.50 M — calculated as 0.50 mol ÷ 1.00 L (liters of solution)"
    - "0.40 M — calculated as the average of the solute moles and total volume"
    - "1.00 M — because 0.50 mol in 0.50 L of water gives 1.0 M before dilution"
  answer: 1
  explanation: "Molarity = moles of solute ÷ liters of solution. The denominator is the total volume of the final solution (1.00 L), not the volume of solvent added (0.80 L). Using 0.80 L gives 0.625 M — the most common error, and the misconception option A represents. The final solution volume is what matters because molarity is defined with respect to the container holding the complete mixture. In practice, you would add solute to a volumetric flask and fill to the calibration mark with solvent — the 1.00 L is the endpoint, not the starting water volume."

- question: "You need exactly 0.25 moles of HCl for a reaction. You have a 0.50 M HCl stock solution. What volume of stock solution should you measure out?"
  type: multiple-choice
  options:
    - "0.125 L — because 0.25 mol × 0.50 M = 0.125"
    - "0.50 L — because 0.25 mol ÷ 0.50 M = 0.50 L"
    - "0.50 L — because 0.50 M solution contains 0.50 mol per 0.50 L"
    - "2.0 L — because 0.25 mol × (1 L / 0.50 mol) = 0.50... wait, you need more"
  answer: 1
  explanation: "Rearranging M = n/V gives V = n/M = 0.25 mol ÷ 0.50 mol/L = 0.50 L. You measure 500 mL of the stock solution, which contains exactly 0.50 mol/L × 0.50 L = 0.25 mol of HCl. Option A is a dimensional-analysis error that multiplies instead of divides. This calculation — converting a mole requirement into a volume measurement — is the core practical application of molarity, used in every titration, dilution, and solution-based synthesis."

- question: "To prepare a 1.0 M solution of NaCl, you should dissolve 1.0 mol of NaCl in exactly 1.0 L of water (solvent)."
  type: true-false
  answer: false
  explanation: "This is the single most common error in solution preparation. Molarity is defined as moles per liter of *solution*, not moles per liter of *solvent*. Adding 1.0 mol of NaCl to 1.0 L of water typically produces a final solution volume greater than 1.0 L (the solute occupies space). To make exactly 1.0 M, you would dissolve the solute in a smaller amount of solvent, then add additional solvent until the total solution volume reaches exactly 1.0 L — which is what a volumetric flask's calibration mark indicates."

- question: "Molality is preferred over molarity for colligative property calculations because molality does not change with temperature, while molarity does."
  type: true-false
  answer: true
  explanation: "Molarity uses volume of solution in its denominator. As temperature changes, liquids expand or contract, changing the solution volume and therefore the molarity — even if the moles of solute and mass of solvent are unchanged. Molality uses mass of solvent (kg), which is temperature-independent. For colligative properties like boiling point elevation and freezing point depression, whose magnitude depends on the number of solute particles per unit solvent mass, molality gives a temperature-stable measure that does not drift as conditions change."

- question: "Explain why molarity is defined using liters of solution rather than liters of solvent, and give an example of why this distinction matters in practice."
  type: short-answer
  answer: "Molarity measures how many moles of solute are present in a given volume of the final solution. Using solution volume (not solvent volume) ensures that when you measure out a given volume with a pipette or graduated cylinder, you know exactly how many moles you have obtained — because the solution is what you actually handle. If molarity used solvent volume, you would need to know how much the solute changed the total volume before calculating moles, which is impractical. In practice: to make 1.0 M NaCl, you dissolve NaCl in some water, then add water until the total solution volume reaches exactly 1.0 L in a volumetric flask. Adding 1.0 mol to 1.0 L of water gives slightly more than 1.0 L of solution and therefore slightly less than 1.0 M."
  explanation: "The distinction matters most in concentrated solutions, where the solute contribution to total volume is significant. For very dilute aqueous solutions, the difference between solution volume and solvent volume is negligible, which is why the error 'dissolve in X liters of water' is often close enough in practice but wrong in principle. In precision work — analytical chemistry, pharmaceutical preparation, primary standard solutions — the distinction is always maintained."
```

## Explainer

You already understand that the mole is chemistry's counting unit — one mole is 6.022 × 10²³ particles — and you know that solutions are homogeneous mixtures of solute dissolved in solvent. The concept of **concentration** bridges these ideas by answering a practical question: how much solute is actually present in a given volume of solution? Without a way to express this, you could not reliably carry out reactions in solution, because simply saying "some salt dissolved in water" tells you nothing about how many moles of reactant you are working with.

**Molarity** (abbreviated M) is defined as moles of solute divided by liters of solution: M = n/V. Notice that the denominator is liters of *solution*, not liters of solvent — this is a common source of error. If you dissolve 0.50 moles of NaCl in enough water to make 1.0 liter of total solution, the molarity is 0.50 M. The power of molarity is that it converts a volume measurement (which is easy to make with a graduated cylinder or volumetric flask) into a mole measurement (which is what stoichiometry requires). If you know a solution is 0.50 M and you measure out 0.200 L of it, you have exactly 0.50 × 0.200 = 0.10 moles of solute. This is the calculation that makes solution-based chemistry quantitative.

Molarity is not the only way to express concentration. **Molality** (m) uses moles of solute per kilogram of solvent — it does not change with temperature because mass is temperature-independent, making it preferred for colligative property calculations. **Mass percent** expresses grams of solute per 100 grams of solution, which is intuitive for everyday concentrations (like a 5% saline solution). **Parts per million (ppm)** is used for very dilute solutions, such as trace contaminants in drinking water, where molarity values would be inconveniently small numbers. Each unit has its context, but molarity dominates in the chemistry lab because it connects directly to the mole ratios you use in balanced equations.

To build fluency, practice converting between these units using the ratio skills you already have. A typical problem might give you mass of solute and volume of solution, asking for molarity — you would first convert grams to moles using molar mass, then divide by volume in liters. Or you might need to find what volume of a known molarity solution contains a required number of moles, rearranging to V = n/M. These conversions are the foundation for dilution calculations, titration problems, and virtually every quantitative technique in wet chemistry.
