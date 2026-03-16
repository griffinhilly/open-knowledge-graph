---
id: bayesian-games-strategy
title: Bayesian Games and Information Uncertainty
domain: economics
course: microeconomics
prerequisites:
- id: bayesian-games
  type: hard
builds-toward:
- signaling-in-markets
- screening-mechanism-design
tags:
- game theory
- information
- Bayesian equilibrium
stage: abstract-reasoning
status: draft
---

# Bayesian Games and Information Uncertainty

## Core Idea
Bayesian games model incomplete information: players have private information (types) drawn from a distribution. Bayesian Nash equilibrium is a strategy profile for each type where no type wants to deviate given beliefs about others' types. The revelation principle shows that any equilibrium outcome can be achieved through a direct mechanism where players report types truthfully. Applications include auctions, signaling, and insurance markets.

## Explainer

From your prerequisite work on Bayesian games, you know that a **type** encodes the private information a player holds — their valuation for a good, their cost of production, their risk tolerance. In a Bayesian game, each player knows their own type but only has a probability distribution over others' types. The strategic problem is therefore not just "what should I do given what others will do?" but "what should each possible version of me do, given what each possible version of them will do?" This layered uncertainty is what distinguishes Bayesian games from standard Nash games.

A **Bayesian Nash equilibrium** (BNE) is a strategy for each type of each player such that every type is choosing a best response given their beliefs about the type distribution of others. Think of it as Nash equilibrium applied to an expanded game in which the players are not individuals but type-contingent strategies. In a sealed-bid auction, for example, your strategy is a bidding function: a rule mapping every possible valuation you could have to a bid. Equilibrium requires that the bid you'd submit at any given valuation is optimal given that your opponent is also following their equilibrium bidding function.

The **revelation principle** is the deep result that ties mechanism design together. It says: for any BNE of any mechanism — however complicated or indirect — there exists a direct mechanism (where each player simply reports their type) with a truthful BNE that produces the same outcome. This is powerful because it lets a designer search over only the space of direct, incentive-compatible mechanisms rather than the much larger space of all possible game formats. The key condition is **incentive compatibility**: each type must prefer to report truthfully over lying, because the mechanism is designed so that no misreport improves expected payoff.

The practical payoff appears in auction theory and insurance design. In a first-price sealed-bid auction, bidders shade their bids below their true valuation — the equilibrium bidding function balances the gain from winning at a lower price against the increased risk of losing. In contrast, a second-price (Vickrey) auction is truthfully incentive-compatible: your dominant strategy is to bid your true value regardless of what others do, because your bid only determines whether you win, not what you pay. Both are applications of BNE reasoning to mechanisms with private types. In insurance markets, an insurer who cannot observe risk type must design contracts that separate high-risk and low-risk customers through self-selection — a direct application of the revelation principle to real market design.
