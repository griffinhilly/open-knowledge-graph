---
id: time-complexity-classes-formal
title: Time Complexity and the Class P
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: big-o-notation
  type: hard
- id: algorithm-complexity
  type: soft
- id: divide-and-conquer-recurrences
  type: soft
builds-toward:
- nondeterministic-turing-machines
- np-and-polynomial-time
- space-complexity-classes-formal
tags:
- complexity
- time-complexity
- polynomial-time
- P
stage: advanced
status: validated
---

# Time Complexity and the Class P

## Core Idea
The time complexity of a Turing machine on an input is the number of steps before it halts. DTIME(f(n)) is the class of languages decidable in O(f(n)) steps. The class P = ∪ₖ DTIME(nᵏ) captures 'efficiently solvable' problems — those with polynomial-time algorithms. P is robust to reasonable changes in the computational model (multi-tape TMs, random-access machines), making it the standard definition of tractability. The linear speedup theorem shows that constant factors in time bounds are irrelevant for class membership.

## How It's Best Learned
Work through concrete examples of problems in P: sorting, graph reachability, primality testing (AKS). Then practice proving time bounds by counting TM steps or reasoning about algorithm complexity. Understand why polynomial vs. super-polynomial is the key dividing line rather than, say, linear vs. quadratic.

## Common Misconceptions
- P is not the same as 'fast in practice' — a polynomial algorithm with exponent 100 is theoretically tractable but useless for real inputs.
- The robustness of P across models does not extend to all complexity classes; finer classes like NC or L are sensitive to model choice.
