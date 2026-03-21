---
id: market-maker-economics
title: Market Maker Economics and Bid-Ask Spreads
domain: economics
course: financial-economics
prerequisites:
- id: bid-ask-spreads-and-liquidity
  type: hard
- id: market-microstructure-fundamentals
  type: soft
builds-toward:
- market-microstructure-fundamentals
tags:
- market-microstructure
- liquidity
- trading
- spreads
stage: advanced
status: draft
---

# Market Maker Economics and Bid-Ask Spreads

## Core Idea
Market makers profit from the bid-ask spread but face inventory and adverse selection risks. The spread compensates for three costs: adverse selection (informed traders trade before prices adjust), inventory holding costs, and order processing costs. Understanding these components explains why spreads widen for illiquid assets, volatile markets, and during high-information environments.

## Questions

```yaml
- question: "Stock A has 80% uninformed liquidity traders and 20% informed traders. Stock B has 40% uninformed traders and 60% informed traders. All else equal, which stock has a wider bid-ask spread?"
  type: multiple-choice
  options:
    - "Stock A, because more uninformed traders means more volume and higher order processing costs"
    - "Stock B, because a higher fraction of informed traders raises the adverse selection cost the market maker must recover from uninformed trades"
    - "Both stocks have identical spreads because market makers set prices based on fundamentals, not trader composition"
    - "Stock A, because uninformed traders are harder to serve than informed traders"
  answer: 1
  explanation: "The adverse selection component of the spread is directly proportional to the fraction of informed traders and the magnitude of their information advantage. With 60% informed traders in Stock B, the market maker loses money more often on trades (informed traders only transact when they have an edge) and must widen the spread to recover those losses from the 40% uninformed trades. The Glosten-Milgrom model formalizes this: spreads are inversely related to the proportion of uninformed (liquidity) trading."

- question: "Bid-ask spreads widen sharply around scheduled earnings announcements. Which component of the three-part spread model primarily explains this pattern?"
  type: multiple-choice
  options:
    - "Order processing costs, because announcements increase trading volume and strain market-making infrastructure"
    - "Inventory holding costs, because market makers accumulate large positions during announcement periods"
    - "Adverse selection costs, because earnings announcements increase the fraction of informed traders relative to uninformed ones"
    - "All three components increase equally during announcement periods"
  answer: 2
  explanation: "Earnings announcements are scheduled information events: traders with superior research or information know (or strongly suspect) whether results will beat or miss consensus before the market maker does. The fraction of informed traders rises sharply, increasing the adverse selection risk the market maker faces on every trade. Order processing and inventory costs may shift, but the dominant explanation is adverse selection — the same reason spreads widen around central bank decisions, merger announcements, and other high-information events."

- question: "The bid-ask spread represents pure profit for the market maker — it is compensation for a useful service with no genuine risk."
  type: true-false
  answer: false
  explanation: "Market makers face real risks the spread must compensate. Adverse selection risk: informed traders systematically exploit the market maker's ignorance of true value, so the market maker loses money on every trade with an informed counterparty and must earn it back from uninformed traders. Inventory risk: when order flow is imbalanced, the market maker accumulates unwanted positions exposed to price movements. A market maker setting too narrow a spread is picked off by informed traders and loses money; too wide a spread drives away uninformed order flow. The spread is compensation for bearing genuine economic risks."

- question: "Informed traders widen bid-ask spreads by raising the adverse selection costs that market makers must recover through the spread."
  type: true-false
  answer: true
  explanation: "This is a core result of market microstructure theory. Informed traders transact specifically because they know the true asset value exceeds the ask (to buy) or is below the bid (to sell) — the market maker is always on the wrong side of informed trades. Since market makers cannot distinguish informed from uninformed traders, they must widen the spread so that profits from uninformed trades cover losses from informed trades. A higher fraction of informed traders mechanically requires a wider spread for the market maker to break even."

- question: "Why must a market maker earn money from uninformed (liquidity) traders in order to survive, even if it consistently loses money on trades with informed traders?"
  type: short-answer
  answer: "Market makers cannot distinguish informed traders from uninformed ones at the time of a trade. Informed traders buy when the true value exceeds the ask and sell when the true value is below the bid — the market maker is systematically on the losing side of every informed trade. If only informed traders existed, the market maker would lose money on every transaction. The only counterweight is uninformed liquidity traders (those buying or selling for portfolio rebalancing, cash needs, etc.) who have no information edge. The spread is set wide enough that profits from these uninformed trades exceed losses from informed trades."
  explanation: "The Glosten-Milgrom model formalizes this: the equilibrium spread equals twice the expected loss per unit traded with an informed counterparty. Market makers survive by cross-subsidization — uninformed traders effectively subsidize informed traders through the spread, and market makers extract enough from uninformed flow to cover the adverse selection losses. This is why spreads widen when uninformed trading volume falls: each remaining uninformed trade must subsidize more adverse selection losses."
```

## Explainer

From your study of bid-ask spreads and liquidity, you know that the bid-ask spread is the difference between the price at which a market maker will buy (the bid) and the price at which they will sell (the ask). A market maker is always on the other side of every trade: when you want to buy, the market maker sells to you at the ask; when you want to sell, the market maker buys from you at the bid. The spread is their compensation. But compensation for what, exactly? The three-component model of the spread gives a precise answer.

The **order processing cost component** is the simplest. Running a market-making operation requires technology, staff, and infrastructure. The spread must cover these fixed and variable costs spread across the volume of trades. For heavily traded assets like S&P 500 stocks, volume is so high that even a tiny spread generates enormous revenue; for thinly traded small-cap stocks or illiquid bonds, the same operating costs must be recovered from fewer trades, so spreads must be wider. This component alone explains why spread widths are inversely related to trading volume.

The **inventory holding cost component** reflects the risk that a market maker accumulates over time. When buyers arrive faster than sellers, the market maker's inventory grows — they end up holding more of the asset than they want. This inventory exposes them to price risk: if the asset falls in value while they are holding it, they take a loss. To manage this, market makers adjust their quotes: if they have too much inventory, they lower both bid and ask slightly to attract sellers and discourage buyers, gradually working back to neutral. The spread must be wide enough to compensate for this expected cost. Inventory risk is higher for more volatile assets (prices can move a lot against the market maker before they rebalance) and for assets with less frequent trading (slower inventory turnover means longer holding periods).

The **adverse selection cost component** is the most subtle and arguably the most important. Not all traders are equal. Some traders are **informed** — they know something about the true value of the asset that is not yet reflected in the price, and they trade precisely because of this advantage. The market maker cannot tell informed traders from uninformed ones (liquidity traders who need to buy or sell for portfolio rebalancing or cash needs). When an informed trader buys from the market maker, it is likely because the true value is above the ask price — and the market maker sold at a disadvantageous price. The market maker loses on trades with informed investors and only profits from trades with uninformed ones. The spread must be wide enough that profits from uninformed trading offset losses from informed trading. The Glosten-Milgrom model formalizes this: the bid-ask spread is directly proportional to the probability that the counterparty is informed and the expected magnitude of their information advantage.

These three components together explain several empirical patterns. Spreads widen around earnings announcements, central bank decisions, and other scheduled information events — because the fraction of informed traders rises sharply. Spreads widen during market stress and high volatility — inventory risk increases. Spreads narrow dramatically for large-cap stocks over the past two decades as electronic trading reduced order processing costs to near zero and competition among market makers intensified. **High-frequency trading (HFT)** firms now dominate market making in equity markets; they earn the spread while managing inventory risk through rapid position adjustments and earning the adverse selection component through superior speed rather than information.


