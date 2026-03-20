---
id: bar-graphs-3rd
title: Scaled Bar Graphs
domain: mathematics
course: 3rd-grade
prerequisites:
- id: category-data-collection
  type: hard
- id: interpreting-data-bar-graphs
  type: soft
builds-toward:
- scaled-bar-graphs
- line-graphs
- mean-median-mode
tags:
- bar-graphs
- data
- scaled
- graphing
stage: concrete-operations
status: validated
---

# Scaled Bar Graphs

## Core Idea
A scaled bar graph uses a scale other than 1 (e.g., each unit represents 2, 5, or 10) to display larger data sets compactly. Students read the scale, determine the value of each bar, and answer comparison questions: 'How many more?', 'How many in all?'. They also create scaled bar graphs from data tables.

## How It's Best Learned
Start by reading pre-made bar graphs with different scales, identifying the scale first. Then have students create their own using survey data from class. Explicitly compare a scale-of-1 graph to a scale-of-5 graph for the same data.

## Common Misconceptions
- Reading bars between gridlines incorrectly when the scale is not 1.
- Forgetting to multiply by the scale value when calculating the total for a bar.

## Questions

```yaml
- question: "A bar graph has a scale of 5 (each gridline = 5 students). The bar for 'soccer' reaches the 6th gridline. How many students chose soccer?"
  type: multiple-choice
  options:
    - "6 students — the bar reaches the 6th line"
    - "30 students — because 6 × 5 = 30"
    - "11 students — because 6 + 5 = 11"
    - "15 students — because the scale adds 5 per bar"
  answer: 1
  explanation: "The scale tells you what each gridline represents. If each unit = 5, then a bar at the 6th gridline represents 6 × 5 = 30. Reading the bar height as a face value (6) is the most common error on scaled bar graphs — it ignores the scale entirely."

- question: "On a scaled bar graph where each unit = 10, the 'red' bar reaches halfway between the 30 and 40 gridlines, and the 'blue' bar reaches the 50 gridline. How many more students chose blue than red?"
  type: multiple-choice
  options:
    - "15 more — because 50 − 35 = 15"
    - "10 more — the bars differ by one full gridline"
    - "20 more — because 50 − 30 = 20"
    - "5 more — they differ by half a unit"
  answer: 0
  explanation: "Halfway between 30 and 40 on a scale-of-10 graph is 35. Blue = 50. The difference is 50 − 35 = 15. Option B ignores the halfway position. Option C ignores the halfway position and rounds down. Once you convert bar heights to real values using the scale, the comparison is ordinary subtraction."

- question: "On a bar graph where each unit equals 5, a bar that reaches the 4th gridline represents 4 students."
  type: true-false
  answer: false
  explanation: "A bar at the 4th gridline represents 4 × 5 = 20 students, not 4. The gridline number must be multiplied by the scale to get the actual value. Reading bar height as face value only works when the scale is 1."

- question: "The main reason to use a scale greater than 1 on a bar graph is to make large data sets fit into a readable, practical chart."
  type: true-false
  answer: true
  explanation: "Scaling compresses large numbers visually. A graph showing 340 students at scale = 1 would need a 340-unit axis. At scale = 10, the same data fits in 34 units. The visual relationships between bars are preserved; only the labeling changes. Scaling doesn't distort the data — it makes it manageable."

- question: "What is the first thing you should do before reading any bar on a scaled bar graph, and why?"
  type: short-answer
  answer: "Identify the scale — find out what value each gridline unit represents. Without knowing the scale, you cannot convert bar height into an actual quantity."
  explanation: "The same bar height means completely different values depending on the scale. A bar at height 4 means 4 students at scale=1, 20 students at scale=5, and 40 students at scale=10. The scale is the key that unlocks the numbers. Always read it first — it's usually labeled on the y-axis or in a legend."
```

## Explainer

You've already worked with basic bar graphs where each unit on the vertical axis stands for exactly one thing — one student, one vote, one item. A **scaled bar graph** uses the same visual format but changes the meaning of each unit. When the scale says "each square = 5 students," a bar that reaches the 4th gridline represents 4 × 5 = 20 students, not 4. The bars still communicate quantity through height, but you must translate height into value using the scale.

Why would anyone use a scale other than 1? Because data can be large. If a school has 340 students and you want to graph attendance by grade, a scale-of-1 bar graph would need to be 340 units tall — impractical to draw or read. A scale of 10 collapses the same data into a 34-unit bar. A scale of 20 makes it 17 units. **Scaling** is a compression tool that makes large numbers visually manageable without losing the ability to compare and calculate.

The critical habit is: **identify the scale before reading any bar**. Look at the y-axis label (e.g., "Number of Students"), find the gridlines, and determine what each unit represents. If the scale is 5 and a bar reaches the 6th gridline, the value is 30 — not 6. When a bar falls between two gridlines, you estimate: if the scale is 10 and a bar is halfway between 40 and 50, the value is 45.

Answering comparison questions ("how many more X than Y?") works the same as with scale-1 graphs — find both values, then subtract. The only added step is converting bar heights to real values using the scale first. Once you have the actual numbers, the arithmetic is ordinary subtraction or addition. A bar graph's job is to make comparisons fast and visual; the scale is just the key that unlocks the numbers.
