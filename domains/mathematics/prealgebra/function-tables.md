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

## Questions

```yaml
- question: "A function table shows inputs 1, 2, 3, 4 and outputs 5, 8, 11, 14. A student checks only the first row and concludes the rule is 'output = input + 4.' What is wrong with this approach?"
  type: multiple-choice
  options:
    - "The rule should always involve multiplication rather than addition"
    - "The student should have checked the last row instead of the first"
    - "The rule works for (1, 5) but fails for (2, 8): 2 + 4 = 6, not 8. A rule must be verified against every row in the table"
    - "Addition rules cannot produce outputs greater than 10"
  answer: 2
  explanation: "Checking only one pair is the most common error in finding function rules. The input-output pair (1, 5) satisfies many rules — output = input + 4, output = 5, output = 5 × input, output = input² + 4, etc. The discipline of verifying against all rows eliminates coincidental matches. The correct rule here is y = 3x + 2: the constant difference between consecutive outputs is 3 (linear), and checking (1,5): 3(1) + 2 = 5 ✓, (2,8): 3(2) + 2 = 8 ✓. Always check every row."

- question: "A table shows inputs 1, 2, 3, 4 with outputs 3, 9, 27, 81. How can you tell this is NOT a linear rule, and what is the correct rule?"
  type: multiple-choice
  options:
    - "The rule is y = 3x because outputs are always multiples of 3; linear rules have outputs that are multiples of the multiplier"
    - "The rule is y = 3^x because consecutive outputs have a constant ratio of 3 (not a constant difference), which indicates exponential growth"
    - "The rule is y = x³ because the outputs 3, 9, 27, 81 are cubes of 3"
    - "The rule is y = x + 2 because the differences are constant at 6, 18, 54"
  answer: 1
  explanation: "Linear rules have a constant *difference* between consecutive outputs (e.g., +3, +3, +3...). Exponential rules have a constant *ratio* (e.g., ×3, ×3, ×3...). Here: 9/3 = 3, 27/9 = 3, 81/27 = 3 — constant ratio of 3, so the rule is y = 3^x. The misconception in option A is confusing 'multiples of 3' with linear growth; y = 3x would give 3, 6, 9, 12 (constant difference of 3), not 3, 9, 27, 81."

- question: "Each row in a function table corresponds to a coordinate pair (input, output) = (x, y), and plotting all such pairs produces the graph of the rule."
  type: true-false
  answer: true
  explanation: "This connection is direct and important: function tables and graphs are two representations of the same relationship. Each table row is one point on the graph. Linear rules (constant difference) plot as straight lines; exponential rules plot as curves; quadratic rules plot as parabolas. Understanding this equivalence means that learning to read tables now directly builds the intuition needed for graphing equations in the next course."

- question: "If a rule correctly predicts the output for the first input-output pair in a table, it is the correct rule for the entire table."
  type: true-false
  answer: false
  explanation: "Many different rules can produce the correct output for a single input. For example, given (2, 8), the rule could be y = 4x, y = x³, y = x + 6, y = 2x + 4, or infinitely many others. The correct rule must work for every row. This is not just a procedural check — it reflects the underlying concept: a function rule is a relationship that holds universally for all inputs, not a coincidence that happens to work once."

- question: "How would you find the rule for a linear function table, and why must you verify the rule against every row rather than stopping after the first match?"
  type: short-answer
  answer: "To find a linear rule: (1) Calculate the difference between consecutive outputs. If the differences are constant, the multiplier (slope) equals that constant difference. (2) Use one input-output pair to find the constant: multiply the input by the slope and compare to the output; the difference is the constant term. This gives the rule y = mx + b. You must verify against every row because any single pair is consistent with infinitely many rules. The correct rule is the one that describes the universal pattern — a relationship that holds for all inputs — not just a coincidence that works for one. A rule that fails any row is not the rule."
  explanation: "The two-step algorithm (constant difference → slope, then one pair → constant) is the systematic method for linear rules. The verification requirement is an instance of a broader mathematical discipline: a proposed rule is only valid when it passes all tests, not just selected ones. This same standard applies throughout algebra — a solution to an equation must satisfy the equation, not just look plausible."
```

## Explainer

You already know how to evaluate variable expressions: substitute a number for the variable, then apply the order of operations. A function table is exactly this process organized systematically. The input column lists values going into the expression; the output column shows the results. If the rule is 3x + 1, then input 2 gives output 7, input 5 gives output 16, and so on. Every row is one substitution. The table makes the pattern visible by laying out many substitutions side by side.

The more powerful skill is the reverse: given a completed table, find the rule. Start by examining how the outputs change as the inputs increase by 1. If consecutive outputs differ by a constant amount — say every time the input goes up by 1, the output goes up by 3 — the relationship is **linear**, meaning the rule has the form mx + b. For example, if inputs 1, 2, 3 give outputs 5, 8, 11, consecutive outputs grow by 3, so the multiplier m = 3. Then check one specific pair: 3 × 1 = 3, but the output is 5, so b = 2. The rule is 3x + 2. This two-step algorithm — find the multiplier from the constant difference, find the constant by checking any pair — handles all linear rules.

Not every table is linear. If the differences between consecutive outputs are not constant, look deeper. A pattern of differences that is itself constant suggests a **quadratic** rule. Constant ratios between outputs suggest an **exponential** rule. Outputs that are perfect squares suggest squaring the input. Whatever your guess, the discipline is the same: verify the rule against every row in the table, not just the first one. A rule that works for one pair by coincidence but fails the rest is not the rule. This same intellectual standard — a rule must be consistent, not merely plausible — appears throughout all of algebra.

The connection to graphing is direct. Each row of a function table is a coordinate pair: (input, output) = (x, y). When you plot these pairs on a coordinate plane, linear rules produce straight lines, quadratic rules produce parabolas, and exponential rules produce curves. Function tables are not a detour on the way to graphing — they are the foundation. A graph is nothing more than infinitely many table rows plotted simultaneously. Building intuition about rules from tables now makes the connection between equations and their graphs transparent when you encounter it in the next course.
