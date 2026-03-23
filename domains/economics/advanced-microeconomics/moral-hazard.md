---
id: moral-hazard
title: Moral Hazard
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games
  type: hard
- id: principal-agent-model
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- screening-contracts
tags:
- contract-theory
- hidden-action
- incentives
stage: expert
status: validated
---

# Moral Hazard

## Core Idea
Moral hazard arises when an agent's actions are unobservable to the principal. The agent may shirk or take excessive risk because consequences are shared. Classic example: insurance reduces incentive to prevent loss. The principal must design contracts (e.g., deductibles, performance pay) to align incentives. Optimal contracts balance risk-sharing with incentives.

## How It's Best Learned
Analyze a simple principal-agent model with continuous effort. Solve for optimal contract. Compare to full-information benchmark to see efficiency loss from hidden action.

## Questions

```yaml
- question: "An insurance company observes that customers with comprehensive car insurance (zero deductible) have 30% more at-fault accidents than customers with high-deductible policies. Assuming customers were randomly assigned to these plans, this pattern is most likely explained by:"
  type: multiple-choice
  options:
    - "Adverse selection — risky drivers systematically choose comprehensive coverage to hide their type from insurers"
    - "Moral hazard — once insured against accident costs, drivers have less financial incentive to drive carefully"
    - "A principal-agent problem with symmetric information — the insurer can observe driving behavior directly"
    - "Selection bias — the insurance company enrolled riskier customers into the comprehensive plan"
  answer: 1
  explanation: "This is the textbook moral hazard example: once the financial consequence of an accident is borne by the insurer (hidden action occurs after contracting), policyholders have reduced incentive to take precautions. Note that option (a) — adverse selection — is a related but distinct concept. Adverse selection involves hidden *type* before contracting (risky drivers self-selecting into comprehensive plans). Moral hazard involves hidden *action* after contracting (policyholders changing their behavior because they are insured). The random assignment in this question's setup eliminates selection, leaving moral hazard as the explanation."

- question: "A principal wants to motivate a risk-averse agent to exert high effort on a task where outcomes are partially determined by luck. The fundamental design challenge is:"
  type: multiple-choice
  options:
    - "Ensuring the agent's hourly wage is high enough to attract talent in a competitive labor market"
    - "Balancing incentive provision against risk-sharing — high-powered pay-for-performance motivates effort but imposes uncontrollable income risk on the risk-averse agent"
    - "Minimizing monitoring costs so the principal can verify agent effort directly"
    - "Timing bonus payments to coincide with high-output periods to maximize the signaling effect"
  answer: 1
  explanation: "The core tradeoff in moral hazard theory: to incentivize unobservable effort, the agent's pay must be sensitive to outcomes (performance pay). But outcomes are partly random, so this sensitivity loads the risk-averse agent with income variance they don't control. A fully risk-averse agent optimally wants a flat salary (full insurance), but a flat salary provides zero incentive to work. The optimal contract sits between these extremes — some pay-for-performance to motivate effort, enough base pay to reduce risk exposure to an acceptable level. This tradeoff cannot be eliminated as long as effort is hidden."

- question: "Paying an agent a flat salary (the same regardless of outcomes) is the optimal contract whenever the agent is risk-averse, because it protects them from uncontrollable income variation."
  type: true-false
  answer: false
  explanation: "A flat salary is optimal from a pure risk-sharing perspective — it fully insures the risk-averse agent. But with hidden actions, a flat salary eliminates incentives entirely: if pay is independent of outcomes, the agent prefers to exert minimal effort (which reduces their private cost of effort). The optimal contract with moral hazard always involves some pay-for-performance, even for highly risk-averse agents — enough to motivate effort, though less than the full residual claim that would be optimal for a risk-neutral agent."

- question: "The term 'moral hazard' specifically refers to situations where agents behave dishonestly or unethically because their compensation structure incentivizes deception."
  type: true-false
  answer: false
  explanation: "Despite its name, moral hazard has nothing to do with ethics or dishonesty. The term originated in the insurance industry and simply describes the tendency to change behavior when the costs of certain actions are shifted to others — shirking, taking excessive risk, or reducing precautions. The agent is not deceiving anyone; they are rationally responding to changed incentives. 'Moral' is historical and misleading. What matters economically is that the action is hidden (unobservable), not whether it is morally wrong."

- question: "What is the 'efficiency loss' from moral hazard, and why can it not be fully eliminated through better contract design?"
  type: short-answer
  answer: "The efficiency loss is the gap between the first-best outcome (achievable when effort is observable) and the second-best outcome under hidden actions. When effort is observable, the principal can pay directly for effort — no risk tradeoff is needed. With hidden actions, the contract can only condition on outcomes (mixing effort and luck). To motivate effort, the agent must bear outcome risk; compensating a risk-averse agent for that risk requires a 'risk premium' — extra expected pay to accept income volatility. This deadweight cost is the efficiency loss. It cannot be eliminated as long as (1) effort is unobservable and (2) outcomes are noisy — because tying pay more tightly to outcomes both reduces efficiency loss from shirking and increases the risk premium required."
  explanation: "Moral hazard theory predicts that hidden action always produces a strictly worse outcome than observable effort. Policy responses — deductibles in insurance, performance bonuses in employment, equity stakes for executives — reduce but cannot eliminate this loss. The efficiency cost is the fundamental price of information asymmetry."
```

## Explainer

From the principal-agent model, you know the basic setup: one party (the principal) delegates a task to another (the agent), and their interests may not align. **Moral hazard** is the specific problem that arises when the agent's *actions* are hidden — the principal can observe the outcome but cannot verify whether the agent worked hard, cut corners, or took excessive risks. The term originally comes from insurance, where it described the tendency of insured people to be less careful, but the concept applies wherever effort or behavior is unobservable.

Consider a concrete example: a restaurant owner (principal) hires a manager (agent) to run the business. The owner can observe monthly revenue, but cannot monitor whether the manager is working diligently, networking to attract customers, and maintaining food quality — or whether the manager is coasting, leaving early, and cutting corners. Revenue depends on both the manager's effort and random factors (weather, local events, economic conditions). High effort makes good outcomes more likely, but does not guarantee them — and low effort does not guarantee bad outcomes either. This **randomness in the mapping from effort to outcome** is what makes moral hazard so difficult. The owner sees the result, not the cause.

If the owner could observe effort directly, the solution would be simple: pay for effort. Write a contract that says "work hard, get paid well; shirk, get fired." But with hidden action, the contract can only be conditioned on **observable outcomes** — revenue, profit, customer ratings. The principal must design a contract that gives the agent an incentive to exert effort even when no one is watching. This typically means making the agent's pay sensitive to outcomes: performance bonuses, commissions, stock options, or profit sharing. The agent bears some risk (their pay varies with outcomes they don't fully control), but this risk exposure is the price of providing incentives.

Here lies the fundamental tradeoff at the heart of moral hazard theory: **incentives versus risk-sharing**. If the agent is risk-averse (as most people are), the ideal risk-sharing arrangement would fully insure the agent — pay a flat salary regardless of outcomes. But a flat salary provides zero incentive to exert effort. Conversely, making the agent the full residual claimant (keeping all profits) provides maximal incentives but loads the agent with all the risk. The **optimal contract** balances these two forces, providing enough pay-for-performance to motivate effort while not exposing the risk-averse agent to so much volatility that they demand a huge risk premium. This optimal contract is always less efficient than what could be achieved if effort were observable — the **efficiency loss** from moral hazard is the cost of information asymmetry.

Moral hazard is pervasive in economic life. Insurance deductibles and copays exist to keep policyholders careful. CEO compensation packages tie pay to stock performance to align executive and shareholder interests. Loan covenants restrict borrower behavior to protect lenders. In each case, the contract designer faces the same problem: how to motivate unobservable good behavior through the structure of observable rewards and penalties. Understanding this problem — and the tradeoff between incentives and risk-sharing that constrains its solution — is essential for analyzing contracts, regulation, and institutional design throughout economics.
