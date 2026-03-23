---
id: reaction-mechanisms-elementary-steps
title: Reaction Mechanisms and Elementary Steps
domain: chemistry
course: general-chemistry
prerequisites:
- id: rate-laws-experimental-determination-orders
  type: hard
- id: reaction-mechanisms-overview
  type: soft
builds-toward:
- organic-chemistry-intro
tags:
- mechanism
- elementary-step
- intermediate
- kinetics
stage: formal-systems
status: draft
---

# Reaction Mechanisms and Elementary Steps

## Core Idea
A reaction mechanism is a sequence of elementary steps that sum to the overall reaction. Elementary steps are molecular-level events showing exactly which atoms/molecules collide. An intermediate is produced in one step and consumed in a later step. The rate-determining (slowest) step governs overall kinetics and the rate law must be consistent with the proposed mechanism.

## Questions

```yaml
- question: "The overall balanced equation for a reaction is: 2NO(g) + O₂(g) → 2NO₂(g). A student writes the rate law as rate = k[NO]²[O₂]. What is the problem with this reasoning?"
  type: multiple-choice
  options:
    - "The rate law should use molar concentrations, not partial pressures"
    - "The rate law for an overall reaction cannot be written from its stoichiometry — it must be determined experimentally or derived from the mechanism's rate-determining step"
    - "The exponents should equal 1 for each reactant in any rate law"
    - "Only products can appear in a rate law, not reactants"
  answer: 1
  explanation: "Rate laws for overall reactions must be determined experimentally or derived from the proposed mechanism's rate-determining step. Only for elementary steps can you write the rate law directly from stoichiometry. The overall stoichiometry reflects the net result of multiple steps and gives no direct information about the reaction mechanism or rate law."

- question: "In a proposed two-step mechanism, Step 1 (fast, reversible) produces intermediate X, and Step 2 (slow) converts X into product. The experimentally measured rate law involves only original reactants. How is this consistent?"
  type: multiple-choice
  options:
    - "Intermediates never appear in rate laws because they have zero concentration"
    - "The pre-equilibrium approximation expresses [X] in terms of original reactants using the equilibrium constant of Step 1, which is then substituted into the rate law for Step 2"
    - "The intermediate X is treated as a reactant because it is consumed in Step 2"
    - "Only the fast step determines the rate law, so X's concentration is irrelevant"
  answer: 1
  explanation: "Since Step 1 is fast and reversible, it reaches equilibrium before the slow step proceeds. Setting the forward and reverse rates of Step 1 equal gives an expression for [X] in terms of the original reactants and the equilibrium constant. Substituting this into the rate expression for the slow step eliminates the intermediate, producing a rate law in terms of measurable concentrations."

- question: "For an elementary bimolecular reaction A + B → C, you can always write the rate law as rate = k[A][B] directly from the stoichiometry."
  type: true-false
  answer: true
  explanation: "Elementary steps are single molecular-level events. For a bimolecular step, two specific molecules must collide, so the rate depends on the probability of both being present — which is proportional to [A][B]. This is the one case where stoichiometry directly gives the rate law. This rule applies only to elementary steps, not to overall reactions."

- question: "If the overall balanced equation for a reaction is first order in A and first order in B, the reaction must proceed through a single bimolecular elementary step."
  type: true-false
  answer: false
  explanation: "The experimentally observed rate law tells you about the rate-determining step, not the overall mechanism. A second-order rate law could arise from a multi-step mechanism in which the slow step happens to involve one molecule of A and one of B — even if the overall equation has different stoichiometry or if earlier steps involve other species. The mechanism cannot be read off from the overall rate law alone."

- question: "Why can't the concentration of a reaction intermediate appear in the final rate law, and how does the pre-equilibrium approximation solve this problem?"
  type: short-answer
  answer: "Intermediates are produced and consumed within the mechanism — they are not present at the start of the reaction, so their concentration cannot be directly measured or controlled. The pre-equilibrium approximation solves this by using the equilibrium constant of a fast reversible step that produces the intermediate: setting forward rate = reverse rate gives an algebraic expression for [intermediate] in terms of original reactant concentrations. Substituting this expression into the slow-step rate law replaces the unmeasurable intermediate with measurable quantities."
  explanation: "The pre-equilibrium approximation is valid when the step producing the intermediate is much faster than the step consuming it, so the intermediate concentration stays at its quasi-equilibrium value. The result is a rate law written entirely in terms of species present at the start of the reaction."
```

## Explainer

When you determined rate laws experimentally, you discovered that the mathematical relationship between concentration and rate often does not match the stoichiometry of the balanced equation. That mismatch is the clue that the reaction does not happen in a single step. A **reaction mechanism** is the proposed sequence of simple, molecular-level events — called **elementary steps** — that together account for the overall transformation. Each elementary step describes exactly which molecules collide and which bonds break or form in a single event, so for elementary steps alone, the rate law can be written directly from the stoichiometry (a unimolecular step is first order, a bimolecular step is second order).

Think of a mechanism like driving directions between two cities. The balanced equation tells you the start and the destination; the mechanism tells you which roads you take and in what order. Along the way you pass through towns that are neither your origin nor your destination — these are **reaction intermediates**, species produced in one elementary step and consumed in a subsequent step. Intermediates are real molecules with finite lifetimes, but they do not appear in the overall balanced equation because they cancel out when you sum all the elementary steps. This summation requirement is your first test of a proposed mechanism: the elementary steps must add up to the observed overall reaction.

The second test involves kinetics. Among the elementary steps, one is typically much slower than the rest — this is the **rate-determining step**, the bottleneck that controls how fast the entire reaction proceeds. The analogy is a highway that narrows to one lane: no matter how wide the road is before and after, overall traffic flow is limited by that bottleneck. The rate law predicted by the mechanism must match the experimentally determined rate law you already know how to measure. If the slow step involves two molecules of reactant A, the overall rate law should be second order in A — regardless of what the balanced equation's coefficients say.

A common complication arises when the rate-determining step involves an intermediate rather than an original reactant. Since intermediates are not present at the start of the reaction, their concentration cannot appear in the final rate law. You resolve this by using a **pre-equilibrium approximation**: if a fast, reversible step precedes the slow step, you express the intermediate's concentration in terms of the original reactants using the equilibrium constant of that fast step, then substitute back into the rate law for the slow step. The result is a rate law written entirely in terms of measurable reactant concentrations — exactly what your experimental data can confirm or refute. This interplay between mechanism proposal and experimental verification is the core method of chemical kinetics.
