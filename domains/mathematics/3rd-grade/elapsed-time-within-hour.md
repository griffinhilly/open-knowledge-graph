---
id: elapsed-time-within-hour
title: Elapsed Time Within an Hour
domain: mathematics
course: 3rd-grade
prerequisites:
- id: elapsed-time-simple-2nd
  type: hard
- id: telling-time-5-minute-intervals-2nd
  type: hard
builds-toward:
- elapsed-time
tags:
- time
- measurement
- elapsed-time
stage: concrete-operations
status: draft
---

# Elapsed Time Within an Hour

## Core Idea
Elapsed time is the duration between a start time and end time. From 2:15 PM to 2:45 PM, 30 minutes have elapsed. Students count on by 5s or 1s on a clock face, or subtract end time from start time, to find elapsed time within one hour.

## Questions

```yaml
- question: "A movie starts at 3:20 PM and ends at 3:55 PM. How many minutes did the movie last?"
  type: multiple-choice
  options:
    - "25 minutes"
    - "35 minutes"
    - "75 minutes"
    - "45 minutes"
  answer: 1
  explanation: "Elapsed time within the same hour can be found by subtracting the start minutes from the end minutes: 55 − 20 = 35 minutes. You can also count on by 5s: 3:20 → 3:25 → 3:30 → 3:35 → 3:40 → 3:45 → 3:50 → 3:55 = 7 hops of 5 = 35 minutes. The hour (3) stays the same throughout, so only the minutes change. Option A (25) is a common error from 55 − 30 or 50 − 20; option D (45) would be the duration from 3:10 to 3:55."

- question: "Leah solves this problem: 'A timer starts at 4:10 and stops at 4:40. How long did it run?' She answers '4:40.' What is Leah confusing?"
  type: multiple-choice
  options:
    - "She is confused about which hand to read on the clock"
    - "She is reporting the end time (a clock reading — a position in time) instead of the elapsed time (a duration — how long passed, which is 30 minutes)"
    - "She forgot to count by 5s and used a different strategy"
    - "She subtracted incorrectly: 40 − 10 should give 30, not 4:40"
  answer: 1
  explanation: "Leah answered 'what time did it stop?' rather than 'how long did it run?' These are two completely different questions. '4:40' is a clock reading — it tells you a position in time. '30 minutes' is elapsed time — it tells you a duration, how much time passed. The elapsed time is 40 − 10 = 30 minutes, not 4:40. This confusion between clock readings and durations is the central misconception the topic addresses."

- question: "'30 minutes' is an example of elapsed time, while '2:45 PM' is an example of a clock reading."
  type: true-false
  answer: true
  explanation: "Elapsed time is a duration — it measures how long something lasted and is expressed as a quantity of time (30 minutes, 1 hour, 2 hours and 15 minutes). A clock reading is a position in time — it tells you when something happened (2:45 PM). These are fundamentally different kinds of information. The explainer states: 'elapsed time is a duration, not a clock reading.' This distinction becomes especially important when elapsed time spans across the hour mark."

- question: "If a film starts at 1:15 and ends at 1:50, the elapsed time is 1:50 — you simply read the end time from the clock."
  type: true-false
  answer: false
  explanation: "The elapsed time is 35 minutes (50 − 15 = 35), not 1:50. Reporting the end time as the elapsed time is the core misconception this topic addresses. '1:50' tells you *when* the film ended; '35 minutes' tells you *how long* it ran. These are fundamentally different. A film that ends at 1:50 could have lasted 5 minutes (if it started at 1:45) or 50 minutes (if it started at 1:00) — the end time alone tells you nothing about duration."

- question: "Explain the difference between a 'clock reading' and 'elapsed time.' Why is this distinction important when solving time problems?"
  type: short-answer
  answer: "A clock reading is a position in time — it tells you when something happened (e.g., 3:15 PM). Elapsed time is a duration — it tells you how long something lasted (e.g., 45 minutes). Clock readings describe moments; elapsed time describes intervals between moments. The distinction is important because elapsed time problems ask for a duration, not a time — the answer should be in minutes (or hours and minutes), not in 'o'clock' form. Confusing the two leads to reporting the end time as the answer rather than calculating the difference between start and end."
  explanation: "The explainer states: 'elapsed time is a duration, not a clock reading. When you say 30 minutes passed, you are describing how long something lasted, not pointing to a moment in time.' This distinction matters even more for later problems that cross the hour mark, where reasoning about positions vs. amounts of time becomes essential for avoiding errors."
```

## Explainer

You already know how to read times to five-minute intervals — you can look at a clock and say "it is 2:15" or "it is 2:45." **Elapsed time** asks a different question: not *what time is it*, but *how long did something take*? The difference between a start time and an end time is the elapsed time, and it is measured in minutes (or hours and minutes for longer durations).

The most reliable strategy is **counting on** using the clock face. Imagine the minute hand starting at 2:15. You want to reach 2:45. Count by 5s as the minute hand sweeps forward: 2:15 → 2:20 → 2:25 → 2:30 → 2:35 → 2:40 → 2:45. That is 6 hops of 5 minutes each: 6 × 5 = **30 minutes** elapsed. You can also use a number line, marking the start time at one end and hopping forward in jumps of 5 or 10 until you reach the end time.

A second strategy is **subtraction**. If start is 2:15 and end is 2:45, subtract the minutes: 45 − 15 = 30 minutes. This works cleanly when both times share the same hour. Be careful if the minutes would require borrowing (e.g., 3:05 to 3:52) — in those cases, counting on is often easier and less error-prone.

The key concept to hold onto is that elapsed time is a **duration**, not a clock reading. When you say "30 minutes passed," you are describing how long something lasted, not pointing to a moment in time. This distinction becomes essential when you later work with problems that cross the hour mark — knowing whether you are tracking a position on a clock versus an amount of time is what keeps the reasoning straight.
