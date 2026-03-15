---
id: boltzmann-equation-kinetic
title: Boltzmann Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: kinetic-theory-basics
  type: hard
- id: boltzmann-transport-equation
  type: soft
- id: differential-equations-intro
  type: hard
builds-toward:
- chapman-enskog-expansion
tags:
- kinetic-theory
- transport
- non-equilibrium
stage: advanced
status: draft
---

# Boltzmann Equation

## Core Idea
The Boltzmann equation describes the evolution of single-particle distribution f(r,p,t) in phase space, accounting for both free streaming and collisions: ∂f/∂t + (p/m)·∇_r f + F·∇_p f = (∂f/∂t)_collision. Its solutions yield transport properties and show how systems relax toward equilibrium through irreversible processes.
