---
id: growing-patterns
title: Growing Patterns
domain: formal-sciences-and-logic
course: patterns-and-logic
prerequisites:
- id: number-patterns-logic
  type: hard
- id: shape-patterns
  type: hard
- id: pattern-rules
  type: soft
- id: patterns-and-sequences
  type: soft
builds-toward:
- sequences-and-series-logic
tags:
- patterns
- growth
- algebra-readiness
- visual
stage: concrete-operations
status: validated
---

# Growing Patterns

## Core Idea
A growing pattern is a sequence where each step is larger than the one before, following a consistent rule. Unlike repeating patterns (which cycle through the same unit), growing patterns build on themselves — each step adds new elements. A staircase that gains one block per step, an L-shape that extends by one tile on each arm, or a number sequence that increases by a fixed amount are all growing patterns. Analyzing how and why a pattern grows connects visual reasoning to numerical reasoning and lays the groundwork for understanding functions.

## How It's Best Learned
Build growing patterns with physical tiles or blocks so students can see each step. Use a table to record the step number and the count of tiles at each step. Ask: "How many tiles were added this step? Is it the same amount each time?" Have students predict the count at step 10 or step 20 using their rule. Draw the pattern on grid paper to make the growth visible. Compare growing patterns with different rates of growth (add 1 each time vs. add 3 each time).

## Common Misconceptions
- Confusing growing patterns with repeating patterns — a growing pattern does not cycle back; it keeps getting bigger.
- Assuming all growing patterns add the same amount each step — some growing patterns add more and more each step (e.g., 1, 3, 6, 10 adds 2, then 3, then 4).
- Not seeing the connection between the visual growth and the number pattern — the number of tiles added corresponds to the numerical rule.

## Questions

```yaml
- question: "A staircase pattern has 1 block at step 1, 3 blocks at step 2, 6 blocks at step 3, and 10 blocks at step 4. How many blocks are added at each step?"
  type: multiple-choice
  options:
    - "2 blocks added each step"
    - "3 blocks added each step"
    - "The amount added increases: 2, then 3, then 4"
    - "The amount added decreases each step"
  answer: 2
  explanation: "From step 1 to 2: 3-1=2 blocks added. From step 2 to 3: 6-3=3 blocks added. From step 3 to 4: 10-6=4 blocks added. The amount added is increasing by 1 each time (2, 3, 4, so the next step adds 5). This is a non-constant growth rate, which is different from patterns that add the same amount each step. These are called triangular numbers."

- question: "A growing pattern adds 4 tiles at each step. Step 1 has 4 tiles. How many tiles does step 7 have?"
  type: multiple-choice
  options:
    - "24 tiles"
    - "28 tiles"
    - "32 tiles"
    - "16 tiles"
  answer: 1
  explanation: "If step 1 has 4 tiles and each step adds 4 more: step 2 has 8, step 3 has 12, step 4 has 16, step 5 has 20, step 6 has 24, step 7 has 28. Alternatively, step n has 4n tiles, so step 7 = 4 x 7 = 28 tiles. The position rule (4 times the step number) gets you there without listing every step."

- question: "A repeating pattern and a growing pattern are the same thing because both follow rules."
  type: true-false
  answer: false
  explanation: "Both follow rules, but they are fundamentally different types. A repeating pattern cycles through the same unit over and over (circle-square-circle-square — no step is bigger than another). A growing pattern gets larger at each step (1 tile, 3 tiles, 5 tiles, 7 tiles — each step has more). The rule for a repeating pattern says 'what to cycle'; the rule for a growing pattern says 'how much to add each step.'"

- question: "Why is it useful to record a growing pattern in a table with step numbers and tile counts?"
  type: short-answer
  answer: "A table organizes the data so you can see the numerical relationship clearly. By putting step numbers in one column and tile counts in another, you can spot the rule: is the count increasing by the same amount? Is it doubling? Is it connected to the step number by a formula? The table converts a visual pattern into a numerical one, making it easier to find the rule and predict future steps. It also prepares you for graphing and function tables in later math."
  explanation: "The table is a bridge between the visual and the abstract. When students see 'step 1 → 3, step 2 → 5, step 3 → 7,' they can spot 'add 2 each time' more easily than by counting tiles in increasingly complex figures. This is also the format of input-output tables, which are a stepping stone to understanding functions."
```

## Explainer

You have been working with repeating patterns (circle-square-circle-square) and number patterns (3, 6, 9, 12). Now you are going to explore a special kind of pattern that does something different: it **grows**. Each step is bigger than the one before, and the way it grows follows a rule.

Imagine building a staircase out of blocks. Step 1 is just 1 block. Step 2 adds a column of 2 blocks next to it, making 3 blocks total. Step 3 adds a column of 3, making 6 total. You can see the staircase getting taller and wider — that is a growing pattern. The visual growth (the staircase shape getting bigger) connects to a number pattern (1, 3, 6, 10...) and a growth rule (each step adds one more block than the previous step added).

The simplest growing patterns add the same amount each step. If you build with square tiles and add 2 tiles at each step, you get: 2, 4, 6, 8, 10. The growth is constant — the pattern gets bigger by the same amount every time. But some growing patterns are more interesting: they add more and more each step. The staircase pattern adds 2, then 3, then 4, then 5. The growth itself is growing. These patterns produce numbers that increase faster and faster.

To analyze a growing pattern, make a **table** with two columns: the step number and the count. Then look at the differences between consecutive counts. If the differences are constant (always +3), you have a simple growing pattern. If the differences change in a regular way (increasing by 1 each time), you have a more complex pattern with its own rule. Either way, the table turns a visual pattern into a number pattern, making the rule easier to spot. This table-based analysis — looking at inputs, outputs, and the relationship between them — is exactly what you will do later with functions and equations.
