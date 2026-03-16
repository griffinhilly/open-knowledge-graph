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
status: draft
---

# Substitution and Instantiation in Predicate Logic

## Core Idea
Substitution replaces variables with terms; instantiation substitutes a variable with a constant. Key rule: from ∀x φ(x), we can derive φ(t) for any term t. Capture-avoiding substitution prevents free variables of the substituted term from becoming unintentionally bound.

## Explainer

You already understand the distinction between free and bound variables: a free variable is a placeholder waiting to be given a value; a bound variable is one controlled by a quantifier (∀ or ∃) within the formula. **Substitution** is the operation of replacing a free variable with a specific term — a constant, another variable, or a complex expression built from function symbols. The notation φ[t/x] (or φ(t)) means: take the formula φ, and replace every free occurrence of x with the term t. Substitution is the mechanism by which general statements are applied to specific cases.

The most important inference rule that uses substitution is **universal instantiation**: from ∀x φ(x), derive φ(t) for any term t. In English: if a property holds for every element, it holds for this particular element. For example, from the axiom ∀x (x + 0 = x), we can instantiate with t = 5 to get 5 + 0 = 5, or with t = (a + b) to get (a + b) + 0 = (a + b). The substituted term can be anything in the domain — a numeral, a variable, or a complex expression. This rule is the engine of mathematical reasoning: universal statements about all numbers, all sets, or all functions become usable facts about specific objects by instantiation.

The complication is **variable capture**, and it is the main subtlety in substitution. Suppose φ(x) is the formula ∃y (y > x), meaning "there exists something larger than x." Now try substituting t = y for x, giving φ(y) = ∃y (y > y). This is a disaster: the free variable y in the term t has been accidentally captured by the quantifier ∃y in the formula, and the resulting formula says "there exists something larger than itself," which is false in any standard order. We have changed the meaning.

**Capture-avoiding substitution** prevents this by renaming bound variables whenever a conflict arises. Before substituting y for x in ∃y (y > x), we first rename the bound variable: ∃z (z > x), and then substitute to get ∃z (z > y). This is the correct result — "there exists something larger than y." The renaming step is called **alpha-renaming** (by analogy with lambda calculus, where it is central). The rule is: a substitution φ[t/x] is safe as long as no free variable of t is bound in φ; if it is, rename the offending bound variable first. Mechanically implementing this correctly is essential for proof assistants, logic programming, and compilers — anywhere formal terms must be manipulated symbolically without corrupting meaning.
