---
id: lhopitals-rule-rigorous
title: L'Hôpital's Rule (Rigorous)
domain: mathematics
course: real-analysis
prerequisites:
- id: mean-value-theorem-rigorous
  type: hard
tags:
- lhopitals
- limits
- indeterminate-forms
stage: advanced
status: draft
---

# L'Hôpital's Rule (Rigorous)

## Core Idea
L'Hôpital's Rule provides a rigorous method for evaluating limits of the form 0/0 or ∞/∞: if lim f(x)/g(x) is indeterminate and lim f'(x)/g'(x) exists, then they are equal (with care about the domain). The proof uses the Cauchy Mean Value Theorem and careful limit analysis. The rule extends to one-sided and infinite limits.

## Explainer

You know from the Mean Value Theorem that on an interval [a, b], there exists some c where f'(c) equals the average rate of change (f(b) − f(a))/(b − a). The **Cauchy Mean Value Theorem** generalizes this: for differentiable functions f and g on [a, b] with g'(c) ≠ 0, there exists c where f'(c)/g'(c) = (f(b) − f(a))/(g(b) − g(a)). This is the engine of L'Hôpital's proof. In the 0/0 case, take x approaching a: both f(x) → 0 and g(x) → 0, so f(x)/g(x) = (f(x) − f(a))/(g(x) − g(a)) (since both limits are zero). By the Cauchy MVT, for each x near a there is a c between a and x where this ratio equals f'(c)/g'(c). As x → a, c is squeezed between a and x, so c → a too — and if lim f'(x)/g'(x) exists at a, this forces lim f(x)/g(x) to equal the same limit.

The 0/0 case is the clearest to visualize: near the indeterminate point, both functions are nearly zero, so the ratio is determined entirely by their rates of departure from zero — their derivatives. If f'(a) = 2 and g'(a) = 3, then near a, f(x) ≈ 2(x − a) and g(x) ≈ 3(x − a), so f/g ≈ 2/3. L'Hôpital's rule formalizes this linearization idea and extends it to cases where the derivatives themselves form indeterminate forms, allowing repeated application. The ∞/∞ case requires a different argument (one cannot write ∞ − ∞ as zero), but the conclusion is the same.

Several hypotheses are essential and easily overlooked. First, the indeterminate form must actually occur: the rule applies only when the original limit is 0/0 or ±∞/∞. Applying it to a limit like (x + 1)/(x + 2) → 1/2 would give the wrong answer. Second, lim f'(x)/g'(x) must exist (or equal ±∞) for the rule to apply — if the ratio of derivatives oscillates without converging, no conclusion follows. Third, g'(x) must be nonzero near the limit point (though possibly at zero at the limit itself). Forgetting any of these conditions is a common source of error in application.

Other **indeterminate forms** — 0 · ∞, ∞ − ∞, 0⁰, 1^∞, ∞⁰ — are not covered directly by the rule but can be algebraically converted to 0/0 or ∞/∞ first. For example, 0 · ∞ can be rewritten as 0/(1/∞) = 0/0, and exponential forms like 1^∞ are handled by taking logarithms and then applying the rule to the resulting 0 · ∞ product. The rule is powerful precisely because it reduces all these forms to a single computational procedure, but the rigorous version demands you verify the hypotheses each time — repeated application of a rule in an invalid context is one of the most common errors in analysis.


