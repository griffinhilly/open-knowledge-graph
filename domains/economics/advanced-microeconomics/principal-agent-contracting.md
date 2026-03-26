---
id: principal-agent-contracting
title: The Principal-Agent Problem
domain: economics
course: advanced-microeconomics
prerequisites:
- id: moral-hazard
  type: hard
- id: adverse-selection-signaling
  type: hard
- id: pooling-separating-equilibrium
  type: soft
- id: screening-and-self-selection
  type: soft
tags:
- contract-theory
- information-asymmetry
stage: expert
status: validated
---
# The Principal-Agent Problem

## Core Idea
The principal-agent problem arises when a principal (firm owner) hires an agent (manager) whose effort is unobservable (moral hazard) and whose ability/type may be unknown (adverse selection). The principal must design compensation schemes balancing incentive provision (to motivate effort and attract high-ability agents) against risk-sharing (given agent risk aversion).

## Questions

```yaml
- question: "In the optimal principal-agent contract, why does the principal distort the low-ability agent's contract away from first-best efficiency, even though this reduces total surplus?"
  type: multiple-choice
  options:
    - "To make the low-ability agent's contract unattractive enough that the high-ability agent will not want to mimic it, reducing the information rent the principal must pay the high type"
    - "To punish the low-ability agent for being less productive and reduce moral hazard"
    - "Because the participation constraint for the low type is harder to satisfy with an efficient contract"
    - "To satisfy the incentive compatibility constraint of the low type, who would otherwise prefer the high-type contract"
  answer: 0
  explanation: "The distortion serves one purpose: to deter mimicry by the high type. If the low-type contract were efficient (first-best), the high type would happily accept it and claim to be low ability while enjoying better terms. By making the low-type contract sufficiently unattractive — lower pay, less responsibility — the principal ensures the high type prefers her own contract. The cost is deadweight loss on low-type trades, but it reduces the information rent paid to the high type."

- question: "What does the 'no distortion at the top' result mean in optimal contract design?"
  type: multiple-choice
  options:
    - "The highest-ability agent receives an efficient (first-best) contract with no distortion, though she earns an information rent above her outside option"
    - "The highest-ability agent's contract is not distorted because she faces no moral hazard problem"
    - "The principal never distorts any contract because doing so always reduces her profit"
    - "The high-ability agent receives a contract that exactly equals her outside option with no surplus"
  answer: 0
  explanation: "In the optimal menu, the high type's contract specifies the first-best efficient effort level — there is no distortion of her actions. However, she earns a positive information rent (surplus above her outside option). The distortion occurs only in the low type's contract, which is less efficient than first-best. This 'no distortion at the top' pattern is a central result of mechanism design and screening theory."

- question: "In the optimal principal-agent solution, the high-ability agent earns strictly more than her outside option (her reservation utility)."
  type: true-false
  answer: true
  explanation: "True. This excess surplus is the information rent — the unavoidable payment the principal makes to the high type for truthfully revealing her type. If the principal tried to leave the high type with exactly her outside option, the high type would prefer to mimic the low type's contract and earn a better deal. The rent is the minimum bribe needed to make self-selection incentive compatible."

- question: "A principal can generally achieve the first-best outcome by offering a single contract that ties most compensation purely to observed output, eliminating any need for menus or information rents."
  type: true-false
  answer: false
  explanation: "False. Pure output-based contracts face two problems: (1) they expose risk-averse agents to income risk, violating the participation constraint or requiring a risk premium that is costly to the principal; (2) they cannot separate types — a single contract cannot simultaneously satisfy both the high type's and low type's incentive compatibility constraints if the principal does not know which type is which. Menus of contracts and information rents are necessary features of second-best optimal contracting, not avoidable inefficiencies."

- question: "Why are information rents unavoidable in the principal-agent problem with adverse selection? What happens if the principal tries to design contracts that leave the high-ability agent with exactly her outside option?"
  type: short-answer
  answer: "If the high-ability agent is left with exactly her outside option, she prefers to mimic the low-ability agent's contract — which, if designed for a less capable agent, would still give the high type more than her outside option given her higher ability. To prevent this mimicry, the principal must make the high type's own contract sufficiently attractive, leaving her with surplus (the information rent). Eliminating the rent by reducing the high type's contract makes it less attractive than the low type's, so the high type defects. The rent is the minimum payment required to make truthful self-selection incentive compatible."
  explanation: "The information rent arises from the participation constraint of the high type plus the incentive compatibility constraint. The principal must satisfy both simultaneously: the high type must prefer to participate (PC) and must prefer her own contract over the low type's (IC). These constraints jointly require strictly positive surplus for the high type. This is a fundamental constraint of mechanism design under asymmetric information — not a failure of contract design."
```

## Explainer

From moral hazard, you understand how hidden actions distort incentives. From adverse selection and signaling, you understand how hidden information creates screening problems. The **principal-agent problem** combines both: the principal faces an agent who may be a hidden type (high or low ability) and who takes hidden actions (high or low effort). Designing a contract that simultaneously solves both problems is the central challenge of contract theory.

Consider a firm owner (principal) hiring a division manager (agent). The owner does not know whether the manager is talented or mediocre (adverse selection), and cannot observe how hard the manager works (moral hazard). A high fixed salary attracts both types and motivates neither. Pure performance pay motivates effort but exposes the agent to risk and may fail to separate types. The principal needs a **menu of contracts** — different compensation packages designed so that each type of agent voluntarily selects the contract intended for them (self-selection) and then exerts the desired level of effort (incentive compatibility).

The formal structure builds on two constraints for each agent type. The **participation constraint** ensures the agent prefers the contract to her outside option — otherwise she walks away. The **incentive compatibility constraint** ensures two things: the agent truthfully reveals her type by choosing the right contract from the menu, and conditional on that contract, she exerts the intended effort level. The principal's problem is to maximize expected profit subject to all these constraints simultaneously. A key insight is that information rents are unavoidable: to prevent a high-ability agent from mimicking a low-ability agent and grabbing a better deal, the principal must leave the high type with surplus beyond her outside option. This rent is the price of eliciting truthful self-selection.

The optimal contract typically **distorts the low type's contract** away from the first-best to reduce the information rent paid to the high type. The high type gets an efficient contract (no distortion at the top) but earns a rent. The low type gets a less attractive contract — lower pay, less responsibility, or worse terms — that the high type would not want to mimic. This "no distortion at the top, distortion at the bottom" pattern appears throughout mechanism design and regulation. In practice, principal-agent theory explains why executive compensation packages combine base salary, bonuses, stock options, and deferred compensation — each component addresses a different dimension of the information problem. Salary provides insurance, bonuses incentivize effort, stock aligns long-run interests, and vesting periods discourage the agent from taking hidden actions that inflate short-term performance at the expense of long-term value.
