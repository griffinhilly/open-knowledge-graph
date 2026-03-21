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
stage: advanced
status: draft
---

# General Equilibrium and Existence of Walrasian Equilibrium

## Core Idea
A Walrasian equilibrium is a price vector where quantity demanded equals quantity supplied in all markets. Existence requires convex preferences, continuous demand, and market-clearing at some price vector. The fixed-point theorems (Brouwer, Kakutani) guarantee existence under these conditions. Equilibrium prices convey information allowing decentralized trade without central planning. Uniqueness and stability (tatonnement convergence) depend on demand elasticities and substitutability.

## Questions

```yaml
- question: "An economist uses Kakutani's fixed-point theorem to prove that a Walrasian equilibrium exists in a particular economy. What exactly has been established?"
  type: multiple-choice
  options:
    - "That the tâtonnement price-adjustment process will converge to the equilibrium from any initial prices"
    - "That there exists at least one price vector at which quantity supplied equals quantity demanded in every market simultaneously"
    - "That the equilibrium price vector is unique and can be computed by solving a system of equations"
    - "That the equilibrium allocation is Pareto efficient and cannot be improved by reallocation"
  answer: 1
  explanation: "The fixed-point theorem guarantees existence — the existence of at least one solution — and nothing more. It does not guarantee uniqueness (multiple equilibria are possible), stability (tâtonnement may not converge), or efficiency (that requires the First Welfare Theorem separately). The confusion between 'a solution exists' and 'the adjustment process finds it' is the central misconception to avoid."

- question: "Which condition on consumer preferences is most critical for applying a fixed-point theorem to prove that Walrasian equilibrium exists?"
  type: multiple-choice
  options:
    - "Preferences must be monotone — consumers always prefer more of every good"
    - "Preferences must be convex — consumers prefer averages to extremes — ensuring demand correspondences are convex-valued rather than jumping discontinuously"
    - "Preferences must be separable across goods so that demand in each market can be analyzed independently"
    - "There must be a finite number of consumers, so that aggregate demand is well-defined"
  answer: 1
  explanation: "Convexity is the key substantive economic assumption. Non-convex preferences can produce demand correspondences that jump discontinuously — for example, a consumer who switches abruptly from buying only good A to only good B as their relative price changes. Such discontinuities can prevent the existence of a fixed point. Convex preferences ensure that demand is convex-valued (or at least upper hemicontinuous), which is exactly the condition Kakutani's theorem requires. Monotonicity is often assumed but is not the critical assumption for existence."

- question: "Proving that a Walrasian equilibrium exists using a fixed-point theorem also establishes that the tâtonnement price-adjustment process will converge to that equilibrium from any initial price vector."
  type: true-false
  answer: false
  explanation: "Existence and stability are entirely separate questions. A fixed-point theorem proves that at least one equilibrium price vector exists — a mathematical property of the demand function. Whether an iterative adjustment process (like tâtonnement) will actually reach that equilibrium depends on global stability conditions, most notably the gross substitutes condition. Without gross substitutes, the tâtonnement process can cycle or diverge even when an equilibrium exists. The existence proof says a solution is there; it says nothing about how to find it."

- question: "An economy satisfying all the conditions needed for Walrasian equilibrium existence may have multiple distinct equilibrium price vectors."
  type: true-false
  answer: true
  explanation: "Existence guarantees at least one equilibrium, not uniqueness. Multiple equilibria are entirely consistent with the convexity and continuity assumptions used in the fixed-point argument. Uniqueness is a separate, stricter condition that requires additional assumptions (such as the gross substitutes condition or strong restrictions on income effects). The possibility of multiple equilibria creates fundamental challenges for comparative statics: if a policy shifts the economy to a different equilibrium entirely, standard single-equilibrium analysis breaks down."

- question: "Explain why proving the existence of a Walrasian equilibrium requires a fixed-point theorem, and which economic assumption about preferences makes demand well-behaved enough to apply the theorem."
  type: short-answer
  answer: "A Walrasian equilibrium is a price vector p* such that excess demand z(p*) = 0. Finding p* means showing that a particular mapping — which adjusts prices upward where demand exceeds supply and downward where supply exceeds demand — has a fixed point. For Brouwer's or Kakutani's theorem to apply, this mapping must be continuous (or upper hemicontinuous for correspondences) on a compact convex set. The key economic assumption is convexity of preferences: it ensures demand correspondences are convex-valued and upper hemicontinuous rather than jumping discontinuously. Without convexity, demand can jump, the mapping is not continuous, and the theorem cannot be applied — and in fact equilibria may not exist. Prices are normalized to the unit simplex (a compact convex set) to satisfy the compactness requirement."
  explanation: "The fixed-point approach is essentially a non-constructive existence proof: it says 'a solution must exist' without providing an algorithm to compute it. This is why existence, uniqueness, and stability are three separate questions requiring three separate arguments, even though all three are often conflated in casual discussions of market equilibrium."
```

## Explainer

Your prerequisite work on general equilibrium established the concept of simultaneous market-clearing across all markets at once. The existence question now asks something more foundational: is there *guaranteed* to be any price vector at which all markets clear? This is not obvious. With thousands of goods and millions of consumers, there is no reason to assume that a solution must exist — unless we can prove it mathematically.

The proof strategy uses **fixed-point theorems**. Imagine a mapping that takes any price vector and returns a new one — the prices implied by the excess demands at those prices. If demand exceeds supply, the price should rise; if supply exceeds demand, it should fall. Walras's **tâtonnement** process is one version of this: an auctioneer calls out prices, observes excess demands, adjusts, and repeats. The question is whether this process converges to a fixed point — a price vector that maps to itself, meaning markets clear. **Brouwer's fixed-point theorem** (for continuous functions on compact convex sets) and **Kakutani's theorem** (for correspondences, needed when demand is not single-valued) guarantee such a fixed point exists if the demand function satisfies certain regularity conditions.

The key conditions are: preferences must be **convex** (so demand correspondences are convex-valued, not just single points), demand must be **continuous** in prices, and the price simplex must be compact. Convexity of preferences is the substantive economic assumption — it ensures consumers spread consumption across goods rather than concentrating on corners, which keeps demand well-behaved. Together these allow you to normalize prices to live on a compact set (the unit simplex), construct a continuous mapping, and invoke the fixed-point theorem to assert that at least one equilibrium exists.

Existence is distinct from two other questions that are often conflated with it. **Uniqueness** asks whether there is only one equilibrium price vector. In general, there is not — multiple equilibria are possible, and this creates significant challenges for comparative statics. **Stability** asks whether tâtonnement actually converges to equilibrium from an arbitrary starting point. Stability depends on the **gross substitutes** condition: if raising the price of one good increases demand for all others, then the tâtonnement process is globally stable. Without gross substitutes, the process may cycle or diverge. The existence proof says *a* solution exists; it says nothing about whether markets can find it through decentralized price adjustment.
