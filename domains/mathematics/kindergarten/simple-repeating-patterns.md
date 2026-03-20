---
id: simple-repeating-patterns
title: Simple Repeating Patterns (AB, ABC)
domain: mathematics
course: kindergarten
prerequisites:
- id: sorting-by-attributes
  type: soft
tags:
- patterns
- algebra-readiness
- sequences
stage: pre-formal
status: validated
---

# Simple Repeating Patterns (AB, ABC)

## Core Idea
A repeating pattern is a sequence where a core unit repeats over and over, such as red-blue-red-blue (AB pattern) or circle-square-triangle-circle-square-triangle (ABC pattern). Children learn to identify, extend, and create patterns. Recognizing patterns is a foundational algebraic thinking skill.

## How It's Best Learned
Use colored cubes, clapping rhythms, and body movements. Ask children to 'read' the pattern aloud, identify the core unit, and predict what comes next. Have them create their own patterns.

## Common Misconceptions
- Extending a pattern by repeating the last element rather than the whole core unit.
- Not recognizing that a pattern with different materials (clap-stomp vs. red-blue) can be the same structure.

## Questions

```yaml
- question: "A pattern goes: circle, square, triangle, circle, square, triangle, circle. What comes next?"
  type: multiple-choice
  options:
    - "Circle — because the last item was a circle"
    - "Square — because the core unit is circle-square-triangle and square is next in the cycle"
    - "Triangle — because triangles always come after circles"
    - "Circle-square-triangle — because the whole unit repeats at once"
  answer: 1
  explanation: "The core unit is circle-square-triangle (an ABC pattern). After two full repetitions, 'circle' has started the third repetition — so 'square' comes next. The most common mistake is to repeat the last element (circle again), but that ignores the structure. To extend any pattern correctly, you must find the core unit and determine where you are within it."

- question: "Which of these sequences has the same pattern structure as red-blue-red-blue?"
  type: multiple-choice
  options:
    - "Clap-stomp-clap-stomp — two actions alternating, the same AB structure"
    - "Clap-stomp-snap-clap-stomp-snap — three different things in the core unit"
    - "Clap-clap-stomp-clap-clap-stomp — clap appears twice in a row"
    - "Stomp-stomp-stomp — only one kind of thing repeating"
  answer: 0
  explanation: "An AB pattern has exactly two distinct elements in the core unit that alternate: A, B, A, B, ... Clap-stomp-clap-stomp has the core unit 'clap-stomp' — two distinct actions taking turns — which is exactly the AB structure of red-blue-red-blue. The materials (colors vs. movements) don't determine the structure; the number and order of distinct elements do. Recognizing the same structure in different materials is the key algebraic insight."

- question: "A clap-snap-clap-snap pattern and a red-blue-red-blue pattern have the same mathematical structure."
  type: true-false
  answer: true
  explanation: "Both are AB patterns: a two-element core unit that repeats. The material (sound vs. color) is completely irrelevant to the pattern structure. This is what makes patterns mathematical — you can strip away the specific objects and ask only about the structure: how many distinct elements, in what order. Recognizing the same structure across different materials is the beginning of algebraic thinking."

- question: "To find out what comes next in a pattern, you just need to look at the last element and repeat it."
  type: true-false
  answer: false
  explanation: "This is the most common error in pattern extension. For example, in red-blue-red-blue-red, the last element is red — but the next element is blue, because the core unit is red-blue and you are in the middle of a new repetition. You must identify the complete core unit and determine your position within it, then apply what comes next in that unit. Looking only at the last element gives the right answer only by accident."

- question: "Why do you need to find the core unit of a pattern before you can extend it correctly?"
  type: short-answer
  answer: "Because the core unit is what repeats — it defines the full cycle of the pattern. If you only look at the last element, you might guess it repeats, but that is only correct if that element happens to be at the end of the core unit. Only by knowing the full core unit can you determine where you are in the cycle and what correctly comes next."
  explanation: "A pattern is defined by its core unit, not by any individual element. The core unit is the fundamental repeating group. Once identified, you can determine your position within any repetition and predict any future element. Without the core unit, you have no principled basis for prediction — you might get lucky by repeating the last item, but for AB patterns ending mid-cycle, the last-item strategy gives the wrong answer every time."
```

## Explainer

A **pattern** is something that repeats in a predictable way. Look at this sequence: red, blue, red, blue, red, blue. It keeps going the same way over and over. The part that repeats — "red, blue" — is called the **core unit**. Once you find the core unit, you can predict what comes next, no matter how long the pattern gets.

An **AB pattern** has two things that trade off: A, then B, then A, then B, and so on. Red-blue-red-blue is an AB pattern. Clap-stomp-clap-stomp is also an AB pattern. Even though one uses colors and the other uses movements, they have the same shape — two things taking turns. An **ABC pattern** has three things in the core: circle, square, triangle, circle, square, triangle. Now three things rotate, and you need to see all three before the unit repeats.

The secret to extending a pattern is to find the core unit first, not just look at what comes last. Suppose a pattern ends with: red, blue, red. What comes next? If you only looked at the last thing (red) and said "red again," you'd be wrong. You need to find the core unit — red, blue — and see where you are in it. After the second red, the core starts over, so blue comes next.

Patterns show up everywhere: in music (verse-chorus-verse), in nature (petals on a flower, stripes on a zebra), and in numbers (2, 4, 6, 8 — the core unit is "add 2"). Learning to spot the core unit and predict what comes next is the beginning of the mathematical idea of **algebraic thinking** — noticing structure and using it to make predictions.
