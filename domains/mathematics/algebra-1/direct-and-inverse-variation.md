---
id: direct-and-inverse-variation
title: Direct and Inverse Variation
domain: mathematics
course: algebra-1
prerequisites:
- id: proportional-relationships
  type: hard
- id: solving-multi-step-equations
  type: hard
- id: solving-proportions
  type: soft
builds-toward:
- graphing-rational-functions
tags:
- variation
- direct
- inverse
- proportionality
- modeling
stage: abstract-reasoning
status: validated
---
# Direct and Inverse Variation

## Core Idea
In direct variation, y = kx: as x increases, y increases proportionally. The constant k is the constant of variation (or proportionality). The graph is a line through the origin. In inverse variation, y = k/x: as x increases, y decreases, and vice versa. The product xy is constant. The graph is a hyperbola. These two variation types model many real-world relationships: direct variation appears in unit pricing and Hooke's law; inverse variation appears in the relationship between speed and time for a fixed distance, or pressure and volume (Boyle's law).

## How It's Best Learned
Use tables to identify which type of variation applies: if y/x is constant, it is direct; if xy is constant, it is inverse. Write the equation, find k from a given data point, and use it to find other values. Graph both types and compare their shapes. Use word problems from science and everyday life. Emphasize that direct variation is a special case of a linear function (with b = 0).

## Common Misconceptions
- Confusing direct and inverse variation (not checking whether the ratio or the product is constant).
- Thinking inverse variation means y = −kx (that is a line with negative slope, not inverse variation).
- Forgetting that direct variation passes through the origin — if it has a y-intercept, it is not direct variation.

## Questions

```yaml
- question: "A student claims: 'If y decreases when x increases, the relationship is inverse variation.' Which data table below disproves this claim?"
  type: multiple-choice
  options:
    - "x=1, y=12; x=2, y=6; x=4, y=3 — product xy = 12 in each row"
    - "x=1, y=−2; x=2, y=−4; x=3, y=−6 — ratio y/x = −2 in each row"
    - "x=2, y=10; x=4, y=5; x=5, y=4 — product xy = 20 in each row"
    - "x=1, y=8; x=2, y=4; x=4, y=2 — product xy = 8 in each row"
  answer: 1
  explanation: "Table B shows y decreasing as x increases, yet y/x is constant (= −2) — making this direct variation (y = −2x), not inverse variation. The student's claim confuses 'y decreases as x increases' with inverse variation, but a line with negative slope also has this property. Inverse variation requires the product xy to be constant, which is not the case in table B. Tables A, C, and D all have constant products and are genuine inverse variation."

- question: "A car travels a fixed distance of 300 km. As average speed increases, travel time decreases. What type of relationship describes speed and time?"
  type: multiple-choice
  options:
    - "Direct variation — time = k × speed, where k = 300"
    - "Inverse variation — speed × time = 300 (a constant product)"
    - "Neither — the relationship is exponential because time decreases rapidly at first"
    - "Direct variation, because distance acts as the constant of proportionality"
  answer: 1
  explanation: "Speed × time = distance = 300, a constant. This is the definition of inverse variation: xy = k. As speed doubles, time halves; the product is always 300. Option A has the equation backwards — if time = k × speed, time would increase as speed increases, which is wrong. Options C and D misidentify the structure of the relationship."

- question: "In direct variation, the graph always passes through the origin (0, 0)."
  type: true-false
  answer: true
  explanation: "The defining equation y = kx produces y = 0 when x = 0, regardless of k. This is built into the equation — the origin is always on the line. This distinguishes direct variation from other linear functions like y = kx + b (b ≠ 0), which are proportional relationships but not direct variations. If a linear graph does not pass through the origin, it cannot be a direct variation."

- question: "Inverse variation means y = −kx — the two quantities vary inversely because one is the negative of the other."
  type: true-false
  answer: false
  explanation: "Inverse variation means y = k/x (equivalently, xy = k), which produces a hyperbola — not a line. 'Inversely' here means the variables change in opposite directions with their product held constant. A line y = −kx with negative slope is actually direct variation with a negative constant of proportionality, because the ratio y/x = −k is constant. The graph of inverse variation never produces a straight line."

- question: "How do you determine from a table of values whether two quantities have direct variation, inverse variation, or neither?"
  type: short-answer
  answer: "Compute two quantities for each row: the ratio y/x and the product xy. If y/x is constant across all rows, the relationship is direct variation and k = y/x. If xy is constant across all rows, the relationship is inverse variation and k = xy. If neither is constant, the relationship is neither type. Only one should be constant for any given non-trivial relationship."
  explanation: "This diagnostic procedure is the practical core of the topic. It works because direct variation requires y = kx (so y/x = k), and inverse variation requires xy = k. Running both checks on a table quickly identifies the variation type and extracts the constant k, which then gives the full equation for predicting any additional values."
```

## Explainer

**Direct variation** means two quantities grow together in a fixed ratio: double one, and the other doubles; triple one, and the other triples. The defining equation is y = kx, where **k** is the **constant of variation**. You already know proportional relationships from your prerequisites — direct variation is exactly that, formalized as an equation. Its graph is always a straight line through the origin with slope k. The absence of a y-intercept is the defining visual feature: if the line doesn't pass through (0, 0), it's a linear function but not a direct variation.

**Inverse variation** means one quantity increases as the other decreases, with their product staying constant. The defining equation is y = k/x, equivalently xy = k. Double x and y is cut in half. Triple x and y becomes one-third. The graph is a **hyperbola** — two curved branches that approach but never touch the axes. There is no value at x = 0, which distinguishes it sharply from direct variation. The constant k tells you how "spread out" the hyperbola is.

To identify which type applies from a table of values, use two tests. Compute the ratio y/x for each row — if it's constant, you have direct variation and k = y/x. Compute the product xy for each row — if it's constant, you have inverse variation and k = xy. You only need one of these to be constant; the other will vary. Once you've identified the type and found k, the equation lets you find any missing value: if y varies directly with x and y = 12 when x = 4, then k = 12/4 = 3, so y = 3x, and when x = 7, y = 21.

These two models appear throughout science. Direct variation: Hooke's law (force = k × stretch), unit pricing (total cost = price × quantity), distance at constant speed (d = rt). Inverse variation: speed and time for a fixed distance (speed × time = distance constant), Boyle's law for gases at fixed temperature (pressure × volume = constant). Recognizing which type of relationship a situation follows — by checking the ratio or the product — is the first step in building a mathematical model of any real-world problem.
