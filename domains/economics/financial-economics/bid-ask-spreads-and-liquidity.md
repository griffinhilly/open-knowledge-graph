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
stage: formal-systems
status: draft
---

# Bid-Ask Spreads and Market Liquidity

## Core Idea
The bid-ask spread is the transaction cost faced by traders, compensating dealers for order processing, inventory costs, and risk from adverse selection. Spreads widen when volatility or information asymmetry increases and narrow in liquid markets with many competitors. Liquidity varies significantly across assets and market conditions, affecting trading costs and execution strategy.

## Explainer

From market microstructure, you know that trading is not instantaneous — buyers and sellers don't arrive at the same moment, so market makers stand ready to buy and sell continuously, providing **immediacy**. From information asymmetry, you know that some traders have private information that others lack. The bid-ask spread sits at the intersection of these two ideas: it is the price market makers charge for the service of immediacy, calibrated to protect them from being picked off by traders who know more than they do.

The spread has three distinct economic components, each corresponding to a cost borne by the market maker. **Order processing costs** are the operational overhead of running a trading desk — technology, staff, clearing fees. These are relatively fixed and small in liquid markets. **Inventory costs** arise because market makers cannot always immediately offset a trade in the opposite direction. When a market maker buys shares (at the bid), they hold inventory that may lose value before they can sell it. The spread must compensate for this holding risk. **Adverse selection costs** are the most economically interesting: some fraction of traders who want to deal with the market maker possess private information — about forthcoming earnings, a pending merger, or fundamental value — that the market maker does not have. Every time the market maker trades with an informed counterparty, they lose money. The spread must be wide enough that profits from uninformed traders cover these losses.

The adverse selection mechanism deserves a closer look. Imagine you are a market maker quoting a spread of $0.10 on a stock. A large trader arrives wanting to sell 50,000 shares. Should you worry? If the trader is a pension fund rebalancing its portfolio, the trade is uninformed — you'll make the spread and be fine. If the trader just received a tip that the company will miss earnings tomorrow, you're about to buy a large position at a price that will soon be much lower. You cannot distinguish these two traders before dealing. A narrower spread increases your volume from uninformed traders but also increases your losses from informed ones; a wider spread protects you from adverse selection but drives away uninformed order flow. The equilibrium spread balances these forces.

**Liquidity** is a composite concept describing how easily you can trade a large position without moving the price. It has three dimensions: the bid-ask spread (cost per share), **depth** (how many shares can be absorbed at the quoted price before the price moves), and **resilience** (how quickly the spread and depth recover after a large trade). Liquid assets — large-cap equities, on-the-run Treasury bonds, major currency pairs — have all three in abundance because they attract many competing market makers, generate high volume (making inventory turnover fast), and involve low information asymmetry (prices are publicly known and widely followed). Illiquid assets — micro-cap equities, distressed corporate bonds, real estate — have wide spreads because all three cost components are high.

Liquidity is not a fixed property of an asset — it fluctuates, and can evaporate suddenly. During market stress, volatility rises (increasing inventory risk), uncertainty about fundamentals increases (raising adverse selection), and market makers reduce their capital commitments (widening spreads and reducing depth). This creates **liquidity spirals**: wider spreads force leveraged investors to sell; forced selling moves prices; larger price moves increase volatility; increased volatility widens spreads further. The dynamic feeds on itself. The March 2020 COVID-related market stress and the 2008 financial crisis both exhibited this pattern — assets that had traded with minimal spreads for years became nearly untradeable within days. Understanding the components of the spread explains why: when the inputs to the spread (volatility, information asymmetry, dealer capital) all spike simultaneously, liquidity collapses rather than just declining gradually.
