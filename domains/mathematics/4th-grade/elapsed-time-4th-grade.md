---
id: elapsed-time-4th-grade
title: Elapsed Time
domain: mathematics
course: 4th-grade
prerequisites:
- id: multi-digit-subtraction
  type: soft
- id: telling-time-to-5-minutes
  type: soft
- id: telling-time-to-minute
  type: soft
builds-toward: []
tags:
- measurement
- time
- problem-solving
stage: concrete-operations
status: validated
---
# Elapsed Time

## Core Idea
Elapsed time is the amount of time that passes between a start time and an end time. Calculating elapsed time is tricky because time uses a base-60 system (60 minutes in an hour, 60 seconds in a minute) rather than base-10. Students learn to find elapsed time, end times, and start times in problems like "A movie starts at 2:45 PM and is 1 hour 35 minutes long. When does it end?" This is a practical life skill and also reinforces flexible reasoning with non-decimal number systems.

## How It's Best Learned
Use open number lines: jump from the start time to the end time in convenient chunks (jump to the next hour, then add remaining minutes). Analog clocks help students see the movement of time visually. Practice with real schedules (bus timetables, class schedules, cooking times). Avoid teaching a single algorithm -- flexible "jump" strategies build better number sense.

## Common Misconceptions
- Treating time as base-10 (computing 2:45 + 1:35 = 3:80 instead of 4:20).
- Confusing AM and PM when crossing noon or midnight.
- Difficulty with "counting backwards" to find a start time.

## Questions

```yaml
- question: "A movie starts at 2:45 PM and lasts 1 hour and 35 minutes. A student adds the times directly and gets 3:80 PM. What is wrong with this answer?"
  type: multiple-choice
  options:
    - "The student forgot to add the hours portion correctly"
    - "3:80 is not a real time — minutes go up to 60, so the correct answer is 4:20 PM"
    - "The student should have subtracted 1:35 instead of adding it"
    - "The answer is almost right; 3:80 PM simply means 3 hours and 80 minutes"
  answer: 1
  explanation: "Time uses base-60: 60 minutes make one hour, not 100. When the raw addition gives 3:80, that 80 minutes must be converted — 80 minutes = 1 hour + 20 minutes. So 3 hours + 1 hour = 4 hours, with 20 minutes remaining: 4:20 PM. Option D is wrong because there is no such thing as 80 minutes on a clock. The base-60 trap is exactly why raw arithmetic on clock times fails."

- question: "Why is the 'jump to the next whole hour first' strategy so effective for elapsed time problems?"
  type: multiple-choice
  options:
    - "It avoids needing to know any multiplication"
    - "It provides a clean anchor point that keeps you working with real clock positions, preventing base-60 errors"
    - "It only works for problems where the elapsed time is less than one hour"
    - "It only applies when working with AM times, not PM"
  answer: 1
  explanation: "Whole hours are anchor points where minutes reset to zero — clean, familiar positions on the clock. By jumping to the next whole hour first, you never have to do arithmetic that might push minutes past 60. Each jump stays within the rules of the base-60 system, so you can't accidentally produce '3:80' or similar nonsense. The strategy works for any elapsed time, including crossing noon (AM to PM)."

- question: "Using a jump strategy on a number line (e.g., jumping to the next whole hour, then adding remaining minutes) prevents the base-60 errors that happen with raw arithmetic."
  type: true-false
  answer: true
  explanation: "Yes — the jump strategy keeps you anchored to real, valid clock times throughout the calculation. Each intermediate step is a real time you could see on a clock face. This sidesteps the base-60 problem entirely because you never do raw addition on clock digits. You work with the clock's actual structure rather than pretending minutes behave like base-10 digits."

- question: "2:45 plus 1 hour and 35 minutes equals 3:80, because you simply add the hours (2+1=3) and the minutes (45+35=80) separately."
  type: true-false
  answer: false
  explanation: "This is the classic base-60 error. When minutes add up to 60 or more, you must carry: 45 + 35 = 80 minutes = 1 hour and 20 minutes. Adding that extra hour to the 3 gives 4 hours total, so the correct answer is 4:20. '3:80' violates the base-60 system — there is no such time. You cannot treat clock arithmetic like ordinary base-10 addition."

- question: "Why does calculating elapsed time require a different approach than ordinary addition? Describe what goes wrong when you treat clock times as base-10 numbers."
  type: short-answer
  answer: "Time uses base-60 for minutes (60 minutes = 1 hour), not base-10. If you treat clock digits like ordinary numbers and add 2:45 + 1:35, you get 3:80 — but 80 minutes doesn't exist on a clock. The minutes column 'overflows' at 60, not at 100. The fix is to use strategies that stay anchored to real clock positions, like jumping to the next whole hour first, so you never produce an invalid time."
  explanation: "The base-60 system is the core reason elapsed time requires special treatment. In base-10, every column overflows at 10; in time, the minutes column overflows at 60. Raw arithmetic ignores this and produces impossible times. Jump strategies work because they use the structure of the clock directly — you move from one real time to the next, always staying within valid clock positions, so the base-60 constraint is automatically satisfied."
```

## Explainer

**Elapsed time** is the amount of time that passes between two moments — the answer to "how long did that take?" or "when does it finish?" You already know how to read a clock to the minute, which means you can identify start and end times precisely. What makes elapsed time tricky is that time uses a **base-60 system**: 60 minutes make an hour, not 100. That single fact breaks every instinct you have built around our usual base-10 number system.

The most powerful tool for elapsed time is an **open number line**. Draw a line, mark the start time on the left, and jump toward the right in convenient chunks — first to the next whole hour, then in larger hour-sized hops, then in smaller minute-sized adjustments at the end. For example, to find how long it takes from 10:45 AM to 1:20 PM: jump 15 minutes to get to 11:00 (a clean hour boundary), then jump 2 hours to get to 1:00 PM, then jump 20 minutes to 1:20 PM. Total: 15 min + 2 hr + 20 min = 2 hours 35 minutes. Notice how hitting the "clean hour" first simplifies everything — it is the same strategy as making change by counting up to a round dollar. The number line makes the jumps visible and prevents the base-60 trap.

The base-60 trap looks like this: a movie starts at 2:45 and lasts 1 hour 35 minutes, so you try to compute 2:45 + 1:35. If you treat the minutes like a normal base-10 addition, you get 3:80 — but 3:80 is not a real time. The correct answer is 4:20, because when the minutes exceed 60, you carry one hour and keep the remainder: 45 + 35 = 80 minutes = 1 hour and 20 minutes, then 2 + 1 + 1 = 4 hours. The jump strategy sidesteps this problem by keeping you anchored to real clock positions throughout, rather than doing raw arithmetic that might violate the 60-minute boundary. Once you are fluent with forward jumps, you can run the same process in reverse — jumping backwards from an end time to find when something started.
