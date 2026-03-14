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
