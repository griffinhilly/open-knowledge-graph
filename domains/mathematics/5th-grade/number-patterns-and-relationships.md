---
id: number-patterns-and-relationships
title: Number Patterns and Relationships
domain: mathematics
course: 5th-grade
prerequisites:
- id: patterns-and-sequences
  type: hard
- id: input-output-tables
  type: hard
- id: plotting-ordered-pairs
  type: soft
- id: arithmetic-patterns-3rd
  type: soft
builds-toward: []
tags:
- algebra-readiness
- patterns
- relationships
- graphing
stage: concrete-operations
status: validated
---
# Number Patterns and Relationships

## Core Idea
In fifth grade, students analyze two related number patterns simultaneously and identify the relationship between them. Given the rule "add 3" starting from 0 and the rule "add 6" starting from 0, the sequences are (0, 3, 6, 9, 12) and (0, 6, 12, 18, 24). Students observe that each term in the second sequence is twice the corresponding term in the first. They form ordered pairs from corresponding terms -- (0,0), (3,6), (6,12), (9,18), (12,24) -- and plot them on the coordinate plane, discovering they form a straight line. This is the earliest encounter with the idea that a relationship between two quantities can be expressed as a rule and visualized as a graph.

## How It's Best Learned
Generate paired sequences from two rules, record in a two-column table, then plot as ordered pairs. Ask students to describe the relationship between the paired values. Use real-world contexts: "If you earn $3 per hour and your friend earns $6 per hour, how do your total earnings compare after 1, 2, 3, 4, 5 hours?" Observe that the plotted points form a line.

## Common Misconceptions
- Confusing the relationship within a sequence (add 3 each time) with the relationship between sequences (one is double the other).
- Not forming ordered pairs from corresponding terms (mispairing terms).
- Difficulty articulating the relationship in words ("the second number is always twice the first").

## Questions

```yaml
- question: "Sequence A uses 'add 4' starting from 0: (0, 4, 8, 12, 16). Sequence B uses 'add 8' starting from 0: (0, 8, 16, 24, 32). What is the relationship between corresponding terms?"
  type: multiple-choice
  options:
    - "Each term in Sequence B is 4 more than the corresponding term in Sequence A"
    - "Each term in Sequence B is twice the corresponding term in Sequence A"
    - "There is no consistent relationship — it changes at different term positions"
    - "Each term in Sequence A is twice the corresponding term in Sequence B"
  answer: 1
  explanation: "At every position: 8 = 2×4, 16 = 2×8, 24 = 2×12, 32 = 2×16. The multiplicative relationship is constant because Sequence B's rule (add 8) is exactly double Sequence A's rule (add 4). The relationship between the rules determines the relationship between corresponding outputs. Option A is the common confusion — adding 4 describes the pattern *within* Sequence A, not the relationship *between* sequences."

- question: "You pair corresponding terms from two sequences — 'add 3' and 'add 6,' both starting at 0 — as ordered pairs: (0,0), (3,6), (6,12), (9,18). When you plot these on a coordinate plane, what do you see?"
  type: multiple-choice
  options:
    - "A curved arc that bends upward"
    - "A zigzag pattern alternating high and low"
    - "A straight line"
    - "A random scatter with no visible pattern"
  answer: 2
  explanation: "When two sequences have a constant ratio between corresponding terms (here, 2:1), the ordered pairs fall on a straight line through the origin. A straight line through (0,0) is the geometric signature of a constant multiplicative relationship. This is the earliest encounter with what will later be called a linear function."

- question: "The relationship between two paired sequences changes depending on which term position you examine — it is not constant."
  type: true-false
  answer: false
  explanation: "When both sequences start at 0 and have constant rules, the ratio between corresponding terms is fixed at every position. If the first rule is 'add 3' and the second is 'add 6,' the second term is always exactly double the first — at position 1 (3 vs. 6), position 2 (6 vs. 12), position 10 (30 vs. 60), and so on. The consistency comes from the constant ratio between the two rules."

- question: "If Sequence A uses 'add 5' and Sequence B uses 'add 10,' each term in Sequence B will always be exactly double the corresponding term in Sequence A."
  type: true-false
  answer: true
  explanation: "Since 10 = 2 × 5, Sequence B adds twice as much per step as Sequence A. Starting both from 0: Sequence A is 0, 5, 10, 15, 20... and Sequence B is 0, 10, 20, 30, 40... Each term in B is exactly double the corresponding term in A. The multiplicative relationship between the rules is preserved in every pair of corresponding terms."

- question: "Explain why the relationship between two paired sequences depends on the rules that generated them, not just on a few specific terms."
  type: short-answer
  answer: "Each sequence grows by adding a fixed amount per step. If one rule adds twice as much as the other, the outputs will always be in a 2:1 ratio — not by coincidence at one step, but consistently at every step. The relationship is built into the rules, so it holds for all corresponding pairs, and is why plotting the pairs produces a straight line."
  explanation: "Students who check only one or two pairs might think the relationship could be different elsewhere. But because both rules operate at a constant rate from the same starting point, the ratio between corresponding terms equals the ratio between the rules — permanently. This is what makes the relationship predictable enough to graph as a line."
```

## Explainer

You've worked with sequences before — rules like "add 3" that generate a chain of numbers (0, 3, 6, 9, ...). You've also used input-output tables to track how one quantity changes with another, and you've plotted ordered pairs on a coordinate grid. This topic brings all three together: when you run two sequences side by side and pair their corresponding terms, you're creating a **relationship between two quantities** that you can describe, tabulate, and graph all at once.

Start with two rules: "add 3" and "add 6," both beginning from 0. The first sequence is 0, 3, 6, 9, 12... and the second is 0, 6, 12, 18, 24... Line them up in a table — the first pair of corresponding terms is (3, 6), the second is (6, 12), the third is (9, 18). Look across each row: the second number is always exactly double the first. That doubling relationship isn't a coincidence — it comes from the fact that the second rule adds twice as much per step as the first rule does. The relationship between the outputs mirrors the relationship between the rules that generated them.

When you plot those ordered pairs on a coordinate plane — (0, 0), (3, 6), (6, 12), (9, 18), (12, 24) — they fall in a straight line. This is the geometric signature of a **constant ratio between two quantities**: every time the first quantity increases by a fixed amount, the second increases by a fixed amount too. A straight line through the origin (0, 0) means both sequences started at 0 with a fixed multiplicative relationship between their rules. If the second rule were "add 6" but started at a different value, the points would still be collinear — but the line wouldn't pass through the origin.

This is the earliest form of **algebraic thinking**: the idea that a rule connecting two quantities can be described in words ("the second is always double the first"), captured as specific pairs in a table, and seen as a geometric pattern on a graph. These three representations — rule, table, graph — all encode the same underlying relationship. When you study functions in later courses, you'll express the same idea with an equation like y = 2x, and you'll work with all three representations again in much greater depth. The foundation being built here is learning to move fluidly between them and recognizing that the pattern is the same thing no matter which form it appears in.
