---
id: market-microstructure-fundamentals
title: Market Microstructure Fundamentals
domain: economics
course: financial-economics
prerequisites:
- id: supply-and-demand-basics
  type: hard
- id: efficient-market-hypothesis
  type: soft
builds-toward:
- bid-ask-spreads-and-liquidity
tags:
- market-structure
- trading
- mechanics
stage: formal-systems
status: draft
---

# Market Microstructure Fundamentals

## Core Idea
Market microstructure examines the detailed mechanics of how financial markets function: order types, dealer behavior, information processing, and price formation. Spread levels reflect order processing, inventory, and adverse selection costs. Understanding microstructure is essential for low-latency trading, optimal execution, and liquidity analysis.

## Explainer

Supply and demand — your core prerequisite — describes markets at equilibrium: a price clears the market when quantity supplied equals quantity demanded. But that framework treats price as an outcome of a static matching process. Market microstructure asks the more granular question: moment to moment, how does a price actually get discovered? Who stands on the other side of a trade, and what does it cost to transact immediately? The answers matter enormously for anyone actually operating in financial markets, not just theorizing about them.

The foundation is the distinction between **order types**. A **market order** is an instruction to buy or sell immediately at whatever price is currently available — it prioritizes speed over price certainty. A **limit order** is an instruction to buy or sell only at a specified price or better — it prioritizes price certainty over execution certainty. A **limit order book** is the collection of all outstanding limit orders at various price levels, organized by price and then by time priority within each price level. The **bid price** is the highest price a buyer has stated willingness to pay; the **ask price** (or offer) is the lowest price a seller has stated willingness to accept. The gap between them is the **bid-ask spread**.

**Market makers** (or dealers) provide liquidity by continuously posting both bid and ask prices, standing ready to buy from sellers and sell to buyers. Their profit comes from the spread — buying at the bid and selling at the ask — but they bear three distinct costs. **Order processing costs** are operational: clearing, settlement, compliance. **Inventory costs** arise because a market maker who absorbs a large imbalanced order accumulates a position in one direction, exposing themselves to adverse price moves while they wait for the offsetting order flow. **Adverse selection costs** are the most theoretically important: some traders have private information about true value. If the market maker systematically trades against informed investors (buying when an informed seller knows the stock is overvalued; selling when an informed buyer knows it's undervalued), they lose money on average. The spread must be wide enough to recoup these losses from uninformed traders. This is why spreads are wider for smaller, less-traded stocks — the probability of trading against an informed counterparty is higher when fewer participants are monitoring the security.

The connection to the efficient market hypothesis is direct: markets become informationally efficient through the trading process itself. When an informed trader places a market order, the resulting trade and its price impact signals information to the market maker, who then adjusts their quotes. Over many trades, information gets progressively incorporated into prices — not instantaneously and costlessly as EMH's simplest form implies, but through a mechanism with friction, cost, and strategic behavior. Understanding this process explains phenomena like **price impact** (large orders move prices against the trader), **execution cost** (the true cost of trading exceeds just the commission), and why institutional investors care deeply about execution quality. A fund managing billions cannot simply buy everything at the posted price without moving prices significantly against itself.
