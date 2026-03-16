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

## Explainer

Your trigonometric ratios — sine, cosine, and tangent — were originally defined for right triangles: sin(A) = opposite/hypotenuse, and so on. But most triangles in real problems have no right angle. The **Law of Sines** extends your trigonometric toolkit to any triangle by establishing a clean proportionality: each side is proportional to the sine of its opposite angle. In any triangle with sides a, b, c and opposite angles A, B, C, the ratio a/sin(A) = b/sin(B) = c/sin(C).

The derivation is a direct application of the right-triangle definitions you already know. Drop an altitude from vertex C to side c, creating height h. In the left sub-triangle, sin(A) = h/b, so h = b·sin(A). In the right sub-triangle, sin(B) = h/a, so h = a·sin(B). Setting these equal: b·sin(A) = a·sin(B), which rearranges to a/sin(A) = b/sin(B). Repeating with a different altitude gives b/sin(B) = c/sin(C). A beautiful bonus: each common ratio equals the diameter of the triangle's **circumscribed circle** — the circle passing through all three vertices. So 2R = a/sin(A), where R is the circumradius.

The law is cleanest for **AAS** (two angles and any side) and **ASA** (two angles and the included side). If you know two angles, the third is determined by the angle sum A + B + C = 180°. Then knowing any side sets the common ratio, and you can solve for the remaining sides by cross-multiplying. SAS and SSS configurations are better handled by the Law of Cosines, because those involve two sides without both opposite angles.

The tricky case is **SSA** (two sides and an angle opposite one of them) — the **ambiguous case**. Suppose you know sides a and b and angle A. You compute sin(B) = b·sin(A)/a. If sin(B) > 1, no triangle exists. If sin(B) = 1, exactly one right triangle exists. If sin(B) < 1, there are two possible values for B: one acute (B) and one obtuse (180°−B). Each gives a different triangle — unless the obtuse B would make A + B > 180°, which is impossible, eliminating that solution. The ambiguity is not a flaw in the formula; it reflects a genuine geometric fact: a short side opposite an acute angle can swing to two different positions while still reaching the opposite side. Sketching the triangle before computing is the best way to see which case you are in.
