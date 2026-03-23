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
status: validated
---

# Connected and Simply Connected Regions

## Core Idea
A region D is connected if it cannot be split into two disjoint non-empty open sets. A region is simply connected if every closed loop can be continuously shrunk to a point (equivalently, its fundamental group is trivial). Simply connected domains are crucial for Cauchy's theorem and ensuring that complex line integrals are path-independent.

## Questions

```yaml
- question: "A function f is analytic everywhere on ℂ\\{0, 1}. A student wants to integrate f along two different paths from point A to point B, both staying within the domain. Can they assume the two integrals are equal?"
  type: multiple-choice
  options:
    - "Yes — since f is analytic on the domain, path-independence is guaranteed by Cauchy's theorem"
    - "No — the domain has holes at 0 and 1, so it is not simply connected, and path-independence is not guaranteed"
    - "Yes — both paths stay within the domain, so they can be continuously deformed into each other"
    - "No — complex integration is never path-independent regardless of the domain"
  answer: 1
  explanation: "Path-independence for analytic functions requires a simply connected domain. ℂ\\{0, 1} has two holes (the removed points), so it is not simply connected. A path that winds around the puncture at 0 cannot be continuously deformed into one that does not — the hole blocks the deformation. For functions like 1/z or 1/(z-1), integrating around these holes gives nonzero results. Option C is wrong because paths that wind differently around holes cannot be continuously deformed into each other even though both stay in the domain."

- question: "The annulus A = {z : 1 < |z| < 2} is connected but not simply connected. What does 'not simply connected' mean geometrically for this region?"
  type: multiple-choice
  options:
    - "The annulus has two separate components that cannot be connected by a path within the region"
    - "The annulus is one piece, but a loop circling the inner hole cannot be continuously shrunk to a point while staying inside the annulus"
    - "The annulus has infinitely many connected components, one for each point removed from the disk"
    - "The outer and inner boundary circles each form separate connected components"
  answer: 1
  explanation: "Connected means the region is in one piece: any two points can be joined by a path inside A. The annulus satisfies this — you can travel from any point to any other without leaving A. Simply connected additionally requires no holes: every closed loop can be contracted to a point within the region. A loop winding around the inner hole of the annulus cannot be contracted to a point without crossing that hole. The annulus is the canonical example of a connected-but-not-simply-connected domain."

- question: "The integral ∮_C (1/z) dz = 2πi for a circle C centered at the origin demonstrates that ℂ\\{0} is not simply connected."
  type: true-false
  answer: true
  explanation: "If ℂ\\{0} were simply connected, Cauchy's theorem would guarantee that the integral of any analytic function around any closed curve equals zero. The fact that ∮ 1/z dz = 2πi ≠ 0 for a loop around the origin reveals that something is topologically non-trivial — the loop cannot be contracted to a point, because the origin (a hole) is inside it. The function 1/z 'detects' the hole through integration; the nonzero residue is a topological signature."

- question: "A connected region in ℂ is automatically simply connected."
  type: true-false
  answer: false
  explanation: "Connectivity only requires that the region is in one piece — any two points can be joined by a path inside the region. Simple connectivity is a stronger condition requiring additionally that every closed loop can be contracted to a point, i.e., that the region has no holes. The annulus {1 < |z| < 2} and the punctured plane ℂ\\{0} are both connected (one piece) but not simply connected (they have holes). The implication goes one way: simply connected implies connected, but connected does not imply simply connected."

- question: "Why is simple connectivity, rather than mere connectivity, the condition required to guarantee that analytic functions have path-independent integrals?"
  type: short-answer
  answer: "In a connected but not simply connected domain, two paths from A to B can wind differently around holes in the domain. If the function has a singularity at such a hole, the contribution from winding around it (the residue) causes the two integrals to differ. Simple connectivity rules out holes entirely: any two paths from A to B can be continuously deformed into each other without leaving the domain, and for analytic functions this deformation preserves the integral value. Connectivity alone (one piece) is insufficient because it does not prevent paths from winding differently around holes; simple connectivity removes the holes that would allow such winding."
  explanation: "The geometric intuition is that simple connectivity means there is 'nothing inside' any closed curve — no singularity the curve can encircle. Cauchy's theorem formalizes this: ∮_C f(z) dz = 0 for every closed curve in a simply connected domain where f is analytic. The punctured plane and annulus show the consequences of failure: 1/z has a pole at the origin, and integrating around it gives 2πi rather than 0, because the hole allows the curve to detect the singularity."
```

## Explainer

From topology of the complex plane, you know that open sets and neighborhoods define the basic structure of ℂ. **Connectivity** is the first topological property we extract from that structure. A region D ⊆ ℂ is **connected** if it cannot be partitioned into two disjoint non-empty open subsets — informally, D is "in one piece." Every point in D can be reached from every other point by a path staying inside D. The disk {|z| < 1} is connected; the set {|z| < 1} ∪ {|z| > 2} is not, because the two parts are disconnected from each other with no path between them.

**Simple connectivity** is a stronger condition. A connected region is **simply connected** if every closed curve in D can be continuously deformed (shrunk) to a point while staying within D. The intuition is that D has no holes. A disk is simply connected. An annulus {1 < |z| < 2} is connected but not simply connected, because a loop encircling the inner hole cannot be shrunk to a point without crossing the hole. The punctured plane ℂ\{0} is also not simply connected — a circle around the origin cannot be contracted.

Why does simple connectivity matter in complex analysis? When you integrate a complex function along a curve, the value can depend on the path — unless the domain is simply connected. In a simply connected domain, any two paths from point A to point B can be continuously deformed into each other, and for analytic functions, this deformation preserves the integral value. This is the geometric content behind path-independence. Cauchy's theorem (your next topic) will state this precisely: if f is analytic on a simply connected domain D, then ∮_C f(z) dz = 0 for every closed curve C in D. The simply connected condition ensures there is "nothing inside" the curve that could contribute a nonzero integral.

The canonical example where simple connectivity fails — and matters — is f(z) = 1/z on ℂ\{0}. Integrating around a circle enclosing the origin gives 2πi, not 0. The punctured plane has a hole at the origin, and the function 1/z detects that hole through integration. Simple connectivity is the condition that rules out such holes and guarantees that antiderivatives exist globally within the domain — a result that will underpin both Cauchy's integral formula and the definition of the complex logarithm.


