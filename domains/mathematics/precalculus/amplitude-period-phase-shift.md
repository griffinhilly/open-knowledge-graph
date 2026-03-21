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

## Questions

```yaml
- question: "The function y = 3 sin(2x − π) is rewritten in standard form. What is the phase shift?"
  type: multiple-choice
  options:
    - "π units to the left — the minus sign indicates a leftward shift"
    - "π units to the right — the constant being subtracted from the argument is π"
    - "π/2 units to the right — factor out B = 2 to get y = 3 sin(2(x − π/2))"
    - "π/2 units to the left — dividing by B reverses the direction of the shift"
  answer: 2
  explanation: "To find the phase shift, the expression inside sin must be written as B(x − C). Factor out B = 2: 2x − π = 2(x − π/2). Now C = π/2, giving a rightward shift of π/2. Option B is the most common error: reading the raw constant π as the phase shift without factoring out B first. Always extract B before reading C. The phase shift is C in the factored form B(x − C), not the raw constant in the unfactored expression."

- question: "For the function y = −4 cos(x) + 3, what is the amplitude?"
  type: multiple-choice
  options:
    - "−4, because A is the coefficient of cosine and it equals −4"
    - "4, because amplitude is |A| and is always a positive quantity"
    - "3, because the midline is at y = 3 and amplitude is measured from the midline to zero"
    - "7, because the function reaches a maximum value of 3 + 4 = 7"
  answer: 1
  explanation: "Amplitude is defined as |A|, the absolute value of the vertical stretch coefficient. A = −4 means the graph is reflected over the midline (flipped upside down) but the waves still reach 4 units above and below the midline. The negative sign changes orientation, not height. Option C confuses the midline value (3) with the amplitude. Option D gives the maximum y-value, not the amplitude — the maximum is D + |A| = 3 + 4 = 7, but amplitude is just |A| = 4."

- question: "In the function y = sin(Bx), increasing the value of B stretches the graph horizontally, producing a longer period."
  type: true-false
  answer: false
  explanation: "Increasing B compresses the graph horizontally, producing a shorter period. The period is 2π/|B| — a larger B makes the denominator larger, so the period shrinks. Think of B as the wave's speed: B = 2 means the wave completes its cycle in half the usual horizontal distance (period = π instead of 2π). The common confusion is that multiplying the input 'feels like' stretching, but multiplying the input compresses the horizontal scale, just as multiplying the output stretches the vertical scale."

- question: "For y = A sin(B(x − C)) + D, the graph oscillates between the values D − |A| and D + |A|."
  type: true-false
  answer: true
  explanation: "The vertical shift D moves the midline from y = 0 to y = D. The amplitude |A| is the maximum distance from the midline in either direction. So the wave reaches a maximum of D + |A| and a minimum of D − |A|. This formula holds regardless of the sign of A — a negative A flips the wave but doesn't change where the extremes are. For example, y = −3 sin(x) + 5 oscillates between 5 − 3 = 2 and 5 + 3 = 8."

- question: "In y = sin(x − C), why does a positive value of C shift the graph to the right, even though subtracting seems like it should move the graph left?"
  type: short-answer
  answer: "The phase shift moves the graph so that the pattern which began at x = 0 now begins at x = C. In y = sin(x), the wave starts its cycle where the argument equals zero — at x = 0. In y = sin(x − C), the argument equals zero when x = C, so the starting point has moved to x = C: a rightward shift. To get the same output that occurred at x = 0, you now need x = C — you must go further right to reach the same input value."
  explanation: "The confusion arises from thinking of the transformation as acting on the output (like a vertical shift), when it actually acts on the input. With input transformations, the effect is always reversed from intuition: subtracting C from the input means you need a larger x to reach the same argument value, so the graph shifts right. This is opposite to output transformations, where adding D shifts the graph up. The rule: input changes shift horizontally opposite to their sign; output changes shift vertically matching their sign."
```

## Explainer

You already know how to graph y = sin(x) and y = cos(x) on the parent scale: one full wave over the interval [0, 2π], reaching a maximum of 1 and a minimum of -1. You also know from function transformations that multiplying a function by a constant stretches it vertically, multiplying the input compresses it horizontally, adding to the input shifts it left or right, and adding to the output shifts it up or down. The general sinusoidal form y = A sin(B(x - C)) + D is precisely those four transformations applied to y = sin(x), one parameter at a time.

The **amplitude** |A| is the vertical stretch: it sets the maximum and minimum of the wave to +|A| and -|A|. A negative A flips the graph upside down (reflection over the x-axis) but doesn't change the height of the waves, which is why amplitude is always the absolute value. The **vertical shift** D moves the entire wave up or down, relocating the midline from y = 0 to y = D. These two parameters control the vertical range: the wave oscillates between D - |A| and D + |A|.

The **period** is the length of one complete cycle, and B compresses or stretches the wave horizontally. The parent function y = sin(x) completes one cycle over [0, 2π], so y = sin(Bx) completes one cycle when Bx goes from 0 to 2π — that is, when x goes from 0 to 2π/B. So the period is 2π/|B|. A larger B makes the wave repeat faster (shorter period); a smaller B makes it repeat slower (longer period). Think of B as the "speed" of the wave: B = 2 means the wave goes twice as fast, completing its cycle in half the distance.

The **phase shift** C is the trickiest parameter because the sign is counterintuitive. In y = sin(B(x - C)), the argument (x - C) equals zero when x = C, which is where the shifted function "begins" its cycle. Since the wave starts at x = C instead of x = 0, it has shifted C units to the right. Writing it as x + C (a minus negative C) shifts it left. The easy rule: the sign of the phase shift matches the direction of movement — but only if you factor the expression so it's written as B(x - C), not as Bx + something. Always extract B first, then read C as the rightward shift. With all four parameters identified, you can sketch any sinusoidal function by locating its midline, marking one period's worth of key points, and scaling the amplitude up and down from there.
