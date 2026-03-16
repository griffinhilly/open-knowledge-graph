---
id: center-of-mass-motion
title: Center of Mass Motion
domain: physics
course: classical-mechanics
prerequisites: []
builds-toward:
- reduced-mass-problem
- angular-momentum-of-rigid-body
tags:
- center-of-mass
- dynamics
- systems
- conservation
stage: formal-systems
status: draft
---

# Center of Mass Motion

## Core Idea
The center of mass (CM) of a system moves as if all mass were concentrated there with external forces applied there: M·a_CM = F_external. Internal forces do not affect CM motion, only the motion of individual parts relative to the CM. This theorem greatly simplifies multi-body problems by separating overall motion (CM trajectory) from internal dynamics (orbits about the CM).

## Explainer

Imagine a firework exploding in the sky. After the explosion, hundreds of fragments fly outward, spinning and tumbling in all directions. The internal forces of the explosion are enormous — far larger than gravity during the brief detonation. Yet if you track the **center of mass** of all the fragments together, weighting each fragment's position by its mass, that single point traces the same smooth parabolic arc the intact firework would have followed. It ignores the explosion entirely. This is the center of mass theorem: the explosion's internal forces come in equal-and-opposite pairs that cancel out, leaving only gravity — the external force — to govern how the CM moves.

The formal statement is compact: M·**a**_CM = **F**_net,external, where M is the total mass of the system and **F**_net,external is the vector sum of all forces exerted by agents outside the system. This is Newton's second law applied to an imaginary point particle carrying the total mass at the CM location. For the firework, only gravity acts from outside: **F**_ext = M**g** downward, so **a**_CM = **g** downward — a parabola, regardless of how chaotically the fragments fly. Every internal force one fragment exerts on another has an equal-and-opposite reaction (Newton's third law), so internal forces sum to zero and vanish from the CM equation entirely.

The practical power of this theorem is **decomposition**: any multi-body problem splits cleanly into two independent pieces. First, solve the CM motion using only external forces — this is a single-particle problem. Second, analyze the motion of parts relative to the CM — this is governed by internal forces and is independent of external ones. For a binary star system with no external forces, the CM moves in a straight line at constant velocity forever; each star orbits the CM in an ellipse. The two analyses decouple completely, letting you solve each piece with the tools appropriate to it.

The CM theorem and **conservation of momentum** are the same principle from two perspectives. If net external force is zero, M·**a**_CM = 0, so **v**_CM is constant — the total momentum **p** = M**v**_CM is conserved. This is why an isolated system's CM cannot accelerate without external influence: no amount of internal rearrangement can move the CM. An astronaut floating in space cannot propel herself forward by waving her arms — her CM stays fixed. But she can throw a wrench backward, making her CM remain fixed while she and the wrench move in opposite directions to keep **p** = 0. Grasping the CM as the "translation handle" of any system, and understanding that only external forces move it, is one of the most powerful simplifying principles in all of classical mechanics.
