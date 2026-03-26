---
id: scaled-picture-graphs
title: Scaled Picture Graphs
domain: mathematics
course: 2nd-grade
prerequisites:
- id: picture-graphs
  type: hard
- id: skip-counting-by-2s
  type: soft
- id: skip-counting-by-5s
  type: soft
builds-toward:
- scaled-bar-graphs
- interpreting-data-bar-graphs
tags:
- data
- picture-graphs
- scale
- interpret
stage: concrete-operations
status: validated
---

# Scaled Picture Graphs

## Core Idea
A scaled picture graph uses a key where each symbol represents more than one unit — for example, each star = 2 votes. To find the total for a category, multiply the number of symbols by the scale value. If 5 stars represent votes for pizza and each star = 2, then 10 students voted for pizza. Scaled graphs are used when individual symbols would become too numerous.

## How It's Best Learned
Begin by asking students to draw a picture graph where each picture = 1, then show how many symbols it requires for large data sets. Introduce the key concept as a solution. Practice reading, interpreting, and drawing scaled picture graphs with a variety of scales (×2, ×5, ×10).

## Common Misconceptions
- Ignoring the scale key and reading each symbol as 1.
- Forgetting to account for partial symbols when data doesn't divide evenly.
- Not writing a key when creating their own scaled picture graphs.

## Questions

```yaml
- question: "A picture graph shows 3 stars in the 'basketball' row. The key says ★ = 5 students. How many students chose basketball?"
  type: multiple-choice
  options:
    - "3 students — there are 3 stars"
    - "8 students — add 3 and 5"
    - "15 students — multiply 3 stars × 5 students each"
    - "2 students — subtract 5 minus 3"
  answer: 2
  explanation: "In a scaled picture graph, each symbol represents the scale value, not 1. So 3 stars × 5 students per star = 15 students. Reading each star as '1 student' is the most common mistake with scaled graphs — it ignores the key entirely and treats the graph like a one-to-one picture graph."

- question: "A survey of 40 students asks about their favorite season. The most popular season has 20 responses. Which scale would make the most readable picture graph?"
  type: multiple-choice
  options:
    - "1 — one symbol per response gives the most accurate picture"
    - "2 — each symbol represents 2 responses"
    - "5 — each symbol represents 5 responses"
    - "20 — each symbol represents 20 responses"
  answer: 2
  explanation: "A scale of 5 means the largest category uses 20 ÷ 5 = 4 symbols — compact and readable. A scale of 1 requires 20 symbols in one row (crowded and slow to draw). A scale of 20 gives exactly 1 symbol for the largest category and less than 1 for smaller ones — too little detail. A scale is chosen so the graph is accurate and legible; scales of 2, 5, and 10 are most common because they align with skip-counting fluency."

- question: "If you don't read the key of a scaled picture graph, you cannot correctly interpret the data shown."
  type: true-false
  answer: true
  explanation: "The key tells you what each symbol is worth. Without it, you have no way to know whether a star means 1, 2, 5, or 10 units. Two graphs with identical arrangements of symbols but different keys represent completely different data. Reading the key is the first required step — it is the decoding tool that connects symbol count to real quantity."

- question: "A scaled picture graph and a regular picture graph (where each symbol = 1) generally show the same number of symbols for the same data."
  type: true-false
  answer: false
  explanation: "Scaling is specifically designed to reduce the number of symbols. If 30 students chose soccer and the scale is 5, you draw only 6 symbols. On a one-to-one graph, you'd draw 30 symbols. The fewer symbols are the whole point of scaling — it makes large data sets manageable and graphs with many categories readable without becoming crowded."

- question: "A student looks at a scaled picture graph, counts 4 sun symbols in the 'sunny days' row, and says 'there were 4 sunny days.' What information is the student missing, and why does it change the answer?"
  type: short-answer
  answer: "The student hasn't checked the key (scale). Without knowing what one sun symbol represents, you cannot determine the actual count. If the key says 1 sun = 3 days, then 4 suns represent 4 × 3 = 12 sunny days, not 4. The key is essential: you must multiply the number of symbols by the scale value to get the real quantity."
  explanation: "Every symbol in a scaled picture graph is a compressed representation of multiple items. The key is the tool that decompresses it. Skipping the key and reading symbols as single units treats a scaled graph like a one-to-one graph — which will give the wrong answer whenever the scale is anything other than 1."
```

## Explainer

You already know how to read and make picture graphs where each picture stands for exactly one thing — one vote, one book, one student. That works well for small amounts. But what if you surveyed 60 students about their favorite sport? You'd need to draw 60 symbols. That's slow, crowded, and hard to read. The **scale** solves this problem by letting each symbol stand for more than one item.

The most important piece of any scaled picture graph is the **key** (sometimes called a legend). The key tells you what one symbol is worth — for example, "★ = 5 students." Without the key, the graph is unreadable. When you look at a graph and see 4 stars in the "soccer" row, the key is what tells you that means 4 × 5 = 20 students. This multiplication step is what distinguishes a scaled graph from a simple one-to-one graph.

Your skip-counting knowledge is the engine here. If each symbol equals 2, you read the graph by skip-counting by 2s: 2, 4, 6, 8... If each symbol equals 5, you skip-count by 5s: 5, 10, 15, 20... The scale you use is usually chosen to match what you can skip-count easily. That's why scales of 2, 5, and 10 are most common — you already have those sequences memorized.

When you create your own scaled picture graph, you have to make a key decision upfront: what should the scale be? If your largest category has 30 responses and you want no more than 10 symbols in a row, you'd choose a scale of at least 3. If all your counts are multiples of 5, a scale of 5 keeps everything clean. **Designing the scale** requires thinking about the data before you draw — another example of the "organize first, graph second" principle. A well-chosen scale makes a graph that's both accurate and easy to read.
