---
id: pipe-roughness-absolute-relative
title: 'Pipe Roughness: Absolute and Relative Effects on Friction'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: friction-factor-determination-methods
  type: hard
- id: moody-diagram-friction-factor
  type: soft
builds-toward:
- pipe-network-solutions-hardy-cross
tags:
- roughness
- friction-factor
- surface-texture
stage: advanced
status: draft
---

# Pipe Roughness: Absolute and Relative Effects on Friction

## Core Idea
Absolute roughness (ε, actual surface irregularity height) becomes significant only at high Reynolds numbers where the viscous sublayer shrinks below roughness projections. Relative roughness (ε/D) determines the friction factor in turbulent flow; smooth pipes and very rough pipes have asymptotic limits on the Moody chart. Pipe age and material cause roughness to increase, increasing friction factor and reducing system capacity over time.

## Explainer

You already know from the Moody diagram that the friction factor f depends on two parameters: Reynolds number Re and relative roughness ε/D. But why does relative roughness — rather than absolute roughness ε alone — determine friction losses? The answer lies in how turbulent flow actually interacts with a rough surface, and understanding it gives you physical intuition for what the Moody chart is showing.

Even in turbulent flow, there is a thin layer of fluid immediately adjacent to the pipe wall — the **viscous sublayer** — where viscosity dominates and flow is essentially laminar. This sublayer has a thickness that scales inversely with Reynolds number: the faster and more turbulent the flow, the thinner the sublayer. **Absolute roughness** ε describes the physical height of the surface irregularities (sand grains, machining marks, corrosion bumps). The critical comparison is between ε and the sublayer thickness. When the sublayer is thicker than ε, the roughness is buried beneath it; the pipe behaves as hydraulically smooth, and friction depends only on Re (the smooth-pipe region of the Moody chart). When Re is high enough that the sublayer shrinks below ε, roughness elements protrude into the turbulent core, generate additional eddies, and dramatically increase friction losses.

**Relative roughness** ε/D enters because what matters for a fluid parcel traveling through a pipe is not the absolute size of the bumps but how large they are relative to the flow channel. A roughness height of 0.1 mm in a 10-mm pipe (ε/D = 0.01) creates ten times more disruption per diameter of travel than the same roughness in a 100-mm pipe (ε/D = 0.001). At very high Reynolds numbers — the fully rough regime — the viscous sublayer effectively disappears and friction losses become independent of Re entirely, depending only on ε/D. On the Moody chart this appears as horizontal lines at large Re: once fully rough, increasing flow speed no longer changes the friction factor because viscosity has stopped being relevant.

The engineering implication is significant for long-lived piping systems. A new commercial steel pipe has ε ≈ 0.046 mm; after years of service, corrosion and biological fouling can increase ε by an order of magnitude. For a 200-mm pipe (ε/D going from 0.00023 to 0.002), this shifts the friction factor from roughly 0.015 to 0.024 in fully turbulent flow — a 60% increase. Pipeline operators use this to project how pump station requirements will grow over the service life of a pipeline, and to plan cleaning or relining schedules. When you encounter a field pipe with an unexpectedly high head loss, ε/D degradation from aging is often the first thing to check.
