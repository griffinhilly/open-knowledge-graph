---
id: extending-patterns-logic
title: Extending Patterns
domain: formal-sciences-and-logic
course: patterns-and-logic
prerequisites:
- id: recognizing-patterns
  type: hard
- id: extending-and-creating-patterns
  type: soft
builds-toward:
- number-patterns-logic
- growing-patterns
tags:
- patterns
- prediction
- sequences
stage: concrete-operations
status: draft
---

# Extending Patterns

## Core Idea
Extending a pattern means using the rule you have identified to predict what comes next — and what comes after that, and after that. This is more than guessing: it requires understanding the rule well enough to apply it reliably. Extending patterns builds the habit of reasoning forward from a rule, which is the foundation of logical prediction and, eventually, algebraic thinking.

## How It's Best Learned
Give students patterns with the first several elements shown and ask them to continue for 3-5 more elements. Start with repeating patterns (AB, ABC, AABB) before moving to growing patterns (add 2 each time). Have students explain their reasoning: "I know the next one is blue because the pattern goes red-blue-red-blue, and the last one was red." Include "find the mistake" exercises where a pattern is extended incorrectly and students must identify where it went wrong.

## Common Misconceptions
- Extending by repeating only the last element instead of the full repeating unit (e.g., writing circle-square-circle-square-square instead of circle-square-circle-square-circle-square).
- Correctly extending a pattern for 1-2 steps but losing track of the rule for longer extensions.
- Assuming the pattern must continue forever in one direction — patterns can also be extended backward.

## Questions

```yaml
- question: "A pattern goes: triangle, circle, circle, triangle, circle, circle, triangle, circle, circle. What are the next three shapes?"
  type: multiple-choice
  options:
    - "Triangle, triangle, triangle"
    - "Circle, circle, circle"
    - "Triangle, circle, circle"
    - "Circle, triangle, circle"
  answer: 2
  explanation: "The repeating unit is triangle-circle-circle (an ABC pattern). After the third complete cycle ends with circle-circle, the pattern starts over: triangle, circle, circle. Identifying the core unit (three elements long) is the key — then extending is just repeating that unit."

- question: "The number pattern 5, 10, 15, 20, 25 continues with the rule 'add 5.' What is the 8th number in this pattern?"
  type: multiple-choice
  options:
    - "35"
    - "40"
    - "45"
    - "50"
  answer: 1
  explanation: "The pattern is 5, 10, 15, 20, 25, 30, 35, 40. The 8th number is 40. You can find it by continuing the 'add 5' rule: 25 + 5 = 30 (6th), 30 + 5 = 35 (7th), 35 + 5 = 40 (8th). Knowing the rule lets you extend to any position without listing every term."

- question: "Extending a pattern backward (figuring out what came before the first shown element) requires the same rule as extending it forward."
  type: true-false
  answer: true
  explanation: "The rule works in both directions. If a pattern adds 3 each step (4, 7, 10, 13...), then going backward means subtracting 3: the term before 4 would be 1. If a pattern repeats circle-square, then going backward from circle-square-circle... the previous element would be square. The rule defines the pattern in both directions."

- question: "If you can correctly predict the next element in a pattern, does that prove you understand the rule? Explain why or why not."
  type: short-answer
  answer: "Not necessarily. Getting the next element right might be a lucky guess or based on a shallow observation. Understanding the rule means you can extend the pattern many steps forward, extend it backward, explain why each element is what it is, and recognize the same rule in a different context. For example, knowing the next color in red-blue-red-blue is red shows some recognition, but stating 'the pair red-blue repeats' and being able to say what the 20th element would be shows genuine understanding."
  explanation: "This is why teachers ask students to explain their reasoning, not just give the next answer. The explanation reveals whether the student has grasped the underlying rule or is just pattern-matching the surface. True understanding is testable by asking for distant terms (what is the 50th element?) or by presenting the same pattern in different materials."
```

## Explainer

You have learned to recognize patterns — to notice when something follows a predictable rule. Now you are going to use that recognition to do something powerful: **extend the pattern** by predicting what comes next, and next, and next.

Extending a repeating pattern is like knowing the lyrics to a song's chorus. Once you have identified the core unit — say, clap-snap-clap-snap — you know the chorus repeats. So after the fourth element (snap), the fifth must be clap, the sixth must be snap, and so on. The key is identifying the **core unit** (clap-snap, which is 2 elements long) and then cycling through it.

For number patterns, extending means applying the rule step by step. If the pattern is 3, 6, 9, 12 and the rule is "add 3," then the next terms are 15, 18, 21. But here is what makes extending more than guessing: if you truly understand the rule, you can jump ahead. What is the 10th term? It is 30, because each term is 3 times its position number. You do not need to list all ten terms to find it — the rule does the work.

Extending also works **backward**. If a pattern goes 10, 8, 6, 4 (subtract 2 each time), then the term before 10 must be 12. This is the same rule applied in reverse. Being able to extend in both directions is a strong sign that you truly understand the pattern, not just the next step.

The habit you are building here — "I know the rule, so I can predict any element" — is the seed of algebraic thinking. Eventually, a rule like "start at 5 and add 3 each time" will become a formula. But right now, the important thing is confidence: once you have the rule, you own the entire pattern.
