---
id: related-rates
title: Related Rates
domain: mathematics
course: calculus-1
prerequisites:
  - id: implicit-differentiation
    type: hard
  - id: chain-rule
    type: hard
builds-toward:
  - optimization-problems
tags: [derivatives, applications, related-rates]
stage: formal-systems
status: validated
---

# Related Rates

## Core Idea
Related rates problems involve two or more quantities that change with respect to time, connected by an equation. You differentiate the equation with respect to time (using implicit differentiation and the chain rule) to relate the rates of change. For example, if a balloon's volume V and radius r are related by V = (4/3)*pi*r^3, then dV/dt = 4*pi*r^2 * dr/dt. This is one of the most important applications of the derivative.

## How It's Best Learned
Follow a systematic process: draw a diagram, identify variables and rates, write the relating equation, differentiate with respect to time, substitute known values, and solve for the unknown rate. Work many examples: ladders, cones filling with water, shadows, expanding circles.

## Common Misconceptions
- Substituting known values before differentiating (this destroys the variable relationships).
- Forgetting that all variables are functions of time t.
- Not correctly identifying what rate is given vs. what rate is asked for.

## Explainer

Related rates problems are an application of two tools you already own: the **chain rule** and **implicit differentiation**. The chain rule tells you how to differentiate a composition of functions; implicit differentiation lets you differentiate an equation involving multiple variables without solving for one variable first. Related rates put these together in a time-based setting: two quantities are changing simultaneously, they're linked by a geometric or physical equation, and you want to know one rate of change given the other.

The key mental shift is recognizing that every variable in a related-rates problem is secretly a function of time t, even if t doesn't appear explicitly in the equation. A sphere's volume V and radius r are related by V = (4/3)πr³. This equation is always true, so differentiating both sides with respect to t — treating r and V as functions of t and applying the chain rule — gives dV/dt = 4πr² · dr/dt. This says: the rate at which the volume grows equals 4πr² times the rate at which the radius grows. If you know how fast the radius is increasing (dr/dt) and the current radius, you can find dV/dt instantly.

The procedure for any related-rates problem follows a reliable sequence: (1) **Draw and label** a diagram with all variables marked. (2) **Write the relating equation** — the geometry or formula that connects the variables (Pythagorean theorem, similar triangles, volume formula, etc.). (3) **Differentiate both sides with respect to t**, applying the chain rule wherever a variable appears. (4) **Substitute the known values** (including the rates and the current values of variables) into the differentiated equation. (5) **Solve** for the unknown rate. The crucial rule: steps 3 and 4 must stay in this order. Substituting before differentiating freezes variables that must remain variable during differentiation, destroying the relationship.

A classic example: a 10-foot ladder leans against a wall. The base slides away from the wall at 2 ft/s. How fast is the top sliding down when the base is 6 feet from the wall? Label: x = horizontal distance, y = vertical height. The Pythagorean theorem gives x² + y² = 100. Differentiating: 2x(dx/dt) + 2y(dy/dt) = 0. At the moment x = 6: y = √(100 − 36) = 8. Substituting: 2(6)(2) + 2(8)(dy/dt) = 0, so dy/dt = −24/16 = −3/2 ft/s. The negative sign confirms the top is sliding *down*. Every related-rates problem is a variant of this template: a geometric constraint, implicit differentiation with respect to time, and careful substitution after differentiating.
