---
id: cantor-diagonalization
title: Cantor's Diagonalization Argument
domain: mathematics
course: methods-of-proof
prerequisites:
- id: cardinality-and-countability
  type: hard
- id: proof-by-contradiction
  type: soft
tags:
- diagonalization
- uncountability
- Cantor
- real-numbers
- power-set
stage: formal-systems
status: validated
---

# Cantor's Diagonalization Argument

## Core Idea
Cantor's diagonalization argument proves that the real numbers in [0,1] are uncountable: assume for contradiction that they can be listed r₁, r₂, r₃, …, then construct a new real number d whose nth decimal digit differs from the nth digit of rₙ. This number d is in [0,1] but differs from every entry on the list, contradicting the assumption. The same argument shows that for any set A, the power set P(A) has strictly greater cardinality than A, implying there is no largest infinity.

## How It's Best Learned
Work through the argument step by step with a concrete table of decimal expansions. Explicitly construct d and verify it is not on the list. Then discuss implications: there are infinitely many levels of infinity. Contrast with the countability of ℚ to emphasize how different ℝ is.

## Common Misconceptions
- Thinking the constructed number d could appear somewhere else on the list — d was built precisely to differ from every listed element.
- Worrying about decimal ambiguity (e.g., 0.999… = 1.000…) — this is handled by using digits 1 and 2 only, avoiding nines and zeros.
- Assuming the argument only works for real numbers — it generalizes to any power set.

## Explainer

From cardinality and countability, you know that two sets have the same cardinality when there exists a bijection between them, and that a set is **countable** when it can be placed in bijection with the natural numbers ℕ — equivalently, when its elements can be listed in a sequence r₁, r₂, r₃, …. Cantor's diagonalization argument proves that the real numbers in [0,1] cannot be listed this way. The proof proceeds by contradiction and by construction: assume you *have* a complete list, then construct a number that isn't on it.

Here is the argument made concrete. Suppose, for contradiction, that [0,1] is countable and we have a list: r₁ = 0.a₁₁a₁₂a₁₃…, r₂ = 0.a₂₁a₂₂a₂₃…, r₃ = 0.a₃₁a₃₂a₃₃…, and so on, where aᵢⱼ denotes the j-th decimal digit of the i-th number. Now construct a new real number d by reading down the **diagonal** — the entries a₁₁, a₂₂, a₃₃, … — and changing each digit: if aₙₙ = 1, set the n-th digit of d to 2; otherwise set it to 1. The resulting d is a real number in [0,1]. But d ≠ r₁ because they differ in the 1st digit. And d ≠ r₂ because they differ in the 2nd digit. In general, d ≠ rₙ because they differ in the n-th digit. So d is not on the list — contradicting the assumption that the list was complete.

The proof-by-contradiction structure is the same one you've practiced before. What makes diagonalization special is the *mechanism* of construction: instead of guessing a missing element, you systematically ensure the new element differs from every listed element at a specific, designated position. The diagonal position aₙₙ is the clever choice — it's the one position where the construction can target rₙ without interfering with the distinctions already made from r₁, …, rₙ₋₁. Using only digits 1 and 2 sidesteps the decimal ambiguity (0.999… = 1.000…) that would otherwise undermine the argument.

The same idea generalizes far beyond real numbers. For *any* set A, define a function f: A → {0,1}^A (the set of all binary-valued functions on A). Cantor's theorem says no such f can be surjective: given any f, define g(a) = 1 − f(a)(a) — a function that differs from f(a) on the input a, for every a. This is diagonalization in its abstract form, and it proves that **P(A)** — the power set of A — has strictly larger cardinality than A itself. Since you can apply this to ℕ, to P(ℕ), to P(P(ℕ)), and so on indefinitely, there is no largest infinity. The diagonalization argument is the engine behind the entire hierarchy of infinite cardinalities.
