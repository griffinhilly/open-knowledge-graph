---
id: solving-logarithmic-equations
title: Solving Logarithmic Equations
domain: mathematics
course: algebra-2
prerequisites:
  - id: logarithm-properties
    type: hard
  - id: logarithms-intro
    type: hard
builds-toward:
  - natural-logarithm-and-e
tags: [logarithms, equations, solving, extraneous-solutions]
stage: formal-systems
status: validated
---

# Solving Logarithmic Equations

## Core Idea
Logarithmic equations contain logarithmic expressions with the variable in the argument. Two main strategies: (1) If the equation has a single log on each side with the same base, set the arguments equal: log_b(A) = log_b(B) implies A = B. (2) If the equation has log = constant, convert to exponential form: log_b(A) = c means A = b^c. Use log properties to condense multiple log terms first. Always check for extraneous solutions (arguments of log must be positive).

## How It's Best Learned
Practice converting between log and exponential forms. Solve equations by condensing log expressions using properties, then converting. Emphasize domain checking: solutions must make all original log arguments positive. Give examples where extraneous solutions arise.

## Common Misconceptions
- Not checking domain restrictions (log of a negative number is undefined).
- Forgetting to condense multiple log terms before converting to exponential form.
- Confusing log_b(x) = y with b*x = y (should be b^y = x).
- Thinking that because algebraic steps produce a valid number, it must be a valid solution (must check domain).

## Questions

```yaml
- question: "You solve log₂(x) + log₂(x − 6) = 4 and obtain two candidates: x = 8 and x = −2. What is the correct solution set?"
  type: multiple-choice
  options:
    - "Both x = 8 and x = −2, since the algebra produces two valid numbers"
    - "x = 8 only, because x = −2 makes the argument log₂(−2) undefined"
    - "x = −2 only, because x = 8 makes the equation unbalanced"
    - "No real solution exists — the equation is undefined for positive x"
  answer: 1
  explanation: "After condensing to log₂(x(x−6)) = 4 and converting to x(x−6) = 16, the quadratic yields x = 8 and x = −2. But logarithms require strictly positive arguments. At x = −2, the original expressions log₂(−2) and log₂(−8) are both undefined. x = −2 is an extraneous solution — algebraically produced but not valid. x = 8 gives log₂(8) = 3 and log₂(2) = 1, which sum to 4. Only x = 8 is accepted."

- question: "To solve log₃(2x + 1) + log₃(x) = 2, what is the correct first step?"
  type: multiple-choice
  options:
    - "Set the arguments equal: 2x + 1 = x, then solve the linear equation"
    - "Apply the power rule and rewrite as log₃((2x + 1)·x²) = 2"
    - "Condense using the product rule: log₃(x(2x + 1)) = 2, then convert to 3² = x(2x + 1)"
    - "Convert each log separately: 3² = 2x + 1 and 3² = x, then solve the system"
  answer: 2
  explanation: "When multiple log terms share the same base, condense them first using log properties before converting to exponential form. The product rule gives log₃(x(2x+1)) = 2, which becomes 9 = 2x² + x, or 2x² + x − 9 = 0. Setting arguments equal (option A) only works when you have log_b(A) = log_b(B) — not log = constant. Converting each log separately (option D) misapplies the definition."

- question: "If solving a logarithmic equation yields x = 7, and plugging back in gives log₅(7 − 7) = log₅(0), then x = 7 is a valid solution."
  type: true-false
  answer: false
  explanation: "log₅(0) is undefined — logarithms require strictly positive arguments. Even though the algebra produced x = 7, it is an extraneous solution that must be rejected. The argument of any logarithm must be greater than zero. This is why domain checking is mandatory for every candidate solution."

- question: "An equation log_b(A) = log_b(B) can be solved by setting A = B because the logarithm function is one-to-one."
  type: true-false
  answer: true
  explanation: "This is correct. Because log_b is a one-to-one function (strictly increasing for b > 1), equal outputs force equal inputs: log_b(A) = log_b(B) implies A = B. This is the second main strategy for logarithmic equations. Note that you still must verify the resulting solution makes all original log arguments positive — setting A = B can itself produce an extraneous solution."

- question: "Why must you always check candidate solutions to a logarithmic equation against the original equation, even when the algebra produces a 'clean' numeric answer?"
  type: short-answer
  answer: "Because logarithms are only defined for strictly positive arguments. When combining log terms using properties (e.g., product or quotient rules) and converting to polynomial form, the algebra can produce values that satisfy the polynomial equation but make one or more original log arguments zero or negative. These are extraneous solutions — artifacts of the algebraic manipulation, not true solutions. Only values that keep every log argument strictly positive are valid."
  explanation: "The domain restriction (argument > 0) is intrinsic to logarithms. Once you convert a log equation to a polynomial via condensing and exponentiating, the polynomial's solution set may include points outside the domain of the original logarithmic expressions. There is no shortcut: every candidate answer must be substituted back into the original equation and all argument expressions checked."
```

## Explainer

Solving logarithmic equations rests on two ideas you already know: the definition of a logarithm as the inverse of exponentiation, and the log properties that let you combine or split logarithmic expressions. The definition says log_b(A) = c means exactly b^c = A — the log asks "what exponent on b gives A?" That relationship is the key to unlocking equations where the unknown is inside a logarithm.

There are two main situations. In the first, you have a single log equal to a number: log_b(expression) = c. Here you simply convert to exponential form — b^c = expression — and solve the resulting algebraic equation. For example, log₂(x + 3) = 4 becomes 2⁴ = x + 3, so x = 13. In the second situation, you have logs on both sides with the same base: log_b(A) = log_b(B). Since the log function is one-to-one (each output corresponds to exactly one input), equal outputs require equal inputs: A = B. So you set the arguments equal and solve. For log₃(2x + 1) = log₃(x + 4), you get 2x + 1 = x + 4, giving x = 3.

When an equation has multiple log terms, your first move should always be to **condense** them into a single log using log properties. The key properties are: log_b(MN) = log_b(M) + log_b(N), log_b(M/N) = log_b(M) − log_b(N), and log_b(M^r) = r·log_b(M). For example, to solve log₂(x) + log₂(x − 2) = 3, first condense the left side: log₂(x(x−2)) = 3, then convert: 2³ = x(x−2), giving 8 = x² − 2x, or x² − 2x − 8 = 0, so (x−4)(x+2) = 0, producing x = 4 and x = −2.

Here is where the domain check becomes critical. The argument of any logarithm must be **strictly positive** — log of zero or a negative number is undefined. Plug both candidates back into the original equation: if x = 4, the arguments x = 4 and x−2 = 2 are both positive, so x = 4 is valid. If x = −2, the argument x = −2 is negative, so x = −2 is **extraneous** — rejected. The algebra produced it, but it is not a solution to the original equation. Always check every candidate answer against the domain conditions in the original problem; extraneous solutions arise precisely because squaring or combining logs can obscure domain restrictions.
