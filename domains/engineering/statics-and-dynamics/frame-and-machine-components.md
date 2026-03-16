---
id: frame-and-machine-components
title: Frame and Machine Component Analysis
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rigid-body-equilibrium-planar
  type: hard
- id: frames-machines-analysis
  type: soft
tags:
- frames
- machines
- multi-force members
- pins
- internal forces
stage: formal-systems
status: draft
---

# Frame and Machine Component Analysis

## Core Idea
Frames and machines consist of multi-force members (not just two-force members) connected by pins and supports, transmitting forces and moments between components. Analysis involves isolating individual members, applying equilibrium conditions to each, and solving the resulting coupled systems of equations to find all internal and external forces and moments.

## Explainer

In your earlier work on rigid-body equilibrium, you drew free-body diagrams of single objects and applied the three equilibrium equations (ΣFx = 0, ΣFy = 0, ΣM = 0). Frames and machines extend this skill to assemblies of multiple connected members. The key distinction from trusses is that truss members carry only axial force (two-force members), while frame and machine members are **multi-force members** that carry both force and moment at their connections. This means you cannot simplify them as lines of tension or compression — you must treat each member as a full rigid body.

The analysis strategy is: take the whole structure apart. For the complete assembly, draw an FBD and find external reactions at supports — this is just rigid-body equilibrium applied to the entire system, which you already know. Now comes the new step: isolate each member individually and draw its own FBD. At every pin connection between members, the two members exert equal and opposite forces on each other (Newton's third law). So if member AC pushes member BD at pin C with a force (Cx, Cy), then member BD pushes back on member AC with (-Cx, -Cy). These **internal pin forces** are unknowns you must solve for.

The system of equations grows quickly. A two-member frame produces six equilibrium equations (three per member), typically with six unknowns (two external reactions and four pin-force components). The equations are usually coupled — the unknowns appear in multiple equations — so you must solve them as a system. A common strategy is to start with the member that has more known forces or moments, write its moment equation about the pin it connects to (eliminating the pin forces at that point), and solve for one unknown at a time to avoid simultaneous solving.

**Machines** work identically but emphasize force transmission: the goal is usually to find the mechanical advantage — how an input force at the handle or crank translates into an output force at the gripper, jaw, or piston. The answer depends entirely on geometry (moment arms) and the equilibrium equations at each member. A well-designed machine amplifies force at the cost of displacement, or vice versa. Tracing forces through members with moment arms gives you the ratio.

The most common mistake is forgetting to flip the sign of internal forces when moving from one member's FBD to its neighbor's. At every shared pin, the action-reaction pair must be explicit in both FBDs with opposite signs. Missing this sign flip leads to equations that are internally inconsistent and unsolvable, or to incorrect force magnitudes that violate equilibrium somewhere in the assembly.
