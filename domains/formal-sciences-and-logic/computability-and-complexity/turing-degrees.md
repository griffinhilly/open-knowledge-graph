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
- id: oracle-turing-machines-computability-and-complexity
  type: soft
- id: partial-vs-total-recursive-functions
  type: soft
- id: recursively-enumerable-languages-properties
  type: soft
- id: computability-complexity-overview
  type: soft
- id: reducibility-many-one-formal
  type: soft
builds-toward:
- arithmetical-hierarchy
tags:
- computability
- degree-theory
- reducibility
stage: advanced
status: validated
---
# Turing Degrees

## Core Idea
Two sets have the same Turing degree if each is Turing-reducible to the other — they are equally hard to compute. The Turing degrees form a partially ordered structure under reducibility, with the computable sets at degree 0 (the bottom) and the halting problem at degree 0' (zero-jump). The jump operator maps each degree d to a strictly higher degree d', producing an ascending chain. Post's problem asked whether there exist degrees strictly between 0 and 0'; Friedberg and Muchnik independently answered yes using the priority method, revealing that the degree structure is far richer than a simple linear chain.

## How It's Best Learned
First internalize Turing reducibility as "A is computable given B as an oracle." Then study the jump operator and verify that 0 < 0' < 0'' forms a strict chain. Finally, learn the statement (not necessarily the full proof) of the Friedberg-Muchnik theorem to appreciate that incomparable degrees exist — the structure branches, not just climbs.

## Common Misconceptions
- The Turing degrees are NOT linearly ordered — there exist incomparable degrees where neither set is reducible to the other.
- Turing degree 0 contains infinitely many distinct sets (all computable sets), not just the empty set — a degree is an equivalence class, not a single set.

## Questions

```yaml
- question: "Suppose A ≤_T B but B is not ≤_T A. What can we conclude about the Turing degrees of A and B?"
  type: multiple-choice
  options:
    - "A and B have the same Turing degree, since A is computable from B"
    - "A has a strictly lower Turing degree than B — B is strictly harder to compute than A"
    - "This situation is impossible — if A ≤_T B, then B ≤_T A must also hold"
    - "A and B are incomparable — neither is harder than the other"
  answer: 1
  explanation: "Two sets have the same Turing degree when each is reducible to the other (mutual reducibility). If A ≤_T B but B is not ≤_T A, then the mutual reducibility fails: B carries strictly more computational information than A. The degree of A is strictly lower than the degree of B. This is analogous to a strict partial order: A's degree sits below B's degree, but the relation is not symmetric. Incomparable degrees arise only when neither set reduces to the other — a different situation."

- question: "What was the significance of the Friedberg-Muchnik theorem for understanding the structure of Turing degrees?"
  type: multiple-choice
  options:
    - "It proved that all non-computable sets have the same Turing degree as the halting problem"
    - "It showed that the Turing degrees form a linear (total) order — every two degrees are comparable"
    - "It showed that there exist Turing degrees strictly between 0 and 0', proving the structure branches rather than forming a single chain"
    - "It proved that the jump operator d → d' produces every degree above 0, with no gaps"
  answer: 2
  explanation: "Post's problem asked whether there exists a Turing degree strictly between 0 (the computable sets) and 0' (the halting problem). Friedberg and Muchnik independently proved such degrees exist, constructing two sets A and B that are each non-computable (above degree 0) yet neither reduces to the other (incomparable to each other, both below 0'). This shattered the naive picture of a linear hierarchy and revealed the degree structure as a complex partial order that branches at every level — with incomparable degrees existing throughout."

- question: "The jump operator guarantees that for any Turing degree d, the degree d' (its jump) is strictly higher than d."
  type: true-false
  answer: true
  explanation: "The jump d' is defined by relativizing the halting problem to a d-oracle. It is always the case that d <_T d': d is reducible to d' (trivially, since d' has all the oracle power of d plus more), but d' is not reducible to d. This strict increase is a fundamental property of the jump operator and produces the infinite ascending chain 0 < 0' < 0'' < 0''' < ⋯. Each jump yields strictly more computational power than the previous level."

- question: "The Turing degrees form a linearly ordered set — given any two Turing degrees, one should be reducible to the other."
  type: true-false
  answer: false
  explanation: "This is the most important misconception to correct. The Friedberg-Muchnik theorem proves that incomparable Turing degrees exist: sets A and B can both be non-computable, yet neither A ≤_T B nor B ≤_T A holds. Such pairs are incomparable in the partial order of Turing degrees. The degree structure branches at every level, with infinitely many pairwise incomparable degrees above any fixed degree. It is a rich, complex partial order — not a chain."

- question: "What does it mean for two sets to have the same Turing degree, and why does degree 0 contain infinitely many distinct sets rather than just one?"
  type: short-answer
  answer: "Two sets have the same Turing degree when each is Turing-reducible to the other — they are mutual oracles, carrying the same computational information. A Turing degree is an equivalence class of mutually reducible sets, not a single set. Degree 0 is the class of all computable sets. Every computable set reduces to every other computable set (trivially, since no oracle is needed), so all computable sets — the empty set, finite sets, the set of primes, and infinitely many others — fall into degree 0. The degree is the class, not one representative."
  explanation: "The key insight is that Turing degrees classify sets by their 'oracular information content,' not by their syntactic description or size. Two very different-looking sets can have the same degree if each can simulate the other as an oracle. Degree 0 captures all computationally trivial sets, of which there are infinitely many. This equivalence class structure is why the degree structure is both precise (it distinguishes levels of non-computability) and coarse (many different sets share each degree)."
```

## Explainer

You already know Turing reducibility: A ≤_T B means A is computable given an oracle for B. Think of an oracle as a black box that answers membership queries about B in one step — your algorithm for A can call the oracle freely. If A ≤_T B, then B is "at least as hard" as A in terms of computational power. Now define the equivalence relation A ≡_T B when both A ≤_T B and B ≤_T A. Two sets in the same equivalence class are interchangeable as oracles — each can simulate the other. These equivalence classes are the **Turing degrees**: a degree bundles together everything that is "equally hard to compute."

The **degree of the computable sets** is called **0** (zero). Every computable set has degree 0 because if A is computable, you can compute it without any oracle, so A ≤_T B for any B; and any computable B can be computed from A's oracle trivially. Above 0 sits **0'** (zero-jump), the degree of the halting problem. The **jump operator** maps any degree d to a strictly higher degree d' by taking the halting problem *relativized* to a d-oracle. This gives an infinite ascending chain: 0 < 0' < 0'' < 0''' < ..., mirroring the arithmetical hierarchy you'll study next.

The jump might suggest the degrees form a single ascending chain. Post's problem, posed in 1944, asked: is there a degree strictly between 0 and 0'? The answer is *yes*, and its proof — the **Friedberg-Muchnik theorem** — inaugurated the priority method, one of the deepest proof techniques in computability theory. The construction builds two sets A and B that are each not computable (above 0) yet neither reduces to the other (incomparable below 0'). This means the degree structure is not a chain but a **partial order** that *branches* — it has incomparable elements at every level. Above any degree, there exist infinitely many pairwise incomparable degrees.

The Turing degrees are the finest grain at which we can classify non-computable sets by their "information content." Two sets have the same degree exactly when they carry the same oracular information. The structure has remarkable complexity: it is dense (between any two comparable degrees lies another), there are minimal degrees (just above 0 with nothing between), and the first-order theory of the degrees is undecidable. What started as a clean hierarchy — computable, halting, second jump — turns out to be an extraordinarily rich and complicated universe, most of which remains not fully understood.

