---
id: open-sets-real-line
title: Open Sets on the Real Line
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
builds-toward:
- closed-sets-real-line
- compact-sets
- epsilon-delta-continuity
tags:
- open-sets
- topology
- neighborhoods
stage: abstract-reasoning
status: draft
---

# Open Sets on the Real Line

## Core Idea
A set U ⊆ ℝ is open if for every x ∈ U, there exists ε > 0 such that the interval (x - ε, x + ε) ⊆ U. Open sets are the basic objects of topology: unions of open sets are open, finite intersections of open sets are open, and ℝ and ∅ are open. They formalize the idea of 'interior points'.

## How It's Best Learned
Verify (a,b), ℝ, and ∅ are open; show [a,b] is not open (endpoints have no ε-neighborhood inside). Prove that finite intersection of open intervals can be closed: (0,2) ∩ (1,3) = (1,2) is open, but ∩ᵢ(0,1/i) = ∅.

## Common Misconceptions
- Confusing open with 'having no boundary'; (0,1) is open but has a well-defined boundary.
- Assuming open means 'sparse' or 'disconnected'; ℝ is open and fully connected.
- Forgetting infinite unions of open sets are open but infinite intersections need not be.
