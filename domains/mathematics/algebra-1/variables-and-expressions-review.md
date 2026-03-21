---
id: variables-and-expressions-review
title: Variables and Expressions Review
domain: mathematics
course: algebra-1
prerequisites:
  - id: variable-expressions
    type: hard
  - id: combining-like-terms
    type: hard
  - id: distributive-property
    type: hard
builds-toward:
  - solving-multi-step-equations
  - literal-equations
tags: [variables, expressions, review, algebra-foundations]
stage: abstract-reasoning
status: validated
---

# Variables and Expressions Review

## Core Idea
This topic consolidates prealgebra skills with variables: evaluating expressions by substitution, simplifying by combining like terms, and applying the distributive property. In algebra 1, these skills must be automatic because they are used in nearly every subsequent topic — from solving equations to manipulating polynomials. Students should be fluent with multi-variable expressions, nested parentheses, and expressions involving rational numbers. This review also formalizes the distinction between expressions (no equals sign, cannot be "solved") and equations (has an equals sign, can be solved for a variable).

## How It's Best Learned
Use a diagnostic assessment to identify gaps from prealgebra. Practice problems that combine multiple skills: distribute, then combine like terms, then evaluate for given variable values. Emphasize that simplification means writing an equivalent expression with fewer terms. Include expressions with fractions and negative coefficients.

## Common Misconceptions
- Thinking you can "solve" an expression (expressions are simplified, not solved).
- Distributing incorrectly with negative signs outside parentheses.
- Treating different variables as like terms (3x + 2y cannot be simplified further).

## Questions

```yaml
- question: "A student is given the expression 3x + 2y − x + 5 and told to 'solve for x.' What is the fundamental problem with this instruction?"
  type: multiple-choice
  options:
    - "There is no problem — the student should isolate x on one side of the expression"
    - "The problem has no solution because there are two variables, which is not allowed in Algebra 1"
    - "'Solving' does not apply to expressions — expressions are simplified, not solved; solving requires an equation with an equals sign"
    - "The student must first apply the distributive property before any other steps"
  answer: 2
  explanation: "This is the core distinction: expressions are simplified (rewritten in equivalent form with fewer terms), while equations are solved (a value of the variable is found that makes both sides equal). An expression like 3x + 2y − x + 5 has no equals sign, so it cannot be 'solved.' It can be simplified to 2x + 2y + 5. The right action depends entirely on which type of mathematical object you're working with."

- question: "A student simplifies 4x + 3y − x and writes 6xy as the answer. Which error did they make?"
  type: multiple-choice
  options:
    - "They forgot to apply the distributive property before combining terms"
    - "They treated 4x and 3y as like terms and combined them — but unlike terms cannot be combined"
    - "They applied the wrong order of operations, adding before subtracting"
    - "They dropped the negative sign when subtracting the final x term"
  answer: 1
  explanation: "Like terms must have identical variable parts — same variables, same exponents. The terms 4x and 3y have different variables (x vs. y), so they are unlike terms and cannot be combined. The correct simplification is 4x − x + 3y = 3x + 3y. Writing 6xy confuses addition (which preserves the variable parts) with multiplication (which would produce xy). This is one of the most persistent errors in early algebra."

- question: "The expression 5a − 3b + 2a can be correctly simplified to 7a − 3b."
  type: true-false
  answer: true
  explanation: "5a and 2a are like terms — they share the same variable (a) with the same exponent (1). Combining them: 5a + 2a = 7a. The term −3b has a different variable and cannot be combined with the a-terms. The simplified form is 7a − 3b. This is a straightforward application of combining like terms."

- question: "Distributing the negative sign in −(2x − 4) gives −2x − 4."
  type: true-false
  answer: false
  explanation: "The negative multiplies every term inside the parentheses. −(2x − 4) = −1 · 2x + (−1) · (−4) = −2x + 4. The second term's sign flips because negative times negative equals positive. Writing −2x − 4 is the most common error when distributing negatives. The correct result is −2x + 4."

- question: "Why can't you 'solve' the expression 3x + 7? What operation applies to it instead, and what additional information would you need to find a specific numerical value for x?"
  type: short-answer
  answer: "An expression has no equals sign, so there is no constraint pinning down the value of x. You can simplify an expression — rewrite it in a cleaner or shorter equivalent form — but 'solving' requires an equation. To find a specific value for x, you would need either an equation (e.g., 3x + 7 = 22, which you can solve to get x = 5) or a specific value to substitute for x (e.g., if x = 4, then 3(4) + 7 = 19)."
  explanation: "The expression vs. equation distinction determines which algebraic operations are even meaningful. Confusing them leads to nonsense: 'solving' an expression, or trying to 'simplify' an equation without maintaining the equality. Every algebra problem starts with identifying what you have — expression or equation — because that determines what you do with it."
```

## Explainer

An **expression** is a mathematical phrase built from numbers, variables, and operations — but with no equals sign. It has a value (which may depend on the variables), but it cannot be "solved." The right word is **simplified**: rewriting it in an equivalent form with fewer terms or a cleaner structure. Contrast this with an **equation**, which has an equals sign and can be solved for a variable. This distinction matters every time you encounter a new problem: your first move is always to ask, "Is this an expression to simplify, or an equation to solve?"

You already know the two main simplification tools. **Combining like terms** groups terms that have identical variable parts: 5x² − 2x + 3x² + 7 simplifies to 8x² − 2x + 7. The rule is strict — terms are "like" only if every variable and every exponent match exactly. So 3x and 3x² are not like terms, and 3x and 3y are not like terms. Only the coefficients (the numerical parts) change when you combine; the variable part stays the same. The **distributive property** lets you remove parentheses: 2(3x − 4) = 6x − 8, because 2 multiplies every term inside. The most common error is distributing a negative: −(3x − 4) = −3x + 4, not −3x − 4. The negative multiplies both terms, flipping the sign of each.

**Evaluation** means substituting specific numbers for variables and computing. If f = 3x² − 2x + 1 and x = −2, substitute: 3(−2)² − 2(−2) + 1 = 3(4) + 4 + 1 = 17. Two habits prevent errors: always write parentheses around substituted values (especially negatives), and follow order of operations carefully — exponents before multiplication before addition. Using parentheses around −2 before squaring ensures you compute 3 × 4, not (3)(−2)(2) = −12.

These skills need to be automatic because algebra 1 builds on them everywhere. Solving equations requires simplifying both sides before isolating the variable. Factoring polynomials requires recognizing patterns in expressions. Graphing functions requires evaluating them at many input values. The goal of this review is not the skills themselves but what they enable: once combining like terms and distributing feel effortless, cognitive attention is free to focus on new ideas rather than algebraic bookkeeping.
