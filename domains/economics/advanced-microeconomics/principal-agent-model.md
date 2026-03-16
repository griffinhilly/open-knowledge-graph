---
id: principal-agent-model
title: The Principal-Agent Model
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games
  type: hard
- id: constrained-optimization-lagrange
  type: soft
builds-toward:
- moral-hazard
- adverse-selection
tags:
- contract-theory
- delegation
- incentives
stage: abstract-reasoning
status: draft
---

# The Principal-Agent Model

## Core Idea
The principal-agent model formalizes the problem of contracting when a principal hires an agent who has private information or unobservable actions. The principal designs a contract (payoff function) to maximize expected payoff subject to the agent's incentive and participation constraints. This framework encompasses moral hazard, adverse selection, and signaling.

## Explainer

The principal-agent model begins with a simple observation: much of economic life involves **delegation**. Shareholders hire managers. Patients rely on doctors. Voters elect politicians. In each case, one party (the **principal**) wants something done but depends on another party (the **agent**) to do it. The problem is that the agent has their own interests, which may not align with the principal's, and the agent typically knows something the principal does not — either about their own characteristics (adverse selection) or about their own actions (moral hazard). The principal-agent model provides a unified framework for analyzing how to design contracts that manage this tension.

The principal moves first by offering a **contract** — a mapping from observable variables to payments. The agent then decides whether to accept (the **participation constraint**) and, if they accept, what action to take or what information to reveal. The principal's design problem is constrained optimization: maximize expected payoff subject to the agent voluntarily participating and behaving as intended. From your work with Lagrangian methods and Bayesian games, you already have the mathematical machinery. The participation constraint ensures the agent gets at least their reservation utility. The **incentive compatibility constraint** ensures the agent finds it optimal to take the action (or reveal the information) the principal wants, given the contract terms.

What makes this framework powerful is its generality. When the hidden element is the agent's *action* (effort, care, diligence), you get **moral hazard** — the agent may shirk because effort is unobservable. The principal must tie pay to noisy outcomes to motivate effort, bearing a cost in risk. When the hidden element is the agent's *type* (ability, risk level, cost structure), you get **adverse selection** — the principal cannot distinguish high types from low types and must design contract menus or accept pooling. When the informed party moves first to reveal their type, you get **signaling**; when the uninformed party moves first to sort types, you get **screening**. All four phenomena — moral hazard, adverse selection, signaling, and screening — are special cases of the same principal-agent structure with different information assumptions.

The model's central lesson is that **information asymmetry has real costs**. In a world of perfect information, the principal could write a complete contract specifying exactly what the agent should do in every state and paying them accordingly — the **first-best**. With asymmetric information, the best achievable outcome (the **second-best**) is strictly worse. The gap between first-best and second-best is the cost of imperfect information, and contract design is the art of minimizing that gap. This framework underpins everything from insurance design to executive compensation to government regulation, and it is the lens through which modern economics analyzes any situation where one person depends on another who knows more or whose actions are hard to observe.
