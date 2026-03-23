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
status: validated
---

# Call and Put Options: Rights, Exercise, and Payoffs

## Core Idea
A call option gives the right (not obligation) to buy at a strike price; a put gives the right to sell. European options exercise only at maturity; American options exercise anytime. Payoffs are call = max(S − K, 0) and put = max(K − S, 0), where S is stock price and K is strike.

## How It's Best Learned
Draw payoff diagrams for long/short calls and puts at various strikes. Calculate payoffs at different stock prices and understand when exercise is optimal.

## Questions

```yaml
- question: "You hold an American call option on a stock with strike K = $60. The stock currently trades at $75. A friend says 'Exercise now and lock in your $15 profit before the price drops.' What is wrong with this advice?"
  type: multiple-choice
  options:
    - "Nothing — exercising immediately is always optimal for in-the-money American calls"
    - "Early exercise sacrifices the option's time value; the option is worth more than $15 alive, so selling it in the market dominates early exercise"
    - "You cannot exercise an American call when the stock is above the strike price"
    - "The $15 gain is not real profit until you separately sell the acquired shares"
  answer: 1
  explanation: "An in-the-money option has both intrinsic value ($15 = S − K) and time value. Early exercise captures only the intrinsic value and forfeits the time value. For a non-dividend-paying stock, it is almost never optimal to exercise an American call early — you are better off selling the option itself for more than $15. The friend's advice treats the option as if it were the stock, ignoring the option's remaining optionality."

- question: "You buy a put option with strike K = $40 for a premium of $3. At expiration, the stock is at $35. What is your net profit per share?"
  type: multiple-choice
  options:
    - "−$3 (the option expires worthless)"
    - "+$2 (put payoff of $5 minus $3 premium)"
    - "+$5 (the full put payoff)"
    - "−$5 (you are obligated to sell at $40)"
  answer: 1
  explanation: "Put payoff = max(K − S, 0) = max(40 − 35, 0) = $5. You exercise because K > S. Net profit = $5 payoff − $3 premium = $2. Option A is wrong because S < K so the put is in-the-money and will be exercised. Option D reflects the fundamental misconception that options create obligations — the put buyer has a RIGHT to sell, not an obligation."

- question: "A put option becomes more valuable as the underlying stock price rises."
  type: true-false
  answer: false
  explanation: "Put payoff = max(K − S, 0). As S rises above K, the payoff goes to zero — the put moves out of the money and loses value. Puts are bearish instruments that profit when the stock falls below the strike price. Calls increase in value when the stock rises; puts increase in value when the stock falls."

- question: "The maximum loss for the buyer of a call option is limited to the premium paid, regardless of what happens to the underlying stock price."
  type: true-false
  answer: true
  explanation: "The call buyer holds a RIGHT but not an OBLIGATION to buy. If the stock falls below the strike at expiration, they simply don't exercise — the option expires worthless, and the loss is exactly the premium paid, nothing more. This is the asymmetry that defines options: the buyer's downside is capped at the premium while the upside is theoretically unlimited (for calls) or large (for puts)."

- question: "Why is the 'right but not obligation' feature of options fundamental to understanding their payoff structure? How does it create the asymmetric risk profiles for buyers versus sellers?"
  type: short-answer
  answer: "Holders exercise only when it benefits them — when S > K for calls or K > S for puts — so the payoff is never negative: max(S − K, 0) and max(K − S, 0). This means buyers face limited downside (premium paid) and potentially large upside. Sellers take the opposite side: they collect the premium but face the buyer's upside as their potential loss. For call sellers, this loss is theoretically unlimited as S can rise without bound. This zero-sum asymmetry at expiration is what makes options useful for hedging: one party transfers risk and pays a premium; the other bears the risk in exchange for the premium."
  explanation: "The right-not-obligation structure is what distinguishes options from futures or forward contracts, where both parties have obligations. It is precisely this optionality that gives options their characteristic payoff shape and makes them powerful but also often misunderstood."
```

## Explainer

From your study of options basics and payoff diagrams, you know that options are contracts giving the holder a right without an obligation. Let's sharpen exactly what that right looks like for calls and puts, when you would use it, and how the payoff formulas encode those decisions.

A **call option** gives you the right to buy an asset at a predetermined **strike price** K. Suppose you hold a call on a stock with K = $50. If the stock price S at expiration is $70, you exercise: you pay $50 for something worth $70, pocketing a $20 gain per share. If S = $40, you do nothing — you would not pay $50 for something worth $40 when you can simply buy it in the market for $40. This is the max(S − K, 0) payoff formula in action: exercise when S > K, walk away when S ≤ K. The right, not obligation, is what caps your downside at zero.

A **put option** is the mirror image: the right to sell at strike K. If S = $30 and K = $50, you exercise by selling something worth $30 for $50 — a $20 gain. If S = $60, there is no point selling at $50 when you could sell in the market for $60, so you let the put expire. Payoff: max(K − S, 0). Puts increase in value when the underlying falls; calls increase in value when the underlying rises. This asymmetry is the defining feature of options: unlimited upside (for calls) or large downside protection (for puts), with losses capped at the premium paid.

The **European versus American** distinction matters for when exercise can happen. European options can only be exercised at expiration; American options can be exercised at any point before expiration. For a non-dividend-paying stock, it is almost never optimal to exercise an American call early — the option has **time value** that you sacrifice by exercising before maturity. Early exercise of American puts can be optimal, however: if a stock collapses near zero, you might prefer the certainty of the K − S payoff now rather than waiting while time value decays.

The payoff diagrams you drew in your prerequisite course encode a crucial point about who bears risk. The long call buyer has a limited loss (premium paid) and theoretically unlimited gain. The short call writer — the person on the other side — has limited gain (premium received) and unlimited potential loss. Long and short positions in the same option are perfect opposites in their risk profiles. This zero-sum structure at expiration is why options are central to hedging: for every risk-taker who wants exposure to a price move, there is a hedger who wants to transfer that exact risk away.
