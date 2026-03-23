---
id: picture-graphs-scaled-3rd
title: Scaled Picture Graphs
domain: mathematics
course: 3rd-grade
prerequisites:
- id: picture-graphs-3rd
  type: hard
builds-toward:
- data-representation-analysis
tags:
- pictographs
- data
- scaled
stage: concrete-operations
status: validated
---

# Scaled Picture Graphs

## Core Idea
A scaled pictograph uses symbols where each symbol represents multiple items (e.g., each picture = 2 or 5 items). This works for larger quantities better than one-to-one pictographs.

## How It's Best Learned
Interpret existing scaled pictographs. Create pictographs with class data using a chosen scale.

## Common Misconceptions
Not reading the scale correctly; forgetting to multiply the scale value; drawing incorrect partial symbols.

## Questions

```yaml
- question: "A scaled pictograph shows books read by students. The key says: each 📚 = 4 books. Kenji's row shows 3 full book symbols and one half-symbol. How many books did Kenji read?"
  type: multiple-choice
  options:
    - "3 — there are 3 full symbols in his row"
    - "7 — add 3 full symbols plus 1 half-symbol"
    - "14 — multiply 3.5 symbols × 4 books per symbol"
    - "12 — multiply only the 3 full symbols by 4, ignoring the half-symbol"
  answer: 2
  explanation: "Each full symbol = 4 books; a half-symbol = 2 books (half of 4). So: 3 × 4 = 12 books from the full symbols, plus 2 books from the half-symbol = 14 total. Option D is the common error of ignoring the half-symbol. Option A ignores the scale entirely — that mistake is the same as reading a scaled pictograph like a one-to-one pictograph."

- question: "A teacher has data: Soccer: 20 students, Basketball: 15, Swimming: 10. Which scale makes the cleanest scaled pictograph?"
  type: multiple-choice
  options:
    - "Each symbol = 3 students — 20 ÷ 3 and 15 ÷ 3 don't divide evenly"
    - "Each symbol = 4 students — 15 ÷ 4 doesn't divide evenly"
    - "Each symbol = 5 students — 20 ÷ 5 = 4, 15 ÷ 5 = 3, 10 ÷ 5 = 2 (all whole numbers)"
    - "Each symbol = 6 students — none of the values divide evenly by 6"
  answer: 2
  explanation: "The best scale divides evenly into all data values to avoid partial or broken symbols. 5 divides cleanly into 20, 15, and 10 — producing exactly 4, 3, and 2 whole symbols. The other scales produce remainders, which require awkward partial symbols that are hard to draw accurately and hard to interpret."

- question: "In a scaled pictograph where each symbol = 5 items, a row with 6 symbols means there are 6 items in that category."
  type: true-false
  answer: false
  explanation: "In a scaled pictograph, you must multiply the number of symbols by the scale value. 6 symbols × 5 items per symbol = 30 items — not 6. Reading the symbol count directly as the data value is the most common error when working with scaled pictographs; it treats the graph as if it were a one-to-one pictograph."

- question: "You must read the key (legend) of a scaled pictograph before interpreting any data in the graph."
  type: true-false
  answer: true
  explanation: "Without the key, you don't know what each symbol represents. Every calculation you make — reading individual values, comparing categories, finding totals — depends entirely on the scale defined in the key. A pictograph without its key is uninterpretable: the same row of symbols could mean 6 items, 12 items, 30 items, or any other value depending on the scale."

- question: "Explain why pictographs use a scale (where each symbol represents more than one item) and what goes wrong if you forget to apply the scale when reading one."
  type: short-answer
  answer: "We use a scale so that large data values can be shown with fewer symbols — drawing 80 individual symbols for a category would be tedious and hard to read. A scale of 10 reduces 80 symbols to just 8. If you forget to apply the scale, you read the symbol count as the data value and get the wrong answer. For example, if each symbol = 10 and a row has 7 symbols, you'd misread 7 instead of the correct 70."
  explanation: "The scale is the key difference between a one-to-one pictograph and a scaled one. In a one-to-one graph, you just count symbols. In a scaled graph, counting symbols gives you only the intermediate step — you must then multiply by the scale value. Forgetting this step produces answers that are off by exactly the scale factor."
```

## Explainer

You already know how to read a pictograph where each symbol stands for exactly one item. A **scaled pictograph** extends that idea: each symbol now stands for more than one item — maybe 2, maybe 5, maybe 10. The graph itself looks the same, but the **key** (or **legend**) tells you the scale, and that changes how you interpret every row.

Suppose a pictograph shows favorite fruits. The key reads "each ★ = 5 students." If the Mango row has 4 stars, that doesn't mean 4 students chose mango — it means 4 × 5 = 20 students chose mango. Every symbol counts as 5, so you multiply the number of symbols by the scale value to get the true count. Reading the key before anything else is the essential first step.

Scaled pictographs exist because a one-to-one graph gets impractical when data is large. Drawing 80 symbols for a category with 80 responses would be tedious. Using a scale of 10 reduces that to just 8 symbols, making the graph clear and compact. The tradeoff is that you need to apply the scale every time you read or build a value.

Half-symbols sometimes appear in scaled graphs to represent half the scale value — for example, a half-star represents 2.5 students when each full star equals 5. When you build your own scaled pictograph, choose a scale that divides evenly into your data values so you can avoid awkward partial symbols. If your data includes 15 and 20 and 35, a scale of 5 works cleanly; a scale of 3 would create messy fractions.

