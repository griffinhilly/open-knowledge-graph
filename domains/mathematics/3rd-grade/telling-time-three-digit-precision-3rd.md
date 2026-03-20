---
id: telling-time-three-digit-precision-3rd
title: Telling Time to the Minute
domain: mathematics
course: 3rd-grade
prerequisites:
- id: telling-time-to-5-minutes
  type: hard
builds-toward:
- elapsed-time-calculation-3rd
tags:
- time
- clocks
- minute
stage: concrete-operations
status: draft
---

# Telling Time to the Minute

## Core Idea
Telling time to the minute requires reading both the hour hand and minute hand. The minute hand pointing to a number tells how many groups of 5 minutes have passed (e.g., pointing to 6 means 30 minutes). Between numbers, count individual minute marks.

## Questions

```yaml
- question: "The minute hand on a clock is pointing 3 tick marks past the 7. What are the minutes?"
  type: multiple-choice
  options:
    - "7 minutes — the hand is pointing near 7"
    - "35 minutes — because 7 × 5 = 35, plus 3 = 38"
    - "38 minutes — because 7 × 5 = 35, plus 3 individual tick marks = 38"
    - "73 minutes — because the hand is at 7 and 3 ticks"
  answer: 2
  explanation: "The two-step method: multiply the numbered section by 5 to get the base (7 × 5 = 35 minutes), then count the individual tick marks past it (3 more). 35 + 3 = 38 minutes. Option B makes an arithmetic error (shows the method but gets the wrong answer). Option A ignores the tick marks entirely and misreads the number as the minutes. Option D adds the digits rather than using the base-5 system."

- question: "It is 1:59 on a clock. One minute later, what time does the clock show?"
  type: multiple-choice
  options:
    - "1:60"
    - "2:00"
    - "1:100"
    - "2:60"
  answer: 1
  explanation: "Time uses a base-60 system for minutes: once you reach 60 minutes, you don't write 1:60 — instead, you carry over to the next hour, making it 2:00. This is unlike our base-10 number system where 9 + 1 = 10 stays within the same 'place.' In base-60, 60 minutes = 1 hour, so the minute count resets to 00 and the hour advances by 1."

- question: "To find the exact minutes shown by a clock's minute hand, you multiply the last numbered marker the hand passed by 5, then add the number of individual tick marks past that number."
  type: true-false
  answer: true
  explanation: "This two-step method is the standard approach for reading to the minute. Each number on the clock represents 5 minutes (since 60 ÷ 12 = 5), and the small tick marks between numbers each represent 1 minute. So: base = number × 5, then add the individual ticks. For example, 2 ticks past the 9 = 9 × 5 + 2 = 47 minutes."

- question: "The hour hand always points exactly at a number, making it easy to read the hour precisely."
  type: true-false
  answer: false
  explanation: "The hour hand moves continuously throughout the hour — it doesn't jump from number to number at the stroke of each hour. At 3:30, the hour hand is halfway between 3 and 4, not pointing at either. The correct method is to identify the most recent number the hour hand has *passed*, not the nearest number it points to. This is why reading the hour hand requires some judgment, especially when the minute hand is past 30."

- question: "Explain the two steps needed to read the exact minutes from a clock's minute hand."
  type: short-answer
  answer: "Step 1: identify the most recent numbered marker the minute hand has passed, and multiply that number by 5 to get the base minutes. Step 2: count how many individual tick marks the hand has traveled past that number, and add them to the base. For example, if the hand is 4 ticks past the 3: 3 × 5 = 15, plus 4 = 19 minutes."
  explanation: "The two-step method works because the clock is divided into 12 sections of 5 minutes each (5 × 12 = 60), with small tick marks for the individual minutes within each section. Recognizing this structure — major divisions of 5 plus individual minutes — is what makes reading to the exact minute systematic rather than guesswork."
```

## Explainer

You can already read time to 5-minute intervals — you know that when the minute hand points at the 6, that's 30 minutes, and when it points at the 9, that's 45 minutes. Each number on a clock face represents 5 minutes of the minute hand's journey. Between any two neighboring numbers, there are 5 small tick marks, each representing 1 minute. Reading time to the minute means being precise about exactly which tick mark the minute hand is on, not just which number it's near.

Here's how to read any time: first, identify the hour from the hour hand (whichever number it has most recently passed). Then read the minute hand in two steps. Ask "which numbered section has the minute hand just passed?" — multiply that number by 5 to get the base minutes. Then count how many individual tick marks past that number the hand has traveled. Add those two amounts together for the exact minutes. For example, if the minute hand is 2 ticks past the 4, that's 4 × 5 = 20, plus 2 = 22 minutes.

The language of time has some quirks worth knowing. When minutes are 0–30, we say the time directly: 8:22 is "eight twenty-two." When minutes are past 30, we might say "twenty-two minutes to nine" (60 − 38 = 22 minutes remaining). Both describe the same moment. Clock reading to the minute is also your first encounter with a **base-60** counting system — unlike our base-10 number system where ten ones make a ten, here sixty minutes make one hour. That's why 60 minutes doesn't roll over to 1:60 but instead to 2:00. Keeping this structure in mind will help enormously when you calculate elapsed time — how much time has passed between two clock readings.
