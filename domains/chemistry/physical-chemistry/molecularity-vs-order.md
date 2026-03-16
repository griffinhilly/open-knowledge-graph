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

## Explainer

From collision theory, you know that reactions occur when molecules collide with sufficient energy and proper orientation. **Molecularity** formalizes this at the level of a single elementary step: it is simply the count of reactant molecules (or atoms, or ions) that participate in that one step. A **unimolecular** step involves one molecule rearranging or breaking apart on its own (like the isomerization of cyclopropane to propene). A **bimolecular** step involves two molecules colliding and reacting (like SN2 displacement or an E2 elimination). A **termolecular** step would require three molecules to collide simultaneously — which is so statistically unlikely that genuine termolecular elementary steps are exceedingly rare.

The crucial distinction is that molecularity applies only to **elementary steps** — reactions that occur in a single event with no intermediates. For an elementary step, the rate law follows directly from molecularity: a unimolecular step A → products has rate = k[A], a bimolecular step A + B → products has rate = k[A][B], and so on. This is not an empirical observation — it is a logical consequence of the step being elementary. If two molecules must collide for the reaction to happen, the rate must depend on the concentrations of both.

**Reaction order**, by contrast, is an empirical quantity. It describes how the experimentally measured rate of the overall reaction depends on concentration: if rate = k[A]^m[B]^n, then the reaction is m-th order in A, n-th order in B, and (m + n)-th order overall. For an elementary reaction, order equals molecularity. But most reactions are not elementary — they proceed through a mechanism of multiple elementary steps, and the overall rate law is determined by the rate-limiting step and the relationships between intermediates. The overall order can be fractional, zero, negative, or any value; it bears no necessary relationship to the stoichiometric coefficients of the balanced equation.

Consider a concrete example: the decomposition of ozone, 2O₃ → 3O₂. The stoichiometry might suggest second order, but the experimentally observed rate law is rate = k[O₃]²[O₂]⁻¹ — the reaction is negative first-order in O₂, something that makes no sense if you try to read order from stoichiometry. The mechanism involves a fast equilibrium (O₃ ⇌ O₂ + O) followed by a slow bimolecular step (O + O₃ → 2O₂). Deriving the rate law from this mechanism, using the pre-equilibrium approximation, yields the observed rate expression. The molecularity of each step is well-defined (unimolecular dissociation, then bimolecular collision), but the overall order reflects the combined kinetics of the entire mechanism. Keeping this distinction clear — molecularity describes mechanism, order describes measurement — is essential for correctly interpreting kinetic data and proposing mechanisms.
