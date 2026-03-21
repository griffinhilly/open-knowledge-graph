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
stage: formal-systems
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

## Questions

```yaml
- question: "To solve 5^x = 13, a student writes: '5x = 13, so x = 13/5 = 2.6.' What error did this student make?"
  type: multiple-choice
  options:
    - "The student should have used natural log instead of common log"
    - "The student incorrectly treated the exponent as multiplied by the base, skipping the logarithm step"
    - "The student forgot to verify that 13 is positive before taking a logarithm"
    - "The equation has no solution because 13 is not a power of 5"
  answer: 1
  explanation: "The power rule for logarithms states log(b^x) = x·log(b), but this only applies AFTER taking the logarithm of both sides. You cannot bring down the exponent directly. The correct approach: log(5^x) = log(13) → x·log(5) = log(13) → x = log(13)/log(5) ≈ 1.594. The student's answer of 2.6 treats the equation as if it were 5·x = 13, which completely ignores what it means for a variable to be in an exponent."

- question: "Which equation is solved MOST EFFICIENTLY using the common base method (rewriting both sides as powers of the same base)?"
  type: multiple-choice
  options:
    - "7^x = 50"
    - "3^x = 15"
    - "4^x = 32"
    - "2^x = 10"
  answer: 2
  explanation: "4^x = 32 can be rewritten as 2^(2x) = 2^5, so 2x = 5 and x = 5/2. Both sides are expressible as powers of 2. The other equations have no convenient common base (7, 50, 3, 15, 10 don't simplify to powers of the same base with small integers), so they require the logarithm strategy. Recognizing when common base is possible saves work and gives exact answers."

- question: "You can simplify log(2^x + 5) as x·log(2) + log(5) using logarithm properties."
  type: true-false
  answer: false
  explanation: "Log properties apply to products, quotients, and powers — not sums. log(A + B) ≠ log(A) + log(B), and there is no property that distributes log across addition. The power rule log(A^n) = n·log(A) requires the entire argument to be raised to a power, not added to something else. The expression log(2^x + 5) cannot be simplified with standard log properties, and trying to do so is one of the most common errors when solving exponential equations."

- question: "When solving an exponential equation by taking the logarithm of both sides, it does not matter which logarithm base you use — you will get the same numerical answer."
  type: true-false
  answer: true
  explanation: "The change-of-base formula guarantees this: log_a(x)/log_a(b) = log_c(x)/log_c(b) for any valid bases a and c. For example, x = log(20)/log(3) = ln(20)/ln(3) = log₂(20)/log₂(3) ≈ 2.727 in all cases. The choice between log₁₀ and ln is one of computational convenience, not correctness. For equations with base e (like e^x = k), using ln is most convenient since ln(e^x) = x exactly."

- question: "Explain why taking the logarithm of both sides is the key step that allows you to solve 3^x = 20, and what logarithm property makes this work."
  type: short-answer
  answer: "Taking the logarithm of both sides converts an equation where the variable is trapped in an exponent into one where the variable is a coefficient you can isolate algebraically. The power rule for logarithms — log(b^x) = x·log(b) — moves the exponent down as a multiplier, but only after the log is applied: log(3^x) = log(20) → x·log(3) = log(20) → x = log(20)/log(3). This works because logarithm and exponential are inverse operations — applying log undoes the exponential the same way division undoes multiplication."
  explanation: "The key is sequencing: you cannot apply the power rule to bring down the exponent until after you have taken the logarithm of both sides. Students who skip this step treat 3^x as if it were 3·x. Once the log is applied, the power rule transforms the equation from exponential to linear, and basic algebra handles the rest."
```

## Explainer

Solving an exponential equation means finding the value of a variable that appears in an exponent. You already know from your work with exponential functions that the graph of y = bˣ is one-to-one — it passes the horizontal line test — so each output corresponds to exactly one input. That one-to-one property is what guarantees exponential equations have unique solutions and is what both solution strategies exploit.

The **common base strategy** works when both sides of the equation can be written as powers of the same base. For example, 4ˣ = 32 becomes 2²ˣ = 2⁵, so 2x = 5 and x = 5/2. This works because if bᵐ = bⁿ and b ≠ 1, then m = n — identical outputs from the same one-to-one function mean identical inputs. The skill is rewriting numbers as powers: 4 = 2², 8 = 2³, 27 = 3³, 1/9 = 3⁻², and so on. When you can do this, you reduce the exponential equation to a linear or polynomial equation.

The **logarithm strategy** handles the cases where a common base isn't obvious — which is most real-world cases. The equation 3ˣ = 20 has no convenient common base, so you apply log to both sides: log(3ˣ) = log(20). Using the power rule for logarithms (which you know: logₐ(mⁿ) = n·logₐ(m)), this becomes x·log(3) = log(20), so x = log(20)/log(3) ≈ 2.727. The power rule is what allows you to bring the exponent down as a coefficient — but only after taking the logarithm, never before. The logarithm "undoes" the exponential the same way division undoes multiplication: they are inverse operations.

A practical guide: for equations with base e, use the natural logarithm (ln) because ln(eˣ) = x exactly. For all other bases, any logarithm works (the ratio log(b)/log(a) is the same regardless of which log base you use), but base-10 log or ln are the most convenient. The biggest trap is misapplying log properties to sums: log(2ˣ + 5) is not x·log(2) + log(5). Log properties only simplify products, quotients, and powers — not sums. If you see a sum inside a logarithm, or a sum of exponential terms, the expression usually requires a substitution or a different approach entirely.
