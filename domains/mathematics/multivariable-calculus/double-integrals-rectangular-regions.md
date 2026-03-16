---
id: double-integrals-rectangular-regions
title: Double Integrals over Rectangular Regions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: iterated-integrals-fubini
  type: hard
builds-toward:
- double-integrals-general-regions
- double-integrals-polar
tags:
- rectangular-regions
- computation
- bounds
stage: formal-systems
status: draft
---

# Double Integrals over Rectangular Regions

## Core Idea
For a rectangular region R = [a, b] × [c, d], the double integral ∬_R f dA = ∫_a^b ∫_c^d f(x, y) dy dx is straightforward: the bounds are constants. This is the entry point for computing double integrals; the order of integration does not matter for rectangles.

## Explainer

From Fubini's theorem and iterated integrals, you already know the central result: a double integral over a rectangle can be evaluated by integrating one variable at a time. The **double integral** ∬_R f(x, y) dA accumulates the value of f(x, y) over every point in the region R, multiplied by an infinitesimal area element dA. Geometrically, when f ≥ 0, this equals the volume of the solid sitting between the xy-plane and the surface z = f(x, y) directly above R. When f takes negative values, the integral counts volume below the plane as negative — the signed volume interpretation parallels the single-variable signed area.

For a rectangular region R = [a, b] × [c, d], Fubini's theorem gives the computation rule: ∬_R f dA = ∫_a^b ∫_c^d f(x, y) dy dx. The inner integral ∫_c^d f(x, y) dy treats x as a fixed constant and integrates f over the y-interval [c, d]. The result is a function of x alone — call it A(x) — representing the "cross-sectional area" of the solid at that x-value. The outer integral ∫_a^b A(x) dx then adds up all those cross-sections across [a, b]. Think of slicing the solid with vertical planes perpendicular to the x-axis: you first compute each slice's area, then integrate the areas to get the total volume.

The critical feature of rectangular regions is that both pairs of bounds are **constants**: a, b, c, d do not depend on x or y. This means you can also integrate in the opposite order — ∫_c^d ∫_a^b f(x, y) dx dy — and get the same answer. Switching order is freely available on rectangles, which makes them computationally flexible. Choose whichever order makes the inner integral easier to compute. For non-rectangular regions, the bounds of the inner integral will depend on the outer variable, and switching order requires re-determining the bounds — a more involved process. Mastering constant-bound rectangles builds the mechanics (and the intuition for what "slicing" means) before that complication arises.

The setup step is as important as the antidifferentiation. Given ∬_R f dA, explicitly write R = [a, b] × [c, d], confirm both pairs of bounds are constants, declare your order of integration, and write the nested integral before computing. A clean setup prevents the most common errors: using a bound for the wrong variable, or accidentally treating an outer variable as a constant inside the inner integral. Once the setup is correct, the inner integral is a standard single-variable antiderivative problem — the outer variable is just a parameter held fixed while you do it.
