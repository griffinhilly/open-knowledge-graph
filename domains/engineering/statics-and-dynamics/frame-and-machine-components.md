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

## Questions

```yaml
- question: "What fundamentally distinguishes a multi-force member (in a frame) from a two-force member (in a truss)?"
  type: multiple-choice
  options:
    - "Multi-force members are always longer and carry more load than two-force members"
    - "Two-force members are straight; multi-force members can be curved or angled"
    - "Two-force members carry only axial force along their length; multi-force members also carry forces not along their axis, generating moments at connections"
    - "Multi-force members must be made of steel; two-force members can be made of any material"
  answer: 2
  explanation: "The defining distinction is mechanical, not geometric. A two-force member has forces applied at exactly two points and both forces must be equal, opposite, and collinear — so only axial tension or compression is transmitted. A multi-force member has forces or moments applied at three or more points, or has distributed loads, meaning the forces at connections can be in any direction and generate bending moments. This is why truss analysis is simpler (method of joints uses only force equations) while frame analysis requires treating each member as a full rigid body with its own moment equation."

- question: "You isolate member AB in a frame and find that at pin C (shared with member CD), member CD exerts a force of (6, −4) N on member AB. What force does member AB exert on member CD at pin C?"
  type: multiple-choice
  options:
    - "(6, −4) N — the same force, because both members must carry the same load at the pin"
    - "(−6, 4) N — equal in magnitude but opposite in direction, by Newton's third law"
    - "(0, 0) N — internal forces cancel each other out at the pin"
    - "Cannot be determined without knowing the external loads on the full structure"
  answer: 1
  explanation: "Newton's third law applies directly at every pin connection: if member CD exerts force (6, −4) N on member AB, then member AB exerts the equal and opposite force (−6, 4) N on member CD. This is not optional — it is a fundamental law. When drawing the FBD of each member, you must explicitly show these action-reaction pairs with opposite signs. Forgetting to flip the sign is the single most common error in frame analysis and produces equations that are internally inconsistent or give wrong force values."

- question: "To analyze a frame, it is sufficient to draw a free-body diagram of the entire structure and apply equilibrium equations — you do not need to isolate individual members."
  type: true-false
  answer: false
  explanation: "The whole-structure FBD is only the first step, and it can only find the external support reactions. The internal pin forces between members — the forces members exert on each other at connections — are invisible in a whole-structure FBD because they are internal to the system and cancel out. To find these internal forces, you must disassemble the structure and draw a separate FBD for each member. This is the essential and new step in frame analysis that goes beyond single-body equilibrium."

- question: "In a machine, the mechanical advantage (ratio of output force to input force) depends entirely on the geometry of the members — specifically the moment arms — not on the material or cross-sectional area of the members."
  type: true-false
  answer: true
  explanation: "Mechanical advantage is a purely geometric quantity determined by moment arm ratios. By applying moment equilibrium to each member, the input force times its moment arm equals the output force times its moment arm. A machine that amplifies force by a factor of 5 does so because the input moment arm is 5 times longer than the output moment arm — regardless of whether the parts are steel or aluminum, thick or thin. Material properties affect whether the machine will fail under load, but they do not change the mechanical advantage of a working machine."

- question: "Why must the internal pin force between two connected frame members be shown with opposite signs in the FBD of each member? What physical law requires this?"
  type: short-answer
  answer: "Newton's third law requires that for every force exerted by body A on body B, body B exerts an equal and opposite force on body A. At a shared pin, member A pushes member B with some force (Cx, Cy); therefore member B pushes back on member A with (−Cx, −Cy). Each member's FBD must show the force that the other member exerts on it — these forces are opposite in sign because they are an action-reaction pair. If both FBDs showed the same force in the same direction, you would be violating Newton's third law and the resulting equilibrium equations would be inconsistent."
  explanation: "This sign discipline is the core bookkeeping challenge of frame analysis. The pin force components (Cx, Cy) are unknowns you are solving for. Once you solve for them in one member's equations, the values plug into the other member's equations with flipped signs. Getting this right ensures the system of equations is consistent and the solution satisfies equilibrium everywhere in the structure."
```

## Explainer

In your earlier work on rigid-body equilibrium, you drew free-body diagrams of single objects and applied the three equilibrium equations (ΣFx = 0, ΣFy = 0, ΣM = 0). Frames and machines extend this skill to assemblies of multiple connected members. The key distinction from trusses is that truss members carry only axial force (two-force members), while frame and machine members are **multi-force members** that carry both force and moment at their connections. This means you cannot simplify them as lines of tension or compression — you must treat each member as a full rigid body.

The analysis strategy is: take the whole structure apart. For the complete assembly, draw an FBD and find external reactions at supports — this is just rigid-body equilibrium applied to the entire system, which you already know. Now comes the new step: isolate each member individually and draw its own FBD. At every pin connection between members, the two members exert equal and opposite forces on each other (Newton's third law). So if member AC pushes member BD at pin C with a force (Cx, Cy), then member BD pushes back on member AC with (-Cx, -Cy). These **internal pin forces** are unknowns you must solve for.

The system of equations grows quickly. A two-member frame produces six equilibrium equations (three per member), typically with six unknowns (two external reactions and four pin-force components). The equations are usually coupled — the unknowns appear in multiple equations — so you must solve them as a system. A common strategy is to start with the member that has more known forces or moments, write its moment equation about the pin it connects to (eliminating the pin forces at that point), and solve for one unknown at a time to avoid simultaneous solving.

**Machines** work identically but emphasize force transmission: the goal is usually to find the mechanical advantage — how an input force at the handle or crank translates into an output force at the gripper, jaw, or piston. The answer depends entirely on geometry (moment arms) and the equilibrium equations at each member. A well-designed machine amplifies force at the cost of displacement, or vice versa. Tracing forces through members with moment arms gives you the ratio.

The most common mistake is forgetting to flip the sign of internal forces when moving from one member's FBD to its neighbor's. At every shared pin, the action-reaction pair must be explicit in both FBDs with opposite signs. Missing this sign flip leads to equations that are internally inconsistent and unsolvable, or to incorrect force magnitudes that violate equilibrium somewhere in the assembly.
