---
id: double-integrals
title: 'Double Integrals: Definition and Setup'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: definite-integral-definition
  type: hard
- id: functions-of-several-variables
  type: hard
builds-toward:
- iterated-integrals-fubini
- double-integrals-rectangular-regions
tags:
- double-integrals
- riemann-sum
- definition
stage: formal-systems
status: draft
---

# Double Integrals: Definition and Setup

## Core Idea
The double integral ∬_R f(x, y) dA extends integration to 2D: partition region R into small rectangles, form Riemann sums by approximating f as constant on each, and take the limit as partition size shrinks. The result measures the volume under the surface z = f(x, y).

## Questions

```yaml
- question: "A student immediately sets up ∫∫ f(x,y) dx dy to compute ∬_R f dA, reasoning that a double integral is just two nested single integrals by definition. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — the double integral is defined as two nested single integrals in the order dx dy"
    - "The student should integrate dy dx instead, since x comes first in the Cartesian plane"
    - "Computing as iterated integrals is justified by Fubini's theorem, not the definition — the definition is a limit of Riemann sums"
    - "The student needs to include a Jacobian factor to account for the 2D area element"
  answer: 2
  explanation: "The double integral ∬_R f dA is defined as the limit of 2D Riemann sums — the same limiting process as in 1D, extended to rectangles in the plane. Fubini's theorem then proves (under appropriate conditions) that this limit equals the iterated integral ∫∫ f dy dx or ∫∫ f dx dy. The iterated-integral computation method and the definition are different things. This distinction matters because Fubini's theorem has conditions, and it explains why you can sometimes swap integration order (justified by Fubini) but can't always do so blindly."

- question: "If f(x,y) = 1 everywhere on region R, what does ∬_R f(x,y) dA equal?"
  type: multiple-choice
  options:
    - "1, since f is constantly 1 and integration of a constant just returns that constant"
    - "0, since a flat surface at height 1 has no interesting volume"
    - "The area of region R"
    - "The perimeter of region R"
  answer: 2
  explanation: "When f = 1, the Riemann sum becomes ∑ 1·ΔA = ∑ ΔA, which approximates the total area of region R. In the limit, ∬_R 1 dA = area(R). Geometrically, the 'volume' under the flat surface z = 1 above R is just the base area R times height 1. This is the simplest and most important special case: the double integral degenerates to an area computation when the integrand is 1."

- question: "The double integral ∬_R f(x,y) dA can be negative when f takes negative values on part of R."
  type: true-false
  answer: true
  explanation: "Just like the 1D definite integral gives signed area (subtracting where f < 0), the double integral gives signed volume. Where f < 0, the 'boxes' in the Riemann sum have negative height, contributing negatively to the sum. If f is negative everywhere on R, ∬_R f dA is negative. This makes double integrals useful for computing net quantities (like net electric charge or net probability density) rather than just positive volumes."

- question: "The double integral ∬_R f(x,y) dA is defined as two successive single integrals; this is its definition, not a theorem."
  type: true-false
  answer: false
  explanation: "This is the key conceptual error to avoid. The double integral is defined as the limit of 2D Riemann sums: partition R into small rectangles, evaluate f at sample points, multiply by area ΔA, sum, and take the limit as rectangle size shrinks. Fubini's theorem is what guarantees (under appropriate conditions on f and R) that this limit equals the iterated integral ∫_a^b [∫_c^d f(x,y) dy] dx. Definition and computation method are different things, and conflating them causes errors when Fubini's conditions aren't met."

- question: "Why is it important to distinguish the definition of the double integral from the method of computing it as iterated integrals?"
  type: short-answer
  answer: "The definition (limit of Riemann sums) tells you what the double integral means and when it exists. The iterated-integral computation method is justified by Fubini's theorem, which has conditions (f must be integrable, and for non-rectangular regions, the limits of integration must correctly describe the region). Keeping them separate matters in practice because: (1) when changing the order of integration, you must re-derive the limits from the geometry of R — the region doesn't change, but how you slice it does; (2) some functions violate Fubini's conditions and the two iterated integrals give different values even though the double integral is well-defined."
  explanation: "The practical payoff of this conceptual clarity is that you can swap integration order confidently (because Fubini justifies it) while knowing that the limits of integration must be rederived from scratch — they aren't symmetric. You also recognize that ∬ 1 dA = area(R) and ∬ f dA can be negative, which are properties of the definition, not artifacts of the computation method."
```

## Explainer

A single definite integral ∫_a^b f(x)dx measures the signed area under a 1D curve. The double integral ∬_R f(x, y) dA extends this to two dimensions: instead of area, you accumulate **volume** under the surface z = f(x, y) above a planar region R. The construction mirrors the 1D Riemann sum you already know, scaled up by one dimension.

The definition partitions R into small rectangles of area ΔA = Δx · Δy. On each rectangle, pick a sample point (xᵢⱼ, yᵢⱼ) and approximate the solid above that rectangle as a thin box of height f(xᵢⱼ, yᵢⱼ) and volume f(xᵢⱼ, yᵢⱼ) · ΔA. The **Riemann sum** ∑ᵢ∑ⱼ f(xᵢⱼ, yᵢⱼ)ΔA approximates the total volume by summing all boxes. Taking the limit as rectangle dimensions shrink to zero gives ∬_R f(x, y) dA — if the limit exists independently of partition choice and sample points, f is integrable over R.

A critical conceptual point: the double integral is a single limit, not two nested limits. The **Fubini theorem** (your next topic) is what allows you to compute double integrals as iterated single integrals — but that is a theorem, not the definition. Keeping definition and computation method separate matters when you encounter situations where the order of integration must be swapped, or when working with non-rectangular regions that require careful setup.

When f can be negative, the double integral gives signed volume: regions where f < 0 subtract from the total. When f = 1 everywhere, ∬_R 1 dA = area(R) — the integral degenerates to measuring the region itself. More broadly, double integrals compute mass (when f is a density), electric charge, probability, center of mass, and many other quantities distributed over a 2D region. The setup skill — identifying R, understanding the geometry of the solid, and recognizing what f represents — is what separates successful integration from mechanical symbol manipulation.
