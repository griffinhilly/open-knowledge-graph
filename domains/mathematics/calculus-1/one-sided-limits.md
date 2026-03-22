---
id: one-sided-limits
title: One-Sided Limits
domain: mathematics
course: calculus-1
prerequisites:
- id: limit-definition-intuitive
  type: hard
- id: piecewise-functions
  type: soft
- id: piecewise-functions-graphing
  type: soft
builds-toward:
- continuity-definition
- infinite-limits
tags:
- limits
- one-sided
- left-right
stage: formal-systems
status: validated
---
# One-Sided Limits

## Core Idea
A one-sided limit describes the behavior of f(x) as x approaches a from only one direction: from the left (x -> a-) or from the right (x -> a+). The two-sided limit exists if and only if both one-sided limits exist and are equal. One-sided limits are essential for analyzing piecewise functions, absolute value functions, and functions with jump discontinuities.

## How It's Best Learned
Evaluate one-sided limits from graphs and from piecewise function definitions. Compare left and right limits to determine whether the two-sided limit exists. Connect to continuity: a function is continuous at a only if both one-sided limits equal f(a).

## Common Misconceptions
- Assuming the limit exists whenever one side exists (both sides must agree).
- Confusing the notation: the minus sign in x -> a- means "from the left," not "negative a."
- Forgetting that at endpoints of a domain, only one-sided limits make sense.

## Questions

```yaml
- question: "For f(x) = x² when x < 2 and f(x) = x + 1 when x ≥ 2, what is lim_{x→2} f(x)?"
  type: multiple-choice
  options:
    - "The limit does not exist — the left-hand limit is 4 but the right-hand limit is 3"
    - "4 — substitute into the x < 2 piece"
    - "3 — substitute into the x ≥ 2 piece"
    - "2 — the input value is 2, so the limit is 2"
  answer: 0
  explanation: "The two-sided limit exists only when both one-sided limits agree. From the left: lim_{x→2⁻} x² = 4. From the right: lim_{x→2⁺} (x+1) = 3. Since 4 ≠ 3, the two-sided limit does not exist — this is a jump discontinuity. Options B and C each use only one side; option D confuses the input value with the limit value. The two-sided limit requires consensus from both directions."

- question: "A student evaluates a function and finds lim_{x→5⁺} g(x) = 7. She concludes that lim_{x→5} g(x) = 7. What error has she made?"
  type: multiple-choice
  options:
    - "She computed only the right-hand limit; the two-sided limit also requires lim_{x→5⁻} g(x) = 7"
    - "Nothing — if the right-hand limit exists and equals 7, the two-sided limit is automatically 7"
    - "She should have computed lim_{x→5⁻} instead, since the two-sided limit is defined by the left approach"
    - "The two-sided limit requires the function value g(5) to also equal 7"
  answer: 0
  explanation: "The two-sided limit requires both one-sided limits to exist AND agree. Knowing the right-hand limit gives only half the picture. The function could have lim_{x→5⁻} g(x) = 3, in which case the two-sided limit would not exist despite the right-hand limit being defined. The student has made the classic error of treating one-sided existence as sufficient for two-sided existence."

- question: "If lim_{x→a⁻} f(x) = 5 and lim_{x→a⁺} f(x) = 5, then lim_{x→a} f(x) = 5."
  type: true-false
  answer: true
  explanation: "This is the precise theorem: the two-sided limit equals L if and only if both the left-hand limit and the right-hand limit equal L. When both one-sided limits exist and agree on the same value, the two-sided limit exists and equals that value. Note that f(a) itself could be undefined, different from 5, or equal to 5 — the limit only depends on the behavior near a, not at a."

- question: "In the notation lim_{x→a⁻} f(x), the minus superscript means x is approaching a negative value."
  type: true-false
  answer: false
  explanation: "The superscript '−' means 'from the left' — that is, x approaches a through values strictly less than a (e.g., lim_{x→5⁻} means x takes values like 4.9, 4.99, 4.999...). It has nothing to do with a being negative. You can write lim_{x→(−3)⁻} for a left-hand limit at a = −3, or lim_{x→100⁻} for a left-hand limit at a positive number. The sign indicates direction of approach, not the sign of a."

- question: "Explain in your own words why a function can have both one-sided limits exist at a point, yet the two-sided limit fails to exist."
  type: short-answer
  answer: "The two-sided limit requires the function to be approaching a single agreed-upon value from both directions simultaneously. If the left-hand limit and right-hand limit converge to different values, then as x approaches a from different sides, f(x) is heading toward two different targets — there is no single value that f(x) gets arbitrarily close to. The two-sided limit captures the idea of approach from all directions at once."
  explanation: "The sign function sgn(x) = |x|/x is the classic example: it approaches −1 from the left and +1 from the right at x = 0. Both one-sided limits exist (well-defined targets), but the two-sided limit fails because the two sides disagree. The function is 'doing something different' on each side of 0. A piecewise function with different formulas on each side often produces this situation."
```

## Explainer

From your work with **limits**, you know that lim_{x→a} f(x) = L means f(x) gets arbitrarily close to L as x gets close to a from *either* direction simultaneously. But what if the function behaves differently depending on which side of a you approach from? That's exactly what one-sided limits capture. The **left-hand limit** lim_{x→a⁻} f(x) asks: what does f(x) approach as x approaches a while remaining strictly less than a? The **right-hand limit** lim_{x→a⁺} f(x) asks the same question from above. The superscript "−" means "from the left" (values smaller than a), not "negative a."

The connection to the two-sided limit is precise: lim_{x→a} f(x) = L if and only if *both* lim_{x→a⁻} f(x) = L and lim_{x→a⁺} f(x) = L. Both one-sided limits must exist *and* agree. A **piecewise function** like f(x) = x² for x < 2 and f(x) = x + 1 for x ≥ 2 illustrates this. From the left, lim_{x→2⁻} f(x) = 4. From the right, lim_{x→2⁺} f(x) = 3. These don't agree, so the two-sided limit at x = 2 does not exist, even though both one-sided limits exist. This is a **jump discontinuity** — a gap where the function's value jumps instantaneously.

Absolute value functions also require one-sided analysis. Consider lim_{x→0} |x|/x. For x > 0, |x|/x = x/x = 1. For x < 0, |x|/x = −x/x = −1. The right-hand limit is 1 and the left-hand limit is −1; they disagree, so the two-sided limit does not exist. The expression |x|/x is essentially defining the sign function: it outputs +1 or −1 depending on which side of zero x is on. Without one-sided limits, you'd have no clean way to describe this behavior.

One-sided limits also matter at **domain endpoints**. The function f(x) = √x is only defined for x ≥ 0, so only the right-hand limit lim_{x→0⁺} √x = 0 makes sense at x = 0 — there is no left-hand limit because the function doesn't exist to the left of 0. This connects directly to the definition of **continuity** you'll study next: a function is continuous at an interior point a if and only if both one-sided limits equal f(a), and continuous at an endpoint if the one relevant one-sided limit equals f(a).
