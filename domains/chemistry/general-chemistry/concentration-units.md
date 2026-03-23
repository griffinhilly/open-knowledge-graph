---
id: concentration-units
title: Concentration Units
domain: chemistry
course: general-chemistry
prerequisites:
- id: solution-concentration
  type: hard
- id: mole-concept
  type: hard
builds-toward:
- colligative-properties
- vapor-pressure-raoults-law
tags:
- molarity
- molality
- mole-fraction
- mass-percent
- dilution
- parts-per-million
stage: formal-systems
status: validated
---
# Concentration Units

## Core Idea
Solution concentration can be expressed in several units, each suited to different applications. Molarity (M = mol solute / L solution) is the most common for aqueous reactions but is temperature-dependent because volume changes with temperature. Molality (m = mol solute / kg solvent) is temperature-independent and used in colligative property calculations. Mole fraction (χ = mol component / total mol) is unitless and essential for Raoult's law and gas mixtures. Mass percent (mass solute / mass solution × 100) and parts per million (ppm) are used in industrial and environmental contexts. The dilution equation M₁V₁ = M₂V₂ relates concentration and volume when adding solvent.

## How It's Best Learned
Practice converting between concentration units for the same solution — this requires knowing solution density to bridge mass-based and volume-based units. Work dilution problems by recognizing that moles of solute remain constant when only solvent is added.

## Common Misconceptions
- Molarity and molality are not interchangeable. Molarity uses liters of solution (solute + solvent), while molality uses kilograms of solvent only. For dilute aqueous solutions they are numerically similar, but they diverge for concentrated solutions or non-aqueous solvents.
- Adding solute to a fixed volume of solvent does not give the correct molarity — molarity requires the final volume of the solution, which changes when solute is added.

## Questions

```yaml
- question: "A chemist prepares 0.50 mol NaCl by two methods: Method A dissolves the salt in 1.00 L of water; Method B dissolves the salt and then adds water until the total solution volume reaches 1.00 L. Which method produces a 0.50 M solution?"
  type: multiple-choice
  options:
    - "Method A, because 0.50 mol divided by 1.00 L of water equals 0.50 M"
    - "Method B, because molarity requires liters of solution, not liters of solvent"
    - "Both methods produce 0.50 M because the same amount of solute is used"
    - "Neither method, because molarity also depends on the density of the solvent"
  answer: 1
  explanation: "Molarity is moles of solute per liter of *solution* (solute + solvent combined). Method A uses 1.00 L of water as the solvent, but the final solution volume will exceed 1.00 L once solute is added — giving a molarity slightly below 0.50 M. Method B correctly measures the final solution volume as 1.00 L, yielding exactly 0.50 M. This is the most common practical error when preparing solutions: confusing the volume of solvent with the final volume of solution."

- question: "A 1.0 m aqueous glucose solution is prepared at 25°C. The solution is then heated to 75°C, causing the solution to expand slightly in volume. Which of the following best describes what happens to the concentration?"
  type: multiple-choice
  options:
    - "Both molarity and molality decrease because the solution expands"
    - "Molarity decreases but molality remains unchanged"
    - "Molality decreases but molarity remains unchanged"
    - "Both molarity and molality remain unchanged because the amount of solute is constant"
  answer: 1
  explanation: "Molarity is moles per liter of solution, and liquid volume changes with temperature — so heating expands the solution, increasing its volume, and the molarity decreases. Molality is moles per kilogram of *solvent*, and mass is unaffected by temperature. The same grams of solvent remain, so molality is invariant. This is exactly why molality — not molarity — is used in colligative property calculations, which are often performed across temperature ranges."

- question: "Adding water to a solution decreases its molarity while the number of moles of solute remains constant."
  type: true-false
  answer: true
  explanation: "This is the principle behind the dilution equation M₁V₁ = M₂V₂. Moles of solute = M × V. When only solvent is added, the moles of solute do not change, but the total volume increases, so molarity (moles/volume) decreases. The equation works precisely because moles are conserved: M₁V₁ = moles = M₂V₂."

- question: "For any aqueous solution, molarity and molality always have the same numerical value because water has a density of 1 kg/L."
  type: true-false
  answer: false
  explanation: "Molarity and molality are only approximately equal for *dilute* aqueous solutions. Molarity uses total solution volume (solute + solvent); molality uses solvent mass only. For dilute solutions where the solute contributes little to the total volume or mass, the values are numerically close. But for concentrated solutions — like 18 M sulfuric acid — they diverge dramatically. And for non-aqueous solvents, the approximation breaks down even at low concentrations."

- question: "Why is molality preferred over molarity for calculating colligative properties such as boiling point elevation and freezing point depression?"
  type: short-answer
  answer: "Molality is preferred because it is temperature-independent. Colligative property calculations require a concentration unit that reflects the ratio of solute particles to solvent, and this ratio must not change as temperature changes. Molarity uses solution volume, which expands or contracts with temperature, so the same solution has different molarities at different temperatures. Molality uses solvent mass, which is invariant with temperature, ensuring the concentration value stays constant across the conditions of the calculation."
  explanation: "The physical laws underlying colligative properties (boiling point elevation = Kbm, etc.) are formulated in terms of molality for exactly this reason. Using molarity would require knowing the exact temperature at the time of measurement, and the calculated values would shift if the temperature changed. Molality neatly sidesteps this problem by anchoring concentration to a temperature-independent quantity."
```

## Explainer

You already know that a solution's concentration describes how much solute is dissolved in a given amount of solution or solvent, and you know the mole as the chemist's counting unit. Concentration units are the different ways of expressing that ratio, and each one exists because different chemical situations demand different denominators.

**Molarity (M)** — moles of solute per liter of solution — is the workhorse of aqueous chemistry because it directly tells you how many moles of reactant you are pipetting when you measure a volume. If you need 0.01 moles of HCl for a reaction, you simply take 10 mL of a 1.0 M solution. The limitation is that volume changes with temperature (liquids expand when heated), so molarity is technically temperature-dependent. For most bench chemistry at room temperature this doesn't matter, but for precise physical measurements it does.

**Molality (m)** — moles of solute per kilogram of solvent — solves the temperature problem by using mass instead of volume. Since mass doesn't change with temperature, molality is the unit of choice for colligative property calculations (boiling point elevation, freezing point depression, osmotic pressure) where you need a concentration that stays constant regardless of thermal conditions. Notice the critical difference in denominator: molarity uses total solution volume while molality uses solvent mass only. For dilute aqueous solutions the numerical values are close (because 1 L of dilute solution weighs approximately 1 kg and is mostly solvent), but they diverge significantly for concentrated solutions or non-water solvents.

**Mole fraction (χ)** expresses concentration as the ratio of moles of one component to the total moles of all components. It is unitless, always between 0 and 1, and it matters most in gas mixtures and vapor pressure calculations — Raoult's law, which you will encounter soon, is stated entirely in terms of mole fraction. **Mass percent** and **parts per million (ppm)** express concentration using mass ratios and are common in environmental and industrial chemistry where you might report pollutant levels as "5 ppm lead in drinking water." Converting between these units requires knowing the solution's density to bridge mass-based and volume-based measures.

The **dilution equation** M₁V₁ = M₂V₂ is not a separate law but a direct consequence of conservation of moles: when you add solvent to a solution, you change its volume and therefore its molarity, but the number of moles of solute stays the same. If you start with 50 mL of 2.0 M NaCl and dilute to 200 mL, the new concentration is (2.0 × 50)/200 = 0.50 M. This relationship only works for molarity (or any volume-based unit), and only when solvent is added — not when solute is added or removed. Mastering unit conversions among these systems is essential because real chemistry constantly shifts between them: you prepare solutions in molarity, calculate colligative properties in molality, and apply Raoult's law in mole fraction.
