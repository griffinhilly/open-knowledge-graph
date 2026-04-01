---
id: geochemical-thermodynamics
title: Geochemical Thermodynamics
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: chemical-potential-thermodynamics
  type: hard
- id: chemical-equilibrium
  type: hard
builds-toward:
- mineral-stability-phase-diagrams
- aqueous-geochemistry
- redox-geochemistry
tags:
- thermodynamics
- Gibbs-free-energy
- equilibrium
- geochemistry
stage: expert
status: validated
---

# Geochemical Thermodynamics

## Core Idea
Geochemical thermodynamics applies the principles of chemical thermodynamics -- Gibbs free energy, enthalpy, entropy, and chemical potential -- to predict the stability of minerals, the direction of geochemical reactions, and the composition of natural systems at equilibrium. The central quantity is the Gibbs free energy of reaction (delta-G), which determines whether a reaction proceeds spontaneously at given temperature and pressure. At equilibrium, delta-G = 0, and the equilibrium constant K relates to standard-state free energy by delta-G-naught = -RT ln K. Because geological systems operate over enormous temperature (0-1400 C) and pressure (1 atm to 30+ GPa) ranges, geochemical thermodynamics must account for T-P dependence of thermodynamic properties -- a complexity rarely encountered in benchtop chemistry.

## Questions

```yaml
- question: "The dissolution of calcite in rainwater (CaCO3 + CO2 + H2O -> Ca2+ + 2HCO3-) has a negative delta-G at Earth's surface conditions. What does this predict about limestone weathering?"
  type: multiple-choice
  options:
    - "Calcite precipitation is favored at Earth's surface"
    - "The reaction is thermodynamically favorable and will proceed spontaneously, dissolving calcite -- consistent with the observed formation of karst landscapes, caves, and limestone dissolution in acidic groundwater"
    - "The reaction will not occur because calcite is a stable mineral"
    - "Kinetics prevent any dissolution regardless of thermodynamics"
  answer: 1
  explanation: "A negative delta-G means the reaction is thermodynamically favorable in the forward direction. This correctly predicts that calcite dissolves in CO2-bearing water, forming karst landscapes, cave systems, and contributing calcium and bicarbonate to rivers and groundwater. However, thermodynamics only predicts the direction and equilibrium state -- kinetics determines the rate, which is fast for calcite dissolution."

- question: "A mineral assemblage that is stable at high temperature and pressure will remain stable when brought to Earth's surface conditions because minerals do not change once formed."
  type: true-false
  answer: false
  explanation: "Thermodynamic stability depends on the ambient T-P conditions. Minerals stable at depth (high-T, high-P) are often metastable or unstable at surface conditions. Olivine weathers rapidly at the surface; high-pressure polymorphs (coesite, diamond) are metastable at 1 atm. The reason some high-T/P minerals persist at the surface is kinetics -- reaction rates are too slow at low temperature for thermodynamic equilibrium to be achieved in geologic time. Thermodynamics predicts what should happen; kinetics determines whether it actually does."

- question: "Explain why the equilibrium constant for a geochemical reaction changes with temperature, and what this implies for mineral stability across Earth's temperature gradient."
  type: short-answer
  answer: "The van't Hoff equation relates K to temperature: d(ln K)/dT = delta-H/(RT^2). For endothermic reactions (positive delta-H), K increases with temperature, shifting equilibrium toward products. For exothermic reactions, K decreases with temperature. This means mineral stability fields shift systematically with depth -- minerals stable at surface temperatures may dissolve or transform at depth, and vice versa. This T-dependence drives metamorphic mineral reactions, hydrothermal alteration, and the zonation of mineral assemblages in plutonic systems."
  explanation: "The coupling of K with T through enthalpy is why geologists can use mineral assemblages as geothermometers -- the specific minerals present record the temperature at which the system last equilibrated."
```

## Explainer

Geochemical thermodynamics takes the abstract framework of chemical thermodynamics and applies it to the messy, heterogeneous, extreme-condition systems of the Earth. The core question is always the same: given the temperature, pressure, and composition of a system, what minerals, fluids, and gases should be present at equilibrium?

The Gibbs free energy is the master variable. For any reaction, delta-G = delta-G-naught + RT ln Q, where Q is the reaction quotient. If delta-G is negative, the reaction proceeds forward; if positive, it proceeds in reverse; at equilibrium, delta-G = 0 and Q = K. Standard-state thermodynamic data (delta-G-naught-f, delta-H-naught-f, S-naught, and heat capacity Cp) for minerals, aqueous species, and gases are tabulated in databases (Holland and Powell, SUPCRT, JANAF) and form the foundation for all equilibrium calculations.

The geological challenge is that standard-state data are typically for 25 C and 1 bar, while geological processes occur at temperatures up to 1400 C and pressures up to 30 GPa. Extrapolating thermodynamic properties requires heat capacity data (for temperature dependence), molar volume and compressibility data (for pressure dependence), and equations of state for fluids and melts. For aqueous species at hydrothermal conditions, the HKF (Helgeson-Kirkham-Flowers) model provides a framework for calculating properties up to 1000 C and 5 kbar.

A key conceptual distinction is between equilibrium and metastability. Thermodynamics predicts what should exist at equilibrium, but many geological materials persist far from equilibrium because reaction kinetics are too slow. Diamond is thermodynamically unstable at Earth's surface (graphite is the stable carbon polymorph at 1 atm), yet diamonds persist for billions of years because the activation energy for the transformation is prohibitively high at surface temperatures. This tension between thermodynamic prediction and kinetic reality pervades geochemistry.
