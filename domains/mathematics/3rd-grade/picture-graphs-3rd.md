---
id: picture-graphs-3rd
title: Scaled Picture Graphs (Pictographs)
domain: mathematics
course: 3rd-grade
prerequisites:
- id: category-data-collection
  type: hard
- id: picture-graphs
  type: soft
builds-toward:
- scaled-picture-graphs
tags:
- pictograph
- data
- scaled
- symbol
stage: concrete-operations
status: validated
---

# Scaled Picture Graphs (Pictographs)

## Core Idea
A picture graph (pictograph) uses symbols to represent data, with a key telling how many each symbol represents. In scaled pictographs, each symbol may represent 2, 5, or 10 items. Students read the key, multiply to find totals, use half-symbols when appropriate, and create pictographs from data.

## How It's Best Learned
Read pictographs with varying scales and discuss how to handle a category that doesn't divide evenly by the scale (use a half symbol). Have students create their own pictograph from a provided data table.

## Common Misconceptions
- Forgetting to use the key — counting symbols as if each equals 1.
- Not knowing how to represent a number that is not a multiple of the scale (half-symbols solve this).

## Questions

```yaml
- question: "A pictograph shows that Classroom A has 6 apple symbols. The key says: 🍎 = 5 students. How many students are in Classroom A?"
  type: multiple-choice
  options:
    - "6 students — count the symbols"
    - "11 students — add 6 + 5"
    - "30 students — multiply 6 × 5"
    - "5 students — the key value is always the answer"
  answer: 2
  explanation: "The key tells you that each symbol represents 5 students, not 1. You must multiply: 6 symbols × 5 students per symbol = 30 students. Counting the symbols as if each equals 1 is the most common error with scaled pictographs — it's exactly what the key is designed to prevent. The key is the first thing to read before interpreting any data in the graph."

- question: "A data table shows that 25 students chose soccer as their favorite sport. If the pictograph key is ⚽ = 5 students, how many soccer ball symbols should appear in the soccer row?"
  type: multiple-choice
  options:
    - "25 symbols — one for each student"
    - "20 symbols — subtract 25 − 5"
    - "5 symbols — divide 25 ÷ 5"
    - "125 symbols — multiply 25 × 5"
  answer: 2
  explanation: "To convert a data value into symbols, divide by the scale: 25 ÷ 5 = 5 symbols. This is the reverse process of reading — instead of multiplying symbols × scale to get the count, you divide count ÷ scale to get the number of symbols to draw. Option A (25 symbols) is the error of ignoring the key entirely; option D (125 symbols) reverses the operation."

- question: "A half-symbol in a scaled pictograph represents half the value shown in the key."
  type: true-false
  answer: true
  explanation: "If the key states each symbol = 4, then a half-symbol represents 2. Half-symbols exist specifically to handle data values that fall between multiples of the scale. For example, if a category has 14 items and the scale is 4 (14 ÷ 4 = 3.5), you draw 3 full symbols and 1 half-symbol. Without half-symbols, you could only represent exact multiples of the scale."

- question: "When reading a scaled pictograph, you should count the total number of symbols in a row to find the data value for that category."
  type: true-false
  answer: false
  explanation: "Counting symbols gives you the number of symbols — not the data value. You must always multiply: data value = number of symbols × scale. For example, 4 symbols with a key of ⭐ = 10 means 40 items, not 4. Forgetting to multiply is the defining error with scaled pictographs, which is exactly why the key is the most important element to check before reading any data."

- question: "Why do scaled pictographs use a key, and what would go wrong if you forgot it and just counted the symbols as if each equaled 1?"
  type: short-answer
  answer: "The key tells you how many items each symbol represents. It exists because large datasets would require impractically many individual symbols — scaling lets you represent hundreds of items with a manageable number of symbols. If you forget the key and count symbols as 1 each, you undercount by a factor of the scale. For example, with a scale of 5, a row of 8 symbols represents 40 items — but ignoring the key gives the wrong answer of 8."
  explanation: "Choosing the right scale is itself a skill: you want symbol counts under about 10 per row so the graph stays readable, but you also want the scale to divide evenly into most of your data values. The key is not decoration — it is the conversion factor that makes the entire graph meaningful, and reading it first is the non-negotiable first step."
```

## Explainer

You already know how to read a simple picture graph where each symbol stands for exactly 1 item. Now you are adding a new power: each symbol can represent *more than one* item. A **scaled pictograph** uses a **key** that says something like "⭐ = 5 students." That means every full star you see in a row stands for 5 students — so a row with 6 stars represents 30 students, not 6. The key multiplies your counting.

The reason for scaling is practical: if 200 students were surveyed, drawing 200 individual symbols would take forever and the graph would be enormous. By choosing a scale of 10, you only need 20 symbols for the same data, and the graph stays readable. Choosing the right scale is itself a skill — look at the largest category in your data and pick a scale that keeps symbol counts manageable (usually under about 10 symbols per row).

When you read a scaled pictograph, always multiply — don't just count. If the key says each symbol = 5 and a row has 4 symbols, the answer is 4 × 5 = 20, not 4. This is where your multiplication knowledge (already in progress in 3rd grade) connects directly to reading data. A **half-symbol** represents half the key value: if each whole symbol = 5, then a half-symbol = 2.5, or if each symbol = 4, a half-symbol = 2. Half-symbols let you represent totals that fall between multiples of the scale.

When you create your own pictograph, start from your data table: find the largest value, choose a scale that fits, divide each value by the scale to find the number of symbols needed, and draw them in neat rows aligned to a common baseline. Check your work by reversing the process — multiply your symbol counts by the scale and verify they match the original data. A well-made pictograph lets a reader immediately see comparisons ("twice as many" or "half as many") without doing any arithmetic at all.
