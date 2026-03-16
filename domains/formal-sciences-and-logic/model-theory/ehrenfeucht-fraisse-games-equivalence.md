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

## Explainer

You know that two structures A and B are **elementarily equivalent** if they satisfy exactly the same first-order sentences. But how do you *prove* elementary equivalence — especially for infinite structures that look superficially different? Verifying all sentences directly is impossible. The **Ehrenfeucht-Fraïssé game** replaces this with a concrete, finitary game that encodes precisely as much logical information as needed.

The game EF_n(A, B) is played over n rounds between two players: **Spoiler** (Player I) and **Duplicator** (Player II). Each round, Spoiler picks an element from either A or B, and Duplicator responds with an element from the other structure. After n rounds, the players have jointly selected elements a₁,...,aₙ ∈ A and b₁,...,bₙ ∈ B. Duplicator wins the round-n game if the map aᵢ ↦ bᵢ is a **partial isomorphism** — it preserves all atomic relations and their negations in the signature. If the map fails (some relation holds of aᵢ's but not the corresponding bⱼ's), Spoiler wins. Spoiler's goal is to force a failure; Duplicator's goal is to always respond so no failure occurs.

The fundamental theorem connects the game to logic: **Duplicator has a winning strategy in EF_n(A, B) if and only if A ≡_n B** — that is, A and B agree on all first-order sentences of quantifier depth at most n. More rounds correspond to richer logical sentences. If Duplicator wins for all n, then A ≡ B (full elementary equivalence). This converts an infinite logical question into a sequence of finite games.

The power of this tool appears in **inexpressibility proofs**. Suppose you want to show that first-order logic cannot express "the domain has an even number of elements." You need to exhibit two structures, one of even size and one of odd size, such that Duplicator wins EF_n for all n. Take A = {1,...,2n+1} and B = {1,...,2n+2} — structures of sizes 2n+1 and 2n+2 respectively. Duplicator's strategy: whenever Spoiler picks an element, respond with any element not yet chosen in the other structure (which is always possible since both structures are large). After n rounds, the partial map is an isomorphism (both are linear orders with the same relative ordering among selected elements). Duplicator wins, so no sentence of depth n can distinguish even from odd domains. Since n was arbitrary, finiteness and parity are inexpressible in first-order logic. The game transforms what would otherwise be an unwieldy infinitary argument into a clean, constructive strategy.
