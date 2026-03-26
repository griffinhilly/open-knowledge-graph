---
id: telling-time-minute-3rd
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
- minutes
- analog-clock
stage: concrete-operations
status: validated
---

# Telling Time to the Minute

## Core Idea
On an analog clock, the hour hand shows the hour and the minute hand shows minutes. Count by 5s along the clock (5, 10, 15, ..., 55) for the minute hand, then add extra minutes by 1s.

## How It's Best Learned
Practice with real clocks and clock manipulatives. Draw and label clock faces.

## Common Misconceptions
Confusing hour and minute hands; not counting minutes correctly; difficulty near the hour.

## Questions

```yaml
- question: "The minute hand on a clock is three tick marks past the 7. What is the minute count?"
  type: multiple-choice
  options:
    - "7 minutes — the hand is near the 7"
    - "35 minutes — skip-count to the 7: 5, 10, 15, 20, 25, 30, 35"
    - "38 minutes — skip-count to the 7 (35), then count on 3 more"
    - "37 minutes — the hand is between 35 and 40"
  answer: 2
  explanation: "The skip-counting scaffold gets you to 35 (the 7 on the clock face). Then you count individual tick marks: one past the 7 = 36, two past = 37, three past = 38. The method is always the same: skip-count by 5s to the last number the hand passed, then count individual marks from there. Option B stops at 35 but ignores the three extra ticks."

- question: "The hour hand is between the 3 and the 4, closer to the 4. The minute hand points to the 10. What time is it?"
  type: multiple-choice
  options:
    - "4:50 — the hour hand is close to the 4"
    - "3:50 — the hour hand is between the 3 and the 4, so the hour is 3"
    - "3:10 — the minute hand is near the 10, which means 10 minutes"
    - "4:10 — the hour hand is almost on the 4"
  answer: 1
  explanation: "The hour hand shows *which hour you are in*, not which number it's nearest to. If it's anywhere between the 3 and the 4, the hour is 3 — you haven't yet reached 4 o'clock. The minute hand on the 10 means skip-count to 10: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50. The time is 3:50. When the hour hand looks close to the next number, it means you're near the end of that hour — not that the next hour has started."

- question: "Most tick mark on a clock face represents 5 minutes, so you should count by 5s for most mark when reading time to the minute."
  type: true-false
  answer: false
  explanation: "Each of the 60 tick marks represents exactly 1 minute. The twelve numbered positions on the clock each represent multiples of 5 (5, 10, 15... 60), which is why skip-counting by 5s works to get to those positions quickly. But between the numbers, every individual tick mark is 1 minute. The skill of telling time to the minute means counting each of those individual marks after your last five-minute skip."

- question: "If the hour hand is anywhere between the 6 and the 7, the correct hour to read is 6."
  type: true-false
  answer: true
  explanation: "The hour hand moves continuously throughout the hour. Any position between two numbers means you are *in* the earlier hour — you haven't reached the next one yet. Between 6 and 7 means it's 6-something. Only when the hour hand is exactly on the 7 (at 7:00 precisely) does the hour become 7. This is especially important when the hour hand is very close to the next number — it still belongs to the earlier hour."

- question: "Explain the two-step method for reading the minute hand when it falls between two numbers on the clock face."
  type: short-answer
  answer: "Step 1: Skip-count by 5s to the last numbered position the minute hand passed (e.g., if it's past the 4 but before the 5, count 5, 10, 15, 20). Step 2: Count individual tick marks from that number to where the hand actually points. Add those single minutes to the skip-count total."
  explanation: "This two-step method uses skip-counting as a scaffold and then adds precision. You do not start over from scratch — you use the five-minute marks as checkpoints and finish with single-minute counting. For example, if the hand is two ticks past the 4: skip-count to 20, then count 21, 22. The time is __:22. This is exactly how mental arithmetic builds on earlier skills."
```

## Explainer

You already know how to read an analog clock to the nearest 5 minutes. Telling time to the minute extends that skill one step further: instead of stopping at the nearest labeled tick mark, you count individual minutes between the marks. The **minute hand** still travels the same clock face, but now every single mark — all 60 of them — counts as exactly one minute.

The trick is to use your skip-counting by fives as a scaffold. When the minute hand is between two numbers on the clock face, first count by fives to the number it just passed, then count individual minutes from there to where the hand actually points. If the minute hand is two ticks past the 4, count: 5, 10, 15, 20 (landing on the 4), then 21, 22. The time is __ :22. You're not starting over from scratch — you're finishing with single-minute precision where your five-minute reading left off.

The **hour hand** provides the first number in the time. Remember that it moves continuously throughout the hour, never sitting exactly on a number unless it's precisely o'clock. If the hour hand is anywhere between the 2 and the 3, the hour is 2, regardless of where the minute hand points. The two hands work together: the hour hand answers "which hour are we in?" and the minute hand answers "how many minutes into that hour?"

Common confusion arises near the top of the clock. When the minute hand is close to 12, the hour hand is near transition — it may look almost on the next number. If the minute hand is past the 6 (more than 30 minutes have passed), the hour hand has traveled over halfway toward the next number, so it can look deceptively close to it. Reading the hour hand carefully — asking "which two numbers is it *between*?" rather than "which number is it near?" — prevents misidentifying the hour when the hands are in awkward positions.
