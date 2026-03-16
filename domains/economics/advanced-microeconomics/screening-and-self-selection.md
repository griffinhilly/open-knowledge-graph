---
id: screening-and-self-selection
title: Screening and Contract Menus
domain: economics
course: advanced-microeconomics
prerequisites:
- id: adverse-selection-signaling
  type: hard
- id: mechanism-design-basics
  type: hard
tags:
- contract-theory
- information-asymmetry
- mechanism-design
stage: advanced
status: draft
---

# Screening and Contract Menus

## Core Idea
Screening describes actions by the uninformed party to differentiate types of the informed party. The principal designs a menu of contracts (bundles of terms and conditions) such that self-interested agents of different types choose different contracts, revealing their types. Incentive compatibility constraints ensure each type prefers contracts designed for them.

## Explainer

Signaling and screening are two sides of the same information asymmetry coin. In signaling, the *informed* party moves first — a worker gets a degree to prove ability. In **screening**, the *uninformed* party moves first, designing a set of options that induce the informed party to sort themselves. Think of an insurance company that cannot observe whether applicants are high-risk or low-risk. Instead of asking (cheap talk), the company offers a **menu of contracts**: one with a high premium and low deductible, another with a low premium and high deductible. The key insight is that if the menu is designed correctly, each type voluntarily chooses the contract intended for them, and their choice reveals their private information.

The mechanism works through **self-selection**. High-risk individuals, who expect to file many claims, prefer comprehensive coverage even at a higher premium — the high deductible would cost them more in expected out-of-pocket expenses. Low-risk individuals, who rarely file claims, prefer to save on premiums and accept the higher deductible, since they are unlikely to pay it. The uninformed party (the insurer) never needs to ask "are you risky?" — the menu of contracts extracts this information through revealed preference. Each type's choice is incentive-compatible: given the options available, no type wants to pretend to be a different type.

Designing incentive-compatible menus requires satisfying two sets of constraints simultaneously. The **participation constraints** ensure each type prefers their designated contract to walking away entirely. The **incentive compatibility (IC) constraints** ensure each type prefers their designated contract to the one designed for other types. In practice, the binding IC constraint is typically the one preventing the "good" type from being mimicked by the "bad" type. To prevent high-risk individuals from choosing the low-risk contract (which has cheaper premiums), the principal must **distort** the low-risk contract away from its first-best design — offering less coverage than low-risk types would receive under full information. This distortion is the cost of asymmetric information: the low-risk type gets a worse deal than they would in a world where risk types were observable.

A key result is that **the top type gets no distortion but the bottom type does**. In the insurance example, high-risk types receive their first-best full-coverage contract (no reason to distort it — no one wants to mimic a high-risk type). Low-risk types receive a distorted contract with less coverage than ideal. This "no distortion at the top" result generalizes across screening models — from nonlinear pricing to labor contracts to regulation. The pattern reflects a deep economic logic: the principal sacrifices efficiency for the lower type to reduce the **information rent** — the extra surplus — that must be left to the higher type to keep them from mimicking. Screening is never as efficient as full-information contracting, but it recovers substantial value by cleverly harnessing the informed party's self-interest as a sorting mechanism.
