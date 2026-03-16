---
id: gas-laws
title: Gas Laws
domain: chemistry
course: general-chemistry
prerequisites:
- id: mole-concept
  type: hard
- id: stoichiometry-calculations
  type: soft
- id: kinetic-molecular-theory-basics
  type: soft
builds-toward:
- gas-stoichiometry
- real-gases-van-der-waals
tags:
- Boyles-law
- Charless-law
- Avogadros-law
- ideal-gas-law
- PV-equals-nRT
- combined-gas-law
stage: abstract-reasoning
status: draft
---
# Gas Laws

## Core Idea
The behavior of ideal gases is described by relationships between pressure (P), volume (V), temperature (T), and amount (n). Boyle's law (P₁V₁ = P₂V₂ at constant T, n), Charles's law (V₁/T₁ = V₂/T₂ at constant P, n), and Avogadro's law (V ∝ n at constant P, T) combine into the ideal gas equation PV = nRT, where R is the universal gas constant. The combined gas law (P₁V₁/T₁ = P₂V₂/T₂) handles situations where n is constant but P, V, and T all change. At STP (0°C, 1 atm), one mole of an ideal gas occupies 22.4 L.

## How It's Best Learned
Derive the combined gas law by holding variables constant one at a time to recover each individual law. Practice converting temperature to Kelvin before any calculation. Use dimensional analysis to select the correct value of R for the units given in each problem.

## Common Misconceptions
- Temperature must always be in Kelvin for gas law calculations. Using Celsius produces incorrect results because the gas laws require an absolute temperature scale.
- The ideal gas law is an approximation — real gases deviate significantly at high pressures and low temperatures where intermolecular forces and molecular volume matter.

## Explainer

From the mole concept, you know how to count particles using Avogadro's number, and from kinetic molecular theory, you know that gas particles move randomly, collide elastically, and exert pressure through collisions with container walls. The gas laws translate that molecular picture into quantitative relationships you can calculate with. Each law isolates the relationship between two variables by holding everything else constant, and they all combine into one master equation.

**Boyle's law** says that at constant temperature and amount of gas, pressure and volume are inversely proportional: P₁V₁ = P₂V₂. The intuition is straightforward — squeeze a gas into half the volume and the particles hit the walls twice as often, doubling the pressure. You can feel this when you push a syringe plunger with the tip sealed. **Charles's law** says that at constant pressure and amount, volume is directly proportional to absolute temperature: V₁/T₁ = V₂/T₂. Heat a gas and the particles move faster, pushing the container walls outward — this is why a balloon expands in a warm room and shrinks in a freezer. **Avogadro's law** says that at constant temperature and pressure, volume is proportional to the number of moles: more particles need more space. This is why equal volumes of gases at the same temperature and pressure contain equal numbers of molecules, regardless of the gas's identity.

All three laws merge into the **ideal gas law**: **PV = nRT**. The constant R (8.314 J/(mol·K), or 0.08206 L·atm/(mol·K)) bridges the units. This single equation handles any ideal gas problem: if you know three of the four variables (P, V, n, T), you can solve for the fourth. When n is constant but all three other variables change, you use the **combined gas law**: P₁V₁/T₁ = P₂V₂/T₂. A critical procedural point: temperature must always be in Kelvin. Charles's law breaks mathematically with Celsius because 0°C is not zero molecular motion — that's 0 K (−273.15°C). Using Celsius would predict that gas volume drops to zero at 0°C, which is obviously wrong.

At **STP** (standard temperature and pressure: 0°C and 1 atm), one mole of any ideal gas occupies 22.4 L — a useful conversion factor for stoichiometry involving gases. But remember that the ideal gas law is an idealization. It assumes gas particles have no volume and no attractive forces between them. Real gases follow PV = nRT well at moderate temperatures and low pressures, where particles are far apart and moving fast. At high pressures (particles squeezed close together, their own volume matters) or low temperatures (particles moving slowly enough for intermolecular attractions to matter), deviations become significant — which is why there are corrections like the van der Waals equation that you will encounter later.
