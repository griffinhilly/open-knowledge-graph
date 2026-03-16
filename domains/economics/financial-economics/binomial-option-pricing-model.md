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

## Explainer

You already know that a call option gives the right to buy an asset at a fixed **strike price** K before expiration, and that its value depends on the gap between the current stock price and K, adjusted for time and uncertainty. What the binomial model does is provide a precise, no-arbitrage method to determine what that value must be — not by guessing expected returns, but by finding the portfolio that perfectly replicates the option's payoff.

Start with the simplest case: a single period. A stock currently trades at S. Next period it either rises to S·u (up factor) or falls to S·d (down factor), where u > 1 > d. A call option with strike K expires at the end of the period. In the up state the option pays Cᵤ = max(S·u − K, 0); in the down state it pays Cᵈ = max(S·d − K, 0). The **replicating portfolio** holds Δ shares of stock and a position B in a riskless bond. Set Δ and B so the portfolio exactly replicates both payoffs: Δ·S·u + B·(1+r) = Cᵤ and Δ·S·d + B·(1+r) = Cᵈ. Solving gives a unique Δ (the **hedge ratio** or **delta** of the option) and a unique B. By no-arbitrage, the option must cost exactly Δ·S + B today — if it traded for more or less, you could lock in a riskless profit.

A cleaner way to express the same result uses **risk-neutral probabilities**. Define p* = [(1+r) − d] / [u − d]. This is the probability that makes the expected return on the stock equal to the risk-free rate — it is not the real-world probability that the stock rises. Under this artificial probability, the option price is simply the discounted expected payoff: C = [p*·Cᵤ + (1−p*)·Cᵈ] / (1+r). The real-world probability of an up move plays no role in pricing. This is the central insight: option prices depend on the risk-free rate, current stock price, and the up/down factors — not on what investors believe the stock will actually do.

Multi-period pricing works by backward induction. Build a tree of stock prices at each node. At expiration, compute option payoffs at each terminal node. Then work backward: at each intermediate node, apply the one-period formula to find the option value as the discounted risk-neutral expectation of the two next-period values. This recursion is exactly the **recursion** concept from your prerequisites — the value at any node depends only on the values at the nodes it leads to. As you subdivide time into more and more short intervals (more binomial steps), the binomial tree converges to the continuous-time **Black-Scholes** formula, making the binomial model both an intuitive teaching device and a legitimate precursor to continuous finance.
