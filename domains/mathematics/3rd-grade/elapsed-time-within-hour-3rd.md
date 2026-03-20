---
id: elapsed-time-within-hour-3rd
title: Calculating Elapsed Time Within an Hour
domain: mathematics
course: 3rd-grade
prerequisites:
- id: elapsed-time-simple-2nd
  type: soft
- id: telling-time-three-digit-precision-3rd
  type: hard
builds-toward:
- elapsed-time-calculation-3rd
tags:
- elapsed-time
- time
- calculation
stage: concrete-operations
status: draft
---

# Calculating Elapsed Time Within an Hour

## Core Idea
Elapsed time is the amount of time that passes between a start time and end time. Within an hour, students can count up by fives and ones, or subtract minute values, to find elapsed time.

## Questions

```yaml
- question: "A movie clip starts at 2:14 and ends at 2:47. A student counts up: 2:14 → 2:15 (1 min), then by fives to 2:45 (30 more min), then adds 2 ones to reach 2:47. What is the elapsed time?"
  type: multiple-choice
  options:
    - "61 minutes, by adding 14 + 47"
    - "33 minutes, by counting the total minutes added"
    - "27 minutes, by subtracting 47 - 14 incorrectly"
    - "The elapsed time cannot be found without knowing the hour"
  answer: 1
  explanation: "Counting up: 1 + 30 + 2 = 33 minutes. The student hops from the start time forward in chunks — 1 minute to reach the nearest 5, then by fives, then individual ones — keeping a running total. This mirrors making change: count forward from the price until you reach the amount paid. Since both times are in the same hour (2:__), subtracting 47 - 14 = 33 also works as a shortcut."

- question: "A class activity begins at 2:08 and ends at 2:44. Which approach correctly finds the elapsed time?"
  type: multiple-choice
  options:
    - "44 + 8 = 52 minutes"
    - "Subtracting the minute values: 44 - 8 = 36 minutes"
    - "Count backward from 2:44 to 2:08, which gives 36 minutes"
    - "Elapsed time cannot be found because the hour digit is the same in both times"
  answer: 1
  explanation: "Since both times are within the same hour, you can directly subtract the minute values: 44 - 8 = 36 minutes. This arithmetic shortcut gives the same answer as counting up. Option A adds instead of subtracts. Counting backward (C) works but is harder than counting forward. Option D has it backwards — same-hour times are the easy case, not a barrier."

- question: "Elapsed time is the amount of time between a start time and an end time — it answers the question 'how long did that take?'"
  type: true-false
  answer: true
  explanation: "Correct. Elapsed time is the duration between two clock readings. It is found by identifying the start and end times and calculating the gap — either by counting up from start to end, or by subtracting minute values when both times fall within the same hour."

- question: "You can always find elapsed time by subtracting the start minute value from the end minute value."
  type: true-false
  answer: false
  explanation: "Subtracting minute values only works cleanly when both times are within the same hour. If a task starts at 1:48 and ends at 2:15, subtracting 48 from 15 gives a negative number, which is wrong. For cross-hour problems, counting up is the safer strategy: count from 1:48 to 2:00 (12 minutes), then 2:00 to 2:15 (15 minutes) = 27 minutes total."

- question: "A game starts at 3:17 and ends at 3:52. Explain how to use the counting-up strategy to find the elapsed time."
  type: short-answer
  answer: "Start at 3:17 and hop forward in chunks: +3 minutes to reach 3:20, then count by fives — 3:25, 3:30, 3:35, 3:40, 3:45, 3:50 (30 more minutes), then +2 to reach 3:52. Total: 3 + 30 + 2 = 35 minutes."
  explanation: "Counting up is like making change — start at the beginning and add chunks until you reach the end, keeping a running total. The clock's 5-minute marks make counting by fives natural. Add all the chunks together to get the elapsed time. You can verify with subtraction: 52 - 17 = 35 minutes."
```

## Explainer

**Elapsed time** is the gap between a start time and an end time — the answer to "how long did that take?" You already know how to read a clock to the nearest minute, which means you can identify both the start time and the end time precisely. The new skill is calculating the difference between them.

The most reliable strategy within a single hour is **counting up**: start at the start time, and hop forward in convenient chunks until you reach the end time, keeping a running total of the minutes you have added. Because a clock face is divided into groups of 5 minutes, counting up by fives is natural. For example, if a movie clip starts at 2:14 and ends at 2:47, you can count up from 2:14 — hop to 2:15 (1 minute), then count by fives: 2:20, 2:25, 2:30, 2:35, 2:40, 2:45 (that is 31 minutes so far), then add 2 more ones to reach 2:47. Total: 33 minutes. The counting-up approach mirrors what you do naturally when making change — you count forward from the price to the amount paid rather than subtracting directly.

Once you are comfortable counting up, you can also **subtract the minute values** directly: 47 − 14 = 33. This arithmetic shortcut gives the same answer and can be faster when the numbers work out cleanly. The key condition for this shortcut is that both times are within the same hour — start and end times have the same hour digit. When you cross from one hour into the next, the subtraction gets more complicated, and the counting-up strategy remains the safest option. For now, staying within one hour keeps the focus on understanding what elapsed time means and building fluency with minute arithmetic before tackling the harder cross-hour problems you will encounter next.
