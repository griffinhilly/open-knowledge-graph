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
stage: formal-systems
status: validated
---

# Lovász Local Lemma

## Core Idea
The Lovász Local Lemma is a powerful tool showing that if many 'bad events' have limited dependencies, then with positive probability none occur. If each event has probability at most p and affects at most d others, and ep(d+1) ≤ 1, then P(no bad event) > 0. This lemma resolves seemingly impossible combinatorial existence questions.

## How It's Best Learned
Apply the lemma to a concrete problem like showing existence of graphs with low discrepancy or high girth.

## Common Misconceptions
The condition ep(d+1) ≤ 1 is sufficient but not necessary; the actual threshold for positivity can be better. Also, 'd' counts neighbors in the dependency graph, not arbitrary other events.

## Questions

```yaml
- question: "You have 500 bad events, each with probability 1/50, and each sharing randomness with at most 4 other events. Does the Lovász Local Lemma guarantee that all bad events can simultaneously be avoided?"
  type: multiple-choice
  options:
    - "No — with 500 events each at probability 1/50, the expected number of bad events is 10, so some must occur"
    - "Yes — the LLL condition ep(d+1) ≤ 1 becomes e·(1/50)·5 ≈ 0.272 ≤ 1, so P(none occur) > 0"
    - "No — the LLL only applies when bad events are fully independent, not merely locally dependent"
    - "Yes — with probability 1/50 per event, each event is unlikely enough to guarantee avoidability regardless of dependency structure"
  answer: 1
  explanation: "Check the LLL condition: p = 1/50, d = 4, so ep(d+1) = e · (1/50) · 5 = e/10 ≈ 0.272 ≤ 1. The condition is satisfied, so P(no bad event occurs) > 0. Option A is the classic confusion: a positive expected number of bad events does not prevent the possibility of avoiding all of them. The union bound fails to prove the result, but the LLL's exploitation of limited dependency succeeds. The LLL is precisely the tool for situations where naive expectation arguments are misleading."

- question: "In the LLL's condition ep(d+1) ≤ 1, what does 'd' represent?"
  type: multiple-choice
  options:
    - "The total number of bad events in the combinatorial problem"
    - "The maximum number of bad events that share randomness with a given bad event — its degree in the dependency graph"
    - "The probability that any particular bad event occurs"
    - "The number of independent random choices underlying the probability space"
  answer: 1
  explanation: "d is the maximum degree in the dependency graph — the largest number of other bad events that any single bad event can share randomness with. Two bad events are neighbors in the dependency graph if knowing whether one occurred gives information about the other (i.e., they are not independent). A common error is to set d to the total number of events; the LLL is powerful precisely because d only counts local neighbors, not all other events. When d is small relative to 1/p, the LLL condition is easily satisfied even with large numbers of events."

- question: "The LLL is more powerful than a simple union bound because it can guarantee P(no bad event) > 0 even when the union bound ΣP(Aᵢ) exceeds 1."
  type: true-false
  answer: true
  explanation: "The union bound P(∪Aᵢ) ≤ ΣP(Aᵢ) becomes vacuous when the sum exceeds 1, since all probabilities are at most 1. In problems with many bad events — even individually unlikely ones — the sum easily exceeds 1, and the union bound cannot prove that any avoidance is possible. The LLL exploits limited dependency structure to prove positivity of P(no bad event) in exactly these situations. This is why the LLL is so important in combinatorics: it handles regimes where the naive probabilistic argument completely breaks down."

- question: "The LLL condition ep(d+1) ≤ 1 is both necessary and sufficient: if this condition fails, it is impossible to simultaneously avoid all bad events."
  type: true-false
  answer: false
  explanation: "The condition ep(d+1) ≤ 1 is sufficient but not necessary. It is a clean, checkable threshold that guarantees P(no bad event) > 0, but the actual threshold at which simultaneous avoidance becomes impossible can be considerably weaker — the LLL is not tight at this bound. In some structured settings, stronger variants (such as the asymmetric LLL) give tighter conditions. The Common Misconceptions section of this topic makes this point explicitly: failing the ep(d+1) ≤ 1 condition does not prove impossibility."

- question: "Why can't a simple union bound prove the existence results that the LLL proves, and what key property does the LLL exploit instead?"
  type: short-answer
  answer: "A union bound says P(∪Aᵢ) ≤ ΣP(Aᵢ). When there are many bad events, this sum easily exceeds 1, making the bound vacuous — it cannot establish that P(no bad event) > 0. The union bound also implicitly treats all events as if they were independent, ignoring the dependency structure entirely. The LLL exploits a weaker, more realistic property: limited dependency. Each bad event needs to share randomness with at most d other events, and if ep(d+1) ≤ 1, then an inductive argument shows that the probability each event occurs, conditioned on all nearby events being avoided, remains at most p. This mutual consistency is maintained across the whole system simultaneously, proving that global avoidance is achievable. The insight is that you don't need full independence — bounded locality in the dependency graph is enough."
  explanation: "The LLL's power is that it converts 'there are too many bad interactions for a naive argument' into 'the interactions are local enough that we can avoid them all.' This has made it one of the most widely applied tools in probabilistic combinatorics, with applications ranging from graph coloring to hypergraph satisfiability to Ramsey theory."
```

## Explainer

From your work with the **probabilistic method**, you know the basic technique: define a random object, compute the expected value of some property, and conclude that an object achieving that value must exist. The simplest version avoids all "bad events" by showing P(all bad events occur) < 1 — but this requires the probability of each bad event to be small and, critically, that the bad events are *independent*. The Lovász Local Lemma is a powerful generalization that works when bad events are nearly, but not perfectly, independent.

The central tension is this: in most combinatorial problems, bad events overlap. If event Aᵢ says "edge i is too long" and Aⱼ says "edge j is too long," and i and j share a vertex, these events are not independent — they share randomness. Pure union-bound arguments (P(∪Aᵢ) ≤ Σ P(Aᵢ)) can be useless when there are many events. The **LLL** exploits the fact that *limited* dependency is enough. Each bad event Aᵢ may depend on at most d other events, and if each event has probability at most p with ep(d+1) ≤ 1 (where e = 2.718…), then with positive probability, none of the bad events occur simultaneously.

The condition ep(d+1) ≤ 1 is doing real work. Rearranging: p ≤ 1/(e(d+1)). This says each bad event can be somewhat probable (up to 1/e times 1/(d+1)) as long as it has limited dependencies. The lemma's proof uses a clever inductive argument: it shows that the probability any specific event occurs, conditioned on all the "nearby" events not having occurred, is still at most p. This mutual consistency is maintained throughout the induction, so the entire system of avoidances is achievable simultaneously.

A canonical application: show that any graph with maximum degree Δ ≤ 2^(k−2) can be properly k-colored. For each edge, define the bad event that its two endpoints receive the same color. With a random coloring, P(each bad event) = 1/k. Each bad event shares randomness with at most 2(Δ−1) ≤ 2Δ neighboring edges. Setting p = 1/k and d = 2Δ, the LLL condition ep(d+1) ≤ 1 becomes e·(1/k)·(2Δ+1) ≤ 1, which holds when k is large enough relative to Δ. Existence of a proper coloring follows — no construction needed, just the probabilistic argument. This is the characteristic power of the LLL: it transforms "there are too many bad interactions for a naive argument" into "the interactions are local enough that we can avoid them all."
