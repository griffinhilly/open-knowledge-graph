---
id: two-digit-addition-no-regrouping-2nd
title: Two-Digit Addition Without Regrouping
domain: mathematics
course: 2nd-grade
prerequisites:
- id: addition-within-20
  type: hard
- id: place-value-tens-and-ones
  type: hard
- id: decomposing-two-digit-numbers
  type: soft
builds-toward:
- addition-two-digit-regrouping-2nd
tags:
- addition
- two-digit
- algorithm
stage: concrete-operations
status: draft
---

# Two-Digit Addition Without Regrouping

## Core Idea
Adding two-digit numbers without regrouping means adding ones to ones and tens to tens separately. For example, 23 + 14 = (20 + 10) + (3 + 4) = 30 + 7 = 37. This foundation precedes regrouping situations.

## Explainer

You already know two things that make this possible: how to add numbers within 20, and how place value splits any two-digit number into tens and ones. Two-digit addition without regrouping combines both skills at once.

The central idea is **column independence**: ones only talk to ones, and tens only talk to tens. When you see 23 + 14, think of it as two separate mini-problems stacked side by side. The ones column: 3 + 4 = 7. The tens column: 2 + 1 = 3 (meaning 20 + 10 = 30). Put them together: 37. You never need to mix the columns, because the ones total (7) stays safely under 10.

You can also think of it as decomposing numbers — a skill you've practiced. Break 23 into 20 + 3, and break 14 into 10 + 4. Then rearrange: (20 + 10) + (3 + 4) = 30 + 7 = 37. Both approaches — the column method and the expanded-form method — give the same answer because they both respect place value.

The phrase "without regrouping" is the key qualifier here. **Regrouping** becomes necessary when the ones column sums to 10 or more — for instance, 27 + 15 has ones summing to 12, which spills over into the tens place. This lesson deliberately stays in cases where that doesn't happen (ones digits sum to 9 or less), so you can build fluency with the column procedure before adding the extra step of carrying. Master the clean cases first; then regrouping is just one additional rule on top of exactly what you're doing now.
