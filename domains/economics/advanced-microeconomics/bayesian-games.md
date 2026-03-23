---
id: bayesian-games
title: Bayesian Games (Games of Incomplete Information)
domain: economics
course: advanced-microeconomics
prerequisites:
- id: game-theory-basics-microeconomics
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
- id: bayes-theorem
  type: soft
builds-toward:
- perfect-bayesian-equilibrium
- mechanism-design-intro
tags:
- game-theory
- incomplete-information
- types
stage: expert
status: draft
---

# Bayesian Games (Games of Incomplete Information)

## Core Idea
A Bayesian game models situations where players have private information (types). Each player has a type from a set T_i, a payoff function u_i(a, t), and beliefs over others' types. A Bayesian Nash equilibrium is a strategy for each type such that each type's strategy maximizes expected payoff given beliefs. This framework unifies signaling, screening, and mechanism design.

## Questions

```yaml
- question: "In a Bayesian game, what is the distinction between a player's 'type' and their 'strategy'?"
  type: multiple-choice
  options:
    - "A type is the action a player chooses in the game; a strategy is their long-run plan across multiple games."
    - "A type is private information the player holds (such as their valuation or cost); a strategy is a function mapping each possible type to an action."
    - "A type is a player's role or identity; a strategy is their belief about what other players will do."
    - "Types and strategies are interchangeable — both describe what a player will do given their information."
  answer: 1
  explanation: "Type captures what a player privately knows (e.g., how much they value an item, their production cost, their risk tolerance). Strategy in a Bayesian game is a complete contingent plan: it specifies what action to take for every type the player might be. This is more complex than in complete-information games, where a strategy is just an action choice."

- question: "In a Bayesian Nash equilibrium, each player's optimal strategy requires knowing the actual types of all other players."
  type: true-false
  answer: false
  explanation: "Players do NOT observe other players' types — that is the whole point of incomplete information. Instead, each player maximizes their *expected* payoff, averaging over the possible types of others weighted by their prior beliefs. The equilibrium requires that each type's strategy be optimal given those beliefs, not given knowledge of actual types."

- question: "Describe a real-world situation that can be modeled as a Bayesian game and identify what 'types' represent in that context."
  type: short-answer
  answer: "A first-price sealed-bid auction is a canonical example. Each bidder is a player, and their type is their private valuation for the item being auctioned. Bidders choose how much to bid (their strategy) without knowing others' valuations. A Bayesian Nash equilibrium describes a bidding function — a rule mapping each valuation to a bid — such that no bidder can improve their expected payoff by deviating."
  explanation: "The auction example clearly illustrates the key features: private information (only you know your value), beliefs (you have a distribution over others' values), and strategies that are type-contingent (your bid depends on your value). Other examples include entry games with private costs, insurance markets with private risk levels, and bilateral trade with privately known gains from trade."
```

## Explainer

The game theory you encountered in introductory microeconomics assumed that all players know everything relevant — the payoffs, the strategies available, and crucially, who they are playing against. This is the **complete information** assumption, and it is often unrealistic. In most real strategic situations, you face uncertainty about the other party: Does the seller know something about this car that I don't? How much does my rival bidder value this contract? Is my opponent in negotiation a tough type or a soft type? Bayesian game theory is the framework for analyzing exactly these situations.

The central innovation is the concept of a **type**. A type is a bundle of private information that a player holds and others do not observe. In an auction, your type is your valuation for the item. In an insurance market, your type is your risk level. In a negotiation, your type might be your reservation price. Each player knows their own type but only has probabilistic beliefs about others' types — typically modeled as a common prior distribution that everyone agrees on (the Harsanyi assumption). When you play, you cannot condition on information you don't have; you must form expectations.

A **strategy** in a Bayesian game is therefore richer than in a standard game. It is a function from types to actions: "if I am type t, I will take action a(t)." A high-value bidder bids differently from a low-value bidder, so the equilibrium specifies a rule for every possible type, not a single action. A **Bayesian Nash equilibrium** is a profile of such strategies — one for each player — such that no type of any player can gain by deviating. Each type is best-responding given its beliefs about others' type distributions and the strategies those other types are playing.

Consider a first-price sealed-bid auction as a clean example. You must submit a bid without seeing anyone else's. Your type is your private value v. You know that others' values are drawn from some distribution (say, uniform on [0, 100]). The equilibrium bidding strategy — derivable from the expected payoff calculation — has you bid less than your true value (bid-shading), because winning at a price equal to your value earns zero profit. The precise amount to shade depends on the number of bidders and the distribution. This is a Bayesian Nash equilibrium: given that everyone follows the same bidding function, no single bidder can improve their expected payoff by deviating.

This framework is foundational for everything that follows: mechanism design asks how to structure rules to achieve outcomes when participants have private types; signaling models players actively trying to reveal or conceal their types; screening models the uninformed party trying to sort types through contract design. All of these are applications of the Bayesian game structure.
