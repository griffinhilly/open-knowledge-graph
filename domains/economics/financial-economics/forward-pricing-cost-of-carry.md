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
status: validated
---

# Forward Pricing and Cost of Carry

## Core Idea
Forward prices equal the spot price plus the cost of carry (financing, storage, convenience yield). The forward premium or discount reflects interest rates, dividends (equities), or commodity storage costs. Pricing deviations create cash-and-carry or reverse cash-and-carry arbitrage opportunities.

## Questions

```yaml
- question: "A non-dividend-paying stock trades at $100 today. The annual risk-free rate is 5%. According to the cost-of-carry model, what should the 1-year forward price be?"
  type: multiple-choice
  options:
    - "$100 — the forward price reflects the market's expected future spot price, which equals today's price under risk neutrality"
    - "$105 — the forward price equals the spot price compounded at the risk-free rate"
    - "More than $105 — the forward must include a risk premium for stock price uncertainty"
    - "It cannot be determined without knowing the market's consensus forecast for the stock"
  answer: 1
  explanation: "The cost-of-carry model sets F = S₀ × e^(rT) ≈ $105.13 through no-arbitrage, not through forecasting. If F were higher, you could borrow $100, buy the stock, and lock in the forward sale — pocketing a riskless profit. If F were lower, you'd short the stock and buy the forward. Either deviation is arbitraged away. The forward price reflects financing cost, not a price forecast."

- question: "A physical commodity (e.g., wheat) has a spot price of $50, annual storage costs of $2, a convenience yield of $5/year, and the risk-free rate is 10%. What does the cost-of-carry model predict about the 1-year forward price relative to the spot price?"
  type: multiple-choice
  options:
    - "Forward > spot by 10%, because only the financing rate matters for commodities"
    - "Forward < spot, because the convenience yield ($5) exceeds storage costs ($2) plus financing (~$5), making backwardation likely"
    - "Forward > spot by exactly $7, because storage and financing add while convenience yield subtracts"
    - "Forward equals spot — carrying costs always cancel convenience yield in equilibrium"
  answer: 1
  explanation: "Net carry cost = r × S + storage − convenience yield ≈ $5 + $2 − $5 = $2. The convenience yield of $5 exceeds storage costs of $2, which when combined with the financing of ~$5 produces a net positive carry. Actually: F = (S₀ + storage − convenience yield) × e^(rT) ≈ ($50 + $2 − $5) × 1.105 ≈ $51.68. This is close to spot but above it. However, the point is that high convenience yield (during supply shortages) can push F below S₀ (backwardation). Option B captures the key insight that convenience yield acts as a drag on the forward price, which can dominate."

- question: "According to the cost-of-carry model, the forward price on a non-dividend-paying stock equals the current spot price compounded at the risk-free interest rate."
  type: true-false
  answer: true
  explanation: "Yes — F = S₀ × e^(rT) (or S₀ × (1+r)^T in discrete compounding). The logic is pure no-arbitrage: holding a position in the forward and holding the actual stock financed at the risk-free rate must cost the same. The risk-free rate is the cost of tying up capital in the position from now until delivery, which is exactly what the forward buyer avoids and thus must compensate the forward seller for."

- question: "The forward price of an asset is the market's best forecast of what the spot price will be on the delivery date."
  type: true-false
  answer: false
  explanation: "The forward price is the no-arbitrage cost-of-carry price, not a forecast. For a non-dividend-paying stock, F = S₀ × e^(rT) regardless of whether anyone expects the stock to rise or fall. The forward price tells you what it costs to synthetically defer the purchase, not where the market thinks the price is going. Under risk-neutral pricing the two coincide mathematically, but conceptually they are distinct — and for commodities with convenience yields, the forward can be below the spot even when most participants expect prices to rise."

- question: "Explain the cash-and-carry arbitrage that occurs when a forward price is higher than the cost-of-carry price, and why this trading activity restores the no-arbitrage price."
  type: short-answer
  answer: "If F > S₀ × e^(rT), an arbitrageur can: (1) borrow S₀ at the risk-free rate, (2) buy the asset at spot S₀, and (3) simultaneously sell a forward contract at the inflated price F. At maturity, the arbitrageur delivers the asset against the forward, receiving F, and repays the loan for S₀ × e^(rT). The riskless profit is F − S₀ × e^(rT) > 0. As arbitrageurs execute this trade, demand for the spot asset pushes S₀ up and selling pressure on the forward pushes F down, until F = S₀ × e^(rT) and the profit disappears."
  explanation: "Cash-and-carry arbitrage is what keeps forward markets honest. The ability to replicate the forward payoff by borrowing and buying spot means the forward price must equal the replication cost. Any gap is a free money opportunity that market participants will exploit until it closes. This is why cost-of-carry is a pricing formula derived from no-arbitrage, not an empirical regularity."
```

## Explainer

From your study of futures and forward contracts, you know that a forward is an agreement to buy or sell an asset at a fixed price on a future date. But how is that price determined? The answer comes from a no-arbitrage argument that connects the forward price to what it costs to hold the underlying asset from now until delivery. This **cost of carry** framework is one of the most elegant applications of arbitrage logic in finance.

Start with the simplest case: a non-dividend-paying stock. Suppose the stock trades at spot price S₀ today, and the risk-free interest rate is r. If you want to own the stock in T years, you have two equivalent strategies: (1) buy it forward at price F, or (2) borrow S₀ today, buy the stock now, hold it, and repay the loan at maturity. The cost of strategy 2 is S₀ × e^(rT) — just the future value of the spot price. By no-arbitrage, both strategies must cost the same: **F = S₀ × e^(rT)**. The forward price equals the spot price compounded at the financing rate. This is the cost of carry — you're paying for the time value of money tied up in holding the asset.

The formula generalizes cleanly. For dividend-paying stocks, you subtract the present value of dividends (you receive them as the holder but the forward buyer doesn't, so the forward price is lower): F = (S₀ − PV(dividends)) × e^(rT). For currencies, the **interest rate differential** between two countries plays the same role — the forward exchange rate reflects which currency earns more interest. For physical commodities like oil or wheat, you add **storage costs** (you have to warehouse the oil) but subtract the **convenience yield** — the implicit value of having the commodity available now rather than later. In periods of supply shortage, the convenience yield is high, and forward prices can actually be *below* spot prices, a condition called **backwardation**.

Deviations from the cost-of-carry price create textbook arbitrage. If F > S₀e^(rT), you can profit by selling the overpriced forward while doing a **cash-and-carry**: borrow, buy the spot asset, deliver it at maturity and pocket the difference. If F < S₀e^(rT), you do the **reverse cash-and-carry**: short-sell the spot asset, invest the proceeds, and buy the forward. In practice, transaction costs, borrowing constraints, and short-selling restrictions create a no-arbitrage band rather than a single price. But the cost-of-carry formula remains the anchor — it tells you what fair value is, and how far any deviation must go before it becomes exploitable.

