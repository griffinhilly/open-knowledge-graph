---
id: hedging-with-derivatives
title: Hedging with Derivatives
domain: economics
course: financial-economics
prerequisites:
- id: futures-and-forward-contracts
  type: hard
- id: portfolio-diversification
  type: soft
builds-toward:
- value-at-risk-measurement
tags:
- hedging
- risk-management
- derivatives
stage: formal-systems
status: draft
---

# Hedging with Derivatives

## Core Idea
Hedging uses derivatives to offset or reduce exposure to unwanted risks (interest rate, currency, commodity, or equity price risk). Perfect hedges reduce risk to zero; imperfect hedges reduce but do not eliminate risk. The cost of hedging (option premiums or forward discounts) must be weighed against the benefit of reduced uncertainty.

## Explainer

From your study of futures and forward contracts, you know that these instruments lock in a price today for a transaction that will happen in the future. A hedge turns that locking-in mechanism into a risk management tool: you hold an existing exposure to some price, and you take an offsetting position in a derivative so that gains on one side roughly cancel losses on the other. The economic purpose is not to profit from the derivative — it is to neutralize a risk you don't want to bear so you can focus on the risks you do want to bear.

Consider a simple example. An airline knows it will buy one million gallons of jet fuel in three months. If jet fuel prices rise, its costs spike and profits fall — this is the underlying exposure. To hedge, the airline buys fuel futures contracts locking in today's price. If fuel prices rise, the airline pays more in the spot market but gains on its futures position; if prices fall, it pays less in the spot market but loses on the futures. Either way, the net cost is approximately the futures price agreed to today. The airline has traded price uncertainty for price certainty. The cost of this hedge is the difference between the futures price and whatever the spot price turns out to be — sometimes that difference is a gain (if prices rose), sometimes a loss (if prices fell), but the airline accepted that tradeoff knowingly to protect its operating budget.

A **perfect hedge** — where the derivative's payoff exactly offsets the exposure in every scenario — is rare in practice. **Basis risk** is the most common source of imperfection: the derivative may be written on a slightly different asset, a different delivery location, or a different maturity than your actual exposure. A wheat farmer hedging with corn futures faces basis risk from the price spread between the two crops; a US company hedging Euro revenue with EUR/USD futures faces basis risk if it actually invoices in British pounds. The **hedge ratio** — how many derivative contracts to hold per unit of underlying exposure — requires careful calculation to minimize residual risk. For commodity futures, this is straightforward; for equity portfolios, you may use beta to determine how many index futures contracts offset your portfolio's systematic exposure.

The decision to hedge is ultimately about whether the cost of certainty is worth it. From your portfolio diversification prerequisite, you know that investors who hold diversified portfolios don't need companies to hedge every risk — they can diversify it away themselves. This is why pure financial risks (like stock price risk) are rarely worth hedging at the firm level. Hedging is most valuable when the risk threatens the firm's ability to operate — when cash flow volatility could force costly financial distress, cause firms to forgo profitable investments, or create customer and supplier uncertainty. The classic hedging candidates are commodity producers, exporters and importers facing currency risk, and financial institutions managing interest rate sensitivity. The key question is always: who can bear this risk most cheaply — the firm, its shareholders, or a counterparty in the derivatives market?
