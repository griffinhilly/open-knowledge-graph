---
id: limit-laws
title: Limit Laws
domain: mathematics
course: calculus-1
prerequisites:
  - id: limit-definition-intuitive
    type: hard
builds-toward:
  - continuity-definition
  - squeeze-theorem
  - limits-at-infinity
tags: [limits, laws, computation]
stage: formal-systems
status: validated
---

# Limit Laws

## Core Idea
Limit laws are rules that allow you to compute limits algebraically by breaking complex expressions into simpler pieces. If lim f(x) = L and lim g(x) = M, then lim(f + g) = L + M, lim(f * g) = L * M, lim(f/g) = L/M (when M is not 0), and lim(f^n) = L^n. These laws formalize the intuition that the limit of a combination equals the combination of limits, and they are the workhorse tools for evaluating limits without tables or graphs.

## How It's Best Learned
State each law, verify with examples, then practice applying them to compute limits of polynomial and rational functions. Show that for polynomials, limits can be found by direct substitution (a consequence of the limit laws). Emphasize the cases where the laws do not directly apply (0/0 indeterminate forms).

## Common Misconceptions
- Applying the quotient law when the denominator's limit is zero (this requires further analysis, not the quotient law).
- Assuming all limit laws hold for infinite limits (some do, some produce indeterminate forms).
- Believing limit laws are definitions rather than consequences of the precise limit definition.

## Questions

```yaml
- question: "You want to find lim_{x→2} (x² + 3x)/(x − 2). You apply the quotient law and get (4 + 6)/(2 − 2) = 10/0. What should you conclude?"
  type: multiple-choice
  options:
    - "The limit is infinity, since 10/0 = ∞"
    - "The limit does not exist, since the quotient law produces an undefined result"
    - "The quotient law cannot be applied here because the denominator's limit is 0; further analysis is required"
    - "You should apply L'Hôpital's rule directly to get lim = 10/1 = 10"
  answer: 2
  explanation: "The quotient law states lim(f/g) = L/M only when M ≠ 0. When M = 0, the quotient law simply does not apply — you cannot draw any conclusion from it. The result 10/0 is not '∞'; it signals that this case requires different analysis. Here lim(x²+3x) = 10 ≠ 0 and lim(x−2) = 0, which indicates vertical asymptote behavior — but you must determine this through further work, not by mechanically writing '10/0 = ∞.'"

- question: "A student evaluates lim_{x→3} (x²−9)/(x−3) by substituting x = 3, gets 0/0, and concludes the limit doesn't exist. A second student factors to get lim_{x→3}(x+3) = 6. Who is correct?"
  type: multiple-choice
  options:
    - "The first student; substituting x = 3 gives 0/0 which means the limit is undefined"
    - "Neither; a 0/0 form always means further limit laws must be applied iteratively"
    - "The second student; 0/0 is an indeterminate form signaling the quotient law fails, not that the limit doesn't exist"
    - "Both are correct; 0/0 and 6 are equivalent in limit notation"
  answer: 2
  explanation: "0/0 is an indeterminate form — it means the quotient law fails and further algebraic work is needed, not that the limit is undefined or doesn't exist. The second student correctly factors the numerator as (x−3)(x+3), cancels (x−3) (valid since x ≠ 3 in a limit), and applies direct substitution to (x+3), getting 6. The indeterminate form is a signal to look for hidden algebraic structure, not a dead end."

- question: "For any polynomial p(x), the limit as x approaches any real number a can be found by direct substitution: lim_{x→a} p(x) = p(a)."
  type: true-false
  answer: true
  explanation: "This follows directly from the limit laws. A polynomial is built from sums and products of constants and powers of x. The limit laws say limits distribute over sums and products. The foundational limits lim_{x→a} c = c and lim_{x→a} x = a hold by definition. Applying the limit laws repeatedly through the polynomial's structure reduces everything to p(a). Direct substitution for polynomials is not magic — it is the limit laws working automatically."

- question: "Limit laws are the definitions of what limits mean — they establish how limits of sums, products, and quotients are computed."
  type: true-false
  answer: false
  explanation: "Limit laws are theorems, not definitions. The limit is defined independently (via epsilon-delta or as the value a function approaches). The limit laws are then proved from that definition: if you can get f close to L and g close to M, you can prove rigorously that f+g gets close to L+M. The laws are derived results that make computation convenient. This distinction matters because the laws have conditions (like M ≠ 0 for the quotient law) that make no sense if they were definitions."

- question: "Explain why the quotient law fails when the denominator's limit is zero, and what this failure tells you about how to proceed."
  type: short-answer
  answer: "The quotient law requires M ≠ 0 because division by zero is undefined, and when M = 0, the ratio f/g can behave in any number of ways as x approaches a: it might approach a finite value (0/0 indeterminate form, requiring algebraic simplification), blow up to ±∞ (vertical asymptote), or fail to exist. The failure of the quotient law is a diagnostic signal — not a final answer — that tells you which case you're in and that a different technique is needed: factoring and canceling, conjugate multiplication, L'Hôpital's rule, or the squeeze theorem."
  explanation: "Recognizing when limit laws fail is as important as knowing what they say. 'The law doesn't apply' is informative: it tells you that you're in a case requiring special treatment. Students who mechanically write '0/0' as an answer have misunderstood the quotient law; students who recognize it as an indeterminate form know they need a different strategy."
```

## Explainer

When you first learned about limits, you built intuition: the limit of f(x) as x → a is the value f(x) approaches as x gets close to a. That intuition is powerful but it leaves a practical question unanswered: how do you actually *compute* a limit for a complicated expression? **Limit laws** answer this by giving you a toolkit for breaking a complex limit into smaller, manageable pieces — much like order of operations lets you evaluate arithmetic by breaking it into steps.

The core laws say that limits distribute across the basic operations. If lim f(x) = L and lim g(x) = M (as x → a), then: the limit of f + g is L + M, the limit of f · g is L · M, and the limit of f/g is L/M — provided M ≠ 0. There is also a power law: the limit of [f(x)]ⁿ is Lⁿ. These are not definitions or conventions; they are theorems that follow from the precise epsilon-delta definition of a limit. The idea behind each law is the same: if you can get f as close to L as you like, and g as close to M as you like, then their sum (or product) gets as close to L + M (or L · M) as you like.

The most immediate application is **direct substitution for polynomials**. Every polynomial p(x) satisfies lim_{x→a} p(x) = p(a). Why? Because a polynomial is just sums and products of constants and powers of x, and by the limit laws, you can push the limit through every sum and product until you are evaluating limits of the form lim x = a and lim c = c — both of which are obvious from the definition. This makes evaluating polynomial limits trivial: just plug in. Rational functions work the same way whenever the denominator is not zero at the point.

The limit laws break down at exactly one point: the **quotient law fails when M = 0**. If lim g(x) = 0, you cannot conclude anything from L/M because division by zero is undefined — and the limiting behavior can be anything: the limit might be finite (0/0 indeterminate form requiring algebraic simplification), infinite (one-sided vertical asymptote), or genuinely nonexistent. This is the boundary where limit laws end and more specialized techniques — factoring and canceling, L'Hôpital's rule, conjugate multiplication — take over. Recognizing when you are in the 0/0 or ∞/∞ regime, and knowing that the limit laws alone cannot resolve it, is as important as knowing what the laws do say.
