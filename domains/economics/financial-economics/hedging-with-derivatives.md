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
- id: options-greeks-trading-applications
  type: soft
- id: interest-rate-swaps-mechanics
  type: soft
- id: forward-pricing-cost-of-carry
  type: soft
builds-toward:
- value-at-risk-measurement
tags:
- hedging
- risk-management
- derivatives
stage: formal-systems
status: validated
---
# Hedging with Derivatives

## Core Idea
Hedging uses derivatives to offset or reduce exposure to unwanted risks (interest rate, currency, commodity, or equity price risk). Perfect hedges reduce risk to zero; imperfect hedges reduce but do not eliminate risk. The cost of hedging (option premiums or forward discounts) must be weighed against the benefit of reduced uncertainty.

## Questions

```yaml
- question: "An airline buys fuel futures to hedge its jet fuel exposure. Fuel prices fall sharply, so the airline pays less in the spot market but loses money on its futures position. How should we evaluate this hedge?"
  type: multiple-choice
  options:
    - "The hedge failed — the airline would have been better off without it"
    - "The hedge succeeded — the airline achieved its goal of price certainty, which is what hedging is for"
    - "The hedge was imperfect because a perfect hedge would have broken even regardless of price movement"
    - "The hedge failed because basis risk caused the derivative loss to exceed the spot market gain"
  answer: 1
  explanation: "This is the most common misconception about hedging. The purpose of a hedge is not to profit from the derivative — it is to exchange price uncertainty for price certainty. When the airline bought fuel futures, it accepted a fixed cost in exchange for protection against price spikes. If fuel prices fell, the spot market savings and the futures losses roughly cancel, and the airline pays approximately the futures price it locked in. That is exactly what it set out to do. Judging the hedge a 'failure' because prices moved favorably is like calling home insurance a failure because your house didn't burn down."

- question: "A gold mining company hedges its entire expected production by selling gold futures. Which of the following statements best describes the economic rationale for hedging at the firm level rather than leaving it to shareholders?"
  type: multiple-choice
  options:
    - "Shareholders cannot hedge commodity exposure themselves, so firms must do it on their behalf"
    - "The hedge reduces systematic risk, lowering the firm's required rate of return"
    - "Gold price volatility threatens the firm's ability to fund operations and investment — cash flow stability has direct value when financial distress is costly"
    - "Regulators require mining companies to hedge commodity exposure to protect employees"
  answer: 2
  explanation: "From portfolio diversification theory, shareholders can diversify away commodity price risk themselves — so hedging purely financial risk at the firm level doesn't add value in a frictionless world. Firm-level hedging is most valuable when cash flow volatility creates real costs: financial distress, inability to fund profitable projects, or uncertainty for suppliers and customers. A gold miner that could go bankrupt if gold prices fall has strong reason to hedge because distress costs are real and hedging reduces the probability of incurring them. Shareholders cannot avoid these corporate-level distress costs through personal diversification."

- question: "A hedge that uses a derivative written on a closely related but not identical asset introduces basis risk, meaning the hedge may not fully offset the underlying exposure."
  type: true-false
  answer: true
  explanation: "Basis risk arises whenever the derivative and the underlying exposure are not perfectly correlated. A wheat farmer hedging with corn futures faces basis risk from the spread between wheat and corn prices; a US firm hedging European sales in USD/EUR futures faces basis risk if actual invoices are in British pounds. The hedge reduces exposure but some residual risk remains. A perfect hedge — zero basis risk — is rare in practice and would require a derivative written on exactly the same asset, location, quantity, and date as the actual exposure."

- question: "Hedging with derivatives is most valuable for companies facing risks that their shareholders can easily diversify away in their investment portfolios."
  type: true-false
  answer: false
  explanation: "This is backwards. In efficient markets, risks that shareholders can diversify away through portfolio construction don't create value when hedged at the firm level — shareholders can simply hold a diversified portfolio and neutralize those risks themselves. Firm-level hedging is most valuable for risks that threaten the company's ability to operate — risks that, if they materialize, cause financial distress, constrain investment, or create stakeholder uncertainty. Commodity producers, exporters, and financial institutions hedge because their core operating risks are too large or concentrated to leave to shareholder diversification."

- question: "Why does the economic purpose of a hedge mean that a derivative position that loses money can still represent a successful hedge?"
  type: short-answer
  answer: "A hedge's purpose is to reduce or eliminate price uncertainty, not to generate profit. When a firm holds an underlying exposure (e.g., it will need to buy fuel at the market price in three months), it uses a derivative to lock in a price today. If prices move favorably, the derivative position loses money but the spot purchase costs less — the net outcome is approximately the locked-in price either way. The firm traded the possibility of a favorable outcome for the certainty of a known outcome. Calling this a failure confuses the goal of hedging (certainty) with the goal of speculation (profit)."
  explanation: "This distinction between hedging and speculation is foundational to risk management. A speculator takes derivative positions hoping to profit from price movement; a hedger takes derivative positions to offset an existing exposure. For a hedger, the derivative is insurance — you pay a premium (or forego potential gains) to eliminate downside risk. A hedge that 'costs money' when prices moved favorably is functioning exactly as designed."
```

## Explainer

From your study of futures and forward contracts, you know that these instruments lock in a price today for a transaction that will happen in the future. A hedge turns that locking-in mechanism into a risk management tool: you hold an existing exposure to some price, and you take an offsetting position in a derivative so that gains on one side roughly cancel losses on the other. The economic purpose is not to profit from the derivative — it is to neutralize a risk you don't want to bear so you can focus on the risks you do want to bear.

Consider a simple example. An airline knows it will buy one million gallons of jet fuel in three months. If jet fuel prices rise, its costs spike and profits fall — this is the underlying exposure. To hedge, the airline buys fuel futures contracts locking in today's price. If fuel prices rise, the airline pays more in the spot market but gains on its futures position; if prices fall, it pays less in the spot market but loses on the futures. Either way, the net cost is approximately the futures price agreed to today. The airline has traded price uncertainty for price certainty. The cost of this hedge is the difference between the futures price and whatever the spot price turns out to be — sometimes that difference is a gain (if prices rose), sometimes a loss (if prices fell), but the airline accepted that tradeoff knowingly to protect its operating budget.

A **perfect hedge** — where the derivative's payoff exactly offsets the exposure in every scenario — is rare in practice. **Basis risk** is the most common source of imperfection: the derivative may be written on a slightly different asset, a different delivery location, or a different maturity than your actual exposure. A wheat farmer hedging with corn futures faces basis risk from the price spread between the two crops; a US company hedging Euro revenue with EUR/USD futures faces basis risk if it actually invoices in British pounds. The **hedge ratio** — how many derivative contracts to hold per unit of underlying exposure — requires careful calculation to minimize residual risk. For commodity futures, this is straightforward; for equity portfolios, you may use beta to determine how many index futures contracts offset your portfolio's systematic exposure.

The decision to hedge is ultimately about whether the cost of certainty is worth it. From your portfolio diversification prerequisite, you know that investors who hold diversified portfolios don't need companies to hedge every risk — they can diversify it away themselves. This is why pure financial risks (like stock price risk) are rarely worth hedging at the firm level. Hedging is most valuable when the risk threatens the firm's ability to operate — when cash flow volatility could force costly financial distress, cause firms to forgo profitable investments, or create customer and supplier uncertainty. The classic hedging candidates are commodity producers, exporters and importers facing currency risk, and financial institutions managing interest rate sensitivity. The key question is always: who can bear this risk most cheaply — the firm, its shareholders, or a counterparty in the derivatives market?
