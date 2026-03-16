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
stage: abstract-reasoning
status: draft
---

# Screening and Contract Design

## Core Idea
In screening, the uninformed principal moves first by offering a menu of contracts. Informed agents self-select into contracts based on their type. The principal designs contracts so that incentive compatibility is satisfied: each type prefers the contract meant for them. Example: insurance companies offer plans with different deductibles to reveal risk types.

## Explainer

From adverse selection, you know that when one party has private information about their type, market outcomes can be severely distorted — the lemons problem shows how markets can unravel entirely. From incentive compatibility, you know that mechanism design must respect agents' ability to misrepresent themselves. **Screening** is the uninformed party's strategic response to this problem: instead of trying to observe the hidden information directly, the principal designs a menu of options that induces agents to *reveal* their types through their own choices.

The classic example is an insurance company that cannot directly observe whether a customer is high-risk or low-risk. If it offers a single policy, adverse selection kicks in — high-risk customers are more eager to buy, premiums rise, and low-risk customers may exit. Instead, the company offers a **menu of contracts**: one with a low deductible and high premium, another with a high deductible and low premium. The key design principle is that high-risk customers, who expect to file many claims, will prefer the low-deductible plan (paying more upfront but less per claim). Low-risk customers, who rarely file claims, will prefer the high-deductible plan (paying less upfront and absorbing the rare loss). The customers' own choices separate them by type — the contract menu acts as a **self-selection device**.

For this to work, the menu must satisfy two constraints. The **incentive compatibility constraint** (IC) requires that each type genuinely prefers the contract designed for them over any other option on the menu. If the low-deductible plan were too cheap, low-risk types would take it too, defeating the purpose. The **individual rationality constraint** (IR, also called the participation constraint) requires that each type prefers their designated contract to no contract at all — otherwise they simply walk away. The principal's optimization problem is to maximize profit (or minimize cost) subject to these IC and IR constraints.

A critical result in screening theory is that the principal can typically extract the **full surplus from the lowest type** (making their IR constraint bind — they are just barely willing to participate) while leaving **information rents** to higher types. In the insurance example, low-risk customers get a plan that is just barely acceptable, while high-risk customers get a more generous plan — not out of kindness, but because that generosity is what prevents low-risk types from mimicking high-risk types. The information rent is the cost the principal pays for being uninformed: it is the premium that must be offered to prevent profitable misrepresentation.

Compared to the full-information benchmark, screening always involves a **distortion** of the contract offered to at least one type. The principal typically distorts the low type's contract downward (less coverage, less quantity, lower quality) to make it unattractive to the high type, thereby preserving separation. The high type's contract is often efficient (no distortion) — a result known as "no distortion at the top." This pattern appears across screening applications: quantity discounts that offer less-than-efficient small packages, airlines that make economy class deliberately uncomfortable, software companies that cripple basic versions. In each case, the distortion is not arbitrary — it is the precise cost of eliciting truthful self-selection in a world where the principal cannot observe what the agent knows.
