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

## Explainer

When you analyzed trusses, every member was a **two-force member** — connected at exactly two pins with no load applied between them, so the force had to act along the member's axis. That simplification made truss analysis efficient. Frames and machines break that simplification: their members have loads applied at intermediate points, or they connect to more than two other members, meaning they carry bending and shear in addition to axial load. You cannot assume the force acts along the member's axis, so the two-force shortcut is off the table.

The key operation is **disassembly at internal pins**. Rather than treating the entire assembled structure as a single free body, you separate it at each internal pin connection and draw individual free-body diagrams for each member. At each cut, you introduce internal pin force components — typically two unknowns (horizontal and vertical) per pin. This is what makes frames solvable: the equilibrium equations (ΣFx = 0, ΣFy = 0, ΣM = 0) apply independently to each isolated member, giving you three equations per member to work with.

**Newton's third law** is the thread that ties the members back together. If member A pushes on member B through a pin with force components (Ax, Ay), then member B pushes back on member A with exactly (-Ax, -Ay). This means you only introduce unknowns once — write them on the first member and flip the signs on the second. Violating this, or introducing independent variables for each side of a pin, produces a system with more unknowns than equations that cannot be solved. Before writing any equilibrium equations, always label your unknowns consistently across all FBDs.

**Machines** extend this framework to moving parts. A hydraulic jack, pliers, or a toggle clamp uses a mechanism — a chain of connected members — to trade displacement for force, or vice versa. The analysis is identical in principle: disassemble, apply Newton's third law at each pin, and solve the equilibrium equations. What changes is that you're often interested in the **mechanical advantage** — how a small input force at one point creates a large output force at another. That mechanical advantage emerges directly from the geometry: moment arms in the equilibrium equations determine the force multiplication ratio. A well-drawn FBD with dimensions is the entire solution method.
