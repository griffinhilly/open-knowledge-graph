---
id: group-definition-examples
title: Group Definition and Examples
domain: mathematics
course: abstract-algebra
prerequisites:
- id: binary-operations-algebraic-structures
  type: hard
builds-toward:
- group-basic-properties
- permutation-groups
- ring-definition-examples
tags:
- groups
- closure
- associativity
- identity
- inverse
stage: advanced
status: validated
---

# Group Definition and Examples

## Core Idea
A group is a set G with a binary operation satisfying four axioms: closure, associativity, existence of an identity element, and existence of inverses for every element. Groups appear throughout mathematics and physics as the formalization of symmetry.

## Questions

```yaml
- question: "Consider the set of odd integers under ordinary addition. Which group axiom fails?"
  type: multiple-choice
  options:
    - "Associativity — regrouping odd integers changes the sum"
    - "Closure — the sum of two odd integers is even, which is not in the set"
    - "Identity — there is no odd integer that acts as the additive identity"
    - "Inverses — the additive inverse of an odd integer is not odd"
  answer: 1
  explanation: "The sum of any two odd integers is always even (e.g., 3 + 5 = 8), so the set of odd integers is not closed under addition. The result leaves the set, violating closure immediately. Note that options C and D are also technically true (0 is not odd; −3 is odd so inverses exist... wait, −3 is odd), but closure fails first and most directly. Closure is the axiom students most often overlook because it seems obvious — but it must be verified for the specific set, not just the operation."

- question: "Which of the following is a group under its given operation?"
  type: multiple-choice
  options:
    - "(ℤ, ×) — integers under multiplication"
    - "(ℕ, +) — natural numbers {0, 1, 2, ...} under addition"
    - "(ℚ \\ {0}, ×) — nonzero rational numbers under multiplication"
    - "(2ℤ, ×) — even integers under multiplication"
  answer: 2
  explanation: "The nonzero rationals under multiplication satisfy all four axioms: closure (product of two nonzero rationals is a nonzero rational), associativity (inherited from multiplication), identity (1 is a nonzero rational), and inverses (every p/q ≠ 0 has inverse q/p). The others fail: (ℤ, ×) has no inverse for 2 since 1/2 ∉ ℤ; (ℕ, +) has no inverse for 1 since −1 ∉ ℕ; (2ℤ, ×) has no identity since 1 is not even. Whether a structure is a group depends on the combination of set AND operation."

- question: "The identity element in a group is unique — no group can have two different elements that both satisfy the identity axiom."
  type: true-false
  answer: true
  explanation: "This is a provable theorem about groups: suppose e and e′ are both identity elements. Then e = e ∗ e′ (since e′ is an identity) = e′ (since e is an identity). So e = e′. The proof works for any group, no matter what the set or operation is — this is the abstraction payoff. You prove uniqueness once for abstract groups and it immediately applies to all groups: integer addition, rational multiplication, rotations, permutations, and every other example simultaneously."

- question: "Whether a set forms a group depends only on the properties of the set, not on which binary operation is used."
  type: true-false
  answer: false
  explanation: "Both the set and the operation together determine whether a group exists. The integers ℤ form a group under addition (every integer has an additive inverse −n) but not under multiplication (2 has no multiplicative inverse in ℤ). The set is the same; the operation changes everything. This is why the proper notation specifies both: (ℤ, +) is a group, (ℤ, ×) is not. Students who think of 'the integers' as simply being or not being a group are missing half the definition."

- question: "Explain why (ℤ, ×) — the integers under multiplication — fails to be a group. Which axiom is violated, and why does it fail for this particular set-operation pair?"
  type: short-answer
  answer: "The integers under multiplication fail the inverse axiom. The group axiom requires that for every element a in the set, there exists an element a⁻¹ in the same set such that a × a⁻¹ = 1. For a = 2, the multiplicative inverse would need to be 1/2 — but 1/2 is not an integer. The same problem occurs for every integer except 1 and −1 (which are their own inverses). Since most elements lack inverses within ℤ, (ℤ, ×) fails to be a group."
  explanation: "The other axioms do hold: closure (product of two integers is an integer), associativity (always true for multiplication), and identity (1 is the multiplicative identity in ℤ). The failure is specifically and only the inverse axiom. This is why the nonzero rationals (ℚ \\ {0}, ×) form a group while integers do not: the rationals contain all the fractions needed to invert every nonzero element."
```

## Explainer

The concept of a group captures what it means for an operation to be "fully reversible and rearrangeable." You already know from binary operations that combining elements is not always well-behaved — the four group axioms pin down exactly the properties needed to do algebra reliably. **Closure** means the operation stays inside the set. **Associativity** means you can regroup computations: (a ∗ b) ∗ c = a ∗ (b ∗ c). The **identity element** is the "do nothing" element — it leaves everything unchanged. And **inverses** let you undo any move, so no element is a dead end.

Consider integer addition as your first example: you can add any two integers and stay in ℤ (closure); grouping doesn't change the result — (3 + 4) + 5 = 3 + (4 + 5) (associativity); 0 leaves everything unchanged (identity); and every n has −n (inverse). So (ℤ, +) is a group. Now contrast with integer multiplication: 2 has no multiplicative inverse inside ℤ (since 1/2 ∉ ℤ), so (ℤ, ×) is not a group. But (ℚ \ {0}, ×) is. Whether something forms a group depends on both the *set* and the *operation* together.

The power of the group definition is its breadth. The six rotations of an equilateral triangle form a group. The set of all permutations of {1, 2, 3} forms a group under composition. The nonzero real numbers form a group under multiplication. These look completely different, yet they all satisfy the same four axioms. A theorem proved for abstract groups — say, that the identity is unique, or that inverses are unique — automatically applies to all of these at once. This is the abstraction payoff: you prove something once and it lands everywhere.

When working with groups, always verify all four axioms explicitly until intuition develops. Closure is the one most often overlooked: even if the operation is familiar, the *set* might not be closed under it. The even integers under addition are closed; the odd integers are not (odd + odd = even). Groups build toward subgroups, homomorphisms, quotient groups, and ultimately to classifying all possible symmetric structures in mathematics — but the four axioms are the foundation everything rests on.
