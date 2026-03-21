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

## Questions

```yaml
- question: "Consider f(x) = 1/(x−3). Which of the following best describes the behavior of f near x = 3?"
  type: multiple-choice
  options:
    - "lim(x→3) f(x) = ∞, because both one-sided limits go to +∞"
    - "lim(x→3) f(x) does not exist; the left-side limit is −∞ and the right-side limit is +∞"
    - "lim(x→3) f(x) = 0, because the denominator becomes zero"
    - "lim(x→3) f(x) = ∞ or −∞ depending on which side you approach from, so the limit equals ±∞"
  answer: 1
  explanation: "From the right, (x−3) is small and positive, so 1/(x−3) → +∞. From the left, (x−3) is small and negative, so 1/(x−3) → −∞. Because the one-sided limits disagree, the two-sided limit does not exist — not even as ±∞. Option A is wrong because the left side goes to −∞, not +∞. Option C reverses the idea: a zero denominator causes the function to blow up, not approach zero. Option D misuses the notation ±∞ as if it were a single value."

- question: "A function has a horizontal asymptote at y = 2. Which concept does this correspond to?"
  type: multiple-choice
  options:
    - "An infinite limit: lim(x→a) f(x) = ∞ for some finite a"
    - "A limit at infinity: lim(x→∞) f(x) = 2"
    - "An infinite limit from only one side near x = 2"
    - "A vertical asymptote where the output is bounded by 2"
  answer: 1
  explanation: "A horizontal asymptote describes the output settling toward a finite value as the input grows without bound — that is a limit at infinity, lim(x→∞) f(x) = 2. An infinite limit is the opposite scenario: the input approaches a finite value (x → a) while the output blows up. These two concepts are easy to conflate because both involve the word 'infinite,' but one refers to an infinite output near a finite input (vertical asymptote), and the other refers to a finite output as the input becomes infinite (horizontal asymptote)."

- question: "Writing lim(x→a) f(x) = ∞ means the limit exists and equals the number infinity."
  type: true-false
  answer: false
  explanation: "Infinity is not a real number, so a limit that 'equals' ∞ technically does not exist in the standard real-number sense. The notation lim(x→a) f(x) = ∞ is a precise way of reporting a specific kind of non-existence: the function grows without bound as x approaches a. It conveys useful directional information about the failure mode, but it does not mean the limit has a real-number value."

- question: "If lim(x→a⁺) f(x) = +∞ and lim(x→a⁻) f(x) = −∞, then lim(x→a) f(x) = ∞."
  type: true-false
  answer: false
  explanation: "For the two-sided limit to exist (even as ∞), both one-sided limits must agree. Here the right-side limit is +∞ and the left-side limit is −∞ — they disagree in sign. Therefore the two-sided limit does not exist at all, not even as an infinite limit. Each one-sided infinite limit exists and conveys information, but they cannot be combined into a single two-sided limit when they go in opposite directions."

- question: "Why does an infinite limit technically 'not exist' as a real number, and what useful information does writing lim(x→a) f(x) = ∞ still convey?"
  type: short-answer
  answer: "The limit does not exist because ∞ is not a real number — the function never settles at a specific finite value. However, writing lim = ∞ communicates that the function grows without bound in the positive direction as x approaches a, which identifies a vertical asymptote and tells you the function's behavior is unbounded and in what direction. This is more informative than simply saying 'DNE.'"
  explanation: "Distinguishing 'technically DNE' from 'DNE but in a specific infinite way' is crucial for rigorous analysis. The notation lim = ∞ is a shorthand for 'for every M > 0, there exists δ > 0 such that |x − a| < δ implies f(x) > M' — a precise statement about unbounded growth, not an assertion that the limit has value ∞. Keeping the technical DNE and the descriptive ∞ notation separate prevents the common error of treating infinity as an arithmetic constant."
```

## Explainer

You already understand limits intuitively: lim(x→a) f(x) = L means f(x) gets arbitrarily close to L as x approaches a. **Infinite limits** arise when f(x) doesn't settle toward any finite number — instead it grows without bound. Writing lim(x→a) f(x) = ∞ is a way of reporting that failure precisely: we're not claiming ∞ is a number the function "reaches," but that f(x) exceeds any finite bound you name as x gets close to a.

The mechanism behind infinite limits is always a denominator approaching zero while the numerator stays finite. Consider f(x) = 1/(x−3) near x = 3. As x approaches 3 from the right, the denominator (x−3) is a tiny positive number, so 1/(x−3) is a huge positive number — it blows up toward +∞. From the left, (x−3) is a tiny *negative* number, so 1/(x−3) blows up toward −∞. This is why **one-sided limits matter** for infinite limits: the two sides often go in opposite directions. When lim from the left is −∞ and from the right is +∞, there is no single infinite limit — the two-sided limit simply does not exist, though both one-sided limits exist (as infinite).

To determine the sign (+∞ or −∞), analyze the sign of f(x) on each side of the asymptote. For a rational function, factor and evaluate the sign of each factor just to the left and right of the vertical asymptote. A product of an odd number of negative factors gives a negative result. This sign analysis doesn't require computing any values — just tracking positives and negatives.

One critical naming distinction to lock in: **infinite limits** (this topic) describe behavior near a finite x-value where the output blows up — these correspond to vertical asymptotes. **Limits at infinity** (a separate topic) describe behavior as x itself grows without bound and ask whether the output settles toward a finite value — these correspond to horizontal asymptotes. The word "infinite" appears in both phrases but refers to different things: in one case it's the output that's infinite, in the other it's the input. Keeping this straight will prevent systematic confusion in L'Hôpital's rule and later asymptotic analysis.
