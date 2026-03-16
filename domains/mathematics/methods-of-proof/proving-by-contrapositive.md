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
status: draft
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

## Explainer

You already know the logical relationships between a conditional and its transformations: the **contrapositive** of "P → Q" is "¬Q → ¬P", and crucially, these two are logically equivalent — they have exactly the same truth table. That equivalence is the entire engine behind contrapositive proof. If you can prove ¬Q → ¬P by any method (direct proof works well here), then P → Q is automatically proven as well. You are not using a trick or an approximation; you are proving the exact same statement in a different but equivalent form.

The strategic value of contrapositive proof is that the contrapositive is often easier to work with directly. Consider: "If n² is even, then n is even." Proving this directly requires reasoning about what makes a perfect square even, which is awkward. The contrapositive is: "If n is odd, then n² is odd." This is straightforward: if n is odd then n = 2k + 1 for some integer k, so n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, which is odd. Done. The contrapositive version required almost no creativity beyond substitution — the hypothesis gave us exactly what we needed in a usable form.

The process is always the same three steps: (1) identify the contrapositive ¬Q → ¬P, (2) assume ¬Q (the negation of the conclusion), and (3) prove ¬P (the negation of the hypothesis) by direct reasoning. Notice that in step 2 you *assume* the negation of what you want to conclude in the original statement, and in step 3 you *prove* the negation of what was originally assumed. The logical flow is inverted and negated relative to a direct proof.

The critical mistake to avoid — which your prerequisites have already flagged — is proving the **converse** Q → P instead of the contrapositive ¬Q → ¬P. The converse is not logically equivalent to P → Q, so proving it establishes nothing about the original. The contrapositive and the converse look superficially similar (both swap P and Q), but the contrapositive negates both, and that negation is everything. When choosing between direct proof and contrapositive proof, ask: which hypothesis is more useful to assume? If assuming ¬Q gives you more to work with than assuming P, choose the contrapositive.
