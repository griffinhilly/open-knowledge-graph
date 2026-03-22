---
id: lhopitals-rule
title: 'L''Hopital''s Rule'
domain: mathematics
course: calculus-1
prerequisites:
- id: limits-at-infinity
  type: hard
- id: derivatives-of-trigonometric-functions
  type: soft
- id: derivatives-of-exponential-functions
  type: soft
- id: infinite-limits
  type: soft
- id: mean-value-theorem
  type: soft
builds-toward:
- improper-integrals-convergence
- taylor-series
tags:
- limits
- indeterminate-forms
- lhopital
stage: formal-systems
status: validated
---
# L'Hopital's Rule

## Core Idea
L'Hopital's Rule states that if lim f(x)/g(x) produces an indeterminate form 0/0 or infinity/infinity, then the limit equals lim f'(x)/g'(x), provided this latter limit exists. The rule can be applied repeatedly for persistent indeterminate forms. Other indeterminate forms (0 * infinity, infinity - infinity, 0^0, 1^infinity, infinity^0) can be converted to 0/0 or infinity/infinity form first.

## How It's Best Learned
Verify indeterminate form before applying. Practice with 0/0 and infinity/infinity cases. Then learn to convert other indeterminate forms. Compare with algebraic techniques (factoring, rationalizing) which sometimes work better. Emphasize that L'Hopital's Rule applies to f'/g', not (f/g)'.

## Common Misconceptions
- Applying L'Hopital's Rule when the form is not indeterminate (e.g., 1/0 is not indeterminate).
- Using the quotient rule instead of differentiating numerator and denominator separately.
- Applying the rule in a circular loop without recognizing the limit can be computed directly.

## Questions

```yaml
- question: "A student evaluates lim(x→0) x/sin(2x) using L'Hôpital's Rule. They apply the quotient rule to compute d/dx[x/sin(2x)] = (sin(2x) − 2x·cos(2x))/sin²(2x) and then take the limit as x→0. What mistake did the student make?"
  type: multiple-choice
  options:
    - "L'Hôpital's Rule does not apply here because the form is not indeterminate"
    - "The student used the quotient rule instead of differentiating numerator and denominator separately; the rule requires lim f′(x)/g′(x), not lim (f/g)′(x)"
    - "The student should have applied the rule twice before evaluating the limit"
    - "The form is ∞/∞, not 0/0, so a different conversion is needed first"
  answer: 1
  explanation: "L'Hôpital's Rule says replace f/g with f′/g′ — differentiate top and bottom separately. Using the quotient rule gives (f/g)′, which is a different expression entirely and will produce the wrong answer. Here, the correct application gives 1/(2cos(2x)) → 1/2 as x→0."

- question: "Which of the following limits requires rewriting into 0/0 or ∞/∞ form before L'Hôpital's Rule can be applied?"
  type: multiple-choice
  options:
    - "lim(x→0) sin(x)/x"
    - "lim(x→∞) eˣ/x²"
    - "lim(x→0⁺) x·ln(x)"
    - "lim(x→1) (x² − 1)/(x − 1)"
  answer: 2
  explanation: "lim x·ln(x) as x→0⁺ is 0·(−∞) — a product, not a ratio. L'Hôpital's Rule requires a ratio, so you must rewrite it as ln(x)/(1/x), which gives −∞/∞ form, then apply the rule. Options A, C (actually C is the answer), D are already ratios in 0/0 or ∞/∞ form."

- question: "Applying L'Hôpital's Rule to lim(x→0) (x+1)/x is valid because substituting x = 0 produces a fraction with 0 in the denominator."
  type: true-false
  answer: false
  explanation: "The form is 1/0, which is NOT indeterminate. A nonzero numerator over a shrinking denominator tells you the limit diverges to ±∞ — no ambiguity about the limit's value. L'Hôpital's Rule only applies to 0/0 and ∞/∞. Applying it to 1/0 gives the wrong answer."

- question: "When applying L'Hôpital's Rule, you differentiate the numerator and denominator as separate functions, not as a quotient."
  type: true-false
  answer: true
  explanation: "This is the central procedural point: lim f(x)/g(x) = lim f′(x)/g′(x). You compute f′ and g′ independently, then form their ratio. Using the quotient rule — computing (f/g)′ = (f′g − fg′)/g² — is the most common algebraic error and produces a different, incorrect expression."

- question: "Explain why L'Hôpital's Rule cannot be applied to a limit of the form 3/0, even though substitution produces an undefined expression."
  type: short-answer
  answer: "3/0 is not indeterminate — it means the limit is ±∞. The numerator stays near 3 while the denominator vanishes, so the ratio grows without bound. Indeterminate forms like 0/0 or ∞/∞ give no information about the limit because two competing tendencies are in tension (both numerator and denominator approach 0 or ∞ simultaneously). L'Hôpital's Rule resolves that tension; there is no tension to resolve in 3/0."
  explanation: "The word 'indeterminate' is precise: the form alone cannot determine the limit's value, so more information (derivatives) is needed. A form like 3/0 tells you exactly what happens: the expression blows up. Applying L'Hôpital there would give 0/1 = 0, which is simply wrong."
```

## Explainer

From limits at infinity and derivatives, you know that most limits can be evaluated by substitution — just plug in the limiting value and simplify. The problem arises when substitution produces a form like 0/0 or ∞/∞. These are called **indeterminate forms** because the expression itself gives no information about the limit's value — the limit could be any number, or it might not exist. For example, lim (sin x)/x as x → 0 gives 0/0, yet the limit is 1. **L'Hôpital's Rule** resolves this by turning a limit of a ratio into a limit of a ratio of derivatives: if lim f(x)/g(x) is 0/0 or ∞/∞, then lim f(x)/g(x) = lim f′(x)/g′(x), provided the latter limit exists.

The critical procedure is always to check the indeterminate form first. Only 0/0 and ∞/∞ qualify directly. If the form is 3/0, the limit is ±∞ (not indeterminate — you don't need the rule, and applying it would be wrong). Once you confirm the form, differentiate numerator and denominator **separately** — this is not the quotient rule, which differentiates the whole fraction as a single entity. The rule says replace f/g with f′/g′, not with (f/g)′. This is the most common algebraic error.

Other indeterminate forms — 0·∞, ∞−∞, 0⁰, 1^∞, ∞⁰ — are handled by converting them to 0/0 or ∞/∞ first. For 0·∞: rewrite f·g as f/(1/g) or g/(1/f). For ∞−∞: find a common denominator or multiply by a conjugate. For exponential forms like 1^∞: take the natural log first — ln(f(x)^g(x)) = g(x)·ln(f(x)), which converts the problem to 0·∞ form, then apply L'Hôpital, then exponentiate at the end. The standard example is lim (1 + 1/x)^x as x → ∞: taking the log gives x·ln(1 + 1/x), a 0·∞ form that resolves to 1, so the original limit is e¹ = e.

Algebraic methods — factoring, rationalizing, known limits like sin(x)/x — are often faster and should be preferred when they apply. L'Hôpital's Rule is a fallback, not a first resort. The rule can also be applied repeatedly if the new limit is still indeterminate, but watch for loops: trying to evaluate lim (eˣ/eˣ) by L'Hôpital keeps reproducing eˣ/eˣ = 1, which is the answer all along — just simplify directly. The rule will lead you in circles only when the limit is already accessible by simpler means.


