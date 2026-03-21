---
id: gas-mixtures-partial-pressures-daltons-law
title: Gas Mixtures and Dalton's Law of Partial Pressures
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: thermodynamic-systems-engineering
  type: hard
tags:
- gas-mixtures
- daltons-law
- partial-pressures
stage: advanced
status: draft
---

# Gas Mixtures and Dalton's Law of Partial Pressures

## Core Idea
Dalton's law states total pressure of a non-reacting gas mixture equals the sum of partial pressures (pressure each gas would exert alone). Component properties (enthalpy, entropy) are calculated separately and summed by mass fraction; mixing is ideal when component interactions are negligible. This framework enables analysis of air as a mixture (79% N₂, 21% O₂) and combustion products as mixtures of CO₂, H₂O, O₂, N₂.

## Questions

```yaml
- question: "A sealed container holds 0.6 mol of N₂ and 0.4 mol of O₂ at a total pressure of 200 kPa. What is the partial pressure of O₂?"
  type: multiple-choice
  options:
    - "40 kPa, because O₂ is the minority component and contributes less pressure"
    - "80 kPa, because the mole fraction of O₂ is 0.4 and partial pressure = mole fraction × total pressure"
    - "100 kPa, because each gas component occupies half the container volume"
    - "200 kPa, because ideal gases exert the same pressure regardless of composition"
  answer: 1
  explanation: "Partial pressure = mole fraction × total pressure. O₂ has 0.4 mol out of 1.0 mol total, so y_O₂ = 0.4. P_O₂ = 0.4 × 200 kPa = 80 kPa. Option C incorrectly applies an equal-volume split (which is not how partial pressures work); option D confuses ideal gas pressure independence from other gases with the total-pressure calculation. Each component contributes pressure proportional to its mole fraction."

- question: "An engineer calculates the enthalpy of an ideal gas combustion exhaust containing CO₂, H₂O, N₂, and O₂ at known mole fractions. What is the correct approach?"
  type: multiple-choice
  options:
    - "Look up enthalpy in a combustion-gas table for the specific mixture composition"
    - "Use the enthalpy of air as an approximation, since exhaust is mostly nitrogen"
    - "Calculate h_i for each component separately using its pure-component property table at the mixture temperature, then sum each by its mass fraction: h_mix = Σ(mf_i × h_i)"
    - "Average the component enthalpies equally since they are all at the same temperature"
  answer: 2
  explanation: "For ideal gas mixtures, mixture enthalpy is calculated as the mass-fraction-weighted sum of pure-component enthalpies at the mixture temperature. Because ideal gas enthalpy is pressure-independent, you only need the temperature and the pure-component tables for each species — no special mixture tables required. This separability is the practical power of the ideal mixture assumption. Option D (equal averaging) ignores the different mass fractions and molecular weights of each component."

- question: "When two different ideal gases are mixed at constant temperature and volume, the total pressure equals the sum of the individual pressures each gas would exert if it alone occupied the entire container."
  type: true-false
  answer: true
  explanation: "This is an exact statement of Dalton's law of partial pressures for ideal gas mixtures. Because ideal gas molecules are assumed to have no intermolecular interactions, each component behaves as if the others are absent — it exerts its own partial pressure based solely on its mole fraction and the total conditions. The total pressure is the sum of all partial pressures."

- question: "Mixing two ideal gases at the same temperature and pressure produces no change in entropy because no energy is exchanged and the total volume is unchanged."
  type: true-false
  answer: false
  explanation: "Mixing distinct ideal gases is an irreversible process that increases entropy even with no energy transfer and no volume change. The entropy of mixing is Δs_mix = −R Σ(y_i ln y_i) per mole, which is always positive (since ln y_i < 0 for all mole fractions between 0 and 1). This reflects the increased disorder from dispersing distinguishable gas molecules throughout the container — they can no longer be separated without doing work. Entropy increases whenever distinguishable substances mix spontaneously."

- question: "Explain why the ideal gas mixture assumption allows engineers to use pure-component property tables (like JANAF tables) for mixture calculations, rather than requiring new tables for every possible mixture composition."
  type: short-answer
  answer: "Under the ideal mixture assumption, each gas component behaves as if it were alone in the entire container — its partial pressure, enthalpy, and entropy (at its partial pressure) are determined by its own properties at the mixture temperature, independent of the other components. This means mixture properties are simply weighted sums of pure-component properties: h_mix = Σ(mf_i × h_i) and similarly for entropy (with the addition of the mixing term). Engineers need only the pure-component tables for each species plus the mole fractions — they can compute any mixture property without a new table."
  explanation: "The separability of mixture properties is the key engineering utility of Dalton's model. It transforms complex multi-component analysis into a set of independent single-component calculations combined by superposition. The assumption is valid when intermolecular interactions between different species are negligible — generally a good approximation for gases at moderate conditions."
```

## Explainer

From your study of thermodynamic systems, you're comfortable analyzing pure substances — a single-component fluid with well-defined properties. Real gases are almost always mixtures: air is nitrogen and oxygen (plus trace argon and CO₂), exhaust gas contains CO₂, H₂O, O₂, and N₂ in varying proportions, and natural gas is methane plus ethane plus impurities. To apply thermodynamics to these mixtures, you need a framework for connecting the mixture's macroscopic properties to the individual components' properties.

**Dalton's model of ideal gas mixtures** starts with the simplest possible assumption: each gas in the mixture behaves as if it were alone in the entire volume. The **partial pressure** of component i is the pressure it would exert if it alone occupied the container at the mixture temperature: P_i = y_i · P_total, where y_i = n_i/n_total is the **mole fraction** of component i. Dalton's law then states P_total = ΣP_i, which is automatically satisfied by this definition. Mole fractions are additive and sum to 1: Σy_i = 1. For dry air, y_N₂ ≈ 0.79 and y_O₂ ≈ 0.21, so at standard atmospheric pressure, P_N₂ ≈ 79.6 kPa and P_O₂ ≈ 21.2 kPa.

Mixture thermodynamic properties follow from the same logic. The enthalpy of an ideal gas mixture is H_mix = Σ(n_i · h_i), where each h_i is the molar enthalpy of component i at the mixture temperature (and its partial pressure, though for ideal gases enthalpy is pressure-independent). On a mass basis, h_mix = Σ(m_f_i · h_i), where m_f_i is the mass fraction. Entropy is slightly more complex: the entropy of a mixture is not simply the sum of component entropies at the mixture temperature — there is an **entropy of mixing** term that accounts for the irreversibility of mixing distinguishable gases. For ideal mixtures, Δs_mix = −R Σ(y_i ln y_i) per mole, which is always positive, reflecting the irreversibility of mixing.

The practical payoff is that you can analyze air as a mixture with known composition, use ideal gas property tables for N₂ and O₂ separately, and combine the results. When you compute combustion products from burning methane in air, the exhaust stream contains known mole fractions of CO₂, H₂O, O₂ (excess), and N₂ — all calculable from stoichiometry. Each component's contribution to total enthalpy and entropy is computed independently and summed. This separability is what makes mixture analysis tractable: instead of needing a new set of tables for every possible mixture, you reuse the pure-component tables you already have.
