---
id: patterns-and-sequences
title: Patterns and Sequences
domain: mathematics
course: 4th-grade
prerequisites:
- id: multi-digit-addition
  type: soft
- id: multi-digit-multiplication
  type: soft
- id: input-output-tables
  type: soft
builds-toward:
- number-patterns-and-relationships
- writing-numerical-expressions
tags:
- algebra-readiness
- patterns
- sequences
stage: concrete-operations
status: validated
---
# Patterns and Sequences

## Core Idea
A pattern is a regularity that allows prediction. Number patterns (sequences) follow a rule: in the sequence 3, 7, 11, 15, 19, the rule is "add 4." Students learn to identify the rule, extend the sequence, and find specific terms. They also work with shape patterns that grow according to a rule (each figure adds 3 tiles). Recognizing patterns is a core mathematical habit of mind and the foundation of algebraic thinking -- eventually, the rule "start at 3 and add 4" becomes the expression 4n - 1.

## How It's Best Learned
Use visual patterns (tile arrangements, dot arrays) alongside number sequences so students see the structure, not just the arithmetic. Ask students to describe patterns in their own words before formalizing. Practice both extending patterns forward and filling in missing terms. Include patterns with different operations (add, subtract, multiply) and growing shape patterns.

## Common Misconceptions
- Assuming all patterns are "add a constant" (arithmetic sequences) and not recognizing multiplicative or alternating patterns.
- Correctly identifying the pattern for the first few terms but miscounting when extending further.
- Describing only what changes without stating the starting point (the rule "add 3" is incomplete without knowing the first term).

## Questions

```yaml
- question: "A student says the rule for a sequence is 'add 4.' She uses this rule to write: 4, 8, 12, 16... Her classmate uses the same rule to write: 1, 5, 9, 13... Who is right?"
  type: multiple-choice
  options:
    - "The first student — 'add 4' must start at 4"
    - "The second student — 'add 4' must start at 1"
    - "Both are right — 'add 4' is an incomplete rule without a starting value, so both sequences are valid"
    - "Neither — a rule must describe a multiplicative pattern to be valid"
  answer: 2
  explanation: "A rule like 'add 4' describes only the common difference — how the sequence grows. Without knowing the starting value, infinitely many different sequences all follow the rule 'add 4.' Both sequences shown are valid arithmetic sequences with common difference 4, just starting at different values. A complete rule for an arithmetic sequence requires BOTH the starting value and the common difference."

- question: "In the sequence 2, 6, 18, 54, 162, a student claims the rule is 'add 4 each time.' What error has she made?"
  type: multiple-choice
  options:
    - "She identified the wrong starting value — it should start at 0"
    - "She assumed the pattern was additive when it is actually multiplicative — each term is multiplied by 3"
    - "She is correct; 2 + 4 = 6 so the rule works for the first step"
    - "She should have said 'add 16' because the gap between 2 and 18 is 16"
  answer: 1
  explanation: "The gaps between consecutive terms are 4, 12, 36, 108 — widening each time, not staying constant. This is the signature of a multiplicative pattern: 2×3=6, 6×3=18, 18×3=54. An additive pattern ('add a constant') has equal gaps; a multiplicative pattern has gaps that themselves grow by a constant ratio. Assuming all patterns are arithmetic (add a constant) is the most common pattern-recognition error."

- question: "To find the 20th term of an arithmetic sequence, you must first list all 19 terms before it."
  type: true-false
  answer: false
  explanation: "False. Once you know the starting value and the common difference, you can jump directly to any term. The 20th term equals the starting value plus 19 times the common difference (you add the difference 19 times to get from term 1 to term 20). For the sequence 3, 7, 11, 15... the 20th term is 3 + 19×4 = 79. This 'jump to any term' property is what makes pattern rules powerful — and it is the core idea behind algebraic expressions."

- question: "A pattern's rule is fully described by its common difference alone (e.g., 'add 5' is a complete description of an arithmetic sequence)."
  type: true-false
  answer: false
  explanation: "False. 'Add 5' tells you how the sequence grows but not where it starts. The sequences 1, 6, 11, 16... and 3, 8, 13, 18... and 100, 105, 110... all follow 'add 5' but are completely different sequences. A complete description requires both the starting value and the common difference. This becomes especially important when using the rule to find specific terms."

- question: "A student says the rule for a pattern is 'add 3.' Why is this description incomplete, and what additional information is needed to fully define the sequence?"
  type: short-answer
  answer: "The description is incomplete because 'add 3' only specifies the common difference — how much the sequence grows at each step. Without a starting value, infinitely many different sequences all follow this rule (e.g., 1, 4, 7, 10... and 2, 5, 8, 11... and 10, 13, 16, 19...). To fully define the sequence, you also need the first term (the starting value). Together, 'start at 2, add 3 each time' is a complete rule."
  explanation: "The need for two pieces of information — starting value and common difference — mirrors what you will later learn about linear equations (which have both a y-intercept and a slope). A rule with only one piece is ambiguous; it describes a family of sequences rather than one specific sequence."
```

## Explainer

A **pattern** is a regularity — a structure that repeats or grows in a predictable way. In mathematics, patterns are not decorative; they are the first sign of a rule waiting to be discovered. When you see 3, 7, 11, 15, 19, you can feel the rhythm: something keeps getting added. The skill being built here is not just spotting that rhythm, but naming the rule precisely enough to continue the sequence indefinitely — or to find any term without listing all the ones before it.

The most common type at this level is an **arithmetic sequence**, where a constant amount is added (or subtracted) each time. The rule has two components: the **starting value** and the **common difference**. For 3, 7, 11, 15, 19..., the starting value is 3 and the rule is "add 4." Both parts are necessary. "Add 4" alone tells you how the sequence grows but not where it begins — you could start at 1, 6, or 100 and get completely different sequences. Your prior work with multi-digit addition and multiplication helps you both identify the difference and compute future terms quickly.

**Multiplicative patterns** are also important: in 2, 6, 18, 54, each term is multiplied by 3. These grow much faster than additive patterns and feel different — the gaps between terms widen. Your multiplication skills let you check these patterns by dividing consecutive terms to find the common ratio. Visual or **growing patterns** — tile arrangements where each figure adds a fixed number of tiles — connect the numeric rule to a spatial structure. Seeing that the 10th figure has (starting tiles) + 9 × (tiles added per step) is the first step toward writing expressions like 4n + 1.

This topic is labeled "algebra-readiness" for good reason. Recognizing that a pattern has a rule, and that the rule lets you compute distant terms without listing every step, is the core insight of algebra. Your prerequisite skill with input-output tables already introduced the idea of a rule that transforms one number into another. Patterns and sequences extend that to sequences in time: term 1, term 2, term 3... each position feeds into the rule. When you get to writing numerical expressions, you will formalize rules like "start at 3 and add 4" as 4n − 1 — and that expression will feel like a natural translation of something you already understand intuitively.
