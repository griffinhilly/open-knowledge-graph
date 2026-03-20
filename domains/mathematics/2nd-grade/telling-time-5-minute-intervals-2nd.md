---
id: telling-time-5-minute-intervals-2nd
title: Telling Time by 5-Minute Intervals
domain: mathematics
course: 2nd-grade
prerequisites:
- id: telling-time-to-hour-half-hour-2nd
  type: hard
- id: skip-counting-by-5s
  type: hard
builds-toward:
- elapsed-time-simple-2nd
tags:
- time
- 5-minute-intervals
- clock
stage: concrete-operations
status: draft
---

# Telling Time by 5-Minute Intervals

## Core Idea
Clock faces divide into 5-minute intervals. From 12 to 1 is 5 minutes, 1 to 2 is 5 minutes, etc. Skip counting by 5s helps determine minutes: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60. The minute hand moves to each number for every 5 minutes.

## Questions

```yaml
- question: "The minute hand on a clock points to the 4. A student says the time is 'something:4' — meaning 4 minutes past the hour. What error did the student make, and what is the correct number of minutes?"
  type: multiple-choice
  options:
    - "No error — the minute hand at 4 means exactly 4 minutes past the hour"
    - "The student forgot to multiply by 5; the minute hand at 4 means 20 minutes past the hour"
    - "The student should use the hour hand, not the minute hand, to count the minutes"
    - "The student should count by 2s from 12 to the minute hand's position"
  answer: 1
  explanation: "Each number on the clock face marks a 5-minute interval, not a 1-minute mark. To find the minutes, skip count by 5s from 12 to where the minute hand points: 5 (at 1), 10 (at 2), 15 (at 3), 20 (at 4). Reading the clock number directly as minutes is the most common error when learning 5-minute interval time."

- question: "The hour hand is just past the 7, and the minute hand points to the 9. What time is it?"
  type: multiple-choice
  options:
    - "7:09"
    - "7:90"
    - "7:45"
    - "9:07"
  answer: 2
  explanation: "Skip count by 5s from 12 to the 9: 5, 10, 15, 20, 25, 30, 35, 40, 45 — that's 45 minutes. The hour hand just past 7 tells you it's in the 7 o'clock hour. So the time is 7:45. Option A (7:09) is the classic error of reading the number 9 directly as '9 minutes' rather than skip-counting to get 45."

- question: "When the minute hand points to the 6, it means 6 minutes have passed in that hour."
  type: true-false
  answer: false
  explanation: "The minute hand at 6 means 30 minutes have passed (6 × 5 = 30), not 6 minutes. The 6 is the halfway mark — 'half past' the hour. Every number on the clock represents a 5-minute gap, so the number the minute hand points to must always be multiplied by 5 to get the actual minutes."

- question: "Skip counting by 5s is useful for reading the minute hand because each number on the clock face represents a 5-minute interval."
  type: true-false
  answer: true
  explanation: "This is exactly the connection between skip counting and clock reading. There are 12 numbers on the clock, and each gap between consecutive numbers is 5 minutes. 12 × 5 = 60 minutes in one full hour. Because the clock is built on 5-minute intervals, skip counting by 5s from 12 to the minute hand's position gives the exact number of minutes."

- question: "How do you find the number of minutes shown on an analog clock? Why can't you just read the number the minute hand is pointing to?"
  type: short-answer
  answer: "You find the minutes by skip counting by 5s, starting from 12, up to the number the minute hand is pointing at. You can't read the number directly because each number on the clock represents 5 minutes, not 1 minute. For example, the minute hand at 3 means 15 minutes (5 + 5 + 5), not 3 minutes."
  explanation: "The clock face is designed with only 12 numbers to represent 60 minutes, so each number must stand for 5 minutes. The minute hand's position tells you how many 5-minute intervals have passed, which is why skip counting by 5s — a skill learned separately — is exactly the right tool for reading it."
```

## Explainer

You already know how to tell time to the hour and half hour, and you know how to skip count by 5s. This topic connects those two skills: the minute hand on a clock is literally a skip-counter by fives. Every time the minute hand moves from one number to the next, exactly 5 minutes pass. Twelve numbers on the clock face × 5 minutes each = 60 minutes in one full hour.

The key is reading the **minute hand** using skip counting. When the minute hand points to the 3, you don't say "3 minutes" — you count by fives: 5 (at 1), 10 (at 2), 15 (at 3). So the minute hand at 3 means 15 minutes. When the minute hand points to 7, count: 5, 10, 15, 20, 25, 30, 35 — that's 35 minutes. The **hour hand** tells you which hour you're in; the minute hand (read by skip counting) tells you how many minutes past that hour.

A useful anchor is the **half hour**: when the minute hand points straight down at 6, you've counted 30 minutes (5×6 = 30). You already knew that 6:30 means "half past six." Now you know why — the minute hand has traveled exactly half of its journey around the clock. Similarly, when the minute hand is at 3, it's "quarter past" the hour (15 minutes = one quarter of 60). When it's at 9, it's "quarter to" the next hour (45 minutes gone, 15 to go).

To read any time: first look at the hour hand and identify which hour it just passed. Then skip count by 5s from 12 to wherever the minute hand points. For example, if the hour hand is just past 4 and the minute hand points to 8, count 5–10–15–20–25–30–35–40: the time is 4:40. With practice, reading the minute hand becomes automatic, and you'll stop needing to count every step — you'll just see "at the 7" and instantly know "35 minutes."
