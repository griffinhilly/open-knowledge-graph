---
id: law-of-sines
title: Law of Sines
domain: mathematics
course: precalculus
prerequisites:
  - id: trigonometric-ratios-review
    type: hard
builds-toward:
  - polar-coordinates
tags: [trigonometry, triangles, law-of-sines]
stage: formal-systems
status: validated
---

# Law of Sines

## Core Idea
The Law of Sines states that in any triangle, a/sin(A) = b/sin(B) = c/sin(C), where a, b, c are sides and A, B, C are opposite angles. It extends trigonometry beyond right triangles to oblique triangles and is used when you know two angles and a side (AAS or ASA) or two sides and an angle opposite one of them (SSA, the ambiguous case).

## How It's Best Learned
Derive from the area formula or by dropping an altitude. Practice AAS/ASA cases first (straightforward), then tackle the ambiguous case (SSA) where zero, one, or two triangles may exist. Use diagrams to illustrate why the ambiguous case occurs.

## Common Misconceptions
- Ignoring the ambiguous case in SSA configurations.
- Forgetting that the Law of Sines gives the sine of an angle, which could correspond to two different angles (supplementary).
- Applying the Law of Sines when the Law of Cosines is more appropriate (SSS or SAS).

## Questions

```yaml
- question: "You know sides a = 7, b = 10, and angle A = 30° in a triangle. You compute sin(B) = b·sin(A)/a ≈ 0.714. How many valid triangles exist?"
  type: multiple-choice
  options:
    - "Exactly one — the Law of Sines always gives a unique solution"
    - "Possibly two — sin(B) < 1, so B could be either acute or obtuse"
    - "None — side b is longer than side a, so the triangle cannot be constructed"
    - "Infinitely many — SSA configurations are always indeterminate"
  answer: 1
  explanation: "This is the ambiguous case (SSA). When sin(B) < 1 and angle A is acute, two values of B are possible: one acute (B ≈ 45.6°) and one obtuse (B ≈ 134.4°). Since both give A + B < 180°, both produce valid triangles. The key insight is that sin is not one-to-one on [0°, 180°]: sin(θ) = sin(180°−θ), so a computed sine value corresponds to two possible angles. Checking whether each yields a valid angle sum determines how many triangles exist."

- question: "You are solving triangle ABC where angle A = 50°, angle B = 70°, and side c = 15. What is the correct first step using the Law of Sines?"
  type: multiple-choice
  options:
    - "Use the Law of Cosines first: c² = a² + b² − 2ab·cos(C)"
    - "Find C = 60° from the angle sum, then set up a/sin(50°) = 15/sin(60°)"
    - "No law applies — you need at least two sides to solve any triangle"
    - "Apply the Law of Sines but first verify the triangle inequality"
  answer: 1
  explanation: "This is an ASA configuration (two angles and a non-included side — but once you find C, it becomes effectively AAS). First, find the third angle: C = 180° − 50° − 70° = 60°. Now all three angles and one side are known, so the Law of Sines gives a unique solution: a = 15·sin(50°)/sin(60°). This clean case produces no ambiguity because two angles fully determine the triangle's shape."

- question: "In the Law of Sines, the ratio a/sin(A) equals twice the radius of the triangle's circumscribed circle."
  type: true-false
  answer: true
  explanation: "A beautiful consequence of the derivation: the common ratio a/sin(A) = b/sin(B) = c/sin(C) = 2R, where R is the circumradius — the radius of the circle passing through all three vertices. This follows from the inscribed angle theorem. The Law of Sines is secretly a statement about the circumscribed circle, which is why the same formula appears in circle geometry."

- question: "The ambiguous case (SSA) in the Law of Sines is a flaw in the formula — it means the Law of Sines gives an incorrect or incomplete answer for certain inputs."
  type: true-false
  answer: false
  explanation: "The ambiguous case is not a formula flaw — it reflects a genuine geometric fact. When you specify two sides and an angle opposite one of them (SSA), there may be zero, one, or two geometrically valid triangles. A short side opposite an acute angle can swing to two different positions and still close the triangle. The Law of Sines correctly captures all possible solutions; the 'ambiguity' is in the problem setup, not the formula. Sketching the triangle before computing is the best way to see which sub-case applies."

- question: "In an SSA configuration, when does the ambiguous case produce exactly zero valid triangles? Explain geometrically."
  type: short-answer
  answer: "Zero triangles exist when sin(B) > 1, which is mathematically impossible. Geometrically, this occurs when the side opposite the given angle is too short to reach across and close the triangle — the arc swept by the swinging side falls short of the base line entirely. For example, if angle A = 30° and a is very short relative to b, the side a cannot bridge the gap to complete the triangle. Checking sin(B) = b·sin(A)/a > 1 is the algebraic test for this geometric impossibility."
  explanation: "Grounding the algebraic condition (sin(B) > 1) in the geometric picture (the swinging side falls short) turns a seemingly arbitrary rule into an insight. Students who only memorize the algebraic test often cannot explain why it means 'no triangle exists.'"
```

## Explainer

Your trigonometric ratios — sine, cosine, and tangent — were originally defined for right triangles: sin(A) = opposite/hypotenuse, and so on. But most triangles in real problems have no right angle. The **Law of Sines** extends your trigonometric toolkit to any triangle by establishing a clean proportionality: each side is proportional to the sine of its opposite angle. In any triangle with sides a, b, c and opposite angles A, B, C, the ratio a/sin(A) = b/sin(B) = c/sin(C).

The derivation is a direct application of the right-triangle definitions you already know. Drop an altitude from vertex C to side c, creating height h. In the left sub-triangle, sin(A) = h/b, so h = b·sin(A). In the right sub-triangle, sin(B) = h/a, so h = a·sin(B). Setting these equal: b·sin(A) = a·sin(B), which rearranges to a/sin(A) = b/sin(B). Repeating with a different altitude gives b/sin(B) = c/sin(C). A beautiful bonus: each common ratio equals the diameter of the triangle's **circumscribed circle** — the circle passing through all three vertices. So 2R = a/sin(A), where R is the circumradius.

The law is cleanest for **AAS** (two angles and any side) and **ASA** (two angles and the included side). If you know two angles, the third is determined by the angle sum A + B + C = 180°. Then knowing any side sets the common ratio, and you can solve for the remaining sides by cross-multiplying. SAS and SSS configurations are better handled by the Law of Cosines, because those involve two sides without both opposite angles.

The tricky case is **SSA** (two sides and an angle opposite one of them) — the **ambiguous case**. Suppose you know sides a and b and angle A. You compute sin(B) = b·sin(A)/a. If sin(B) > 1, no triangle exists. If sin(B) = 1, exactly one right triangle exists. If sin(B) < 1, there are two possible values for B: one acute (B) and one obtuse (180°−B). Each gives a different triangle — unless the obtuse B would make A + B > 180°, which is impossible, eliminating that solution. The ambiguity is not a flaw in the formula; it reflects a genuine geometric fact: a short side opposite an acute angle can swing to two different positions while still reaching the opposite side. Sketching the triangle before computing is the best way to see which case you are in.
