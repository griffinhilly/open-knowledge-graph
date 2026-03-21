---
id: futures-and-forward-contracts
title: Futures and Forward Contracts
domain: economics
course: financial-economics
prerequisites:
- id: present-value-and-discounting
  type: hard
- id: options-basics-financial
  type: soft
builds-toward:
- forward-pricing-cost-of-carry
- hedging-with-derivatives
tags:
- derivatives
- futures
- forwards
stage: formal-systems
status: draft
---

# Futures and Forward Contracts

## Core Idea
Futures are standardized exchange-traded contracts obligating delivery of an asset at a future date at an agreed-upon price. Forwards are OTC equivalents. Both lock in prices but differ in standardization, liquidity, and margin requirements. Futures enable hedging, speculation, and arbitrage in commodity, stock, and interest rate markets.

## Questions

```yaml
- question: "A wheat farmer enters a forward contract to sell 10,000 bushels at $4.80 in six months. At harvest, the market price is $3.50. What has the forward contract done for the farmer?"
  type: multiple-choice
  options:
    - "The farmer gains: the contract obligates the buyer to pay $4.80, above the market price — $1.30/bushel more than the market would give"
    - "The farmer loses: the contract obligates the farmer to sell below the fair market value of $5.00 at the time of writing"
    - "The farmer is neutral: forwards are settled at the prevailing market price at delivery"
    - "The farmer loses: by locking in $4.80, the farmer gave up the possibility of prices recovering above $4.80"
  answer: 0
  explanation: "The forward contract obligates the buyer to purchase at $4.80 regardless of the market price at delivery. Since the market fell to $3.50, the farmer receives $1.30/bushel more than the market would have paid — the hedge succeeded. Option D is factually true (the farmer did forgo upside above $4.80) but that's not what the contract 'did for' the farmer in this scenario. Forwards settle at the contracted price, not the prevailing market price (option C)."

- question: "A futures contract and a forward contract on the same asset and delivery date have the same economic exposure. The key mechanical difference is:"
  type: multiple-choice
  options:
    - "Futures contracts require physical delivery; forward contracts can be cash-settled"
    - "Forward contracts are priced higher than futures because they carry more counterparty risk"
    - "Futures contracts mark to market daily, transferring gains and losses between accounts each day; forwards settle only at maturity"
    - "Futures contracts cannot be used for hedging, only for speculation"
  answer: 2
  explanation: "The key mechanical difference is daily mark-to-market settlement. Futures exchanges transfer gains and losses between accounts each day as prices move. The economic exposure is the same as a forward, but the timing of cash transfers differs fundamentally — you may pay or receive margin daily, while a forward has no cash flow until delivery. This daily settlement also eliminates counterparty credit risk (the exchange backstops each trade), unlike forwards which are bilateral."

- question: "Speculators in futures markets are harmful because they cause price volatility without contributing anything productive."
  type: true-false
  answer: false
  explanation: "Speculators are necessary for futures markets to function: hedgers need counterparties willing to absorb price risk, and speculators fill that role. Without speculators, hedgers would have difficulty finding parties to take the other side of their trades, and bid-ask spreads would widen significantly. Speculators also contribute to price discovery by incorporating their expectations about future prices. All three roles — hedgers, speculators, arbitrageurs — are mutually necessary."

- question: "If the futures price of oil significantly exceeds the spot price plus storage and financing costs, an arbitrageur can earn a risk-free profit by buying oil spot and selling futures."
  type: true-false
  answer: true
  explanation: "This is the cost-of-carry arbitrage. If F > S(1+r)^T + storage costs, you buy the asset at spot price S, finance it at rate r, store it, and simultaneously sell a futures contract at F. At delivery, you deliver the asset and receive F, having paid S(1+r)^T in total costs — the difference is a risk-free profit. Competitive arbitrage drives futures prices back to fair value."

- question: "Why must the futures price of an asset approximately equal the spot price plus financing and storage costs, and what happens when it doesn't?"
  type: short-answer
  answer: "The cost-of-carry model: if you can buy an asset today, store it, and deliver it at the futures price, your total cost is the spot price plus financing (and storage) over the delivery period. The futures price must equal this cost; otherwise a risk-free arbitrage profit is available. If the futures price exceeds this cost, arbitrageurs buy spot and sell futures, earning a guaranteed profit — this trading pressure drives the futures price down and the spot price up, restoring the relationship."
  explanation: "The cost-of-carry relationship F ≈ S(1+r)^T is enforced by arbitrage, not assumption. Whenever it fails, rational traders lock in risk-free profits, and their trading corrects the mispricing. This is why futures prices in competitive markets closely track their theoretical fair values. Understanding this relationship is the foundation for pricing all forward-dated contracts — from commodities to currencies to interest rates."
```

## Explainer

Start with the simplest version of the problem. Imagine you are a wheat farmer who will harvest 10,000 bushels in six months. The current price is $5 per bushel, but you don't know what the price will be at harvest. If prices fall to $3, your revenue collapses. You want certainty. A grain elevator operator faces the opposite risk: they need to buy wheat at harvest but worry prices will rise. Both parties have a problem that the other can solve. A **forward contract** is the bilateral agreement that resolves this: you agree today to sell 10,000 bushels in six months at $4.80 — a price you both can live with. No money changes hands now; the obligation is settled at delivery. You have locked in revenue; they have locked in cost.

A **futures contract** achieves the same economic goal but is engineered for liquidity and scale. Futures are standardized by exchanges: the contract specifies exact quantity, quality, delivery location, and settlement date. Because contracts are identical, they are tradeable — a farmer can exit their position before harvest by selling the contract to someone else, without negotiating with the original counterparty. The exchange also interposes itself as buyer to every seller and seller to every buyer, eliminating counterparty credit risk. To enforce this guarantee, both parties post **initial margin** (a good-faith deposit) and daily **mark-to-market** settlement transfers gains and losses between accounts as prices move. This daily cash flow is the key mechanical difference from forwards, which settle only at maturity.

Your prerequisite — present value and discounting — underlies the pricing of both instruments. The **cost-of-carry model** says the fair forward price F is approximately F = S × (1 + r)^T, where S is today's spot price and r is the risk-free rate over the period T. The intuition: if you could buy the asset today and store it until the delivery date, your total cost would be the spot price plus financing costs (and storage, insurance, etc.). The forward price must equal that cost-to-carry; otherwise arbitrage profits would be available. If F > S(1+r)^T, you buy the asset spot, sell a forward, and pocket the difference. Competitive arbitrage drives the price back to fair value.

The three uses of futures follow naturally from this framework. **Hedgers** like our farmer take positions that offset existing price exposure. **Speculators** take positions without offsetting exposure — they are betting on directional price moves and provide the liquidity that hedgers need. **Arbitrageurs** enforce the cost-of-carry relationship by exploiting mispricings. All three are necessary: hedgers transfer risk they don't want, speculators absorb it for expected profit, and arbitrageurs keep prices aligned across time. Understanding which role a participant is playing — and what their position looks like at expiration — is the core analytical skill in derivatives markets.
