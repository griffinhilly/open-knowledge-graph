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
stage: advanced
status: draft
---
# Concentration Units

## Core Idea
Solution concentration can be expressed in several units, each suited to different applications. Molarity (M = mol solute / L solution) is the most common for aqueous reactions but is temperature-dependent because volume changes with temperature. Molality (m = mol solute / kg solvent) is temperature-independent and used in colligative property calculations. Mole fraction (χ = mol component / total mol) is unitless and essential for Raoult's law and gas mixtures. Mass percent (mass solute / mass solution × 100) and parts per million (ppm) are used in industrial and environmental contexts. The dilution equation M₁V₁ = M₂V₂ relates concentration and volume when adding solvent.

## How It's Best Learned
Practice converting between concentration units for the same solution — this requires knowing solution density to bridge mass-based and volume-based units. Work dilution problems by recognizing that moles of solute remain constant when only solvent is added.

## Common Misconceptions
- Molarity and molality are not interchangeable. Molarity uses liters of solution (solute + solvent), while molality uses kilograms of solvent only. For dilute aqueous solutions they are numerically similar, but they diverge for concentrated solutions or non-aqueous solvents.
- Adding solute to a fixed volume of solvent does not give the correct molarity — molarity requires the final volume of the solution, which changes when solute is added.

## Explainer

You already know that a solution's concentration describes how much solute is dissolved in a given amount of solution or solvent, and you know the mole as the chemist's counting unit. Concentration units are the different ways of expressing that ratio, and each one exists because different chemical situations demand different denominators.

**Molarity (M)** — moles of solute per liter of solution — is the workhorse of aqueous chemistry because it directly tells you how many moles of reactant you are pipetting when you measure a volume. If you need 0.01 moles of HCl for a reaction, you simply take 10 mL of a 1.0 M solution. The limitation is that volume changes with temperature (liquids expand when heated), so molarity is technically temperature-dependent. For most bench chemistry at room temperature this doesn't matter, but for precise physical measurements it does.

**Molality (m)** — moles of solute per kilogram of solvent — solves the temperature problem by using mass instead of volume. Since mass doesn't change with temperature, molality is the unit of choice for colligative property calculations (boiling point elevation, freezing point depression, osmotic pressure) where you need a concentration that stays constant regardless of thermal conditions. Notice the critical difference in denominator: molarity uses total solution volume while molality uses solvent mass only. For dilute aqueous solutions the numerical values are close (because 1 L of dilute solution weighs approximately 1 kg and is mostly solvent), but they diverge significantly for concentrated solutions or non-water solvents.

**Mole fraction (χ)** expresses concentration as the ratio of moles of one component to the total moles of all components. It is unitless, always between 0 and 1, and it matters most in gas mixtures and vapor pressure calculations — Raoult's law, which you will encounter soon, is stated entirely in terms of mole fraction. **Mass percent** and **parts per million (ppm)** express concentration using mass ratios and are common in environmental and industrial chemistry where you might report pollutant levels as "5 ppm lead in drinking water." Converting between these units requires knowing the solution's density to bridge mass-based and volume-based measures.

The **dilution equation** M₁V₁ = M₂V₂ is not a separate law but a direct consequence of conservation of moles: when you add solvent to a solution, you change its volume and therefore its molarity, but the number of moles of solute stays the same. If you start with 50 mL of 2.0 M NaCl and dilute to 200 mL, the new concentration is (2.0 × 50)/200 = 0.50 M. This relationship only works for molarity (or any volume-based unit), and only when solvent is added — not when solute is added or removed. Mastering unit conversions among these systems is essential because real chemistry constantly shifts between them: you prepare solutions in molarity, calculate colligative properties in molality, and apply Raoult's law in mole fraction.
