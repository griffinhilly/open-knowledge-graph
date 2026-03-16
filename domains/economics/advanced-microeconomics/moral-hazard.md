---
id: moral-hazard
title: Moral Hazard
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games
  type: hard
- id: principal-agent-model
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- screening-contracts
tags:
- contract-theory
- hidden-action
- incentives
stage: abstract-reasoning
status: draft
---

# Moral Hazard

## Core Idea
Moral hazard arises when an agent's actions are unobservable to the principal. The agent may shirk or take excessive risk because consequences are shared. Classic example: insurance reduces incentive to prevent loss. The principal must design contracts (e.g., deductibles, performance pay) to align incentives. Optimal contracts balance risk-sharing with incentives.

## How It's Best Learned
Analyze a simple principal-agent model with continuous effort. Solve for optimal contract. Compare to full-information benchmark to see efficiency loss from hidden action.

## Explainer

From the principal-agent model, you know the basic setup: one party (the principal) delegates a task to another (the agent), and their interests may not align. **Moral hazard** is the specific problem that arises when the agent's *actions* are hidden — the principal can observe the outcome but cannot verify whether the agent worked hard, cut corners, or took excessive risks. The term originally comes from insurance, where it described the tendency of insured people to be less careful, but the concept applies wherever effort or behavior is unobservable.

Consider a concrete example: a restaurant owner (principal) hires a manager (agent) to run the business. The owner can observe monthly revenue, but cannot monitor whether the manager is working diligently, networking to attract customers, and maintaining food quality — or whether the manager is coasting, leaving early, and cutting corners. Revenue depends on both the manager's effort and random factors (weather, local events, economic conditions). High effort makes good outcomes more likely, but does not guarantee them — and low effort does not guarantee bad outcomes either. This **randomness in the mapping from effort to outcome** is what makes moral hazard so difficult. The owner sees the result, not the cause.

If the owner could observe effort directly, the solution would be simple: pay for effort. Write a contract that says "work hard, get paid well; shirk, get fired." But with hidden action, the contract can only be conditioned on **observable outcomes** — revenue, profit, customer ratings. The principal must design a contract that gives the agent an incentive to exert effort even when no one is watching. This typically means making the agent's pay sensitive to outcomes: performance bonuses, commissions, stock options, or profit sharing. The agent bears some risk (their pay varies with outcomes they don't fully control), but this risk exposure is the price of providing incentives.

Here lies the fundamental tradeoff at the heart of moral hazard theory: **incentives versus risk-sharing**. If the agent is risk-averse (as most people are), the ideal risk-sharing arrangement would fully insure the agent — pay a flat salary regardless of outcomes. But a flat salary provides zero incentive to exert effort. Conversely, making the agent the full residual claimant (keeping all profits) provides maximal incentives but loads the agent with all the risk. The **optimal contract** balances these two forces, providing enough pay-for-performance to motivate effort while not exposing the risk-averse agent to so much volatility that they demand a huge risk premium. This optimal contract is always less efficient than what could be achieved if effort were observable — the **efficiency loss** from moral hazard is the cost of information asymmetry.

Moral hazard is pervasive in economic life. Insurance deductibles and copays exist to keep policyholders careful. CEO compensation packages tie pay to stock performance to align executive and shareholder interests. Loan covenants restrict borrower behavior to protect lenders. In each case, the contract designer faces the same problem: how to motivate unobservable good behavior through the structure of observable rewards and penalties. Understanding this problem — and the tradeoff between incentives and risk-sharing that constrains its solution — is essential for analyzing contracts, regulation, and institutional design throughout economics.
