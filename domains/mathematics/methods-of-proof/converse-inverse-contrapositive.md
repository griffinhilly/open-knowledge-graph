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
status: validated
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

## Questions

```yaml
- question: "Given P → Q ('If it rains, the ground gets wet'), which of the following is logically equivalent to the original conditional?"
  type: multiple-choice
  options:
    - "Q → P (If the ground is wet, it rained)"
    - "¬P → ¬Q (If it didn't rain, the ground isn't wet)"
    - "¬Q → ¬P (If the ground isn't wet, it didn't rain)"
    - "¬P → Q (If it didn't rain, the ground is still wet)"
  answer: 2
  explanation: "The contrapositive ¬Q → ¬P is the only form logically equivalent to P → Q — they have identical truth values under every assignment. Option A is the converse and option B is the inverse; these are equivalent to each other but not to the original. The contrapositive merely reverses and negates both sides simultaneously, which preserves the logical content exactly."

- question: "A mathematician wants to prove 'If n² is even, then n is even' but finds it easier to work with the negation of the conclusion. Which substitution is logically valid?"
  type: multiple-choice
  options:
    - "Prove 'If n is even, then n² is even' — the converse, which is equivalent"
    - "Prove 'If n is odd, then n² is odd' — the contrapositive, which is equivalent"
    - "Prove 'If n² is odd, then n is even' — by negating only the hypothesis"
    - "Either the converse or the contrapositive — both are equivalent to the original"
  answer: 1
  explanation: "The contrapositive ('If n is odd, then n² is odd') is logically equivalent to the original, so proving it proves the original. This is a direct application of proof by contrapositive. The converse ('If n is even, then n² is even') is actually true here, but that's a coincidence of this particular statement — it is not equivalent in general. Option D is wrong because the converse is not equivalent to the original."

- question: "The converse and contrapositive of a conditional statement are logically equivalent to each other."
  type: true-false
  answer: false
  explanation: "The contrapositive (¬Q → ¬P) is logically equivalent to the original (P → Q). The converse (Q → P) is logically equivalent to the inverse (¬P → ¬Q). Converse and contrapositive are NOT equivalent to each other — they are equivalent to different things. Confusing these is one of the most common sources of invalid proofs."

- question: "If P → Q is false, then its contrapositive ¬Q → ¬P must also be false."
  type: true-false
  answer: true
  explanation: "The contrapositive is logically equivalent to the original — they have the same truth value in every possible scenario. If P → Q is false (P is true but Q is false), then substituting into the contrapositive: Q is false so ¬Q is true, and P is true so ¬P is false — making ¬Q → ¬P also false. They are not just 'related'; they are the same logical statement written differently."

- question: "Why is substituting the contrapositive valid in a proof, while substituting the converse is not?"
  type: short-answer
  answer: "The contrapositive (¬Q → ¬P) is logically equivalent to the original (P → Q) — they are true under exactly the same conditions. Proving one proves the other. The converse (Q → P) makes a different claim about the world; it may be true when the original is false, or false when the original is true. Substituting the converse would prove a different statement, not the one you set out to prove."
  explanation: "Logical equivalence is the key concept: two statements are equivalent if they always have the same truth value, regardless of what P and Q mean. Truth tables confirm that P → Q and ¬Q → ¬P share a truth column; P → Q and Q → P do not. This equivalence is what licenses the substitution in proof by contrapositive — you are not making an assumption, you are exploiting an identity."
```

## Explainer

You've learned that a **conditional statement** P → Q ("if P, then Q") is the backbone of mathematical reasoning. Now you need to handle three related but distinct statements built from the same P and Q — and critically, understand which ones are logically equivalent to the original. Confusing these is one of the most common sources of invalid proofs, so getting this right is foundational to everything that follows.

Given P → Q, the three variants are: the **converse** Q → P (reverse the arrow), the **inverse** ¬P → ¬Q (negate both sides), and the **contrapositive** ¬Q → ¬P (reverse *and* negate). A truth table confirms the pivotal fact: the contrapositive is logically equivalent to the original — they share the same truth value under every assignment of truth values to P and Q. The converse and inverse are equivalent to *each other*, but neither is equivalent to the original.

A concrete example makes this vivid. Let P = "it is raining" and Q = "the ground is wet." Then P → Q = "if it rains, the ground is wet." The contrapositive is "if the ground is not wet, then it is not raining" — equally valid, because dry ground conclusively rules out rain. But the converse "if the ground is wet, then it rained" is a different claim: sprinklers could have run. The inverse "if it didn't rain, the ground isn't wet" is equally suspect. Converse and inverse make an independent claim about the world; the contrapositive is simply a restatement of the original.

The practical payoff is **proof technique**. To prove P → Q, you may equally prove its contrapositive ¬Q → ¬P — because they are logically identical. This substitution is valid. Substituting the converse is not. The contrapositive is especially useful when the negation of Q is a cleaner starting hypothesis than P itself. For example, "if n² is even, then n is even" is easier to prove via its contrapositive: "if n is odd, then n² is odd," which reduces to a direct calculation (n = 2k+1 gives n² = 4k²+4k+1, which is odd). Always check: is the contrapositive easier to work with than the original direction?
