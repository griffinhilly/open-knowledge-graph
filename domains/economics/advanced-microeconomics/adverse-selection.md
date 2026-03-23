---
id: adverse-selection
title: Adverse Selection
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games
  type: hard
- id: principal-agent-model
  type: hard
- id: bayes-theorem
  type: soft
- id: conditional-probability
  type: soft
- id: probability-axioms
  type: soft
builds-toward:
- lemons-market
- signaling-games
tags:
- contract-theory
- hidden-information
- information-asymmetry
stage: expert
status: validated
---

# Adverse Selection

## Core Idea
Adverse selection occurs when one party has private information about their type/quality and this affects contracting. Example: insurance buyers know health risk better than insurers. High-risk types seek coverage eagerly; insurers cannot distinguish types. Standard contracts collapse (high risks drive out low risks). Solutions: screening (insurer offers menu of contracts) or signaling (informed party reveals type).

## Questions

```yaml
- question: "In the classic adverse selection insurance model, why does a single pooling contract (priced at average risk) tend to be unstable?"
  type: multiple-choice
  options: ["High-risk types refuse to buy insurance at any price", "High-risk types over-buy while low-risk types drop out, raising average claims above the pooled premium", "Low-risk types voluntarily cross-subsidize high-risk types", "Regulators prohibit average-cost pricing in insurance markets"]
  answer: 1
  explanation: "At a premium reflecting average risk, the contract is a good deal for high-risk individuals (who expect to collect more than they pay) but overpriced for low-risk individuals (who expect to collect less). Low-risk types exit, leaving a riskier pool. The insurer must raise premiums to cover actual costs, which drives out more low-risk types — a death spiral. This adverse selection dynamic is why a single pooling contract is unstable in competitive markets."

- question: "Adverse selection is a pre-contractual problem (hidden type), while moral hazard is a post-contractual problem (hidden action)."
  type: true-false
  answer: true
  explanation: "Adverse selection arises from private information that exists *before* contracting — the informed party's type (risk level, quality, ability) influences who self-selects into the contract. Moral hazard arises *after* the contract is signed, when the insured party changes their behavior because they are now protected. Both are asymmetric information problems, but the timing and the nature of the hidden information differ fundamentally."

- question: "What is a separating equilibrium in the context of adverse selection, and why does it solve the information problem?"
  type: short-answer
  answer: "A separating equilibrium is a menu of contracts designed so each type of agent self-selects the contract intended for them. High-risk types choose the full-coverage, high-premium contract; low-risk types choose a partial-coverage, low-premium contract — and neither type wants to mimic the other. The uninformed party (insurer) can then infer each agent's type from their contract choice, effectively revealing the private information through incentive-compatible design."
  explanation: "The key mechanism is that the low-risk contract must be distorted — less than full coverage — to make it unattractive to high-risk types who would otherwise mimic low-risk buyers. This distortion creates an efficiency loss (low-risk types are under-insured relative to the full-information optimum), which is the unavoidable cost of screening under asymmetric information."
```

## Explainer

You have learned from Bayesian games and the principal-agent model that strategic interaction looks very different when one party holds private information. Adverse selection is the specific problem that arises when this information concerns a fixed characteristic — a *type* — that exists before any contract is signed. The classic setting is insurance: each buyer knows their own health risk, but the insurer can only observe the population distribution. A high-risk person knows they are likely to file large claims; a low-risk person knows they are unlikely to. The insurer knows that some buyers are high-risk and some are low-risk, but cannot tell them apart.

The trouble begins when the insurer tries to offer a single contract at a price reflecting the average risk in the population. For high-risk buyers, this is a great deal — they will likely collect more in claims than they pay in premiums. For low-risk buyers, it is a bad deal — they are effectively subsidizing the high-risk group. Rational low-risk buyers drop out of the market, leaving a riskier pool. The insurer now faces a pool that is worse than average and must raise prices, which pushes out more low-risk buyers. This unraveling logic — which Akerlof famously analyzed in the market for used cars ("lemons") — shows that adverse selection can cause markets to collapse entirely or serve only the worst risks.

Two solutions have been studied extensively. *Screening* is initiated by the uninformed party (the insurer): rather than offering one contract, the insurer designs a *menu* of contracts. Full coverage at a high premium is attractive to high-risk types; partial coverage at a low premium is designed to attract low-risk types. Crucially, the contracts are designed so that each type prefers the contract meant for them — this is the incentive-compatibility constraint. The resulting *separating equilibrium* effectively extracts the private information through self-selection, but at a cost: the low-risk contract must be distorted below full coverage to deter high-risk mimics, creating an efficiency loss relative to the full-information benchmark.

*Signaling*, by contrast, is initiated by the informed party. Rather than being screened, the high-quality agent voluntarily takes a costly action that only high types can afford (e.g., getting an expensive education, posting a bond, offering a warranty). If the signal is credible — if low-quality types cannot profitably mimic it — the signal separates types and credibly communicates private information. Signaling games, which you will study next, formalize the conditions under which such equilibria exist.

A key institutional implication is that mandatory participation can restore efficiency. If everyone must buy insurance (as in social insurance systems), the adverse selection death spiral is broken — low-risk types cannot exit, so the pooling premium is stable. This is part of the economic rationale for mandatory health insurance coverage requirements, even from a purely efficiency standpoint, separate from any distributional motivation.
