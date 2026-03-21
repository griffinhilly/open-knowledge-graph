---
id: ehrenfeucht-fraisse-games-equivalence
title: Ehrenfeucht-Fraïssé Games and Elementary Equivalence
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: elementary-equivalence-indistinguishability
  type: hard
tags:
- back-and-forth
- EF-game
- game characterization
- finite approximation
stage: advanced
status: draft
---

# Ehrenfeucht-Fraïssé Games and Elementary Equivalence

## Core Idea
The Ehrenfeucht-Fraïssé game is a two-player game where Player I attempts to distinguish two structures and Player II attempts to maintain local equivalence. At each round, Player I selects an element from one structure and Player II responds from the other, preserving all relations. If Player II survives n rounds, the structures are equivalent up to quantifier depth n.

## Questions

```yaml
- question: "A logician sets up EF_n games between structure A (a set of 30 elements with no relations) and structure B (a set of 200 elements with no relations). For which values of n does Duplicator have a winning strategy?"
  type: multiple-choice
  options:
    - "For all n, since two pure sets look identical locally regardless of their sizes"
    - "For all n < 30, since Duplicator can always respond while unused elements remain in the smaller structure"
    - "For no value of n, since the structures have different sizes and one round is enough to distinguish them"
    - "Only for n = 1, since Duplicator can match the first move but no further"
  answer: 1
  explanation: "In a pure set (no relations in the signature), the only atomic formulas involve equality. Spoiler's only winning move is to force Duplicator to map two distinct elements to the same element (violating injectivity). With 30 elements in A, Duplicator can always respond to Spoiler's selections with fresh elements until A is exhausted. For n < 30, after n rounds only n elements of A have been selected, leaving 30−n unused. Duplicator always has a valid response. For n ≥ 30, Spoiler can exhaust all elements of A and pick a 31st from B with no corresponding element — winning the game."

- question: "What does it mean, in logical terms, for Duplicator to have a winning strategy in EF_n(A, B)?"
  type: multiple-choice
  options:
    - "A and B are isomorphic — they have the same structure in every detail"
    - "A and B satisfy all the same first-order sentences of quantifier depth at most n"
    - "A and B satisfy all the same first-order sentences of quantifier depth exactly n, but may differ on simpler sentences"
    - "Every sentence true in A of depth ≤ n is also true in B, but not necessarily vice versa"
  answer: 1
  explanation: "The fundamental theorem of EF games: Duplicator wins EF_n(A, B) if and only if A ≡_n B, meaning A and B agree on all first-order sentences of quantifier depth at most n. More rounds correspond to a richer logical language. Winning for all n simultaneously means A ≡ B (full elementary equivalence). The game translates an infinite logical question — do A and B agree on all FO sentences? — into a sequence of finite combinatorial games, each certifying agreement up to a specific logical complexity."

- question: "If Duplicator has a winning strategy in EF_n(A, B) for every natural number n, then A and B must be isomorphic."
  type: true-false
  answer: false
  explanation: "Winning for all n implies elementary equivalence (A ≡ B) — they agree on all first-order sentences. But elementary equivalence is strictly weaker than isomorphism. The dense linear order of the rationals (ℚ, <) and the reals (ℝ, <) are elementarily equivalent (both satisfy the same first-order theory of dense linear orders without endpoints) but are not isomorphic — ℝ is uncountable and ℚ is countable. First-order logic cannot express uncountability, so the EF game never produces a Spoiler win, yet the structures are structurally very different."

- question: "The Ehrenfeucht-Fraïssé game is particularly powerful for proving inexpressibility results — showing that certain properties cannot be captured by any first-order sentence."
  type: true-false
  answer: true
  explanation: "Inexpressibility proofs are the game's signature application. To show a property P is not first-order expressible, exhibit two structures A (with P) and B (without P) such that Duplicator wins EF_n(A, B) for all n. This means no FO sentence of any quantifier depth can distinguish them — so no FO sentence can capture P. Classic results proved this way: parity of domain size, finiteness, connectivity of graphs, and transitive closure are all inexpressible in first-order logic. The game converts what would otherwise be an unwieldy argument over infinitely many sentences into a constructive winning strategy."

- question: "Explain why Duplicator winning EF_n(A, B) for every natural number n does not imply that A and B are isomorphic."
  type: short-answer
  answer: "Duplicator winning for all n implies A ≡ B — elementary equivalence — meaning the two structures satisfy exactly the same first-order sentences. But first-order logic has limited expressive power: it cannot distinguish structures that differ only in properties inexpressible in FO, such as cardinality. The canonical example is the dense linear order of the rationals (ℚ, <) and the reals (ℝ, <). Both satisfy the same first-order theory of dense linear orders without endpoints (DLO), so Duplicator wins every EF game between them. Yet they are not isomorphic: ℝ is uncountable while ℚ is countable. No FO sentence detects this difference, so the games cannot reveal it — illustrating the expressive gap between FO and full model-theoretic equivalence."
  explanation: "This gap between elementary equivalence and isomorphism is one of the central themes of model theory. The compactness theorem and Löwenheim-Skolem theorems together imply that any first-order theory with an infinite model has models of every infinite cardinality — so distinct cardinalities are always elementarily equivalent in the absence of cardinality-constraining axioms (which FO cannot express). EF games are precisely calibrated to this expressive power."
```

## Explainer

You know that two structures A and B are **elementarily equivalent** if they satisfy exactly the same first-order sentences. But how do you *prove* elementary equivalence — especially for infinite structures that look superficially different? Verifying all sentences directly is impossible. The **Ehrenfeucht-Fraïssé game** replaces this with a concrete, finitary game that encodes precisely as much logical information as needed.

The game EF_n(A, B) is played over n rounds between two players: **Spoiler** (Player I) and **Duplicator** (Player II). Each round, Spoiler picks an element from either A or B, and Duplicator responds with an element from the other structure. After n rounds, the players have jointly selected elements a₁,...,aₙ ∈ A and b₁,...,bₙ ∈ B. Duplicator wins the round-n game if the map aᵢ ↦ bᵢ is a **partial isomorphism** — it preserves all atomic relations and their negations in the signature. If the map fails (some relation holds of aᵢ's but not the corresponding bⱼ's), Spoiler wins. Spoiler's goal is to force a failure; Duplicator's goal is to always respond so no failure occurs.

The fundamental theorem connects the game to logic: **Duplicator has a winning strategy in EF_n(A, B) if and only if A ≡_n B** — that is, A and B agree on all first-order sentences of quantifier depth at most n. More rounds correspond to richer logical sentences. If Duplicator wins for all n, then A ≡ B (full elementary equivalence). This converts an infinite logical question into a sequence of finite games.

The power of this tool appears in **inexpressibility proofs**. Suppose you want to show that first-order logic cannot express "the domain has an even number of elements." You need to exhibit two structures, one of even size and one of odd size, such that Duplicator wins EF_n for all n. Take A = {1,...,2n+1} and B = {1,...,2n+2} — structures of sizes 2n+1 and 2n+2 respectively. Duplicator's strategy: whenever Spoiler picks an element, respond with any element not yet chosen in the other structure (which is always possible since both structures are large). After n rounds, the partial map is an isomorphism (both are linear orders with the same relative ordering among selected elements). Duplicator wins, so no sentence of depth n can distinguish even from odd domains. Since n was arbitrary, finiteness and parity are inexpressible in first-order logic. The game transforms what would otherwise be an unwieldy infinitary argument into a clean, constructive strategy.
