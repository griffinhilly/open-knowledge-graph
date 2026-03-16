---
id: lovasz-local-lemma
title: Lovász Local Lemma
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: probabilistic-method-graphs
  type: hard
tags:
- combinatorics
- probability
stage: advanced
status: draft
---

# Lovász Local Lemma

## Core Idea
The Lovász Local Lemma is a powerful tool showing that if many 'bad events' have limited dependencies, then with positive probability none occur. If each event has probability at most p and affects at most d others, and ep(d+1) ≤ 1, then P(no bad event) > 0. This lemma resolves seemingly impossible combinatorial existence questions.

## How It's Best Learned
Apply the lemma to a concrete problem like showing existence of graphs with low discrepancy or high girth.

## Common Misconceptions
The condition ep(d+1) ≤ 1 is sufficient but not necessary; the actual threshold for positivity can be better. Also, 'd' counts neighbors in the dependency graph, not arbitrary other events.

## Explainer

From your work with the **probabilistic method**, you know the basic technique: define a random object, compute the expected value of some property, and conclude that an object achieving that value must exist. The simplest version avoids all "bad events" by showing P(all bad events occur) < 1 — but this requires the probability of each bad event to be small and, critically, that the bad events are *independent*. The Lovász Local Lemma is a powerful generalization that works when bad events are nearly, but not perfectly, independent.

The central tension is this: in most combinatorial problems, bad events overlap. If event Aᵢ says "edge i is too long" and Aⱼ says "edge j is too long," and i and j share a vertex, these events are not independent — they share randomness. Pure union-bound arguments (P(∪Aᵢ) ≤ Σ P(Aᵢ)) can be useless when there are many events. The **LLL** exploits the fact that *limited* dependency is enough. Each bad event Aᵢ may depend on at most d other events, and if each event has probability at most p with ep(d+1) ≤ 1 (where e = 2.718…), then with positive probability, none of the bad events occur simultaneously.

The condition ep(d+1) ≤ 1 is doing real work. Rearranging: p ≤ 1/(e(d+1)). This says each bad event can be somewhat probable (up to 1/e times 1/(d+1)) as long as it has limited dependencies. The lemma's proof uses a clever inductive argument: it shows that the probability any specific event occurs, conditioned on all the "nearby" events not having occurred, is still at most p. This mutual consistency is maintained throughout the induction, so the entire system of avoidances is achievable simultaneously.

A canonical application: show that any graph with maximum degree Δ ≤ 2^(k−2) can be properly k-colored. For each edge, define the bad event that its two endpoints receive the same color. With a random coloring, P(each bad event) = 1/k. Each bad event shares randomness with at most 2(Δ−1) ≤ 2Δ neighboring edges. Setting p = 1/k and d = 2Δ, the LLL condition ep(d+1) ≤ 1 becomes e·(1/k)·(2Δ+1) ≤ 1, which holds when k is large enough relative to Δ. Existence of a proper coloring follows — no construction needed, just the probabilistic argument. This is the characteristic power of the LLL: it transforms "there are too many bad interactions for a naive argument" into "the interactions are local enough that we can avoid them all."
