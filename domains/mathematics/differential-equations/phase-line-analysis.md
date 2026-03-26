---
id: phase-line-analysis
title: Phase Line Analysis for Autonomous Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: autonomous-equations
  type: hard
- id: direction-fields-and-solution-curves
  type: soft
builds-toward:
- bifurcation-in-odes
- stability-classification
- phase-portraits-linear-systems
tags:
- qualitative
- stability
- visualization
stage: formal-systems
status: validated
---

# Phase Line Analysis for Autonomous Equations

## Core Idea
A phase line is a one-dimensional diagram showing the equilibrium solutions of dy/dx = f(y) and arrows indicating whether y increases or decreases. This visual tool predicts the long-term behavior of all solutions without solving the equation explicitly.

## How It's Best Learned
Draw the y-axis and mark all equilibrium points (zeros of f). Use the sign of f(y) between equilibria to determine flow direction with arrows. Classify equilibria as stable (sink) or unstable (source) based on arrow behavior.

## Common Misconceptions
- Thinking the phase line shows the x-direction; it only shows y-dynamics. - Confusing stable equilibria (arrows point toward) with unstable ones (arrows point away). - Forgetting that semi-stable equilibria exist where stability differs on each side.

## Questions

```yaml
- question: "For the autonomous equation dy/dx = y(2 − y), what is the stability classification of the equilibrium y = 2?"
  type: multiple-choice
  options:
    - "Unstable, because y = 2 is the larger equilibrium value"
    - "Stable, because arrows on both sides of y = 2 point toward it"
    - "Semi-stable, because the sign of f(y) is different on each side"
    - "Unstable, because f(y) > 0 just below y = 2"
  answer: 1
  explanation: "Check the sign of f(y) = y(2−y) on each side of y = 2. For y slightly less than 2 (e.g., y = 1.9): f(1.9) = 1.9(0.1) > 0, so dy/dx > 0, meaning y increases toward 2. For y slightly greater than 2 (e.g., y = 2.1): f(2.1) = 2.1(−0.1) < 0, so dy/dx < 0, meaning y decreases toward 2. Arrows point toward y = 2 from both sides — stable (sink). Option D is correct about f(y) > 0 just below but draws the wrong conclusion: arrows pointing upward toward y = 2 is exactly what makes it stable."

- question: "A phase line for dy/dx = f(y) shows an equilibrium y* where the arrow below y* points upward and the arrow above y* also points upward. What is the stability classification of y*?"
  type: multiple-choice
  options:
    - "Stable, because solutions below y* approach it"
    - "Unstable, because solutions above y* move away from it"
    - "Semi-stable — stable from below (solutions approach) but unstable from above (solutions move away)"
    - "Unstable — arrows pointing upward mean all solutions increase without bound"
  answer: 2
  explanation: "Semi-stability occurs when arrows point toward the equilibrium on one side and away on the other. Here, the arrow below y* points up (toward y*) — solutions below approach it. The arrow above y* also points up (away from y*) — solutions above move further away. This asymmetric behavior is semi-stability. It differs from full stability (arrows toward on both sides) and full instability (arrows away on both sides)."

- question: "Phase line analysis can determine the long-term behavior of all solutions to an autonomous ODE without ever solving the equation explicitly."
  type: true-false
  answer: true
  explanation: "This is the essential power of the phase line. By finding only the zeros of f(y) (equilibria) and determining the sign of f(y) between them (direction of change), you can classify every equilibrium as stable, unstable, or semi-stable, and predict that any solution starting in a given interval will converge to or diverge from the nearby equilibria. The logistic equation example in the Explainer shows this: without solving dy/dx = y(1−y), the phase line tells you all positive initial conditions lead to y = 1."

- question: "On a phase line for dy/dx = f(y), an upward arrow in a region means that x is increasing in that region."
  type: true-false
  answer: false
  explanation: "The phase line shows the dynamics of y, not x. An upward arrow means dy/dx > 0 — y is increasing as x increases. The horizontal axis in the full direction field (x) never appears on the phase line itself; the phase line collapses the direction field to a single axis representing y values only. Confusing the direction of y-change with x-change is a common error when first interpreting phase lines."

- question: "Explain why finding the zeros of f(y) is the first step in phase line analysis, and what these zeros represent about the solutions to dy/dx = f(y)."
  type: short-answer
  answer: "The zeros of f(y) are the values of y where dy/dx = 0, meaning the solution neither increases nor decreases. These are equilibrium solutions — constant functions y(x) = y* that satisfy the ODE for all x. They divide the y-axis into intervals within which f(y) maintains a constant sign (either positive or negative). This sign determines whether y increases or decreases in each interval. The equilibria are therefore both the solutions themselves and the boundaries that separate all other solutions into regions with predictable long-term behavior — flowing toward a stable equilibrium or away from an unstable one."
  explanation: "The phase line technique derives its power from the intermediate value theorem and sign analysis: f is continuous, so it can only change sign by passing through zero. The zeros partition the real line into intervals of constant sign. Within each interval, solutions are monotone (all increasing or all decreasing). This means stability classification is complete once you locate the zeros and check signs — a task far simpler than solving the ODE."
```

## Explainer

An **autonomous equation** is one where the right-hand side depends only on y, not on x: dy/dx = f(y). From your study of direction fields, you know that for autonomous equations the slope depends only on the height y — every horizontal strip in the direction field has the same slope. The **phase line** compresses this entire direction field into a single vertical axis, capturing everything you need to know about long-term behavior.

To draw a phase line: first find all **equilibrium solutions**, which are the values of y where f(y) = 0. Plot these points on the y-axis. Between them, determine the sign of f(y): if f(y) > 0, then dy/dx > 0 and y is increasing, so draw an upward arrow. If f(y) < 0, then dy/dx < 0 and y is decreasing, so draw a downward arrow. The result is a complete portrait of where every solution is headed without computing a single formula.

**Stability** of an equilibrium y* is read directly from the arrows. If arrows on both sides point *toward* y*, then nearby solutions converge to it — y* is a **stable equilibrium** (or "sink"). Perturbations decay and the system returns. If arrows on both sides point *away* from y*, then nearby solutions diverge — y* is an **unstable equilibrium** (or "source"). Small perturbations grow. If arrows point toward on one side and away on the other, y* is **semi-stable** — stable from one direction, unstable from the other.

Consider dy/dx = y(1 − y), the logistic equation. Setting f(y) = 0 gives equilibria at y = 0 and y = 1. For y slightly negative, f(y) < 0 so arrows point down. For 0 < y < 1, f(y) > 0 so arrows point up. For y > 1, f(y) < 0 so arrows point down. Reading the phase line: y = 0 has arrows pointing away on both sides — unstable. y = 1 has arrows pointing toward on both sides — stable. No matter what positive initial condition you start with, the solution eventually approaches y = 1. The phase line told you this without solving the equation at all. This qualitative power — predicting long-term behavior from the sign of f alone — is what makes phase line analysis essential before the richer phase portraits of two-dimensional systems.
