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
