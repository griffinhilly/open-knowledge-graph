---
id: ideal-real-gas-equations-state
title: Ideal and Real Gas Behavior
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: compressibility-factor-generalized
  type: hard
- id: ideal-gas-law
  type: soft
builds-toward:
- gas-mixture-thermodynamics-daltons
- combustion-stoichiometry-energy-release
tags:
- ideal-gas
- real-gas
- equations
- compressibility
stage: formal-systems
status: validated
---

# Ideal and Real Gas Behavior

## Core Idea
The ideal gas law Pv = RT assumes negligible intermolecular forces and molecular volume; it fails near saturation and at high pressures. Real gases use compressibility factor Z = Pv/RT and generalized correlations (law of corresponding states) or specific equations (virial, van der Waals). Engineering thermodynamics requires switching between ideal-gas approximations and real-gas corrections based on operating conditions.

## Questions

```yaml
- question: "A gas is stored at high pressure where its compressibility factor Z is measured to be 1.18. What does this tell you about the dominant real-gas effect at these conditions?"
  type: multiple-choice
  options:
    - "Intermolecular attractions dominate — the gas is easier to compress than the ideal law predicts"
    - "The gas is behaving ideally — Z is close enough to 1 to ignore corrections"
    - "Molecular volume exclusion dominates — the gas is harder to compress than the ideal law predicts"
    - "The gas is near its saturation curve and about to condense"
  answer: 2
  explanation: "Z = Pv/RT > 1 means the actual specific volume v is larger than the ideal prediction RT/P — the gas occupies more space than ideal. This happens when molecular volume exclusion (finite size of molecules) dominates: molecules physically cannot be compressed into a smaller volume than their own size. Intermolecular attractions would pull Z below 1 (gas easier to compress, v smaller than ideal). Z > 1 typically occurs at very high pressures or for gases with weak attractions (like hydrogen or helium)."

- question: "An engineer is sizing a storage vessel for ammonia refrigerant at 150 bar and near-ambient temperature, which is close to ammonia's saturation curve. She uses the ideal gas law. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "No significant error — ideal gas is always accurate for common engineering gases"
    - "The vessel will be oversized — real ammonia is harder to compress than the ideal law predicts"
    - "The vessel will be undersized — intermolecular attractions make real ammonia easier to compress than ideal, so Z < 1 and the actual specific volume is smaller than the ideal prediction"
    - "The result depends only on temperature, not pressure"
  answer: 2
  explanation: "Near saturation and at high pressure, ammonia (a polar molecule with strong intermolecular attractions) has Z significantly less than 1. This means the real specific volume is smaller than RT/P. If the engineer assumes ideal behavior, she calculates a specific volume larger than reality and therefore designs the vessel too small — it will not hold the required mass of refrigerant. This is a practical safety consequence: real-gas corrections are mandatory for ammonia, CO₂, and other refrigerants near their saturation curves."

- question: "Real gases always have a compressibility factor Z less than 1, because intermolecular attractions reduce pressure below the ideal gas prediction."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about real-gas behavior. Two competing effects determine Z: intermolecular attractions (pulling Z below 1) and molecular volume exclusion (pushing Z above 1). At moderate pressures, attractions often dominate first (Z < 1). At very high pressures, excluded volume wins (Z > 1). For gases with weak attractions like hydrogen or helium, Z > 1 even at moderate pressures. The compressibility chart shows both regions, and the actual Z depends on both reduced temperature and reduced pressure."

- question: "For a gas at reduced temperature Tr > 2 and reduced pressure Pr < 0.5, using the ideal gas law introduces less than about 1% error."
  type: true-false
  answer: true
  explanation: "This is the standard engineering rule of thumb for when ideal gas treatment is acceptable. At high reduced temperature (far above critical point) and low reduced pressure (far from condensation), molecules are dilute and fast-moving: intermolecular forces are negligible and molecular volume is tiny compared to total volume. The law of corresponding states tells us this condition generalizes across all gases — Tr > 2 and Pr < 0.5 reliably keeps Z within about 1% of 1.0 for most species."

- question: "Why do intermolecular attractions and molecular volume exclusion affect the compressibility factor Z in opposite directions, and which effect typically becomes dominant first as you raise pressure from a low value?"
  type: short-answer
  answer: "Intermolecular attractions pull molecules together, reducing the pressure the gas exerts on its container — effectively making the gas easier to compress than ideal (Z < 1). Molecular volume exclusion means molecules cannot occupy the same space, so the available volume is reduced — making the gas harder to compress than ideal (Z > 1). At low-to-moderate pressures, molecules are still far enough apart that attractions have more effect than the small correction for finite molecular size, so Z dips below 1 first. At very high pressures where molecules are tightly packed, volume exclusion dominates and Z rises above 1."
  explanation: "This directional competition is why compressibility charts show a minimum in Z versus pressure for most gases at moderate temperatures: Z drops below 1 at first (attractions win) then rises back above 1 (volume exclusion wins) as pressure increases. For the engineer, the practical takeaway is to always check the operating conditions against the Z chart rather than assuming corrections go in a fixed direction."
```

## Explainer

The ideal gas law Pv = RT is one of the most useful engineering approximations ever formulated — and like all approximations, its value comes from knowing exactly when it breaks down. You already know the ideal gas law from prerequisites, and you know the **compressibility factor** Z = Pv/RT, which equals 1 for an ideal gas and deviates from 1 when real-gas effects become significant. This topic is about building the intuition for those deviations and the equations engineers use to correct for them.

At the molecular level, the ideal gas model makes two simplifying assumptions: molecules have zero volume, and they exert no intermolecular forces on each other. Both assumptions are reasonable when molecules are far apart — that is, at low pressures and high temperatures where the gas is dilute. As pressure rises, molecules are squeezed together and their finite volume becomes significant: you cannot compress them below a certain minimum. As temperature falls near the saturation curve (or as pressure rises), intermolecular **van der Waals attractions** slow molecules down and pull them together, reducing the pressure below the ideal prediction. These two effects work in opposite directions: volume exclusion pushes Z above 1 (gas harder to compress than ideal); attractions pull Z below 1 (gas easier to compress than ideal). At moderate pressures, attractions often dominate first (Z < 1), while at very high pressures, volume exclusion wins (Z > 1).

The **van der Waals equation** (P + a/v²)(v − b) = RT captures both effects with two constants: *b* accounts for molecular volume (excluded volume correction), and *a/v²* is the pressure reduction due to intermolecular attractions. It is the simplest cubic equation of state and gives qualitative insight into liquid-vapor behavior — including why Z dips below 1 near saturation. More accurate engineering practice uses the **law of corresponding states**: when pressures and temperatures are expressed as reduced variables Pr = P/Pc and Tr = T/Tc (normalized by critical-point values), nearly all gases follow similar Z(Pr, Tr) surfaces. This is the basis for **generalized compressibility charts**, which let you estimate Z for any gas from its critical constants without knowing the specific molecular parameters.

When precision matters, engineers use **virial equations of state** — Z = 1 + B/v + C/v² + ... — which are rigorous power series expansions from statistical mechanics, with coefficients B, C, ... that depend on temperature and the gas species. The second virial coefficient B is the most important correction and is tabulated for common gases. At moderate densities, truncating after B is usually sufficient. For natural gas and petroleum applications, more sophisticated cubic equations (Peng-Robinson, Redlich-Kwong-Soave) are used, calibrated to match both phase equilibria and volumetric behavior across a wide range.

The practical engineering decision is knowing when to bother. As a rule of thumb, ideal-gas treatment is accurate to within 1% for Tr > 2 and Pr < 0.5. Near saturation, or for gases in high-pressure applications (hydrogen storage, supercritical CO₂ cycles, ammonia refrigeration), Z can deviate by 10–30% and real-gas corrections are mandatory. The compressibility factor is the universal diagnostic: check Z first, and if it differs meaningfully from 1.0 at your operating conditions, use the appropriate equation of state.
