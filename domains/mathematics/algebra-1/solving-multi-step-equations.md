---
id: solving-multi-step-equations
title: Solving Multi-Step Equations
domain: mathematics
course: algebra-1
prerequisites:
- id: two-step-equations
  type: hard
- id: combining-like-terms
  type: hard
- id: distributive-property
  type: hard
- id: variables-and-expressions-review
  type: soft
- id: properties-of-operations
  type: soft
- id: rational-numbers-operations
  type: soft
builds-toward:
- equations-variables-both-sides
- literal-equations
- systems-substitution
tags:
- equations
- multi-step
- solving
- algebra
stage: abstract-reasoning
status: validated
---
# Solving Multi-Step Equations

## Core Idea
Multi-step equations require more than two operations to solve and often involve combining like terms or distributing before isolating the variable. For example, 3(2x − 4) + 5 = 17 requires distributing (6x − 12 + 5 = 17), combining like terms (6x − 7 = 17), adding 7 (6x = 24), and dividing by 6 (x = 4). The strategy is always the same: simplify each side first, then use inverse operations to isolate the variable. This topic builds the equation-solving fluency that is needed for every subsequent algebra topic.

## How It's Best Learned
Teach a consistent procedure: (1) distribute, (2) combine like terms on each side, (3) use inverse operations to isolate the variable, (4) check by substitution. Practice with equations that have parentheses, fractions, and decimals. Include equations where the variable term ends up negative (e.g., −2x = 10, so x = −5). Emphasize checking the solution in the original equation.

## Common Misconceptions
- Forgetting to distribute to all terms inside parentheses.
- Combining terms from different sides of the equation without moving them first.
- Making sign errors when distributing negatives (e.g., −2(x − 3) = −2x + 6, not −2x − 6).

## Questions

```yaml
- question: "What is the correct first step when solving 2(3x − 1) + 4 = 18?"
  type: multiple-choice
  options:
    - "Subtract 4 from both sides."
    - "Divide both sides by 2."
    - "Distribute 2 to get 6x − 2 + 4 = 18."
    - "Add 1 to both sides."
  answer: 2
  explanation: "The first phase is always to simplify each side. Parentheses must be cleared by distributing before you can combine like terms or use inverse operations. Subtracting 4 or dividing by 2 first would leave the parentheses unresolved and produce incorrect results."

- question: "When distributing −3 across (x − 5), the correct result is −3x − 15."
  type: true-false
  answer: false
  explanation: "Distributing means multiplying −3 by each term inside: −3 · x = −3x and −3 · (−5) = +15. A negative times a negative is positive, so the result is −3x + 15. Writing −3x − 15 is one of the most common algebra errors and stems from only applying the sign to the first term or forgetting the sign rule for multiplication."

- question: "After solving a multi-step equation and finding x = 4, why should you substitute 4 back into the original equation rather than a simplified version?"
  type: short-answer
  answer: "Substituting into the original equation checks every step of your work, including any distributing or combining done during simplification. A simplified version may already contain an error, so checking against it would not catch that mistake."
  explanation: "Each simplification step is an opportunity for an arithmetic or sign error. The original equation is the ground truth — if your answer satisfies it, the solution is correct regardless of what happened in between. Checking a simplified form only validates the final inverse-operation steps, not the earlier simplification steps."
```

## Explainer

You have already solved two-step equations like 2x + 3 = 11 by undoing operations in reverse order: subtract 3 first, then divide by 2. Multi-step equations extend this idea, but they require an extra phase before you can apply inverse operations. The full strategy has two phases: simplify first, then isolate.

In the simplification phase, you work on each side of the equation independently. Start by distributing any multiplication over parentheses, then combine like terms. For example, 3(2x − 4) + 5 = 17 becomes 6x − 12 + 5 = 17 after distributing, then 6x − 7 = 17 after combining −12 and +5. You have now turned a multi-step equation into a familiar two-step equation.

In the isolation phase, proceed exactly as before: undo addition or subtraction first (add 7 to both sides: 6x = 24), then undo multiplication or division (divide by 6: x = 4). The principle is always to peel away operations from the outside in — the last operation applied to x is the first one you undo.

The step that generates the most errors is distributing a negative. When distributing −2 across (x − 3), every term inside gets multiplied by −2: −2·x = −2x and −2·(−3) = +6, giving −2x + 6. Students frequently write −2x − 6 because they apply the sign only to the first term or forget that negative times negative is positive. Writing out the multiplication term by term before combining eliminates most of these errors.

Always verify your answer by substituting it into the original, un-simplified equation. Checking x = 4 in 3(2·4 − 4) + 5 confirms 3(4) + 5 = 17. This validation habit not only catches arithmetic mistakes but builds confidence in the procedure. The simplify-then-isolate strategy scales up to every future algebra topic — equations with variables on both sides, literal equations, and systems of equations all follow the same two-phase structure.
