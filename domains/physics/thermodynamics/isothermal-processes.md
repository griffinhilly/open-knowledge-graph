---
id: isothermal-processes
title: Isothermal Processes
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: hard
- id: ideal-gas-law
  type: hard
- id: work-as-integral
  type: soft
builds-toward:
- carnot-cycle
tags:
- isothermal
- constant-temperature
- Boyles-law
- work
- heat
stage: formal-systems
status: validated
---

# Isothermal Processes

## Core Idea
An isothermal process occurs at constant temperature. For an ideal gas, ΔU = 0 in any isothermal process (since U depends only on T), so by the first law, Q = W. The work done by the gas in expanding isothermally from V₁ to V₂ is W = nRT ln(V₂/V₁). On a PV diagram, an isotherm follows the hyperbola PV = constant. Isothermal processes require slow, quasi-static changes with continuous heat exchange to maintain constant temperature.

## How It's Best Learned
Derive the isothermal work integral from W = ∫P dV with P = nRT/V. Evaluate for specific numbers (e.g., 1 mol of gas at 300 K doubling its volume). Compare to the work that would be done in a free expansion — which is zero and is not quasi-static.

## Common Misconceptions
- Isothermal does not mean no heat exchange — isothermal processes require continuous heat exchange to maintain constant temperature.
- Real processes are not truly isothermal unless done infinitely slowly with a perfect heat reservoir.

## Explainer

You already know that thermodynamic processes are constrained by which state variables are held fixed. An **isothermal process** holds temperature T constant throughout. For an ideal gas, this single constraint has a powerful consequence via the ideal gas law: if T is fixed, then PV = nRT = constant, so pressure and volume move in inverse proportion along a **hyperbola** on the PV diagram. As you expand the gas, pressure drops; as you compress, pressure rises — always staying on the same isotherm.

The first law, ΔU = Q − W, becomes especially transparent here. For an ideal gas, internal energy U depends only on temperature (from the equipartition theorem you know from prerequisites). Since T is constant, ΔU = 0 for any isothermal process on an ideal gas. The first law then requires Q = W: every joule of work done by the expanding gas must be supplied as heat from the reservoir, and every joule of work done on a compressed gas must be expelled as heat. Temperature stays flat because the reservoir absorbs or supplies heat as needed — which is exactly why isothermal processes require continuous thermal contact with a reservoir.

The work integral W = ∫ P dV with P = nRT/V gives W = nRT ∫(V₁ to V₂) dV/V = nRT ln(V₂/V₁). Notice the logarithm: the work is not simply P·ΔV (which would be appropriate for a constant-pressure process) but depends on the ratio of volumes. Doubling the volume at 300 K for 1 mole of gas gives W = (8.314)(300) ln(2) ≈ 1729 J. This is less work than a constant-pressure expansion over the same volume range, because pressure drops continuously during the isothermal expansion.

The isothermal process appears in the **Carnot cycle** (your next topic) as the reversible heat exchange steps. Its reversibility is precisely why it requires infinite slowness: a truly quasi-static isothermal expansion allows the system to remain in equilibrium at every point, with no temperature gradients, no viscous dissipation, and no irreversibilities. Real industrial processes approach isothermal behavior when the working fluid is in good thermal contact with a large heat reservoir and changes are slow relative to thermal equilibration timescales — a useful approximation for slow compression of gases in heat exchangers.
