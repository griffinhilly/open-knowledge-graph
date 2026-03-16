---
id: turing-degrees
title: Turing Degrees
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: computability-reductions
  type: hard
- id: halting-problem-formal
  type: hard
builds-toward:
- arithmetical-hierarchy
tags:
- computability
- degree-theory
- reducibility
stage: formal-systems
status: draft
---

# Turing Degrees

## Core Idea
Two sets have the same Turing degree if each is Turing-reducible to the other — they are equally hard to compute. The Turing degrees form a partially ordered structure under reducibility, with the computable sets at degree 0 (the bottom) and the halting problem at degree 0' (zero-jump). The jump operator maps each degree d to a strictly higher degree d', producing an ascending chain. Post's problem asked whether there exist degrees strictly between 0 and 0'; Friedberg and Muchnik independently answered yes using the priority method, revealing that the degree structure is far richer than a simple linear chain.

## How It's Best Learned
First internalize Turing reducibility as "A is computable given B as an oracle." Then study the jump operator and verify that 0 < 0' < 0'' forms a strict chain. Finally, learn the statement (not necessarily the full proof) of the Friedberg-Muchnik theorem to appreciate that incomparable degrees exist — the structure branches, not just climbs.

## Common Misconceptions
- The Turing degrees are NOT linearly ordered — there exist incomparable degrees where neither set is reducible to the other.
- Turing degree 0 contains infinitely many distinct sets (all computable sets), not just the empty set — a degree is an equivalence class, not a single set.

## Explainer

You already know Turing reducibility: A ≤_T B means A is computable given an oracle for B. Think of an oracle as a black box that answers membership queries about B in one step — your algorithm for A can call the oracle freely. If A ≤_T B, then B is "at least as hard" as A in terms of computational power. Now define the equivalence relation A ≡_T B when both A ≤_T B and B ≤_T A. Two sets in the same equivalence class are interchangeable as oracles — each can simulate the other. These equivalence classes are the **Turing degrees**: a degree bundles together everything that is "equally hard to compute."

The **degree of the computable sets** is called **0** (zero). Every computable set has degree 0 because if A is computable, you can compute it without any oracle, so A ≤_T B for any B; and any computable B can be computed from A's oracle trivially. Above 0 sits **0'** (zero-jump), the degree of the halting problem. The **jump operator** maps any degree d to a strictly higher degree d' by taking the halting problem *relativized* to a d-oracle. This gives an infinite ascending chain: 0 < 0' < 0'' < 0''' < ..., mirroring the arithmetical hierarchy you'll study next.

The jump might suggest the degrees form a single ascending chain. Post's problem, posed in 1944, asked: is there a degree strictly between 0 and 0'? The answer is *yes*, and its proof — the **Friedberg-Muchnik theorem** — inaugurated the priority method, one of the deepest proof techniques in computability theory. The construction builds two sets A and B that are each not computable (above 0) yet neither reduces to the other (incomparable below 0'). This means the degree structure is not a chain but a **partial order** that *branches* — it has incomparable elements at every level. Above any degree, there exist infinitely many pairwise incomparable degrees.

The Turing degrees are the finest grain at which we can classify non-computable sets by their "information content." Two sets have the same degree exactly when they carry the same oracular information. The structure has remarkable complexity: it is dense (between any two comparable degrees lies another), there are minimal degrees (just above 0 with nothing between), and the first-order theory of the degrees is undecidable. What started as a clean hierarchy — computable, halting, second jump — turns out to be an extraordinarily rich and complicated universe, most of which remains not fully understood.

