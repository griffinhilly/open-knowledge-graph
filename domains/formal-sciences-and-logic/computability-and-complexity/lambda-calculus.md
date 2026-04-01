---
id: lambda-calculus
title: Lambda Calculus
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: first-order-logic-syntax
  type: soft
- id: injective-surjective-bijective
  type: soft
- id: propositional-syntax
  type: soft
- id: functions-and-function-properties
  type: soft
- id: composition-of-functions
  type: soft
- id: function-composition-and-inverses
  type: hard
- id: set-fundamentals
  type: soft
- id: functions-and-mappings-formal
  type: soft
- id: composition-of-functions-sets
  type: soft
- id: function-composition-and-inverses
  type: soft
builds-toward:
- church-turing-thesis-formal
- general-recursive-functions
tags:
- computation
- functional-programming
- models-of-computation
- rewriting-systems
stage: formal-systems
status: validated
---

# Lambda Calculus

## Core Idea
Lambda calculus is a formal system for expressing computation through function abstraction and application. The syntax is minimal: variables, lambda abstractions (λx.M), and applications (M N). Computation proceeds via β-reduction: replacing formal parameters with actual arguments. Despite its simplicity, lambda calculus is Turing-complete and captures all computable functions, making it the theoretical foundation of functional programming languages.

## How It's Best Learned
Practice β-reduction step by step on concrete lambda terms before studying Church encodings of booleans, natural numbers, and recursion. Understanding the Y combinator (fixed-point combinator) is a key milestone that illustrates how recursion emerges from pure function application.

## Common Misconceptions
- Lambda calculus has no built-in numbers, booleans, or data structures — these must be encoded as functions (Church encodings).
- α-equivalence means λx.x and λy.y are the same term; variable names carry no meaning beyond scope.

## Questions

```yaml
- question: "What is the result of one step of β-reduction applied to (λx. λy. x) z?"
  type: multiple-choice
  options: ["λy. z", "λx. z", "z", "λz. z"]
  answer: 0
  explanation: "β-reduction substitutes the argument z for every free occurrence of x in the body λy. x, yielding λy. z. The outer lambda abstraction is consumed by the application, but the inner abstraction λy remains because only one argument is being applied. The variable y is bound in the result and x no longer appears."

- question: "In lambda calculus, the number 3 is a built-in constant, just as it is in most programming languages."
  type: true-false
  answer: false
  explanation: "Lambda calculus has no built-in data types — no numbers, booleans, pairs, or lists. Natural numbers must be encoded as functions. The Church numeral for 3 is λf. λx. f (f (f x)), representing 'apply f three times to x.' This encoding shows that all of computation can emerge from pure function abstraction and application, with no primitive constants required."

- question: "What is β-reduction, and in what sense does it model computation?"
  type: short-answer
  answer: "β-reduction is the rule (λx.M) N → M[x := N]: applying a lambda abstraction to an argument substitutes that argument for every free occurrence of the bound variable in the body. It models computation because each reduction step corresponds to one unit of work — evaluating a function call. A sequence of β-reductions transforms a lambda term until no further reductions are possible (normal form), representing the final computed value."
  explanation: "This single rewrite rule is the entire computational engine of lambda calculus. All of arithmetic, logic, and recursion are encoded so that evaluating them reduces to repeated application of β-reduction. Turing-completeness means every computable function can be expressed as a lambda term that β-reduces to the correct output — demonstrating that function application alone is sufficient for all of computation."
```

## Explainer

Lambda calculus strips computation down to its absolute minimum: variables, function definitions, and function application. A lambda abstraction λx.M defines an anonymous function with parameter x and body M. An application (M N) calls function M with argument N. That is the entire syntax — no numbers, no loops, no built-in operations. Yet from this, everything computable can be expressed.

The one rule that drives all computation is β-reduction: (λx.M) N → M[x := N]. When you apply a function to an argument, you substitute the argument for the parameter throughout the body. For example, (λx. x + 1) 5 reduces to 5 + 1. But because lambda calculus has no built-in "+" or numbers, even this must be encoded. Natural numbers are represented as Church numerals: the number n is the function that applies its argument f exactly n times to a starting value x. So 3 = λf. λx. f (f (f x)) — not a constant, but a function that captures the *act* of applying something three times.

This encoding might seem artificial, but it demonstrates something profound: data and functions are not fundamentally different things. Booleans, pairs, lists, and even recursion can all be encoded as lambda terms. The famous Y combinator — Y = λf. (λx. f (x x)) (λx. f (x x)) — implements general recursion from pure function application, with no special "recursion" primitive needed. When you call Y applied to a function, the result applies that function to itself indefinitely, enabling loops.

Alpha-equivalence (α-equivalence) says that λx.x and λy.y are the same term — variable names are just placeholders, not meaningful identifiers. This means you must be careful when substituting: if the body M contains a free variable y and you substitute N containing y for x, you must rename the bound y first to avoid "capturing" the free variable. This renaming is called α-conversion, and managing it carefully is essential to correct implementation of β-reduction.

Lambda calculus is Turing-complete, meaning every computation a Turing machine can perform can also be expressed as a lambda term that reduces to the correct answer. This is the theoretical foundation of functional programming: languages like Haskell, ML, and Scheme are, at their core, elaborated lambda calculi with syntactic sugar and type systems layered on top. Understanding lambda calculus gives you the deepest possible insight into what a function is and why function application is computationally universal.
