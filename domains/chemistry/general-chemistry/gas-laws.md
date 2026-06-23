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
- id: kinetic-molecular-theory
  type: soft
- id: gas-behavior-intro
  type: soft
- id: properties-of-gases
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
stage: formal-systems
status: validated
---
# Gas Laws

## Core Idea
The behavior of ideal gases is described by relationships between pressure (P), volume (V), temperature (T), and amount (n). Boyle's law (P₁V₁ = P₂V₂ at constant T, n), Charles's law (V₁/T₁ = V₂/T₂ at constant P, n), and Avogadro's law (V ∝ n at constant P, T) combine into the ideal gas equation PV = nRT, where R is the universal gas constant. The combined gas law (P₁V₁/T₁ = P₂V₂/T₂) handles situations where n is constant but P, V, and T all change. At STP (0°C, 1 atm), one mole of an ideal gas occupies 22.4 L.

## How It's Best Learned
Derive the combined gas law by holding variables constant one at a time to recover each individual law. Practice converting temperature to Kelvin before any calculation. Use dimensional analysis to select the correct value of R for the units given in each problem.

## Common Misconceptions
- Temperature must always be in Kelvin for gas law calculations. Using Celsius produces incorrect results because the gas laws require an absolute temperature scale.
- The ideal gas law is an approximation — real gases deviate significantly at high pressures and low temperatures where intermolecular forces and molecular volume matter.

## Questions

```yaml
- question: "A gas occupies 3.0 L at 27°C. What volume does it occupy at 54°C at the same pressure and amount? (Assume ideal behavior.)"
  type: multiple-choice
  options:
    - "6.0 L — temperature doubled (54/27 = 2), so volume doubles"
    - "1.5 L — temperature increased, so pressure increases and volume decreases"
    - "3.27 L — using Kelvin: V₂ = 3.0 × (327 K / 300 K)"
    - "4.0 L — temperature increased by 27°C, which is one-ninth of 27°C, so volume increases by one-ninth"
  answer: 2
  explanation: "Charles's law requires absolute temperature: V₁/T₁ = V₂/T₂ in Kelvin. Convert: 27°C = 300 K, 54°C = 327 K. Then V₂ = 3.0 L × (327/300) = 3.27 L. The Celsius-trap answer (option A) multiplies by 54/27 = 2, doubling the volume — this is wrong because Celsius zero is not absolute zero. Temperature only doubled in Celsius (from 27 to 54); in Kelvin it increased by only about 9% (from 300 to 327). Using Celsius in gas law calculations produces wildly incorrect results."

- question: "Under which conditions do real gases deviate most significantly from ideal gas behavior?"
  type: multiple-choice
  options:
    - "High temperature and low pressure"
    - "Low temperature and high pressure"
    - "Any temperature at very low amounts of gas"
    - "Conditions where the gas has a low molar mass"
  answer: 1
  explanation: "The ideal gas law assumes (1) gas molecules have negligible volume and (2) there are no intermolecular forces. Both assumptions break down under extreme conditions. At high pressure, molecules are squeezed close together — their own volume becomes a significant fraction of the total volume. At low temperature, molecules move slowly enough that intermolecular attractive forces can pull them together, reducing pressure below the ideal prediction. Real gases behave most ideally when far apart and moving fast: low pressure and high temperature."

- question: "According to Charles's law, a gas sample at exactly 0°C would have zero volume."
  type: true-false
  answer: false
  explanation: "This is the classic Celsius error. Charles's law states V ∝ T only when T is in Kelvin. Zero volume corresponds to absolute zero, which is 0 K = −273.15°C. A gas at 0°C is actually at 273.15 K, and it still occupies a substantial volume. Using Celsius in gas law calculations as if 0°C = zero volume is precisely the error the Kelvin requirement prevents. Lord Kelvin defined the absolute temperature scale specifically so that gas laws work correctly: 0 K is where an ideal gas would have zero volume."

- question: "At the same temperature and pressure, equal volumes of different ideal gases contain the same number of molecules, regardless of the identity of the gas."
  type: true-false
  answer: true
  explanation: "This is Avogadro's law: V ∝ n at constant T and P, which means equal volumes at the same T and P contain equal n (moles), and therefore equal numbers of molecules. It doesn't matter whether the gas is H₂, O₂, CO₂, or Ar — the identity of the gas is irrelevant to this relationship for ideal gases. This principle underpins STP stoichiometry: 22.4 L/mol applies to any ideal gas at 0°C and 1 atm, which is a direct consequence of Avogadro's law combined with the ideal gas equation."

- question: "Why must temperature always be converted to Kelvin when using the gas laws, and what physically incorrect prediction would you get if you used Celsius instead?"
  type: short-answer
  answer: "The gas laws require an absolute temperature scale because they describe proportional relationships between gas properties and the average kinetic energy of molecules. Kelvin is absolute: 0 K means zero molecular motion (theoretically). Celsius is an arbitrary offset scale where 0°C is the freezing point of water — not zero molecular motion. Using Celsius, Charles's law (V ∝ T) would predict that a gas at 0°C has zero volume — physically impossible and obviously wrong. Converting 0°C to 273.15 K gives the correct nonzero volume. More generally, Celsius arithmetic gives the wrong ratio: doubling from 10°C to 20°C is only a 3.5% increase in Kelvin (283 K to 293 K), not a doubling of volume."
  explanation: "The Kelvin scale makes the mathematics work because it starts at the physically meaningful zero (no thermal energy). Any other scale's zero is arbitrary and breaks the proportionality. Temperature in gas laws is a proxy for kinetic energy, and kinetic energy only goes to zero at absolute zero — not at 0°C."
```

## Explainer

From the mole concept, you know how to count particles using Avogadro's number, and from kinetic molecular theory, you know that gas particles move randomly, collide elastically, and exert pressure through collisions with container walls. The gas laws translate that molecular picture into quantitative relationships you can calculate with. Each law isolates the relationship between two variables by holding everything else constant, and they all combine into one master equation.

**Boyle's law** says that at constant temperature and amount of gas, pressure and volume are inversely proportional: P₁V₁ = P₂V₂. The intuition is straightforward — squeeze a gas into half the volume and the particles hit the walls twice as often, doubling the pressure. You can feel this when you push a syringe plunger with the tip sealed. **Charles's law** says that at constant pressure and amount, volume is directly proportional to absolute temperature: V₁/T₁ = V₂/T₂. Heat a gas and the particles move faster, pushing the container walls outward — this is why a balloon expands in a warm room and shrinks in a freezer. **Avogadro's law** says that at constant temperature and pressure, volume is proportional to the number of moles: more particles need more space. This is why equal volumes of gases at the same temperature and pressure contain equal numbers of molecules, regardless of the gas's identity.

All three laws merge into the **ideal gas law**: **PV = nRT**. The constant R (8.314 J/(mol·K), or 0.08206 L·atm/(mol·K)) bridges the units. This single equation handles any ideal gas problem: if you know three of the four variables (P, V, n, T), you can solve for the fourth. When n is constant but all three other variables change, you use the **combined gas law**: P₁V₁/T₁ = P₂V₂/T₂. A critical procedural point: temperature must always be in Kelvin. Charles's law breaks mathematically with Celsius because 0°C is not zero molecular motion — that's 0 K (−273.15°C). Using Celsius would predict that gas volume drops to zero at 0°C, which is obviously wrong.

At **STP** (standard temperature and pressure: 0°C and 1 atm), one mole of any ideal gas occupies 22.4 L — a useful conversion factor for stoichiometry involving gases. But remember that the ideal gas law is an idealization. It assumes gas particles have no volume and no attractive forces between them. Real gases follow PV = nRT well at moderate temperatures and low pressures, where particles are far apart and moving fast. At high pressures (particles squeezed close together, their own volume matters) or low temperatures (particles moving slowly enough for intermolecular attractions to matter), deviations become significant — which is why there are corrections like the van der Waals equation that you will encounter later.
