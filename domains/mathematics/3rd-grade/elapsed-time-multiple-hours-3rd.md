---
id: elapsed-time-multiple-hours-3rd
title: Elapsed Time Across Hours
domain: mathematics
course: 3rd-grade
prerequisites:
- id: elapsed-time-within-hour-3rd
  type: hard
- id: elapsed-time-calculation-3rd
  type: soft
tags:
- elapsed-time
- time
- hours
stage: concrete-operations
status: validated
---
# Elapsed Time Across Hours

## Core Idea
When elapsed time spans more than one hour, students add hours and minutes separately. For example, from 2:15 PM to 5:30 PM is 3 hours and 15 minutes. Number lines and timelines help visualize the passage of time.

## Questions

```yaml
- question: "A student calculates elapsed time from 3:40 PM to 6:10 PM and arrives at '2 hours and 90 minutes.' What should the correct final answer be?"
  type: multiple-choice
  options:
    - "2 hours 90 minutes — this is already correct"
    - "2 hours 30 minutes — drop the extra 60 minutes"
    - "3 hours 30 minutes — because 90 minutes = 1 hour and 30 minutes, so 2 hours + 90 min = 3 hours 30 min"
    - "4 hours — round up when minutes exceed 60"
  answer: 2
  explanation: "Time uses base-60: there are 60 minutes in an hour, not 100. When minutes total 90, you must regroup: 90 = 60 + 30, so 90 minutes = 1 hour and 30 minutes. Adding that to the 2 hours already counted gives 3 hours and 30 minutes. This regrouping step is the most common source of error in elapsed-time problems, and it only applies because minutes work on a 60-unit cycle, not a 10-unit one."

- question: "Why is it helpful to jump to the nearest whole hour first when calculating elapsed time across multiple hours?"
  type: multiple-choice
  options:
    - "Because you must always start counting from 12:00 on the clock"
    - "Whole-hour marks are natural breakpoints in the clock's structure, allowing you to add hours and minutes separately and cleanly without mixing them"
    - "Because minutes and hours cannot be added together in the same calculation"
    - "Whole hours are the only units you are allowed to count in 3rd grade"
  answer: 1
  explanation: "Clock time is structured around whole hours as natural dividing points. Starting from 2:15, jumping first to 3:00 (45 minutes), then counting whole hours to 5:00 (2 hours), then adding remaining minutes to 5:30 (30 minutes) keeps the hours and minutes separate and easy to combine. Trying to count all 195 minutes in one go is error-prone; using the clock's own structure breaks the problem into manageable pieces."

- question: "When calculating elapsed time, if your minutes total reaches 75, you must convert it: 75 minutes = 1 hour and 15 minutes."
  type: true-false
  answer: true
  explanation: "Because there are 60 minutes in an hour, any minutes total of 60 or more must be regrouped. 75 = 60 + 15, so 75 minutes equals 1 additional hour plus 15 remaining minutes. Failing to regroup is the most common elapsed-time error and produces answers that are off by exactly one hour."

- question: "Elapsed time uses the same regrouping rules as regular addition — just like adding two-digit numbers."
  type: true-false
  answer: false
  explanation: "Regular addition regroups at 10 (10 ones = 1 ten). Elapsed time regroups at 60 (60 minutes = 1 hour). This is the critical difference: time is base-60, not base-10. A student who applies base-10 thinking to time might write '1 hour 30 minutes' when the real answer is '1 hour 30 minutes' only if the minutes happened to be exactly 90 — but the regrouping threshold is always 60, not 100. Every elapsed-time calculation must check whether minutes have reached 60 or more, not 100 or more."

- question: "Why can't you use the same regrouping rules from regular addition when working with hours and minutes? Give a specific example."
  type: short-answer
  answer: "Regular addition regroups when a column reaches 10 (because our number system is base-10). Time regroups when minutes reach 60, because there are 60 minutes in an hour — not 100. For example: if you calculate 45 minutes + 35 minutes, you get 80 minutes. In base-10 addition, 80 is a valid two-digit number. But in time, 80 minutes must be regrouped: 80 = 60 + 20, so 80 minutes = 1 hour and 20 minutes. Ignoring the base-60 structure and treating it like base-10 would incorrectly leave 80 minutes as-is."
  explanation: "This distinction trips up students who are fluent in base-10 arithmetic because they apply a familiar rule in an unfamiliar context. Recognizing when a rule does NOT transfer — and understanding why — is a key part of mathematical reasoning. The base-60 structure of time is one of several places in math where the usual base-10 intuitions break down."
```

## Explainer

You already know how to find elapsed time when the start and end are within the same hour. If something starts at 2:10 and ends at 2:45, you count up by minutes: 35 minutes have passed. That strategy works perfectly inside one hour. But what do you do when time crosses the hour mark — or spans several hours?

The key idea is to **break the problem into steps**, using whole-hour marks as natural stopping points. Suppose you want to find the elapsed time from 2:15 PM to 5:30 PM. Rather than calculating it all at once, use the clock's structure: from 2:15 to 3:00 is 45 minutes (completing the current hour); from 3:00 to 5:00 is exactly 2 whole hours; from 5:00 to 5:30 is 30 more minutes. Add those pieces: 45 minutes + 2 hours + 30 minutes. Combining: 2 hours and 75 minutes — but 75 minutes is 1 hour and 15 minutes, so the total is **3 hours and 15 minutes**. You can also count whole hours directly (2:15 to 5:15 = exactly 3 hours, then 15 more minutes to 5:30), which is often even faster.

A **number line** makes this visual. Place the start time on the left and the end time on the right. Draw labeled jumps for whole hours, then a smaller jump for the remaining minutes. The total elapsed time is the sum of all your jumps. This builds directly on your experience using number lines to add — the same tool, now applied to time instead of whole numbers.

The most important thing to watch: time does not use base-ten grouping — there are **60 minutes** in an hour, not 100. If your calculation produces 75 minutes, you must regroup: 75 minutes = 1 hour and 15 minutes (since 75 = 60 + 15). Always check whether your minutes total reaches 60 or more, and convert if so. Missing this regrouping is the most common source of errors in elapsed-time problems, and checking it takes only a moment.
