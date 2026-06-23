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
- id: acceleration-and-velocity
  type: hard
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

## Questions

```yaml
- question: "A ball is thrown upward at 20 m/s. Using a = −9.8 m/s², which kinematic equation most directly gives the maximum height (without first solving for time)?"
  type: multiple-choice
  options:
    - "v = v₀ + at (this equation has no displacement term)"
    - "x = x₀ + v₀t + ½at² (this requires knowing time first)"
    - "v² = v₀² + 2aΔx (relates v, v₀, a, and displacement without needing time)"
    - "x = x₀ + ½(v₀ + v)t (this requires knowing both final velocity and time)"
  answer: 2
  explanation: "At maximum height, v = 0. The equation v² = v₀² + 2aΔx contains exactly the quantities we know (v₀ = 20, v = 0, a = −9.8) and the one we want (Δx), with time absent entirely. Solving: 0 = 400 + 2(−9.8)Δx → Δx ≈ 20.4 m. This equation-selection strategy — identify what you know, what you want, and which equation contains exactly those — is the core practical skill."

- question: "A car accelerates from rest to 30 m/s, then brakes to a stop. Why can't you find the total distance with a single kinematic equation?"
  type: multiple-choice
  options:
    - "Kinematic equations only apply when the initial velocity is zero"
    - "The acceleration is not constant throughout — braking has a different acceleration than the initial accelerating phase"
    - "The final velocity is zero, making the equations undefined"
    - "Kinematic equations require the direction of motion to remain the same"
  answer: 1
  explanation: "Kinematic equations are valid ONLY when acceleration is constant throughout the entire interval. A car that first accelerates then brakes has two distinct constant-acceleration phases (with different values of a). You must solve each phase separately and chain the results: the final position and velocity of phase 1 become the initial conditions for phase 2. Applying one equation across both phases would assume a single constant acceleration that doesn't exist."

- question: "The four kinematic equations are independent physical laws that is expected to each be memorized separately, because they describe different aspects of motion."
  type: true-false
  answer: false
  explanation: "The four equations are four algebraic rearrangements of the same underlying situation — constant acceleration — all derivable by integrating a = constant. Starting with v = v₀ + at and using average velocity × time gives x = x₀ + v₀t + ½at². Eliminating t between these two gives v² = v₀² + 2aΔx. The fourth combines average velocity with time. They are the same physics expressed in forms that make different quantities easy to isolate."

- question: "In a kinematic problem where 'upward' is defined as the positive direction, an object in free fall should be assigned a negative value for acceleration."
  type: true-false
  answer: true
  explanation: "Sign convention is not a physical fact — it is a bookkeeping choice. Once you define upward as positive, gravity points downward, so a = −9.8 m/s². The kinematic equations are algebraically neutral about direction; they produce correct results as long as signs are applied consistently throughout the problem. Many errors arise not from wrong equations but from inconsistent sign choices — switching the positive direction midway through a problem."

- question: "Why is it important to select the right kinematic equation before solving, rather than using whichever one comes to mind first?"
  type: short-answer
  answer: "Each kinematic equation involves four of the five kinematic quantities (x₀, x, v₀, v, a, t). A given problem specifies three knowns and one unknown. The correct equation is the one that contains exactly those three knowns plus the unknown — with the fifth quantity absent, so you can solve in one step. Choosing the wrong equation forces you to first solve for an unneeded intermediate quantity, adding steps and opportunities for error. Equation selection is the primary strategy, not algebra."
  explanation: "For example, if you know v₀, a, and Δx but not t, the equation v² = v₀² + 2aΔx is the tool — it omits t entirely. Using v = v₀ + at instead requires first solving for t using another equation, doubling the work. Identifying what's known and unknown before touching algebra is the hallmark of efficient problem-solving in kinematics."
```

## Explainer

From your study of 1D kinematics, you know the basic concepts: **position** (where something is), **velocity** (how fast position changes), and **acceleration** (how fast velocity changes). The kinematic equations for constant acceleration are what you get when you work out, algebraically, exactly what happens to position and velocity when acceleration is held constant throughout the motion.

The derivation builds directly from the definition of constant acceleration. If acceleration is constant at value *a*, and velocity starts at *v₀*, then after time *t*, velocity is *v = v₀ + at* — velocity increases linearly with time. Now integrate: if velocity changes linearly from *v₀* to *v* over time *t*, then the average velocity is ½(v₀ + v), and displacement is average velocity times time: *x = x₀ + ½(v₀ + v)t*. Substituting *v = v₀ + at* into this gives *x = x₀ + v₀t + ½at²*. Finally, eliminating *t* between the first two equations gives *v² = v₀² + 2a(x − x₀)*. These four equations are not independent facts to memorize — they are four algebraic faces of the same underlying physical situation.

The practical skill is matching equations to problems. Each equation involves four of the five kinematic quantities: position (x₀ and x), initial velocity (v₀), final velocity (v), acceleration (a), and time (t). A typical problem gives you three known quantities and asks for a fourth. The equation you want is the one that contains exactly those four variables — the three you know plus the one you want — allowing you to solve algebraically. For example, if you know initial velocity, final velocity, and acceleration but not time, the equation *v² = v₀² + 2a·Δx* is your tool because it contains no *t* at all.

The most important discipline is **sign convention**. Pick a positive direction before you start the problem and stick to it consistently. If up is positive and you drop something, acceleration is −9.8 m/s². If an object moves in the negative direction, its velocity is negative. The equations are algebraically neutral about sign — they don't care which direction is positive — but you must be internally consistent throughout a problem. Many errors come not from misapplying the equations but from inconsistent sign choices partway through. The other critical discipline is recognizing when these equations do *not* apply: they are valid only when acceleration is constant throughout the entire interval. A car that accelerates from rest and then brakes to a stop cannot be treated as a single constant-acceleration problem — you must split it into phases, each with its own constant acceleration, and chain the equations across the boundary.
