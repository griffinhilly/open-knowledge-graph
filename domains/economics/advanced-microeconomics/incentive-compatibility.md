---
id: incentive-compatibility
title: Incentive Compatibility
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games
  type: hard
- id: incentive-compatibility-constraints
  type: soft
builds-toward:
- mechanism-design-basics
- screening-contracts
tags:
- mechanism-design
- truthfulness
- incentives
stage: expert
status: validated
---
# Incentive Compatibility

## Core Idea
Incentive compatibility (IC) is a constraint in mechanism design: truth-telling must be optimal for each agent. Formal IC: for all types t_i, t_i', agent i weakly prefers reporting true type t_i over lying and reporting t_i'. Strong IC requires strict preference. IC is necessary for mechanisms to elicit honest information without monitoring.

## Questions

```yaml
- question: "A government awards a contract to the firm that reports the lowest cost, then pays that cost. This procurement rule is NOT incentive-compatible because:"
  type: multiple-choice
  options:
    - "Firms cannot accurately estimate their own costs under uncertainty"
    - "Every firm has an incentive to report a cost higher than its true cost to extract a larger payment"
    - "The government cannot verify actual costs even after the contract is completed"
    - "Firms will collude to report identical costs, making the auction unable to select a winner"
  answer: 1
  explanation: "Under naive cost-plus procurement, a firm with true cost c knows it will be paid whatever it reports. Reporting c + ε earns ε more profit at no cost — there is no incentive to reveal true costs. This is a textbook IC failure: the mechanism makes lying strictly profitable. An IC-compliant mechanism must restructure payments so that for every possible true type, the expected payoff from truthful reporting weakly dominates any lie. Option C (verification) is a related but distinct issue — IC must hold even without ex-post verification."

- question: "Dominant-strategy incentive compatibility (DSIC) is stronger than Bayesian incentive compatibility (BIC) because:"
  type: multiple-choice
  options:
    - "DSIC requires truth-telling to be optimal regardless of what any other agent reports; BIC only requires it to be optimal in expectation over the distribution of others' types"
    - "DSIC applies to settings with continuous type spaces; BIC only applies to discrete types"
    - "DSIC eliminates information rents entirely; BIC allows them to persist"
    - "DSIC guarantees a unique equilibrium; BIC only guarantees existence of at least one"
  answer: 0
  explanation: "DSIC means truth-telling is a dominant strategy — it is optimal no matter what other agents report, no matter what type they actually are. BIC is weaker: truth-telling is optimal only in expectation, integrating over the distribution of others' types. DSIC is therefore more robust — it does not rely on correct beliefs about others — but harder to achieve. Vickrey auctions (second-price) satisfy DSIC; some Bayesian auction formats satisfy BIC but not DSIC."

- question: "An incentive-compatible mechanism gets agents to report truthfully by appealing to their honesty and moral character, rather than by making honesty the self-interested choice."
  type: true-false
  answer: false
  explanation: "False. Incentive compatibility is a purely strategic concept — it means that truthful reporting is the *self-interested* choice, regardless of moral preferences. The mechanism is designed so that lying is weakly dominated: no agent can do better by misrepresenting their type, given the payments and allocations the mechanism delivers. IC does not assume or require agents to be honest by nature. This is the mechanism design insight: instead of asking people to 'be honest,' design the rules so that honesty serves their own interests."

- question: "Achieving incentive compatibility often requires leaving 'information rents' — extra payoff — to agents with favorable private information, rather than extracting the full available surplus."
  type: true-false
  answer: true
  explanation: "True. This is the fundamental IC constraint in adverse selection settings. A low-cost (high-efficiency) firm must be paid enough that it would not benefit from mimicking a high-cost firm — otherwise it would misreport to capture better terms. The extra payoff that makes truthful reporting rational is the 'information rent.' Extracting these rents completely while maintaining IC is impossible: the designer faces a tradeoff between efficiency and rent extraction. This is why optimal auctions, optimal contracts, and optimal regulation all leave some surplus with privately-informed agents."

- question: "Why can't a mechanism designer simply instruct all agents to 'report their true type' and rely on the instruction to ensure honest disclosure?"
  type: short-answer
  answer: "Agents are self-interested: if misreporting yields a better allocation or larger payment, they will lie regardless of instructions. An instruction to 'be honest' provides no strategic reason to comply when honesty is costly. Incentive compatibility solves this by structuring the mechanism — the mapping from reports to outcomes and transfers — so that truthful reporting is the payoff-maximizing choice. Only when honesty is the dominant (or equilibrium) strategy can the mechanism reliably elicit private information."
  explanation: "This is the core insight of mechanism design: the designer controls the rules, not the agents' preferences or information. Since agents' types are unverifiable before the mechanism runs, the only lever the designer has is the incentive structure — the relationship between reported types and outcomes. IC translates 'how do we get honest reports?' from a vague request into a formal constraint that can be solved for, checked, and incorporated into optimal mechanism design."
```

## Explainer

From Bayesian games, you know that players often have private information — their own costs, valuations, or preferences — that others cannot observe. A natural follow-up question is: can we design rules (mechanisms) that get people to honestly reveal this private information? **Incentive compatibility** is the formal condition that makes this possible. A mechanism is incentive-compatible when every participant finds it in their own self-interest to report their true type, rather than misrepresenting it to gain an advantage.

Consider a concrete setting. A government wants to allocate a public contract to the firm that can deliver it most cheaply, but each firm privately knows its own cost. If the government simply asks firms to report their costs and awards the contract to the cheapest, every firm has an incentive to exaggerate — reporting higher costs to extract a larger payment. An incentive-compatible mechanism restructures the payments so that this lying is no longer profitable. The key insight is that the mechanism must make truthful reporting a **dominant strategy** (or at least a Bayesian-Nash equilibrium strategy): for every possible type a firm might be, and for every possible report by other firms, honesty must yield at least as high a payoff as any lie.

Formally, let each agent have a **type** t_i drawn from some distribution — this type captures their private information. The mechanism asks agents to report a type, then determines an allocation and transfers based on the reports. The IC constraint says: for agent i with true type t_i, the expected payoff from reporting t_i must be at least as large as the expected payoff from reporting any alternative type t_i'. **Bayesian incentive compatibility** (BIC) requires this in expectation over others' types; **dominant-strategy incentive compatibility** (DSIC) requires it for every possible realization of others' types. DSIC is stronger — it means honesty is optimal regardless of what anyone else does — while BIC only requires honesty to be optimal on average.

The concept has a remarkable structural implication. In many settings, incentive compatibility constrains the mechanism designer to leave **information rents** to agents with favorable private information. A low-cost firm, by being willing to truthfully reveal its efficiency, must be paid enough that it would not prefer to mimic a high-cost firm. These information rents are the price the designer pays for truthful revelation. This tradeoff between extracting surplus and maintaining honesty is central to auction design, regulation, taxation, and contract theory — wherever a principal must elicit information from better-informed agents. Incentive compatibility turns "how do we get people to tell the truth?" from a vague aspiration into a precise, solvable constraint.
