---
id: bayesian-games-incomplete-info
title: Bayesian Games and Incomplete Information
domain: economics
course: advanced-microeconomics
prerequisites:
- id: nash-equilibrium-microeconomics
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
- id: bayes-theorem
  type: soft
- id: conditional-probability
  type: soft
- id: bayes-theorem-and-inference
  type: hard
- id: conditional-probability-fundamentals
  type: hard
builds-toward:
- perfect-bayesian-equilibrium
- mechanism-design-basics
tags:
- game-theory
- information-asymmetry
- types
stage: expert
status: draft
---

# Bayesian Games and Incomplete Information

## Core Idea
Bayesian games model strategic situations where players have incomplete information about each other's payoffs or types. Players have private types drawn from a common prior distribution, and each player's strategy is conditioned on their type. Bayesian Nash equilibrium is a strategy profile where each player's type-contingent strategy is optimal given beliefs about others' types.

## Questions

```yaml
- question: "In a sealed-bid auction where each bidder has a private valuation, how does a bidder determine their optimal bid under Bayesian Nash equilibrium?"
  type: multiple-choice
  options:
    - "They bid their true value, since they have no information about rivals"
    - "They bid the same amount as they would in a complete-information Nash equilibrium"
    - "They choose a bid that is a best response for their valuation type, given the probability distribution of rivals' types and those rivals' type-contingent bidding strategies"
    - "They bid zero, since uncertainty makes any positive bid potentially unprofitable"
  answer: 2
  explanation: "In a Bayesian game, a strategy is a type-contingent plan — a function mapping one's own type (valuation) to an action (bid). BNE requires that each type maximizes expected payoff given beliefs about others' types, not given a single fixed opponent action. A bidder doesn't know the rival's exact value, but they know its distribution (the common prior) and can compute the optimal bid as a function of their own value. This is fundamentally different from complete-information Nash equilibrium, where all payoffs are common knowledge."

- question: "What distinguishes a strategy in a Bayesian game from a strategy in a standard Nash equilibrium game?"
  type: multiple-choice
  options:
    - "Bayesian strategies require players to randomize over all actions simultaneously, while Nash strategies may be pure"
    - "In a Bayesian game, a strategy is a function mapping each possible type to an action, rather than a single action or probability distribution over actions"
    - "Bayesian strategies are updated using posterior beliefs after observing others' actions, while Nash strategies are fixed"
    - "There is no substantive difference — a Bayesian game just adds a dummy player called Nature"
  answer: 1
  explanation: "This is the central conceptual shift. In a standard game, a strategy specifies what to do (possibly with randomization). In a Bayesian game, a strategy specifies what to do *for each type you might be* — a complete contingent plan covering every private-information scenario. Player 1 must plan: 'If my type is low-cost, I'll do X; if high-cost, I'll do Y.' This type-contingency is what makes Bayesian games tractable: equilibrium is a fixed point in the space of type-contingent strategies, not just action profiles."

- question: "In a Bayesian game, all players share a common prior distribution over the possible type space, even though each player observes only their own realized type."
  type: true-false
  answer: true
  explanation: "The common prior is the defining modeling assumption introduced by Harsanyi. All players agree on the probability distribution from which types are drawn — they may not know each other's realizations, but they agree on the statistical structure. This assumption is what makes expected-payoff maximization tractable: each player can compute E[payoff | own type] by integrating over others' type distributions using the shared prior. Without a common prior, players might disagree about the distribution itself, creating infinite regress in higher-order beliefs."

- question: "Bayesian Nash equilibrium requires that each player's strategy maximizes their payoff against every possible realization of their opponents' types simultaneously."
  type: true-false
  answer: false
  explanation: "BNE requires each type's strategy to maximize *expected* payoff, where the expectation is taken over the distribution of opponents' types (using the common prior). A strategy does not need to be a best response against every individual type realization — only against the probability-weighted distribution. Requiring a best response against every realization would be a much stronger condition (something like a dominant strategy), which would rarely hold. The expected-payoff requirement is what makes BNE achievable in settings with genuine uncertainty."

- question: "Why does the common prior assumption transform incomplete information into a tractable strategic problem, and what would game-theoretic analysis look like without it?"
  type: short-answer
  answer: "With a common prior, all players agree on which type distributions are likely, enabling each to compute expected payoffs by integrating over the shared distribution. Equilibrium becomes a fixed-point problem in type-contingent strategies — solvable with standard tools. Without a common prior, players might disagree about the distribution of types, leading to disagreements about the distribution of opponents' beliefs, beliefs about beliefs, and so on — an infinite regress of higher-order uncertainty. This regress makes equilibrium analysis intractable and undermines the basic modeling framework. The common prior collapses all this into a single shared probability model, making Bayesian games as tractable as standard Nash games."
  explanation: "The common prior assumption is powerful but controversial. Real agents in novel or adversarial settings may genuinely not agree on the distribution of types (e.g., arms negotiations between countries with fundamentally different intelligence). Robust mechanism design and ambiguity theory try to handle settings where the prior is itself uncertain or contested."
```

## Explainer

In the standard games you studied when learning Nash equilibrium, every player knows the full structure of the game — who the players are, what actions are available, and what payoffs result from each outcome. But real strategic situations are rarely so transparent. A firm entering a market does not know its rival's cost structure. A bidder at an auction does not know how much others value the item. A country negotiating a treaty does not know the other side's true resolve. **Bayesian games** extend game theory to handle exactly this kind of uncertainty.

The key modeling innovation is the concept of a **type**. Each player has a type that determines their payoffs, and this type is private information — known to the player but not to others. Before the game begins, nature draws each player's type from a probability distribution called the **common prior**. All players know this prior distribution (they agree on the statistical structure of uncertainty), but each player observes only their own realized type. So when Player 1 is deciding what to do, they know their own type but must form beliefs about Player 2's type using Bayes' theorem and the common prior — exactly the probabilistic reasoning you developed in your prerequisites.

A **strategy** in a Bayesian game is no longer a single action — it is a complete contingent plan that specifies an action for every possible type a player could be. Think of it as a function mapping types to actions. Player 1's strategy says: "If I'm the low-cost type, I'll do X; if I'm the high-cost type, I'll do Y." The solution concept, **Bayesian Nash equilibrium (BNE)**, requires that every type of every player is playing a best response, given their beliefs about others' type-contingent strategies. Each type maximizes their expected payoff, where the expectation is taken over the possible types of the other players, weighted by the prior.

Consider a concrete example: two firms simultaneously choosing whether to enter a market, where each firm's profitability depends on a cost parameter only it knows. A low-cost firm might enter regardless of what the other does, while a high-cost firm enters only if it believes the other is likely to stay out. In BNE, each firm's entry decision for each cost type must be optimal given the probability distribution over the rival's cost type and the rival's type-contingent entry strategy. The equilibrium captures the interplay of private information and strategic reasoning — each player's action reflects both what they know about themselves and what they can infer about others.

Bayesian games are the foundation for nearly everything in information economics. Auctions, bargaining under uncertainty, signaling, mechanism design, and the analysis of markets with asymmetric information all build on this framework. The common prior assumption — that players agree on the distribution of types even if they don't observe each other's realizations — is both the framework's great simplifying power and its most debated feature. It transforms a problem of radical uncertainty into a tractable probabilistic calculation, making equilibrium analysis possible even when players operate in the dark about each other's true characteristics.
