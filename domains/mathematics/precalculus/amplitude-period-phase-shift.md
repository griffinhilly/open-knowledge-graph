---
id: amplitude-period-phase-shift
title: Amplitude, Period, and Phase Shift
domain: mathematics
course: precalculus
prerequisites:
  - id: graphing-sine-and-cosine
    type: hard
  - id: function-transformations
    type: hard
builds-toward:
  - trigonometric-integrals
tags: [trigonometry, graphing, transformations, sinusoidal]
stage: formal-systems
status: validated
---

# Amplitude, Period, and Phase Shift

## Core Idea
The general sinusoidal function y = A sin(B(x - C)) + D has four parameters: amplitude |A| (vertical stretch, controls height), period 2*pi/|B| (horizontal stretch, controls how fast it repeats), phase shift C (horizontal translation), and vertical shift D. These four numbers completely determine the shape and position of any sinusoidal graph.

## How It's Best Learned
Start from the parent graph and apply one parameter at a time, predicting the effect before graphing. Work both directions: given an equation, sketch the graph; given a graph, write the equation. Real-world modeling (tides, temperature, Ferris wheels) makes the parameters concrete.

## Common Misconceptions
- Confusing period with frequency (period = 1/frequency in context, but 2*pi/B in the formula).
- Getting the phase shift direction wrong: y = sin(x - C) shifts right by C.
- Forgetting the absolute value on A for amplitude (amplitude is always positive).

## Explainer

You already know how to graph y = sin(x) and y = cos(x) on the parent scale: one full wave over the interval [0, 2π], reaching a maximum of 1 and a minimum of -1. You also know from function transformations that multiplying a function by a constant stretches it vertically, multiplying the input compresses it horizontally, adding to the input shifts it left or right, and adding to the output shifts it up or down. The general sinusoidal form y = A sin(B(x - C)) + D is precisely those four transformations applied to y = sin(x), one parameter at a time.

The **amplitude** |A| is the vertical stretch: it sets the maximum and minimum of the wave to +|A| and -|A|. A negative A flips the graph upside down (reflection over the x-axis) but doesn't change the height of the waves, which is why amplitude is always the absolute value. The **vertical shift** D moves the entire wave up or down, relocating the midline from y = 0 to y = D. These two parameters control the vertical range: the wave oscillates between D - |A| and D + |A|.

The **period** is the length of one complete cycle, and B compresses or stretches the wave horizontally. The parent function y = sin(x) completes one cycle over [0, 2π], so y = sin(Bx) completes one cycle when Bx goes from 0 to 2π — that is, when x goes from 0 to 2π/B. So the period is 2π/|B|. A larger B makes the wave repeat faster (shorter period); a smaller B makes it repeat slower (longer period). Think of B as the "speed" of the wave: B = 2 means the wave goes twice as fast, completing its cycle in half the distance.

The **phase shift** C is the trickiest parameter because the sign is counterintuitive. In y = sin(B(x - C)), the argument (x - C) equals zero when x = C, which is where the shifted function "begins" its cycle. Since the wave starts at x = C instead of x = 0, it has shifted C units to the right. Writing it as x + C (a minus negative C) shifts it left. The easy rule: the sign of the phase shift matches the direction of movement — but only if you factor the expression so it's written as B(x - C), not as Bx + something. Always extract B first, then read C as the rightward shift. With all four parameters identified, you can sketch any sinusoidal function by locating its midline, marking one period's worth of key points, and scaling the amplitude up and down from there.
