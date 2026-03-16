---
id: arithmetical-hierarchy
title: The Arithmetical Hierarchy
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: re-and-co-re-languages
  type: hard
- id: first-order-logic-syntax
  type: hard
- id: formal-arithmetic-and-expressibility
  type: soft
- id: godels-incompleteness-theorems
  type: soft
- id: mathematical-induction
  type: soft
- id: cardinality-and-countability
  type: soft
tags:
- computability
- definability
- logic
- hierarchy
stage: advanced
status: validated
---

# The Arithmetical Hierarchy

## Core Idea
The arithmetical hierarchy classifies sets of natural numbers by the complexity of their first-order definitions over arithmetic. A set is Σ₁ if definable with one existential quantifier block (equivalently, RE); Π₁ if definable with one universal quantifier block (co-RE). Higher levels Σₙ and Πₙ alternate quantifier blocks, and no level collapses into the one below — each level contains strictly harder problems. This hierarchy connects computability theory to logic and forms the foundation for more refined degree theory.

## How It's Best Learned
Study both the syntactic characterization (quantifier alternation depth) and the semantic one (oracle TM computation). Verify that the halting problem is Σ₁-complete and that the totality problem (does TM M halt on all inputs?) is Π₂-complete as a concrete example of a higher-level problem.

## Common Misconceptions
- The arithmetical hierarchy is not the polynomial hierarchy from complexity theory — the former concerns computability and definability, the latter concerns polynomial-time computation.
- Σₙ and Πₙ are not disjoint; their intersection Δₙ contains problems definable both ways, and Δ₁ equals exactly the class of decidable sets.

## Explainer

You already know that RE languages (Σ₁) are those accepted by a Turing machine that may loop on non-members, and co-RE (Π₁) are their complements — languages where membership can be disproved by a halting TM. The arithmetical hierarchy generalizes this by asking: how many alternating blocks of quantifiers does it take to *define* a set of natural numbers in the language of arithmetic?

The key idea is that quantifier alternation depth measures definitional complexity. A set is **Σ₁** if you can express membership as "there exists a number n such that some computable predicate holds" — equivalently, it is RE. A set is **Π₁** if it requires a universal quantifier at the front: "for all n, ..." — equivalently, co-RE. The sets you can decide outright (decidable/recursive) sit in **Δ₁**, the intersection of Σ₁ and Π₁: they are both RE and co-RE simultaneously. This should feel natural — you know that a language is decidable iff both it and its complement are RE.

The hierarchy climbs by alternating quantifiers. A **Σ₂** set has the form ∃x ∀y P(n,x,y) for computable P — you first guess a witness, then universally check it. A **Π₂** set flips the order: ∀x ∃y P(n,x,y). The classic Σ₂ example is the set of indices of TMs that halt on *some* input (Σ₂-complete). The classic Π₂ example is the **totality problem**: the set of TM indices e such that Mₑ halts on *every* input. You cannot solve totality with just one quantifier type — you need to say "for all inputs x, there exists a halting computation," which requires a ∀∃ shape.

The separation result — no level collapses into the one below — means the hierarchy is strict and infinite. Each level contains genuinely harder problems that no number of oracle queries can push down. The arithmetic hierarchy also connects back to Gödel's incompleteness: Σ₁ statements are exactly the ones provably equivalent to a computation halting, and the unprovable sentences of arithmetic live at the boundary between definable levels and truth in the standard model. Understanding the hierarchy is the foundation for degree theory, where you study reductions between problems rather than just their class membership.

The hierarchy can alternatively be presented through **oracle computation**: a set is Σₙ iff it is RE relative to a Σₙ₋₁-complete oracle (such as the nth jump of the halting problem). This oracle presentation makes the levels feel more computational and connects directly to the reducibility theory you will encounter in degree theory. Whether you prefer the syntactic (quantifier-counting) or semantic (oracle) perspective, the hierarchy gives you a fine-grained map of the landscape between decidable and arbitrarily hard arithmetic.
