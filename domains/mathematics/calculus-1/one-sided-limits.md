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

## Explainer

From your work with **limits**, you know that lim_{x→a} f(x) = L means f(x) gets arbitrarily close to L as x gets close to a from *either* direction simultaneously. But what if the function behaves differently depending on which side of a you approach from? That's exactly what one-sided limits capture. The **left-hand limit** lim_{x→a⁻} f(x) asks: what does f(x) approach as x approaches a while remaining strictly less than a? The **right-hand limit** lim_{x→a⁺} f(x) asks the same question from above. The superscript "−" means "from the left" (values smaller than a), not "negative a."

The connection to the two-sided limit is precise: lim_{x→a} f(x) = L if and only if *both* lim_{x→a⁻} f(x) = L and lim_{x→a⁺} f(x) = L. Both one-sided limits must exist *and* agree. A **piecewise function** like f(x) = x² for x < 2 and f(x) = x + 1 for x ≥ 2 illustrates this. From the left, lim_{x→2⁻} f(x) = 4. From the right, lim_{x→2⁺} f(x) = 3. These don't agree, so the two-sided limit at x = 2 does not exist, even though both one-sided limits exist. This is a **jump discontinuity** — a gap where the function's value jumps instantaneously.

Absolute value functions also require one-sided analysis. Consider lim_{x→0} |x|/x. For x > 0, |x|/x = x/x = 1. For x < 0, |x|/x = −x/x = −1. The right-hand limit is 1 and the left-hand limit is −1; they disagree, so the two-sided limit does not exist. The expression |x|/x is essentially defining the sign function: it outputs +1 or −1 depending on which side of zero x is on. Without one-sided limits, you'd have no clean way to describe this behavior.

One-sided limits also matter at **domain endpoints**. The function f(x) = √x is only defined for x ≥ 0, so only the right-hand limit lim_{x→0⁺} √x = 0 makes sense at x = 0 — there is no left-hand limit because the function doesn't exist to the left of 0. This connects directly to the definition of **continuity** you'll study next: a function is continuous at an interior point a if and only if both one-sided limits equal f(a), and continuous at an endpoint if the one relevant one-sided limit equals f(a).
