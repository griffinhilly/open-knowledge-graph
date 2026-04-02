---
id: moral-hazard-contracting
title: Moral Hazard and Optimal Contracting
domain: economics
course: microeconomics
prerequisites:
- id: moral-hazard
  type: hard
tags:
- information asymmetry
- moral hazard
- principal-agent
stage: expert
status: validated
---

# Moral Hazard and Optimal Contracting

## Core Idea
Moral hazard arises when an agent's hidden actions (effort, risk-taking) are unobservable to a principal who bears the cost. The principal cannot condition payment on effort, so must use output-based contracts to incentivize. Optimal contracts balance incentive provision (high-powered) against risk imposition on risk-averse agents (low-powered). Insurance, employment, and debt contracts exemplify this tradeoff: full insurance eliminates incentive; no insurance removes the principal's control.

## Questions

```yaml
- question: "A company is designing a compensation package for its sales team. It is considering Option A (fixed salary with no performance component) and Option B (pure commission with no base salary). An HR consultant says neither extreme is optimal. Why?"
  type: multiple-choice
  options:
    - "Labor law requires a mix of fixed and variable pay in most jurisdictions"
    - "Fixed salary eliminates effort incentives entirely; pure commission imposes all output risk on agents regardless of luck, which is inefficient for risk-averse employees"
    - "Salespeople prefer a mix because it reduces income tax liability"
    - "Pure commission leads to overwork, while fixed salary leads to underperformance, so a mix averages these effects"
  answer: 1
  explanation: "This is the core risk-vs-incentives tradeoff. A fixed salary provides perfect insurance to the risk-averse agent but breaks the link between effort and pay — the agent bears no cost from low output. Pure commission creates strong incentives (pay rises with sales) but forces the agent to bear outcome risk that partly reflects luck, not just effort. A salesperson who has a bad quarter due to a recession bears 100% of that loss under pure commission, which is inefficient from an insurance perspective. The optimal contract combines some fixed pay (insurance) with some performance component (incentives), accepting some inefficiency on each dimension to reduce inefficiency on the other."

- question: "A firm is deeply insolvent — its debt exceeds the value of its assets. The shareholders (equity holders) are considering a high-risk project that has a 20% chance of a $200M payoff and an 80% chance of losing an additional $50M. The project has a negative expected value. Why might shareholders take it anyway?"
  type: multiple-choice
  options:
    - "Shareholders are irrational and do not correctly calculate expected values"
    - "Shareholders benefit from the upside if the project succeeds but creditors bear most of the additional downside since equity is already worthless"
    - "Regulators require insolvent firms to pursue high-risk strategies to attempt recovery"
    - "The project's high variance reduces the firm's risk as a whole through diversification"
  answer: 1
  explanation: "This is the 'gambling for resurrection' moral hazard problem in debt contracts. When the firm is already insolvent, equity value is zero in the bad state regardless of whether the firm loses another $50M or $0 — creditors absorb that loss. But in the 20% success scenario, equity captures the gain. Shareholders face a payoff structure like a call option: heads they win, tails creditors lose. This asymmetry gives them incentive to take negative-expected-value gambles that transfer wealth from creditors to equity. This is why debt covenants restrict high-risk activities and why creditors demand collateral: to reduce this moral hazard."

- question: "When effort is fully observable (first-best contracting), the optimal contract for a risk-averse agent pays a fixed wage in exchange for a specified effort level, providing both efficient effort and perfect insurance."
  type: true-false
  answer: true
  explanation: "True. Under full information, the principal can write a forcing contract: 'If you exert effort e*, I pay you W; if you exert anything less, you get your outside option.' The agent is indifferent between exerting e* at wage W and their outside option, so they comply. Because the wage is fixed, the agent bears no income risk — all output variability falls on the principal, who is better positioned to absorb it (risk-neutral or diversified). The first-best achieves both incentive efficiency (correct effort level) and risk efficiency (optimal insurance) simultaneously. Moral hazard only arises when effort is hidden and this forcing contract is unavailable."

- question: "The optimal contract under moral hazard provides the agent with full insurance against most income risk."
  type: true-false
  answer: false
  explanation: "False. Full insurance (a fixed wage) eliminates all income risk for the agent but also eliminates all effort incentives — the agent receives the same pay regardless of outcome and therefore has no reason to work hard. The optimal second-best contract deliberately imposes some income risk on the agent by making pay partially dependent on output. This is less efficient than full insurance from a pure risk-sharing perspective, but it recovers some incentive to exert effort. The optimal contract accepts some welfare loss from risk imposition to gain the benefit of higher effort, trading off the two sources of inefficiency to minimize total loss."

- question: "An employer is deciding how much of a salesperson's pay to make performance-based. Explain the tradeoff the employer faces and why the optimal contract is neither pure salary nor pure commission."
  type: short-answer
  answer: "The employer faces a risk-incentives tradeoff. More performance-based pay increases the agent's effort incentives (since higher effort now translates to higher pay) but forces the risk-averse agent to bear more income risk from factors outside their control, such as market conditions. Pure salary provides perfect insurance but removes incentives entirely. Pure commission maximizes incentives but imposes all output variance on the agent, who must be compensated with higher expected pay to accept the risk (via the participation constraint). The optimal contract balances these: some fixed base provides insurance and reduces the risk premium the employer must pay, while a performance component preserves some incentive. The exact mix depends on the agent's degree of risk aversion, the variance of the output signal, and how sensitive output is to effort."
  explanation: "This tradeoff is fundamental across domains: insurance deductibles (copays restore prevention incentives while maintaining some coverage), executive equity compensation (aligns manager-shareholder interests but forces concentrated undiversified risk), and debt covenants (restricts risky behavior while allowing the firm to borrow). In every case, the designer accepts some inefficiency on one dimension to recover efficiency on the other."
```

## Explainer

From your prerequisite study of moral hazard, you know the core problem: a principal (employer, insurer, lender) wants an agent (employee, policyholder, borrower) to take a costly action — exert effort, drive carefully, run the business prudently — but cannot directly observe whether they do. The question now is: what contract should the principal offer? The answer is not obvious because there are two things the principal wants simultaneously, and they pull in opposite directions.

The first goal is **risk sharing**. If the agent is risk-averse and the principal is risk-neutral (or has better access to diversification), efficiency requires that the principal absorb the output variability. The agent should receive a fixed payment regardless of outcomes. A salaried employee is the clearest example: the employer takes the revenue risk, the worker gets a stable paycheck. But here is the problem: once the employee's income is fixed, they bear no personal cost from low output. The effort-supply incentive disappears entirely. This is the fundamental tension.

The second goal is **incentive provision**. To restore effort incentives, the contract must make the agent's pay depend on output. A commission salesperson earns more when they sell more — that creates incentive. But now the agent bears outcome risk that partly reflects luck, not just effort. A good salesperson can have a bad quarter because of macro conditions. Forcing them to bear that risk is inefficient from a pure insurance standpoint. The **optimal contract** navigates this tradeoff: it imposes just enough output-contingent pay to induce the desired effort level, and no more. The tradeoff is often called **risk vs. incentives**: high-powered contracts (large pay-for-performance) provide strong incentives but impose large risk; low-powered contracts (near-flat pay) impose little risk but provide weak incentives.

Applications across domains follow the same logic. Insurance: full coverage eliminates the policyholder's incentive to prevent loss (drive carefully, lock doors). Insurers respond with deductibles and co-pays — partial loss-bearing restores prevention incentives. Debt: once a firm is deeply insolvent, shareholders bear no additional downside but capture any upside, so they have incentive to take excessive risk ("gambling for resurrection"). Equity-based executive compensation aligns manager incentives with shareholders but forces executives to hold concentrated, undiversified wealth. In each case, the contract designer faces the same tradeoff and picks an interior solution that accepts some inefficiency on one dimension to reduce inefficiency on the other.
