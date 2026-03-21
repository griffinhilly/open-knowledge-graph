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

## Questions

```yaml
- question: "An ideal gas expands isothermally at 300 K. Which statement correctly describes the energy flow?"
  type: multiple-choice
  options:
    - "No heat flows in or out — the constant temperature means the thermal energy is unchanged"
    - "Heat flows into the gas from the reservoir, supplying the energy for the work done by the expanding gas"
    - "The internal energy increases because the gas now occupies a larger volume"
    - "The gas does work on the surroundings and its temperature drops, requiring external heating only to compensate"
  answer: 1
  explanation: "For an ideal gas, internal energy U depends only on temperature. Since T is constant (isothermal), ΔU = 0. The first law then gives Q = W: every joule of work the gas does on its surroundings must be supplied as heat from the reservoir. The most common misconception — option A — confuses 'temperature stays constant' with 'no heat flows.' The reservoir continuously supplies heat precisely to keep the temperature from dropping as the gas does work."

- question: "On a PV diagram, what shape does an isothermal process trace for an ideal gas, and why?"
  type: multiple-choice
  options:
    - "A horizontal line, because pressure is held constant during an isothermal process"
    - "A vertical line, because volume doesn't change at constant temperature"
    - "A hyperbola, because PV = nRT = constant means P and V vary inversely"
    - "A straight line with negative slope, because pressure decreases as volume increases"
  answer: 2
  explanation: "The ideal gas law PV = nRT. With T fixed, PV = constant, which is the equation of a hyperbola (P = C/V). As volume increases, pressure decreases, but their product stays the same. A horizontal line would be an isobaric (constant pressure) process; a vertical line would be an isochoric (constant volume) process. The hyperbolic isotherm is distinct from both."

- question: "An isothermal process requires the system to be thermally isolated from its surroundings to prevent heat exchange from changing the temperature."
  type: true-false
  answer: false
  explanation: "False — this is the opposite of what is required. An isothermal process demands continuous thermal contact with a heat reservoir. When the gas expands and does work, heat must flow in from the reservoir to prevent the temperature from dropping. If the system were thermally isolated (adiabatic), temperature would fall during expansion. Thermal isolation is the definition of an adiabatic process, not an isothermal one."

- question: "For an ideal gas in an isothermal expansion, the magnitude of heat absorbed by the gas equals the magnitude of work done by the gas."
  type: true-false
  answer: true
  explanation: "True. For an ideal gas, ΔU = 0 in any isothermal process because internal energy depends only on temperature (T = constant). The first law ΔU = Q − W then gives 0 = Q − W, so Q = W. Every joule of work output is matched by a joule of heat input from the reservoir. This makes isothermal processes perfectly efficient at converting heat to work within the process — though the Carnot efficiency limits apply to any full cycle."

- question: "Why doesn't the temperature of an ideal gas drop when it expands isothermally and does work on the surroundings? What prevents the cooling?"
  type: short-answer
  answer: "In a free expansion (no contact with a reservoir), the temperature of an ideal gas actually stays constant too — because ideal gas internal energy depends only on T, not volume. But in a quasi-static isothermal process against external pressure, the gas does real work, which would normally lower the kinetic energy of molecules and cool the gas. A heat reservoir in thermal contact continuously supplies heat Q = W to replace that energy, maintaining constant temperature. Without the reservoir, the process cannot be truly isothermal."
  explanation: "This question targets the distinction between 'isothermal' as a constraint maintained by a reservoir versus the accidental constancy of ideal gas internal energy. The reservoir is essential for quasi-static isothermal processes that do net work. In a Joule free expansion (into vacuum), no work is done, no heat flows, and T stays constant for an ideal gas regardless — but that process is irreversible and not quasi-static."
```

## Explainer

You already know that thermodynamic processes are constrained by which state variables are held fixed. An **isothermal process** holds temperature T constant throughout. For an ideal gas, this single constraint has a powerful consequence via the ideal gas law: if T is fixed, then PV = nRT = constant, so pressure and volume move in inverse proportion along a **hyperbola** on the PV diagram. As you expand the gas, pressure drops; as you compress, pressure rises — always staying on the same isotherm.

The first law, ΔU = Q − W, becomes especially transparent here. For an ideal gas, internal energy U depends only on temperature (from the equipartition theorem you know from prerequisites). Since T is constant, ΔU = 0 for any isothermal process on an ideal gas. The first law then requires Q = W: every joule of work done by the expanding gas must be supplied as heat from the reservoir, and every joule of work done on a compressed gas must be expelled as heat. Temperature stays flat because the reservoir absorbs or supplies heat as needed — which is exactly why isothermal processes require continuous thermal contact with a reservoir.

The work integral W = ∫ P dV with P = nRT/V gives W = nRT ∫(V₁ to V₂) dV/V = nRT ln(V₂/V₁). Notice the logarithm: the work is not simply P·ΔV (which would be appropriate for a constant-pressure process) but depends on the ratio of volumes. Doubling the volume at 300 K for 1 mole of gas gives W = (8.314)(300) ln(2) ≈ 1729 J. This is less work than a constant-pressure expansion over the same volume range, because pressure drops continuously during the isothermal expansion.

The isothermal process appears in the **Carnot cycle** (your next topic) as the reversible heat exchange steps. Its reversibility is precisely why it requires infinite slowness: a truly quasi-static isothermal expansion allows the system to remain in equilibrium at every point, with no temperature gradients, no viscous dissipation, and no irreversibilities. Real industrial processes approach isothermal behavior when the working fluid is in good thermal contact with a large heat reservoir and changes are slow relative to thermal equilibration timescales — a useful approximation for slow compression of gases in heat exchangers.
