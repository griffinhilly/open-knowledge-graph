---
id: converse-inverse-contrapositive
title: Converse, Inverse, and Contrapositive
domain: mathematics
course: methods-of-proof
prerequisites:
- id: conditional-implication-statements
  type: hard
builds-toward:
- proving-by-contrapositive
- modus-ponens-and-modus-tollens
tags:
- logic
- conditional
- converse
- contrapositive
stage: formal-systems
status: draft
---

# Converse, Inverse, and Contrapositive

## Core Idea
Given a conditional P → Q: the converse is Q → P (not logically equivalent), the inverse is ¬P → ¬Q (not equivalent), and the contrapositive is ¬Q → ¬P (logically equivalent to the original). Understanding these relationships is crucial for proof techniques.

## How It's Best Learned
Use truth tables to verify that contrapositive is equivalent while converse and inverse are not. Practice converting conditionals to their contrapositives.

## Common Misconceptions
- Thinking converse and contrapositive are the same.
- Assuming the converse of a true statement is true.
- Forgetting that contrapositive is logically equivalent to the original.

## Explainer

You've learned that a **conditional statement** P → Q ("if P, then Q") is the backbone of mathematical reasoning. Now you need to handle three related but distinct statements built from the same P and Q — and critically, understand which ones are logically equivalent to the original. Confusing these is one of the most common sources of invalid proofs, so getting this right is foundational to everything that follows.

Given P → Q, the three variants are: the **converse** Q → P (reverse the arrow), the **inverse** ¬P → ¬Q (negate both sides), and the **contrapositive** ¬Q → ¬P (reverse *and* negate). A truth table confirms the pivotal fact: the contrapositive is logically equivalent to the original — they share the same truth value under every assignment of truth values to P and Q. The converse and inverse are equivalent to *each other*, but neither is equivalent to the original.

A concrete example makes this vivid. Let P = "it is raining" and Q = "the ground is wet." Then P → Q = "if it rains, the ground is wet." The contrapositive is "if the ground is not wet, then it is not raining" — equally valid, because dry ground conclusively rules out rain. But the converse "if the ground is wet, then it rained" is a different claim: sprinklers could have run. The inverse "if it didn't rain, the ground isn't wet" is equally suspect. Converse and inverse make an independent claim about the world; the contrapositive is simply a restatement of the original.

The practical payoff is **proof technique**. To prove P → Q, you may equally prove its contrapositive ¬Q → ¬P — because they are logically identical. This substitution is valid. Substituting the converse is not. The contrapositive is especially useful when the negation of Q is a cleaner starting hypothesis than P itself. For example, "if n² is even, then n is even" is easier to prove via its contrapositive: "if n is odd, then n² is odd," which reduces to a direct calculation (n = 2k+1 gives n² = 4k²+4k+1, which is odd). Always check: is the contrapositive easier to work with than the original direction?
