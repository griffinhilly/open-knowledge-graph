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
status: validated
---

# Boundary Work and P-V Diagrams

## Core Idea
Boundary work (also called PV work) is W = ∫PdV, the work done by a gas as it expands or compresses against external pressure. On a P-V diagram, the area under the curve represents work. The actual work depends on the process path, not just initial and final states, making work a path function.

## How It's Best Learned
Sketch P-V diagrams for different processes and calculate work as the area under the curve. Compare isothermal, adiabatic, and polytropic expansions.

## Common Misconceptions
- Thinking work depends only on initial and final states; work is path-dependent.
- Forgetting sign conventions: work is positive when gas expands (does work on surroundings).

## Questions

```yaml
- question: "A gas expands from state A (P=4 atm, V=1 L) to state B (P=1 atm, V=4 L) by two paths: Path 1 expands at constant P=4 atm then cools at constant V; Path 2 cools at constant V then expands at constant P=1 atm. Which path does more work?"
  type: multiple-choice
  options:
    - "Both paths do the same work because they share the same initial and final states"
    - "Path 1 does more work because it expands at the higher pressure"
    - "Path 2 does more work because the lower pressure expands over a larger volume range"
    - "Cannot be determined without knowing the temperature at each state"
  answer: 1
  explanation: "Work is path-dependent. Path 1 expands at P=4 atm over ΔV=3 L, giving W=12 atm·L (zero work in the constant-volume step). Path 2 has zero work in the constant-volume step then expands at P=1 atm over ΔV=3 L, giving W=3 atm·L. Path 1 does four times more work. On a P-V diagram, Path 1's curve encloses a much larger area. Option A — the intuitive 'same endpoints, same work' answer — is precisely the misconception this topic addresses: work is a path function, not a state function."

- question: "A gas is compressed from V=5 L to V=2 L at constant pressure. The boundary work done BY the gas is:"
  type: multiple-choice
  options:
    - "Positive, because pressure times volume is a positive quantity"
    - "Negative, because volume decreases (dV < 0) so W = ∫P dV < 0"
    - "Zero, because constant pressure means no net energy change"
    - "Positive, because the surroundings gain energy from the gas"
  answer: 1
  explanation: "Boundary work done by the gas is W = ∫P dV. During compression, volume decreases (dV < 0), so the integral is negative — the gas does negative work, meaning work is done ON the gas by the surroundings. On the P-V diagram, the path moves leftward and the area carries a negative sign by convention. Option D describes the surroundings' perspective; the question asks about the gas."

- question: "Two different processes connecting the same two states on a P-V diagram can do different amounts of work."
  type: true-false
  answer: true
  explanation: "This is the defining statement that work is a path function. Work equals the area under the process path on the P-V diagram, and two paths connecting the same endpoints can enclose vastly different areas. Unlike state functions (internal energy, temperature), there is no function W(P,V) — the work depends on every point along the route. This is why thermodynamic cycles produce nonzero net work: traversing a closed loop encloses a finite area."

- question: "An isochoric (constant-volume) process can do positive boundary work if pressure increases enough."
  type: true-false
  answer: false
  explanation: "Boundary work is W = ∫P dV. If volume is constant, dV = 0 everywhere, so W = 0 regardless of pressure change. On the P-V diagram, an isochoric process is a vertical line — there is no area in the horizontal direction. No boundary work is exchanged in a constant-volume process, no matter how much the pressure or temperature changes."

- question: "Explain what it means to say work is a 'path function' and why this matters for engineering applications."
  type: short-answer
  answer: "A path function is a quantity whose value depends on the process route, not just the starting and ending states. Work is a path function because W = ∫P dV — the integral along the actual process path on the P-V diagram. Different paths between the same two states produce different amounts of work. Engineers cannot speak of 'the work for this state change' without specifying the process. This also explains why heat engines extract net work from a thermodynamic cycle: the forward and return paths enclose nonzero area on the P-V diagram."
  explanation: "The contrast with state functions like internal energy (ΔU) illuminates this. ΔU depends only on initial and final states — path is irrelevant. But W and Q individually depend on the route. The first law ΔU = Q - W is non-trivial precisely because you can distribute the same ΔU between heat and work in infinitely many ways depending on the process path. Engine designers choose cycles (Carnot, Otto, Rankine) to maximize the enclosed P-V area relative to heat input."
```

## Explainer

From your work on work and energy, you know that work is force times displacement. For a gas pushing a piston, that force is pressure times area (F = PA), and the displacement is dx, so the infinitesimal work done by the gas is dW = F dx = PA dx = P dV. Integrating gives **W = ∫P dV** — the boundary work, or PV work. The name "boundary work" reflects that this is work done at the moving boundary (the piston face) between the system and its surroundings. Every thermodynamic process that involves a volume change involves boundary work.

The P-V diagram is the key visualization tool. Plot pressure on the vertical axis and volume on the horizontal. Any thermodynamic process traces a path on this diagram, and the work done by the gas is the **area under the curve**. An expansion moves right (dV > 0), and the area is positive — the gas does work on the surroundings. A compression moves left (dV < 0), and the area is negative — the surroundings do work on the gas. For a constant-volume process (isochoric), the path is a vertical line and the area is zero: no boundary work is done. This geometric interpretation makes comparing processes immediate and intuitive.

The crucial insight is that this area — and therefore the work — depends on the shape of the path, not just its endpoints. Compare two ways to expand a gas from state A (high pressure, small volume) to state B (low pressure, large volume): path 1 expands at constant pressure then cools at constant volume; path 2 cools at constant volume then expands at constant pressure. Draw both on a P-V diagram and you will see they enclose different areas — the first path does more work than the second, even though they start and end at the same states. This is what "work is a path function" means: unlike internal energy, there is no function W(P, V) whose value at a state tells you the work. You must integrate along the actual process path.

For specific processes you will encounter repeatedly: a **constant-pressure** (isobaric) expansion has W = PΔV, a rectangle on the P-V diagram; an **isothermal** expansion of an ideal gas has P = nRT/V, giving W = nRT ln(V_f/V_i), a curved path; an **adiabatic** expansion (no heat exchange) has PV^γ = const, giving a steeper curve than isothermal. In a complete **cycle** — a closed loop on the P-V diagram — the net work is the enclosed area. Clockwise loops do net positive work (heat engines); counterclockwise loops require net work input (refrigerators). The P-V diagram is thus not just a bookkeeping tool but the geometric heart of thermodynamic cycle analysis.


