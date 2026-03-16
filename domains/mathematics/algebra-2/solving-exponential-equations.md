---
id: solving-exponential-equations
title: Solving Exponential Equations
domain: mathematics
course: algebra-2
prerequisites:
- id: logarithm-properties
  type: hard
- id: exponential-functions-and-graphs
  type: hard
- id: exponential-growth-and-decay
  type: soft
builds-toward:
- natural-logarithm-and-e
tags:
- exponential
- equations
- logarithms
- solving
stage: abstract-reasoning
status: validated
---
# Solving Exponential Equations

## Core Idea
Exponential equations have the variable in the exponent. Two main strategies: (1) If both sides can be written with the same base, set exponents equal (e.g., 2^x = 8 becomes 2^x = 2^3, so x = 3). (2) If not, take the logarithm of both sides and use log properties to isolate the variable (e.g., 3^x = 20 becomes x = log(20)/log(3)). Strategy 2 is the general method and works for all cases.

## How It's Best Learned
Start with equations solvable by rewriting with a common base. Then introduce the "take log of both sides" technique for equations that cannot be simplified to a common base. Practice with various bases including e. Apply to real-world problems (population doubling time, radioactive decay half-life).

## Common Misconceptions
- Trying to "bring down" the exponent without taking a logarithm first.
- Distributing log across addition: log(2^x + 5) != x*log(2) + log(5).
- Forgetting that log(both sides) requires both sides to be positive.
- Confusing e^x = 5 (take ln of both sides) with ln(x) = 5 (exponentiate both sides).

## Explainer

Solving an exponential equation means finding the value of a variable that appears in an exponent. You already know from your work with exponential functions that the graph of y = bˣ is one-to-one — it passes the horizontal line test — so each output corresponds to exactly one input. That one-to-one property is what guarantees exponential equations have unique solutions and is what both solution strategies exploit.

The **common base strategy** works when both sides of the equation can be written as powers of the same base. For example, 4ˣ = 32 becomes 2²ˣ = 2⁵, so 2x = 5 and x = 5/2. This works because if bᵐ = bⁿ and b ≠ 1, then m = n — identical outputs from the same one-to-one function mean identical inputs. The skill is rewriting numbers as powers: 4 = 2², 8 = 2³, 27 = 3³, 1/9 = 3⁻², and so on. When you can do this, you reduce the exponential equation to a linear or polynomial equation.

The **logarithm strategy** handles the cases where a common base isn't obvious — which is most real-world cases. The equation 3ˣ = 20 has no convenient common base, so you apply log to both sides: log(3ˣ) = log(20). Using the power rule for logarithms (which you know: logₐ(mⁿ) = n·logₐ(m)), this becomes x·log(3) = log(20), so x = log(20)/log(3) ≈ 2.727. The power rule is what allows you to bring the exponent down as a coefficient — but only after taking the logarithm, never before. The logarithm "undoes" the exponential the same way division undoes multiplication: they are inverse operations.

A practical guide: for equations with base e, use the natural logarithm (ln) because ln(eˣ) = x exactly. For all other bases, any logarithm works (the ratio log(b)/log(a) is the same regardless of which log base you use), but base-10 log or ln are the most convenient. The biggest trap is misapplying log properties to sums: log(2ˣ + 5) is not x·log(2) + log(5). Log properties only simplify products, quotients, and powers — not sums. If you see a sum inside a logarithm, or a sum of exponential terms, the expression usually requires a substitution or a different approach entirely.
