---
id: molecularity-vs-order
title: 'Molecularity vs Reaction Order: Elementary and Complex Reactions'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: collision-theory-advanced-kinetics
  type: hard
builds-toward:
- bimolecular-reaction-dynamics
tags:
- molecularity
- reaction-order
- elementary-reactions
- unimolecular
- bimolecular
- termolecular
- rate-law
stage: advanced
status: draft
---

# Molecularity vs Reaction Order: Elementary and Complex Reactions

## Core Idea
Molecularity is the number of reactant molecules that come together in a single elementary step: unimolecular (one molecule rearranges or dissociates), bimolecular (two molecules collide), or termolecular (three molecules collide simultaneously, which is rare). For elementary reactions, molecularity directly determines the rate law -- a bimolecular step A + B -> products has rate = k[A][B]. Reaction order, by contrast, is an empirical quantity determined from the overall rate law of the observed reaction, which may involve multiple elementary steps. For complex (multi-step) reactions, the overall order bears no necessary relation to the stoichiometry or to the molecularity of any individual step. The distinction is critical: molecularity is a mechanistic concept that applies only to elementary steps, while order is an experimental observable that applies to the overall reaction.

## How It's Best Learned
Examine a multi-step mechanism (e.g., the decomposition of N2O5 or the H2 + Br2 reaction) and derive the overall rate law using the steady-state or pre-equilibrium approximation. Compare the resulting overall order to the molecularity of each individual step to see clearly that they differ.

## Common Misconceptions
- Assuming reaction order equals the sum of stoichiometric coefficients; this is only true for elementary reactions, not for overall reactions with multi-step mechanisms.
- Believing termolecular reactions are common; simultaneous three-body collisions are statistically improbable, so most "termolecular" processes actually proceed through two sequential bimolecular steps.

## Questions

```yaml
- question: "A reaction has the stoichiometry 2NO + O₂ → 2NO₂. A student writes the rate law as rate = k[NO]²[O₂]. When is this guaranteed to be correct?"
  type: multiple-choice
  options:
    - "Always — stoichiometric coefficients always equal the reaction orders"
    - "Only if the reaction is elementary (occurs in a single step with no intermediates)"
    - "Only if the reaction is carried out at high temperature"
    - "Never — rate laws must always be determined by experiment regardless of mechanism"
  answer: 1
  explanation: "Stoichiometric coefficients equal the rate law exponents ONLY for elementary reactions. For an elementary step, molecularity determines the rate law mechanistically. For a multi-step mechanism, the overall rate law depends on which step is rate-limiting and how intermediates relate — the result can be fractional, zero, or even negative order in a species, with no necessary connection to the balanced equation. The student's rate law may happen to be correct if the reaction is elementary, but you cannot assume it is without mechanistic evidence."

- question: "Ozone decomposes via 2O₃ → 3O₂ with the experimentally measured rate law: rate = k[O₃]²[O₂]⁻¹. What does the negative order in O₂ indicate?"
  type: multiple-choice
  options:
    - "O₂ is a reactant being consumed, which always produces negative order"
    - "The reaction proceeds through a multi-step mechanism where a fast equilibrium produces O₂ as a product that inhibits the rate-limiting step"
    - "The experimenter made an error — orders cannot be negative"
    - "O₂ has a molecularity of −1 in the rate-determining step"
  answer: 1
  explanation: "Negative reaction order is impossible to rationalize from stoichiometry but makes perfect sense mechanistically. In the ozone mechanism, the fast pre-equilibrium O₃ ⇌ O₂ + O produces an oxygen atom intermediate. The slow step is O + O₃ → 2O₂. Applying the pre-equilibrium approximation yields rate = k[O₃]²[O₂]⁻¹ — the O₂ produced by the fast step accumulates and drives it backward, reducing the concentration of the intermediate and slowing the overall reaction. This is only possible in a multi-step mechanism; no elementary step can have negative molecularity."

- question: "For an elementary reaction, molecularity and reaction order are the same thing."
  type: true-false
  answer: true
  explanation: "True. For an elementary reaction — one that occurs in a single molecular event with no intermediates — the rate law follows directly from molecularity. A unimolecular step A → products has rate = k[A] (first order); a bimolecular step A + B → products has rate = k[A][B] (second order overall). This is not empirical but mechanistically necessary: if two molecules must collide for the reaction to happen, the rate must depend on the concentration of both. This identity between molecularity and order breaks down entirely for multi-step (complex) reactions."

- question: "Termolecular elementary steps are common in gas-phase reactions because three molecules can easily collide with sufficient combined energy."
  type: true-false
  answer: false
  explanation: "False. Genuine termolecular elementary steps are exceedingly rare because they require three molecules to collide simultaneously — a statistically improbable event. The probability of a two-body collision is already concentration-dependent; requiring a third body to be present at exactly the right moment and orientation makes simultaneous three-body collisions extremely infrequent. Most reactions that appear termolecular from their stoichiometry actually proceed through two sequential bimolecular steps. This is why unimolecular and bimolecular steps account for nearly all elementary steps in known mechanisms."

- question: "Explain why the overall reaction order for a multi-step reaction cannot be read from the stoichiometric coefficients of the balanced equation, and give the key condition under which stoichiometry DOES determine the rate law."
  type: short-answer
  answer: "For a multi-step reaction, the overall rate law is determined by the mechanism — specifically by the rate-limiting step and the steady-state or pre-equilibrium relationships between intermediates. The stoichiometric coefficients describe the overall change in matter, not which molecules are colliding in any single step. Intermediates can appear in the rate expression even though they are absent from the balanced equation. Stoichiometry determines the rate law only for elementary reactions, where the reaction occurs in a single step and molecularity (the count of reacting molecules) directly dictates the rate law exponents."
  explanation: "The key insight is that molecularity is a mechanistic concept (how many molecules collide in one step), while reaction order is an empirical measurement of the overall kinetics. They coincide only when the reaction has a single elementary step. Any multi-step mechanism can produce any overall order, including fractional and negative orders, depending on the topology of the mechanism and which step limits the rate."
```

## Explainer

From collision theory, you know that reactions occur when molecules collide with sufficient energy and proper orientation. **Molecularity** formalizes this at the level of a single elementary step: it is simply the count of reactant molecules (or atoms, or ions) that participate in that one step. A **unimolecular** step involves one molecule rearranging or breaking apart on its own (like the isomerization of cyclopropane to propene). A **bimolecular** step involves two molecules colliding and reacting (like SN2 displacement or an E2 elimination). A **termolecular** step would require three molecules to collide simultaneously — which is so statistically unlikely that genuine termolecular elementary steps are exceedingly rare.

The crucial distinction is that molecularity applies only to **elementary steps** — reactions that occur in a single event with no intermediates. For an elementary step, the rate law follows directly from molecularity: a unimolecular step A → products has rate = k[A], a bimolecular step A + B → products has rate = k[A][B], and so on. This is not an empirical observation — it is a logical consequence of the step being elementary. If two molecules must collide for the reaction to happen, the rate must depend on the concentrations of both.

**Reaction order**, by contrast, is an empirical quantity. It describes how the experimentally measured rate of the overall reaction depends on concentration: if rate = k[A]^m[B]^n, then the reaction is m-th order in A, n-th order in B, and (m + n)-th order overall. For an elementary reaction, order equals molecularity. But most reactions are not elementary — they proceed through a mechanism of multiple elementary steps, and the overall rate law is determined by the rate-limiting step and the relationships between intermediates. The overall order can be fractional, zero, negative, or any value; it bears no necessary relationship to the stoichiometric coefficients of the balanced equation.

Consider a concrete example: the decomposition of ozone, 2O₃ → 3O₂. The stoichiometry might suggest second order, but the experimentally observed rate law is rate = k[O₃]²[O₂]⁻¹ — the reaction is negative first-order in O₂, something that makes no sense if you try to read order from stoichiometry. The mechanism involves a fast equilibrium (O₃ ⇌ O₂ + O) followed by a slow bimolecular step (O + O₃ → 2O₂). Deriving the rate law from this mechanism, using the pre-equilibrium approximation, yields the observed rate expression. The molecularity of each step is well-defined (unimolecular dissociation, then bimolecular collision), but the overall order reflects the combined kinetics of the entire mechanism. Keeping this distinction clear — molecularity describes mechanism, order describes measurement — is essential for correctly interpreting kinetic data and proposing mechanisms.
