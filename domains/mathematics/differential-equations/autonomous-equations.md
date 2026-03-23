---
id: autonomous-equations
title: Autonomous Equations and Equilibrium Solutions
domain: mathematics
course: differential-equations
prerequisites:
- id: separable-differential-equations
  type: hard
builds-toward:
- phase-line-analysis
- bifurcation-in-odes
- stability-classification
tags:
- first-order
- qualitative
- equilibrium
stage: formal-systems
status: validated
---

# Autonomous Equations and Equilibrium Solutions

## Core Idea
An autonomous ODE has the form dy/dx = f(y), depending only on y, not on x. Equilibrium solutions occur where f(y) = 0. Autonomous equations are time-independent, making them ideal for studying long-term behavior and stability without explicitly solving.

## Questions

```yaml
- question: "For the autonomous equation dy/dt = y(1 − y), which of the equilibrium solutions is stable?"
  type: multiple-choice
  options:
    - "y = 0 is stable — it is the trivial solution and autonomous systems return to zero"
    - "y = 1 is stable — solutions above it are pushed down and solutions below it are pushed up"
    - "Both y = 0 and y = 1 are stable — all equilibria of autonomous equations are stable"
    - "Neither is stable — stability cannot be determined without solving the ODE"
  answer: 1
  explanation: "Evaluate f(y) = y(1−y) on either side of each equilibrium. Near y = 1: for y slightly below 1 (say y = 0.9), f(0.9) = 0.9(0.1) > 0, so solutions increase toward y = 1. For y slightly above 1 (say y = 1.1), f(1.1) = 1.1(−0.1) < 0, so solutions decrease toward y = 1. Both sides push toward y = 1 — it is stable. Near y = 0: for y slightly below 0, f(y) < 0 (solutions move away); for y slightly above 0, f(y) > 0 (solutions move away). Both sides push away from y = 0 — it is unstable."

- question: "For dy/dt = f(y), suppose f(y) > 0 for 0 < y < 2 and f(y) < 0 for y > 2, with f(2) = 0. What can you conclude?"
  type: multiple-choice
  options:
    - "y = 2 is an unstable equilibrium — the sign of f(y) changes there"
    - "y = 2 is a stable equilibrium — solutions below it increase toward it and solutions above it decrease toward it"
    - "y = 2 is a semi-stable equilibrium — it attracts from above but repels from below"
    - "Nothing can be concluded without solving the ODE explicitly"
  answer: 1
  explanation: "The phase-line analysis is direct: f(y) > 0 below y = 2 means solutions there are increasing (arrows point up, toward y = 2). f(y) < 0 above y = 2 means solutions there are decreasing (arrows point down, toward y = 2). Both sides funnel toward y = 2 — it is a stable equilibrium (a sink/attractor). This determination required no integration, only evaluating the sign of f(y) on either side of the equilibrium."

- question: "An equilibrium solution y = c of an autonomous ODE is always stable."
  type: true-false
  answer: false
  explanation: "False. Equilibria can be stable (attractors/sinks), unstable (repellers/sources), or semi-stable. For dy/dt = y(1−y), y = 1 is stable but y = 0 is unstable — solutions near y = 0 move away from it. Stability depends on the sign of f(y) on either side of the equilibrium: if f changes from positive to negative through the equilibrium, it is stable; if from negative to positive, unstable. Nothing about being an equilibrium (f(c) = 0) guarantees attraction."

- question: "The long-run behavior of any solution to an autonomous ODE dy/dt = f(y) can be determined from the phase line without explicitly solving the equation."
  type: true-false
  answer: true
  explanation: "True. The phase line encodes the sign of f(y) on each interval between equilibria and at each equilibrium. This is sufficient to determine where every solution goes as t → ∞: solutions follow the arrows on the phase line — moving in the direction f(y) points — until they reach a stable equilibrium or diverge to ±∞. No integration is required because the qualitative structure (which equilibria exist and which are stable) completely determines long-run behavior from any initial condition."

- question: "Why does an autonomous equation dy/dx = f(y) — where only y appears on the right, not x — make it especially amenable to qualitative (phase-line) analysis?"
  type: short-answer
  answer: "Because the rate of change depends only on the current value of y, the behavior is the same regardless of when or where you start. The phase line captures all possible behaviors: at each value of y, f(y) tells you whether solutions increase or decrease, and equilibria (where f(y) = 0) are fixed points that cannot be crossed. Since f(y) is fixed across all x, the arrows on the phase line never change — you can trace every solution's long-run fate without solving the equation."
  explanation: "In contrast, a non-autonomous equation dy/dx = g(x, y) has a rate of change that varies with x, so the same y-value produces different behavior depending on where you are in x. A phase line would need to change as x changes, making qualitative analysis far harder. Autonomy removes this complication: the system's 'rules' are the same at every x, making the phase line a complete and time-independent map of all solution behaviors."
```

## Explainer

From separable equations, you know how to solve dy/dx = g(x)h(y) by separating and integrating. An **autonomous equation** is the special case where there is no x on the right-hand side at all: dy/dx = f(y). The rate of change depends only on the current value of y, not on when or where you are. A population growing at a rate proportional to its size, dy/dt = ky, is autonomous. So is the logistic equation dy/dt = ry(1 − y/K). The defining feature is that the behavior of the system is fully determined by where y currently is, not by the value of t.

**Equilibrium solutions** (also called **steady states** or **fixed points**) are constant solutions y(x) = c where f(c) = 0. At these values, the rate of change is zero, so if the system ever reaches an equilibrium, it stays there. To find them, just solve the algebraic equation f(y) = 0. For dy/dt = y(1 − y), the equilibria are y = 0 and y = 1.

The more important question than "what are the equilibria?" is "are they stable?" A **stable equilibrium** (also called a **sink** or attractor) pulls nearby solutions toward it. An **unstable equilibrium** (also called a **source** or repeller) pushes nearby solutions away. You can determine stability without solving the ODE: if f(y) > 0 just below the equilibrium and f(y) < 0 just above it, then solutions are pushed upward from below and downward from above — toward the equilibrium — making it stable. The opposite sign pattern means unstable.

This analysis is the basis for the **phase line**: a number line displaying the equilibria as points, with arrows indicating the sign of f(y) between them. A solution starting anywhere on the phase line follows the arrows in the direction they indicate. The phase line gives you the complete qualitative picture of every solution's long-run behavior without integrating a single equation. This geometric approach to ODEs — understanding the shape of solutions from f(y) alone — is one of the most powerful ideas in the subject, and it extends to higher-dimensional systems in your upcoming work on phase planes and stability classification.
