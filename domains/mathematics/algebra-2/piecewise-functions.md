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
stage: formal-systems
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

## Questions

```yaml
- question: "Let f(x) = {3x + 1 if x < 2;  x² − 1 if x ≥ 2}. What is f(2)?"
  type: multiple-choice
  options:
    - "7 — substituting x = 2 into 3x + 1 gives 3(2) + 1 = 7"
    - "3 — substituting x = 2 into x² − 1 gives 2² − 1 = 3"
    - "Both 7 and 3 — the function has two values at boundary points"
    - "Undefined — x = 2 sits exactly on the boundary between pieces"
  answer: 1
  explanation: "The domain restriction x ≥ 2 means the second piece owns the boundary point x = 2. The first piece, x < 2, does not include x = 2 (strict inequality). So f(2) = 2² − 1 = 3. Option A is the classic error — applying the first formula without checking the inequality. Always determine which interval contains your input value before evaluating."

- question: "A piecewise function is defined as f(x) = {x + 1 if x ≤ 1;  2x if x > 1}. A student argues the function is discontinuous at x = 1 because two different formulas are defined there. Which response is most accurate?"
  type: multiple-choice
  options:
    - "Correct — any piecewise function is discontinuous at its boundary points"
    - "Incorrect — both pieces give the same output at x = 1 (both equal 2), so the function is continuous there"
    - "Incorrect — only the first piece applies at x = 1, so continuity is determined solely by that formula"
    - "Correct — a closed circle and an open circle at the same x-value always indicate a discontinuity"
  answer: 1
  explanation: "Continuity at a boundary depends on whether the pieces agree in value there — not on whether multiple formulas exist. First piece at x = 1: f(1) = 1 + 1 = 2 (closed circle, x ≤ 1). Second piece limit from the right: lim_{x→1+} 2x = 2 (open circle). Both equal 2, so the graph has no jump and the function is continuous at x = 1. The student's reasoning is the most common misconception: the mere existence of two formulas does not cause discontinuity. You must check whether they agree at the boundary."

- question: "Nearly every piecewise-defined function has a jump discontinuity at each boundary point between its pieces."
  type: true-false
  answer: false
  explanation: "Many piecewise functions are perfectly continuous. The absolute value function |x| = {x if x ≥ 0; −x if x < 0} is continuous at x = 0 because both pieces give y = 0 there. Continuity at a boundary requires that the left-hand limit, right-hand limit, and function value all agree. The piecewise structure introduces the possibility of discontinuity, but whether one actually occurs depends on the specific formulas."

- question: "On the graph of a piecewise function, a closed circle at a boundary point means that piece includes that endpoint value."
  type: true-false
  answer: true
  explanation: "Graphical convention: a closed (filled) circle means the endpoint is included in the piece — the function actually equals that y-value at that x. An open (hollow) circle means the piece approaches but does not include that endpoint. When one piece ends with an open circle and another begins with a closed circle at the same x, exactly one piece owns the point, and the function is well-defined there (not necessarily continuous, but unambiguous)."

- question: "Explain how to evaluate a piecewise function at a specific input value, and describe what must be true at a boundary point for the function to be continuous there."
  type: short-answer
  answer: "To evaluate a piecewise function at x = a: first determine which interval a belongs to by checking the domain conditions (the inequalities), then apply the formula for that interval. At a boundary point, the function is continuous if the output values from the piece to the left and the piece to the right both equal the same number — the graph has no jump. If they differ, there is a jump discontinuity."
  explanation: "The two-step process — check the condition, then apply the formula — is the whole algorithm. The continuity condition formalizes the intuition of a 'connected' graph: the left limit equals the right limit equals the function value. Piecewise functions can fail continuity in various ways: a jump (different left and right limits), a removable hole (limits agree but function value differs), or the function being undefined at the boundary."
```

## Explainer

A **piecewise function** is a single function that uses different rules depending on where the input falls. You've seen this structure before without naming it: the absolute value function |x| is just a piecewise function with the rule "use x if x ≥ 0, use −x if x < 0." This makes intuitive sense — |x| has to do something different for positive and negative inputs. Piecewise functions generalize this idea: you can stitch together any number of formulas, each responsible for a different piece of the domain.

Evaluating a piecewise function requires two steps. First, determine which interval your input x belongs to. Second, apply the formula for that interval. For example, if f(x) = {x² for x < 0; 2x + 1 for x ≥ 0}, then f(−3) uses the first piece: (−3)² = 9. But f(2) uses the second piece: 2(2) + 1 = 5. The domain restrictions are the guardrails — you must check which "case" applies before computing. This is directly connected to solving inequalities: the condition "x < 0" is an inequality, and you're using your inequality-solving skills to decide which branch applies.

Graphing a piecewise function means drawing each piece only on its specified interval, like coloring within strict boundary lines. At the boundary point between two pieces, you must decide which piece "owns" that point. An **open circle** at an endpoint means the piece stops just before that value (the point is excluded); a **closed circle** means the piece includes that endpoint. If two pieces meet at the same y-value at their shared boundary, the function is continuous there — the graph has no jump. If they meet at different y-values, there is a jump discontinuity. The absolute value function is piecewise but continuous because both pieces give y = 0 at x = 0.

Real-world contexts are full of piecewise functions. Tax brackets are a classic example: you pay one rate on income up to a threshold, a higher rate on income above it. Postage pricing works similarly — a letter under 1 oz costs one amount, 1–2 oz costs more. These scenarios naturally produce piecewise rules because the underlying relationship genuinely changes at boundary values. Recognizing this pattern — "different rules for different ranges" — is the core skill that piecewise functions develop, and it's foundational for understanding continuity more rigorously in calculus.
