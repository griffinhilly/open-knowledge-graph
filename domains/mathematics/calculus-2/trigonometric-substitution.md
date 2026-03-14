---
id: trigonometric-substitution
title: Trigonometric Substitution
domain: mathematics
course: calculus-2
prerequisites:
- id: trigonometric-integrals
  type: hard
- id: inverse-trigonometric-functions
  type: hard
- id: derivatives-of-inverse-trig-functions
  type: soft
- id: graphing-tangent-and-reciprocal-trig
  type: soft
builds-toward:
- arc-length
tags:
- integration
- techniques
- trig-substitution
stage: formal-systems
status: validated
---
# Trigonometric Substitution

## Core Idea
Trigonometric substitution handles integrands containing sqrt(a^2 - x^2), sqrt(a^2 + x^2), or sqrt(x^2 - a^2) by substituting x = a*sin(theta), x = a*tan(theta), or x = a*sec(theta) respectively. The substitution eliminates the square root using a Pythagorean identity. After integrating in theta, you convert back to x using a reference triangle.

## How It's Best Learned
Memorize the three cases and which substitution matches each radical form. Practice drawing the reference triangle to convert back. Work through complete examples for each case. Connect to completing the square when the expression under the radical is not in standard form.

## Common Misconceptions
- Using the wrong substitution for the given radical form.
- Forgetting to convert back from theta to x at the end.
- Not completing the square first when the quadratic under the radical is not in standard form (e.g., sqrt(2x - x^2)).
