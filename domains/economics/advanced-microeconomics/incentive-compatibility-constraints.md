---
id: incentive-compatibility-constraints
title: Incentive Compatibility and Individual Rationality
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games
  type: hard
- id: quasi-linear-preferences
  type: soft
- id: individual-rationality-mechanism
  type: soft
builds-toward:
- moral-hazard
- mechanism-design-basics
tags:
- contract-theory
- mechanism-design
stage: expert
status: validated
---
# Incentive Compatibility and Individual Rationality

## Core Idea
Incentive compatibility requires that each agent's optimal action is truth-telling (or the action chosen). Individual rationality requires agents accept the contract (participate). In contract design, these constraints limit efficiency: the planner must offer rents to induce truthful reporting or effort, creating information rents that reduce total surplus. The tradeoff between incentives and efficiency is fundamental to contract theory.

## Questions

```yaml
- question: "An insurance company offers two health plans. Low-risk customers are intended to pick the low-coverage plan; high-risk customers are intended to pick the high-coverage plan. High-risk customers prefer their intended plan. For incentive compatibility to also hold for low-risk customers, which condition must be satisfied?"
  type: multiple-choice
  options:
    - "Low-risk customers must weakly prefer the low-coverage plan over the high-coverage plan"
    - "High-risk customers must be indifferent between the two plans"
    - "The insurer must be able to verify each customer's true risk type"
    - "Both types must prefer participating to their outside option"
  answer: 0
  explanation: "Incentive compatibility requires that EACH type weakly prefers its intended contract over the contract designed for other types. If low-risk customers preferred the high-coverage plan, they would misrepresent themselves as high-risk, breaking the mechanism. Option C is wrong — the entire purpose of IC constraints is to design contracts that work WITHOUT the ability to verify types. Option D describes the individual rationality (IR) constraint, which is a separate requirement from IC."

- question: "A mechanism designer achieves first-best efficiency AND satisfies incentive compatibility by extracting all surplus from every agent type. Is this generally possible under private information?"
  type: multiple-choice
  options:
    - "Yes — the designer can always achieve both by choosing the right allocation rule"
    - "No — achieving incentive compatibility typically requires leaving information rents to well-informed agents"
    - "Yes — if the designer has commitment power, information rents become unnecessary"
    - "No — incentive compatibility makes first-best impossible even if agents have no private information"
  answer: 1
  explanation: "Under private information, achieving incentive compatibility typically requires leaving information rents — surplus given to well-informed agents precisely because they could profitably misrepresent themselves. A high-type agent must receive at least as much utility from their intended contract as they would get by pretending to be a low type. The designer cannot simultaneously satisfy IC and extract all surplus. With quasi-linear preferences, the analysis simplifies but information rents persist."

- question: "The individual rationality (IR) constraint and the incentive compatibility (IC) constraint are the same requirement expressed differently."
  type: true-false
  answer: false
  explanation: "They are distinct requirements. The IC constraint says each agent prefers the outcome designed for their true type over outcomes designed for other types — it governs truth-telling between agent types. The IR constraint says each agent prefers participating in the mechanism to their outside option — it governs whether agents join at all. A mechanism can satisfy IR (everyone participates) but violate IC (some agents lie), or satisfy IC (truth-telling is optimal) but violate IR (some types prefer not to participate)."

- question: "In a world of complete information, a contract designer can achieve the first-best allocation without leaving any information rents."
  type: true-false
  answer: true
  explanation: "With complete information, the designer knows every agent's type and can directly assign the efficient outcome to each type without any incentive to misrepresent. Because the designer can tailor contracts precisely, there is no need to make truth-telling incentive-compatible. Information rents arise only under INCOMPLETE information, where agents can profitably misrepresent their private type. This comparison reveals that information rents are the pure cost of private information."

- question: "Why must a contract designer leave 'information rents' to some agent types when designing an incentive-compatible mechanism, and what determines how large these rents must be?"
  type: short-answer
  answer: "Information rents are extra utility given to agents who have private information that they could use to misrepresent themselves. A high-type agent (e.g., a high-value buyer) must receive at least as much utility from their intended contract as they would get by pretending to be a low type. Because the low-type contract offers positive utility to the high type, the high-type contract must be even more attractive — guaranteeing a rent above the minimum participation level. The rent size is determined by how tempting the low-type option is for the high type — the 'mimicry payoff' that must be exceeded."
  explanation: "The fundamental tradeoff is: reducing information rents (to extract more surplus) requires distorting the allocation for low types (to make mimicry less attractive), reducing overall efficiency. Optimal mechanism design finds the allocation that maximizes the designer's objective subject to both IC and IR, accepting the unavoidable efficiency loss from information rents."
```

## Explainer

Imagine you are an insurance company designing a health plan, and your customers know more about their own health risks than you do. You would like each customer to choose the plan suited to their actual risk level — healthy people pick the low-coverage plan, sick people pick the high-coverage plan. But sick people might prefer the cheaper low-coverage plan if it saves them money upfront, and healthy people might claim to be sick to get extra coverage at a subsidized rate. The challenge is designing a menu of contracts where every type of customer voluntarily selects the option intended for them. This is the problem that **incentive compatibility** constraints address.

Formally, an **incentive compatibility (IC) constraint** says that each agent must weakly prefer the outcome designed for their true type over the outcome designed for any other type. If you are a high-risk customer, the contract meant for high-risk people must give you at least as much utility as pretending to be low-risk would. An **individual rationality (IR) constraint** (also called a participation constraint) says that each agent must prefer participating in the mechanism to their outside option — walking away entirely. Together, IC and IR define the feasible set of contracts: any contract design that violates IC will be gamed by some agents lying about their type, and any design that violates IR will be rejected outright.

The deep insight from your study of **Bayesian games and incomplete information** is that these constraints have real costs. In a world of complete information, the designer could simply assign the efficient outcome to each type. But with private information, the designer must make it in each agent's self-interest to reveal their type truthfully, and this typically requires leaving **information rents** — extra surplus that well-informed agents capture precisely because they could profitably misrepresent themselves. High-value buyers in an auction get rents because they could pretend to be low-value. Productive workers get rents because they could shirk. These rents are the price of truthful revelation.

The tradeoff between efficiency and information rents shapes virtually every real-world contract and institution. Tax authorities cannot observe taxpayers' true incomes, so they must design tax schedules where honest reporting is incentive-compatible — this is why optimal income taxes involve distortions away from the first-best. Employers cannot observe workers' effort directly, so they use performance pay that satisfies IC for effort provision. With **quasi-linear preferences** (which you may have studied), the analysis simplifies considerably because the IC constraints reduce to conditions on the allocation alone, independent of baseline wealth, making the mathematical characterization of optimal mechanisms much cleaner. But the fundamental lesson holds regardless of preference structure: whenever one party has private information, the other party must sacrifice some surplus to elicit truthful behavior, and the optimal mechanism balances this information cost against allocative efficiency.
