---
id: moody-diagram-friction-factor
title: Moody Diagram and Friction Factor
domain: engineering
course: fluid-mechanics
prerequisites:
- id: turbulent-pipe-flow
  type: hard
- id: reynolds-number
  type: hard
tags:
- Moody diagram
- Darcy friction factor
- Colebrook equation
- pipe roughness
- flow regimes
- Darcy-Weisbach
stage: formal-systems
status: validated
---
# Moody Diagram and Friction Factor

## Core Idea
The Moody diagram is the central engineering tool for pipe flow analysis, plotting the Darcy friction factor f against Reynolds number Re_D for various values of relative roughness ε/D. It encodes three regimes: laminar (f = 64/Re, independent of roughness), transitional (Re ≈ 2000–4000, uncertain and avoided in design), and turbulent (f depends on both Re and ε/D). In the turbulent regime, smooth pipes follow the Blasius correlation (f ≈ 0.316/Re^0.25) at moderate Re, while at high Re the friction factor becomes independent of Re and depends only on roughness — the fully rough regime. The implicit Colebrook equation, 1/√f = −2.0 log(ε/3.7D + 2.51/Re√f), unifies the smooth and rough limits and is the basis for the turbulent portion of the Moody diagram. The friction factor enters the Darcy-Weisbach equation h_f = f(L/D)(V²/2g) to compute head loss in pipes.

## How It's Best Learned
Use the Moody diagram to solve a series of pipe flow problems: given flow rate, pipe size, and material (roughness), find the pressure drop; then reverse the problem to find required diameter for a given allowable head loss. Iterate the Colebrook equation by hand for one case, then compare against the explicit Swamee-Jain approximation. Plot your own Moody diagram from the Colebrook equation to understand why the curves fan out at higher roughness and collapse to the laminar line at low Re.

## Common Misconceptions
- The Darcy friction factor is 4 times the Fanning friction factor. Confusing the two introduces a factor-of-4 error in head loss — always check which convention a source uses.
- Roughness that matters is the sand-grain equivalent roughness ε, not the actual surface profile. Real surfaces have different roughness characters (riveted steel vs. corroded cast iron) that map to different equivalent sand-grain values.
- The "fully rough" regime does not mean the flow is more turbulent — it means the roughness elements protrude beyond the viscous sublayer, so viscous effects no longer influence the friction factor and f becomes independent of Re.

## Questions

```yaml
- question: "A pipe carrying water operates at Re = 5×10⁶ and relative roughness ε/D = 0.05 (fully rough regime). An engineer doubles the flow velocity, which doubles the Reynolds number to 10⁷. What is the best prediction for the Darcy friction factor?"
  type: multiple-choice
  options:
    - "It decreases significantly, because higher Re means a thinner viscous sublayer and less friction"
    - "It stays approximately the same, because in the fully rough regime f depends only on ε/D, not Re"
    - "It doubles, because friction scales with velocity in turbulent flow"
    - "It falls to zero, because viscous effects become negligible at very high Re"
  answer: 1
  explanation: "In the fully rough regime, roughness elements protrude through the viscous sublayer so thoroughly that viscous effects no longer influence friction. The Moody diagram shows horizontal asymptotes on the right — f depends only on relative roughness ε/D, not Re. Doubling Re changes nothing. The common misconception is that more turbulence always means more friction variation, but the fully rough regime is defined precisely by this independence from Re."

- question: "A reference gives the Fanning friction factor f_F = 0.005 for a pipe flow. What Darcy friction factor should be used in the Darcy-Weisbach equation h_f = f(L/D)(V²/2g)?"
  type: multiple-choice
  options:
    - "0.005 — the two friction factors are identical"
    - "0.00125 — the Darcy factor is one-quarter of the Fanning factor"
    - "0.010 — the Darcy factor is twice the Fanning factor"
    - "0.020 — the Darcy factor is four times the Fanning factor"
  answer: 3
  explanation: "f_Darcy = 4 × f_Fanning. This is one of the most consequential unit-convention errors in fluid mechanics — confusing the two introduces a factor-of-4 error in calculated head loss. Always check which convention a reference uses. The Darcy-Weisbach equation as written above uses the Darcy (Moody) friction factor."

- question: "In laminar pipe flow (Re < 2000), a smoother pipe wall will produce a lower friction factor than a rougher one."
  type: true-false
  answer: false
  explanation: "In laminar flow, the viscous sublayer is thick enough to completely cover all surface roughness. The flowing fluid 'sees' a smooth wall regardless of actual surface condition. The friction factor f = 64/Re exactly in laminar flow — independent of roughness. Roughness only matters once the flow is turbulent and the viscous sublayer thins enough for roughness elements to protrude through it."

- question: "In the fully turbulent (fully rough) regime, the Darcy friction factor depends only on relative roughness ε/D and becomes independent of Reynolds number."
  type: true-false
  answer: true
  explanation: "Correct. This is the defining characteristic of the fully rough regime: roughness elements fully protrude beyond the viscous sublayer, generating turbulent eddies and pressure drag that dominate friction. Viscous effects — which depend on Re — become negligible. On the Moody diagram, each ε/D curve converges to a horizontal asymptote at high Re, reading a constant f determined solely by ε/D."

- question: "Why must the Colebrook equation be solved iteratively rather than directly for the friction factor, and what does this imply about engineering practice?"
  type: short-answer
  answer: "The Colebrook equation is implicit in f — f appears inside the square root on the right-hand side as well as on the left. It cannot be algebraically rearranged to give f explicitly. In practice, you start with an initial guess (e.g., f = 0.02), substitute into the right side, solve for a new f, and repeat until convergence (typically 2–3 iterations). The explicit Swamee-Jain approximation avoids iteration at the cost of a small error (~3%). The Moody diagram is a graphical solution to the same equation."
  explanation: "The iterative nature reflects that turbulent friction involves a genuine self-consistent relationship: the friction factor depends on flow conditions that in turn depend on the friction factor (through velocity and head loss). Engineers in practice either use the Moody diagram graphically, the Swamee-Jain approximation explicitly, or run 2–3 Colebrook iterations — all converge quickly because f varies weakly with Re in the turbulent regime."
```

## Explainer

Pipe flow problems share a common structure: you know the geometry (length, diameter, roughness) and the flow rate, and you need to find the pressure drop — or vice versa. The Darcy-Weisbach equation, h_f = f(L/D)(V²/2g), reduces all the fluid physics to a single dimensionless number: the **Darcy friction factor** f. But f is not a constant — it depends on flow regime and surface condition, which is exactly what the Moody diagram encodes.

From your Reynolds number prerequisite, you know Re = VD/ν and that laminar flow (Re < 2000) has a parabolic velocity profile with analytic friction behavior. In laminar flow, f = 64/Re exactly — no roughness dependence, because the smooth viscous sublayer that covers the wall completely masks whatever roughness lies beneath it. As Re increases into the turbulent regime (Re > 4000), the viscous sublayer thins. Once it becomes thin enough that roughness elements protrude through it, those elements generate turbulent eddies and pressure-drag contributions that add to friction. Smooth-pipe turbulence follows the Blasius correlation — f ≈ 0.316/Re^0.25 — valid for moderate Re. Rough pipes follow a higher f that depends on relative roughness ε/D, where ε is the sand-grain equivalent roughness. At very high Re, the sublayer is so thin that the rough elements fully dominate and f becomes independent of Re: this is the **fully rough** regime, represented by the horizontal asymptotes at the right edge of the Moody diagram.

The **Colebrook equation** — 1/√f = −2.0 log(ε/3.7D + 2.51/Re√f) — is the implicit formula that generates the entire turbulent region of the Moody diagram. It is implicit in f, so solving it requires iteration: start with a first guess (e.g., f = 0.02), substitute into the right side, compute a new f, repeat until convergence (2–3 iterations typically suffice). The explicit Swamee-Jain approximation avoids iteration at the cost of a small error. In practice, the Moody diagram is a graphical version of the Colebrook equation: you locate your Re on the x-axis, trace horizontally to your ε/D curve, then read f on the y-axis.

Using the diagram for a real problem: you need the pipe diameter to deliver a specified flow rate within an allowable pressure drop. This "sizing" problem is iterative because both Re and f depend on V, which depends on the diameter you're trying to find. The standard approach is to assume a diameter, compute Re and ε/D, read f from the Moody diagram, check the head loss, and adjust. Alternatively, because f varies weakly with Re in the turbulent regime, a first guess of f ≈ 0.02 followed by one or two diagram corrections typically converges quickly. Every pipe system — water distribution networks, HVAC ducting, oil pipelines — runs through this same calculation, making the Moody diagram one of the most practically used figures in all of engineering fluid mechanics.
