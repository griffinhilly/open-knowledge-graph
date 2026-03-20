---
id: separation-axioms-t0-t1-t2
title: 'Separation Axioms: T₀, T₁, and T₂ (Hausdorff)'
domain: mathematics
course: topology
prerequisites:
- id: limit-points-convergence-topology
  type: hard
builds-toward:
- hausdorff-spaces
- separation-axioms-t3-regular
tags:
- separation-axioms
- t0
- t1
- t2
- hausdorff
stage: advanced
status: draft
---

# Separation Axioms: T₀, T₁, and T₂ (Hausdorff)

## Core Idea
Separation axioms form a hierarchy measuring how well a topology distinguishes points. T₀ (Kolmogorov) requires that for any two distinct points, at least one has an open neighborhood not containing the other. T₁ (Fréchet) strengthens this so that each point has a neighborhood excluding the other, which is equivalent to requiring all singletons to be closed. T₂ (Hausdorff) requires disjoint open neighborhoods for any two distinct points, guaranteeing that limits of convergent sequences are unique. Each level excludes more pathological spaces: most spaces encountered in analysis and geometry are at least Hausdorff, making T₂ the practical baseline for well-behaved topology.

## How It's Best Learned
Examine concrete examples at each level: the indiscrete topology fails even T₀, the cofinite topology on an infinite set is T₁ but not T₂, and the Euclidean topology is T₂. Seeing exactly where each axiom fails in these examples makes the hierarchy concrete.

## Common Misconceptions
T₁ does not imply Hausdorff—the cofinite topology on an infinite set separates points from each other with open sets but cannot produce disjoint neighborhoods. Students also sometimes think Hausdorff is an exotic condition, when in fact most familiar spaces (metric spaces, manifolds) are automatically Hausdorff.

