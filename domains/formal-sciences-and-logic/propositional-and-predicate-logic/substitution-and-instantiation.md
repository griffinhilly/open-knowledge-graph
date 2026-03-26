---
id: substitution-and-instantiation
title: Substitution and Instantiation in Predicate Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: free-variables-and-bound-variables
  type: hard
builds-toward:
- natural-deduction-fol
- skolem-functions-and-witnesses
tags:
- syntax
- inference
- first-order-logic
stage: formal-systems
status: validated
---

# Substitution and Instantiation in Predicate Logic

## Core Idea
Substitution replaces variables with terms; instantiation substitutes a variable with a constant. Key rule: from ∀x φ(x), we can derive φ(t) for any term t. Capture-avoiding substitution prevents free variables of the substituted term from becoming unintentionally bound.

## Questions

```yaml
- question: "We want to substitute y for x in the formula ∃y (y > x), writing φ[y/x]. Naive substitution produces ∃y (y > y). What went wrong?"
  type: multiple-choice
  options:
    - "Only constants may be substituted for variables — substituting a variable for a variable is always invalid"
    - "The free variable y in the substituted term was captured by the quantifier ∃y in the formula, producing a formula with a completely different meaning"
    - "Universal instantiation applies only to ∀, so this substitution requires a different rule"
    - "The substitution is valid — ∃y (y > y) is logically equivalent to ∃y (y > x)"
  answer: 1
  explanation: "The free variable y we tried to introduce got 'captured' by the existing quantifier ∃y, which now binds it. The original formula ∃y (y > x) means 'something is larger than x' — true for most x. After naive substitution, ∃y (y > y) means 'something is larger than itself' — false in any standard order. The meaning changed entirely. The fix is alpha-renaming: first rename the bound variable to z, giving ∃z (z > x), then substitute to get ∃z (z > y), which correctly means 'something is larger than y.'"

- question: "From ∀x P(x), which of the following instantiations are valid under universal instantiation?"
  type: multiple-choice
  options:
    - "Only P(a) for a specific constant a — universal instantiation works only for constants"
    - "Only P(x) — reinstantiating the same variable is the safe choice"
    - "P(a) or P(b) for constants, but not P(f(a,b)) for complex terms"
    - "P(t) for any term t in the domain — constants, variables, or complex function expressions"
  answer: 3
  explanation: "Universal instantiation says: from ∀x φ(x), derive φ(t) for ANY term t — a numeral, a variable, a function applied to other terms, anything in the domain. From ∀x (x + 0 = x) you can derive 5 + 0 = 5, or y + 0 = y, or (a + b) + 0 = (a + b). The power of universal statements is precisely that they license instantiation with arbitrarily complex terms. The only constraint is capture-avoidance: if t contains free variables, make sure those variables are not bound in φ."

- question: "Capture-avoiding substitution is only necessary when the substituted term is a variable; substituting a constant never causes variable capture."
  type: true-false
  answer: true
  explanation: "Variable capture occurs when a free variable in the substituted term t gets bound by a quantifier in the target formula. Constants have no free variables — there is nothing to capture. If t = 5 or t = a (a constant), substituting it for x in any formula is always safe; no quantifier can bind a constant. Capture is exclusively a problem when t contains free variables that could be 'swallowed' by a quantifier in the formula."

- question: "The formula φ[t/x] usually has the same logical meaning as φ, just with t appearing where x was."
  type: true-false
  answer: false
  explanation: "This is only true for capture-avoiding substitution. Naive substitution can radically change meaning through variable capture, as in ∃y (y > x)[y/x] = ∃y (y > y), which changes 'something is greater than x' (often true) to 'something is greater than itself' (always false). Capture-avoiding substitution — with alpha-renaming when needed — preserves meaning. The claim that substitution always preserves meaning confuses a correct procedure with its naive (and incorrect) version."

- question: "What is 'variable capture' in predicate logic substitution, and how does capture-avoiding substitution prevent it? Use an example."
  type: short-answer
  answer: "Variable capture occurs when a free variable in the term being substituted accidentally becomes bound by a quantifier in the target formula, changing the formula's meaning. Example: substituting y for x in ∃y (y > x) naively gives ∃y (y > y) — the y we introduced is now bound by ∃y. Capture-avoiding substitution prevents this by alpha-renaming the offending bound variable before substituting: first rename bound y to z, giving ∃z (z > x), then substitute to get ∃z (z > y), which preserves the intended meaning."
  explanation: "The key insight is that bound variable names are arbitrary — ∃y (y > x) and ∃z (z > x) are logically identical (alpha-equivalent). Alpha-renaming exploits this: we can always rename a bound variable to one that does not appear free in the term we are substituting, making the substitution safe. This is not just a theoretical nicety — proof assistants, compilers, and logic programming systems must implement capture-avoiding substitution correctly or risk silently producing wrong results."
```

## Explainer

You already understand the distinction between free and bound variables: a free variable is a placeholder waiting to be given a value; a bound variable is one controlled by a quantifier (∀ or ∃) within the formula. **Substitution** is the operation of replacing a free variable with a specific term — a constant, another variable, or a complex expression built from function symbols. The notation φ[t/x] (or φ(t)) means: take the formula φ, and replace every free occurrence of x with the term t. Substitution is the mechanism by which general statements are applied to specific cases.

The most important inference rule that uses substitution is **universal instantiation**: from ∀x φ(x), derive φ(t) for any term t. In English: if a property holds for every element, it holds for this particular element. For example, from the axiom ∀x (x + 0 = x), we can instantiate with t = 5 to get 5 + 0 = 5, or with t = (a + b) to get (a + b) + 0 = (a + b). The substituted term can be anything in the domain — a numeral, a variable, or a complex expression. This rule is the engine of mathematical reasoning: universal statements about all numbers, all sets, or all functions become usable facts about specific objects by instantiation.

The complication is **variable capture**, and it is the main subtlety in substitution. Suppose φ(x) is the formula ∃y (y > x), meaning "there exists something larger than x." Now try substituting t = y for x, giving φ(y) = ∃y (y > y). This is a disaster: the free variable y in the term t has been accidentally captured by the quantifier ∃y in the formula, and the resulting formula says "there exists something larger than itself," which is false in any standard order. We have changed the meaning.

**Capture-avoiding substitution** prevents this by renaming bound variables whenever a conflict arises. Before substituting y for x in ∃y (y > x), we first rename the bound variable: ∃z (z > x), and then substitute to get ∃z (z > y). This is the correct result — "there exists something larger than y." The renaming step is called **alpha-renaming** (by analogy with lambda calculus, where it is central). The rule is: a substitution φ[t/x] is safe as long as no free variable of t is bound in φ; if it is, rename the offending bound variable first. Mechanically implementing this correctly is essential for proof assistants, logic programming, and compilers — anywhere formal terms must be manipulated symbolically without corrupting meaning.
