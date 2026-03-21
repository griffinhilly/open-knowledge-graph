---
id: line-integrals-definition-properties
title: Line Integrals of Scalar and Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-valued-functions-curves
  type: hard
builds-toward:
- conservative-vector-fields-potential
- greens-theorem-applications
tags:
- line-integrals
- scalar
- vector-fields
stage: formal-systems
status: draft
---

# Line Integrals of Scalar and Vector Fields

## Core Idea
For a curve C parametrized by r(t), the line integral of scalar f is ∫_C f ds = ∫_a^b f(r(t)) |r'(t)| dt. For vector field F, ∫_C F · dr = ∫_a^b F(r(t)) · r'(t) dt represents work done by F along C.

## Questions

```yaml
- question: "A particle traverses curve C from point A to point B. If the direction of traversal is reversed (B to A), which of the following is true?"
  type: multiple-choice
  options:
    - "Both ∫_C f ds and ∫_C F·dr change sign"
    - "Only ∫_C F·dr changes sign; ∫_C f ds is unaffected"
    - "Only ∫_C f ds changes sign; ∫_C F·dr is unaffected"
    - "Neither integral changes sign, because the same curve C is used"
  answer: 1
  explanation: "The scalar line integral ∫_C f ds uses the arc-length element ds = |r'(t)| dt, which is always positive — it measures distance regardless of direction. So reversing the path does not change the value. The vector line integral ∫_C F·dr uses dr = r'(t) dt, which carries direction: reversing the path negates r'(t), flipping the sign of the entire integral. This sign flip is physically meaningful — it says that work done against a force (going the wrong way) is negative work."

- question: "If f(x, y, z) = 1 everywhere, what does the scalar line integral ∫_C f ds compute?"
  type: multiple-choice
  options:
    - "The area of the surface bounded by C"
    - "The arc length of the curve C"
    - "The volume swept out as C moves through space"
    - "Zero, because a constant function contributes no information"
  answer: 1
  explanation: "When f = 1, the integrand ∫_C 1 ds reduces to ∫_a^b |r'(t)| dt — the standard formula for arc length. This is a useful sanity check on the definition: the scalar line integral with f = 1 must recover arc length, and the |r'(t)| factor is precisely what ensures this. If you omit |r'(t)| you would get ∫_a^b dt = b − a, which is the length of the parameter interval, not the actual curve length."

- question: "The scalar line integral ∫_C f ds gives the same value regardless of which parametrization is used to traverse curve C."
  type: true-false
  answer: true
  explanation: "The |r'(t)| factor in ∫_a^b f(r(t)) |r'(t)| dt acts as a speed-correction term. If you parametrize the same curve twice as fast, r'(t) is twice as large and the parameter interval is half as long — the two effects cancel exactly. This is the whole point of weighting by |r'(t)|: it converts the parameter integral into a true geometric integral over arc length, independent of how fast you move along the curve."

- question: "Because the vector line integral ∫_C F·dr contains a dot product, it measures the total magnitude of F accumulated along C."
  type: true-false
  answer: false
  explanation: "The dot product F·dr picks out only the component of F *parallel to the curve's direction* at each point — the component perpendicular to the curve contributes nothing. The integral measures how much F 'helps or hinders' motion along C, i.e., work. A force perpendicular to motion does zero work even if it is very large. This is why ∫_C F·dr depends on the direction of traversal (direction of dr), not just the geometric curve."

- question: "Why does the scalar line integral use |r'(t)| while the vector line integral uses r'(t) without the absolute value? What different things are each formula measuring?"
  type: short-answer
  answer: "The scalar line integral weights f by arc length: the |r'(t)| factor converts the parameter derivative into actual distance traveled, so the integral accumulates f as if you were walking along the curve measuring physical length. The vector line integral measures work: dr = r'(t) dt is the infinitesimal displacement vector, which has both magnitude (how far) and direction (which way). Taking F·dr extracts the component of F along the direction of motion. The absolute value is dropped because direction matters — moving against the field does negative work. The two integrals answer different questions: the scalar case asks 'how much of f is there along C?'; the vector case asks 'how much does F assist or resist motion along C?'"
  explanation: "The key distinction is geometric vs. directional accumulation. Arc length is always positive and direction-independent; work depends on whether force and motion point the same way. The |r'(t)| vs r'(t) difference encodes this: |r'(t)| strips direction, r'(t) preserves it."
```

## Explainer

From your work with vector-valued functions and curves, you know that r(t) = (x(t), y(t), z(t)) parametrizes a path through space and that r'(t) is the tangent vector with magnitude |r'(t)| equal to the speed along the curve. A **line integral** generalizes ordinary integration to functions defined along a curve — instead of integrating f(x) over an interval on the x-axis, you integrate f over an arbitrary path in 2D or 3D space.

The **scalar line integral** ∫_C f ds answers: "If f(x, y, z) is a quantity defined at every point in space (say, temperature, or the linear density of a wire), what is the total accumulated value along the curve?" The arc-length element ds = |r'(t)| dt converts the parameter t back into actual distance along the curve, ensuring the answer doesn't depend on how fast you traverse the path. The result ∫_a^b f(r(t)) |r'(t)| dt evaluates f at each point on the curve, weights it by the arc-length element, and sums. If f = 1, you recover the arc length of C — a special case confirming the formula's meaning.

The **vector line integral** ∫_C F · dr has a fundamentally different structure and interpretation. Here F is a vector field — a vector attached to every point in space — and dr = r'(t) dt is the infinitesimal displacement along the curve. The dot product F · dr picks out the component of F *parallel to the curve's direction* at each point, then multiplies by the arc length element. Summing these up gives the total **work** done by the field F on a particle moving along C. If F is a force field (gravity, electromagnetism), this integral gives the physical work. Notice: the |r'(t)| factor that appeared in the scalar case cancels here because dr already carries direction and magnitude. The result ∫_a^b F(r(t)) · r'(t) dt *does* depend on the direction of traversal — reversing the path negates the integral, reflecting the fact that work against a force is negative.

Both integrals share a common structure: evaluate the integrand at each point of the curve (using the parametrization), multiply by the appropriate measure of "how much curve" you've accumulated, and integrate over the parameter. The scalar version uses |r'(t)| to measure arc length; the vector version uses r'(t) to capture both length and direction. This distinction between the two types of line integrals is the conceptual foundation for everything that follows — conservative fields, the gradient theorem, Green's theorem, and Stokes' theorem all hinge on properties of vector line integrals.
