---
id: boundary-work-pv-diagram
title: Boundary Work and P-V Diagrams
domain: physics
course: thermodynamics
prerequisites:
- id: work-and-energy
  type: hard
builds-toward:
- work-in-thermodynamic-processes
tags:
- work
- pv-diagram
- expansion
stage: formal-systems
status: draft
---

# Boundary Work and P-V Diagrams

## Core Idea
Boundary work (also called PV work) is W = ∫PdV, the work done by a gas as it expands or compresses against external pressure. On a P-V diagram, the area under the curve represents work. The actual work depends on the process path, not just initial and final states, making work a path function.

## How It's Best Learned
Sketch P-V diagrams for different processes and calculate work as the area under the curve. Compare isothermal, adiabatic, and polytropic expansions.

## Common Misconceptions
- Thinking work depends only on initial and final states; work is path-dependent.
- Forgetting sign conventions: work is positive when gas expands (does work on surroundings).

## Explainer

From your work on work and energy, you know that work is force times displacement. For a gas pushing a piston, that force is pressure times area (F = PA), and the displacement is dx, so the infinitesimal work done by the gas is dW = F dx = PA dx = P dV. Integrating gives **W = ∫P dV** — the boundary work, or PV work. The name "boundary work" reflects that this is work done at the moving boundary (the piston face) between the system and its surroundings. Every thermodynamic process that involves a volume change involves boundary work.

The P-V diagram is the key visualization tool. Plot pressure on the vertical axis and volume on the horizontal. Any thermodynamic process traces a path on this diagram, and the work done by the gas is the **area under the curve**. An expansion moves right (dV > 0), and the area is positive — the gas does work on the surroundings. A compression moves left (dV < 0), and the area is negative — the surroundings do work on the gas. For a constant-volume process (isochoric), the path is a vertical line and the area is zero: no boundary work is done. This geometric interpretation makes comparing processes immediate and intuitive.

The crucial insight is that this area — and therefore the work — depends on the shape of the path, not just its endpoints. Compare two ways to expand a gas from state A (high pressure, small volume) to state B (low pressure, large volume): path 1 expands at constant pressure then cools at constant volume; path 2 cools at constant volume then expands at constant pressure. Draw both on a P-V diagram and you will see they enclose different areas — the first path does more work than the second, even though they start and end at the same states. This is what "work is a path function" means: unlike internal energy, there is no function W(P, V) whose value at a state tells you the work. You must integrate along the actual process path.

For specific processes you will encounter repeatedly: a **constant-pressure** (isobaric) expansion has W = PΔV, a rectangle on the P-V diagram; an **isothermal** expansion of an ideal gas has P = nRT/V, giving W = nRT ln(V_f/V_i), a curved path; an **adiabatic** expansion (no heat exchange) has PV^γ = const, giving a steeper curve than isothermal. In a complete **cycle** — a closed loop on the P-V diagram — the net work is the enclosed area. Clockwise loops do net positive work (heat engines); counterclockwise loops require net work input (refrigerators). The P-V diagram is thus not just a bookkeeping tool but the geometric heart of thermodynamic cycle analysis.


