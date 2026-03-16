---
id: adverse-selection-screening
title: Adverse Selection and Screening Mechanisms
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games-and-incomplete-information
  type: hard
- id: probability-theory
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
- id: constrained-optimization-lagrange
  type: soft
builds-toward:
- labor-market-signaling
- insurance-markets-and-selection
tags:
- contract-theory
- information-asymmetry
stage: advanced
status: draft
---

# Adverse Selection and Screening Mechanisms

## Core Idea
Adverse selection occurs when private information (type) is correlated with transaction value. Screening mechanisms—menus of contracts with different terms—allow the uninformed party to infer types and separate market participants. Self-selection constraints ensure each type prefers its intended contract. Screening reduces but does not eliminate efficiency loss from adverse selection.

## Explainer

From your study of Bayesian games and incomplete information, you know that players may hold private information that affects strategic outcomes. **Adverse selection** is what happens when this private information distorts market participation itself. The classic example is insurance: healthy people know they are low-risk and find high premiums unattractive, while sick people know they are high-risk and find the same premiums a bargain. If the insurer cannot distinguish types, the pool of buyers skews toward high-risk individuals — the selection of participants is adverse to the uninformed party. George Akerlof's "market for lemons" showed that in the extreme case, this unraveling can destroy the entire market.

**Screening** is the uninformed party's strategic response. Instead of offering a single contract and hoping for the best, the uninformed party offers a **menu of contracts** designed so that each type voluntarily selects the contract intended for them. Consider an insurance company offering two policies: a comprehensive plan with high premiums and low deductibles, and a basic plan with low premiums and high deductibles. High-risk individuals prefer the comprehensive plan because they expect to file many claims; low-risk individuals prefer the basic plan because they rarely need coverage. By designing the menu carefully, the insurer gets each type to **self-select** and reveal their private information through their choice.

The key technical constraints are **incentive compatibility** (each type must prefer the contract designed for it over any other contract in the menu) and **individual rationality** (each type must prefer participating to walking away). These constraints formalize what "designed carefully" means. Using the tools of constrained optimization you have studied, the screening problem becomes: maximize the uninformed party's payoff subject to incentive compatibility and participation constraints for every type. The solution typically involves **distorting** the contract offered to the low type — giving them less coverage or lower quality — to make their contract unattractive to the high type. The high type gets an efficient contract but pays a premium that extracts their information rent.

This distortion is the fundamental cost of adverse selection: efficiency is sacrificed to achieve separation. In a world of perfect information, both types would get efficient contracts. With screening, the high type does fine, but the low type receives a suboptimal deal. The gap between the first-best (full information) and second-best (screening) outcome represents the **information rent** — the price society pays for asymmetric information. This framework extends far beyond insurance: employers screening workers with probationary contracts, banks screening borrowers with collateral requirements, and airlines screening passengers with fare classes all follow exactly the same logic.
