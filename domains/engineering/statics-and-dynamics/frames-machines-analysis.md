---
id: frames-machines-analysis
title: Analysis of Frames and Machines
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: equilibrium-rigid-bodies
  type: hard
- id: truss-method-of-joints
  type: soft
- id: truss-method-of-sections
  type: soft
- id: statically-determinate-indeterminate
  type: soft
- id: two-force-and-three-force-members
  type: soft
builds-toward:
- dry-friction-coulombs-law
tags:
- statics
- frames
- machines
- multi-body analysis
- internal forces
stage: formal-systems
status: validated
---
# Analysis of Frames and Machines

## Core Idea
Frames are stationary structures with at least one multi-force member (carrying bending, shear, and axial loads). Machines are structures with moving parts designed to transmit or amplify forces. Unlike trusses, members cannot be assumed to carry only axial load. Analysis requires disassembling the structure at internal connections (pins), drawing individual FBDs for each member, and applying three equilibrium equations per member. Newton's third law governs internal pin forces: the force that member A exerts on member B is equal and opposite to the force B exerts on A.

## How It's Best Learned
Always disassemble at internal pins before writing equilibrium equations. Label internal pin force components consistently across members. Check your total equation count equals the total unknown count before solving.

## Common Misconceptions
- Treating frame members as two-force members when they have intermediate loads or three or more connection points.
- Neglecting Newton's third law when transferring pin force components between members.
- Attempting to analyze the assembled structure when individual members must be isolated.

## Questions

```yaml
- question: "You are drawing separate FBDs for two frame members connected by an internal pin. You label the pin force on member A as components (Cx, Cy). What force components must appear on member B at that same pin?"
  type: multiple-choice
  options:
    - "(Cx, Cy) — the same force acts on both members simultaneously"
    - "(-Cx, -Cy) — Newton's third law requires the reaction to be equal and opposite"
    - "New independent unknowns (Dx, Dy), since each member has its own FBD"
    - "Zero, because internal pin forces cancel when the whole structure is in equilibrium"
  answer: 1
  explanation: "Newton's third law is the thread connecting separated FBDs: if A pushes on B with (Cx, Cy), then B pushes back on A with (-Cx, -Cy). Introducing independent unknowns (Dx, Dy) for each side of the pin — option C — is the classic mistake. It creates more unknowns than equations, making the system unsolvable. You introduce the pin force once, then negate it on the adjacent member."

- question: "A frame member has pin connections at three points and carries a distributed load between two of them. How should it be classified and analyzed?"
  type: multiple-choice
  options:
    - "As a two-force member, since all forces must ultimately balance to maintain equilibrium"
    - "As a multi-force member — it carries bending and shear — requiring three equilibrium equations applied to its isolated FBD"
    - "By summing moments only, since axial and shear forces cancel in a symmetric member"
    - "As a truss member, provided the distributed load is replaced by equivalent point loads"
  answer: 1
  explanation: "A two-force member requires exactly two pin connections and no loads applied between them, so the force acts along the member's axis. Three connection points and an intermediate distributed load mean the member carries bending and shear — it is definitively a multi-force member. The two-force shortcut is invalid here. You must isolate it, draw a complete FBD, and apply ΣFx = 0, ΣFy = 0, ΣM = 0."

- question: "Disassembling a frame at its internal pins, rather than analyzing the entire assembled structure, is necessary because the assembled FBD alone does not provide enough equations to find all internal forces."
  type: true-false
  answer: true
  explanation: "The assembled structure gives at most 3 equilibrium equations (in 2D), which can only find the external support reactions. Internal pin forces between members are additional unknowns that only appear when you cut through the pins and draw individual member FBDs. Disassembly is what exposes those unknowns and provides the equations to solve them."

- question: "A frame member connected at exactly two pins with no load applied between them can be treated as a two-force member, regardless of whether the overall frame is statically determinate."
  type: true-false
  answer: true
  explanation: "The two-force member classification depends only on the member's own geometry and loading conditions — two pin connections, no intermediate loads — not on the overall structure's determinacy. Such a member carries only axial force along the line joining its pins. This simplification is valid whenever the member meets those conditions, and should be exploited to reduce unknowns."

- question: "Why does violating Newton's third law when transferring pin forces between member FBDs make the system unsolvable?"
  type: short-answer
  answer: "Each internal pin introduces two unknown force components. Newton's third law says those components appear with opposite signs on the two members sharing the pin — so there are only two unknowns per pin, not four. If you introduce independent unknowns on each side instead of negating, you double the unknowns without adding any equations, giving an underdetermined system with no unique solution. The law isn't just a physics requirement; it is the constraint that keeps the equation count equal to the unknown count."
  explanation: "This is why consistent FBD labeling is non-negotiable in frame analysis. Mistakes here don't produce a wrong number — they produce an unsolvable system, which is a signal to go back and check all pin force signs across every FBD before attempting to solve."
```

## Explainer

When you analyzed trusses, every member was a **two-force member** — connected at exactly two pins with no load applied between them, so the force had to act along the member's axis. That simplification made truss analysis efficient. Frames and machines break that simplification: their members have loads applied at intermediate points, or they connect to more than two other members, meaning they carry bending and shear in addition to axial load. You cannot assume the force acts along the member's axis, so the two-force shortcut is off the table.

The key operation is **disassembly at internal pins**. Rather than treating the entire assembled structure as a single free body, you separate it at each internal pin connection and draw individual free-body diagrams for each member. At each cut, you introduce internal pin force components — typically two unknowns (horizontal and vertical) per pin. This is what makes frames solvable: the equilibrium equations (ΣFx = 0, ΣFy = 0, ΣM = 0) apply independently to each isolated member, giving you three equations per member to work with.

**Newton's third law** is the thread that ties the members back together. If member A pushes on member B through a pin with force components (Ax, Ay), then member B pushes back on member A with exactly (-Ax, -Ay). This means you only introduce unknowns once — write them on the first member and flip the signs on the second. Violating this, or introducing independent variables for each side of a pin, produces a system with more unknowns than equations that cannot be solved. Before writing any equilibrium equations, always label your unknowns consistently across all FBDs.

**Machines** extend this framework to moving parts. A hydraulic jack, pliers, or a toggle clamp uses a mechanism — a chain of connected members — to trade displacement for force, or vice versa. The analysis is identical in principle: disassemble, apply Newton's third law at each pin, and solve the equilibrium equations. What changes is that you're often interested in the **mechanical advantage** — how a small input force at one point creates a large output force at another. That mechanical advantage emerges directly from the geometry: moment arms in the equilibrium equations determine the force multiplication ratio. A well-drawn FBD with dimensions is the entire solution method.
