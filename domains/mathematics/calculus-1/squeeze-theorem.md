---
id: squeeze-theorem
title: Squeeze Theorem
domain: mathematics
course: calculus-1
prerequisites:
  - id: limit-laws
    type: hard
builds-toward:
  - derivatives-of-trigonometric-functions
tags: [limits, squeeze-theorem, special-limits]
stage: formal-systems
status: validated
---

# Squeeze Theorem

## Core Idea
The Squeeze Theorem states that if g(x) <= f(x) <= h(x) near x = a, and lim g(x) = lim h(x) = L, then lim f(x) = L. The function f is "squeezed" between two functions that converge to the same limit. The most famous application is proving lim(x->0) sin(x)/x = 1, a result needed for the derivative of sin(x).

## How It's Best Learned
Prove lim(x->0) sin(x)/x = 1 geometrically using the unit circle area argument. Then apply the squeeze theorem to related limits like lim(x->0) (1 - cos(x))/x = 0. Practice identifying bounding functions in other squeeze theorem problems (e.g., x^2 * sin(1/x) near 0).

## Common Misconceptions
- Trying to apply the squeeze theorem when the bounding functions do not converge to the same limit.
- Confusing the squeeze theorem with limit comparison (they are different tools).
- Not verifying the inequality g(x) <= f(x) <= h(x) holds near the point of interest.

## Questions

```yaml
- question: "A student wants to find lim(x→0) x²·sin(1/x). They note that sin(1/x) oscillates wildly near 0 and conclude the limit does not exist. Which approach correctly finds the limit?"
  type: multiple-choice
  options:
    - "Direct substitution: 0²·sin(1/0) = 0, so the limit is 0"
    - "Since −x² ≤ x²sin(1/x) ≤ x² and both ±x² → 0 as x → 0, the Squeeze Theorem gives the limit as 0"
    - "Apply L'Hôpital's rule to the expression to resolve the oscillation"
    - "The limit does not exist because sin(1/x) has no limit as x → 0"
  answer: 1
  explanation: "Even though sin(1/x) oscillates infinitely near 0, we always have −1 ≤ sin(1/x) ≤ 1, which gives −x² ≤ x²sin(1/x) ≤ x². Both bounding functions approach 0, so the Squeeze Theorem forces the limit to 0. The oscillation of sin(1/x) is irrelevant — the bounding functions trap f regardless. L'Hôpital's rule doesn't apply here (x²sin(1/x) is not in 0/0 or ∞/∞ form), and option D ignores that f can still have a limit even when a factor does not."

- question: "To apply the Squeeze Theorem to find lim(x→a) f(x), a student finds g(x) ≤ f(x) ≤ h(x) near x = a, with lim g(x) = 2 and lim h(x) = 3. What conclusion is valid?"
  type: multiple-choice
  options:
    - "lim f(x) = 2.5, the midpoint of the two limiting values"
    - "lim f(x) = 2, since g is the lower bound"
    - "The Squeeze Theorem cannot be applied; the bounding limits must be equal"
    - "2 ≤ lim f(x) ≤ 3, a valid squeeze-theorem conclusion"
  answer: 2
  explanation: "The Squeeze Theorem requires that both bounding functions converge to the *same* limit L. When lim g(x) = 2 ≠ 3 = lim h(x), the theorem gives no conclusion — f could approach any value in [2, 3], or the bounds might not trap f tightly enough to determine the limit at all. Option D sounds reasonable but is NOT what the Squeeze Theorem provides; it only applies when both limits are equal. The theorem is an equality result, not an interval result."

- question: "The Squeeze Theorem can be used to find lim(x→0) sin(x)/x = 1 even though sin(x)/x is undefined at x = 0."
  type: true-false
  answer: true
  explanation: "The Squeeze Theorem only requires the bounding inequality g(x) ≤ f(x) ≤ h(x) to hold *near* x = a — not necessarily at x = a itself. The function sin(x)/x is undefined at 0, but the bounds cos(x) ≤ sin(x)/x ≤ 1 hold for all small nonzero x in radians. Since both bounds converge to 1 as x → 0, the limit is 1. This is precisely the power of limit arguments: behavior at a point is irrelevant to the limit."

- question: "If g(x) ≤ f(x) ≤ h(x) near x = a, and lim(x→a) g(x) = lim(x→a) h(x) = L, then f(x) = L for most x near a."
  type: true-false
  answer: false
  explanation: "The Squeeze Theorem concludes that lim(x→a) f(x) = L — a statement about the *limit*, not about the function's values. f(x) can oscillate, dip, or spike away from L at individual points near a, as long as it is trapped between g and h and those bounds squeeze toward L. For example, x²sin(1/x) oscillates wildly near 0 but has limit 0. Confusing a limit with a function value is a fundamental error."

- question: "Why does proving lim(x→0) sin(x)/x = 1 require geometric reasoning rather than algebraic manipulation?"
  type: short-answer
  answer: "Direct substitution gives 0/0 — an indeterminate form that algebraic simplification cannot resolve, because sin(x)/x has no simpler closed form at x = 0. The geometric argument uses the unit circle to establish the inequality cos(x) ≤ sin(x)/x ≤ 1 for small positive x in radians, derived by comparing the areas of a triangle, a circular sector, and a larger triangle. The Squeeze Theorem then takes over from there, forcing the limit to 1 since both bounds converge to 1."
  explanation: "This limit is foundational because it underlies the derivative of sin(x). The geometric proof reveals *why* the limit is 1 — it is a consequence of how arc length compares to chord length on the unit circle, not an algebraic accident. The bounding strategy (find a function always ≥ f and always ≤ f with the same limit) is the core skill: once you have the bounds, the Squeeze Theorem is automatic."
```

## Explainer

From your study of limit laws, you know how to compute limits of sums, products, and quotients algebraically. But some functions resist those techniques — particularly functions like sin(x)/x near x = 0, where direct substitution gives 0/0, an indeterminate form. The Squeeze Theorem is a geometric argument that sidesteps algebraic manipulation by trapping the function between two simpler ones.

The logic is intuitive: if you know a value lies between 3.99 and 4.01, you know it's close to 4. The Squeeze Theorem makes this precise for limits. If g(x) ≤ f(x) ≤ h(x) for all x near a (but not necessarily at a), and both g and h approach the same limit L as x → a, then f is permanently trapped between values approaching L — so f must also approach L. There is no room for f to wander off to a different value.

The canonical application is proving **lim(x→0) sin(x)/x = 1**, which is essential for deriving d/dx[sin x] = cos x. The proof uses a geometric argument on the unit circle: comparing the areas of a small triangle, a circular sector, and a larger triangle, one obtains sin x ≤ x ≤ tan x for small positive x (in radians). Dividing through by sin x and taking reciprocals gives the bounds cos x ≤ sin(x)/x ≤ 1. Since lim(x→0) cos x = 1 and lim(x→0) 1 = 1, the Squeeze Theorem forces lim(x→0) sin(x)/x = 1. Every trigonometric derivative you will compute from this point onward rests on this single limit.

A second class of applications involves functions like f(x) = x² sin(1/x) near x = 0. Direct substitution fails (1/x is undefined at 0), and algebraic manipulation is impossible because sin(1/x) oscillates infinitely rapidly. But you know −1 ≤ sin(1/x) ≤ 1 always, so −x² ≤ x² sin(1/x) ≤ x². Both bounding functions approach 0 as x → 0, so the limit is 0. The **bounding strategy** — find a function that is always ≥ f and one always ≤ f, both with the same limit — is the skill to internalize. The bounds do not need to be tight everywhere, only near the point of interest.
