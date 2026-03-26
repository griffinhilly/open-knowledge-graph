---
id: work-in-thermodynamic-processes
title: Work in Thermodynamic Processes
domain: physics
course: thermodynamics
prerequisites:
- id: ideal-gas-law
  type: hard
- id: work-and-energy
  type: hard
- id: work-as-integral
  type: soft
- id: definite-integral-definition
  type: soft
builds-toward:
- first-law-of-thermodynamics
- thermodynamic-processes
tags:
- thermodynamic-work
- PV-work
- expansion
- compression
- area-under-PV-curve
stage: formal-systems
status: validated
---

# Work in Thermodynamic Processes

## Core Idea
In thermodynamics, work done by a gas expanding against an external pressure is W = ∫P dV. For a process on a PV diagram, work equals the area under the P-V curve. Work is positive when a gas expands (does work on surroundings) and negative when compressed (surroundings do work on the gas). The work done in a cyclic process — traversing a closed loop on a PV diagram — equals the enclosed area, and its sign depends on whether the loop is traversed clockwise (net positive work out) or counterclockwise.

## How It's Best Learned
Calculate work graphically from PV diagrams before applying formulas. Compare work done along different paths between the same two states — this path-dependence is fundamental and distinguishes work and heat from state functions like internal energy.

## Common Misconceptions
- Work in thermodynamics is not simply force times distance — it is pressure times change in volume.
- Work is path-dependent: different processes connecting the same initial and final states generally do different amounts of work.
- Sign conventions vary by text; always establish whether W is work done BY the gas or ON the gas.

## Questions

```yaml
- question: "A gas is taken from state A (P = 2 atm, V = 1 L) to state B (P = 1 atm, V = 2 L) via two different paths. Path 1: expand isobarically at 2 atm until V = 2 L, then cool isochorically to P = 1 atm. Path 2: cool isochorically at V = 1 L to P = 1 atm, then expand isobarically at 1 atm to V = 2 L. Which statement is correct?"
  type: multiple-choice
  options:
    - "Both paths do the same work because the initial and final states are identical"
    - "Path 1 does more work than Path 2 because it expands at higher pressure"
    - "Path 2 does more work than Path 1 because it ends at lower pressure"
    - "Work cannot be determined without knowing the temperature at each state"
  answer: 1
  explanation: "Path 1 expands isobarically at 2 atm: W₁ = PΔV = 2 atm × 1 L = 2 L·atm. Path 2 expands isobarically at 1 atm: W₂ = 1 atm × 1 L = 1 L·atm. The final state is the same but the work done is different — Path 1 does twice the work of Path 2. This directly demonstrates that work is a path function: it depends on the route taken through PV space, not just the endpoints. This is the critical contrast with state functions like internal energy, which depends only on (P, V, T)."

- question: "A gas completes a clockwise cycle on a PV diagram, passing through states A → B → C → A. The area enclosed by the cycle is 400 J. What is the net work done BY the gas over the complete cycle?"
  type: multiple-choice
  options:
    - "0 J, because the gas returns to its original state and all quantities reset"
    - "+400 J, because traversing a clockwise loop means net positive work output"
    - "−400 J, because the gas compresses during part of the cycle"
    - "Cannot be determined without knowing the pressure and volume at each state"
  answer: 1
  explanation: "The net work done by the gas in a cyclic process equals the enclosed area on the PV diagram, with sign determined by traversal direction. Clockwise means the expanding (outward) path lies above the compressing (return) path — the gas expands at higher pressure than it is compressed at, so net work output is positive. The gas does return to its original state, so ΔU = 0 for the cycle, but that means Q = W, not W = 0. Counterclockwise cycles produce net negative work (work is done on the gas, as in a refrigerator)."

- question: "The work done by a gas expanding from volume V₁ to volume V₂ depends on the exact path taken through pressure-volume space, not just on V₁ and V₂."
  type: true-false
  answer: true
  explanation: "Work is W = ∫P dV. The value of this integral depends on how P varies with V along the entire path, not just on the limits of integration. An isobaric expansion at high pressure does more work than an isobaric expansion at low pressure between the same volumes. A curved path traces a different area than a straight-line path between the same endpoints. This path-dependence is what makes work a path function, in contrast to state functions like internal energy."

- question: "Because the First Law of Thermodynamics (ΔU = Q − W) relates work to internal energy, and internal energy is a state function, work is expected to also be a state function — the same work is done along any path between two states."
  type: true-false
  answer: false
  explanation: "This reasoning is flawed. The First Law says ΔU = Q − W, where ΔU is path-independent but Q and W are individually path-dependent. For two different paths between the same states, ΔU is the same — but Q and W can both be different, as long as their difference Q − W stays constant. A state function is determined by the state alone; W is not — it depends on the route. The First Law constrains the combination Q − W, not the individual values."

- question: "Why is thermodynamic work a path function rather than a state function? How does this property distinguish it from internal energy?"
  type: short-answer
  answer: "Work is W = ∫P dV — an integral over a path in PV space. The value depends on how pressure varies along the entire path, not just on the starting and ending states. Two paths connecting the same (P₁, V₁) and (P₂, V₂) trace different areas under the PV curve and therefore do different amounts of work. Internal energy U, by contrast, is determined entirely by the thermodynamic state (T, P, V) — no matter which path the system took to arrive at that state, U has the same value. The difference ΔU = Q − W is fixed between two states, but Q and W individually can vary as long as they change together."
  explanation: "Intuitively: the 'area under the curve' depends on which curve you draw, not just where it starts and ends. A tall rectangle and a flat rectangle can share start and end points (same total width) but have very different areas. Internal energy is like height above sea level — a state property — while work is like the distance traveled to get there, which depends on the route."
```

## Explainer

You already know work in mechanics: force applied over a distance. In thermodynamics, the same idea applies to gases, but the "force" is pressure and the "distance" is volume change. When a gas expands and pushes a piston outward, it exerts pressure P over an area A, moving the piston a small distance dx. Force times distance gives P·A·dx = P·dV. Summing over the entire expansion gives W = ∫P dV — the **PV work** formula. This is not a new concept; it is force-times-distance expressed in terms of fluid variables.

The **PV diagram** is the key visual tool. Plot pressure on the y-axis and volume on the x-axis, and any thermodynamic process becomes a path drawn on that plane. The work done by the gas along any path equals the area under the curve — literally the geometric area between the curve and the V-axis. An isobaric (constant-pressure) process is a horizontal line; its area is a simple rectangle, W = PΔV. A more complex process traces a curved path, and you compute the area by integration. The sign rule is intuitive: when volume increases (gas expands), work is positive — the gas pushes outward and does work on its surroundings. When volume decreases (compression), work is negative — the surroundings do work on the gas.

Here is where path-dependence becomes crucial. Your prerequisite knowledge of integrals tells you that ∫P dV depends on how P varies with V along the entire path, not just the endpoints. Two processes starting at the same state (P₁, V₁) and ending at the same state (P₂, V₂) but following different curves in between will trace different areas — and therefore do different amounts of work. This makes work a **path function**, not a state function. Internal energy is a state function (it depends only on where you are); work is not. This distinction is the conceptual heart of the First Law, which you'll encounter next.

Cyclic processes — closed loops on the PV diagram — are especially important for understanding heat engines. When the system traverses a clockwise loop, the area enclosed equals net work output: the gas does more work expanding (bottom of loop, lower pressure) than the surroundings do compressing it (top of loop, higher pressure). A counterclockwise loop means net work is done on the gas — this is a refrigerator cycle. The enclosed area, regardless of direction, is the magnitude of the net work. Memorizing the clockwise = positive convention is less important than understanding why: the expanding path has a larger area under it than the compressing return path when the loop runs clockwise.
