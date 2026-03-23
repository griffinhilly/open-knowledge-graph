---
id: bayesian-games-and-incomplete-information
title: Bayesian Games and Incomplete Information
domain: economics
course: advanced-microeconomics
prerequisites:
- id: strategic-form-games
  type: hard
- id: bayes-theorem
  type: hard
builds-toward:
- signaling-games-and-pooling-separating
- mechanism-design-and-vickrey-clarke-groves
tags:
- game-theory
- information-asymmetry
stage: expert
status: draft
---

# Bayesian Games and Incomplete Information

## Core Idea
Bayesian games model incomplete information: players have private types drawn from a distribution, known only to themselves. A Bayesian Nash equilibrium specifies each type's strategy such that no type wants to deviate given beliefs about other types. Harsanyi's representation embeds incomplete-information games as perfect-information games with an exogenous first move by Nature assigning types.

## Questions

```yaml
- question: "In a Bayesian Nash equilibrium, each player's strategy is a best response to what?"
  type: multiple-choice
  options:
    - "The strategy of the worst-case opponent type, to guarantee a minimum payoff"
    - "The strategy of the most likely opponent type, ignoring low-probability types"
    - "A probability distribution over all possible opponent types, weighted by their prior probabilities"
    - "Their own private type only, since other players' types are unobservable"
  answer: 2
  explanation: "This is the defining feature of Bayesian Nash equilibrium that distinguishes it from standard Nash equilibrium. Because you don't know your opponent's type, you must choose a strategy that is optimal on average across all possible opponent types, weighted by their prior probabilities. You are effectively playing against a probability-weighted mixture of all opponent types simultaneously. Options A and B are wrong because they ignore portions of the type distribution; option D is wrong because your best response must account for what different opponent types would do."

- question: "A seller does not know a buyer's willingness to pay for a used car. Harsanyi's approach to modeling this situation involves:"
  type: multiple-choice
  options:
    - "Assuming both players know the payoff matrix and using standard Nash equilibrium directly"
    - "Introducing Nature as a player who assigns buyer types from a commonly known prior, converting incomplete information to imperfect information"
    - "Eliminating the buyer's private information through mechanism design before solving the game"
    - "Having the buyer and seller negotiate a common prior before the game begins"
  answer: 1
  explanation: "Harsanyi's key trick is to introduce Nature as a first mover who assigns types according to a common prior distribution. The seller doesn't know which type Nature assigned the buyer, but both parties know the distribution. This transforms 'I don't know the payoff structure' (incomplete information — hard to analyze) into 'I didn't observe one of Nature's moves' (imperfect information — tractable with standard game theory tools). The common prior ensures there is shared probabilistic knowledge even when individual types are private."

- question: "The Harsanyi transformation converts a game of incomplete information into a game of imperfect information by introducing Nature as a player who assigns types according to a commonly known prior distribution."
  type: true-false
  answer: true
  explanation: "This is the core technical insight of Harsanyi's approach. 'Incomplete information' (players don't know the payoff structure) is conceptually distinct from 'imperfect information' (players don't observe some moves), and only the latter has a well-established solution concept. By having Nature assign types before the game begins, Harsanyi embeds the missing payoff information as an unobserved move in an otherwise standard extensive-form game, making the Bayesian Nash equilibrium concept applicable."

- question: "In a Bayesian Nash equilibrium, a player's strategy can depend only on their own private type, not on beliefs about the distribution of other players' types."
  type: true-false
  answer: false
  explanation: "A BNE strategy must be a best response given beliefs about other players' types. Since you cannot observe your opponent's type, your optimal strategy depends critically on what you believe the distribution of their types to be — the prior (and any updates from observable signals). For example, a bidding strategy in an auction must account for the probability distribution of rival valuations. Ignoring that distribution and acting only on your own type would typically not be optimal."

- question: "What is the conceptual problem with incomplete-information games that Harsanyi's model solves, and how does his solution work?"
  type: short-answer
  answer: "The problem is that 'incomplete information' — where players don't know the payoff structure itself — resists standard game-theoretic analysis, because players can't even compute best responses without knowing what payoffs are at stake. Harsanyi solved this by reframing incomplete information as imperfect information: he introduced a fictional player, Nature, who moves first and randomly assigns each player a private type from a commonly known prior distribution. After Nature's move, each player knows their own type but not others' types. Now the game is a standard extensive-form game with an unobserved move, and players can use Bayes' theorem to update beliefs and compute best responses against the distribution of possible opponent types. The Bayesian Nash equilibrium is the resulting solution concept."
  explanation: "The elegance of Harsanyi's contribution is that it makes incomplete-information games tractable without eliminating the uncertainty — players still don't know each other's types. Instead, it makes the uncertainty precise by specifying a common prior, turning a vague 'I don't know the game' into a well-defined probability problem that can be solved with standard tools."
```

## Explainer

In the strategic-form games you have already studied, every player knows the payoff matrix — who values what, and how much. But real strategic interactions rarely work that way. A seller may not know how much a buyer is willing to pay. A firm entering a market may not know whether the incumbent has low costs or high costs. A bidder in an auction does not know rival valuations. **Bayesian games** extend game theory to handle this pervasive uncertainty by giving each player a private **type** that determines their payoffs, and that other players can only guess at through probability distributions.

The key modeling trick, due to John Harsanyi, converts incomplete information into imperfect information. Instead of saying "Player 1 doesn't know Player 2's payoffs," we introduce a fictional player called **Nature** who moves first, randomly assigning each player a type according to a commonly known prior distribution. After Nature's move, each player observes their own type but not the types of others. This transforms an intractable problem — how do you strategize when you don't even know the game? — into a well-defined extensive-form game where you simply don't observe one of Nature's moves. You already know how to handle that from Bayes' theorem: update your beliefs given what you observe.

A **Bayesian Nash equilibrium** (BNE) specifies a strategy for every possible type of every player, such that each type's strategy is a best response given their beliefs about the distribution of other players' types. The critical shift from standard Nash equilibrium is that your strategy must be optimal not against a known opponent, but against a probability distribution over opponent types. Think of it as playing against a weighted average of all possible opponents simultaneously. If you are a high-cost firm choosing whether to enter a market, you must weigh your action against the probability that the incumbent is aggressive (low-cost) versus accommodating (high-cost), and your equilibrium strategy must be optimal across that entire distribution.

This framework is the foundation for nearly everything in information economics. Auction theory models bidders as having private value types. Signaling and screening models (which this topic builds toward) ask how informed players can credibly reveal — or strategically conceal — their types. Mechanism design asks how to structure the rules of a game so that players' equilibrium behavior in the Bayesian game achieves a desired outcome. Without the Bayesian game framework, none of these fields would have a rigorous strategic foundation, because they all depend on modeling what happens when players know things that others do not.
