---
id: telling-time-to-hour-half-hour-2nd
title: Telling Time to the Hour and Half Hour
domain: mathematics
course: 2nd-grade
prerequisites:
- id: telling-time-to-hour-1st
  type: hard
builds-toward:
- telling-time-5-minute-intervals-2nd
- elapsed-time-simple-2nd
tags:
- time
- hour
- half-hour
- clock
stage: concrete-operations
status: draft
---

# Telling Time to the Hour and Half Hour

## Core Idea
On an analog clock, the hour hand points to the hour, and the minute hand points to 12 at the hour. At half past, the minute hand points to 6. Time is read as, for example, 'three thirty' and written as 3:30.

## Questions

```yaml
- question: "The minute hand points to the 6 and the hour hand is halfway between 4 and 5. What time is it?"
  type: multiple-choice
  options:
    - "4:60"
    - "5:30 — because the hour hand is moving toward 5"
    - "4:30 — because the hour that started was 4, and 30 minutes have passed"
    - "Half past 5"
  answer: 2
  explanation: "When the minute hand is at 6, you are 30 minutes into the current hour — not yet at the next hour. The hour hand moving halfway between 4 and 5 confirms this: it started at 4 and is traveling toward 5, but has not arrived. The time is 4:30, or 'half past four.' Options B and D make the common error of reading the hour the hand is moving *toward* rather than the hour that already began. The hour number in the time is always the hour that started, not the one coming next."

- question: "Why does the hour hand appear halfway between two numbers when the minute hand points to the 6?"
  type: multiple-choice
  options:
    - "Because the clock is slightly out of alignment and needs to be corrected"
    - "Because the hour hand always moves to the midpoint between numbers to indicate 'half'"
    - "Because 30 minutes is exactly half of 60 minutes, so the hour hand has traveled halfway through its full one-hour journey"
    - "Because the numbers on the clock face are spaced unevenly near the bottom"
  answer: 2
  explanation: "The hour hand makes one complete revolution every 12 hours, taking 60 minutes to move from one number to the next. At 30 minutes — exactly half of 60 — the hour hand has traveled exactly half the distance between two numbers. This is the definition of 'half past': half of an hour has elapsed. Understanding *why* the hour hand is between numbers (not just that it is) prevents the confusion of not knowing which of the two numbers to read."

- question: "At half past the hour, exactly 30 minutes have passed since the last whole hour began."
  type: true-false
  answer: true
  explanation: "This is the definition of 'half past.' An hour contains 60 minutes, and half of 60 is 30. When the minute hand has swept from the 12 down to the 6, it has traveled half the clock face — 30 minutes. This is why 'half past three' and '3:30' mean the same thing. The phrase 'half past' literally means 'halfway past the hour,' which is 30 minutes."

- question: "When reading a half-past time, you should look at the hour hand and read the number it is closest to pointing at directly."
  type: true-false
  answer: false
  explanation: "At half past, the hour hand is positioned halfway between two numbers — equidistant from both — so 'closest to pointing at' is ambiguous and would lead you to read either number. The rule is: read the *lower* (earlier) number, because the hour that is 'in progress' is the one that already started. At 4:30, the hour hand is between 4 and 5 — you read 4, not 5, because the 4 o'clock hour began 30 minutes ago and hasn't ended yet."

- question: "When the minute hand points to the 6, how do you figure out the hour number to write, and why might a student accidentally write the wrong hour?"
  type: short-answer
  answer: "Look at the hour hand: it will be halfway between two numbers. Read the lower (earlier) of those two numbers — that is the hour that has been 'in progress' for the past 30 minutes. A student might write the wrong hour by reading the larger number (the upcoming hour) instead of the one that already started. For example, with the hour hand between 7 and 8, the time is 7:30, not 8:30 — because the 7 o'clock hour started 30 minutes ago."
  explanation: "The two-step check helps avoid this error: first, confirm the minute hand is at 6 (so you know it's a :30 time); then read the hour hand and choose the earlier of the two numbers it is between. The hour doesn't change until the minute hand returns all the way to 12."
```

## Explainer

You already know that when the long (minute) hand points to 12, you read the short (hour) hand directly: if it points to 5, it is 5 o'clock. Now you are adding a second position to recognize: when the minute hand points straight down to the 6, exactly 30 minutes have passed since the hour began. We call this **half past** because 30 minutes is exactly half of the 60 minutes in an hour.

Think of the clock face as a circle divided in two. The top half (from 12 down to 6 going clockwise) takes 30 minutes for the minute hand to travel. The bottom half (from 6 back up to 12) takes another 30 minutes. When the minute hand is at 6, you are exactly halfway through the hour. Look at the hour hand: it has moved halfway between two numbers. If it is halfway between 3 and 4, the time is **3:30** — three thirty, or half past three. If it is halfway between 8 and 9, the time is 8:30.

Writing the time uses a colon: the number before the colon is the hour, and the two digits after the colon are the minutes. On the hour, you write :00 (as in 5:00); at the half hour, you write :30 (as in 5:30). When you read a clock, use a two-step check: first look at the minute hand to figure out whether you are at the hour (:00) or the half hour (:30), then read the hour hand to get the hour number. With practice, both positions become instant to recognize, and you will be ready to move on to times at 5-minute intervals.
