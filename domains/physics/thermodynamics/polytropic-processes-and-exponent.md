---
id: polytropic-processes-and-exponent
title: Polytropic Processes and the Polytropic Index
domain: physics
course: thermodynamics
prerequisites:
- id: adiabatic-processes
  type: hard
- id: isothermal-processes
  type: soft
tags:
- polytropic
- process-index
- pv-relation
stage: formal-systems
status: draft
---

# Polytropic Processes and the Polytropic Index

## Core Idea
A polytropic process follows PV^n = constant, where n is the polytropic index. Special cases: n = 0 (isobaric), n = 1 (isothermal), n = γ (isentropic/adiabatic), n = ∞ (isochoric). Real compressors and turbines often behave polytropically with n between 1 and γ, representing intermediate behavior between isothermal and adiabatic.

## Explainer

From adiabatic processes, you know that a reversible adiabatic expansion of an ideal gas follows PV^γ = constant, where γ = C_p/C_v is the ratio of heat capacities. From isothermal processes, you know that at constant temperature PV = nRT gives PV = constant (since T is fixed), which can be written as PV^1 = constant. These two special cases are not isolated facts — they are members of a unified family described by the **polytropic relation** PV^n = constant, where the index n controls how much heat exchange occurs during the process.

Think of n as a dial between the two extremes you already know. At n = γ (typically ~1.4 for diatomic gases), no heat is exchanged — you recover the adiabatic process. At n = 1, the process is isothermal. For n between 1 and γ, the gas exchanges some heat with the surroundings: it is neither fully insulated nor in perfect thermal equilibrium. This is precisely the regime of real engineering devices. A compressor operating too fast for complete heat exchange but not perfectly insulated might behave polytropically with n ≈ 1.2 to 1.35. The polytropic model lets you fit one parameter n to data and use it to predict work, heat, and temperature changes without needing to solve a detailed heat transfer problem.

The special case n = 0 corresponds to an isobaric (constant pressure) process: PV^0 = P · 1 = constant means P is constant. The case n = ∞ is less obvious. Writing the relation as P^(1/n) · V = constant and taking n → ∞ sends 1/n → 0, so P^0 · V = V = constant — an isochoric (constant volume) process. All four fundamental process types (isobaric, isothermal, adiabatic, isochoric) live within this single framework as limiting or special values of n.

Work done in a polytropic process is W = (P₁V₁ − P₂V₂)/(n − 1) for n ≠ 1, which you can derive by integrating P = C/V^n. For n = 1 (isothermal), you use W = nRT ln(V₂/V₁) as you already know. The temperature and pressure relationship follows from combining PV^n = constant with the ideal gas law PV = nRT: T₂/T₁ = (V₁/V₂)^(n−1) = (P₂/P₁)^((n−1)/n). These relations parallel the adiabatic formulas you know, with γ replaced by n throughout — which is why the polytropic framework is so convenient for engineering calculations.
