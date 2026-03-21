---
id: converting-degrees-and-radians
title: Converting Between Degrees and Radians
domain: mathematics
course: precalculus
prerequisites:
  - id: radian-measure
    type: hard
builds-toward:
  - unit-circle
  - graphing-sine-and-cosine
tags: [trigonometry, radians, degrees, conversion]
stage: formal-systems
status: validated
---

# Converting Between Degrees and Radians

## Core Idea
Since 360 degrees = 2*pi radians, converting between the two systems uses the factor pi/180 (degrees to radians) or 180/pi (radians to degrees). Fluency in conversion is necessary because many real-world problems use degrees while all calculus uses radians. You should eventually recognize common conversions (30 = pi/6, 45 = pi/4, etc.) without computing.

## How It's Best Learned
Derive the conversion factor from the fundamental relationship. Practice converting standard angles in both directions. Build a reference table of common angles and their radian equivalents. Eventually move to instant recognition rather than calculation.

## Common Misconceptions
- Multiplying by the wrong conversion factor (using 180/pi when pi/180 is needed, or vice versa).
- Leaving answers in decimal approximations instead of exact multiples of pi.
- Believing that pi in radian measure is approximately 3.14 degrees.

## Questions

```yaml
- question: "A student converts 90° to radians and writes the answer as 1.5708. What is the problem with this answer?"
  type: multiple-choice
  options:
    - "The conversion is wrong — 90° does not equal π/2 radians"
    - "The student used the wrong conversion factor (180/π instead of π/180)"
    - "Radian answers should be expressed as exact multiples of π (π/2), not as decimal approximations"
    - "Radians cannot be compared to degrees without specifying the radius of the circle"
  answer: 2
  explanation: "1.5708 ≈ π/2, so the numerical value is correct — but the form is wrong. Radian answers should almost always be left as exact multiples of π. Writing 1.5708 instead of π/2 introduces rounding error, makes further calculations messier, and obscures the structure of the angle. Exact form is preferable for the same reason you write 1/3 rather than 0.333... — it's cleaner, more precise, and reveals the underlying relationship."

- question: "If you forget the conversion formula, how can you re-derive the factor for converting degrees to radians?"
  type: multiple-choice
  options:
    - "Recall that 1 radian ≈ 57.3° and use that approximation"
    - "From the fundamental equivalence 360° = 2π radians, divide both sides by 360 to get 1° = π/180 radians"
    - "Use the unit circle: set the radius to 1 and measure arc length in degrees"
    - "The formula must be memorized — there is no way to derive it from first principles"
  answer: 1
  explanation: "The single foundational fact is 360° = 2π radians — a full revolution in both measurement systems. Dividing both sides by 360 gives 1° = π/180 rad, so to convert degrees to radians, multiply by π/180. To go the other direction, divide both sides by 2π to get 1 rad = 180/π degrees. This derivation takes ten seconds and means you never need to memorize the formula outright."

- question: "The derivative of sin(x) equals cos(x) only when x is measured in radians, not when x is in degrees."
  type: true-false
  answer: true
  explanation: "This is one of the most important practical consequences of radian measure. The calculus identity d/dx[sin(x)] = cos(x) relies on the limit (sin h)/h → 1 as h → 0, which holds only when h is in radians. If x is in degrees, the formula gains a factor of π/180. This is why every trigonometric formula in calculus and beyond assumes radian input — and why fluency in radian conversion is prerequisite knowledge for calculus."

- question: "Since π ≈ 3.14, an angle of π radians is approximately equal to 3.14 degrees."
  type: true-false
  answer: false
  explanation: "This is a category error. The number π ≈ 3.14 is just that — a number. In radian measure, π radians means 'π times 1 radian,' which equals 180 degrees (half a full turn). The decimal 3.14 tells you the numerical value of π, not its degree equivalent. Saying 'π radians ≈ 3.14 degrees' confuses the number π with the angle measurement. This misconception often trips students who conflate the symbol π with the angle, rather than recognizing π as a coefficient in the expression."

- question: "Explain why radian answers should be left as exact multiples of π rather than converted to decimal approximations."
  type: short-answer
  answer: "Exact multiples of π preserve the precise relationship between the angle and the underlying geometry. π/4 immediately tells you this is one-eighth of a full turn; 0.785 does not. Exact form avoids accumulated rounding error in subsequent calculations, keeps algebraic manipulation clean (π/4 × 2 = π/2, whereas 0.785 × 2 = 1.570 is already imprecise), and is required for the calculus formulas that use radian measure."
  explanation: "The deeper point is that 'leaving π in the answer' is not laziness — it is precision. The decimal expansion of π is infinite and non-repeating, so any decimal approximation loses information. In the same way that you write √2 instead of 1.414, you write π/3 instead of 1.047. This habit becomes especially important in calculus, where exact radian expressions simplify differentiation and integration of trigonometric functions."
```

## Explainer

The key to converting between degrees and radians is a single foundational equivalence: one full revolution equals both 360 degrees and 2π radians. This is not a definition to memorize blindly — it follows from what **radian measure** means. One radian is the angle that subtends an arc equal in length to the radius. Going all the way around a circle covers an arc of length 2πr (the circumference), so a full revolution sweeps 2π radians. That's it: 360° = 2π rad.

From this single fact, all conversions follow. To go from degrees to radians, multiply by (2π / 360) = π/180. To go from radians to degrees, multiply by (360 / 2π) = 180/π. You can always rederive these factors if you forget them — just start from 360° = 2π and cross-multiply. For example, to convert 90°: multiply by π/180 to get 90π/180 = π/2 radians. To convert 3π/4 radians: multiply by 180/π to get 3 × 180/4 = 135°.

The common angles are worth internalizing as direct associations rather than computed results. 30° = π/6, 45° = π/4, 60° = π/3, 90° = π/2, 180° = π, 270° = 3π/2, 360° = 2π. Once you see these often enough, you should recognize them the way you recognize that 1/4 = 0.25 — not by dividing each time, but instantly. The pattern helps: the denominator tells you what fraction of 180° (= π) you have, so π/6 is one-sixth of a half-turn (= 30°).

Notice that radian answers should generally be left as **exact multiples of π**, not decimal approximations. Writing π/4 is exact and clean; writing 0.785 is an approximation that loses information and makes further calculations messier. The decimal form of pi (3.14159...) is a number, not an angle unit — saying "π radians ≈ 3.14 degrees" is a category error. Fluency in this conversion is essential because calculus uses radians exclusively: the derivative of sin(x) is cos(x) only when x is in radians. Every trigonometric formula from here on assumes radian input.
