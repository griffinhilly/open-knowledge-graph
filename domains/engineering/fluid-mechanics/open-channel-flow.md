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

## Explainer

Pipe flow and open-channel flow both obey Bernoulli's equation, but with a crucial difference: in a pipe, pressure is the primary unknown that adjusts to satisfy continuity. In an open channel, pressure at the free surface is always atmospheric — it is not free to vary. Instead, **depth** adjusts. This makes open-channel flow a problem in which geometry (depth, width, slope) and gravity drive everything, and the free surface is the key unknown. Rivers, irrigation canals, spillways, and storm drains are all open-channel systems.

The **Froude number** Fr = V/√(gD) is the open-channel analogue of the Mach number in gas dynamics. The denominator √(gD) is the speed at which small surface gravity waves propagate in water of depth D. When Fr < 1 (**subcritical flow**), disturbances propagate upstream — throw a rock in a slow, deep river and ripples travel in all directions. When Fr > 1 (**supercritical flow**), the flow outruns its own disturbances — waves cannot propagate upstream, just as a supersonic airplane outruns its own pressure waves. At Fr = 1 (critical flow), disturbances stand still. This wave-speed analogy fully explains why subcritical flow responds to downstream conditions (backwater effects) while supercritical flow does not.

**Manning's equation** Q = (1/n)·A·R_h^(2/3)·S^(1/2) is the workhorse of open-channel design. The hydraulic radius R_h = A/P (cross-sectional area over wetted perimeter) is the effective depth for friction purposes. The slope S is the channel bed slope (or energy grade line slope). Manning's n is an empirical roughness coefficient: n ≈ 0.010–0.013 for smooth concrete, 0.025–0.035 for natural channels, up to 0.05–0.15 for very rough or vegetated channels. The equation is not dimensionally consistent — n has implicit units — so you must use matched unit systems (SI or English, not mixed). For design, you typically know Q and channel geometry and solve for the required slope or depth.

A **hydraulic jump** is one of the most spectacular phenomena in fluid mechanics: a standing, turbulent transition in which supercritical flow suddenly decelerates to subcritical flow, depth increases abruptly, and significant energy is dissipated as heat and noise. It is the open-channel analogue of a shock wave in gas dynamics. Hydraulic jumps occur naturally below dam spillways and sluice gates; engineers deliberately induce them in **stilling basins** to dissipate the energy of high-velocity spillway discharge before it scours downstream riverbeds. The upstream and downstream depths in a jump are related by the conjugate depth equation derived from momentum conservation (not energy, since energy is lost). The energy dissipated — the **head loss** — increases with the strength of the jump, and a strong jump (high upstream Froude number) can dissipate 50–80% of the incoming kinetic energy.
