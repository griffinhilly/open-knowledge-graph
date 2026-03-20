---
id: skip-counting-by-100s
title: Skip Counting by 100s
domain: mathematics
course: 2nd-grade
prerequisites:
- id: skip-counting-by-10s
  type: hard
- id: place-value-hundreds
  type: soft
builds-toward:
- three-digit-number-forms
- number-line-to-1000
- mental-math-add-subtract-hundreds
tags:
- skip-counting
- hundreds
- patterns
- place-value
stage: concrete-operations
status: validated
---

# Skip Counting by 100s

## Core Idea
Skip counting by 100s means adding 100 each time: 100, 200, 300, 400, … 1000. The hundreds digit increases by 1 each step while the tens and ones digits remain unchanged — just as skip counting by 10s changes only the tens digit. This pattern reinforces the structure of the base-ten system and builds readiness for mental addition and subtraction of hundreds.

## How It's Best Learned
Use a hundreds chart extended to 1000. Begin from 0 and count forward; then start from numbers like 250 and count forward or backward by 100. Connect to place-value blocks: adding one flat each time.

## Common Misconceptions
- Changing the tens or ones digits when skip counting (e.g., 345, 445, 555 instead of 445, 545).
- Stopping at 900 and not continuing to 1000.
- Confusing skip counting by 10s and by 100s.

## Questions

```yaml
- question: "Starting from 347, what is the next number when skip counting by 100s?"
  type: multiple-choice
  options:
    - "357 — add 10 to the tens digit"
    - "447 — add 1 to the hundreds digit only"
    - "457 — add 1 to both the hundreds and tens digits"
    - "348 — add 1 to the ones digit"
  answer: 1
  explanation: "When skip counting by 100s, only the hundreds digit increases by 1. The tens digit (4) and ones digit (7) stay exactly the same. 347 → 447. Adding 100 affects only the hundreds place because 100 is exactly one unit in that column — it does not 'spill over' into the tens or ones."

- question: "A student skip counts by 100s starting at 235 and writes: 235, 345, 455, 565. What error is the student making?"
  type: multiple-choice
  options:
    - "The jumps are too small — each should be 200"
    - "The student is changing the tens and ones digits, which should stay fixed at 35"
    - "The student skipped a number — 245 should come before 345"
    - "There is no error — the sequence is correct"
  answer: 1
  explanation: "When skip counting by 100s, the tens and ones digits never change. The correct sequence is 235, 335, 435, 535. The student is incorrectly incrementing other digits: 35 → 45 → 55 → 65. This is a common confusion — the pattern of changing digits when counting by 10s (which affects only the tens digit) is being misapplied here, where only the hundreds digit should change."

- question: "When skip counting by 100s starting from 263, the digits '63' never change throughout the sequence."
  type: true-false
  answer: true
  explanation: "Correct. Adding 100 adds exactly 1 to the hundreds column and nothing to any other column. So 263 → 363 → 463 → 563 → 663 → … The tens digit (6) and ones digit (3) remain fixed throughout. This is a direct consequence of place value: 100 is one unit in the hundreds place only."

- question: "Skip counting by 100s is essentially the same as skip counting by 10s, just with bigger numbers."
  type: true-false
  answer: false
  explanation: "While both patterns share the same structure (only one digit changes), they affect different columns. Skip counting by 10s changes the tens digit while the ones digit stays fixed. Skip counting by 100s changes the hundreds digit while both the tens and ones digits stay fixed. They are analogous but not the same — each operates at its own place-value level."

- question: "When skip counting by 100s starting from 382, which digit changes and which digits stay the same? Why?"
  type: short-answer
  answer: "Only the hundreds digit (3) changes: 382, 482, 582, 682 … The tens digit (8) and ones digit (2) stay the same throughout. This is because adding 100 adds exactly 1 unit to the hundreds column. Since 1 hundred does not affect the tens or ones columns at all, those digits remain untouched."
  explanation: "This question targets the core insight: place value means each column is independent. Adding a value that fits entirely in one column only changes that column. Understanding this makes mental math with hundreds (382 + 100 = 482) feel obvious rather than procedural — you are just incrementing one digit."
```

## Explainer

You already know how to skip count by 10s: 10, 20, 30, 40 … Each jump adds one ten, so the **tens digit** ticks up by one each time while the ones digit stays put. Skip counting by 100s works exactly the same way, one level up. Each jump adds one hundred, so the **hundreds digit** ticks up by one each time — while both the tens digit and the ones digit stay completely unchanged. If you start at 247 and count by 100s, you get 347, 447, 547, 647 — only the first digit changes.

This is a direct consequence of how place value works, your prerequisite knowledge. In our base-ten system, each place is worth ten times the place to its right. Adding 100 affects only the hundreds place because 100 is exactly one unit in that column. It is like adding one flat base-ten block each time: the stacks of rods and the individual cubes never change — only the count of flats grows. Seeing this with physical blocks makes the pattern obvious.

The sequence 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 is the "skeleton" of three-digit numbers. It also sets you up for mental math: adding or subtracting 100 from any number is quick because you are just changing one digit. 638 + 100 = 738; 638 − 100 = 538. No carrying, no borrowing — just a one-digit update in the hundreds place. Practicing this sequence forward and backward, and starting from numbers other than zero (like 250, 350, 450 …), builds the flexibility you will need for that mental arithmetic and for understanding the number line up to 1000.
