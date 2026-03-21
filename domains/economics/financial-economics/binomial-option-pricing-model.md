---
id: binomial-option-pricing-model
title: Binomial Option Pricing and Replicating Portfolios
domain: economics
course: financial-economics
prerequisites:
- id: call-and-put-options-mechanics
  type: hard
- id: option-intrinsic-and-time-value
  type: hard
- id: binomial-distribution
  type: soft
- id: binomial-coefficients
  type: soft
- id: probability-theory
  type: hard
- id: recursion
  type: soft
tags:
- options
- option-pricing
- replicating-portfolio
stage: formal-systems
status: draft
---

# Binomial Option Pricing and Replicating Portfolios

## Core Idea
The binomial model assumes stock price moves up (u) or down (d) in each period. An option is priced by replicating its payoff using stock and bond; the replicating portfolio's cost equals option price. Risk-neutral probability (p*) makes expected return equal to the risk-free rate.

## How It's Best Learned
Value a one-period option by constructing a replicating portfolio. Then extend to multi-period binomial trees and verify that option value converges to Black-Scholes as time steps increase.

## Questions

```yaml
- question: "Two analysts are pricing a call option using the binomial model. Analyst A believes the stock will rise with 80% probability; Analyst B believes 30%. Who will compute the higher option price?"
  type: multiple-choice
  options:
    - "Analyst A — higher real-world probability of a rise increases expected payoff"
    - "Analyst B — lower probability makes the option more of a hedge, increasing its value"
    - "Neither — the real-world probability is not an input to the binomial option price"
    - "It depends on the strike price relative to the current stock price"
  answer: 2
  explanation: "The real-world probability of the stock rising has no role in the binomial pricing formula. Option price is determined by the replicating portfolio — Δ shares + bond — which is derived entirely from the up/down factors (u and d), the current stock price, and the risk-free rate. The risk-neutral probability p* is a mathematical construct that replaces the real-world probability; it is calibrated to make expected stock return equal the risk-free rate, not to reflect anyone's beliefs. Both analysts will compute identical prices if they share the same S, u, d, K, and r."

- question: "A call option has the following binomial payoffs: Cᵤ = $10 (up state), Cᵈ = $0 (down state). You construct a replicating portfolio of Δ shares and a bond. If this portfolio currently costs $4, what must the option's price be?"
  type: multiple-choice
  options:
    - "More than $4, to compensate the seller for risk"
    - "Less than $4, since the option only pays in one state"
    - "Exactly $4, by the no-arbitrage principle"
    - "Exactly $5, since the expected payoff is $5 under equal probabilities"
  answer: 2
  explanation: "By the no-arbitrage principle, two portfolios with identical payoffs in every state must have the same current price. The replicating portfolio is constructed to match the option's payoff exactly in both the up and down state. If the option priced above or below $4, you could buy the cheaper one and sell the more expensive one to lock in a riskless profit — a contradiction in an arbitrage-free market. Option pricing is thus a consequence of no-arbitrage, not of expected-value calculations."

- question: "In the binomial model, a call option on a stock is worth more if investors collectively believe the stock is more likely to rise."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about option pricing. The binomial model prices options through replication — finding a portfolio of stock and bonds that perfectly matches the option's payoffs. The cost of that portfolio depends on the up/down factors (u and d), the current stock price, and the risk-free rate. Real-world beliefs about probabilities are irrelevant because the hedge ratio Δ and bond position B are uniquely determined by no-arbitrage, regardless of what investors believe. The risk-neutral probability p* is not a belief — it is a mathematical tool that produces the same answer as the replicating portfolio method."

- question: "The cost of the replicating portfolio must equal the option's price; if it did not, a trader could construct a riskless profit."
  type: true-false
  answer: true
  explanation: "This is the no-arbitrage foundation of the model. If the option traded above the replicating portfolio cost, you could sell the option and buy the replicating portfolio, locking in the difference risk-free (the replicating portfolio covers all obligations). If the option traded below, you could buy the option and short the replicating portfolio. In both cases, the position has zero net cash flow at expiration but positive cash flow today — a riskless profit. Competitive markets eliminate such opportunities, forcing the option price to equal the replicating portfolio cost exactly."

- question: "Why doesn't the real-world probability of the stock rising affect the option price in the binomial model? What does determine the price instead?"
  type: short-answer
  answer: "The option price is determined by the cost of the replicating portfolio — a combination of Δ shares and a bond position that exactly replicates the option's payoff in every state. This Δ and bond position are uniquely solved from the up/down payoffs and the up/down stock prices, with no reference to how likely each state is. The risk-free rate, current stock price, and up/down factors (u and d) fully determine the price. Real-world probabilities are irrelevant because any option price inconsistent with the replicating portfolio cost would permit riskless arbitrage, which the market eliminates."
  explanation: "This non-intuitive result — that beliefs don't matter — is the central insight of modern derivatives pricing. It follows from no-arbitrage: since the replicating portfolio costs what it costs regardless of probabilities, the option must too. The risk-neutral probability p* is a convenient reformulation of this same no-arbitrage condition, not a belief anyone holds."
```

## Explainer

You already know that a call option gives the right to buy an asset at a fixed **strike price** K before expiration, and that its value depends on the gap between the current stock price and K, adjusted for time and uncertainty. What the binomial model does is provide a precise, no-arbitrage method to determine what that value must be — not by guessing expected returns, but by finding the portfolio that perfectly replicates the option's payoff.

Start with the simplest case: a single period. A stock currently trades at S. Next period it either rises to S·u (up factor) or falls to S·d (down factor), where u > 1 > d. A call option with strike K expires at the end of the period. In the up state the option pays Cᵤ = max(S·u − K, 0); in the down state it pays Cᵈ = max(S·d − K, 0). The **replicating portfolio** holds Δ shares of stock and a position B in a riskless bond. Set Δ and B so the portfolio exactly replicates both payoffs: Δ·S·u + B·(1+r) = Cᵤ and Δ·S·d + B·(1+r) = Cᵈ. Solving gives a unique Δ (the **hedge ratio** or **delta** of the option) and a unique B. By no-arbitrage, the option must cost exactly Δ·S + B today — if it traded for more or less, you could lock in a riskless profit.

A cleaner way to express the same result uses **risk-neutral probabilities**. Define p* = [(1+r) − d] / [u − d]. This is the probability that makes the expected return on the stock equal to the risk-free rate — it is not the real-world probability that the stock rises. Under this artificial probability, the option price is simply the discounted expected payoff: C = [p*·Cᵤ + (1−p*)·Cᵈ] / (1+r). The real-world probability of an up move plays no role in pricing. This is the central insight: option prices depend on the risk-free rate, current stock price, and the up/down factors — not on what investors believe the stock will actually do.

Multi-period pricing works by backward induction. Build a tree of stock prices at each node. At expiration, compute option payoffs at each terminal node. Then work backward: at each intermediate node, apply the one-period formula to find the option value as the discounted risk-neutral expectation of the two next-period values. This recursion is exactly the **recursion** concept from your prerequisites — the value at any node depends only on the values at the nodes it leads to. As you subdivide time into more and more short intervals (more binomial steps), the binomial tree converges to the continuous-time **Black-Scholes** formula, making the binomial model both an intuitive teaching device and a legitimate precursor to continuous finance.
