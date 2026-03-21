---
id: parametric-curves-calculus
title: Calculus of Parametric Curves
domain: mathematics
course: calculus-2
prerequisites:
  - id: parametric-equations-intro
    type: hard
  - id: chain-rule
    type: hard
builds-toward:
  - arc-length-parametric
tags: [parametric, derivatives, calculus]
stage: formal-systems
status: validated
---

# Calculus of Parametric Curves

## Core Idea
For parametric curves x = f(t), y = g(t), the slope of the tangent line is dy/dx = (dy/dt)/(dx/dt), applying the chain rule. The second derivative d^2y/dx^2 = (d/dt[dy/dx])/(dx/dt). These formulas let you find tangent lines, identify horizontal and vertical tangents, determine concavity, and locate extrema for parametrically defined curves without eliminating the parameter.

## How It's Best Learned
Derive dy/dx from the chain rule. Practice finding tangent lines to parametric curves (e.g., the cycloid). Identify horizontal tangents (dy/dt = 0) and vertical tangents (dx/dt = 0). Compute the second derivative for concavity analysis.

## Common Misconceptions
- Computing dy/dx as g(t)/f(t) instead of g'(t)/f'(t).
- Confusing horizontal tangent (dy/dt = 0) with vertical tangent (dx/dt = 0).
- Incorrectly computing the second derivative (it is not d^2y/dt^2 divided by d^2x/dt^2).

## Questions

```yaml
- question: "A parametric curve is defined by x = t², y = t³. A student computes the slope dy/dx as t³/t² = t. What error did they make, and what is the correct answer?"
  type: multiple-choice
  options:
    - "No error — dy/dx = y/x = t³/t² = t is correct"
    - "They used y/x instead of (dy/dt)/(dx/dt); the correct slope is (3t²)/(2t) = 3t/2"
    - "They forgot the chain rule entirely; the slope is dy/dt = 3t²"
    - "They should have eliminated the parameter first and differentiated y = x^(3/2) directly"
  answer: 1
  explanation: "The slope of a parametric curve is dy/dx = (dy/dt)/(dx/dt), not y/x. Here, dy/dt = 3t² and dx/dt = 2t, giving dy/dx = 3t²/(2t) = 3t/2. The error in option A confuses the coordinates (y, x) with the derivatives (dy/dt, dx/dt) — a very common mistake when the parameter t appears in both x and y as simple powers. The correct formula comes from the chain rule: dy/dx = (dy/dt) · (dt/dx) = (dy/dt)/(dx/dt)."

- question: "For the curve x = t², y = t³ − 3t, a student wants to find where horizontal and vertical tangents occur. They set dx/dt = 2t = 0, getting t = 0, and call this a horizontal tangent. What is wrong?"
  type: multiple-choice
  options:
    - "Nothing — dx/dt = 0 gives horizontal tangents"
    - "dx/dt = 0 gives vertical tangents, not horizontal ones; horizontal tangents require dy/dt = 3t² − 3 = 0, giving t = ±1"
    - "The student should eliminate t first and then find where dy/dx = 0 in terms of x"
    - "dx/dt = 0 has no geometric meaning for parametric curves"
  answer: 1
  explanation: "This is the most common confusion in parametric calculus. A horizontal tangent requires dy/dx = 0, which means the numerator (dy/dt) equals zero while the denominator (dx/dt) is nonzero. For this curve, dy/dt = 3t² − 3 = 0 gives t = ±1 → horizontal tangents. A vertical tangent requires dy/dx to be undefined, meaning the denominator (dx/dt) equals zero while the numerator is nonzero. dx/dt = 2t = 0 gives t = 0 → vertical tangent. The student swapped the conditions."

- question: "The formula d²y/dx² = [d/dt(dy/dx)] / (dx/dt) is derived by applying the same chain rule logic that gives dy/dx = (dy/dt)/(dx/dt), but treating dy/dx as the new 'y' quantity."
  type: true-false
  answer: true
  explanation: "This is exactly the logic. The first derivative dy/dx is itself a function of t. To find how it changes with respect to x (i.e., its derivative with respect to x), apply the same chain rule: d(dy/dx)/dx = [d(dy/dx)/dt] / (dx/dt). This is why the second derivative formula works — it is the chain rule applied twice, not some separate rule. The formula is NOT d²y/dt² divided by d²x/dt², which would be a ratio of second derivatives in t with no geometric meaning."

- question: "If dx/dt = 0 at a point on a parametric curve, the curve has a horizontal tangent there."
  type: true-false
  answer: false
  explanation: "dx/dt = 0 means the curve is momentarily not moving in the x-direction — it creates a vertical tangent (the curve moves purely vertically at that instant, making the slope undefined). A horizontal tangent occurs when dy/dt = 0 (no vertical motion) while dx/dt ≠ 0. Mixing these two conditions is listed as a core misconception for this topic because the conditions feel symmetric but their geometric consequences are opposite."

- question: "Explain why the second derivative of a parametric curve is NOT computed as d²y/dt² divided by d²x/dt²."
  type: short-answer
  answer: "d²y/dx² measures how the slope dy/dx changes as you move along the x-axis — it is a geometric quantity about the curve's concavity. d²y/dt² and d²x/dt² measure how fast y and x accelerate as the parameter t changes — these are properties of the parameterization, not the curve's geometry. Dividing them gives a ratio that changes when you reparameterize the same curve (e.g., using t² instead of t), so it cannot represent a geometric property. The correct formula applies the chain rule to d(dy/dx)/dx, treating dy/dx as a new function and converting dt to dx."
  explanation: "A useful sanity check: the second derivative d²y/dx² must be independent of the choice of parameterization (it is a property of the curve, not of how you describe it). The ratio d²y/dt² / d²x/dt² fails this test — it changes if you reparameterize. The correct formula [d/dt(dy/dx)] / (dx/dt) passes the test because (dy/dx) is already parameterization-independent, and dividing its t-derivative by dx/dt correctly converts back to a derivative with respect to x."
```

## Explainer

In standard calculus, y is a function of x, so dy/dx is computed directly. For a **parametric curve**, both x and y depend on a third variable t (time, angle, or a parameter). You have two rates: dx/dt (how fast x changes as t varies) and dy/dt (how fast y changes as t varies). To find the slope dy/dx — how y changes with respect to x along the curve — you apply the **chain rule**: dy/dx = (dy/dt) / (dx/dt). Think of it as a unit conversion: dy/dt has units of (y per t) and dx/dt has units of (x per t), so dividing cancels the t and gives (y per x) as desired.

The geometry of the tangent line follows naturally. A **horizontal tangent** requires dy/dx = 0, which happens when dy/dt = 0 (and dx/dt ≠ 0) — the curve is momentarily moving horizontally. A **vertical tangent** requires dy/dx to be undefined, which happens when dx/dt = 0 (and dy/dt ≠ 0) — the curve is momentarily moving vertically. When both derivatives are zero at the same t, the curve has a **singular point** requiring more careful analysis. These conditions tell you where the curve changes direction without eliminating the parameter.

The **second derivative** d²y/dx² measures concavity along the curve. It is not d²y/dt² divided by d²x/dt² — that would be the ratio of two second derivatives in t, which carries no geometric meaning. Instead, you treat d(dy/dx)/dt as a new "dy/dt" and divide by dx/dt: d²y/dx² = [d/dt(dy/dx)] / (dx/dt). The logic is the same chain rule applied again, but now to the quantity dy/dx rather than to y. Once you have the second derivative, concavity analysis proceeds exactly as in standard calculus — positive means concave up, negative means concave down.

A powerful payoff: many important curves (the cycloid, the ellipse, the astroid) have no clean Cartesian equation y = f(x) but are cleanly expressible parametrically. The calculus of parametric curves lets you find tangent lines, extrema, and concavity for all of them. Later, the same machinery extends to arc length and surface area integrals in parametric form, and it is the conceptual foundation for calculus on curves in polar coordinates and in space.
