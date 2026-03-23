---
id: picture-graphs-read-create-2nd
title: Reading and Creating Picture Graphs
domain: mathematics
course: 2nd-grade
prerequisites:
- id: picture-graphs
  type: hard
- id: picture-graphs-3rd
  type: soft
tags:
- graphs
- picture-graphs
- data
stage: concrete-operations
status: validated
---

# Reading and Creating Picture Graphs

## Core Idea
A picture graph uses symbols to show data. Each symbol may represent 1 or more items (key shows the value). To read, count the symbols in each row; to create, decide on a symbol and draw rows to show data.

## Questions

```yaml
- question: "A picture graph has a key showing ★ = 5 students. The 'soccer' row has 6 stars. How many students chose soccer?"
  type: multiple-choice
  options:
    - "6 — count the symbols in the row"
    - "11 — add the symbol count (6) to the key value (5)"
    - "30 — multiply the symbol count (6) by the key value (5)"
    - "1 — divide the symbol count (6) by the key value (5), rounding down"
  answer: 2
  explanation: "When a key says each symbol represents N items, you must multiply the symbol count by N to recover the actual data value. 6 symbols × 5 students per symbol = 30 students. Reporting just the symbol count (6) is the most common reading error — it ignores the key entirely and gives an answer that is 5 times too small."

- question: "A student is making a picture graph where the largest category has 40 data points. Which key value produces the most readable graph?"
  type: multiple-choice
  options:
    - "Each symbol = 1 (shows exact counts with no multiplication required)"
    - "Each symbol = 10 (at most 4 symbols per row — clean and easy to scan)"
    - "Each symbol = 100 (fewer than 1 symbol for most categories)"
    - "Each symbol = 3 (gives about 13 symbols for the largest row)"
  answer: 1
  explanation: "A key of 10 gives at most 4 symbols in the largest row, which is clean and easy to count at a glance. A key of 1 requires drawing 40 symbols in one row — cluttered and hard to count. A key of 100 would give less than 1 symbol for any category under 100, making the graph unreadable. A key of 3 gives ~13 symbols per row for the largest category, which is workable but busier than necessary. Choosing a key that keeps rows between 2–10 symbols is the standard design goal."

- question: "To find the number of students who chose 'dogs' in a picture graph, you should count the symbols in that row and report that count as your answer."
  type: true-false
  answer: false
  explanation: "This is only correct if the key says each symbol = 1. If the key says each symbol = 3 (or any number greater than 1), you must multiply the symbol count by the key value to get the actual data. Skipping the multiplication step is the most common picture-graph reading error — it produces an answer that is too small by a factor equal to the key value."

- question: "When comparing two rows in a picture graph where each symbol = 3, you should multiply each row's symbol count by 3 before comparing, not compare the symbol counts directly."
  type: true-false
  answer: true
  explanation: "Because the key applies equally to every row, comparing symbol counts directly gives the same relative ordering as comparing the actual values — the row with more symbols always has more data. So in practice, for simple 'which is more' comparisons, you don't have to multiply first. However, when asked 'how many more' or 'what is the total', you must apply the key. The habit of always applying the key before making any numerical comparison prevents errors on these calculation questions."

- question: "Why do picture graphs sometimes use a key where each symbol represents more than one item, instead of drawing one symbol per item?"
  type: short-answer
  answer: "A scaled key lets you represent large data values with far fewer symbols, making the graph easier to read at a glance. If one category has 40 items and you draw one symbol per item, that row contains 40 symbols — visually cluttered and tedious to count. With a key of 'each symbol = 10', you draw only 4 symbols, which is clean and instantly scannable. The cost is that readers must multiply when interpreting the graph, but the visual clarity gained is worth it for large data sets. Choosing the right key value is a design decision about how to represent information efficiently."
  explanation: "This question tests whether the student understands why the key exists at all — not just how to use it. The key is a compression device: it lets a small visual (a few symbols) represent a large quantity. Understanding this 'why' also explains why the key value matters: too small a value gives too many symbols (cluttered), too large a value gives too few symbols to compare meaningfully."
```

## Explainer

You already know that a picture graph uses symbols to represent data. Now you're working with something more powerful: a **key** that says each symbol stands for more than one item. Instead of drawing 14 stars for 14 votes, you could draw 7 stars and write "each ★ = 2 votes." The graph takes less space and is easier to scan — and the key gives readers what they need to recover the exact numbers.

Reading such a graph requires two steps: count the symbols in a row, then multiply by the key value. If the "cats" row has 5 paw prints and the key says each paw print = 3 students, then 5 × 3 = 15 students chose cats. If a row has 4 symbols and each symbol = 10, then 4 × 10 = 40. You're reversing the compression that was applied when the graph was made. This multiplication step is small but important — skipping it and just reporting the symbol count is one of the most common errors when reading picture graphs with scaled keys.

Creating a picture graph adds a decision you don't face when just reading one: **what should the key value be?** A good key keeps the number of symbols manageable — ideally between 2 and 10 per row — so the graph is readable at a glance. If the largest data value is 30, a key of "each symbol = 5" gives at most 6 symbols per row (clean and clear). A key of "each symbol = 1" would produce rows of 30 symbols (cluttered and hard to count). Choosing the right scale is a real design decision, and it's your first encounter with a skill that recurs throughout data work: representing information efficiently without losing accuracy.

When comparing rows, look for the row with the most symbols (most popular) and least symbols (least popular). You can also find differences: if one row has 6 symbols and another has 4, and the key is ×2, then one category has 12 and the other has 8 — a difference of 4. Always apply the key before comparing numbers, not after.
