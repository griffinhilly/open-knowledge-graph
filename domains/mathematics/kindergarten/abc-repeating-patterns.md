---
id: abc-repeating-patterns
title: Recognizing ABC Repeating Patterns
domain: mathematics
course: kindergarten
prerequisites:
- id: grade-seriation
  type: hard
- id: discernment-same-different
  type: soft
- id: ab-repeating-patterns
  type: hard
builds-toward:
- extending-and-creating-patterns
tags:
- patterns
- ABC pattern
- sequence
stage: pre-formal
status: validated
---

# Recognizing ABC Repeating Patterns

## Core Idea
An ABC repeating pattern cycles through three elements: A-B-C-A-B-C-A-B-C. This is more complex than AB patterns and requires stronger prediction and logical thinking skills.

## Explainer

You've already worked with AB repeating patterns, where two elements alternate: A-B-A-B-A-B. The key idea you learned is that a pattern has a **core** — the smallest repeating unit — and that identifying the core lets you predict any element in the sequence. An **ABC pattern** uses the same logic with a three-element core: A-B-C-A-B-C-A-B-C. The core is one group of three, and it repeats over and over.

The challenge with ABC patterns is keeping track of where you are in the three-step cycle. With AB patterns, you only needed to know "odd position or even position?" — two options. With ABC patterns, you track position 1, 2, or 3 within the core. A concrete example: red-blue-green-red-blue-green-red-... The 7th element is red (the cycle restarts at position 1). The 8th is blue. The 9th is green. To find any element, count how many complete cycles of three fit before that position, and identify what's left over. This kind of thinking — keeping a place in a repeating cycle — is the mathematical skill being developed, and it lays groundwork for ideas like skip-counting, multiples, and remainders much later.

ABC patterns appear everywhere in daily life. The days of the week follow a repeating cycle of seven. Traffic lights cycle red-yellow-green. Musical rhythms repeat a beat pattern. When you see stripes on a shirt (three colors, repeating) or clap a rhythm that goes boom-clap-clap-boom-clap-clap, you're experiencing ABC-type repeating structure. The letters A, B, C are just labels — they stand for any three distinct categories: shapes, colors, sounds, actions, or objects. Learning to see through the specific details to the underlying structure (three things, cycling) is exactly what mathematical abstraction means at its earliest stage.

To extend an ABC pattern, identify the core, find where the last given element falls in the cycle, and continue from there. If the sequence ends on C, the next element is A (back to the start of the core). If it ends on B, the next is C. You can also go backwards: if the sequence starts mid-cycle, you can figure out which position in the core the first element represents. Practicing both extending and creating your own ABC patterns — with blocks, stickers, claps, or colors — builds the flexibility to recognize repeating structure no matter what form the elements take.

## Questions

```yaml
- question: "A pattern goes: triangle, circle, square, triangle, circle, square, triangle... What comes next?"
  type: multiple-choice
  options:
    - "triangle"
    - "circle"
    - "square"
    - "star"
  answer: 1
  explanation: "The core of this ABC pattern is triangle-circle-square. After triangle comes circle — we're at position 2 in the core. The pattern continues: triangle (pos 1), circle (pos 2), square (pos 3), then repeat."

- question: "In the pattern red-blue-green-red-blue-green, what color is the 9th element?"
  type: multiple-choice
  options:
    - "red"
    - "blue"
    - "green"
    - "yellow"
  answer: 2
  explanation: "The core is red-blue-green (3 elements). 9 ÷ 3 = 3 with no remainder, so the 9th element is at position 3 in the core, which is green."
```
