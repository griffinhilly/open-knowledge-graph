---
id: composition-of-functions
title: Composition of Functions
domain: mathematics
course: algebra-2
prerequisites:
- id: function-notation-review
  type: hard
- id: step-functions
  type: soft
builds-toward:
- inverse-functions
- chain-rule
tags:
- functions
- composition
- substitution
stage: formal-systems
status: validated
---
# Composition of Functions

## Core Idea
The composition of f and g, written (f o g)(x) = f(g(x)), means applying g first, then applying f to the result. Composition is not commutative: f(g(x)) is generally different from g(f(x)). The domain of f o g is all x in the domain of g such that g(x) is in the domain of f. Composition is the foundation for understanding inverse functions, the chain rule in calculus, and function decomposition.

## How It's Best Learned
Start by evaluating compositions at specific values: if f(x) = x^2 and g(x) = x+1, find f(g(3)) step by step. Then find the composition formula f(g(x)). Practice both f(g(x)) and g(f(x)) to demonstrate non-commutativity. Discuss domain restrictions. Decompose complex functions into compositions of simpler ones.

## Common Misconceptions
- Thinking f(g(x)) = f(x) * g(x) (composition is not multiplication).
- Assuming f(g(x)) = g(f(x)) (composition is not commutative).
- Applying the functions in the wrong order (in f(g(x)), g is applied first).
- Not considering domain restrictions on the composition.

## Questions

```yaml
- question: "Let f(x) = 2x + 1 and g(x) = x². What is f(g(3))?"
  type: multiple-choice
  options: ["7", "19", "49", "37"]
  answer: 1
  explanation: "Apply g first: g(3) = 3² = 9. Then apply f to that result: f(9) = 2(9) + 1 = 19. A common error is applying f first: f(3) = 7, then g(7) = 49 — that computes g(f(3)), not f(g(3)). The order the functions are written in the notation tells you which to apply first (innermost first)."

- question: "For any two functions f and g, f(g(x)) always equals g(f(x))."
  type: true-false
  answer: false
  explanation: "Composition is not commutative in general. Using the same f(x) = 2x + 1 and g(x) = x²: f(g(x)) = 2x² + 1, but g(f(x)) = (2x+1)² = 4x² + 4x + 1 — clearly different expressions. There are special cases where they are equal (e.g., inverse functions), but this is not true in general."

- question: "In the expression f(g(x)), which function is applied first, and how does the notation signal this?"
  type: short-answer
  answer: "g is applied first. The notation signals this because g(x) is the input to f — it sits inside the parentheses of f. You always evaluate from the inside out."
  explanation: "Reading f(g(x)) literally: 'f applied to g(x).' To compute f of something, you first need to know what that something is — so you must evaluate g(x) before you can evaluate f. Inside-out evaluation is the key principle of function composition."
```

## Explainer

Function notation like f(x) means "apply rule f to input x and get an output." Composition of functions takes this one step further: the output of one function becomes the input of another. When you write f(g(x)), you are chaining two rules together — g processes x first, then f processes whatever g produced.

A concrete example makes this tangible. Let g(x) = x + 1 (add one) and f(x) = x² (square). Then f(g(3)) means: first apply g to 3 — you get 4 — then apply f to 4 — you get 16. The notation tells you the order: the innermost function goes first. Always work from inside out. If you applied f first you would get f(3) = 9, then g(9) = 10, which is g(f(3)) — an entirely different computation.

This non-commutativity — f(g(x)) ≠ g(f(x)) in general — is the most important property to internalize. In arithmetic, 3 + 4 = 4 + 3 and 3 × 4 = 4 × 3. Function composition breaks this symmetry. Think of it like getting dressed: socks then shoes gives a very different result from shoes then socks, even though the individual steps are the same.

To find the composed formula f(g(x)) in general, substitute the entire expression for g(x) wherever x appears in f. With f(x) = 2x + 1 and g(x) = x², write f(g(x)) = 2(x²) + 1 = 2x² + 1. Notice that f(x) · g(x) = (2x+1)(x²) = 2x³ + x² — a completely different expression. Composition is substitution, not multiplication.

Composition is the hidden structure inside many formulas you will encounter. In calculus, the chain rule exists precisely to differentiate composed functions. When you see a complex expression like sin(x²) or e^(3x+1), you are looking at a composition — one function wrapped inside another. Learning to decompose and recompose functions is a foundational skill for everything that follows.
