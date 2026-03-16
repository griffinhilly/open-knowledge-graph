---
id: call-and-put-options-mechanics
title: 'Call and Put Options: Rights, Exercise, and Payoffs'
domain: economics
course: financial-economics
prerequisites:
- id: options-basics-financial
  type: hard
- id: options-payoff-diagrams
  type: hard
builds-toward:
- option-intrinsic-and-time-value
tags:
- options
- derivatives
- payoff-analysis
stage: formal-systems
status: draft
---

# Call and Put Options: Rights, Exercise, and Payoffs

## Core Idea
A call option gives the right (not obligation) to buy at a strike price; a put gives the right to sell. European options exercise only at maturity; American options exercise anytime. Payoffs are call = max(S − K, 0) and put = max(K − S, 0), where S is stock price and K is strike.

## How It's Best Learned
Draw payoff diagrams for long/short calls and puts at various strikes. Calculate payoffs at different stock prices and understand when exercise is optimal.

## Explainer

From your study of options basics and payoff diagrams, you know that options are contracts giving the holder a right without an obligation. Let's sharpen exactly what that right looks like for calls and puts, when you would use it, and how the payoff formulas encode those decisions.

A **call option** gives you the right to buy an asset at a predetermined **strike price** K. Suppose you hold a call on a stock with K = $50. If the stock price S at expiration is $70, you exercise: you pay $50 for something worth $70, pocketing a $20 gain per share. If S = $40, you do nothing — you would not pay $50 for something worth $40 when you can simply buy it in the market for $40. This is the max(S − K, 0) payoff formula in action: exercise when S > K, walk away when S ≤ K. The right, not obligation, is what caps your downside at zero.

A **put option** is the mirror image: the right to sell at strike K. If S = $30 and K = $50, you exercise by selling something worth $30 for $50 — a $20 gain. If S = $60, there is no point selling at $50 when you could sell in the market for $60, so you let the put expire. Payoff: max(K − S, 0). Puts increase in value when the underlying falls; calls increase in value when the underlying rises. This asymmetry is the defining feature of options: unlimited upside (for calls) or large downside protection (for puts), with losses capped at the premium paid.

The **European versus American** distinction matters for when exercise can happen. European options can only be exercised at expiration; American options can be exercised at any point before expiration. For a non-dividend-paying stock, it is almost never optimal to exercise an American call early — the option has **time value** that you sacrifice by exercising before maturity. Early exercise of American puts can be optimal, however: if a stock collapses near zero, you might prefer the certainty of the K − S payoff now rather than waiting while time value decays.

The payoff diagrams you drew in your prerequisite course encode a crucial point about who bears risk. The long call buyer has a limited loss (premium paid) and theoretically unlimited gain. The short call writer — the person on the other side — has limited gain (premium received) and unlimited potential loss. Long and short positions in the same option are perfect opposites in their risk profiles. This zero-sum structure at expiration is why options are central to hedging: for every risk-taker who wants exposure to a price move, there is a hedger who wants to transfer that exact risk away.
