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

## Explainer

From your study of thermodynamic systems, you're comfortable analyzing pure substances — a single-component fluid with well-defined properties. Real gases are almost always mixtures: air is nitrogen and oxygen (plus trace argon and CO₂), exhaust gas contains CO₂, H₂O, O₂, and N₂ in varying proportions, and natural gas is methane plus ethane plus impurities. To apply thermodynamics to these mixtures, you need a framework for connecting the mixture's macroscopic properties to the individual components' properties.

**Dalton's model of ideal gas mixtures** starts with the simplest possible assumption: each gas in the mixture behaves as if it were alone in the entire volume. The **partial pressure** of component i is the pressure it would exert if it alone occupied the container at the mixture temperature: P_i = y_i · P_total, where y_i = n_i/n_total is the **mole fraction** of component i. Dalton's law then states P_total = ΣP_i, which is automatically satisfied by this definition. Mole fractions are additive and sum to 1: Σy_i = 1. For dry air, y_N₂ ≈ 0.79 and y_O₂ ≈ 0.21, so at standard atmospheric pressure, P_N₂ ≈ 79.6 kPa and P_O₂ ≈ 21.2 kPa.

Mixture thermodynamic properties follow from the same logic. The enthalpy of an ideal gas mixture is H_mix = Σ(n_i · h_i), where each h_i is the molar enthalpy of component i at the mixture temperature (and its partial pressure, though for ideal gases enthalpy is pressure-independent). On a mass basis, h_mix = Σ(m_f_i · h_i), where m_f_i is the mass fraction. Entropy is slightly more complex: the entropy of a mixture is not simply the sum of component entropies at the mixture temperature — there is an **entropy of mixing** term that accounts for the irreversibility of mixing distinguishable gases. For ideal mixtures, Δs_mix = −R Σ(y_i ln y_i) per mole, which is always positive, reflecting the irreversibility of mixing.

The practical payoff is that you can analyze air as a mixture with known composition, use ideal gas property tables for N₂ and O₂ separately, and combine the results. When you compute combustion products from burning methane in air, the exhaust stream contains known mole fractions of CO₂, H₂O, O₂ (excess), and N₂ — all calculable from stoichiometry. Each component's contribution to total enthalpy and entropy is computed independently and summed. This separability is what makes mixture analysis tractable: instead of needing a new set of tables for every possible mixture, you reuse the pure-component tables you already have.
