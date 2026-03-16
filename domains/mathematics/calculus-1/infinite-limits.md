---
id: infinite-limits
title: Infinite Limits
domain: mathematics
course: calculus-1
prerequisites:
- id: limit-definition-intuitive
  type: hard
- id: rational-functions-asymptotes-review
  type: hard
- id: one-sided-limits
  type: soft
builds-toward:
- lhopitals-rule
tags:
- limits
- infinity
- vertical-asymptotes
stage: formal-systems
status: validated
---
# Infinite Limits

## Core Idea
An infinite limit occurs when f(x) increases or decreases without bound as x approaches a finite value a. We write lim(x->a) f(x) = infinity or -infinity. Strictly speaking, the limit "does not exist" as a real number, but the infinity notation conveys useful directional information. Infinite limits correspond to vertical asymptotes on the graph.

## How It's Best Learned
Analyze rational functions near their vertical asymptotes by checking the sign of the function on each side. Practice determining whether the function goes to +infinity or -infinity from the left vs. right. Connect to the factored form of the denominator.

## Common Misconceptions
- Saying the limit "equals infinity" as if infinity is a number (it is a description of unbounded growth).
- Not checking both sides: the function may go to +infinity from one side and -infinity from the other.
- Confusing infinite limits (vertical asymptotes) with limits at infinity (horizontal asymptotes).

## Explainer

You already understand limits intuitively: lim(x→a) f(x) = L means f(x) gets arbitrarily close to L as x approaches a. **Infinite limits** arise when f(x) doesn't settle toward any finite number — instead it grows without bound. Writing lim(x→a) f(x) = ∞ is a way of reporting that failure precisely: we're not claiming ∞ is a number the function "reaches," but that f(x) exceeds any finite bound you name as x gets close to a.

The mechanism behind infinite limits is always a denominator approaching zero while the numerator stays finite. Consider f(x) = 1/(x−3) near x = 3. As x approaches 3 from the right, the denominator (x−3) is a tiny positive number, so 1/(x−3) is a huge positive number — it blows up toward +∞. From the left, (x−3) is a tiny *negative* number, so 1/(x−3) blows up toward −∞. This is why **one-sided limits matter** for infinite limits: the two sides often go in opposite directions. When lim from the left is −∞ and from the right is +∞, there is no single infinite limit — the two-sided limit simply does not exist, though both one-sided limits exist (as infinite).

To determine the sign (+∞ or −∞), analyze the sign of f(x) on each side of the asymptote. For a rational function, factor and evaluate the sign of each factor just to the left and right of the vertical asymptote. A product of an odd number of negative factors gives a negative result. This sign analysis doesn't require computing any values — just tracking positives and negatives.

One critical naming distinction to lock in: **infinite limits** (this topic) describe behavior near a finite x-value where the output blows up — these correspond to vertical asymptotes. **Limits at infinity** (a separate topic) describe behavior as x itself grows without bound and ask whether the output settles toward a finite value — these correspond to horizontal asymptotes. The word "infinite" appears in both phrases but refers to different things: in one case it's the output that's infinite, in the other it's the input. Keeping this straight will prevent systematic confusion in L'Hôpital's rule and later asymptotic analysis.
