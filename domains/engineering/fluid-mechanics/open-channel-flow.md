---
id: open-channel-flow
title: Open Channel Flow
domain: engineering
course: fluid-mechanics
prerequisites:
- id: bernoullis-equation
  type: hard
- id: reynolds-number
  type: soft
- id: dimensional-analysis-and-similarity
  type: soft
tags:
- open channel
- Manning's equation
- Froude number
- hydraulic jump
- critical flow
stage: advanced
status: validated
---

# Open Channel Flow

## Core Idea
Open channel flow has a free surface exposed to atmospheric pressure, making it fundamentally different from pipe flow. The Froude number Fr = V/√(gD) distinguishes subcritical (Fr < 1, disturbances propagate upstream) from supercritical (Fr > 1, disturbances cannot propagate upstream) flow. Manning's equation Q = (1/n)A·R_h^(2/3)·S^(1/2) relates discharge to channel geometry and slope. A hydraulic jump — a standing wave transition from supercritical to subcritical flow — dissipates energy and is analogous to a shock wave in gas dynamics.

## How It's Best Learned
Use specific energy diagrams to visualize how depth and velocity trade off at fixed discharge. Identify critical depth (minimum specific energy for given Q) and compute it for rectangular channels. Observe hydraulic jumps in a flume or kitchen sink to see the abrupt depth increase and energy dissipation.

## Common Misconceptions
- Faster flow (higher velocity) is not always 'supercritical'; the Froude number depends on both velocity and depth — a deep, fast river can be subcritical.
- Manning's n is an empirical roughness coefficient with units; unlike the Darcy-Weisbach approach, Manning's equation is not dimensionally consistent and requires SI or English unit conventions.
- A hydraulic jump always transitions from supercritical to subcritical, never the reverse — flow cannot jump from subcritical to supercritical.

## Questions

```yaml
- question: "A river has a mean velocity of 5 m/s and an average depth of 5 m. A student classifies it as supercritical because 5 m/s is 'fast flow.' Evaluate this classification."
  type: multiple-choice
  options:
    - "Correct — 5 m/s exceeds the threshold speed for supercritical flow in most natural channels"
    - "Incorrect — the Froude number Fr = V/√(gD) = 5/√(9.81 × 5) ≈ 0.71 < 1, so the flow is subcritical despite the high velocity"
    - "Incorrect — velocity alone never determines flow regime; you need to know the channel slope"
    - "Correct — depth only matters for laminar flow; at turbulent velocities, Fr is not the relevant criterion"
  answer: 1
  explanation: "Fr = 5 / √(9.81 × 5) = 5 / √49.05 = 5 / 7.0 ≈ 0.71 < 1 → subcritical. The denominator √(gD) is the speed of small surface gravity waves in water of depth D. At depth 5 m, gravity waves travel at ~7 m/s, faster than the flow velocity of 5 m/s, so disturbances can still propagate upstream — subcritical. A flow at 5 m/s in a 0.1 m deep channel would be supercritical (Fr = 5/√0.98 ≈ 5.1). The critical insight is that both velocity and depth determine the Froude number; high velocity in deep water can still be subcritical."

- question: "A sluice gate releases water at velocity 8 m/s and depth 0.5 m into a downstream stilling basin (Fr = 8/√(9.81 × 0.5) ≈ 3.6). An engineer wants to design a hydraulic jump to dissipate this energy. Which statement correctly describes the required conditions?"
  type: multiple-choice
  options:
    - "The jump will form spontaneously as long as the downstream channel is deeper, transitioning from subcritical to supercritical flow"
    - "The supercritical flow must be forced to transition to subcritical flow; the jump proceeds from supercritical to subcritical, never the reverse"
    - "The engineer can design the jump to run in either direction by adjusting the downstream depth"
    - "A hydraulic jump requires Fr > 5; at Fr = 3.6, the flow will simply decelerate gradually"
  answer: 1
  explanation: "A hydraulic jump is an irreversible transition from supercritical (Fr > 1) to subcritical (Fr < 1) flow — always in this direction, never the reverse. The thermodynamic reason is entropy: a hydraulic jump dissipates energy (head loss is positive), making it physically possible. A transition from subcritical to supercritical would require energy addition, not dissipation. The engineer designs the stilling basin to provide a tailwater (downstream) depth equal to the conjugate depth, which forces the transition at the desired location. The incoming Fr ≈ 3.6 indicates a 'strong' jump that will dissipate roughly 30–40% of the kinetic energy."

- question: "In a subcritical river reach, constructing a dam downstream will raise the water surface upstream for a considerable distance (backwater effect), but this effect would not occur if the river were supercritical."
  type: true-false
  answer: true
  explanation: "The Froude number determines whether disturbances can propagate upstream. In subcritical flow (Fr < 1), surface gravity waves travel faster than the flow velocity, so information about the dam (a downstream boundary condition) propagates upstream as a backwater curve. In supercritical flow (Fr > 1), the flow outruns all disturbances — no wave can travel faster than the current against the flow. A dam placed downstream of a supercritical reach would cause a hydraulic jump immediately at the dam face, but the surface profile upstream of the jump would be unaffected by the dam's presence."

- question: "Manning's equation Q = (1/n)·A·R_h^(2/3)·S^(1/2) is dimensionally consistent and can be applied with any unit system by simply substituting the appropriate values."
  type: true-false
  answer: false
  explanation: "Manning's equation is empirical and dimensionally inconsistent — Manning's n carries implicit dimensions to make the equation balance. In SI units, n has effective units of s/m^(1/3); in English units (feet, seconds), n has different effective dimensions. The equation was fitted to data in specific unit systems and produces correct results only when the unit system matches the convention used. Mixing SI and English units, or using the SI form of the equation with English measurements without correction, gives errors of roughly 50%. The Darcy-Weisbach equation for pipe flow is dimensionally consistent and unit-agnostic; Manning's equation is not."

- question: "Explain the analogy between the Froude number in open channel flow and the Mach number in compressible gas dynamics — what physical quantities are being compared in each case, and why does the analogy hold?"
  type: short-answer
  answer: "Both the Froude number and the Mach number compare a flow velocity to the speed of small disturbance propagation in that medium. The Mach number Ma = V/c compares flow velocity to the speed of sound (pressure waves) in a compressible gas. The Froude number Fr = V/√(gD) compares flow velocity to the speed of surface gravity waves in a channel of depth D. In both cases, when the flow velocity exceeds the wave speed (Ma > 1 or Fr > 1), disturbances generated at a point cannot propagate against the flow — the flow outruns its own signals. This produces identical physical phenomena: shock waves in gas dynamics correspond to hydraulic jumps in open-channel flow, both being abrupt transitions from supersonic/supercritical to subsonic/subcritical conditions with irreversible energy dissipation. The analogy holds because both cases involve a critical wave speed that divides disturbance-transmitting regimes from disturbance-blocking regimes."
  explanation: "The analogy is not merely pedagogical — it reflects a deep mathematical similarity. The governing equations for shallow water flow and one-dimensional compressible gas flow have the same mathematical form, with the ratio of specific heats in the gas equations corresponding to a factor of 2 in the shallow water equations. This means solutions, stability criteria, and wave phenomena in one domain translate directly to the other. Engineers and physicists studying one domain routinely draw on intuition from the other."
```

## Explainer

Pipe flow and open-channel flow both obey Bernoulli's equation, but with a crucial difference: in a pipe, pressure is the primary unknown that adjusts to satisfy continuity. In an open channel, pressure at the free surface is always atmospheric — it is not free to vary. Instead, **depth** adjusts. This makes open-channel flow a problem in which geometry (depth, width, slope) and gravity drive everything, and the free surface is the key unknown. Rivers, irrigation canals, spillways, and storm drains are all open-channel systems.

The **Froude number** Fr = V/√(gD) is the open-channel analogue of the Mach number in gas dynamics. The denominator √(gD) is the speed at which small surface gravity waves propagate in water of depth D. When Fr < 1 (**subcritical flow**), disturbances propagate upstream — throw a rock in a slow, deep river and ripples travel in all directions. When Fr > 1 (**supercritical flow**), the flow outruns its own disturbances — waves cannot propagate upstream, just as a supersonic airplane outruns its own pressure waves. At Fr = 1 (critical flow), disturbances stand still. This wave-speed analogy fully explains why subcritical flow responds to downstream conditions (backwater effects) while supercritical flow does not.

**Manning's equation** Q = (1/n)·A·R_h^(2/3)·S^(1/2) is the workhorse of open-channel design. The hydraulic radius R_h = A/P (cross-sectional area over wetted perimeter) is the effective depth for friction purposes. The slope S is the channel bed slope (or energy grade line slope). Manning's n is an empirical roughness coefficient: n ≈ 0.010–0.013 for smooth concrete, 0.025–0.035 for natural channels, up to 0.05–0.15 for very rough or vegetated channels. The equation is not dimensionally consistent — n has implicit units — so you must use matched unit systems (SI or English, not mixed). For design, you typically know Q and channel geometry and solve for the required slope or depth.

A **hydraulic jump** is one of the most spectacular phenomena in fluid mechanics: a standing, turbulent transition in which supercritical flow suddenly decelerates to subcritical flow, depth increases abruptly, and significant energy is dissipated as heat and noise. It is the open-channel analogue of a shock wave in gas dynamics. Hydraulic jumps occur naturally below dam spillways and sluice gates; engineers deliberately induce them in **stilling basins** to dissipate the energy of high-velocity spillway discharge before it scours downstream riverbeds. The upstream and downstream depths in a jump are related by the conjugate depth equation derived from momentum conservation (not energy, since energy is lost). The energy dissipated — the **head loss** — increases with the strength of the jump, and a strong jump (high upstream Froude number) can dissipate 50–80% of the incoming kinetic energy.
