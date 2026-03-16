---
id: incentive-compatibility
title: Incentive Compatibility
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games
  type: hard
builds-toward:
- mechanism-design-intro
- screening-contracts
tags:
- mechanism-design
- truthfulness
- incentives
stage: abstract-reasoning
status: draft
---

# Incentive Compatibility

## Core Idea
Incentive compatibility (IC) is a constraint in mechanism design: truth-telling must be optimal for each agent. Formal IC: for all types t_i, t_i', agent i weakly prefers reporting true type t_i over lying and reporting t_i'. Strong IC requires strict preference. IC is necessary for mechanisms to elicit honest information without monitoring.

## Explainer

From Bayesian games, you know that players often have private information — their own costs, valuations, or preferences — that others cannot observe. A natural follow-up question is: can we design rules (mechanisms) that get people to honestly reveal this private information? **Incentive compatibility** is the formal condition that makes this possible. A mechanism is incentive-compatible when every participant finds it in their own self-interest to report their true type, rather than misrepresenting it to gain an advantage.

Consider a concrete setting. A government wants to allocate a public contract to the firm that can deliver it most cheaply, but each firm privately knows its own cost. If the government simply asks firms to report their costs and awards the contract to the cheapest, every firm has an incentive to exaggerate — reporting higher costs to extract a larger payment. An incentive-compatible mechanism restructures the payments so that this lying is no longer profitable. The key insight is that the mechanism must make truthful reporting a **dominant strategy** (or at least a Bayesian-Nash equilibrium strategy): for every possible type a firm might be, and for every possible report by other firms, honesty must yield at least as high a payoff as any lie.

Formally, let each agent have a **type** t_i drawn from some distribution — this type captures their private information. The mechanism asks agents to report a type, then determines an allocation and transfers based on the reports. The IC constraint says: for agent i with true type t_i, the expected payoff from reporting t_i must be at least as large as the expected payoff from reporting any alternative type t_i'. **Bayesian incentive compatibility** (BIC) requires this in expectation over others' types; **dominant-strategy incentive compatibility** (DSIC) requires it for every possible realization of others' types. DSIC is stronger — it means honesty is optimal regardless of what anyone else does — while BIC only requires honesty to be optimal on average.

The concept has a remarkable structural implication. In many settings, incentive compatibility constrains the mechanism designer to leave **information rents** to agents with favorable private information. A low-cost firm, by being willing to truthfully reveal its efficiency, must be paid enough that it would not prefer to mimic a high-cost firm. These information rents are the price the designer pays for truthful revelation. This tradeoff between extracting surplus and maintaining honesty is central to auction design, regulation, taxation, and contract theory — wherever a principal must elicit information from better-informed agents. Incentive compatibility turns "how do we get people to tell the truth?" from a vague aspiration into a precise, solvable constraint.
