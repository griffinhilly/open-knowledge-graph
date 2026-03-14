---
id: counting-complexity-sharp-p
title: Counting Complexity and the Sharp-P Class
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-theorem
  type: hard
- id: alternating-machines-hierarchy
  type: soft
tags:
- counting-complexity
- sharp-p
- '#sat'
- counting-problems
stage: advanced
status: draft
---

# Counting Complexity and the Sharp-P Class

## Core Idea
#P (sharp-P) is the class of counting problems: given a verifier for an NP problem, count how many accepting paths exist. Computing the exact count is at least as hard as deciding membership. #P-complete problems include counting satisfying assignments, perfect matchings, and Hamiltonian cycles—most of which have no known polynomial-time algorithms.

## How It's Best Learned
Study the contrast between decision (SAT ∈ NP) and counting (#SAT ∈ #P). Show that counting perfect matchings is #P-complete even though perfect matching decision is in P.

## Common Misconceptions
- Assuming #P is a subset of NP or vice versa. They are incomparable: #P counts solutions, NP decides membership.
- Thinking counting is 'just' harder than deciding. Some hard-to-count problems have easy-to-decide versions.
