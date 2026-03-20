---
id: measurement-scales-psychology
title: Levels of Measurement
domain: psychology
course: research-methods-psychology
prerequisites:
- id: variables-in-psychology
  type: hard
- id: mean-median-mode
  type: soft
- id: measures-of-spread
  type: soft
builds-toward:
- reliability-in-measurement
- inferential-statistics-psychology
tags:
- nominal
- ordinal
- interval
- ratio
- scales-of-measurement
stage: formal-systems
status: validated
---

# Levels of Measurement

## Core Idea
Stevens's four levels of measurement — nominal, ordinal, interval, and ratio — determine which statistical operations are meaningful for a given variable. Nominal data consist of unordered categories (e.g., diagnosis type). Ordinal data have rank order but unequal intervals (e.g., Likert ratings). Interval data have equal intervals but no true zero (e.g., temperature in Celsius). Ratio data have a true zero and all arithmetic operations apply (e.g., reaction time). The level of measurement constrains which statistics can be legitimately computed.

## How It's Best Learned
Classify common psychology measures by level and explain what operations are permitted. For example: Why can you compute a mean for IQ scores but not for diagnostic categories?

## Common Misconceptions
- Ordinal scales are often treated as interval in psychology (e.g., Likert scales), which is a recognized but debated practice.
- A ratio scale is not 'better' data — it is simply more informative because it allows more mathematical operations.

## Questions

```yaml
- question: "A researcher asks participants to identify their preferred study location from four options: library, dorm room, café, or coffee shop. What is the most statistically appropriate measure of central tendency for this variable?"
  type: multiple-choice
  options: ["Mean", "Median", "Mode", "Standard deviation"]
  answer: 2
  explanation: "Study location is a nominal variable — it consists of unordered categories with no numeric meaning. You cannot rank, add, or average category labels. The only appropriate measure of central tendency for nominal data is the mode (the most frequently chosen category). Standard deviation is a measure of spread, not central tendency."

- question: "Because Celsius temperature has equal intervals between degrees, it is meaningful to say that 40°C is twice as hot as 20°C."
  type: true-false
  answer: false
  explanation: "Celsius is an interval scale, not a ratio scale, because it lacks a true zero point — 0°C does not mean 'no heat.' Ratio statements (twice as much, half as much) require a true zero. On the Kelvin scale, which has an absolute zero, 400K would indeed be twice 200K. The equal intervals of Celsius allow subtraction (40°C is 20° warmer than 20°C), but not ratios."

- question: "Why does a true zero matter for ratio-level measurement?"
  type: short-answer
  answer: "A true zero means the absence of the measured property, which makes ratio comparisons meaningful — you can say one value is twice or half another."
  explanation: "Without a true zero, ratios are mathematically undefined. Reaction time measured in milliseconds has a true zero (0ms = no time elapsed), so 400ms is genuinely twice 200ms. IQ, by contrast, lacks a true zero — an IQ of 0 doesn't mean 'no intelligence,' so saying someone is 'twice as intelligent' is not meaningful. The true zero is what licenses multiplication and division across measurements."
```

## Explainer

Stevens's four levels of measurement — nominal, ordinal, interval, and ratio — form a hierarchy of informativeness, with each level permitting all the operations of the level below it plus additional ones. Understanding which level a variable belongs to determines which statistics are legitimate and, more practically, protects you from drawing conclusions that the data cannot support.

Nominal variables are the most restricted: they are labels with no inherent order. Whether you code biological sex as M/F or 1/2 is arbitrary — the numbers carry no mathematical meaning. The only operations that make sense are counting (how many in each category?) and identifying the mode. Ordinal variables add rank order: finishing 1st, 2nd, and 3rd tells you who was faster, but not by how much. The gap between 1st and 2nd place might be a tenth of a second while the gap between 2nd and 3rd is three minutes. Because intervals are unequal and unknown, computing a mean on ordinal data requires an assumption — often unjustified — that the intervals are approximately equal.

Interval variables have equal, known intervals between all values, which makes subtraction meaningful. The difference between 70°F and 60°F is the same as the difference between 90°F and 80°F. But interval scales lack a true zero, so ratios are meaningless: 80°F is not "twice as hot" as 40°F in any physical sense. Ratio variables add the true zero, unlocking all arithmetic operations. Reaction time, height, and weight are ratio variables because zero means the genuine absence of the quantity, making it valid to say someone ran twice as fast or weighed half as much.

In psychology, the level of measurement is rarely clear-cut. Likert scales (Strongly Disagree to Strongly Agree, scored 1–5) are formally ordinal — we don't know whether the psychological distance from 1 to 2 equals the distance from 4 to 5. Yet computing means on Likert items is standard practice, defended on practical and simulation-based grounds. This is not sloppy — it is a recognized and debated pragmatic choice. Understanding the formal classification helps you reason about when these shortcuts are likely to mislead you.
