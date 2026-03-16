---
id: bifurcation-in-odes
title: Bifurcation in Ordinary Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: autonomous-equations
  type: hard
- id: phase-line-analysis
  type: hard
builds-toward:
- linearization-of-nonlinear-systems
tags:
- dynamics
- parameter-dependence
- qualitative
stage: advanced
status: draft
---

# Bifurcation in Ordinary Differential Equations

## Core Idea
A bifurcation occurs when the qualitative behavior of solutions to dy/dx = f(y, μ) changes as a parameter μ varies—typically when equilibria are created, destroyed, or collide. Bifurcation analysis reveals how system dynamics depend sensitively on parameters.

## Explainer

From autonomous equations and phase-line analysis, you know how to find equilibria of dy/dt = f(y) and classify them as stable or unstable by checking the sign of f'(y) at the equilibrium. You also know how to draw the phase line: a picture showing which intervals have solutions moving upward (f(y) > 0) or downward (f(y) < 0). Bifurcation theory asks what happens when the equation contains a parameter μ, so you have a family of equations dy/dt = f(y, μ), and you watch how the phase line changes as μ varies.

The simplest and most important example is the **saddle-node bifurcation**. Consider dy/dt = μ − y². When μ < 0, the equation f(y) = μ − y² = 0 has no real solutions — no equilibria, and all solutions move in one direction forever. At μ = 0, there is exactly one equilibrium at y = 0, but it is neither stable nor unstable in the usual sense (it is called a **half-stable** equilibrium). When μ > 0, two equilibria appear: y = +√μ (stable) and y = −√μ (unstable). At μ = 0, a stable and unstable equilibrium collide and annihilate each other as μ decreases — or, reading the other way, a stable-unstable pair is *born* as μ increases past 0. The value μ = 0 is the **bifurcation point**.

Other common bifurcation types include the **transcritical bifurcation**, where two equilibria exist for all μ but exchange stability as they pass through each other, and the **pitchfork bifurcation**, where one equilibrium splits into three at the bifurcation point (one losing stability while two stable ones are born). The pitchfork is common in symmetric systems — the classic example is a ball balanced on top of a curved surface, which is unstable but can tip stably to either side. The **bifurcation diagram** visualizes these changes: it plots equilibrium values y* against the parameter μ, using solid curves for stable equilibria and dashed curves for unstable ones. At a bifurcation point, the curves meet or branch.

Bifurcation analysis matters because real systems always have parameters — population models have birth and death rates, physical systems have temperature or pressure. Small changes in a parameter can cause sudden dramatic changes in long-term behavior — a population that was growing suddenly faces extinction, or a structure that was stable suddenly buckles. The bifurcation diagram tells you precisely where those critical thresholds lie and what happens at them, turning qualitative phase-line analysis from a snapshot at one parameter value into a complete map of how behavior depends on the parameter.
