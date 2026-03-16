---
id: polynomial-time-reductions
title: Polynomial-Time Reductions
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-and-polynomial-time
  type: hard
- id: time-complexity-classes-formal
  type: hard
- id: computability-reductions
  type: soft
- id: big-o-notation
  type: soft
builds-toward:
- np-completeness-formal
- cook-levin-theorem-formal
tags:
- reductions
- polynomial-time
- complexity
- NP-hardness
stage: advanced
status: validated
---

# Polynomial-Time Reductions

## Core Idea
A polynomial-time many-one reduction (Karp reduction) from problem A to problem B is a polynomial-time computable function f such that x ∈ A iff f(x) ∈ B. If B has a polynomial-time algorithm, so does A. Polynomial-time reductions are the standard tool for proving NP-hardness: to show a new problem B is NP-hard, reduce a known NP-hard problem to B in polynomial time. This preserves computational hardness upward and solutions downward, enabling systematic comparison of complexity.

## How It's Best Learned
Master the 3-SAT to 3-Colorability reduction as a template: understand both the formal gadget construction and why it is correct. Practice building reductions from 3-SAT to other NP-complete problems, always verifying correctness and polynomial-time running time.

## Common Misconceptions
- The direction of reduction is crucial and often backwards from intuition: to show B is hard, reduce a known-hard problem *to* B, which shows B must be at least as hard.
- Polynomial-time reductions are more restrictive than Turing reductions used in computability theory; they do not allow multiple adaptive queries.

## Questions

```yaml
- question: "You want to prove that problem B is NP-hard. You have a polynomial-time reduction from 3-SAT to B. What does this mean?"
  type: multiple-choice
  options: ["B can be solved by solving 3-SAT", "3-SAT is at least as hard as B", "B is at least as hard as 3-SAT", "B and 3-SAT are equally hard"]
  answer: 2
  explanation: "A reduction from 3-SAT to B means any instance of 3-SAT can be transformed into an instance of B in polynomial time. If B were easy (in P), we could use that solution to solve 3-SAT efficiently — contradiction. So B must be at least as hard as 3-SAT. The reduction passes hardness forward, not backward."

- question: "If A reduces to B in polynomial time (A ≤_p B), and B ∈ P, then A ∈ P."
  type: true-false
  answer: true
  explanation: "This is the fundamental point of reductions: if you can transform every instance of A into an instance of B in polynomial time, and B is solvable in polynomial time, then A is solvable in polynomial time too (transform first, then solve B). Solutions flow in the opposite direction from the reduction."

- question: "Why is the direction of a polynomial-time reduction critical when proving NP-hardness?"
  type: short-answer
  answer: "To prove B is NP-hard, you must reduce a known NP-hard problem TO B (not from B to something else). This shows that solving B would imply solving the known-hard problem, meaning B cannot be easier."
  explanation: "The reduction direction encodes a 'B is at least as hard' relationship. Reducing B to something easy would only show B is easy too. Reducing something hard to B shows B must be at least as hard as that problem. This directional asymmetry is the single most common source of confusion in complexity proofs."
```

## Explainer

Polynomial-time reductions are the backbone of complexity theory's comparative framework. You have already seen computability reductions, which ask whether one problem is computable given an oracle for another. Polynomial-time reductions sharpen that question: not only can we solve A using B, but we can do the transformation efficiently — in polynomial time. This efficiency requirement is what makes them the right tool for distinguishing tractable from intractable problems.

The formal definition of a Karp reduction (many-one polynomial-time reduction) from A to B is a function f computable in polynomial time such that x ∈ A if and only if f(x) ∈ B. Every instance of A gets mapped to an instance of B such that membership is preserved in both directions. If you can solve B efficiently, then to solve A you just transform the input and run B's algorithm. The key consequence: B being easy makes A easy, so B being hard implies A must also be hard.

This asymmetry in how hardness and ease flow is the hardest conceptual piece. The direction of the arrow A ≤_p B says "A reduces to B," meaning B is at least as hard as A — hardness travels upward, against the arrow. To prove a new problem B is NP-hard, you reduce a known NP-hard problem (like 3-SAT) to B. This shows that an efficient algorithm for B would yield an efficient algorithm for 3-SAT, which would imply P = NP. Since we believe P ≠ NP, no such algorithm for B can exist.

The classic example is the reduction from 3-SAT to 3-Colorability: given a 3-SAT formula, construct a graph (using variable gadgets and clause gadgets) such that the graph is 3-colorable exactly when the formula is satisfiable. The construction runs in polynomial time. This proves 3-Colorability is NP-hard, because if you could color graphs efficiently, you could solve 3-SAT efficiently.

Polynomial-time reductions are more restrictive than the Turing reductions encountered in computability theory. A Turing reduction allows multiple adaptive queries to an oracle; a Karp reduction must produce a single transformed instance. In practice, most NP-hardness proofs use Karp reductions, which also compose: if A ≤_p B and B ≤_p C, then A ≤_p C, allowing chains of reductions across the NP-complete problems.
