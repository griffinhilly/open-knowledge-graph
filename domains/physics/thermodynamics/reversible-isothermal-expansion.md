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
status: validated
---

# Reversible Isothermal Expansion

## Core Idea
In a reversible isothermal expansion of an ideal gas, temperature (and internal energy) remain constant, so Q = W = nRT ln(V_f/V_i) = nRT ln(P_i/P_f). The gas does maximum work for a given pressure drop. This process is reversible because the system remains infinitesimally close to equilibrium.

## Questions

```yaml
- question: "An ideal gas undergoes isothermal expansion, absorbing 500 J of heat from a reservoir. How much work does the gas do on its surroundings?"
  type: multiple-choice
  options:
    - "Less than 500 J — some heat goes into increasing internal energy"
    - "Exactly 500 J — all absorbed heat is converted to work"
    - "More than 500 J — the gas uses stored internal energy plus the absorbed heat"
    - "Zero — isothermal processes do no work because temperature doesn't change"
  answer: 1
  explanation: "For an ideal gas, internal energy depends only on temperature: U = nC_vT. If T is constant (isothermal), then ΔU = 0. By the first law: ΔU = Q − W, so 0 = Q − W, meaning W = Q = 500 J. All absorbed heat is converted to mechanical work. This is not a violation of thermodynamics — the temperature stays constant only because the gas continuously draws heat from the reservoir. The common mistake is thinking heat must 'go somewhere' besides work; for an ideal gas at constant T, the only destination is work."

- question: "A gas expands isothermally from V_i to V_f. The same expansion is performed two ways: reversibly (infinitely slowly) and irreversibly (rapidly against lower external pressure). Which produces more work?"
  type: multiple-choice
  options:
    - "Both produce the same work — the initial and final states are identical"
    - "The irreversible process — faster expansion generates more kinetic energy"
    - "The reversible process — it maintains the maximum possible opposing force at every step"
    - "Neither — isothermal processes always produce W = nRT ln(V_f/V_i) regardless of path"
  answer: 2
  explanation: "The reversible isothermal expansion maximizes work because it keeps the external pressure just infinitesimally below the gas pressure at every moment, extracting the maximum possible work against the largest possible opposing force throughout. An irreversible expansion uses a lower external pressure (or free expansion into vacuum with zero opposing force), so less work is extracted. The work done depends on the path, not just the endpoints. Option A and D are wrong for this reason — W = nRT ln(V_f/V_i) is the formula for the reversible path specifically."

- question: "For an ideal gas undergoing reversible isothermal expansion, the internal energy increases because heat is flowing into the gas."
  type: true-false
  answer: false
  explanation: "For an ideal gas, internal energy depends only on temperature. If the process is isothermal (constant T), then ΔU = 0 — internal energy does not change, regardless of how much heat flows in. The absorbed heat Q is entirely converted to work W (by Q = W from the first law with ΔU = 0). This surprises students who expect that adding heat must raise energy, but that is only true if temperature rises. Here the gas absorbs heat and immediately does an equal amount of work, keeping T (and U) constant."

- question: "A reversible isothermal expansion produces the maximum possible work for any expansion between the same two equilibrium states."
  type: true-false
  answer: true
  explanation: "The reversible path is the theoretical maximum work output for an expansion. Any irreversibility (finite pressure differences, friction, unresisted expansion) reduces the work extracted below nRT ln(V_f/V_i). In the extreme of free expansion into vacuum, W = 0 for the same change in volume. The reversible path achieves the maximum by maintaining the system at every instant in equilibrium with the largest possible opposing force, extracting work at every step rather than letting any pressure differential go to waste as thermal dissipation."

- question: "What makes an isothermal expansion 'reversible,' and why does this condition result in maximum work output?"
  type: short-answer
  answer: "A reversible expansion is performed infinitely slowly, with the external pressure kept just infinitesimally below the gas pressure at every moment. This keeps the system in a continuous series of equilibrium states. Because the external pressure is always nearly equal to the gas pressure, the gas does work against the maximum possible opposing force at every step, extracting the most work possible. Any faster expansion sets the external pressure lower than the gas pressure, wasting the pressure difference as unrecovered energy rather than useful work."
  explanation: "The concept of reversibility is key to thermodynamic efficiency. A reversible process is one that can be run in reverse along the same path — infinitesimal perturbations can reverse direction. This requires quasi-static conditions (infinitely slow). The Carnot cycle's efficiency derivation depends on both isothermal steps being reversible; if they were irreversible, the engine could not achieve the theoretical maximum efficiency η = 1 − T_C/T_H."
```

## Explainer

You already know that the boundary work done by a gas expanding against a piston is W = ∫P dV, and that an isothermal process holds temperature constant. For an ideal gas, the internal energy depends only on temperature: U = nC_vT. If T is constant, then ΔU = 0, and the first law immediately gives Q = W — all the heat absorbed from the surroundings is converted to work. This is not a perpetual motion trick: the temperature stays constant only because the system continuously draws heat from an external reservoir at temperature T.

The work integral uses the ideal gas law to substitute P = nRT/V at each point along the path: W = ∫_{V_i}^{V_f} (nRT/V) dV = nRT ln(V_f/V_i). Since the gas expands (V_f > V_i), the logarithm is positive and W > 0 — the gas does positive work and absorbs heat. The equivalent form W = nRT ln(P_i/P_f) follows from PV = const at fixed T: if volume doubles, pressure halves, and ln(V_f/V_i) = ln(P_i/P_f). A doubling of volume at 300 K for one mole gives W = (1)(8.314)(300)ln(2) ≈ 1729 J — entirely absorbed from the heat reservoir.

The word **reversible** means something precise here: the expansion is performed infinitely slowly, with the external pressure kept just infinitesimally below the gas pressure at every moment. This ensures the system passes through a continuous sequence of equilibrium states. Any faster expansion — where the external pressure jumps below the gas pressure and the gas expands into an unresisted space — is irreversible: it produces less work (in the limit of free expansion into a vacuum, zero work) for the same initial and final states. The reversible isothermal path gives the **maximum possible work** for an isothermal expansion between V_i and V_f, because it extracts work against the largest possible opposing force at every step.

This process appears in two critical places you will encounter soon. First, it is one of the four strokes of the **Carnot cycle** — the two isothermal steps (one at T_H, one at T_C) are where the engine exchanges heat with its reservoirs, and the reversibility of those strokes is what makes the Carnot engine achieve the maximum possible efficiency. Second, the entropy change ΔS = Q/T = nR ln(V_f/V_i) calculated here generalizes: for any process, reversible or not, ΔS between two equilibrium states is the same, so the reversible isothermal expression gives you a direct way to compute entropy changes for ideal gas expansions.
