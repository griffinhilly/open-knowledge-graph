---
id: complex-logarithm-branch-cuts
title: Complex Logarithm and Branch Cuts
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-exponential-function
  type: hard
tags:
- logarithm
- branch-cut
- multi-valued
stage: advanced
status: validated
---

# Complex Logarithm and Branch Cuts

## Core Idea
Since e^z is periodic, the logarithm is multi-valued: log(w) = log|w| + i(arg(w) + 2πk) for any integer k. To make log single-valued, we choose a branch cut (conventionally the negative real axis) and define a principal branch Log(w). The principal logarithm Log is holomorphic on ℂ minus the cut and satisfies (Log(z))' = 1/z.

## How It's Best Learned
Trace a path around the origin in the complex plane and observe how Log(z) changes; this reveals the branch cut and the multi-valuedness of the logarithm. Compare the principal branch with other branches.

## Common Misconceptions
Thinking log is single-valued like the real logarithm; all branches are equally valid. Assuming the branch cut is arbitrary; while the location is arbitrary, the fact that a cut is needed is not.

## Questions

```yaml
- question: "A student uses the principal branch to compute Log(-1) = iπ. A classmate says the answer could also be -iπ, or 3iπ, or iπ + 2πki for any integer k. Which student is right, and why?"
  type: multiple-choice
  options:
    - "The first student — Log(-1) = iπ is the unique correct answer because the principal branch is the definition of the logarithm"
    - "The classmate — all values iπ + 2πki for any integer k are valid logarithms of -1; Log gives only the principal branch value by a conventional choice, not because the others are wrong"
    - "The classmate — the logarithm of a negative number is undefined, so neither answer is valid"
    - "Both — iπ and -iπ are both principal branch values depending on which branch cut convention you use"
  answer: 1
  explanation: "The complex logarithm is genuinely multi-valued: since e^(iπ) = e^(-iπ) = e^(iπ + 2πki) = -1 for all integers k, all these are valid solutions to e^z = -1. The principal branch Log selects one of them — the one whose imaginary part lies in (-π, π] — by convention. This is a useful choice for computation but it does not make the other values 'wrong.' Multi-valuedness is intrinsic to the logarithm; the principal branch is a disambiguation tool, not the definition."

- question: "Why must any branch of the complex logarithm have a branch cut — a curve from 0 to ∞ along which the function is discontinuous?"
  type: multiple-choice
  options:
    - "Because the complex logarithm is not holomorphic anywhere, and a branch cut marks the region where it fails to be differentiable"
    - "Because log|z| (the real part of the logarithm) is undefined at the origin, and the branch cut extends this singularity to infinity"
    - "Because any continuous path around the origin forces the argument of z to increase by 2π, making a globally continuous single-valued logarithm on ℂ\\{0} impossible — the discontinuity must live somewhere"
    - "Because the principal argument function Arg(z) is only defined for real z, requiring a cut to extend it to the complex plane"
  answer: 2
  explanation: "The topological reason is definitive: if you trace a closed loop around the origin, the argument of z increases by 2π — a fact built into the geometry of the complex plane. Any single-valued continuous function claiming to be a logarithm must therefore be discontinuous at some point along that loop. The branch cut is where we accept that discontinuity. No clever formula can avoid it; it is a consequence of the plane's topology around the origin. The location of the cut is a choice; the existence of some cut is not."

- question: "Different branch cuts for the complex logarithm are equally valid mathematically — choosing the negative real axis as a branch cut rather than the positive imaginary axis is a convention, not a mathematical necessity."
  type: true-false
  answer: true
  explanation: "Any ray from the origin to infinity (or any curve connecting origin to ∞) can serve as a branch cut. The standard choice — the negative real axis, giving the principal branch with argument in (-π, π] — is conventional and widely used, but a branch cut along the positive imaginary axis, or any other ray, gives an equally valid single-valued holomorphic function on a different domain. What is not conventional is the need for *some* cut: that is topologically forced. The choice of *where* to place it is genuinely arbitrary."

- question: "The multi-valuedness of the complex logarithm is a problem with the standard definition that could be resolved by choosing a better formula — one that is single-valued everywhere on ℂ\\{0}."
  type: true-false
  answer: false
  explanation: "Multi-valuedness is not a defect in the definition — it is an intrinsic consequence of e^z being periodic with period 2πi. Because e^z is not injective, its inverse must be multi-valued; no formula can change this. Any attempt to define a single-valued logarithm on all of ℂ\\{0} must introduce a discontinuity somewhere (the branch cut), because a continuous loop around the origin forces the argument to change by 2π. The branch cut does not solve multi-valuedness — it relocates and acknowledges the unavoidable discontinuity."

- question: "Explain why the complex logarithm is multi-valued, starting from what you know about the complex exponential. Why is a branch cut necessary rather than optional?"
  type: short-answer
  answer: "The complex exponential e^z is periodic: e^(z + 2πi) = e^z for all z, meaning infinitely many distinct inputs map to the same output. The logarithm, as the inverse of e^z, must assign to each w all values z such that e^z = w — and there are infinitely many, each differing by a multiple of 2πi. This is multi-valuedness. To use the logarithm in analysis (integration, complex powers, etc.), we need a single-valued function, which requires choosing one value for each w. But no such choice can be made continuously everywhere on ℂ\\{0}: traversing a loop around the origin forces the argument to increase by 2π, so any single-valued selection must be discontinuous somewhere. A branch cut is the curve where we place that forced discontinuity — making log single-valued and holomorphic on the cut domain, at the cost of being undefined on the cut itself."
  explanation: "The logical chain is: e^z periodic → log multi-valued → any single-valued version must have a discontinuity → branch cut places that discontinuity on a chosen curve. The branch cut is necessary because the complex plane has non-trivial topology around the origin: loops around it are not contractible to points, so they cannot be made argument-continuous. This topological fact forces the cut; only its location is a choice."
```

## Explainer

You already know the complex exponential e^z, and one of its defining features is that it is **periodic**: e^(z + 2πi) = e^z for every z. This means infinitely many inputs map to the same output. For the real exponential, e^x is strictly increasing and therefore injective — each output comes from exactly one input, so the real logarithm is well-defined. The complex exponential's periodicity destroys injectivity and forces the complex logarithm to be **multi-valued**: if log(w) = z, then z + 2πi, z + 4πi, z − 2πi, and so on are all equally valid logarithms of w.

To see this concretely, write w in polar form as w = r·e^(iθ). Then e^z = w requires e^(Re z)·e^(i Im z) = r·e^(iθ), giving Re(z) = log r (the real logarithm of the modulus) and Im(z) = θ + 2πk for any integer k. So log(w) = log|w| + i·arg(w), where arg(w) can take any of infinitely many values differing by multiples of 2π. There is no canonical choice — they are all legitimate.

To use the logarithm in analysis — to integrate 1/z, to define complex powers z^α — we need a **single-valued function**. The solution is to choose a **branch cut**: a curve from the origin to infinity that we agree never to cross. The standard choice is the negative real axis. By declaring that we always measure the argument in (−π, π], we select exactly one angle for each nonzero complex number (except those on the cut itself, where the function is left undefined). This gives the **principal branch**, written Log(z), which is holomorphic on ℂ minus the negative real axis and satisfies (Log z)′ = 1/z.

The key conceptual point is that the cut is a mathematical choice, not a physical one — a different cut (say, the positive imaginary axis) would give a different branch, equally valid, holomorphic on a different domain. What is not a choice is that some cut is necessary: trying to make the logarithm continuous everywhere on ℂ \ {0} is impossible, because any loop around the origin forces the argument to increase by 2π, creating a discontinuity somewhere. The branch cut marks exactly where that unavoidable discontinuity lives.
