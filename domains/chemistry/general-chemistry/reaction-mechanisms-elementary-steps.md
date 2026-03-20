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
stage: advanced
status: draft
---

# Reaction Mechanisms and Elementary Steps

## Core Idea
A reaction mechanism is a sequence of elementary steps that sum to the overall reaction. Elementary steps are molecular-level events showing exactly which atoms/molecules collide. An intermediate is produced in one step and consumed in a later step. The rate-determining (slowest) step governs overall kinetics and the rate law must be consistent with the proposed mechanism.

## Explainer

When you determined rate laws experimentally, you discovered that the mathematical relationship between concentration and rate often does not match the stoichiometry of the balanced equation. That mismatch is the clue that the reaction does not happen in a single step. A **reaction mechanism** is the proposed sequence of simple, molecular-level events — called **elementary steps** — that together account for the overall transformation. Each elementary step describes exactly which molecules collide and which bonds break or form in a single event, so for elementary steps alone, the rate law can be written directly from the stoichiometry (a unimolecular step is first order, a bimolecular step is second order).

Think of a mechanism like driving directions between two cities. The balanced equation tells you the start and the destination; the mechanism tells you which roads you take and in what order. Along the way you pass through towns that are neither your origin nor your destination — these are **reaction intermediates**, species produced in one elementary step and consumed in a subsequent step. Intermediates are real molecules with finite lifetimes, but they do not appear in the overall balanced equation because they cancel out when you sum all the elementary steps. This summation requirement is your first test of a proposed mechanism: the elementary steps must add up to the observed overall reaction.

The second test involves kinetics. Among the elementary steps, one is typically much slower than the rest — this is the **rate-determining step**, the bottleneck that controls how fast the entire reaction proceeds. The analogy is a highway that narrows to one lane: no matter how wide the road is before and after, overall traffic flow is limited by that bottleneck. The rate law predicted by the mechanism must match the experimentally determined rate law you already know how to measure. If the slow step involves two molecules of reactant A, the overall rate law should be second order in A — regardless of what the balanced equation's coefficients say.

A common complication arises when the rate-determining step involves an intermediate rather than an original reactant. Since intermediates are not present at the start of the reaction, their concentration cannot appear in the final rate law. You resolve this by using a **pre-equilibrium approximation**: if a fast, reversible step precedes the slow step, you express the intermediate's concentration in terms of the original reactants using the equilibrium constant of that fast step, then substitute back into the rate law for the slow step. The result is a rate law written entirely in terms of measurable reactant concentrations — exactly what your experimental data can confirm or refute. This interplay between mechanism proposal and experimental verification is the core method of chemical kinetics.
