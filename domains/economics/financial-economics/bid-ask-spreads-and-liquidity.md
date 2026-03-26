---
id: bid-ask-spreads-and-liquidity
title: Bid-Ask Spreads and Market Liquidity
domain: economics
course: financial-economics
prerequisites:
- id: market-microstructure-fundamentals
  type: hard
- id: information-asymmetry-markets
  type: soft
builds-toward:
- price-discovery-and-efficiency
tags:
- liquidity
- spreads
- trading-costs
stage: advanced
status: validated
---

# Bid-Ask Spreads and Market Liquidity

## Core Idea
The bid-ask spread is the transaction cost faced by traders, compensating dealers for order processing, inventory costs, and risk from adverse selection. Spreads widen when volatility or information asymmetry increases and narrow in liquid markets with many competitors. Liquidity varies significantly across assets and market conditions, affecting trading costs and execution strategy.

## Questions

```yaml
- question: "A market maker is quoting a $0.05 spread on a large-cap stock. News breaks that the company's CEO has just resigned unexpectedly. The market maker cannot yet tell whether incoming orders are from informed traders reacting to the news or uninformed traders. What should the market maker do immediately?"
  type: multiple-choice
  options:
    - "Narrow the spread to attract more order flow and recover losses through higher volume"
    - "Widen the spread or withdraw quotes entirely, because adverse selection risk has spiked"
    - "Maintain the current spread since the CEO resignation is already public information"
    - "Only trade with institutional investors until the informed/uninformed ratio normalizes"
  answer: 1
  explanation: "When major news breaks, adverse selection risk spikes immediately — the probability that an incoming order is from an informed trader jumps dramatically. Since the market maker cannot distinguish informed from uninformed traders, they must widen the spread to protect against informed order flow, or pull quotes until price discovery stabilizes. Narrowing the spread would be self-destructive: more volume at a narrow spread means more losses to traders who now know more than the market maker. This is why spreads widen sharply during news events."

- question: "During the March 2020 COVID market stress, spreads on many normally liquid instruments widened by 5–10× within days. The best explanation is:"
  type: multiple-choice
  options:
    - "Trading volume fell, so market makers needed to earn more per trade to cover fixed costs"
    - "Regulators required wider spreads to slow panic selling"
    - "Volatility, uncertainty about fundamentals, and reduced dealer capital all spiked simultaneously, driving up all three components of the spread"
    - "High-frequency traders withdrew, leaving only slower market makers who require wider spreads"
  answer: 2
  explanation: "Liquidity crises occur when all three spread components spike at once. Volatility increased inventory risk dramatically. Uncertainty about fundamental values increased adverse selection. Dealer capital contracted as firms faced margin calls and restricted risk. Each force alone widens spreads; all three together produced a liquidity spiral: wider spreads force leveraged investors to sell; forced selling moves prices; larger price moves increase volatility; increased volatility widens spreads further. The dynamic feeds on itself rather than declining gradually."

- question: "At the optimal bid-ask spread in a competitive market, a market maker earns zero profit from trades with informed traders and positive profit from trades with uninformed traders."
  type: true-false
  answer: false
  explanation: "At the optimal spread, the market maker earns *negative* profit from informed traders (they lose money on every trade with someone who has superior information) and *positive* profit from uninformed traders. The equilibrium spread is set so that profits from uninformed trades exactly cover losses from informed trades, yielding approximately zero economic profit overall in a competitive market. The spread is not set to earn zero from informed traders — that would require being able to identify and screen them, which the market maker by assumption cannot do."

- question: "In a perfectly competitive market with many market makers, bid-ask spreads will converge to zero because competitive pressure eliminates most transaction costs."
  type: true-false
  answer: false
  explanation: "Competitive pressure reduces spreads but cannot eliminate them entirely, because all three cost components remain positive in any real market. Order processing requires real resources; inventory must be financed and carries market risk; and as long as some traders have private information, adverse selection exists. In extremely liquid markets (large-cap equities, on-the-run Treasuries), spreads are very narrow but never reach zero because the underlying economic costs are minimized, not eliminated. Spreads would only converge to zero in a world with no information asymmetry, no inventory risk, and zero operational costs."

- question: "Explain why adverse selection is considered the most economically interesting component of the bid-ask spread. What is the fundamental problem it creates for market makers?"
  type: short-answer
  answer: "Adverse selection arises because some traders possess private information the market maker does not — about upcoming earnings, pending mergers, or fundamental value. The market maker cannot identify which traders are informed before dealing, so every trade carries some probability that the counterparty knows more. Informed traders buy just before a price increase or sell just before a decrease, leaving the market maker holding a position that immediately moves against them. To survive, the market maker sets spreads wide enough that profits from the uninformed majority cover these losses. The fundamental problem is asymmetric information combined with the inability to screen counterparties."
  explanation: "Order processing costs are predictable and manageable; inventory risk can be partially hedged. But adverse selection is intrinsic to the information structure of markets — it exists whenever some traders have access to information others lack, and it cannot be engineered away without destroying market anonymity. This is why information asymmetry (a prerequisite topic) is so central to market microstructure: it directly determines one of the three spread components that all participants pay. Disclosure requirements and price transparency genuinely reduce the adverse selection component and thereby improve liquidity."
```

## Explainer

From market microstructure, you know that trading is not instantaneous — buyers and sellers don't arrive at the same moment, so market makers stand ready to buy and sell continuously, providing **immediacy**. From information asymmetry, you know that some traders have private information that others lack. The bid-ask spread sits at the intersection of these two ideas: it is the price market makers charge for the service of immediacy, calibrated to protect them from being picked off by traders who know more than they do.

The spread has three distinct economic components, each corresponding to a cost borne by the market maker. **Order processing costs** are the operational overhead of running a trading desk — technology, staff, clearing fees. These are relatively fixed and small in liquid markets. **Inventory costs** arise because market makers cannot always immediately offset a trade in the opposite direction. When a market maker buys shares (at the bid), they hold inventory that may lose value before they can sell it. The spread must compensate for this holding risk. **Adverse selection costs** are the most economically interesting: some fraction of traders who want to deal with the market maker possess private information — about forthcoming earnings, a pending merger, or fundamental value — that the market maker does not have. Every time the market maker trades with an informed counterparty, they lose money. The spread must be wide enough that profits from uninformed traders cover these losses.

The adverse selection mechanism deserves a closer look. Imagine you are a market maker quoting a spread of $0.10 on a stock. A large trader arrives wanting to sell 50,000 shares. Should you worry? If the trader is a pension fund rebalancing its portfolio, the trade is uninformed — you'll make the spread and be fine. If the trader just received a tip that the company will miss earnings tomorrow, you're about to buy a large position at a price that will soon be much lower. You cannot distinguish these two traders before dealing. A narrower spread increases your volume from uninformed traders but also increases your losses from informed ones; a wider spread protects you from adverse selection but drives away uninformed order flow. The equilibrium spread balances these forces.

**Liquidity** is a composite concept describing how easily you can trade a large position without moving the price. It has three dimensions: the bid-ask spread (cost per share), **depth** (how many shares can be absorbed at the quoted price before the price moves), and **resilience** (how quickly the spread and depth recover after a large trade). Liquid assets — large-cap equities, on-the-run Treasury bonds, major currency pairs — have all three in abundance because they attract many competing market makers, generate high volume (making inventory turnover fast), and involve low information asymmetry (prices are publicly known and widely followed). Illiquid assets — micro-cap equities, distressed corporate bonds, real estate — have wide spreads because all three cost components are high.

Liquidity is not a fixed property of an asset — it fluctuates, and can evaporate suddenly. During market stress, volatility rises (increasing inventory risk), uncertainty about fundamentals increases (raising adverse selection), and market makers reduce their capital commitments (widening spreads and reducing depth). This creates **liquidity spirals**: wider spreads force leveraged investors to sell; forced selling moves prices; larger price moves increase volatility; increased volatility widens spreads further. The dynamic feeds on itself. The March 2020 COVID-related market stress and the 2008 financial crisis both exhibited this pattern — assets that had traded with minimal spreads for years became nearly untradeable within days. Understanding the components of the spread explains why: when the inputs to the spread (volatility, information asymmetry, dealer capital) all spike simultaneously, liquidity collapses rather than just declining gradually.
