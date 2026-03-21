---
id: principal-agent-model
title: The Principal-Agent Model
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games
  type: hard
- id: constrained-optimization-lagrange
  type: soft
builds-toward:
- moral-hazard
- adverse-selection
tags:
- contract-theory
- delegation
- incentives
stage: advanced
status: draft
---

# The Principal-Agent Model

## Core Idea
The principal-agent model formalizes the problem of contracting when a principal hires an agent who has private information or unobservable actions. The principal designs a contract (payoff function) to maximize expected payoff subject to the agent's incentive and participation constraints. This framework encompasses moral hazard, adverse selection, and signaling.

## Questions

```yaml
- question: "A CEO receives a fixed salary of $5 million per year regardless of whether the company's stock rises or falls. From the principal-agent model's perspective, what problem does this create?"
  type: multiple-choice
  options:
    - "Adverse selection: the company may attract low-quality CEO candidates who prefer fixed pay"
    - "Moral hazard: the CEO has no financial incentive to exert costly effort, since pay does not depend on observable outcomes"
    - "Signaling failure: the CEO cannot credibly signal their quality to the board"
    - "No problem — fixed pay satisfies the participation constraint and is therefore optimal"
  answer: 1
  explanation: "When effort is unobservable (hidden action), a fixed wage severs the link between the agent's effort and their pay, eliminating the financial incentive to work hard. This is the classic moral hazard problem: because the principal cannot directly observe the CEO's effort, the agent may shirk knowing their compensation is unchanged. The solution is performance-based pay that ties compensation to observable outcomes (stock price, profits) that are correlated with effort — even though this forces the risk-averse agent to bear risk, the incentive effect is worth the cost. Option A is technically possible but is adverse selection (about type before hiring), not the ongoing effort problem described."

- question: "What is the 'second-best' outcome in the principal-agent framework, and why is it unavoidable when information is asymmetric?"
  type: multiple-choice
  options:
    - "The outcome where the agent works at minimum effort, satisfying only the participation constraint"
    - "The contract the principal offers when she has complete information about the agent's effort and type"
    - "The best achievable outcome under asymmetric information, which is strictly worse than what would be achievable if all information were observable"
    - "The equilibrium where both principal and agent receive equal payoffs"
  answer: 2
  explanation: "The 'first-best' is what the principal could achieve with perfect information — a complete contract specifying exactly what the agent should do in every state, with payment tied directly to actions rather than noisy outcomes. With asymmetric information, the first-best is unattainable: to motivate effort, the principal must tie pay to outcomes that are only imperfectly correlated with effort (introducing risk), or she must leave information rents to the agent (in adverse selection). The gap between first-best and second-best is the real economic cost of information asymmetry — it is not just a theoretical nuisance but an unavoidable inefficiency that shapes the design of every contract, insurance product, and regulatory scheme."

- question: "Moral hazard and adverse selection are fundamentally different phenomena that require entirely separate theoretical frameworks to analyze."
  type: true-false
  answer: false
  explanation: "Both moral hazard and adverse selection are special cases of the same principal-agent structure, differing only in the nature of the hidden information. In moral hazard, the hidden element is the agent's *action* (effort, care) taken after the contract is signed. In adverse selection, the hidden element is the agent's *type* (ability, risk level, cost) known before the contract is signed. Both fit the same framework: a principal designs a contract subject to the agent's participation and incentive compatibility constraints, and the gap between first-best and second-best arises from the inability to observe or verify the hidden element. Signaling and screening are also special cases of the same structure."

- question: "If the principal knows the agent's exact reservation utility, she can offer a contract that pays exactly that amount and always achieve the first-best outcome, because the participation constraint is satisfied by construction."
  type: true-false
  answer: false
  explanation: "Satisfying the participation constraint is necessary but not sufficient for the first-best. The other binding constraint is the incentive compatibility constraint: the agent must find it optimal to take the action the principal wants, given the contract terms. Paying the agent their reservation utility (making them just willing to participate) says nothing about whether they will exert the desired level of effort or truthfully reveal their type. With hidden actions, a flat payment at the reservation utility gives the agent no reason to work hard — they take the money, shirk, and keep the surplus from saved effort costs. The principal must distort the contract away from first-best to create incentives, which is costly."

- question: "Why does information asymmetry necessarily create costs — why can't the principal simply design a contract that achieves the same outcome as if information were symmetric?"
  type: short-answer
  answer: "With symmetric information, the principal could write a complete contingent contract: 'do action a in state s, and I'll pay you accordingly.' The agent's effort or type is directly contractible. With asymmetric information, the agent's action or type is unverifiable, so the contract can only specify payments as a function of observable outcomes. To motivate the desired action, the principal must make the agent bear outcome risk (in the moral hazard case) — expensive for a risk-averse agent — or must leave the agent an 'information rent' above their reservation utility (in the adverse selection case) to make revealing their true type incentive-compatible. Either way, the principal pays more or accepts lower effort than under symmetric information. The cost is unavoidable because it arises from the fundamental structure of the constraint."
  explanation: "The revelation principle makes this precise: any equilibrium outcome under asymmetric information can be implemented by a direct mechanism where agents truthfully report their type. But even truth-telling mechanisms must satisfy incentive compatibility, which forces the principal to leave rents to high-type agents — rents that could not exist under symmetric information. The second-best is not a failure of clever contract design; it is the theoretical floor."
```

## Explainer

The principal-agent model begins with a simple observation: much of economic life involves **delegation**. Shareholders hire managers. Patients rely on doctors. Voters elect politicians. In each case, one party (the **principal**) wants something done but depends on another party (the **agent**) to do it. The problem is that the agent has their own interests, which may not align with the principal's, and the agent typically knows something the principal does not — either about their own characteristics (adverse selection) or about their own actions (moral hazard). The principal-agent model provides a unified framework for analyzing how to design contracts that manage this tension.

The principal moves first by offering a **contract** — a mapping from observable variables to payments. The agent then decides whether to accept (the **participation constraint**) and, if they accept, what action to take or what information to reveal. The principal's design problem is constrained optimization: maximize expected payoff subject to the agent voluntarily participating and behaving as intended. From your work with Lagrangian methods and Bayesian games, you already have the mathematical machinery. The participation constraint ensures the agent gets at least their reservation utility. The **incentive compatibility constraint** ensures the agent finds it optimal to take the action (or reveal the information) the principal wants, given the contract terms.

What makes this framework powerful is its generality. When the hidden element is the agent's *action* (effort, care, diligence), you get **moral hazard** — the agent may shirk because effort is unobservable. The principal must tie pay to noisy outcomes to motivate effort, bearing a cost in risk. When the hidden element is the agent's *type* (ability, risk level, cost structure), you get **adverse selection** — the principal cannot distinguish high types from low types and must design contract menus or accept pooling. When the informed party moves first to reveal their type, you get **signaling**; when the uninformed party moves first to sort types, you get **screening**. All four phenomena — moral hazard, adverse selection, signaling, and screening — are special cases of the same principal-agent structure with different information assumptions.

The model's central lesson is that **information asymmetry has real costs**. In a world of perfect information, the principal could write a complete contract specifying exactly what the agent should do in every state and paying them accordingly — the **first-best**. With asymmetric information, the best achievable outcome (the **second-best**) is strictly worse. The gap between first-best and second-best is the cost of imperfect information, and contract design is the art of minimizing that gap. This framework underpins everything from insurance design to executive compensation to government regulation, and it is the lens through which modern economics analyzes any situation where one person depends on another who knows more or whose actions are hard to observe.
