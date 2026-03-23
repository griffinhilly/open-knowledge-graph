---
id: autonomous-equations-phase-lines
title: Autonomous Equations and Phase Lines
domain: mathematics
course: differential-equations
prerequisites:
- id: existence-uniqueness-ode
  type: hard
- id: first-derivative-test
  type: hard
builds-toward:
- bifurcation-analysis-ode
- stability-classification
tags:
- autonomous
- phase-line
- qualitative-analysis
stage: formal-systems
status: validated
---

# Autonomous Equations and Phase Lines

## Core Idea
An autonomous ODE dy/dx = f(y) has no explicit x-dependence. Solutions can be analyzed qualitatively using a phase line: equilibria (where f(y) = 0) divide the line into regions where solutions flow toward stable equilibria (sinks) or away from unstable ones (sources). This geometric approach provides deep understanding without solving the equation explicitly.

## Questions

```yaml
- question: "For dy/dt = y(1−y), the equilibria are at y=0 and y=1. Without solving the ODE, how do you determine whether y=0 is a sink or a source?"
  type: multiple-choice
  options:
    - "Solve the ODE explicitly and examine where y(t) goes as t → ∞ for initial conditions near 0"
    - "Check the sign of f(y) on both sides of y=0: f(0.1) > 0 means solutions flow away from 0, and f(−0.1) < 0 also flows away — so y=0 is a source"
    - "Differentiate f(y) and check the sign of f′(0): if positive, it is a source; if negative, a sink"
    - "Stability cannot be determined without knowing the specific initial condition"
  answer: 1
  explanation: "The phase-line method checks the sign of f(y) in the intervals adjacent to the equilibrium. For y slightly above 0: f(0.1) = 0.1(0.9) > 0, so dy/dt > 0 and solutions flow upward — away from 0. For y slightly below 0: f(−0.1) = (−0.1)(1.1) < 0, so dy/dt < 0 and solutions flow downward — also away from 0. Arrows point away from both sides, confirming y=0 is a source. No explicit solution is needed; sign analysis on f(y) is sufficient and is the core technique."

- question: "Which feature of autonomous ODEs makes phase-line analysis valid — that is, why does the sign of f(y) between consecutive equilibria give a complete picture of solution behavior?"
  type: multiple-choice
  options:
    - "Autonomous equations always have explicit closed-form solutions, so the phase line is just a shortcut"
    - "Between consecutive equilibria, f(y) has constant sign, so dy/dt has a definite direction throughout the entire interval — all solutions in that interval flow the same way"
    - "All autonomous equations have exactly two equilibria, making the analysis simple"
    - "The equation is linear, so superposition guarantees the sign pattern is uniform"
  answer: 1
  explanation: "f(y) is continuous and has no zeros between consecutive equilibria (since equilibria are exactly where f = 0). A continuous nonzero function on an interval has constant sign throughout, so dy/dt is uniformly positive or negative in each interval. This means every solution starting in a given interval flows in the same direction — the arrow on the phase line captures the behavior of all initial conditions in that region. No linearity or explicit formula is required."

- question: "A phase-line analysis of dy/dt = f(y) requires solving the differential equation explicitly before you can classify equilibria as stable or unstable."
  type: true-false
  answer: false
  explanation: "The phase line requires only the sign of f(y) between equilibria, not the explicit solution. By checking whether f(y) > 0 or f(y) < 0 on either side of an equilibrium y*, you determine whether arrows point toward it (sink/stable) or away from it (source/unstable). This is the entire point of the qualitative approach: it provides a complete picture of long-run behavior without the often-impossible task of finding a closed-form formula for y(t)."

- question: "Two solutions of the same autonomous ODE dy/dt = f(y) that start at different initial conditions can never cross each other on the ty-plane."
  type: true-false
  answer: true
  explanation: "This follows directly from the existence-uniqueness theorem. If two solutions passed through the same point (t₀, y₀), they would both be solutions to the same initial value problem — but uniqueness guarantees there is only one such solution. Therefore, distinct solution curves cannot intersect. This property is what makes the phase-line picture logically consistent: the arrows never create contradictions, and each initial value leads to exactly one trajectory with a well-defined long-run fate."

- question: "Explain what information the phase line encodes and why it constitutes a 'complete' qualitative picture of solution behavior for an autonomous ODE — without requiring an explicit formula."
  type: short-answer
  answer: "The phase line marks equilibria (where f(y) = 0) on a vertical axis and draws arrows indicating the direction of flow (up where f > 0, down where f < 0) in each interval between equilibria. This tells you: where the system is stationary (equilibria), whether each equilibrium attracts or repels nearby solutions (sink vs. source), and which equilibrium any given initial condition will approach as t → ∞. Because solutions cannot cross (existence-uniqueness), the initial condition's interval completely determines its long-run fate."
  explanation: "The qualitative completeness is the deep point: you don't need y(t) to know where solutions go. The sign pattern of f(y) fully determines the topology of the solution space. This is the power of the autonomous structure — the absence of explicit t-dependence means the vector field is static, and its geometry completely governs behavior. Phase-line analysis is the first example of a broader technique (phase plane, phase portrait) used throughout dynamical systems."
```

## Explainer

An **autonomous ODE** is a differential equation of the form dy/dt = f(y) where the right-hand side depends only on y, not on t. The absence of explicit time dependence is the key feature: the rate of change of y is determined entirely by the current value of y, not by when you're observing it. Population models, cooling laws, and many physical equilibria take this form. Because the equation doesn't depend on t, you can analyze its qualitative behavior without finding a single explicit formula for y(t).

The starting point is finding **equilibrium solutions**: values y* where f(y*) = 0. At these values, dy/dt = 0, so the solution is constant — the system sits still. But equilibria tell you more than just where the system pauses. From your work with the first derivative test, you know that the sign of a function tells you whether a quantity is increasing or decreasing. Here, f(y) plays that role: wherever f(y) > 0, solutions are increasing (y is climbing); wherever f(y) < 0, solutions are decreasing (y is falling).

The **phase line** is a one-dimensional diagram that captures this information. Mark the equilibria on a vertical line representing y-values. Between consecutive equilibria, f(y) has constant sign, so draw arrows pointing up (f > 0) or down (f < 0). These arrows show the direction solutions flow. An equilibrium is a **sink** (stable) if arrows on both sides point toward it — any solution that starts nearby will be attracted to it over time. It is a **source** (unstable) if arrows point away — nearby solutions diverge from it. A **node** has arrows pointing in from one side and out from the other (semi-stable).

This analysis gives a complete qualitative picture without solving the ODE: you know where solutions end up, which starting values lead to which behaviors, and how sensitive the long-run outcome is to initial conditions. The existence-uniqueness theorem you studied guarantees that solution curves starting at different initial conditions cannot cross each other, which is what makes the phase-line picture logically consistent. Each initial value y₀ determines exactly one solution trajectory, and the arrows on the phase line tell you exactly where that trajectory goes as t → ∞.
