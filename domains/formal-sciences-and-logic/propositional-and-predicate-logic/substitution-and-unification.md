---
id: substitution-and-unification
title: Substitution and Unification
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: term-and-atom-fol
  type: hard
builds-toward:
- resolution-fol
- natural-deduction-fol
tags:
- substitution
- unification
- most-general-unifier
- variable-capture
- automated-reasoning
stage: formal-systems
status: draft
---

# Substitution and Unification

## Core Idea
Substitution replaces free occurrences of a variable x in a formula with a term t, written φ[t/x]. The operation must be capture-avoiding: if t contains a variable y that would become bound in φ, the bound variable must first be renamed (alpha-conversion) to prevent the substituted variable from being inadvertently captured. Unification is the inverse problem — given two terms or atoms, find a substitution (called a unifier) that makes them syntactically identical. The most general unifier (MGU) is the least committal such substitution. Robinson's unification algorithm computes the MGU in near-linear time, and it is the engine behind resolution-based theorem proving and logic programming.

## How It's Best Learned
Perform substitutions by hand on formulas with nested quantifiers, deliberately encountering variable-capture problems and fixing them. Then unify pairs of atomic formulas step by step using Robinson's algorithm, building the MGU incrementally.

## Common Misconceptions
- Substitution only replaces free occurrences — bound occurrences of the same variable name are untouched.
- Variable capture is a real and common bug, not an edge case — failing to rename bound variables before substitution can silently change a formula's meaning.
- Not all pairs of terms are unifiable (e.g., f(x) and g(x) cannot unify if f ≠ g); unification can fail, and recognizing failure is part of the algorithm.

## Questions

```yaml
- question: "You try to substitute y for x in the formula ∃y (x = y), obtaining ∃y (y = y). What went wrong?"
  type: multiple-choice
  options:
    - "Nothing — substitution always replaces all variable occurrences and ∃y (y = y) is correct"
    - "Variable capture: the free y being substituted fell under the ∃y quantifier, changing the formula's meaning from 'there exists something equal to x' to 'something equals itself'"
    - "Substitution is not allowed inside quantifier scopes"
    - "The error is that x is bound in ∃y (x = y), so substitution cannot apply"
  answer: 1
  explanation: "This is the canonical variable capture bug. In ∃y (x = y), x is free (not under any quantifier for x) — so substitution of y for x is allowed. But the y being substituted happens to be the same name as the bound variable ∃y. Naively replacing x with y gives ∃y (y = y), which means 'something equals itself' — a tautology true of everything. The original formula means 'there is something equal to x' — a different, non-trivial claim. The fix is alpha-conversion: rename the bound variable first (∃z (x = z)), then substitute safely to get ∃z (y = z)."

- question: "What is the 'occurs check' in Robinson's unification algorithm, and why does failing to perform it cause problems?"
  type: multiple-choice
  options:
    - "It checks whether a term has already appeared in a previous unification step, to avoid redundant work"
    - "It prevents a variable x from being unified with a term t that contains x, which would require an infinite term to satisfy x = t"
    - "It verifies that function symbols match before recursing on subterms"
    - "It checks that both terms have the same number of arguments before attempting unification"
  answer: 1
  explanation: "The occurs check prevents extending the unifier with x ↦ t when x appears inside t. If you allowed x ↦ f(x), you'd need x to equal f(f(f(…))) — an infinite term. Standard first-order logic requires finite terms, so this unification must fail. Skipping the occurs check (as Prolog does for performance reasons) can lead to infinite loops or unsound inferences when cyclic bindings are created. The occurs check is the safeguard that keeps unification within well-formed finite terms."

- question: "Substitution φ[t/x] replaces all occurrences of the variable x in formula φ — including those that appear under quantifiers like ∀x or ∃x."
  type: true-false
  answer: false
  explanation: "Substitution replaces only FREE occurrences of x — those not bound by a quantifier. An occurrence of x under ∀x or ∃x is a bound occurrence and refers to a different, locally scoped variable that happens to share the name x. Substituting into a bound occurrence would change the quantifier's scope incorrectly. The notation φ[t/x] is defined to be capture-avoiding and to leave bound occurrences untouched. This is emphasized in the Common Misconceptions: 'Substitution only replaces free occurrences — bound occurrences of the same variable name are untouched.'"

- question: "The most general unifier (MGU) is the most specific substitution possible — it assigns concrete values to every variable to make the two terms identical."
  type: true-false
  answer: false
  explanation: "The MGU is the LEAST committal unifier, not the most specific. It makes only the minimum variable assignments required to achieve syntactic identity, leaving all other variables free. Any other unifier for the same pair of terms can be obtained by composing the MGU with a further substitution. Using a more specific unifier than the MGU forecloses future flexibility — in resolution theorem proving, this means committing to variable values prematurely and potentially blocking valid inferences. The 'most general' means least constrained, not most detailed."

- question: "Why is the most general unifier preferred over other unifiers in resolution theorem proving and logic programming?"
  type: short-answer
  answer: "The MGU is preferred because it makes the minimum commitments necessary to unify two terms, leaving all other variables free to be instantiated later. In resolution, each inference step unifies complementary literals and applies the resulting substitution to the entire clause — a substitution that assigns values to variables affects all future reasoning steps. Using a more specific unifier than necessary prematurely constrains variables that might need different values in subsequent steps, potentially blocking valid proofs. The MGU preserves maximum flexibility: any other unifier for the same terms is a special case of the MGU under further substitution."
  explanation: "The point is that logical inference is non-deterministic — the correct instantiation of a variable often isn't determined until several steps later. Committing to x = a when x = f(b) might be needed downstream is an irreversible error. The MGU is the uniquely correct choice because it defers all commitments except those forced by the current unification task. This is why Robinson's algorithm explicitly computes the MGU rather than any unifier."
```

## Explainer

From your work on **first-order logic syntax** and **terms and atoms**, you know that a first-order formula is built from terms (variables, constants, function applications) and atomic formulas (predicate applications to terms), combined with logical connectives and quantifiers. **Substitution** is the operation of systematically replacing a variable with a term throughout a formula — it is how you instantiate general claims and how inference rules like universal instantiation are formally defined.

The notation φ[t/x] means "replace every **free** occurrence of variable x in φ with term t." The critical qualifier is *free*: bound occurrences of x (those under a quantifier ∀x or ∃x) are not touched, because they are not the same x — they are a different, locally scoped variable that happens to share the same name. The danger is **variable capture**: if t contains a free variable y, and y happens to be bound in φ at the location where x appears, substituting naively makes y's free occurrence "fall under" a quantifier it didn't before. For example, substituting y for x in ∃y (x = y) should give ∃y (y = y) — but naive substitution captures the free y under the ∃y, silently changing the formula's meaning. The fix is **alpha-conversion**: rename the bound variable first (∃y (x = y) → ∃z (x = z)), then substitute safely (∃z (y = z)).

**Unification** is the inverse problem: given two terms or atomic formulas s and t, find a substitution σ such that σ(s) = σ(t) — they become syntactically identical after applying σ. Such a σ is a **unifier**. The **most general unifier (MGU)** is the least committal one: it makes the minimum commitments necessary to achieve identity, leaving all other variables free to be instantiated later. For example, to unify P(f(x), y) with P(f(a), g(b)), the MGU sets x ↦ a and y ↦ g(b). Any other unifier for these two atoms could be obtained by composing the MGU with a further substitution.

**Robinson's unification algorithm** computes the MGU (or reports failure) by walking two terms in parallel. At each step, if both sides have the same function symbol or constant, recurse on subterms. If one side is a variable x not appearing in the other term t, extend the unifier with x ↦ t. If x appears in t (the **occurs check**), the algorithm fails — there is no finite term satisfying x = f(x). The algorithm runs in near-linear time (with path compression) and is the computational heart of **resolution theorem proving** and **logic programming** (Prolog). Every resolution step finds the MGU of two complementary literals and applies it before cancellation; every Prolog goal is solved by finding the MGU between the goal and a clause head.

Together, substitution and unification transform first-order inference from a semantic matching task — "does this formula follow from those?" — into a syntactic computation over term structure. The MGU is the minimal syntactic bridge between two expressions, and its minimality is essential: using a more specific unifier than necessary forecloses future flexibility, while the MGU commits only to what logic forces.
