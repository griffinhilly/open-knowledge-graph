---
id: options-basics-financial
title: 'Options: Calls, Puts, and Basic Payoffs'
domain: economics
course: financial-economics
prerequisites:
- id: risk-and-return-tradeoff
  type: hard
- id: bond-basics
  type: soft
builds-toward:
- options-payoff-diagrams
- black-scholes-model
tags:
- options
- derivatives
- calls
- puts
- strike-price
- hedging
stage: formal-systems
status: draft
---

# Options: Calls, Puts, and Basic Payoffs

## Core Idea
An option gives its buyer the right, but not the obligation, to buy (call option) or sell (put option) an underlying asset at a specified strike price on or before the expiration date. The option seller (writer) receives a premium upfront and bears the obligation to transact if the buyer exercises. Options have asymmetric payoff profiles: the buyer's maximum loss is the premium paid, while potential gains can be large; the seller's maximum gain is the premium, with potentially large losses. Options serve two broad functions: speculation (leveraged directional bets) and hedging (insuring against adverse price movements in an existing position).

## How It's Best Learned
Draw payoff diagrams at expiration for four basic positions — long call, long put, short call, short put — and confirm the maximum profit, maximum loss, and break-even for each. Explore simple multi-leg strategies like the protective put (stock + long put) and covered call (stock + short call).

## Common Misconceptions
- The payoff diagram at expiration shows intrinsic value, not the option's market price before expiration, which also includes time value.
- Options are not purely speculative instruments — they are widely used by corporations and portfolio managers for legitimate risk management.
