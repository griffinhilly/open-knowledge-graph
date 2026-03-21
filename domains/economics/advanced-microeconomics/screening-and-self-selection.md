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

## Questions

```yaml
- question: "An insurer cannot observe whether applicants are high-risk or low-risk. It offers two contracts: Contract A (high premium, full coverage) and Contract B (low premium, high deductible). A high-risk applicant prefers A, a low-risk applicant prefers B. What has the insurer accomplished without asking anyone to disclose their risk type?"
  type: multiple-choice
  options:
    - "Nothing useful — the insurer still cannot verify which applicants are actually high-risk"
    - "It has induced self-selection: each type reveals their private information through their contract choice"
    - "It has screened out high-risk applicants by making Contract A unattractive to them"
    - "It has eliminated moral hazard by aligning premiums with expected claims"
  answer: 1
  explanation: "This is the central mechanism of screening. The insurer never asks 'are you high-risk?' — that would be cheap talk. Instead, the menu is designed so each type's incentive-compatible choice reveals their type through revealed preference. High-risk applicants, expecting many claims, rationally choose full coverage even at higher cost. Low-risk applicants, who rarely claim, prefer lower premiums. The choice itself is the signal. Note that option A misidentifies the goal: the insurer gains valuable information precisely because the choice is informative, even if it cannot be independently verified."

- question: "In a screening model, the low-risk insurance customer ends up with a contract offering less than full coverage — even though full coverage would be efficient for them under symmetric information. Why does the principal deliberately distort the low-risk contract?"
  type: multiple-choice
  options:
    - "The insurer is unaware that these customers are low-risk, so offers them a cautious contract"
    - "Full coverage for low-risk customers would encourage them to take more risks (moral hazard)"
    - "Offering the low-risk type less than full coverage makes that contract unattractive to high-risk types who might otherwise mimic them"
    - "Regulators require that deductibles be included in all insurance contracts"
  answer: 2
  explanation: "This is the cost of asymmetric information: the principal distorts the low-risk (bottom-type) contract to prevent high-risk (top-type) customers from claiming low-risk status. If low-risk customers received full coverage at low premiums, high-risk customers would prefer that contract too — it would fail the incentive compatibility constraint. By reducing coverage for low-risk types, the principal makes the contract unattractive to high-risk types who value comprehensive coverage highly. The distortion is not about moral hazard (that is a separate problem) but about deterring mimicry."

- question: "In a two-type screening model, the high type receives a distorted contract in order to prevent the low type from mimicking them."
  type: true-false
  answer: false
  explanation: "It is the LOW type's contract that is distorted, not the high type's. The 'no distortion at the top' result says the highest type always receives their first-best contract — distorting it would only reduce the principal's profit without relaxing any incentive constraint. The low type's contract is distorted because: (1) the distortion makes the high type unwilling to pretend to be the low type, and (2) the principal sacrifices efficiency for the low type to reduce the information rent that must be left to the high type. The high type gets the best deal; the low type pays the price of asymmetric information."

- question: "A screening mechanism can recover some surplus compared to no mechanism at all, but never achieves the first-best outcome possible under full information."
  type: true-false
  answer: true
  explanation: "True. Screening extracts partial information and allows the principal to offer differentiated contracts that are better than offering a single pooling contract. But it never achieves first-best efficiency because: (1) the low type's contract must be distorted away from first-best, and (2) the high type must receive an information rent — surplus beyond their outside option — to prevent them from claiming to be the low type. The first-best would require observing types directly; screening is a second-best mechanism that trades off efficiency losses for information gains."

- question: "Why must the principal leave an 'information rent' to the high type in a screening model, and what happens if the principal tries to reduce it to zero?"
  type: short-answer
  answer: "The information rent is the extra surplus the high type receives above their participation constraint — the payoff they would get by accepting their designated contract versus their outside option. It exists because the high type's contract must be good enough that the high type prefers it to the low type's contract (incentive compatibility). If the principal tries to reduce this rent to zero by lowering the high type's payoff, the high type would prefer to claim to be the low type and take that contract instead. The only way to eliminate the rent entirely is to make both types' contracts identical — a pooling equilibrium that sacrifices all informational benefit of the menu."
  explanation: "Information rent is the price of private information. The principal cannot extract all surplus from the high type without violating the IC constraint. The tradeoff is between extracting more rent from the high type (requiring more distortion of the low type's contract) and reducing distortion (but leaving more rent to the high type). The optimal mechanism balances these two costs. This is why screening is always second-best: asymmetric information forces the principal to leave value on the table."
```

## Explainer

Signaling and screening are two sides of the same information asymmetry coin. In signaling, the *informed* party moves first — a worker gets a degree to prove ability. In **screening**, the *uninformed* party moves first, designing a set of options that induce the informed party to sort themselves. Think of an insurance company that cannot observe whether applicants are high-risk or low-risk. Instead of asking (cheap talk), the company offers a **menu of contracts**: one with a high premium and low deductible, another with a low premium and high deductible. The key insight is that if the menu is designed correctly, each type voluntarily chooses the contract intended for them, and their choice reveals their private information.

The mechanism works through **self-selection**. High-risk individuals, who expect to file many claims, prefer comprehensive coverage even at a higher premium — the high deductible would cost them more in expected out-of-pocket expenses. Low-risk individuals, who rarely file claims, prefer to save on premiums and accept the higher deductible, since they are unlikely to pay it. The uninformed party (the insurer) never needs to ask "are you risky?" — the menu of contracts extracts this information through revealed preference. Each type's choice is incentive-compatible: given the options available, no type wants to pretend to be a different type.

Designing incentive-compatible menus requires satisfying two sets of constraints simultaneously. The **participation constraints** ensure each type prefers their designated contract to walking away entirely. The **incentive compatibility (IC) constraints** ensure each type prefers their designated contract to the one designed for other types. In practice, the binding IC constraint is typically the one preventing the "good" type from being mimicked by the "bad" type. To prevent high-risk individuals from choosing the low-risk contract (which has cheaper premiums), the principal must **distort** the low-risk contract away from its first-best design — offering less coverage than low-risk types would receive under full information. This distortion is the cost of asymmetric information: the low-risk type gets a worse deal than they would in a world where risk types were observable.

A key result is that **the top type gets no distortion but the bottom type does**. In the insurance example, high-risk types receive their first-best full-coverage contract (no reason to distort it — no one wants to mimic a high-risk type). Low-risk types receive a distorted contract with less coverage than ideal. This "no distortion at the top" result generalizes across screening models — from nonlinear pricing to labor contracts to regulation. The pattern reflects a deep economic logic: the principal sacrifices efficiency for the lower type to reduce the **information rent** — the extra surplus — that must be left to the higher type to keep them from mimicking. Screening is never as efficient as full-information contracting, but it recovers substantial value by cleverly harnessing the informed party's self-interest as a sorting mechanism.
