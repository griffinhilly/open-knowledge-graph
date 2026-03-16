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
- phase-portraits-for-linear-systems
tags:
- qualitative
- stability
- visualization
stage: formal-systems
status: draft
---

# Phase Line Analysis for Autonomous Equations

## Core Idea
A phase line is a one-dimensional diagram showing the equilibrium solutions of dy/dx = f(y) and arrows indicating whether y increases or decreases. This visual tool predicts the long-term behavior of all solutions without solving the equation explicitly.

## How It's Best Learned
Draw the y-axis and mark all equilibrium points (zeros of f). Use the sign of f(y) between equilibria to determine flow direction with arrows. Classify equilibria as stable (sink) or unstable (source) based on arrow behavior.

## Common Misconceptions
- Thinking the phase line shows the x-direction; it only shows y-dynamics. - Confusing stable equilibria (arrows point toward) with unstable ones (arrows point away). - Forgetting that semi-stable equilibria exist where stability differs on each side.

## Explainer

An **autonomous equation** is one where the right-hand side depends only on y, not on x: dy/dx = f(y). From your study of direction fields, you know that for autonomous equations the slope depends only on the height y — every horizontal strip in the direction field has the same slope. The **phase line** compresses this entire direction field into a single vertical axis, capturing everything you need to know about long-term behavior.

To draw a phase line: first find all **equilibrium solutions**, which are the values of y where f(y) = 0. Plot these points on the y-axis. Between them, determine the sign of f(y): if f(y) > 0, then dy/dx > 0 and y is increasing, so draw an upward arrow. If f(y) < 0, then dy/dx < 0 and y is decreasing, so draw a downward arrow. The result is a complete portrait of where every solution is headed without computing a single formula.

**Stability** of an equilibrium y* is read directly from the arrows. If arrows on both sides point *toward* y*, then nearby solutions converge to it — y* is a **stable equilibrium** (or "sink"). Perturbations decay and the system returns. If arrows on both sides point *away* from y*, then nearby solutions diverge — y* is an **unstable equilibrium** (or "source"). Small perturbations grow. If arrows point toward on one side and away on the other, y* is **semi-stable** — stable from one direction, unstable from the other.

Consider dy/dx = y(1 − y), the logistic equation. Setting f(y) = 0 gives equilibria at y = 0 and y = 1. For y slightly negative, f(y) < 0 so arrows point down. For 0 < y < 1, f(y) > 0 so arrows point up. For y > 1, f(y) < 0 so arrows point down. Reading the phase line: y = 0 has arrows pointing away on both sides — unstable. y = 1 has arrows pointing toward on both sides — stable. No matter what positive initial condition you start with, the solution eventually approaches y = 1. The phase line told you this without solving the equation at all. This qualitative power — predicting long-term behavior from the sign of f alone — is what makes phase line analysis essential before the richer phase portraits of two-dimensional systems.
