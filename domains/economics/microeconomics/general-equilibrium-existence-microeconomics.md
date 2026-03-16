---
id: general-equilibrium-existence-microeconomics
title: General Equilibrium and Existence of Walrasian Equilibrium
domain: economics
course: microeconomics
prerequisites:
- id: general-equilibrium-existence
  type: hard
tags:
- general equilibrium
- existence
- Walrasian
stage: abstract-reasoning
status: draft
---

# General Equilibrium and Existence of Walrasian Equilibrium

## Core Idea
A Walrasian equilibrium is a price vector where quantity demanded equals quantity supplied in all markets. Existence requires convex preferences, continuous demand, and market-clearing at some price vector. The fixed-point theorems (Brouwer, Kakutani) guarantee existence under these conditions. Equilibrium prices convey information allowing decentralized trade without central planning. Uniqueness and stability (tatonnement convergence) depend on demand elasticities and substitutability.

## Explainer

Your prerequisite work on general equilibrium established the concept of simultaneous market-clearing across all markets at once. The existence question now asks something more foundational: is there *guaranteed* to be any price vector at which all markets clear? This is not obvious. With thousands of goods and millions of consumers, there is no reason to assume that a solution must exist — unless we can prove it mathematically.

The proof strategy uses **fixed-point theorems**. Imagine a mapping that takes any price vector and returns a new one — the prices implied by the excess demands at those prices. If demand exceeds supply, the price should rise; if supply exceeds demand, it should fall. Walras's **tâtonnement** process is one version of this: an auctioneer calls out prices, observes excess demands, adjusts, and repeats. The question is whether this process converges to a fixed point — a price vector that maps to itself, meaning markets clear. **Brouwer's fixed-point theorem** (for continuous functions on compact convex sets) and **Kakutani's theorem** (for correspondences, needed when demand is not single-valued) guarantee such a fixed point exists if the demand function satisfies certain regularity conditions.

The key conditions are: preferences must be **convex** (so demand correspondences are convex-valued, not just single points), demand must be **continuous** in prices, and the price simplex must be compact. Convexity of preferences is the substantive economic assumption — it ensures consumers spread consumption across goods rather than concentrating on corners, which keeps demand well-behaved. Together these allow you to normalize prices to live on a compact set (the unit simplex), construct a continuous mapping, and invoke the fixed-point theorem to assert that at least one equilibrium exists.

Existence is distinct from two other questions that are often conflated with it. **Uniqueness** asks whether there is only one equilibrium price vector. In general, there is not — multiple equilibria are possible, and this creates significant challenges for comparative statics. **Stability** asks whether tâtonnement actually converges to equilibrium from an arbitrary starting point. Stability depends on the **gross substitutes** condition: if raising the price of one good increases demand for all others, then the tâtonnement process is globally stable. Without gross substitutes, the process may cycle or diverge. The existence proof says *a* solution exists; it says nothing about whether markets can find it through decentralized price adjustment.
