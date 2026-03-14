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
