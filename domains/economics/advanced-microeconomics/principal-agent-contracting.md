---
id: principal-agent-contracting
title: The Principal-Agent Problem
domain: economics
course: advanced-microeconomics
prerequisites:
- id: moral-hazard-monitoring
  type: hard
- id: adverse-selection-signaling
  type: hard
tags:
- contract-theory
- information-asymmetry
stage: advanced
status: draft
---

# The Principal-Agent Problem

## Core Idea
The principal-agent problem arises when a principal (firm owner) hires an agent (manager) whose effort is unobservable (moral hazard) and whose ability/type may be unknown (adverse selection). The principal must design compensation schemes balancing incentive provision (to motivate effort and attract high-ability agents) against risk-sharing (given agent risk aversion).

## Explainer

From moral hazard, you understand how hidden actions distort incentives. From adverse selection and signaling, you understand how hidden information creates screening problems. The **principal-agent problem** combines both: the principal faces an agent who may be a hidden type (high or low ability) and who takes hidden actions (high or low effort). Designing a contract that simultaneously solves both problems is the central challenge of contract theory.

Consider a firm owner (principal) hiring a division manager (agent). The owner does not know whether the manager is talented or mediocre (adverse selection), and cannot observe how hard the manager works (moral hazard). A high fixed salary attracts both types and motivates neither. Pure performance pay motivates effort but exposes the agent to risk and may fail to separate types. The principal needs a **menu of contracts** — different compensation packages designed so that each type of agent voluntarily selects the contract intended for them (self-selection) and then exerts the desired level of effort (incentive compatibility).

The formal structure builds on two constraints for each agent type. The **participation constraint** ensures the agent prefers the contract to her outside option — otherwise she walks away. The **incentive compatibility constraint** ensures two things: the agent truthfully reveals her type by choosing the right contract from the menu, and conditional on that contract, she exerts the intended effort level. The principal's problem is to maximize expected profit subject to all these constraints simultaneously. A key insight is that information rents are unavoidable: to prevent a high-ability agent from mimicking a low-ability agent and grabbing a better deal, the principal must leave the high type with surplus beyond her outside option. This rent is the price of eliciting truthful self-selection.

The optimal contract typically **distorts the low type's contract** away from the first-best to reduce the information rent paid to the high type. The high type gets an efficient contract (no distortion at the top) but earns a rent. The low type gets a less attractive contract — lower pay, less responsibility, or worse terms — that the high type would not want to mimic. This "no distortion at the top, distortion at the bottom" pattern appears throughout mechanism design and regulation. In practice, principal-agent theory explains why executive compensation packages combine base salary, bonuses, stock options, and deferred compensation — each component addresses a different dimension of the information problem. Salary provides insurance, bonuses incentivize effort, stock aligns long-run interests, and vesting periods discourage the agent from taking hidden actions that inflate short-term performance at the expense of long-term value.
