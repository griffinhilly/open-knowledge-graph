---
id: kinematic-equations
title: Kinematic Equations for Constant Acceleration
domain: physics
course: classical-mechanics
prerequisites:
- id: kinematics-1d
  type: hard
- id: quadratic-formula
  type: soft
builds-toward:
- kinematics-2d
- projectile-motion
- free-fall
tags:
- kinematics
- constant-acceleration
- equations-of-motion
stage: formal-systems
status: validated
---

# Kinematic Equations for Constant Acceleration

## Core Idea
When acceleration is constant, four equations relate position, velocity, acceleration, and time: v = v₀ + at; x = x₀ + v₀t + ½at²; v² = v₀² + 2a(x − x₀); x = x₀ + ½(v₀ + v)t. These are derived by integrating constant acceleration and are valid only when acceleration does not change. They reduce complex motion problems to algebra.

## How It's Best Learned
Categorize each problem by what is known and unknown, then select the equation that relates those four variables. Practice free-fall problems (a = −9.8 m/s²) extensively since they build physical intuition for magnitudes of real quantities.

## Common Misconceptions
- Applying these equations when acceleration is not constant — they break down entirely for variable acceleration.
- Sign errors when choosing a coordinate system: consistently define positive direction at the start of each problem.
- Confusing x for displacement vs. position when using x = v₀t + ½at².

## Explainer

From your study of 1D kinematics, you know the basic concepts: **position** (where something is), **velocity** (how fast position changes), and **acceleration** (how fast velocity changes). The kinematic equations for constant acceleration are what you get when you work out, algebraically, exactly what happens to position and velocity when acceleration is held constant throughout the motion.

The derivation builds directly from the definition of constant acceleration. If acceleration is constant at value *a*, and velocity starts at *v₀*, then after time *t*, velocity is *v = v₀ + at* — velocity increases linearly with time. Now integrate: if velocity changes linearly from *v₀* to *v* over time *t*, then the average velocity is ½(v₀ + v), and displacement is average velocity times time: *x = x₀ + ½(v₀ + v)t*. Substituting *v = v₀ + at* into this gives *x = x₀ + v₀t + ½at²*. Finally, eliminating *t* between the first two equations gives *v² = v₀² + 2a(x − x₀)*. These four equations are not independent facts to memorize — they are four algebraic faces of the same underlying physical situation.

The practical skill is matching equations to problems. Each equation involves four of the five kinematic quantities: position (x₀ and x), initial velocity (v₀), final velocity (v), acceleration (a), and time (t). A typical problem gives you three known quantities and asks for a fourth. The equation you want is the one that contains exactly those four variables — the three you know plus the one you want — allowing you to solve algebraically. For example, if you know initial velocity, final velocity, and acceleration but not time, the equation *v² = v₀² + 2a·Δx* is your tool because it contains no *t* at all.

The most important discipline is **sign convention**. Pick a positive direction before you start the problem and stick to it consistently. If up is positive and you drop something, acceleration is −9.8 m/s². If an object moves in the negative direction, its velocity is negative. The equations are algebraically neutral about sign — they don't care which direction is positive — but you must be internally consistent throughout a problem. Many errors come not from misapplying the equations but from inconsistent sign choices partway through. The other critical discipline is recognizing when these equations do *not* apply: they are valid only when acceleration is constant throughout the entire interval. A car that accelerates from rest and then brakes to a stop cannot be treated as a single constant-acceleration problem — you must split it into phases, each with its own constant acceleration, and chain the equations across the boundary.
