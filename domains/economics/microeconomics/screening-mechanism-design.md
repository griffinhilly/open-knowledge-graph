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
stage: advanced
status: draft
---

# Screening and Optimal Mechanism Design

## Core Idea
When the uninformed party designs a mechanism to induce revelation, they use screening: offering contracts (menus) where different types self-select. Incentive-compatible contracts make truth-telling optimal for each type. Monotonicity and single-crossing conditions ensure separating equilibrium. Applications include insurance contracts (with deductible menus separating risk types), wage schedules (separating ability types), and auctions (revealing bidder values). Mechanism design seeks efficiency-incentive tradeoffs.

## Questions

```yaml
- question: "An insurer wants to offer efficient full coverage to both high-risk and low-risk customers at prices reflecting each type's actuarial cost. Why can't they simply offer two full-coverage contracts at different prices?"
  type: multiple-choice
  options:
    - "Insurance regulations prohibit risk-based pricing in most markets"
    - "High-risk customers would purchase the cheaper low-risk-priced contract, since risk type is private information the insurer cannot observe"
    - "High-risk customers would prefer the full-coverage plan priced for their type, so no mimicry problem arises"
    - "Low-risk customers would exit the market rather than reveal their type"
  answer: 1
  explanation: "This is exactly the screening problem. If the insurer prices each contract at the actuarial cost for that type, high-risk customers would defect to the cheaper low-risk-priced contract—the insurer cannot observe who is truly low-risk. Incentive compatibility requires that each type prefers the contract designed for them over any other. To deter high-risk types from mimicking low-risk ones, the low-risk contract must be made less attractive to high-risk types, typically by adding a deductible."

- question: "In a two-type screening model, what happens to the low-type contract relative to the full-information efficient allocation?"
  type: multiple-choice
  options:
    - "It is distorted upward to attract the low type with extra quality"
    - "It matches the efficient allocation—only the high type's contract is distorted"
    - "It is distorted downward to make mimicry by the high type unattractive"
    - "Both types receive the efficient allocation; information rents are minimized by adjusting prices alone"
  answer: 2
  explanation: "The signature result of screening models is that only the top type receives the efficient (first-best) contract. All other types receive downward-distorted contracts—less quantity, less coverage, less quality than under full information. This distortion serves as a commitment device: it makes the low-type contract unattractive to the high type (by the single-crossing condition), who then self-selects into the high-type contract despite its higher price."

- question: "In a separating equilibrium under screening, the high type earns positive surplus (an information rent) even though the principal would prefer to extract all surplus."
  type: true-false
  answer: true
  explanation: "The information rent is unavoidable. The high type always has the option of taking the low-type contract and mimicking the low type. To prevent this, the principal must leave the high type surplus that makes mimicry not worthwhile. This rent—the direct cost of private information—represents the value of the high type's private knowledge, which the principal cannot extract without violating incentive compatibility."

- question: "The revelation principle implies that the principal can achieve the full-information outcome by offering a direct mechanism in which agents report their types truthfully."
  type: true-false
  answer: false
  explanation: "The revelation principle says that any outcome achievable by any mechanism can also be achieved by a direct mechanism where truth-telling is incentive compatible. But it does not say the principal can achieve the *full-information outcome*—only the best *incentive-compatible* outcome. When agents have private information, truth-telling requires information rents, which make the IC-optimal outcome strictly inferior to the first-best. The revelation principle simplifies the search for optimal mechanisms; it does not eliminate the fundamental cost of private information."

- question: "Why must the principal distort the low-type contract downward, even though this creates inefficiency? What would happen without this distortion?"
  type: short-answer
  answer: "Without distortion, both types would receive the efficient contract priced at each type's actuarial cost. But high-risk types would defect to the cheaper low-risk contract, violating incentive compatibility. To make the low-risk contract unattractive to high-risk types, the principal reduces its quantity or coverage below the efficient level. By the single-crossing condition, high types—who value quality more—find the distorted contract less tempting than low types do, so each type self-selects correctly. The inefficiency is the unavoidable cost of asymmetric information."
  explanation: "The distortion trades off two costs: the efficiency loss from below-efficient low-type contracts versus the information rent that must be paid if high types can costlessly mimic low types. The optimal mechanism minimizes total cost by distorting all types except the top."
```

## Explainer

Your prerequisite on mechanism design basics established that the designer of a mechanism can harness the **revelation principle**: rather than thinking about all the clever ways agents might misreport or game the system, it suffices to look for **direct mechanisms** where telling the truth is each agent's optimal strategy. Screening takes this insight and asks a specific question: when agents have private information about their own type (high-risk vs. low-risk, high-ability vs. low-ability, high-value vs. low-value), how can the uninformed principal design a *menu* of contracts that makes different types voluntarily sort themselves?

The core tool is the **incentive compatibility (IC)** constraint: each type must prefer the contract designed for them over any contract designed for another type. Alongside IC sits the **participation (IR) constraint**: each type must prefer their contract to walking away entirely. The principal maximizes their own objective (profit, efficiency, revenue) subject to both sets of constraints. The key insight is that you typically cannot make every type equally happy — the high type always has the *option* of pretending to be low type and taking the low-type contract. To deter this, the principal must give the high type an **information rent**: extra surplus that makes it not worth mimicking the low type. This rent is the direct cost of private information.

The **single-crossing condition** is what makes clean separation possible. It says that the indifference curves of different types cross only once in the (contract, price) space — or equivalently, high types value quality more than low types do, in a way that cannot reverse. When single-crossing holds, separating equilibria are monotone: high types get higher quantity (or coverage, or effort) than low types. This monotonicity allows the designer to simplify from a combinatorial problem (all possible contracts) to a one-dimensional ordering problem. Violating single-crossing — types that "flip" relative valuations at different quality levels — causes pooling or breakdown of separation.

Insurance deductibles are the canonical illustration. An insurer offers two policies: a full-coverage plan at a high premium, and a partial-coverage plan (high deductible) at a low premium. High-risk customers (who expect to make frequent claims) strongly prefer full coverage and will pay up for it. Low-risk customers find the deductible plan acceptable because they rarely claim anyway — the premium savings outweigh the deductible risk. Each type self-selects into their designed contract without the insurer ever observing their risk type. The inefficiency is that low-risk customers get less insurance than they would receive under full information — the insurer must "distort" the low-risk contract downward to prevent high-risk types from mimicking it. This downward distortion for all but the highest type is the general signature of screening models: the top type gets the efficient contract; everyone else gets a distorted contract that discourages mimicry from above.
