---
id: graphing-rational-functions
title: Graphing Rational Functions
domain: mathematics
course: algebra-2
prerequisites:
  - id: rational-functions-and-asymptotes
    type: hard
builds-toward:
  - solving-rational-equations
tags: [rational-functions, graphing, asymptotes, intercepts]
stage: abstract-reasoning
status: validated
---

# Graphing Rational Functions

## Core Idea
To graph a rational function: (1) factor numerator and denominator, (2) find and plot x-intercepts (numerator zeros), y-intercept (f(0)), (3) identify vertical asymptotes and holes, (4) determine horizontal or oblique asymptotes, (5) use sign analysis or test points to determine behavior in each region, (6) sketch the curve approaching asymptotes. The graph is composed of smooth curves in separate regions defined by the vertical asymptotes.

## How It's Best Learned
Work through complete examples step by step. Emphasize sign analysis: in each interval between vertical asymptotes, determine whether the function is positive or negative. Use graphing technology to verify hand-drawn sketches. Practice identifying key features from the equation before graphing.

## Common Misconceptions
- Drawing the graph crossing a vertical asymptote (it never does, though it can cross a horizontal asymptote).
- Forgetting to check behavior on both sides of a vertical asymptote.
- Not plotting enough points between asymptotes to capture the curve's shape.
- Ignoring holes in the graph.

## Explainer

From your work with rational functions and asymptotes, you already know the key features: vertical asymptotes appear at zeros of the denominator that don't cancel, holes appear at factors that cancel, and horizontal or oblique asymptotes are determined by comparing degrees of numerator and denominator. Graphing takes all that structural information and assembles it into a complete picture of the function's behavior by working through a systematic sequence of steps.

Begin with the **skeleton**: factor both numerator and denominator completely and cancel any common factors. Each cancelled factor creates a **hole** — mark it with a small open circle at the corresponding x-value on the graph. Each remaining factor in the denominator gives a **vertical asymptote** — draw these as dashed vertical lines. These asymptotes divide the real line into separate intervals, and the graph lives in separate corridors between them. Then determine the **end-behavior asymptote**: if the numerator degree is less than the denominator degree, y → 0; if degrees match, y → (ratio of leading coefficients); if the numerator exceeds by one degree, polynomial division gives an oblique asymptote. Draw these as dashed horizontal or diagonal lines.

Next, add the **intercepts**. The x-intercepts are the zeros of the simplified numerator (the x-values where the numerator equals zero, after cancellation). The y-intercept is f(0) — plug in x = 0. Plot these points on the graph; they locate the curve within its corridors.

With the skeleton established, **sign analysis** determines which side of the x-axis the curve occupies in each corridor. Pick one test x-value in each interval (between consecutive vertical asymptotes, and also in the regions beyond the outermost asymptotes). Evaluate the sign of the function at each test point — not the exact value, just positive or negative. You can do this efficiently by tracking the sign contributed by each factor in the numerator and denominator. Once you know the sign in each corridor, you know whether the curve approaches each vertical asymptote from above (+∞) or below (−∞). Connect the intercepts and sign information with smooth curves, one continuous piece per corridor, each approaching its asymptotes without crossing them. Vertical asymptotes are never crossed; horizontal asymptotes may be crossed in the interior but are approached at the extremes.
