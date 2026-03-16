---
id: reversible-isothermal-expansion
title: Reversible Isothermal Expansion
domain: physics
course: thermodynamics
prerequisites:
- id: isothermal-processes
  type: hard
- id: boundary-work-pv-diagram
  type: hard
tags:
- reversible-processes
- isothermal
- work-heat
stage: formal-systems
status: draft
---

# Reversible Isothermal Expansion

## Core Idea
In a reversible isothermal expansion of an ideal gas, temperature (and internal energy) remain constant, so Q = W = nRT ln(V_f/V_i) = nRT ln(P_i/P_f). The gas does maximum work for a given pressure drop. This process is reversible because the system remains infinitesimally close to equilibrium.

## Explainer

You already know that the boundary work done by a gas expanding against a piston is W = ∫P dV, and that an isothermal process holds temperature constant. For an ideal gas, the internal energy depends only on temperature: U = nC_vT. If T is constant, then ΔU = 0, and the first law immediately gives Q = W — all the heat absorbed from the surroundings is converted to work. This is not a perpetual motion trick: the temperature stays constant only because the system continuously draws heat from an external reservoir at temperature T.

The work integral uses the ideal gas law to substitute P = nRT/V at each point along the path: W = ∫_{V_i}^{V_f} (nRT/V) dV = nRT ln(V_f/V_i). Since the gas expands (V_f > V_i), the logarithm is positive and W > 0 — the gas does positive work and absorbs heat. The equivalent form W = nRT ln(P_i/P_f) follows from PV = const at fixed T: if volume doubles, pressure halves, and ln(V_f/V_i) = ln(P_i/P_f). A doubling of volume at 300 K for one mole gives W = (1)(8.314)(300)ln(2) ≈ 1729 J — entirely absorbed from the heat reservoir.

The word **reversible** means something precise here: the expansion is performed infinitely slowly, with the external pressure kept just infinitesimally below the gas pressure at every moment. This ensures the system passes through a continuous sequence of equilibrium states. Any faster expansion — where the external pressure jumps below the gas pressure and the gas expands into an unresisted space — is irreversible: it produces less work (in the limit of free expansion into a vacuum, zero work) for the same initial and final states. The reversible isothermal path gives the **maximum possible work** for an isothermal expansion between V_i and V_f, because it extracts work against the largest possible opposing force at every step.

This process appears in two critical places you will encounter soon. First, it is one of the four strokes of the **Carnot cycle** — the two isothermal steps (one at T_H, one at T_C) are where the engine exchanges heat with its reservoirs, and the reversibility of those strokes is what makes the Carnot engine achieve the maximum possible efficiency. Second, the entropy change ΔS = Q/T = nR ln(V_f/V_i) calculated here generalizes: for any process, reversible or not, ΔS between two equilibrium states is the same, so the reversible isothermal expression gives you a direct way to compute entropy changes for ideal gas expansions.
