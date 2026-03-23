---
id: picture-graphs-with-scale
title: Picture Graphs with Scales
domain: mathematics
course: 3rd-grade
prerequisites:
- id: picture-graphs-read-create-2nd
  type: hard
builds-toward:
- scaled-graphs-reading
tags:
- data
- picture-graphs
- scale
stage: concrete-operations
status: validated
---

# Picture Graphs with Scales

## Core Idea
Picture graphs use symbols (pictures) to represent data. A scale explains what each symbol represents—for example, one apple picture = 2 real apples. Scales are necessary when data quantities are large, making one-symbol-per-item impractical.

## Questions

```yaml
- question: "A picture graph shows that the 'Dogs' row has 5 paw-print symbols. The key says: 'Each paw print = 3 dogs.' A student says there are 5 dogs because they count 5 symbols. What error did the student make?"
  type: multiple-choice
  options:
    - "The student read the wrong row"
    - "The student forgot to divide by 5 to get the scale"
    - "The student treated each symbol as representing 1 item instead of applying the scale — the correct answer is 5 × 3 = 15 dogs"
    - "The student should have added the scale value to the symbol count: 5 + 3 = 8"
  answer: 2
  explanation: "Reading a scaled pictograph requires multiplication: count the symbols, then multiply by the scale value. The student defaulted to 1-to-1 thinking — the habit from earlier pictographs where each symbol represented exactly one item. Once a scale is involved, counting symbols gives you the number of symbols, not the number of items. The key (legend) tells you what each symbol is worth, and you must apply it: 5 symbols × 3 per symbol = 15 dogs."

- question: "Why do scaled picture graphs use a key where each symbol represents more than one item?"
  type: multiple-choice
  options:
    - "To make the graph harder to read so students must think more carefully"
    - "Because all official graphs are legally required to include a scale"
    - "Because large data values would require drawing too many symbols at 1-to-1, making the graph impractically large or cluttered"
    - "To practice multiplication in a different context"
  answer: 2
  explanation: "Scale exists for a practical reason: it makes graphs readable. If a survey of 200 students found 60 preferred soccer, drawing 60 soccer ball symbols would be impractical. With a scale of 10, you draw 6 symbols — clean and easy to compare. Choosing a good scale is a design decision: the scale should divide evenly into most data values to avoid awkward partial symbols, and it should keep the graph compact without losing meaningful differences between categories."

- question: "If a row in a scaled picture graph shows 3 full symbols and 1 half-symbol, and the scale is 'each symbol = 4,' the row represents 14 items."
  type: true-false
  answer: true
  explanation: "Three full symbols × 4 = 12, plus one half-symbol = half of 4 = 2. Total: 12 + 2 = 14. A half-symbol represents half the scale value. This is consistent with the logic of the scale: if a full symbol represents 4, a symbol that is half as large represents half as much. Partial symbols allow the graph to show values that fall between multiples of the scale."

- question: "A picture graph that uses a scale where each symbol = 1 item requires the same multiplication skill as a picture graph where each symbol = 5 items."
  type: true-false
  answer: false
  explanation: "When the scale is 1 (each symbol = 1 item), you simply count the symbols — no multiplication is needed. Scaled picture graphs introduce multiplication as a necessary step precisely because symbols represent multiple items. The skill shift from 1st/2nd grade pictographs (count) to 3rd grade scaled pictographs (count then multiply) is the key conceptual development this topic addresses. Understanding when multiplication is required — and why — is the core insight."

- question: "How do you use the key (scale) in a scaled picture graph to find the actual number of items a row represents? Walk through the steps."
  type: short-answer
  answer: "First, read the key to find out what one symbol is worth (e.g., each symbol = 5 items). Second, count the number of symbols in the row. Third, multiply: number of symbols × scale value = total items. If there is a partial symbol, find its value by taking the appropriate fraction of the scale value (a half-symbol with scale 5 equals 2.5, or if the scale is meant to produce whole numbers, 2 or 3). For example: 4 symbols, scale = 5 → 4 × 5 = 20 items."
  explanation: "The key insight is that reading a scaled pictograph is a multiplication problem in disguise. The graph turns a multiplication question into a visual one: 'how many groups of [scale value] are here?' Students who understand this connection can work backward too — if a category has 30 items and the scale is 5, they know to draw 6 symbols. This bidirectional thinking (reading and creating graphs) deepens the understanding of what scale means."
```

## Explainer

You already know how to read and create picture graphs where each symbol stands for exactly one item — a 1-to-1 picture graph. That works great when the numbers are small. But what if a school survey asked 120 students about their favorite subject, and you had to draw 120 symbols? The graph would be enormous. **Scaled picture graphs** solve this by letting each symbol represent more than one item, so the graph stays a manageable size.

The **scale** is the rule that tells you how many real items each symbol counts for. The scale is always shown in a key (also called a legend) somewhere on the graph, usually written like: "Each 🍎 = 5 apples." Once you know the scale, you can read the graph by multiplying: if the "Apples" row has 6 symbols and each symbol = 5, then 6 × 5 = 30 apples total. If a row has 4 symbols, that row represents 4 × 5 = 20 items. Reading a scaled picture graph is really a multiplication problem in disguise.

Sometimes a row will have a partial symbol — like half a picture. If the scale is "each symbol = 4," then half a symbol means 2. Partial symbols are just a visual way of representing amounts that fall between multiples of the scale. When you see a half symbol, divide the scale value in half to find what it represents.

Choosing the right scale when you create a graph is a decision that requires judgment. If your largest value is 30 and you use a scale of 1, you draw 30 symbols — too many. If you use a scale of 10, you draw 3 symbols — clean and readable. A good scale divides evenly into most of the data values, so you avoid awkward fractions. Thinking about scale is your first taste of the kind of design decisions that make data displays clear and useful.
