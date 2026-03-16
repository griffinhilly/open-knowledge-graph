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

## Explainer

Start with the simplest version of the problem. Imagine you are a wheat farmer who will harvest 10,000 bushels in six months. The current price is $5 per bushel, but you don't know what the price will be at harvest. If prices fall to $3, your revenue collapses. You want certainty. A grain elevator operator faces the opposite risk: they need to buy wheat at harvest but worry prices will rise. Both parties have a problem that the other can solve. A **forward contract** is the bilateral agreement that resolves this: you agree today to sell 10,000 bushels in six months at $4.80 — a price you both can live with. No money changes hands now; the obligation is settled at delivery. You have locked in revenue; they have locked in cost.

A **futures contract** achieves the same economic goal but is engineered for liquidity and scale. Futures are standardized by exchanges: the contract specifies exact quantity, quality, delivery location, and settlement date. Because contracts are identical, they are tradeable — a farmer can exit their position before harvest by selling the contract to someone else, without negotiating with the original counterparty. The exchange also interposes itself as buyer to every seller and seller to every buyer, eliminating counterparty credit risk. To enforce this guarantee, both parties post **initial margin** (a good-faith deposit) and daily **mark-to-market** settlement transfers gains and losses between accounts as prices move. This daily cash flow is the key mechanical difference from forwards, which settle only at maturity.

Your prerequisite — present value and discounting — underlies the pricing of both instruments. The **cost-of-carry model** says the fair forward price F is approximately F = S × (1 + r)^T, where S is today's spot price and r is the risk-free rate over the period T. The intuition: if you could buy the asset today and store it until the delivery date, your total cost would be the spot price plus financing costs (and storage, insurance, etc.). The forward price must equal that cost-to-carry; otherwise arbitrage profits would be available. If F > S(1+r)^T, you buy the asset spot, sell a forward, and pocket the difference. Competitive arbitrage drives the price back to fair value.

The three uses of futures follow naturally from this framework. **Hedgers** like our farmer take positions that offset existing price exposure. **Speculators** take positions without offsetting exposure — they are betting on directional price moves and provide the liquidity that hedgers need. **Arbitrageurs** enforce the cost-of-carry relationship by exploiting mispricings. All three are necessary: hedgers transfer risk they don't want, speculators absorb it for expected profit, and arbitrageurs keep prices aligned across time. Understanding which role a participant is playing — and what their position looks like at expiration — is the core analytical skill in derivatives markets.
