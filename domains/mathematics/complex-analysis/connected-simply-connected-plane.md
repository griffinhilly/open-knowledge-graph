---
id: connected-simply-connected-plane
title: Connected and Simply Connected Regions
domain: mathematics
course: complex-analysis
prerequisites:
- id: topological-spaces-complex-plane
  type: hard
builds-toward:
- cauchys-theorem
- analytic-continuation
tags:
- topology
- connectivity
- simply-connected
stage: advanced
status: draft
---

# Connected and Simply Connected Regions

## Core Idea
A region D is connected if it cannot be split into two disjoint non-empty open sets. A region is simply connected if every closed loop can be continuously shrunk to a point (equivalently, its fundamental group is trivial). Simply connected domains are crucial for Cauchy's theorem and ensuring that complex line integrals are path-independent.

## Explainer

From topology of the complex plane, you know that open sets and neighborhoods define the basic structure of ℂ. **Connectivity** is the first topological property we extract from that structure. A region D ⊆ ℂ is **connected** if it cannot be partitioned into two disjoint non-empty open subsets — informally, D is "in one piece." Every point in D can be reached from every other point by a path staying inside D. The disk {|z| < 1} is connected; the set {|z| < 1} ∪ {|z| > 2} is not, because the two parts are disconnected from each other with no path between them.

**Simple connectivity** is a stronger condition. A connected region is **simply connected** if every closed curve in D can be continuously deformed (shrunk) to a point while staying within D. The intuition is that D has no holes. A disk is simply connected. An annulus {1 < |z| < 2} is connected but not simply connected, because a loop encircling the inner hole cannot be shrunk to a point without crossing the hole. The punctured plane ℂ\{0} is also not simply connected — a circle around the origin cannot be contracted.

Why does simple connectivity matter in complex analysis? When you integrate a complex function along a curve, the value can depend on the path — unless the domain is simply connected. In a simply connected domain, any two paths from point A to point B can be continuously deformed into each other, and for analytic functions, this deformation preserves the integral value. This is the geometric content behind path-independence. Cauchy's theorem (your next topic) will state this precisely: if f is analytic on a simply connected domain D, then ∮_C f(z) dz = 0 for every closed curve C in D. The simply connected condition ensures there is "nothing inside" the curve that could contribute a nonzero integral.

The canonical example where simple connectivity fails — and matters — is f(z) = 1/z on ℂ\{0}. Integrating around a circle enclosing the origin gives 2πi, not 0. The punctured plane has a hole at the origin, and the function 1/z detects that hole through integration. Simple connectivity is the condition that rules out such holes and guarantees that antiderivatives exist globally within the domain — a result that will underpin both Cauchy's integral formula and the definition of the complex logarithm.


