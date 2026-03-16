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
status: draft
---

# Complex Logarithm and Branch Cuts

## Core Idea
Since e^z is periodic, the logarithm is multi-valued: log(w) = log|w| + i(arg(w) + 2πk) for any integer k. To make log single-valued, we choose a branch cut (conventionally the negative real axis) and define a principal branch Log(w). The principal logarithm Log is holomorphic on ℂ minus the cut and satisfies (Log(z))' = 1/z.

## How It's Best Learned
Trace a path around the origin in the complex plane and observe how Log(z) changes; this reveals the branch cut and the multi-valuedness of the logarithm. Compare the principal branch with other branches.

## Common Misconceptions
Thinking log is single-valued like the real logarithm; all branches are equally valid. Assuming the branch cut is arbitrary; while the location is arbitrary, the fact that a cut is needed is not.

## Explainer

You already know the complex exponential e^z, and one of its defining features is that it is **periodic**: e^(z + 2πi) = e^z for every z. This means infinitely many inputs map to the same output. For the real exponential, e^x is strictly increasing and therefore injective — each output comes from exactly one input, so the real logarithm is well-defined. The complex exponential's periodicity destroys injectivity and forces the complex logarithm to be **multi-valued**: if log(w) = z, then z + 2πi, z + 4πi, z − 2πi, and so on are all equally valid logarithms of w.

To see this concretely, write w in polar form as w = r·e^(iθ). Then e^z = w requires e^(Re z)·e^(i Im z) = r·e^(iθ), giving Re(z) = log r (the real logarithm of the modulus) and Im(z) = θ + 2πk for any integer k. So log(w) = log|w| + i·arg(w), where arg(w) can take any of infinitely many values differing by multiples of 2π. There is no canonical choice — they are all legitimate.

To use the logarithm in analysis — to integrate 1/z, to define complex powers z^α — we need a **single-valued function**. The solution is to choose a **branch cut**: a curve from the origin to infinity that we agree never to cross. The standard choice is the negative real axis. By declaring that we always measure the argument in (−π, π], we select exactly one angle for each nonzero complex number (except those on the cut itself, where the function is left undefined). This gives the **principal branch**, written Log(z), which is holomorphic on ℂ minus the negative real axis and satisfies (Log z)′ = 1/z.

The key conceptual point is that the cut is a mathematical choice, not a physical one — a different cut (say, the positive imaginary axis) would give a different branch, equally valid, holomorphic on a different domain. What is not a choice is that some cut is necessary: trying to make the logarithm continuous everywhere on ℂ \ {0} is impossible, because any loop around the origin forces the argument to increase by 2π, creating a discontinuity somewhere. The branch cut marks exactly where that unavoidable discontinuity lives.
