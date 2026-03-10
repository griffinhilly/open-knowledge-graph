---
id: turbulent-pipe-flow
title: Turbulent Pipe Flow and the Moody Chart
domain: engineering
course: fluid-mechanics
prerequisites:
- id: reynolds-number
  type: hard
- id: laminar-pipe-flow
  type: soft
- id: dimensional-analysis-and-similarity
  type: soft
builds-toward:
- pipe-system-losses
tags:
- turbulent flow
- Moody chart
- friction factor
- Colebrook equation
- roughness
stage: formal-systems
status: draft
---

# Turbulent Pipe Flow and the Moody Chart

## Core Idea
Turbulent pipe flow (Re > 4000) has a flatter velocity profile than laminar flow and a friction factor that depends on both Re and relative roughness ε/D. The Colebrook equation implicitly defines f for turbulent flow; the Moody chart graphically displays f vs. Re for various ε/D values. For fully turbulent rough flow, f depends only on roughness. The Darcy-Weisbach equation h_f = f(L/D)(V²/2g) gives head loss in terms of the friction factor.

## How It's Best Learned
Use the Moody chart fluently before applying the Colebrook equation iteratively. Practice the three standard pipe problems: given Q find ΔP, given ΔP find Q, and given ΔP and Q find D. The latter two require iteration since f depends on Re which depends on the unknown.

## Common Misconceptions
- The friction factor f in the Darcy-Weisbach equation is four times the Fanning friction factor used in some textbooks — always confirm which convention is used.
- Smooth pipes still have turbulent friction loss; 'smooth' means hydraulically smooth (roughness sublayer buried in viscous sublayer), not zero loss.
- At very high Re in rough pipes, f becomes constant (fully rough regime) and is independent of Re.
