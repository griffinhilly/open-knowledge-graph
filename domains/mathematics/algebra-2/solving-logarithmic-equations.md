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

## Explainer

Solving logarithmic equations rests on two ideas you already know: the definition of a logarithm as the inverse of exponentiation, and the log properties that let you combine or split logarithmic expressions. The definition says log_b(A) = c means exactly b^c = A — the log asks "what exponent on b gives A?" That relationship is the key to unlocking equations where the unknown is inside a logarithm.

There are two main situations. In the first, you have a single log equal to a number: log_b(expression) = c. Here you simply convert to exponential form — b^c = expression — and solve the resulting algebraic equation. For example, log₂(x + 3) = 4 becomes 2⁴ = x + 3, so x = 13. In the second situation, you have logs on both sides with the same base: log_b(A) = log_b(B). Since the log function is one-to-one (each output corresponds to exactly one input), equal outputs require equal inputs: A = B. So you set the arguments equal and solve. For log₃(2x + 1) = log₃(x + 4), you get 2x + 1 = x + 4, giving x = 3.

When an equation has multiple log terms, your first move should always be to **condense** them into a single log using log properties. The key properties are: log_b(MN) = log_b(M) + log_b(N), log_b(M/N) = log_b(M) − log_b(N), and log_b(M^r) = r·log_b(M). For example, to solve log₂(x) + log₂(x − 2) = 3, first condense the left side: log₂(x(x−2)) = 3, then convert: 2³ = x(x−2), giving 8 = x² − 2x, or x² − 2x − 8 = 0, so (x−4)(x+2) = 0, producing x = 4 and x = −2.

Here is where the domain check becomes critical. The argument of any logarithm must be **strictly positive** — log of zero or a negative number is undefined. Plug both candidates back into the original equation: if x = 4, the arguments x = 4 and x−2 = 2 are both positive, so x = 4 is valid. If x = −2, the argument x = −2 is negative, so x = −2 is **extraneous** — rejected. The algebra produced it, but it is not a solution to the original equation. Always check every candidate answer against the domain conditions in the original problem; extraneous solutions arise precisely because squaring or combining logs can obscure domain restrictions.
