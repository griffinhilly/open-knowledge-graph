---
id: slope-concept
title: Slope of a Line
domain: mathematics
course: algebra-1
prerequisites:
- id: coordinate-plane-intro
  type: hard
- id: unit-rates
  type: hard
- id: dividing-integers
  type: hard
- id: coordinate-plane-all-four-quadrants
  type: soft
- id: function-tables
  type: soft
- id: proportional-relationships
  type: soft
builds-toward:
- slope-intercept-form
- point-slope-form
- parallel-and-perpendicular-slopes
tags:
- slope
- rate-of-change
- linear
- graphing
stage: abstract-reasoning
status: validated
---
# Slope of a Line

## Core Idea
Slope measures the steepness and direction of a line. It is the ratio of vertical change (rise) to horizontal change (run) between any two points on the line: m = (y₂ − y₁) / (x₂ − x₁). A positive slope means the line rises from left to right; a negative slope means it falls. A slope of zero is a horizontal line, and an undefined slope (division by zero) is a vertical line. Slope is identical to the concept of rate of change — it tells you how much y changes for each unit increase in x. Slope is one of the most important concepts in algebra because it characterizes every linear relationship.

## How It's Best Learned
Start with physical models: ramps, staircases, hills. Count rise and run on a graph before using the formula. Plot several lines with different slopes and build intuition for what "steeper" means numerically. Practice computing slope from two points, from a graph, and from a table. Include all four cases: positive, negative, zero, and undefined.

## Common Misconceptions
- Computing run/rise instead of rise/run.
- Subtracting coordinates in inconsistent order: (y₂ − y₁) / (x₁ − x₂) gives the wrong sign.
- Thinking a vertical line has slope of zero (it is undefined) or a horizontal line has undefined slope (it is zero).

## Questions

```yaml
- question: "Which statement about slope is correct?"
  type: multiple-choice
  options: ["A vertical line has a slope of 0", "A horizontal line has an undefined slope", "A line with a negative slope falls from left to right", "A steeper line always has a larger slope value"]
  answer: 2
  explanation: "A negative slope means y decreases as x increases, so the line falls from left to right — this is correct. A vertical line has undefined slope (division by zero in rise/run), not zero. A horizontal line has slope 0, not undefined. 'Steeper' means larger absolute value: a slope of -5 is steeper than a slope of 1, even though -5 < 1."

- question: "If you calculate slope as run/rise instead of rise/run, you get the reciprocal of the correct slope."
  type: true-false
  answer: true
  explanation: "Slope = rise/run. Flipping to run/rise gives the reciprocal. For example, between points with rise 4 and run 2, the correct slope is 4/2 = 2, but run/rise gives 2/4 = 1/2. This reciprocal corresponds to a different (less steep) line — confirming that the order of rise and run matters."

- question: "Student A computes slope between (2, 5) and (6, 13) as (13 − 5)/(6 − 2) = 2. Student B uses (5 − 13)/(2 − 6) = 2. Why do they get the same answer even though they subtracted in opposite orders?"
  type: short-answer
  answer: "Both students subtracted consistently — they both flipped the order of subtraction in both numerator and denominator simultaneously, which is equivalent to multiplying both by -1. The negatives cancel: (-8)/(-4) = 8/4 = 2. Slope is a property of the line, not of which point is labeled first."
  explanation: "The slope formula works with either point as (x₁, y₁) because swapping both subtractions multiplies both rise and run by -1, leaving the ratio unchanged. What causes errors is inconsistency — using (y₂ − y₁) on top but (x₁ − x₂) on the bottom, which flips only one sign and gives the wrong sign for the slope."
```

## Explainer

Slope is the mathematical language for steepness and direction. You have experienced slope physically — walking up a steep hill feels different from a gentle ramp, and a downhill slope feels different from an uphill one. Slope captures all of this in a single number: how much does the line go up (or down) for each step to the right?

The formula m = rise/run answers that question. Rise is the vertical change (y goes up: positive; y goes down: negative). Run is the horizontal change (almost always taken left to right, so positive). A slope of 3 means "for every 1 unit right, the line goes up 3 units." A slope of -2 means "for every 1 unit right, the line goes down 2 units." A slope of 0 means the line doesn't go up or down at all — it's perfectly horizontal. Notice that a vertical line has no defined slope because its run is zero, and you cannot divide by zero.

Slope is exactly the same concept as unit rate from your prior work with proportional relationships. If a car travels 60 miles per hour, the slope of its distance-vs-time graph is 60: for every 1 hour (run), distance increases by 60 miles (rise). This is why slope appears in every linear relationship — it is the rate at which one quantity changes per unit of another.

When computing slope from two points, the biggest pitfall is inconsistency in subtraction order. The formula is (y₂ − y₁)/(x₂ − x₁): whichever point you call "point 2," use it in the numerator and denominator. If you flip both subtractions, you get the same answer (negatives cancel). If you flip only one, you get the wrong sign. A reliable habit: compute rise first (top point minus bottom point's y), then run (right point minus left point's x), and check that positive slope means the line goes up-right and negative slope means it goes down-right before moving on.

Understanding slope deeply — not just as a formula but as a rate of change — is the foundation for everything that follows in algebra. Slope-intercept form (y = mx + b) uses slope directly. Parallel lines have equal slopes. Perpendicular lines have slopes that are negative reciprocals of each other. Every linear relationship you encounter, in mathematics or in the world, is characterized by its slope.
