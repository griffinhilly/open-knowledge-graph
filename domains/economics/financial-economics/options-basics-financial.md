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
status: validated
---

# Options: Calls, Puts, and Basic Payoffs

## Core Idea
An option gives its buyer the right, but not the obligation, to buy (call option) or sell (put option) an underlying asset at a specified strike price on or before the expiration date. The option seller (writer) receives a premium upfront and bears the obligation to transact if the buyer exercises. Options have asymmetric payoff profiles: the buyer's maximum loss is the premium paid, while potential gains can be large; the seller's maximum gain is the premium, with potentially large losses. Options serve two broad functions: speculation (leveraged directional bets) and hedging (insuring against adverse price movements in an existing position).

## How It's Best Learned
Draw payoff diagrams at expiration for four basic positions — long call, long put, short call, short put — and confirm the maximum profit, maximum loss, and break-even for each. Explore simple multi-leg strategies like the protective put (stock + long put) and covered call (stock + short call).

## Common Misconceptions
- The payoff diagram at expiration shows intrinsic value, not the option's market price before expiration, which also includes time value.
- Options are not purely speculative instruments — they are widely used by corporations and portfolio managers for legitimate risk management.

## Questions

```yaml
- question: "You buy a call option on a stock with a strike price of $50, paying a $3 premium. At expiration the stock is trading at $45. What is your outcome?"
  type: multiple-choice
  options:
    - "You exercise the option and lose $5 — the difference between the strike price and the market price"
    - "You lose $3 — the premium paid, which is the maximum possible loss on a long option position"
    - "You profit $3 because the option still has value since you hold the right to buy"
    - "You lose the full $50 strike price since you agreed to buy at that level"
  answer: 1
  explanation: "When the stock is below the strike at expiration, the call has zero intrinsic value — you would never pay $50 for a stock trading at $45. You simply let the option expire unexercised. Your loss is limited to the $3 premium you paid, nothing more. This is the defining asymmetry of a long option position: the maximum loss is always capped at the premium, regardless of how far the asset falls. Option A describes a common error — confusing the payoff of exercising (which you wouldn't do) with the actual outcome of letting it expire."

- question: "A portfolio manager owns $500,000 of stock in a single company. She buys put options with a strike price near the current market price. What is her most likely purpose?"
  type: multiple-choice
  options:
    - "To profit if the stock price rises sharply above the strike"
    - "To generate premium income by selling her obligation to deliver shares"
    - "To speculate on volatility without maintaining her stock position"
    - "To create a price floor on her position, limiting losses if the stock falls"
  answer: 3
  explanation: "A long put gains value when the underlying asset falls — it pays max(K − S, 0) at expiration. Held alongside a stock position, it functions as insurance: if the stock drops below the strike, the put's gains offset the stock's losses, creating a floor on total portfolio losses. This is the protective put strategy. The premium paid is the cost of insurance. This illustrates that options are not purely speculative instruments — hedging existing positions is one of their primary legitimate uses."

- question: "For a call option buyer, the maximum possible loss is the full value of the underlying asset, since the buyer agreed to a purchase price."
  type: true-false
  answer: false
  explanation: "This is a key misconception. The buyer of a call has the right but not the obligation to purchase. If the option expires worthless (stock below strike), the buyer simply walks away — they never have to pay the strike price. The maximum loss is always limited to the premium paid, regardless of what the underlying asset does. This is what makes the option buyer's position fundamentally different from owning the stock outright."

- question: "The seller (writer) of a call option faces potentially larger losses than the buyer, despite receiving the premium upfront."
  type: true-false
  answer: true
  explanation: "The call writer's maximum gain is capped at the premium received — that's all they can ever make. But their potential losses grow dollar-for-dollar as the underlying price rises above the strike, and are theoretically unlimited (a stock can rise without bound). This is the asymmetry reversed: the seller has a capped upside and uncapped downside. This asymmetry is why options exchanges require sellers to post margin — the seller bears the obligation to deliver or buy shares at a disadvantageous price if the buyer exercises."

- question: "Why is the payoff profile of an option called 'asymmetric,' and why does this asymmetry matter differently for buyers versus sellers?"
  type: short-answer
  answer: "An option's payoff is asymmetric because gains and losses respond differently depending on which direction the underlying moves. For a call buyer: if the stock rises above the strike, gains increase dollar-for-dollar; if it falls, the loss is capped at the premium no matter how far it drops. The seller has the exact mirror: gains are capped at the premium regardless of outcome, while losses grow as the stock rises. This means buyers and sellers are not taking symmetric risks — the buyer pays a premium to participate only in favorable outcomes while offloading unfavorable ones; the seller accepts the unfavorable outcomes in exchange for the premium. The asymmetry is what makes options useful for hedging: you can cap your downside while retaining upside."
  explanation: "This asymmetry also explains why the same instrument can serve completely opposite purposes: a speculator buys a call hoping for large upside; a corporate treasurer sells a covered call on stock they own to generate income while willing to give up upside above a target price. The same asymmetric payoff structure serves both."
```

## Explainer

From your study of the risk-return tradeoff, you know that every asset has a probability distribution of future payoffs, and investors accept more risk only in exchange for higher expected returns. Standard assets like stocks and bonds have approximately symmetric payoff profiles — if the market moves against you, you lose proportionally. Options introduce something fundamentally different: **asymmetric payoffs**, where the relationship between the underlying asset's price and your profit and loss is kinked rather than linear. This asymmetry is both the source of options' power and the reason they require careful conceptual grounding.

A **call option** gives its buyer the right, but not the obligation, to purchase the underlying asset at a predetermined **strike price** (K) on or before the **expiration date**. The buyer pays a **premium** upfront for this right. At expiration, the call's payoff is max(S − K, 0), where S is the asset's current price. If the stock rises to $120 and the strike is $100, the call is worth $20 (the buyer can buy at $100 and immediately sell at $120). If the stock falls to $80, the call expires worthless — the buyer simply loses the premium they paid and exercises no obligation. This is the defining feature: the buyer's downside is capped at the premium, while the upside tracks the asset's price gain above the strike.

A **put option** is the mirror image: the right to sell the underlying at the strike price. Its payoff at expiration is max(K − S, 0). If you own a stock trading at $80 and you hold a put with a strike of $100, you can sell at $100 even though the market price is $80 — a $20 gain on the put, which offsets part of your stock loss. This is exactly how put options function as insurance: you pay the premium (like an insurance premium) and collect the payoff if disaster strikes (the price falls). A **protective put** — holding the stock plus a long put — creates a portfolio with a floor on losses. A **covered call** — holding the stock plus writing (selling) a call — generates premium income in exchange for capping upside if the stock rallies sharply.

The four basic positions — long call, long put, short call, short put — have distinct payoff profiles at expiration that form the building blocks of all options strategies. Long positions (buying options) give you the kinked hockey-stick payoff: flat below or above the strike, then rising. Short positions (writing options) are the mirror image — you collect the premium upfront and face potential obligations that can be large. A **short call** (selling a call without owning the underlying) has theoretically unlimited risk if the asset price surges, because you must deliver shares at a price below market. A **short put** has risk limited only by the asset price falling to zero. This asymmetry explains why options markets require margins from sellers. Before expiration, an option's market value also includes **time value** — the extra premium beyond intrinsic value (max(S−K,0) for calls) that reflects the probability of favorable price movements before expiry. As expiration approaches, time value decays — a phenomenon that is central to options pricing and explored fully in the Black-Scholes model you'll encounter next.
