---
id: forward-pricing-cost-of-carry
title: Forward Pricing and Cost of Carry
domain: economics
course: financial-economics
prerequisites:
- id: futures-and-forward-contracts
  type: hard
- id: interest-rates-and-loanable-funds
  type: hard
builds-toward:
- hedging-with-derivatives
- interest-rate-swaps
tags:
- forwards
- pricing
- arbitrage
stage: formal-systems
status: draft
---

# Forward Pricing and Cost of Carry

## Core Idea
Forward prices equal the spot price plus the cost of carry (financing, storage, convenience yield). The forward premium or discount reflects interest rates, dividends (equities), or commodity storage costs. Pricing deviations create cash-and-carry or reverse cash-and-carry arbitrage opportunities.

## Explainer

From your study of futures and forward contracts, you know that a forward is an agreement to buy or sell an asset at a fixed price on a future date. But how is that price determined? The answer comes from a no-arbitrage argument that connects the forward price to what it costs to hold the underlying asset from now until delivery. This **cost of carry** framework is one of the most elegant applications of arbitrage logic in finance.

Start with the simplest case: a non-dividend-paying stock. Suppose the stock trades at spot price S₀ today, and the risk-free interest rate is r. If you want to own the stock in T years, you have two equivalent strategies: (1) buy it forward at price F, or (2) borrow S₀ today, buy the stock now, hold it, and repay the loan at maturity. The cost of strategy 2 is S₀ × e^(rT) — just the future value of the spot price. By no-arbitrage, both strategies must cost the same: **F = S₀ × e^(rT)**. The forward price equals the spot price compounded at the financing rate. This is the cost of carry — you're paying for the time value of money tied up in holding the asset.

The formula generalizes cleanly. For dividend-paying stocks, you subtract the present value of dividends (you receive them as the holder but the forward buyer doesn't, so the forward price is lower): F = (S₀ − PV(dividends)) × e^(rT). For currencies, the **interest rate differential** between two countries plays the same role — the forward exchange rate reflects which currency earns more interest. For physical commodities like oil or wheat, you add **storage costs** (you have to warehouse the oil) but subtract the **convenience yield** — the implicit value of having the commodity available now rather than later. In periods of supply shortage, the convenience yield is high, and forward prices can actually be *below* spot prices, a condition called **backwardation**.

Deviations from the cost-of-carry price create textbook arbitrage. If F > S₀e^(rT), you can profit by selling the overpriced forward while doing a **cash-and-carry**: borrow, buy the spot asset, deliver it at maturity and pocket the difference. If F < S₀e^(rT), you do the **reverse cash-and-carry**: short-sell the spot asset, invest the proceeds, and buy the forward. In practice, transaction costs, borrowing constraints, and short-selling restrictions create a no-arbitrage band rather than a single price. But the cost-of-carry formula remains the anchor — it tells you what fair value is, and how far any deviation must go before it becomes exploitable.

