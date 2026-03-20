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
stage: advanced
status: validated
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

## Explainer

From your study of the Reynolds number, you know that flow transitions from laminar to turbulent when inertial forces overwhelm viscous forces — roughly at Re ≈ 2300 for pipe flow. Laminar flow has an orderly parabolic velocity profile and a friction factor that varies simply as f = 64/Re. Turbulent flow breaks that picture: the velocity profile is flatter, more uniform across the cross-section, with steeper velocity gradients only near the wall. And friction no longer depends only on Re. A second variable enters — the **relative roughness** ε/D, the ratio of the average wall roughness height to pipe diameter. Together, Re and ε/D govern the **Darcy friction factor** f, the key dimensionless parameter for calculating head loss in turbulent pipe flow.

The **Darcy-Weisbach equation** h_f = f(L/D)(V²/2g) relates head loss to friction factor, pipe geometry, and velocity. The challenge in turbulent flow is that f is not a simple closed-form function — the **Colebrook equation** is implicit in f, requiring iteration. The **Moody chart** solves this graphically: on a log-log plot of f vs. Re, each curve corresponds to a different ε/D value. Three regimes are visible. In the **smooth-pipe regime** (low Re or very smooth pipes), roughness is submerged in the viscous sublayer near the wall and plays no role; f depends only on Re and follows the Prandtl smooth-pipe law. In the **transition zone**, both Re and ε/D matter, and the Colebrook equation applies. In the **fully turbulent rough regime** (high Re and/or significant roughness), the viscous sublayer is eroded away, roughness elements protrude into the turbulent core, and f depends only on ε/D — the Moody chart curves become horizontal lines.

For practical calculations, the explicit **Swamee-Jain approximation** avoids iterative solution: f ≈ 0.25 / [log(ε/(3.7D) + 5.74/Re^0.9)]², accurate to within about 3% for most engineering purposes. The three classic pipe-flow problem types exercise different uses of this framework. Given pipe diameter and velocity, find head loss: direct substitution into Darcy-Weisbach. Given head loss, find velocity: iterate since f depends on Re which contains V. Given head loss and velocity, find diameter: iterate since both f and the Darcy-Weisbach equation contain D.

One practical trap deserves special attention: there are two different friction factors in common use. The **Darcy-Weisbach friction factor** (also called the Moody friction factor) used here is four times larger than the **Fanning friction factor** used in chemical engineering and some fluid mechanics texts. Both are legitimately called "friction factor" in the literature. Always check which convention your source uses — plugging the Fanning factor into the Darcy-Weisbach equation yields a head loss four times too low.
