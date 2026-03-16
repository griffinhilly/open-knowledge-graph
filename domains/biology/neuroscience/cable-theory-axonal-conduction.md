---
id: cable-theory-axonal-conduction
title: Cable Theory and Axonal Conduction
domain: biology
course: neuroscience
prerequisites:
- id: resting-membrane-potential
  type: hard
- id: neuron-structure-and-function
  type: hard
- id: partial-differential-equations
  type: soft
- id: differential-equations-intro
  type: soft
builds-toward:
- hodgkin-huxley-model
- saltatory-conduction
tags:
- cable-equation
- length-constant
- time-constant
stage: advanced
status: draft
---

# Cable Theory and Axonal Conduction

## Core Idea
Cable theory models axons as cylinders with resistive and capacitive properties. The cable equation describes voltage decay: V(x,t) = V₀ exp(−x/λ) where λ = √(rm/ri) is the length constant. This determines how far passive current spreads; τ = rm·cm determines the voltage time constant.

## How It's Best Learned
Solve the cable equation for simple geometries. Use compartmental modeling software to simulate branching dendrites.

## Common Misconceptions
Action potentials propagate passively along cables—they require active regeneration. The length constant is fixed—it depends on membrane and axial properties.
