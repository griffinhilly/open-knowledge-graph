---
id: screening-mechanism-design
title: Screening and Optimal Mechanism Design
domain: economics
course: microeconomics
prerequisites:
- id: mechanism-design-basics
  type: hard
tags:
- mechanism design
- information asymmetry
- screening
stage: abstract-reasoning
status: draft
---

# Screening and Optimal Mechanism Design

## Core Idea
When the uninformed party designs a mechanism to induce revelation, they use screening: offering contracts (menus) where different types self-select. Incentive-compatible contracts make truth-telling optimal for each type. Monotonicity and single-crossing conditions ensure separating equilibrium. Applications include insurance contracts (with deductible menus separating risk types), wage schedules (separating ability types), and auctions (revealing bidder values). Mechanism design seeks efficiency-incentive tradeoffs.

## Explainer

Your prerequisite on mechanism design basics established that the designer of a mechanism can harness the **revelation principle**: rather than thinking about all the clever ways agents might misreport or game the system, it suffices to look for **direct mechanisms** where telling the truth is each agent's optimal strategy. Screening takes this insight and asks a specific question: when agents have private information about their own type (high-risk vs. low-risk, high-ability vs. low-ability, high-value vs. low-value), how can the uninformed principal design a *menu* of contracts that makes different types voluntarily sort themselves?

The core tool is the **incentive compatibility (IC)** constraint: each type must prefer the contract designed for them over any contract designed for another type. Alongside IC sits the **participation (IR) constraint**: each type must prefer their contract to walking away entirely. The principal maximizes their own objective (profit, efficiency, revenue) subject to both sets of constraints. The key insight is that you typically cannot make every type equally happy — the high type always has the *option* of pretending to be low type and taking the low-type contract. To deter this, the principal must give the high type an **information rent**: extra surplus that makes it not worth mimicking the low type. This rent is the direct cost of private information.

The **single-crossing condition** is what makes clean separation possible. It says that the indifference curves of different types cross only once in the (contract, price) space — or equivalently, high types value quality more than low types do, in a way that cannot reverse. When single-crossing holds, separating equilibria are monotone: high types get higher quantity (or coverage, or effort) than low types. This monotonicity allows the designer to simplify from a combinatorial problem (all possible contracts) to a one-dimensional ordering problem. Violating single-crossing — types that "flip" relative valuations at different quality levels — causes pooling or breakdown of separation.

Insurance deductibles are the canonical illustration. An insurer offers two policies: a full-coverage plan at a high premium, and a partial-coverage plan (high deductible) at a low premium. High-risk customers (who expect to make frequent claims) strongly prefer full coverage and will pay up for it. Low-risk customers find the deductible plan acceptable because they rarely claim anyway — the premium savings outweigh the deductible risk. Each type self-selects into their designed contract without the insurer ever observing their risk type. The inefficiency is that low-risk customers get less insurance than they would receive under full information — the insurer must "distort" the low-risk contract downward to prevent high-risk types from mimicking it. This downward distortion for all but the highest type is the general signature of screening models: the top type gets the efficient contract; everyone else gets a distorted contract that discourages mimicry from above.
