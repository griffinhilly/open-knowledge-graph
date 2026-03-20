---
id: elapsed-time
title: Elapsed Time
domain: mathematics
course: 1st-grade
prerequisites:
- id: telling-time-to-half-hour
  type: hard
tags:
- time
- duration
stage: pre-formal
status: draft
---

# Elapsed Time

## Core Idea
Elapsed time measures how much time passes from a start time to an end time. Students count forward by hours and half-hours to find how much time has passed.

## Questions

```yaml
- question: "You start playing at 2:00 and stop at 4:30. How much time elapsed?"
  type: multiple-choice
  options:
    - "4 hours and 30 minutes — the end time on the clock"
    - "2 hours and 30 minutes — counted forward from 2:00 to 4:30"
    - "2 hours — from 2:00 to 4:00 only"
    - "30 minutes — the difference between :00 and :30"
  answer: 1
  explanation: "Elapsed time is a duration, not a clock reading. Count forward in steps: 2:00 → 3:00 is 1 hour, 3:00 → 4:00 is another hour, 4:00 → 4:30 is a half-hour — total 2 hours 30 minutes. The most common error is reporting the end time (4:30) as the answer, confusing 'what time is it?' with 'how long did it take?'"

- question: "School starts at 8:30 and ends at 3:00. A student subtracts and writes '3:00 − 8:30 = the school day.' What is the correct elapsed time?"
  type: multiple-choice
  options:
    - "3 hours — from 8:30 to 11:30"
    - "5 hours — from 8:30 to 1:30"
    - "6 hours and 30 minutes — counted forward by whole hours then a half-hour"
    - "8 hours and 30 minutes — the start time in minutes"
  answer: 2
  explanation: "Count forward from 8:30: each step to the next half-hour or hour mark is one jump. 8:30 → 9:30 (1 hr) → 10:30 (2 hr) → 11:30 (3 hr) → 12:30 (4 hr) → 1:30 (5 hr) → 2:30 (6 hr) → 3:00 (half-hour more) = 6 hours 30 minutes. Subtracting clock numbers without careful regrouping leads to errors — the count-forward strategy is more reliable at this stage."

- question: "If a movie starts at 4:00 and ends at 6:30, the elapsed time is 6 hours and 30 minutes."
  type: true-false
  answer: false
  explanation: "6:30 is the end time shown on the clock — not the elapsed time. The elapsed time is how long the movie lasted, found by counting forward: 4:00 → 5:00 (1 hour) → 6:00 (2 hours) → 6:30 (half-hour more) = 2 hours 30 minutes. This is the central misconception in elapsed time: confusing the clock reading at the end with the duration from start to finish."

- question: "Elapsed time is always a duration measured in hours and minutes, not a time you could read off a clock face."
  type: true-false
  answer: true
  explanation: "Elapsed time answers the question 'how long did something take?' — the result is always a duration like '2 hours' or '1 hour 30 minutes.' A clock reading like '3:00' or '4:30' answers 'what time is it right now?' These are different kinds of answers. Recognizing this distinction is the first and most important step in elapsed-time reasoning."

- question: "A student says the answer to 'How long did you sleep if you fell asleep at 8:30 and woke at 7:00 the next morning?' is '7:00.' What is wrong with that answer, and how would you find the correct elapsed time?"
  type: short-answer
  answer: "7:00 is the wake-up time on the clock — it is not the duration of sleep. To find elapsed time, count forward from 8:30: 8:30 → 9:30 → 10:30 → 11:30 → 12:30 → 1:30 → 2:30 → 3:30 → 4:30 → 5:30 → 6:30 → 7:00. That is 10 hours and 30 minutes of sleep."
  explanation: "The error is treating the end time as the elapsed time. Elapsed time requires counting the gap between start and end — it is a measurement of duration, like measuring length between two points, not the value at one endpoint."
```

## Explainer

You already know how to read a clock and tell time to the half-hour. You know that 3:00 means the short hand points to 3 and the long hand points to 12, and that 3:30 means it is halfway to 4. **Elapsed time** is a new kind of question: not "what time is it?" but "how long did something take?" These are different questions, and it helps to see why.

Imagine you start eating lunch at 12:00 and finish at 12:30. You did not eat the number 12 or the number 30 — you ate for **30 minutes**. Elapsed time is always a duration, measured in hours and minutes, not a time on the clock. To find it, you count forward from the start time to the end time: 12:00 → 12:30 is one half-hour jump, so 30 minutes passed.

A clock face is actually a very helpful tool for counting elapsed time. Picture the long hand at 12 for a start time of 1:00. If you want to find how much time passes until 3:00, you count: from 1:00 to 2:00 is one hour, from 2:00 to 3:00 is another hour — two hours total. Each time the short hand moves from one number to the next, one hour passes. Each time the long hand moves from 12 to 6 (or 6 to 12), a half-hour passes. Counting these jumps gives you the elapsed time.

Try it with a story: you start playing at 2:00 and stop at 4:30. Count forward — 2:00 to 3:00 is one hour, 3:00 to 4:00 is another hour, 4:00 to 4:30 is a half-hour. That is two and a half hours of playtime. The key habit is always to start at the earlier time and count forward to the later time in steps you know well — whole hours first, then half-hours.
