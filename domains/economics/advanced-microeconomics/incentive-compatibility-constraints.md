---
id: incentive-compatibility-constraints
title: Incentive Compatibility and Individual Rationality
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games-and-incomplete-information
  type: hard
- id: quasi-linear-preferences
  type: soft
builds-toward:
- moral-hazard-principal-agent
- mechanism-design-and-vickrey-clarke-groves
tags:
- contract-theory
- mechanism-design
stage: advanced
status: draft
---

# Incentive Compatibility and Individual Rationality

## Core Idea
Incentive compatibility requires that each agent's optimal action is truth-telling (or the action chosen). Individual rationality requires agents accept the contract (participate). In contract design, these constraints limit efficiency: the planner must offer rents to induce truthful reporting or effort, creating information rents that reduce total surplus. The tradeoff between incentives and efficiency is fundamental to contract theory.

## Explainer

Imagine you are an insurance company designing a health plan, and your customers know more about their own health risks than you do. You would like each customer to choose the plan suited to their actual risk level — healthy people pick the low-coverage plan, sick people pick the high-coverage plan. But sick people might prefer the cheaper low-coverage plan if it saves them money upfront, and healthy people might claim to be sick to get extra coverage at a subsidized rate. The challenge is designing a menu of contracts where every type of customer voluntarily selects the option intended for them. This is the problem that **incentive compatibility** constraints address.

Formally, an **incentive compatibility (IC) constraint** says that each agent must weakly prefer the outcome designed for their true type over the outcome designed for any other type. If you are a high-risk customer, the contract meant for high-risk people must give you at least as much utility as pretending to be low-risk would. An **individual rationality (IR) constraint** (also called a participation constraint) says that each agent must prefer participating in the mechanism to their outside option — walking away entirely. Together, IC and IR define the feasible set of contracts: any contract design that violates IC will be gamed by some agents lying about their type, and any design that violates IR will be rejected outright.

The deep insight from your study of **Bayesian games and incomplete information** is that these constraints have real costs. In a world of complete information, the designer could simply assign the efficient outcome to each type. But with private information, the designer must make it in each agent's self-interest to reveal their type truthfully, and this typically requires leaving **information rents** — extra surplus that well-informed agents capture precisely because they could profitably misrepresent themselves. High-value buyers in an auction get rents because they could pretend to be low-value. Productive workers get rents because they could shirk. These rents are the price of truthful revelation.

The tradeoff between efficiency and information rents shapes virtually every real-world contract and institution. Tax authorities cannot observe taxpayers' true incomes, so they must design tax schedules where honest reporting is incentive-compatible — this is why optimal income taxes involve distortions away from the first-best. Employers cannot observe workers' effort directly, so they use performance pay that satisfies IC for effort provision. With **quasi-linear preferences** (which you may have studied), the analysis simplifies considerably because the IC constraints reduce to conditions on the allocation alone, independent of baseline wealth, making the mathematical characterization of optimal mechanisms much cleaner. But the fundamental lesson holds regardless of preference structure: whenever one party has private information, the other party must sacrifice some surplus to elicit truthful behavior, and the optimal mechanism balances this information cost against allocative efficiency.
