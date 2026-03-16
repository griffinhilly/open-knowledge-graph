---
id: introduction-to-statics-and-dynamics
title: Introduction to Statics and Dynamics
domain: engineering
course: statics-and-dynamics
prerequisites: []
builds-toward:
- vector-analysis-and-components
- free-body-diagram-methodology
tags:
- mechanics
- statics
- dynamics
- equilibrium
- motion
stage: formal-systems
status: draft
---

# Introduction to Statics and Dynamics

## Core Idea
Statics is the study of objects in equilibrium under the action of forces and moments, with zero acceleration. Dynamics extends this to accelerated motion, examining how forces cause changes in motion through Newton's laws. Together, these form the foundation of mechanical engineering analysis, applicable to machines, structures, and systems.

## Explainer

Every object you encounter is either staying put or changing its motion. A bridge stands still; a car accelerates; a spinning turbine blade moves at constant speed. **Statics** handles the first case: objects with no acceleration, where every force and moment is perfectly balanced. **Dynamics** handles the rest: situations where forces are unbalanced and something is speeding up, slowing down, or changing direction. Both fields are applications of the same underlying physics — Newton's laws — but they ask different questions and use different solution strategies.

In statics, the governing conditions are equilibrium: the sum of all forces equals zero (ΣF = 0) and the sum of all moments about any point equals zero (ΣM = 0). These two vector equations (six scalar equations in 3D) are the complete toolkit. You use them to find unknown support reactions in a bridge, the tension in a cable holding a sign, or the internal forces in a truss. The power of statics is that you don't need to know anything about time or motion — the object isn't going anywhere, so you only need to ensure the forces balance.

Dynamics introduces time, velocity, and acceleration. Newton's second law (ΣF = ma) is the engine: unbalanced forces produce acceleration proportional to mass. Dynamics splits into two branches. **Kinematics** describes *how* things move — position, velocity, acceleration — without asking why. **Kinetics** connects forces to motion, explaining why a given force produces a given acceleration. A mechanical engineer analyzing a car's suspension must do kinematics to describe how the wheel moves up and down, then kinetics to determine what spring and damper forces are required to control that motion.

The conceptual dividing line between the two fields is worth internalizing early: if acceleration is zero (or negligible), use statics. If acceleration matters, use dynamics. Most structures — buildings, bridges, frames — are analyzed statically because they don't move appreciably. Most machines — engines, robots, vehicles — require dynamics because their parts are in motion. As you progress through this course, the tools accumulate: free-body diagrams (from statics) remain essential throughout dynamics, and equilibrium is just the special case where acceleration happens to equal zero.

