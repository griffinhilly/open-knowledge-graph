---
id: moral-hazard-monitoring
title: Moral Hazard and Incentive Contracting
domain: economics
course: advanced-microeconomics
prerequisites:
- id: nash-equilibrium-microeconomics
  type: hard
- id: profit-maximization-microeconomics
  type: hard
builds-toward:
- principal-agent-contracting
tags:
- contract-theory
- information-asymmetry
- incentives
stage: advanced
status: draft
---

# Moral Hazard and Incentive Contracting

## Core Idea
Moral hazard arises when one party (agent) can take unobserved actions affecting payoffs to another party (principal). The agent has incentive to shirk if effort is unobserved; the principal must design incentives (performance pay, profit-sharing, equity) to motivate effort. Optimal contracts balance incentive provision against risk-sharing given the agent's risk aversion.

## Explainer

From Nash equilibrium, you understand strategic interaction where each player optimizes given the other's strategy. From profit maximization, you understand how firms make optimal decisions. **Moral hazard** introduces a twist: what happens when one player's action is hidden from the other? The concept is straightforward — if your boss cannot see whether you are working hard or browsing the internet, you have a temptation to slack off. The deep question is how to design contracts that align incentives when effort is unobservable.

Consider a sales manager (principal) hiring a salesperson (agent). The salesperson can exert high effort (costly, leads to high sales with high probability) or low effort (easy, leads to low sales usually). The manager observes sales revenue but not effort directly. If the manager pays a flat salary, the salesperson has no reason to work hard — she receives the same pay regardless. If the manager pays purely on commission, effort is incentivized but the salesperson bears all the revenue risk, which is inefficient because some variation in sales comes from luck, not effort. The **optimal contract** lies somewhere between these extremes, trading off incentive power against risk exposure.

The formal model captures this tradeoff precisely. The agent chooses effort e to maximize expected utility of compensation minus the cost of effort. The **incentive compatibility constraint** requires that the compensation scheme makes high effort the agent's best response. The **participation constraint** requires that the agent prefers the contract to her outside option. The principal maximizes expected profit subject to both constraints. When the agent is risk-neutral, the solution is simple: sell the agent the firm (or equivalently, pay a franchise fee and let the agent keep all revenue). The agent then fully internalizes the consequences of effort, achieving the **first-best** outcome. But when the agent is risk-averse, full incentive provision requires exposing the agent to too much risk, so the optimal contract dampens incentives to provide insurance — a **second-best** outcome where some shirking occurs in equilibrium.

The gap between first-best and second-best is the **cost of moral hazard** — the efficiency loss from unobservable actions. This cost can be reduced through **monitoring** (making effort partially observable), **relative performance evaluation** (comparing the agent to peers to filter out common noise), or **repeated interactions** (using past performance to infer effort over time). Each of these mechanisms works by tightening the link between effort and measured performance, allowing the principal to provide stronger incentives without imposing as much risk. Understanding this tradeoff is foundational for analyzing employment contracts, insurance design, corporate governance, and any setting where one party's hidden actions affect another's welfare.
