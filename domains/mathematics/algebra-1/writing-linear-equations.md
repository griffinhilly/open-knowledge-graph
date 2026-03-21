---
id: writing-linear-equations
title: Writing Linear Equations
domain: mathematics
course: algebra-1
prerequisites:
  - id: slope-concept
    type: hard
  - id: slope-intercept-form
    type: hard
  - id: point-slope-form
    type: hard
builds-toward:
  - systems-word-problems
  - parallel-and-perpendicular-slopes
  - linear-regression
tags: [writing-equations, linear, slope, modeling]
stage: abstract-reasoning
status: validated
---

# Writing Linear Equations

## Core Idea
Writing a linear equation means constructing the equation of a line from given information: a slope and a point, two points, a graph, a table, or a verbal description. The process varies slightly depending on the input: given slope and y-intercept, use y = mx + b directly; given slope and any point, use point-slope form; given two points, compute slope first. This skill is the inverse of graphing — instead of going from equation to picture, you go from picture (or data) to equation. It is essential for modeling real-world linear relationships.

## How It's Best Learned
Practice with all input types: given m and b, given m and a point, given two points, given a graph, given a word problem. For each, decide which form to write in and convert if needed. Emphasize word problems where students must identify the slope (rate of change) and a known point or initial value from context. Compare the resulting equations to verify they describe the same line.

## Common Misconceptions
- Using the wrong form for the given information (trying to use slope-intercept when the y-intercept is not given).
- Computing the slope from two points incorrectly (subtracting in the wrong order or swapping rise and run).
- Not recognizing the initial value in a word problem as the y-intercept.

## Questions

```yaml
- question: "A line has slope 3 and passes through the point (4, 7). The y-intercept is unknown. What is the most efficient first step to write the equation?"
  type: multiple-choice
  options:
    - "Write y = 3x + b and solve for b by substituting x = 4 and y = 7"
    - "Write y − 7 = 3(x − 4) using point-slope form directly"
    - "Plot the point and count slope triangles back to the y-axis"
    - "Use the two-point formula after creating a second point by moving one unit right"
  answer: 1
  explanation: "When you have a slope and a non-y-intercept point, point-slope form y − y₁ = m(x − x₁) is the direct, efficient choice — plug in the known values and you have the equation immediately. Option A also works, but it requires an extra step: substituting to find b, then rewriting. Option B is slower (you have to invent a second point). The common mistake is defaulting to slope-intercept form (y = mx + b) and treating the y-intercept as unknown — that approach works but is less direct when the y-intercept isn't given information."

- question: "A taxi charges $2.50 per mile plus a $3.00 base fare. A student writes the equation cost = 2.50m + 3.00. What does the 3.00 represent in the context of linear equations?"
  type: multiple-choice
  options:
    - "The slope, because it is the starting value of the fare"
    - "The y-intercept, because it is the cost when miles driven equals zero"
    - "A constant that adjusts the units from miles to dollars"
    - "The x-intercept, because it is paid before any miles are driven"
  answer: 1
  explanation: "In the equation y = mx + b, b is the y-intercept — the value of y when x = 0. Here, when miles = 0, cost = $3.00 (the base fare). So 3.00 is the y-intercept, representing the initial value before any distance is driven. The slope 2.50 is the rate of change (cost per mile). A common word-problem error is identifying the initial flat fee as the 'slope' because it is 'the starting point' — but slope is always a rate of change (how much y changes per unit of x), not an initial value."

- question: "Given only two points on a line, it is impossible to write the equation without first calculating the slope."
  type: true-false
  answer: true
  explanation: "This is true. A line is determined by two pieces of information, but 'two points' does not directly give you slope or intercept — you must extract slope first using m = (y₂ − y₁)/(x₂ − x₁). Only after computing slope can you use either point in point-slope form to write the full equation. There is no shortcut that skips the slope calculation when given two arbitrary points. This is why the process is: compute slope → then write the equation using slope and one point."

- question: "To write the equation of a line, you must always determine the y-intercept first."
  type: true-false
  answer: false
  explanation: "Point-slope form y − y₁ = m(x − x₁) lets you write a valid linear equation using any known point on the line — the y-intercept is not required. If you have slope 4 and the point (3, 11), you can immediately write y − 11 = 4(x − 3) without ever computing the y-intercept. You can then simplify to slope-intercept form afterward if needed, but the y-intercept is an intermediate result, not a prerequisite. Forcing yourself to find b first when it isn't given is a common inefficiency that often leads to extra arithmetic errors."

- question: "A problem gives you only the slope and one point that is NOT on the y-axis. Explain which equation form you should start with and why."
  type: short-answer
  answer: "Use point-slope form: y − y₁ = m(x − x₁). Plug in the known slope for m and the known point coordinates for x₁ and y₁. This form is designed exactly for this situation — you have a slope and a point, so you can write the equation directly without any additional steps."
  explanation: "Slope-intercept form (y = mx + b) requires knowing b, the y-intercept. If the given point is not the y-intercept, you don't know b yet. You could solve for it by substituting into y = mx + b, but that's an extra step. Point-slope form skips that step entirely: it accepts any point, not just the y-intercept, as input. This is why mathematicians invented it — it matches the most common situation in which a line is specified (slope + a point you happen to know)."
```

## Explainer

You already know what slope means and how to read and graph equations in slope-intercept or point-slope form. Now you are doing the inverse: *given* information about a line — a slope and a point, two points, a graph, a table, or a verbal description — *construct* the equation. This is the skill of mathematical modeling in miniature: translating a real-world situation into a formula that can make predictions.

The key insight is that a line is completely determined by two pieces of information. When the given information directly includes the slope and the y-intercept, use **slope-intercept form** y = mx + b by reading off m and b immediately. When you have the slope and any other specific point (not necessarily the y-intercept), use **point-slope form** y − y₁ = m(x − x₁), plugging in the known values directly — no need to hunt for b first. Given two points (x₁, y₁) and (x₂, y₂), compute slope first using m = (y₂ − y₁)/(x₂ − x₁), then feed that slope and either point into point-slope form. In all cases, the goal is the same equation; only the path to get there differs.

Word problems require one more translation step. Look for the **rate of change** (slope) hidden in phrases like "per hour," "each day," or "for every additional unit." Look for the **initial value** (y-intercept) in phrases like "starts at," "begins with," or the value when the independent variable equals zero. For example: "A plumber charges $75 per hour plus a $50 service fee." Here m = 75 (dollars per hour) and b = 50 (the flat fee at zero hours), giving cost = 75h + 50. The equation lets you predict cost for any number of hours without recomputing from scratch every time.

A common error is reaching for slope-intercept form even when the y-intercept is not given, which forces an unnecessary extra step. If you are given slope and a non-y-intercept point, write point-slope form first: y − y₁ = m(x − x₁). Simplify to slope-intercept form afterward if needed. Another pitfall: computing slope as Δx/Δy (run over rise) instead of Δy/Δx (rise over run). Label your points explicitly — (x₁, y₁) and (x₂, y₂) — and write the slope formula before substituting to avoid this swap.
