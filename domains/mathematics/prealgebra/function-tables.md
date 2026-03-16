---
id: function-tables
title: Function Tables and Rules
domain: mathematics
course: prealgebra
prerequisites:
  - id: variable-expressions
    type: hard
  - id: integer-order-of-operations
    type: hard
builds-toward:
  - graphing-linear-equations
  - slope-concept
  - arithmetic-sequences
tags: [functions, tables, patterns, input-output]
stage: abstract-reasoning
status: validated
---

# Input-Output Tables and Function Rules

## Core Idea
An input-output table shows pairs of values where each input is transformed by a rule to produce an output. If the rule is "multiply by 3 and add 1," the table for inputs 1, 2, 3 gives outputs 4, 7, 10. Recognizing the rule from a table — and generating new outputs from new inputs — is an early form of functional thinking. Input-output tables are the precursor to function notation, graphing equations, and understanding linear relationships. They train students to see patterns and express them symbolically.

## How It's Best Learned
Give tables with the rule hidden and ask students to discover it. Start with one-operation rules, then two-operation rules. Have students both complete tables given a rule and find the rule given a table. Connect to the coordinate plane by plotting input-output pairs as points — they will see the points form a line for linear rules.

## Common Misconceptions
- Finding a rule that works for the first pair but not the rest (checking only one pair).
- Confusing additive patterns with multiplicative ones (seeing +3 when the rule is ×2 + 1).
- Not expressing the rule algebraically — staying with verbal descriptions when a formula is expected.

## Explainer

You already know how to evaluate variable expressions: substitute a number for the variable, then apply the order of operations. A function table is exactly this process organized systematically. The input column lists values going into the expression; the output column shows the results. If the rule is 3x + 1, then input 2 gives output 7, input 5 gives output 16, and so on. Every row is one substitution. The table makes the pattern visible by laying out many substitutions side by side.

The more powerful skill is the reverse: given a completed table, find the rule. Start by examining how the outputs change as the inputs increase by 1. If consecutive outputs differ by a constant amount — say every time the input goes up by 1, the output goes up by 3 — the relationship is **linear**, meaning the rule has the form mx + b. For example, if inputs 1, 2, 3 give outputs 5, 8, 11, consecutive outputs grow by 3, so the multiplier m = 3. Then check one specific pair: 3 × 1 = 3, but the output is 5, so b = 2. The rule is 3x + 2. This two-step algorithm — find the multiplier from the constant difference, find the constant by checking any pair — handles all linear rules.

Not every table is linear. If the differences between consecutive outputs are not constant, look deeper. A pattern of differences that is itself constant suggests a **quadratic** rule. Constant ratios between outputs suggest an **exponential** rule. Outputs that are perfect squares suggest squaring the input. Whatever your guess, the discipline is the same: verify the rule against every row in the table, not just the first one. A rule that works for one pair by coincidence but fails the rest is not the rule. This same intellectual standard — a rule must be consistent, not merely plausible — appears throughout all of algebra.

The connection to graphing is direct. Each row of a function table is a coordinate pair: (input, output) = (x, y). When you plot these pairs on a coordinate plane, linear rules produce straight lines, quadratic rules produce parabolas, and exponential rules produce curves. Function tables are not a detour on the way to graphing — they are the foundation. A graph is nothing more than infinitely many table rows plotted simultaneously. Building intuition about rules from tables now makes the connection between equations and their graphs transparent when you encounter it in the next course.
