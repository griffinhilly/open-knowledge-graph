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

## Explainer

You already know what slope means and how to read and graph equations in slope-intercept or point-slope form. Now you are doing the inverse: *given* information about a line — a slope and a point, two points, a graph, a table, or a verbal description — *construct* the equation. This is the skill of mathematical modeling in miniature: translating a real-world situation into a formula that can make predictions.

The key insight is that a line is completely determined by two pieces of information. When the given information directly includes the slope and the y-intercept, use **slope-intercept form** y = mx + b by reading off m and b immediately. When you have the slope and any other specific point (not necessarily the y-intercept), use **point-slope form** y − y₁ = m(x − x₁), plugging in the known values directly — no need to hunt for b first. Given two points (x₁, y₁) and (x₂, y₂), compute slope first using m = (y₂ − y₁)/(x₂ − x₁), then feed that slope and either point into point-slope form. In all cases, the goal is the same equation; only the path to get there differs.

Word problems require one more translation step. Look for the **rate of change** (slope) hidden in phrases like "per hour," "each day," or "for every additional unit." Look for the **initial value** (y-intercept) in phrases like "starts at," "begins with," or the value when the independent variable equals zero. For example: "A plumber charges $75 per hour plus a $50 service fee." Here m = 75 (dollars per hour) and b = 50 (the flat fee at zero hours), giving cost = 75h + 50. The equation lets you predict cost for any number of hours without recomputing from scratch every time.

A common error is reaching for slope-intercept form even when the y-intercept is not given, which forces an unnecessary extra step. If you are given slope and a non-y-intercept point, write point-slope form first: y − y₁ = m(x − x₁). Simplify to slope-intercept form afterward if needed. Another pitfall: computing slope as Δx/Δy (run over rise) instead of Δy/Δx (rise over run). Label your points explicitly — (x₁, y₁) and (x₂, y₂) — and write the slope formula before substituting to avoid this swap.
