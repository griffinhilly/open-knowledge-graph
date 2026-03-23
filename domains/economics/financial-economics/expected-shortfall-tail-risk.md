---
id: expected-shortfall-tail-risk
title: Expected Shortfall and Tail Risk Measurement
domain: economics
course: financial-economics
prerequisites:
- id: value-at-risk-measurement
  type: hard
- id: risk-and-return-tradeoff
  type: soft
builds-toward:
- risk-and-return-tradeoff
tags:
- risk-management
- var
- tail-risk
- measurement
stage: formal-systems
status: validated
---

# Expected Shortfall and Tail Risk Measurement

## Core Idea
Expected shortfall (ES) or conditional value-at-risk measures the expected loss in the tail beyond the VaR threshold, addressing VaR's key weakness: it ignores loss severity. ES = E[Loss | Loss > VaR], and is coherent, satisfying desirable risk measure properties that VaR violates. ES is increasingly preferred for capital allocation and stress testing in regulated financial institutions.

## How It's Best Learned
Calculate both VaR and ES for a portfolio at the same confidence level and observe how ES better captures tail risk from extreme scenarios.

## Questions

```yaml
- question: "Portfolio A has a 99% VaR of $10M with a maximum possible loss of $12M. Portfolio B also has a 99% VaR of $10M, but its maximum possible loss is $200M. How do their Expected Shortfall values compare?"
  type: multiple-choice
  options:
    - "Both have the same ES since they have identical VaR at the same confidence level"
    - "Portfolio A has higher ES because its tail is more concentrated near the VaR threshold"
    - "Portfolio B has higher ES because its tail extends far beyond the VaR threshold"
    - "ES cannot be compared without knowing the exact shape of each distribution"
  answer: 2
  explanation: "VaR only marks where the tail begins — it says nothing about what is inside the tail. ES averages all losses beyond the VaR threshold. Portfolio A's tail spans $2M above VaR; Portfolio B's tail spans $190M above VaR. ES integrates over the entire tail, so Portfolio B's ES is dramatically higher despite identical VaR. This is precisely the failure VaR has that ES corrects: two radically different risk profiles appear identical under VaR."

- question: "Two portfolios each have a 99% VaR of $3M. A risk manager combines them into a single portfolio. What does VaR's violation of subadditivity imply about the combined VaR?"
  type: multiple-choice
  options:
    - "The combined VaR must be exactly $6M by the additivity of risk measures"
    - "The combined VaR must be at most $6M because diversification always reduces risk"
    - "The combined VaR could theoretically exceed $6M, violating the intuition that diversification helps"
    - "The combined VaR must be less than $6M because correlations are never perfectly positive"
  answer: 2
  explanation: "VaR violates subadditivity — the property that the risk of a combined portfolio should be no greater than the sum of its parts. It is mathematically possible to construct two portfolios where their individual VaRs are low but their combined VaR is high. This is not just theoretical: it could incentivize splitting portfolios to game capital requirements. Expected Shortfall is subadditive by construction, making it a more defensible basis for capital allocation."

- question: "Expected Shortfall is preferred over VaR for capital allocation in part because ES captures how severe losses are in extreme scenarios, not just how likely they are to exceed a threshold."
  type: true-false
  answer: true
  explanation: "This is the core distinction. VaR answers 'how likely is a loss bigger than X?' — ES answers 'when losses are extreme, how extreme are they on average?' For capital adequacy, you need to hold enough capital to absorb the actual severity of bad outcomes. ES computes E[Loss | Loss > VaR], integrating over the entire tail. VaR only marks the threshold. Regulators (Basel III/IV) shifted to ES precisely because tail severity, not just tail probability, determines how much capital is needed."

- question: "Two portfolios with identical VaR at the same confidence level must have identical risk profiles."
  type: true-false
  answer: false
  explanation: "VaR gives no information about the shape or severity of losses beyond the threshold. Two portfolios can have identical VaR but radically different tails — one with losses clustering just above the threshold, another with a small probability of catastrophic losses far into the tail. ES distinguishes these; VaR does not. This is why identical VaR is not sufficient evidence of equivalent risk, and why ES is increasingly required for regulatory capital calculations."

- question: "Explain why VaR fails to distinguish between a 'mild tail' and a 'catastrophic tail,' and how Expected Shortfall corrects this."
  type: short-answer
  answer: "VaR marks the loss level exceeded a given percentage of the time — it tells you where the tail begins, not what is inside it. A portfolio with maximum losses of $6M and one with maximum losses of $600M can have identical VaR if both exceed the threshold with equal frequency. Expected Shortfall corrects this by computing E[Loss | Loss > VaR]: the average loss across all scenarios in the tail. A heavier, more severe tail produces a higher ES even when VaR is identical, because ES integrates over tail severity rather than just marking the threshold."
  explanation: "Practically, this matters most for capital adequacy and stress testing. The question is not just 'how often will we lose more than $X?' but 'when we do, how much do we lose on average?' ES forces institutions to model and hold capital against tail severity. This is why the Basel framework shifted from VaR to ES — a bank that holds capital based on VaR is prepared for the frequency of large losses, but not necessarily their magnitude when they occur."
```

## Explainer

From your study of Value at Risk, you know that VaR at a given confidence level (say 99%) answers the question: what is the worst loss I can expect on 99% of trading days? If a portfolio's 1-day 99% VaR is $5 million, it means losses will exceed $5 million only 1% of the time. This is a useful threshold measure — it tells you the cutoff point where the tail begins. But VaR says nothing about what happens *inside* that worst 1% of scenarios. A portfolio could have a 99% VaR of $5 million with a maximum possible loss of $6 million (a mild tail), or with a maximum possible loss of $500 million (a catastrophic tail). The VaR number is identical in both cases.

**Expected shortfall (ES)**, also called **conditional value at risk (CVaR)**, fixes this blind spot by asking: given that we are in the worst 1% of scenarios, what is the average loss? Formally, ES at the α confidence level equals E[Loss | Loss > VaR_α] — the expected value of the loss distribution, conditional on losses exceeding the VaR threshold. This turns the threshold into a window: instead of just marking where the tail begins, ES integrates over the entire tail and reports its average severity. Using the rain analogy from risk-return: VaR tells you there is a 1% chance of more than 2 inches of rain; ES tells you that when it does exceed 2 inches, it averages 3.5 inches.

The technical importance of ES over VaR relates to a property called **coherence**. A coherent risk measure satisfies four axioms that any reasonable measure of portfolio risk should obey; the most practically important is **subadditivity** — the risk of a combined portfolio should be no greater than the sum of the risks of its parts. Subadditivity formalizes the principle that diversification reduces risk. VaR violates subadditivity: it is mathematically possible to construct two portfolios such that their individual VaRs are low but their combined VaR is high, implying that merging them increases measured risk. This is not just a theoretical curiosity — it could incentivize institutions to split portfolios to game capital requirements. ES is subadditive and passes all four coherence axioms, making it a more defensible basis for capital allocation and risk aggregation across business units.

In practice, ES is computed differently depending on whether you use a **parametric** or **historical simulation** approach. Under a parametric normal distribution, ES has a closed-form expression: at the 99% confidence level, ES = μ + σ × φ(z_α)/α, where φ is the normal PDF and z_α is the critical value. Under historical simulation, you identify all scenarios in the worst 1% of the historical return distribution and average their losses — no distributional assumption needed. Under a fat-tailed distribution (like a Student-t, which better describes financial returns), both VaR and ES are larger than the normal distribution predicts, with ES being more sensitive to the tail shape. This sensitivity to tail structure is both ES's strength (it reflects catastrophic scenarios more accurately) and a practical challenge (tail distributions are hard to estimate with limited historical data). Regulators, including the Basel III/IV framework, have shifted from VaR to ES for bank capital requirements precisely because ES forces institutions to confront — and hold capital against — the severity of extreme losses, not just their probability.
