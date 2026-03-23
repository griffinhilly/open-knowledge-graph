---
id: proving-by-contrapositive
title: Proving by Contrapositive
domain: mathematics
course: methods-of-proof
prerequisites:
- id: converse-inverse-contrapositive
  type: hard
- id: proving-by-direct-method
  type: hard
builds-toward:
- proving-by-contradiction
tags:
- proof
- contrapositive
- indirect proof
stage: formal-systems
status: validated
---

# Proving by Contrapositive

## Core Idea
To prove P → Q, prove the contrapositive ¬Q → ¬P instead. Since P → Q is logically equivalent to ¬Q → ¬P, proving one proves the other. This method is useful when the contrapositive is easier to establish than the original statement.

## How It's Best Learned
Identify when the contrapositive is simpler to work with. Practice finding and proving contrapositives of various statements.

## Common Misconceptions
- Confusing contrapositive proof with converse proof (converse is not equivalent).
- Proving the converse instead of the contrapositive.
- Forgetting that the contrapositive is logically equivalent.

## Questions

```yaml
- question: "To prove 'If n is even, then n² is even,' a student instead proves 'If n² is odd, then n is odd.' Has she proven the original statement?"
  type: multiple-choice
  options:
    - "No — she has proven the converse, which is not logically equivalent to the original"
    - "Yes — she has proven the contrapositive, which is logically equivalent to the original"
    - "No — she must prove both the statement and its contrapositive to establish the original"
    - "Yes — she has proven the inverse, which is equivalent to the original"
  answer: 1
  explanation: "She has proven 'If n² is odd, then n is odd,' which is the contrapositive of the original. The contrapositive of P → Q is ¬Q → ¬P — here, negating 'n² is even' gives 'n² is odd' and negating 'n is even' gives 'n is odd.' Since the contrapositive is logically equivalent to the original (same truth table), proving one proves the other. You do not need to prove both."

- question: "A student needs to prove 'If 3n + 2 is odd, then n is odd.' She finds the direct approach awkward. She writes the contrapositive as 'If n is odd, then 3n + 2 is odd.' Is this correct, and why or why not?"
  type: multiple-choice
  options:
    - "Yes — she swapped the two parts of the conditional, which is the contrapositive"
    - "No — she wrote the converse (swapping without negating); the correct contrapositive is 'If n is even, then 3n + 2 is even'"
    - "Yes — the contrapositive just requires negating the conclusion, which she did"
    - "No — the contrapositive requires negating only the hypothesis, giving 'If n is not odd, then 3n + 2 is odd'"
  answer: 1
  explanation: "She wrote the converse (Q → P), not the contrapositive (¬Q → ¬P). The contrapositive of 'If 3n+2 is odd, then n is odd' requires negating both parts and swapping: 'If n is even (¬'n is odd'), then 3n+2 is even (¬'3n+2 is odd').' This version is easy to prove directly: n = 2k gives 3n+2 = 6k+2 = 2(3k+1), which is even. The converse is not equivalent to the original and proves nothing about it."

- question: "Proving the contrapositive ¬Q → ¬P is a valid way to establish P → Q because the two conditionals are logically equivalent — they have the same truth table."
  type: true-false
  answer: true
  explanation: "This is exact, not approximate. P → Q and ¬Q → ¬P are both false only when P is true and Q is false. In all other cases both are true. This complete equivalence is the entire justification for contrapositive proof — you are not approximating or using a shortcut; you are proving the same logical claim in an equivalent form."

- question: "Proving the converse (Q → P) of a statement is a valid way to establish the original statement (P → Q), just like proving the contrapositive."
  type: true-false
  answer: false
  explanation: "The converse Q → P is NOT logically equivalent to P → Q. They can have different truth values: 'If it is a square, then it is a rectangle' is true, but its converse 'If it is a rectangle, then it is a square' is false. By contrast, the contrapositive ¬Q → ¬P is always logically equivalent to P → Q. The converse and contrapositive look superficially similar — both swap the two parts — but the contrapositive negates both parts, and that negation is everything."

- question: "Why would a mathematician choose to prove a statement by contrapositive rather than directly, and what makes this choice logically valid?"
  type: short-answer
  answer: "A mathematician chooses the contrapositive when assuming ¬Q (the negation of the conclusion) is more useful than assuming P (the original hypothesis). For example, proving 'if n² is even, then n is even' is awkward directly, but the contrapositive 'if n is odd, then n² is odd' immediately gives n = 2k+1, which is easy to square. The choice is valid because the contrapositive is logically equivalent to the original — proving one proves the other without any loss."
  explanation: "The strategic question is always: which hypothesis gives me more to work with? If the conclusion's negation (¬Q) leads more naturally to the hypothesis's negation (¬P) than P leads to Q, contrapositive proof is the cleaner path. The key check before starting: make sure you have written ¬Q → ¬P and not the converse Q → P. Both swap the parts, but only the contrapositive negates them."
```

## Explainer

You already know the logical relationships between a conditional and its transformations: the **contrapositive** of "P → Q" is "¬Q → ¬P", and crucially, these two are logically equivalent — they have exactly the same truth table. That equivalence is the entire engine behind contrapositive proof. If you can prove ¬Q → ¬P by any method (direct proof works well here), then P → Q is automatically proven as well. You are not using a trick or an approximation; you are proving the exact same statement in a different but equivalent form.

The strategic value of contrapositive proof is that the contrapositive is often easier to work with directly. Consider: "If n² is even, then n is even." Proving this directly requires reasoning about what makes a perfect square even, which is awkward. The contrapositive is: "If n is odd, then n² is odd." This is straightforward: if n is odd then n = 2k + 1 for some integer k, so n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, which is odd. Done. The contrapositive version required almost no creativity beyond substitution — the hypothesis gave us exactly what we needed in a usable form.

The process is always the same three steps: (1) identify the contrapositive ¬Q → ¬P, (2) assume ¬Q (the negation of the conclusion), and (3) prove ¬P (the negation of the hypothesis) by direct reasoning. Notice that in step 2 you *assume* the negation of what you want to conclude in the original statement, and in step 3 you *prove* the negation of what was originally assumed. The logical flow is inverted and negated relative to a direct proof.

The critical mistake to avoid — which your prerequisites have already flagged — is proving the **converse** Q → P instead of the contrapositive ¬Q → ¬P. The converse is not logically equivalent to P → Q, so proving it establishes nothing about the original. The contrapositive and the converse look superficially similar (both swap P and Q), but the contrapositive negates both, and that negation is everything. When choosing between direct proof and contrapositive proof, ask: which hypothesis is more useful to assume? If assuming ¬Q gives you more to work with than assuming P, choose the contrapositive.
