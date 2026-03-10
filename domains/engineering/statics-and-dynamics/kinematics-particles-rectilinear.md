---
id: kinematics-particles-rectilinear
title: Rectilinear Kinematics of Particles
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-1d
  type: hard
- id: kinematic-equations
  type: hard
- id: differential-equations-intro-separable
  type: soft
builds-toward:
- kinematics-particles-curvilinear
- dynamics-newtons-second-law
tags:
- dynamics
- kinematics
- rectilinear motion
- particles
- integration
stage: formal-systems
status: draft
---

# Rectilinear Kinematics of Particles

## Core Idea
Rectilinear kinematics describes particle motion along a straight line through position x(t), velocity v = dx/dt, and acceleration a = dv/dt. Three analysis cases arise: (1) constant acceleration — use the kinematic equations directly; (2) acceleration as a function of time, a(t) — integrate with respect to time; (3) acceleration as a function of position, a(x) — apply the chain rule identity a = v dv/dx to formulate a separable ODE. Selecting the correct method depends on how acceleration is specified.

## How It's Best Learned
Identify which case applies before choosing a solution method. Practice recognizing when to integrate a(t) and when to use a = v dv/dx. Always apply initial conditions after integrating.

## Common Misconceptions
- Using constant-acceleration kinematic equations when acceleration varies with time or position.
- Confusing total distance traveled (always positive, path length) with displacement (signed, net change in position).
- Forgetting initial conditions when integrating to find velocity or position.
