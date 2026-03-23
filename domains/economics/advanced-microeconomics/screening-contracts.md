---
id: screening-contracts
title: Screening and Contract Design
domain: economics
course: advanced-microeconomics
prerequisites:
- id: incentive-compatibility
  type: hard
- id: adverse-selection
  type: hard
tags:
- contract-theory
- screening
- self-selection
stage: expert
status: validated
---

# Screening and Contract Design

## Core Idea
In screening, the uninformed principal moves first by offering a menu of contracts. Informed agents self-select into contracts based on their type. The principal designs contracts so that incentive compatibility is satisfied: each type prefers the contract meant for them. Example: insurance companies offer plans with different deductibles to reveal risk types.

## Questions

```yaml
- question: "An insurance company cannot observe whether a customer is high-risk or low-risk. It designs a menu: Plan A (low deductible, high premium) and Plan B (high deductible, low premium). Which customer type will select Plan B, and why?"
  type: multiple-choice
  options:
    - "High-risk types, because the high deductible deters frequent claims"
    - "Low-risk types, because they rarely file claims and prefer lower upfront costs"
    - "Both types equally, since the menu is designed to be neutral"
    - "High-risk types, because they want to signal their willingness to absorb risk"
  answer: 1
  explanation: "Low-risk customers self-select into the high-deductible plan because they rarely file claims — the high deductible rarely costs them anything, while the low premium saves money. High-risk customers prefer the low-deductible plan because they expect frequent claims, making the high deductible too costly. The menu works as a self-selection device precisely because the two types have different preferences over this trade-off. The uninformed insurer designed the menu so that each type reveals itself through its own choice."

- question: "In a screening equilibrium, the principal intentionally distorts the contract for the low type below the efficient quantity. Why?"
  type: multiple-choice
  options:
    - "To punish the low type for having less valuable private information"
    - "To reduce production costs, since low types consume less"
    - "To make the low-type contract unattractive to high types, preserving separation"
    - "To satisfy the individual rationality constraint for the high type"
  answer: 2
  explanation: "The distortion is not punitive — it is strategic. If the low-type contract were fully efficient, the high type might prefer it (especially since the high type is already getting more). By making the low-type option less attractive (less quantity, higher deductible, lower quality), the principal ensures the high type has no incentive to mimic the low type. The distortion is the precise cost of information asymmetry: the principal cannot observe types, so it must sacrifice some efficiency at the bottom to maintain separation."

- question: "In a screening equilibrium, the high type typically earns information rents — meaning they receive more than they would if their type were directly observable."
  type: true-false
  answer: true
  explanation: "This is a fundamental result of screening theory. Because the principal cannot observe types, it must make the high type's contract genuinely more attractive than the low type's to prevent the high type from mimicking the low type. This extra attractiveness constitutes an information rent — the premium the principal pays for being uninformed. Under full information (observable types), the principal would extract all surplus. Under asymmetric information, the high type retains a rent."

- question: "In a screening equilibrium, the contract offered to the highest type is distorted below the efficient level, following the general principle that all contracts involve distortions."
  type: true-false
  answer: false
  explanation: "This reverses the 'no distortion at the top' result. In standard screening models, the highest type receives an efficient contract — no distortion. Distortions are applied to lower types' contracts to make them unattractive to higher types. Once the highest type is already at the top of the menu, there is no type above it that needs to be deterred from mimicking it, so no distortion is needed. Distortions propagate downward, not to the top."

- question: "Why must a principal designing a screening menu leave information rents to the high type, even though the principal's goal is to maximize profit by extracting as much surplus as possible?"
  type: short-answer
  answer: "To maintain incentive compatibility: the principal must ensure the high type genuinely prefers the contract designed for it over the low type's contract. If the high type's contract were no more attractive than the low type's, the high type would misrepresent itself and pick the lower-cost option, collapsing the separation. The information rent is the minimum premium that keeps the high type from defecting. It is the price the principal pays for not being able to directly observe the agent's private information."
  explanation: "The information rent is an unavoidable cost of information asymmetry, not a design failure. The only way to eliminate information rents would be to observe types directly (first-best) or to offer a single pooling contract (which loses the benefits of type separation). The principal optimizes by minimizing the rent while still maintaining separation — typically by distorting the low type's contract, making it less desirable to the high type, which reduces how much extra the high type must be given."
```

## Explainer

From adverse selection, you know that when one party has private information about their type, market outcomes can be severely distorted — the lemons problem shows how markets can unravel entirely. From incentive compatibility, you know that mechanism design must respect agents' ability to misrepresent themselves. **Screening** is the uninformed party's strategic response to this problem: instead of trying to observe the hidden information directly, the principal designs a menu of options that induces agents to *reveal* their types through their own choices.

The classic example is an insurance company that cannot directly observe whether a customer is high-risk or low-risk. If it offers a single policy, adverse selection kicks in — high-risk customers are more eager to buy, premiums rise, and low-risk customers may exit. Instead, the company offers a **menu of contracts**: one with a low deductible and high premium, another with a high deductible and low premium. The key design principle is that high-risk customers, who expect to file many claims, will prefer the low-deductible plan (paying more upfront but less per claim). Low-risk customers, who rarely file claims, will prefer the high-deductible plan (paying less upfront and absorbing the rare loss). The customers' own choices separate them by type — the contract menu acts as a **self-selection device**.

For this to work, the menu must satisfy two constraints. The **incentive compatibility constraint** (IC) requires that each type genuinely prefers the contract designed for them over any other option on the menu. If the low-deductible plan were too cheap, low-risk types would take it too, defeating the purpose. The **individual rationality constraint** (IR, also called the participation constraint) requires that each type prefers their designated contract to no contract at all — otherwise they simply walk away. The principal's optimization problem is to maximize profit (or minimize cost) subject to these IC and IR constraints.

A critical result in screening theory is that the principal can typically extract the **full surplus from the lowest type** (making their IR constraint bind — they are just barely willing to participate) while leaving **information rents** to higher types. In the insurance example, low-risk customers get a plan that is just barely acceptable, while high-risk customers get a more generous plan — not out of kindness, but because that generosity is what prevents low-risk types from mimicking high-risk types. The information rent is the cost the principal pays for being uninformed: it is the premium that must be offered to prevent profitable misrepresentation.

Compared to the full-information benchmark, screening always involves a **distortion** of the contract offered to at least one type. The principal typically distorts the low type's contract downward (less coverage, less quantity, lower quality) to make it unattractive to the high type, thereby preserving separation. The high type's contract is often efficient (no distortion) — a result known as "no distortion at the top." This pattern appears across screening applications: quantity discounts that offer less-than-efficient small packages, airlines that make economy class deliberately uncomfortable, software companies that cripple basic versions. In each case, the distortion is not arbitrary — it is the precise cost of eliciting truthful self-selection in a world where the principal cannot observe what the agent knows.
