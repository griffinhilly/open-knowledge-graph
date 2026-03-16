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

## Explainer

From your study of the risk-return tradeoff, you know that every asset has a probability distribution of future payoffs, and investors accept more risk only in exchange for higher expected returns. Standard assets like stocks and bonds have approximately symmetric payoff profiles — if the market moves against you, you lose proportionally. Options introduce something fundamentally different: **asymmetric payoffs**, where the relationship between the underlying asset's price and your profit and loss is kinked rather than linear. This asymmetry is both the source of options' power and the reason they require careful conceptual grounding.

A **call option** gives its buyer the right, but not the obligation, to purchase the underlying asset at a predetermined **strike price** (K) on or before the **expiration date**. The buyer pays a **premium** upfront for this right. At expiration, the call's payoff is max(S − K, 0), where S is the asset's current price. If the stock rises to $120 and the strike is $100, the call is worth $20 (the buyer can buy at $100 and immediately sell at $120). If the stock falls to $80, the call expires worthless — the buyer simply loses the premium they paid and exercises no obligation. This is the defining feature: the buyer's downside is capped at the premium, while the upside tracks the asset's price gain above the strike.

A **put option** is the mirror image: the right to sell the underlying at the strike price. Its payoff at expiration is max(K − S, 0). If you own a stock trading at $80 and you hold a put with a strike of $100, you can sell at $100 even though the market price is $80 — a $20 gain on the put, which offsets part of your stock loss. This is exactly how put options function as insurance: you pay the premium (like an insurance premium) and collect the payoff if disaster strikes (the price falls). A **protective put** — holding the stock plus a long put — creates a portfolio with a floor on losses. A **covered call** — holding the stock plus writing (selling) a call — generates premium income in exchange for capping upside if the stock rallies sharply.

The four basic positions — long call, long put, short call, short put — have distinct payoff profiles at expiration that form the building blocks of all options strategies. Long positions (buying options) give you the kinked hockey-stick payoff: flat below or above the strike, then rising. Short positions (writing options) are the mirror image — you collect the premium upfront and face potential obligations that can be large. A **short call** (selling a call without owning the underlying) has theoretically unlimited risk if the asset price surges, because you must deliver shares at a price below market. A **short put** has risk limited only by the asset price falling to zero. This asymmetry explains why options markets require margins from sellers. Before expiration, an option's market value also includes **time value** — the extra premium beyond intrinsic value (max(S−K,0) for calls) that reflects the probability of favorable price movements before expiry. As expiration approaches, time value decays — a phenomenon that is central to options pricing and explored fully in the Black-Scholes model you'll encounter next.
