---
id: tally-chart-data-collection-1st
title: Creating Tally Charts
domain: mathematics
course: 1st-grade
prerequisites:
- id: tally-charts
  type: hard
- id: data-and-graphs-intro
  type: soft
builds-toward:
- picture-graphs
- bar-graphs-3rd
tags:
- data
- representation
- tally-marks
stage: concrete-operations
status: draft
---

# Creating Tally Charts

## Core Idea
Tally marks (||||) record data quickly. Groups of 5 (||||/) make counting and reading easier. A tally chart organizes categories with their tallies (e.g., favorite color: red, blue, green) and helps answer 'how many?' questions.

## Questions

```yaml
- question: "A student draws ||||/ |||| under 'Blue' in a tally chart. How many votes does Blue have?"
  type: multiple-choice
  options:
    - "2 — there are 2 groups drawn"
    - "5 — only the complete bundle of five counts"
    - "9 — one bundle of five plus four single marks"
    - "8 — four marks plus four marks, ignoring the diagonal"
  answer: 2
  explanation: "The diagonal slash through four vertical marks creates a bundle of five. After it come four more individual marks. Total: 5 + 4 = 9. Option A misreads the number of groups as individual votes. Option D ignores the bundle-of-five structure entirely. The whole point of the diagonal mark is to visually separate groups of five so they can be counted quickly."

- question: "Why do tally marks use a diagonal fifth mark (||||/) instead of just five vertical marks (|||||)?"
  type: multiple-choice
  options:
    - "It is traditional but has no practical advantage"
    - "The diagonal groups marks into visible bundles of five, making totals fast to read"
    - "Five vertical marks would be confused with Roman numeral V"
    - "Diagonal marks take less space on the page"
  answer: 1
  explanation: "The diagonal cross groups the four vertical marks into a clearly visible unit of five. When reading the chart, you count bundles of five (using familiar skip-counting-by-fives) and add any remainders. Without this grouping, you'd count every individual mark from scratch. The visual bundling is the core efficiency of the system."

- question: "A tally chart is built while data is being collected, with each mark recorded as each observation happens."
  type: true-false
