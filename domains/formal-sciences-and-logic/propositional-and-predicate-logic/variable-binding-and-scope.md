---
id: variable-binding-and-scope
title: Variable Binding and Scope
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: term-and-atom-fol
  type: soft
builds-toward:
  - substitution-and-unification
tags:
- free-variables
- bound-variables
- scope
- quantifier-scope
- alpha-equivalence
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "In the formula P(x) ∧ ∀x Q(x), what is the status of the two occurrences of x?"
  type: multiple-choice
  options:
    - "Both occurrences are bound — the ∀x quantifier applies to the entire conjunction"
    - "The x in P(x) is free; the x in Q(x) is bound by the ∀x quantifier"
    - "Both occurrences are free because the quantifier only takes effect after the ∧ connective"
    - "The x in P(x) is bound and the x in Q(x) is free — quantifiers bind leftward"
  answer: 1
  explanation: "The scope of ∀x is only the subformula immediately following it — Q(x). The x in P(x) comes before the quantifier and lies outside its scope, so it is a free occurrence. This formula legally has the same variable name appearing both free (in P(x)) and bound (in Q(x)). It is grammatically valid but stylistically poor — experienced logicians would immediately rename the bound variable to avoid confusion."

- question: "You want to rename the bound variable in ∀x ∃y (x ≠ y) to ∀y ∃y (y ≠ y). Why is this renaming problematic?"
  type: multiple-choice
  options:
    - "Alpha-renaming is never legal in first-order logic — bound variable names are fixed"
    - "The outer ∀y would capture the y that was formerly free in the inner formula, changing 'every x has a different element y' into a self-contradictory claim"
    - "Only existential quantifiers can be alpha-renamed; universal quantifiers bind their variables permanently"
    - "The renaming is fine logically, but stylistically y should be renamed to z to avoid reuse"
  answer: 1
  explanation: "Alpha-renaming is legal only when the new name does not appear free within the scope being renamed. In ∀x ∃y (x ≠ y), the variable y is already used (bound by ∃y). Renaming ∀x to ∀y creates ∀y ∃y (y ≠ y) — the outer ∀y captures the free positions of y in the original inner formula, turning a coherent statement about two different elements into a statement about self-inequality, which is always false. Variable capture completely changes the formula's meaning."

- question: "Alpha-equivalence means ∀x P(x) and ∀z P(z) express the same logical content — the name of a bound variable is an arbitrary label that can be changed without altering meaning, provided no free variable is captured."
  type: true-false
  answer: true
  explanation: "Bound variable names are implementation details. 'For all x, P(x)' and 'For all z, P(z)' make the same claim: every element in the domain satisfies P. The choice of dummy variable is arbitrary, like the choice of loop variable name in code. What matters is the structure of quantifier scope, not the specific labels. This is alpha-equivalence, and it's the theoretical basis for safe variable renaming during substitution."

- question: "In a first-order logic formula, a variable is either free throughout the entire formula or bound throughout — it cannot be simultaneously free in one part and bound in another."
  type: true-false
  answer: false
  explanation: "The same variable name can have both free and bound occurrences in the same formula. In P(x) ∧ ∀x Q(x), x appears free in P(x) and bound in Q(x). These are technically different 'slots' that happen to share a label. A variable occurrence is free or bound based on whether it falls within the scope of a matching quantifier — it is a property of each occurrence, not of the variable name as a whole."

- question: "Why must you check for 'variable capture' when alpha-renaming a bound variable, and what goes wrong if capture occurs?"
  type: short-answer
  answer: "Variable capture occurs when you rename a bound variable to a name that already appears free within the scope of the quantifier being renamed. The newly renamed quantifier then binds those formerly-free occurrences, which were independent variables in the original formula. For example, in ∀x ∃y (x ≠ y), renaming ∀x to ∀y produces ∀y ∃y (y ≠ y) — the outer ∀y inadvertently binds what were free y's in the inner formula, turning a statement about two different elements into a claim about self-inequality. Capture silently transforms the formula's meaning while appearing to be a harmless renaming."
  explanation: "This is why the alpha-renaming rule specifies: rename a bound variable only to a fresh name that doesn't appear free in the scope. The safety condition is not bureaucratic — capture is exactly the error that would make substitution rules (like universal instantiation) unsound if not carefully controlled."
```

## Explainer

From your study of first-order logic syntax, you know that formulas are built from atomic formulas (like R(x, y) or x = y) using connectives (¬, ∧, ∨, →) and quantifiers (∀x, ∃x). Variables appear throughout these formulas, but not all variable occurrences play the same role. The distinction between **free** and **bound** occurrences is the most fundamental scoping concept in formal logic — and it mirrors the distinction between a free variable in a mathematical expression like f(x) = x + c (where c is a parameter) and a dummy variable in a sum like Σ_{i=1}^n i (where i is a placeholder).

A quantifier ∀x or ∃x **binds** the variable x within its **scope** — the subformula immediately following it (delimited by parentheses in the formal syntax). Every occurrence of x inside that scope is a **bound occurrence**, governed by this quantifier. An occurrence of x outside any such scope is a **free occurrence** — it is a parameter of the formula, a name for some element in the domain that must be supplied by context. A formula with free variables expresses a property (or relation) that depends on those variable values; a sentence (no free variables) expresses a statement that is true or false in a model outright.

The phrase "the same variable can appear free and bound in the same formula" is important and often surprising. In the formula P(x) ∧ ∀x Q(x), the first occurrence of x (in P(x)) is free, and the second (in Q(x)) is bound by the ∀x. These are technically different "slots" sharing a name. This is legal in the formal grammar but confusing to read — experienced logicians avoid this style by immediately renaming the bound variable. In practice: treat free and bound occurrences of the same name as if they were different variables that happen to share a label.

**Alpha-equivalence** captures the fact that the name of a bound variable is an implementation detail. ∀x P(x) and ∀y P(y) say exactly the same thing — "every element satisfies P" — regardless of what dummy variable is used. You can freely rename bound variables as long as you do so consistently within their scope and do not **capture** a free variable: ∀x ∃y (x ≠ y) cannot be renamed to ∀y ∃y (y ≠ y) because the outer ∀y would capture the free y from the original inner formula, completely changing the meaning. The rule is: rename a bound variable to a name that does not already appear free in the scope. This alpha-renaming discipline is essential for correct substitution, and substitution is the engine of proof rules like universal instantiation (from ∀x φ, infer φ[a/x]) and existential generalization.

