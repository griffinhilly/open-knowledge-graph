---
id: control-volume-steady-flow-mass
title: 'Control Volume Analysis: Mass Balance'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: continuity-equation-fluid
  type: hard
- id: momentum-equation-control-volume
  type: soft
builds-toward:
- control-volume-momentum-applications
- mechanical-energy-balance-pump-turbine
tags:
- control-volume
- conservation
- continuity
- mass-flow
stage: formal-systems
status: validated
---
# Control Volume Analysis: Mass Balance

## Core Idea
The continuity equation for steady flow states that mass flow rate in equals mass flow rate out for a control volume. Extended to multiple inlets and outlets, Σ(ṁ_in) = Σ(ṁ_out). This fundamental conservation principle applies to all fluid systems regardless of complexity and forms the basis for solving incompressible flow problems with varying areas and velocities.

## Questions

```yaml
- question: "Water flows through a horizontal pipe that narrows from area A₁ = 0.04 m² to A₂ = 0.01 m². If the inlet velocity is V₁ = 2 m/s, what is the outlet velocity V₂?"
  type: multiple-choice
  options:
    - "0.5 m/s — the velocity decreases as the pipe narrows to maintain pressure"
    - "2 m/s — velocity is constant through a steady flow pipe"
    - "8 m/s — volume flow rate is conserved, so A₁V₁ = A₂V₂"
    - "4 m/s — cross-sectional area decreases by factor 4, so velocity doubles"
  answer: 2
  explanation: "For steady, incompressible flow, Q = A₁V₁ = A₂V₂. With A₁ = 0.04 m² and V₁ = 2 m/s, Q = 0.08 m³/s. At outlet, V₂ = Q/A₂ = 0.08/0.01 = 8 m/s. The area decreased by a factor of 4, so velocity increased by a factor of 4. Option A inverts the relationship — velocity increases, not decreases, when area decreases. Option D has an arithmetic error: it correctly identifies the factor-of-4 area decrease but incorrectly says velocity only doubles."

- question: "A pipe branches at a T-junction into two outlet pipes. The inlet carries water at ṁ_in = 10 kg/s. One outlet carries ṁ_out,1 = 6 kg/s. Without knowing the pipe geometry or velocities, what is ṁ_out,2?"
  type: multiple-choice
  options:
    - "4 kg/s — from Σṁ_in = Σṁ_out for steady flow"
    - "6 kg/s — the second outlet matches the first by symmetry"
    - "10 kg/s — each outlet receives the full inlet mass flow"
    - "Cannot be determined without knowing the pipe diameters"
  answer: 0
  explanation: "For steady flow, mass cannot accumulate inside the control volume: Σṁ_in = Σṁ_out. Therefore 10 = 6 + ṁ_out,2, giving ṁ_out,2 = 4 kg/s. No knowledge of pipe geometry, fluid velocity, or internal flow details is needed — the control volume method only requires boundary values. Option D is wrong precisely because the control volume method eliminates the need for interior knowledge; only what crosses the boundary matters."

- question: "In steady, incompressible flow through a pipe that narrows, the fluid velocity decreases at the narrower section to conserve momentum."
  type: true-false
  answer: false
  explanation: "In steady, incompressible flow, it is VOLUME FLOW RATE (Q = AV) that is conserved, not momentum. When area A decreases, velocity V must INCREASE to maintain constant Q. A narrowing (nozzle) accelerates the flow; a widening (diffuser) decelerates it. The misconception often arises from intuition about traffic — fewer lanes, slower speed. But fluid is incompressible and continuous: it cannot queue up at a narrowing, so each element speeds up to pass through the smaller opening at the same volumetric rate."

- question: "The steady-flow mass balance for a control volume applies regardless of the complexity of the flow inside the boundary, including turbulence, swirling, and heat transfer."
  type: true-false
  answer: true
  explanation: "The control volume mass balance is a macroscopic conservation law — it only requires that mass is conserved (always true) and that conditions are steady (nothing accumulates inside). The internal flow structure, however complex, is irrelevant. Turbulence, swirling, mixing, chemical reactions, heat transfer inside the CV — none of these affect the boundary accounting. This is the fundamental power of the control volume framework: it reduces complex interior problems to boundary-condition bookkeeping."

- question: "Explain why the control volume method is useful for fluid mechanics problems, and what 'steady flow' allows you to simplify."
  type: short-answer
  answer: "The control volume method replaces the need to track every fluid particle with a boundary accounting approach: you define an imaginary surface around a region and only track what crosses it. This is useful because real fluid flows inside complex geometries are often intractable to solve in detail. The 'steady flow' simplification eliminates time-dependence: with steady conditions, nothing accumulates inside the CV, so whatever flows in must immediately flow out. This gives Σṁ_in = Σṁ_out — a simple algebraic statement that can solve for unknown velocities or areas at any port without solving the interior flow field at all."
  explanation: "For incompressible flow, density cancels and the equation becomes Σ(AV)_in = Σ(AV)_out. This is why engineers can design pipe networks, pumps, and nozzles using only inlet and outlet conditions — the control volume framework makes the interior a black box."
```

## Explainer

The **control volume** method is an accounting framework. You draw an imaginary boundary around any region of space — a pipe section, a pump, a valve, the interior of a nozzle — and then track what crosses that boundary. You already know from the continuity equation that mass is conserved everywhere in a flow field. The control volume approach takes that local statement and turns it into a global accounting tool: instead of tracking every fluid particle, you only watch what enters and exits the boundary you chose.

For **steady flow**, the key simplification is that nothing accumulates inside the control volume. The density and velocity fields inside are frozen in time. Whatever mass flows in must flow out at exactly the same rate. This gives you Σ(ṁ_in) = Σ(ṁ_out), where **mass flow rate** ṁ = ρAV at each port: density times cross-sectional area times average velocity. If the geometry is simple — one inlet, one outlet — this reduces to ρ₁A₁V₁ = ρ₂A₂V₂.

The real power appears when the geometry is complex. Consider a T-junction where one inlet pipe splits into two outlet branches. You don't need to solve the flow field inside the junction. You only need to know that ṁ_in = ṁ_out,1 + ṁ_out,2. You can solve for an unknown velocity or area in one branch given the other quantities. The interior of the control volume is a black box — only the boundary values matter for the mass balance.

For **incompressible** flows (liquids, and gases at low Mach number), density is constant, so mass conservation becomes **volume flow rate** conservation: Q_in = Q_out, where Q = AV. This is why a pipe that narrows must have higher velocity at the narrow section: A decreases, so V must increase to keep Q constant. The nozzle accelerates flow and the diffuser decelerates it — both follow directly from this single conservation statement. Most hydraulic engineering problems reduce to applying this principle systematically at each junction and section in a network.
