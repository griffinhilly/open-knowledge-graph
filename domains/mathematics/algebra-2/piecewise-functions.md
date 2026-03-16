---
id: piecewise-functions
title: Piecewise Functions
domain: mathematics
course: algebra-2
prerequisites:
- id: function-notation-review
  type: hard
- id: graphing-linear-equations
  type: hard
- id: solving-inequalities
  type: hard
- id: absolute-value-equations
  type: soft
- id: absolute-value-inequalities
  type: soft
builds-toward:
- continuity-definition
- step-functions
tags:
- functions
- piecewise
- graphing
- domain
stage: abstract-reasoning
status: validated
---
# Piecewise Functions

## Core Idea
A piecewise function uses different formulas on different intervals of its domain. Each piece is defined by a rule and a domain restriction. Common examples: absolute value function (|x| = x if x >= 0, -x if x < 0), step functions, and tax brackets. Graphing requires plotting each piece on its specified interval and paying attention to open vs. closed circles at boundary points.

## How It's Best Learned
Start with the absolute value function as a familiar piecewise function. Practice evaluating piecewise functions at specific values (determine which piece applies). Graph by plotting each piece on its interval. Discuss continuity: is the function connected at the boundary points? Create piecewise functions from real-world scenarios (postage rates, tax brackets).

## Common Misconceptions
- Applying the wrong piece for a given x-value (not checking which interval x falls in).
- Drawing pieces beyond their defined intervals.
- Confusing open and closed circles at boundary points (closed means the point is included, open means it is not).
- Thinking all piecewise functions are discontinuous (many are continuous, like |x|).

## Explainer

A **piecewise function** is a single function that uses different rules depending on where the input falls. You've seen this structure before without naming it: the absolute value function |x| is just a piecewise function with the rule "use x if x ≥ 0, use −x if x < 0." This makes intuitive sense — |x| has to do something different for positive and negative inputs. Piecewise functions generalize this idea: you can stitch together any number of formulas, each responsible for a different piece of the domain.

Evaluating a piecewise function requires two steps. First, determine which interval your input x belongs to. Second, apply the formula for that interval. For example, if f(x) = {x² for x < 0; 2x + 1 for x ≥ 0}, then f(−3) uses the first piece: (−3)² = 9. But f(2) uses the second piece: 2(2) + 1 = 5. The domain restrictions are the guardrails — you must check which "case" applies before computing. This is directly connected to solving inequalities: the condition "x < 0" is an inequality, and you're using your inequality-solving skills to decide which branch applies.

Graphing a piecewise function means drawing each piece only on its specified interval, like coloring within strict boundary lines. At the boundary point between two pieces, you must decide which piece "owns" that point. An **open circle** at an endpoint means the piece stops just before that value (the point is excluded); a **closed circle** means the piece includes that endpoint. If two pieces meet at the same y-value at their shared boundary, the function is continuous there — the graph has no jump. If they meet at different y-values, there is a jump discontinuity. The absolute value function is piecewise but continuous because both pieces give y = 0 at x = 0.

Real-world contexts are full of piecewise functions. Tax brackets are a classic example: you pay one rate on income up to a threshold, a higher rate on income above it. Postage pricing works similarly — a letter under 1 oz costs one amount, 1–2 oz costs more. These scenarios naturally produce piecewise rules because the underlying relationship genuinely changes at boundary values. Recognizing this pattern — "different rules for different ranges" — is the core skill that piecewise functions develop, and it's foundational for understanding continuity more rigorously in calculus.
