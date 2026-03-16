---
id: variable-binding-and-scope
title: Variable Binding and Scope
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
builds-toward:
- substitution-and-unification
- quantifier-scope-ambiguity
tags:
- free-variables
- bound-variables
- scope
- quantifier-scope
- alpha-equivalence
stage: formal-systems
status: draft
---

# Variable Binding and Scope

## Core Idea
A quantifier (∀x or ∃x) binds every free occurrence of x within its scope — the subformula it governs. A variable occurrence is free if it is not bound by any quantifier, and bound if it falls within the scope of a matching quantifier. The same variable name can appear both free and bound in a single formula (e.g., P(x) ∧ ∀x Q(x)), which is legal but confusing. Alpha-equivalence says that renaming bound variables (∀x P(x) ≡ ∀y P(y)) does not change a formula's meaning, so bound variable names are arbitrary labels.

## How It's Best Learned
Mark every variable occurrence in a complex formula as free or bound, then draw scope brackets to visualize which quantifier governs which occurrences. Practice alpha-renaming to eliminate variable name clashes and confirm that meaning is preserved.

## Common Misconceptions
- A variable is not inherently free or bound — the same variable can have free and bound occurrences in the same formula.
- Renaming bound variables is always safe (alpha-equivalence), but renaming free variables changes the formula's meaning.
- The scope of a quantifier is determined by the syntactic structure (parentheses), not by proximity or left-to-right reading.

## Explainer

From your study of first-order logic syntax, you know that formulas are built from atomic formulas (like R(x, y) or x = y) using connectives (¬, ∧, ∨, →) and quantifiers (∀x, ∃x). Variables appear throughout these formulas, but not all variable occurrences play the same role. The distinction between **free** and **bound** occurrences is the most fundamental scoping concept in formal logic — and it mirrors the distinction between a free variable in a mathematical expression like f(x) = x + c (where c is a parameter) and a dummy variable in a sum like Σ_{i=1}^n i (where i is a placeholder).

A quantifier ∀x or ∃x **binds** the variable x within its **scope** — the subformula immediately following it (delimited by parentheses in the formal syntax). Every occurrence of x inside that scope is a **bound occurrence**, governed by this quantifier. An occurrence of x outside any such scope is a **free occurrence** — it is a parameter of the formula, a name for some element in the domain that must be supplied by context. A formula with free variables expresses a property (or relation) that depends on those variable values; a sentence (no free variables) expresses a statement that is true or false in a model outright.

The phrase "the same variable can appear free and bound in the same formula" is important and often surprising. In the formula P(x) ∧ ∀x Q(x), the first occurrence of x (in P(x)) is free, and the second (in Q(x)) is bound by the ∀x. These are technically different "slots" sharing a name. This is legal in the formal grammar but confusing to read — experienced logicians avoid this style by immediately renaming the bound variable. In practice: treat free and bound occurrences of the same name as if they were different variables that happen to share a label.

**Alpha-equivalence** captures the fact that the name of a bound variable is an implementation detail. ∀x P(x) and ∀y P(y) say exactly the same thing — "every element satisfies P" — regardless of what dummy variable is used. You can freely rename bound variables as long as you do so consistently within their scope and do not **capture** a free variable: ∀x ∃y (x ≠ y) cannot be renamed to ∀y ∃y (y ≠ y) because the outer ∀y would capture the free y from the original inner formula, completely changing the meaning. The rule is: rename a bound variable to a name that does not already appear free in the scope. This alpha-renaming discipline is essential for correct substitution, and substitution is the engine of proof rules like universal instantiation (from ∀x φ, infer φ[a/x]) and existential generalization.

