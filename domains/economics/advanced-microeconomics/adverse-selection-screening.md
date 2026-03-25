---
id: adverse-selection-screening
title: Adverse Selection and Screening Mechanisms
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games
  type: hard
- id: probability-theory
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
- id: constrained-optimization-lagrange
  type: soft
- id: screening-and-self-selection
  type: soft
- id: pooling-separating-equilibrium
  type: soft
builds-toward:
- labor-market-signaling
- insurance-markets-and-selection
tags:
- contract-theory
- information-asymmetry
stage: expert
status: validated
---
# Adverse Selection and Screening Mechanisms

## Core Idea
Adverse selection occurs when private information (type) is correlated with transaction value. Screening mechanisms—menus of contracts with different terms—allow the uninformed party to infer types and separate market participants. Self-selection constraints ensure each type prefers its intended contract. Screening reduces but does not eliminate efficiency loss from adverse selection.

## Questions

```yaml
- question: "An insurance company wants to separate high-risk and low-risk customers. Which menu design achieves this through screening?"
  type: multiple-choice
  options:
    - "Offer both types the same actuarially fair contract — efficiency maximizes participation from all types"
    - "Offer only the high-risk contract and exclude low-risk customers who find it too expensive"
    - "Offer a comprehensive plan (high premium, low deductible) alongside a basic plan (low premium, high deductible), relying on self-selection"
    - "Ask customers to self-report their risk type and design contracts based on their answers"
  answer: 2
  explanation: "Screening works through incentive-compatible contract menus: high-risk customers prefer the comprehensive plan (they expect many claims, so low deductibles are valuable), while low-risk customers prefer the basic plan (they rarely claim, so low premiums dominate). Each type self-selects the contract designed for them, revealing private information through their choice. Option A fails because a single fair contract attracts mostly high-risk customers, causing adverse selection unraveling. Option D fails because self-reports are not incentive-compatible — high-risk customers would simply lie."

- question: "In a screening equilibrium, the low-type receives a distorted (inefficient) contract. Why is this distortion necessary?"
  type: multiple-choice
  options:
    - "Low-type customers are penalized for being less profitable to the insurer"
    - "The distortion makes the low-type contract unattractive to the high type, preventing the high type from mimicking it to avoid paying high premiums"
    - "Offering efficient contracts to both types would violate individual rationality constraints"
    - "Low types lack sufficient income to afford an efficient contract at actuarially fair prices"
  answer: 1
  explanation: "The distortion of the low-type contract is an incentive device, not a penalty. If the low-type contract were efficient (full coverage at low premiums), the high type would prefer it over their expensive comprehensive contract — destroying the separation. By making the low-type contract less attractive (high deductibles, limited coverage), the insurer ensures only genuinely low-risk customers choose it. The high type could take it, but finds it suboptimal given how often they expect to claim. This is the fundamental cost of adverse selection: the low type receives a worse deal to preserve separation."

- question: "Incentive compatibility requires that each type prefers the contract designed for them over any other contract in the screening menu."
  type: true-false
  answer: true
  explanation: "True. Incentive compatibility (IC) is the formal constraint ensuring self-selection works: a high-risk customer must prefer the comprehensive contract over the basic one, and a low-risk customer must prefer the basic contract over the comprehensive one. If either IC constraint is violated, that type would switch contracts, collapsing the separation. IC constraints, together with individual rationality (IR) constraints (each type must prefer participating to exiting), are the two key constraints in the screening optimization problem."

- question: "A well-designed screening mechanism achieves the same efficiency as the full-information (first-best) outcome — it simply redistributes payments between types."
  type: true-false
  answer: false
  explanation: "False. Screening reduces but does not eliminate the efficiency loss from adverse selection. Under full information, both types receive efficient contracts — no distortions needed. Under screening, the low type receives a deliberately suboptimal contract to prevent high-type mimicry. The gap between the first-best and second-best (screening) outcomes represents the information rent — the efficiency cost society pays for asymmetric information. Screening improves on the adverse-selection pooling outcome but cannot recover full-information efficiency."

- question: "Why must the uninformed party distort the low-type's contract in a screening equilibrium, and what economic cost does this impose?"
  type: short-answer
  answer: "The low-type contract must be made unattractive enough that high types prefer paying the premium for their efficient contract rather than mimicking the low type. This is achieved by reducing coverage, increasing deductibles, or otherwise lowering the value of the low-type contract. The economic cost is that genuinely low-risk individuals receive a suboptimal deal — less coverage than they would get under full information. This efficiency loss is called the information rent: it measures the cost imposed by the informational asymmetry between parties."
  explanation: "This tradeoff is fundamental in contract theory: separation requires that the high type's contract be sufficiently superior to the low-type contract that the high type does not defect, but this can only be achieved by making the low-type contract inferior to what the low type would receive under full information. The same logic applies to employer probationary contracts, bank collateral requirements, and airline fare classes."
```

## Explainer

From your study of Bayesian games and incomplete information, you know that players may hold private information that affects strategic outcomes. **Adverse selection** is what happens when this private information distorts market participation itself. The classic example is insurance: healthy people know they are low-risk and find high premiums unattractive, while sick people know they are high-risk and find the same premiums a bargain. If the insurer cannot distinguish types, the pool of buyers skews toward high-risk individuals — the selection of participants is adverse to the uninformed party. George Akerlof's "market for lemons" showed that in the extreme case, this unraveling can destroy the entire market.

**Screening** is the uninformed party's strategic response. Instead of offering a single contract and hoping for the best, the uninformed party offers a **menu of contracts** designed so that each type voluntarily selects the contract intended for them. Consider an insurance company offering two policies: a comprehensive plan with high premiums and low deductibles, and a basic plan with low premiums and high deductibles. High-risk individuals prefer the comprehensive plan because they expect to file many claims; low-risk individuals prefer the basic plan because they rarely need coverage. By designing the menu carefully, the insurer gets each type to **self-select** and reveal their private information through their choice.

The key technical constraints are **incentive compatibility** (each type must prefer the contract designed for it over any other contract in the menu) and **individual rationality** (each type must prefer participating to walking away). These constraints formalize what "designed carefully" means. Using the tools of constrained optimization you have studied, the screening problem becomes: maximize the uninformed party's payoff subject to incentive compatibility and participation constraints for every type. The solution typically involves **distorting** the contract offered to the low type — giving them less coverage or lower quality — to make their contract unattractive to the high type. The high type gets an efficient contract but pays a premium that extracts their information rent.

This distortion is the fundamental cost of adverse selection: efficiency is sacrificed to achieve separation. In a world of perfect information, both types would get efficient contracts. With screening, the high type does fine, but the low type receives a suboptimal deal. The gap between the first-best (full information) and second-best (screening) outcome represents the **information rent** — the price society pays for asymmetric information. This framework extends far beyond insurance: employers screening workers with probationary contracts, banks screening borrowers with collateral requirements, and airlines screening passengers with fare classes all follow exactly the same logic.
