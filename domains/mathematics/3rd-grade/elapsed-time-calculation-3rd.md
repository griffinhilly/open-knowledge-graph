---
id: elapsed-time-calculation-3rd
title: Finding Elapsed Time
domain: mathematics
course: 3rd-grade
prerequisites:
- id: telling-time-minute-3rd
  type: hard
- id: elapsed-time-within-hour-3rd
  type: hard
- id: telling-time-three-digit-precision-3rd
  type: hard
tags:
- elapsed-time
- duration
- time-intervals
stage: concrete-operations
status: validated
---

# Finding Elapsed Time

## Core Idea
Elapsed time is how much time passes between two times. If an activity starts at 10:00 and ends at 10:45, the elapsed time is 45 minutes. Count on or calculate the difference.

## How It's Best Learned
Use timelines and number lines. Count on from start to end time by 5s and 1s.

## Common Misconceptions
Confusing start and end times; incorrectly adding instead of subtracting; times crossing the hour.

## Questions

```yaml
- question: "A class starts at 1:15 and ends at 3:00. A student subtracts: 3:00 − 1:15 = 1:85. Why is this answer wrong?"
  type: multiple-choice
  options:
    - "The student should have subtracted minutes before hours"
    - "Time is not base-10 — hours have 60 minutes, not 100 — so '85 minutes' is not a valid result"
    - "The student forgot to convert hours to seconds first"
    - "3:00 − 1:15 cannot be calculated and must be estimated from a clock"
  answer: 1
  explanation: "Regular subtraction treats numbers as base-10 (10 units = 1 of the next unit). But time uses base-60 for minutes: 60 minutes = 1 hour, not 100. Subtracting 1:15 from 3:00 as if they were decimals produces a nonsense answer because '85 minutes' is not a unit in the time system. The reliable approach is a number-line strategy: jump to the next clean hour, then count remaining minutes."

- question: "What is the best strategy for finding elapsed time from 9:40 to 10:25?"
  type: multiple-choice
  options:
    - "Subtract: 10:25 − 9:40 = 0:85, so 85 minutes"
    - "Jump from 9:40 to 10:00 (20 minutes), then from 10:00 to 10:25 (25 minutes) — total: 45 minutes"
    - "Convert both times to minutes since midnight, then subtract"
    - "Count forward from 9:40 by individual minutes until reaching 10:25"
  answer: 1
  explanation: "The jump-to-the-hour strategy breaks elapsed time into manageable chunks that respect the 60-minute structure of hours. From 9:40 to 10:00 is 20 minutes (60 − 40 = 20). From 10:00 to 10:25 is 25 minutes. Total: 20 + 25 = 45 minutes. This approach avoids the base-10 error and is far less error-prone than counting by individual minutes. Option A is the classic mistake: treating time notation like base-10 decimal numbers."

- question: "Drawing a number line is a useful strategy for elapsed time problems because it makes the passage of time visible and helps avoid base-10 errors."
  type: true-false
  answer: true
  explanation: "A number line makes elapsed time spatial: mark the start, mark the end, and the distance between them is the elapsed time. More importantly, a number line naturally leads you to the jump-to-the-hour strategy — you can see the nearest clean hour between start and end, and the problem becomes two simple additions. This visual approach prevents the mistake of treating time like base-10 subtraction, where students produce answers like '1:85' or '0:85.'"

- question: "To find elapsed time from 2:30 to 4:00, you can subtract: 4:00 − 2:30 = 1:70, so 1 hour and 70 minutes."
  type: true-false
  answer: false
  explanation: "This is the base-10 subtraction error. '1:70' would mean 1 hour and 70 minutes — but hours only contain 60 minutes, so this is not valid. The correct calculation using the jump strategy: from 2:30 to 3:00 is 30 minutes; from 3:00 to 4:00 is 60 minutes; total = 90 minutes, or 1 hour and 30 minutes. Regular subtraction on time notation always risks this error because minutes are base-60, not base-10."

- question: "Why doesn't regular subtraction work for elapsed time, and what should you do instead?"
  type: short-answer
  answer: "Regular subtraction assumes a base-10 system where borrowing works in groups of 10. But time uses base-60 for minutes — there are 60 minutes in an hour, not 100. Subtracting 1:15 from 3:00 as if it were 300 − 115 gives 185, which is meaningless as a time. Instead, use a number line and jump to the next clean hour: from 1:15 to 2:00 is 45 minutes, from 2:00 to 3:00 is 60 minutes, total 105 minutes = 1 hour 45 minutes."
  explanation: "The foundational issue is that time is not a decimal system. Hours have 60 minutes; you cannot treat '3:00 − 1:15' the way you'd treat 300 − 115. The jump strategy works because it decomposes the problem into segments that each respect the 60-minute hour: getting to the next clean hour is always a subtraction within 60 (easy); then whole hours are added; then remaining minutes are added. Each step is simple; the combination handles any elapsed time problem correctly."
```

## Explainer

You already know how to tell time to the minute — reading a clock face and saying "it's 10:35." Elapsed time asks a different question: not "what time is it now?" but "how long did something take?" If a movie starts at 1:15 and ends at 3:00, elapsed time asks: how many minutes or hours passed between those two points?

The trap students fall into is treating this like ordinary subtraction — subtracting 1:15 from 3:00. But time doesn't work like regular numbers, because hours have 60 minutes, not 100. Trying to do "3:00 minus 1:15" as if it were "300 minus 115" gives the wrong answer. The reliable approach is to use a **timeline** (or open number line): mark the start time, mark the end time, and figure out the jumps in between.

Here is a reliable strategy: **jump to the next clean hour, then count the remaining minutes.** Starting at 1:15, count up to 2:00 — that's 45 minutes. Then from 2:00 to 3:00 is exactly 60 minutes. Total: 45 + 60 = 105 minutes, or 1 hour and 45 minutes. This approach works because it breaks the problem into chunks you can count confidently, rather than trying to do arithmetic on hours and minutes simultaneously.

The same strategy works in reverse: if you know the start time and how long something lasts, you add the elapsed time to find the end time. Start at 9:40, activity lasts 35 minutes — jump from 9:40 to 10:00 (20 minutes), then add the remaining 15 minutes to get 10:15. The key habit to build is **drawing the number line** instead of doing the calculation in your head. Visualizing time as a line, where you move right as time passes, turns an abstract problem into something you can see and count.
