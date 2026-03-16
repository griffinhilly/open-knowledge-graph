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

## Explainer

**Direct variation** means two quantities grow together in a fixed ratio: double one, and the other doubles; triple one, and the other triples. The defining equation is y = kx, where **k** is the **constant of variation**. You already know proportional relationships from your prerequisites — direct variation is exactly that, formalized as an equation. Its graph is always a straight line through the origin with slope k. The absence of a y-intercept is the defining visual feature: if the line doesn't pass through (0, 0), it's a linear function but not a direct variation.

**Inverse variation** means one quantity increases as the other decreases, with their product staying constant. The defining equation is y = k/x, equivalently xy = k. Double x and y is cut in half. Triple x and y becomes one-third. The graph is a **hyperbola** — two curved branches that approach but never touch the axes. There is no value at x = 0, which distinguishes it sharply from direct variation. The constant k tells you how "spread out" the hyperbola is.

To identify which type applies from a table of values, use two tests. Compute the ratio y/x for each row — if it's constant, you have direct variation and k = y/x. Compute the product xy for each row — if it's constant, you have inverse variation and k = xy. You only need one of these to be constant; the other will vary. Once you've identified the type and found k, the equation lets you find any missing value: if y varies directly with x and y = 12 when x = 4, then k = 12/4 = 3, so y = 3x, and when x = 7, y = 21.

These two models appear throughout science. Direct variation: Hooke's law (force = k × stretch), unit pricing (total cost = price × quantity), distance at constant speed (d = rt). Inverse variation: speed and time for a fixed distance (speed × time = distance constant), Boyle's law for gases at fixed temperature (pressure × volume = constant). Recognizing which type of relationship a situation follows — by checking the ratio or the product — is the first step in building a mathematical model of any real-world problem.
