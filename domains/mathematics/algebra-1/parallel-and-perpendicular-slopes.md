---
id: parallel-and-perpendicular-slopes
title: Parallel and Perpendicular Line Slopes
domain: mathematics
course: algebra-1
prerequisites:
- id: slope-concept
  type: hard
- id: writing-linear-equations
  type: hard
builds-toward:
- coordinate-geometry-proofs
tags:
- parallel
- perpendicular
- slope
- linear-equations
stage: abstract-reasoning
status: validated
---
# Parallel and Perpendicular Line Slopes

## Core Idea
Parallel lines have the same slope but different y-intercepts — they never intersect. If one line has slope 2/3, any line parallel to it also has slope 2/3. Perpendicular lines have slopes that are negative reciprocals of each other — their product is −1. If one line has slope 2/3, a perpendicular line has slope −3/2. These relationships allow you to write the equation of a line parallel or perpendicular to a given line through a specified point. They connect algebra to geometry and are used in coordinate geometry proofs, constructions, and engineering design.

## How It's Best Learned
Start with graphing: plot two parallel lines and observe they have the same slope. Plot two perpendicular lines and compute their slopes to discover the negative reciprocal relationship. Practice writing equations of lines parallel or perpendicular to a given line through a given point. Verify graphically that the lines look parallel or perpendicular.

## Common Misconceptions
- Thinking perpendicular slopes are just reciprocals (forgetting the negative sign).
- Confusing the slope of a line with its y-intercept when determining parallel lines.
- Not knowing how to handle slopes of 0 (horizontal) and undefined (vertical) — these are perpendicular to each other.

## Explainer

You already understand that slope measures steepness — rise divided by run, how many units a line climbs for each unit it moves right. Parallel and perpendicular relationships are really just precise statements about what happens to slope when you change a line's angle in specific geometric ways.

**Parallel lines** never meet, which means they rise at exactly the same rate. If one line climbs 2 units for every 3 units right (slope 2/3), a line parallel to it must also climb 2 units for every 3 units right — no more, no less. The only freedom parallel lines have is their vertical position, captured by different y-intercepts. Two lines are parallel if and only if they have the same slope and different y-intercepts. (Two lines with the same slope and the same y-intercept are the same line, not parallel ones.)

**Perpendicular lines** meet at a right angle, which produces a different relationship. Imagine taking a line with slope 2/3 and rotating it 90 degrees. Two things happen: the rise and run swap roles (the new run is what was the old rise), and the direction flips (what went up now goes down, or vice versa). Swapping rise and run turns 2/3 into 3/2 (the reciprocal); flipping the direction introduces the negative sign. The result is −3/2. This is the **negative reciprocal**: flip the fraction upside down and change its sign. You can verify the relationship algebraically: if two lines have slopes m₁ and m₂, they are perpendicular when m₁ · m₂ = −1.

The special cases — horizontal and vertical lines — fit the same pattern. A horizontal line has slope 0; a vertical line has undefined slope. They are clearly perpendicular. The product rule (m₁ · m₂ = −1) breaks down here because you cannot multiply by undefined, but the geometric relationship is unambiguous. These rules let you solve a common class of problems: given a line and a point not on it, write the equation of a new line through that point that is either parallel (copy the slope, use point-slope form) or perpendicular (negate and invert the slope, use point-slope form).
