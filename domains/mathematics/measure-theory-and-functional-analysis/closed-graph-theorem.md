---
id: closed-graph-theorem
title: Closed Graph Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: banach-spaces-definition
  type: hard
tags:
- functional-analysis
stage: expert
status: validated
---

# Closed Graph Theorem

## Core Idea
The closed graph theorem states that a linear operator T: X → Y between Banach spaces is continuous if and only if its graph {(x, T(x)) : x ∈ X} is closed in X × Y. This provides a powerful criterion for continuity without explicit bound verification.

## Questions

```yaml
- question: "A linear operator T: X → Y between Banach spaces has the following property: whenever xₙ → x in X and T(xₙ) → y in Y, it follows that y = T(x). What does the closed graph theorem allow you to conclude?"
  type: multiple-choice
  options:
    - "T is injective (one-to-one) but not necessarily surjective"
    - "T is continuous (equivalently, bounded) — the closed graph condition is equivalent to continuity for linear operators between Banach spaces"
    - "T has a bounded inverse, but T itself may fail to be continuous"
    - "Nothing conclusive — a closed graph implies continuity only for surjective operators"
  answer: 1
  explanation: "The closed graph theorem states precisely that for a linear operator between Banach spaces, having a closed graph (the sequential condition described) is equivalent to being continuous, i.e., bounded. There is no additional requirement on T beyond linearity — injectivity, surjectivity, and bijectivity are irrelevant to the theorem. The value of the theorem is that this sequential condition is often far easier to verify directly from T's definition than finding an explicit bound C with ‖T(x)‖ ≤ C‖x‖."

- question: "Why does the closed graph theorem fail for linear operators between incomplete normed spaces — that is, normed spaces that are not Banach spaces?"
  type: multiple-choice
  options:
    - "Because the norm topology on an incomplete space cannot detect convergence of Cauchy sequences"
    - "Because completeness is required both to run the open mapping theorem in the proof and to ensure Cauchy sequences arising in the argument actually converge"
    - "Because linear operators on incomplete spaces are never bounded, making the conclusion vacuously false"
    - "Because incomplete spaces have no well-defined product topology, so the graph cannot be defined"
  answer: 1
  explanation: "Completeness is not a technicality — it is load-bearing in the proof. The standard proof of the closed graph theorem invokes the open mapping theorem (a bijective bounded linear operator between Banach spaces has a bounded inverse), which itself requires both spaces to be Banach (complete). In an incomplete space, a linear operator can have a closed graph while failing to be bounded: you can construct sequences where the closed graph hypothesis holds formally but the missing limit points (absent because the space is incomplete) allow boundedness to fail. The theorem is genuinely false without completeness."

- question: "For a linear operator T: X → Y between Banach spaces, T having a closed graph is equivalent to T being continuous."
  type: true-false
  answer: true
  explanation: "This is the content of the closed graph theorem. For general maps between metric spaces, these properties are distinct: a function can have a closed graph while failing to be continuous (consider f: ℝ → ℝ with f(x) = 1/x for x ≠ 0 and f(0) = 0 — the graph is closed but f is discontinuous at 0). But for *linear operators between Banach spaces*, the two conditions collapse to the same thing. The linearity and completeness work together to give the equivalence. This is precisely what makes the theorem powerful: it trades a topological property (closed graph) for an analytic one (boundedness)."

- question: "For any function between metric spaces, having a closed graph is equivalent to being continuous — the closed graph theorem is just the specialization of this general fact to Banach spaces."
  type: true-false
  answer: false
  explanation: "This is false, and the failure of the general case is what makes the theorem non-trivial. For arbitrary functions between metric spaces, closed graph and continuity are genuinely different properties. A function can be discontinuous while still having a closed graph: if f(x) = 1/x for x ≠ 0 and f(0) = 0, the graph {(x, f(x))} is closed in ℝ² (it contains all its limit points), but f is discontinuous at 0. The equivalence is special to *linear operators* on *Banach (complete) spaces* — linearity constrains the behavior of the operator globally, and completeness ensures that Cauchy sequences in the argument converge."

- question: "What practical advantage does the closed graph theorem provide when proving that a linear operator is continuous, and why is the completeness of both spaces required?"
  type: short-answer
  answer: "The practical advantage is a shift in the proof burden: instead of finding an explicit constant C such that ‖T(x)‖ ≤ C‖x‖ for all x (which can be difficult or impossible to derive directly), you instead verify the sequential condition — that whenever xₙ → x and T(xₙ) → y, it follows that y = T(x). For many operators defined by formulas (differential or integral operators), this condition is much easier to check from the operator's definition than finding a direct bound. Completeness is required because the proof uses the open mapping theorem, which requires both spaces to be Banach, and because without completeness the Cauchy sequences that appear in the argument may fail to have limits in the spaces, breaking the chain of reasoning."
  explanation: "This is the theorem's mathematical elegance: it converts a quantitative question (find the bound) into a qualitative/topological question (is the graph closed?). Many important operators in analysis — differential operators, integral operators, unbounded operators on function spaces — are most naturally verified continuous via the closed graph theorem because their definitions make the sequential condition easy to check, even when a direct estimate of the norm would be technically demanding."
```

## Explainer

From your study of Banach spaces, you know that a Banach space is a complete normed vector space — complete meaning every Cauchy sequence converges. Continuity of a linear operator T: X → Y means small inputs produce small outputs, equivalently that T is **bounded**: there exists a constant C such that ‖T(x)‖ ≤ C‖x‖ for all x. Proving this directly often requires knowing the bound C explicitly. The closed graph theorem provides an indirect route: instead of bounding T, check a topological property of its graph.

The **graph** of T is the set of input-output pairs Γ(T) = {(x, T(x)) : x ∈ X}, living in the product space X × Y. Saying the graph is **closed** means: whenever a sequence (xₙ, T(xₙ)) converges to some pair (x, y) in X × Y, then y = T(x). In plain English — if inputs converge and outputs converge, the limit of the outputs must equal T applied to the limit of the inputs. This is weaker than continuity, because it requires *both* sequences to converge as a hypothesis; continuity only requires input convergence. For arbitrary maps these notions differ, but for linear operators between Banach spaces they collapse to the same thing.

Why does completeness matter? The proof leverages the open mapping theorem: a bijective bounded linear operator between Banach spaces has a bounded inverse. If T has a closed graph, one can construct an auxiliary operator that makes T continuous by exploiting the closed graph to "borrow" convergence from one space to the other. The full argument uses the completeness of both spaces in a critical way — the theorem fails for incomplete spaces. This is why Banach spaces, not just normed spaces, are the natural setting.

The practical value of the closed graph theorem is that it shifts the proof burden. To show T is continuous, you don't need to find the constant C or directly verify the bound. Instead, you verify a sequential condition: if xₙ → x and T(xₙ) → y, then y = T(x). This is often much easier to check from the definition of T. Many operators in analysis — differential operators, integral operators — are most naturally verified continuous by this route rather than by direct estimation.
