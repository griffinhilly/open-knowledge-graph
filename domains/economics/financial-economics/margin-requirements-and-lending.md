---
id: margin-requirements-and-lending
title: Margin Accounts and Leverage Mechanics
domain: economics
course: financial-economics
prerequisites:
- id: leverage-and-margin-trading
  type: hard
builds-toward:
- short-selling-mechanics-costs
tags:
- leverage
- margin
- credit
- trading
stage: formal-systems
status: draft
---

# Margin Accounts and Leverage Mechanics

## Core Idea
Margin accounts allow investors to borrow money from brokers to finance security purchases, amplifying both gains and losses. Maintenance margin requirements ensure the account equity remains above a minimum percentage of securities value; falling below this threshold triggers a margin call requiring cash infusion or forced liquidation. Understanding leverage mechanics is critical for risk management.

## Explainer

From your study of leverage, you know the core mechanic: borrowing to invest magnifies returns in both directions. A margin account is the institutional implementation of that concept in securities markets. When you open a margin account, the broker extends you credit, using the securities you purchase as collateral. The **initial margin requirement** — set by Reg T in the US at 50% — means you must put up at least half the purchase price in cash. If you want to buy $10,000 of stock, you contribute $5,000 and the broker lends you $5,000. You now control $10,000 of assets but have only $5,000 of equity, giving you 2:1 leverage.

Once the position is open, the **maintenance margin** requirement (typically 25–30%) governs whether the position can remain open. Your margin equity equals the current value of securities minus the loan balance, which stays fixed. As the stock price falls, the security value falls but the loan does not, so equity as a percentage of security value shrinks. When equity falls below the maintenance threshold, the broker issues a **margin call**: deposit additional cash immediately or the broker will liquidate your position to bring the account back into compliance. The math is concrete: if you bought $10,000 of stock with $5,000 borrowed, and the maintenance requirement is 25%, you can withstand a price drop until equity = 25% × security value. Solving: (security value − $5,000) / security value = 0.25 gives security value = $6,667, meaning a 33% price drop triggers the call.

The dangerous amplification works symmetrically. On a 2:1 leveraged position, a 10% rise in the stock produces a 20% return on your equity, while a 10% fall produces a 20% loss on your equity. With higher leverage ratios — some products permit 4:1 or more — the amplification is more extreme. This is not merely a nuance for risk management; it has systemic implications. When prices fall broadly, leveraged investors simultaneously receive margin calls and must sell, which depresses prices further, triggering more margin calls — a **forced deleveraging spiral** that amplified the 2008 financial crisis and many historical panics before it. Margin requirements set by regulators are therefore a macro-prudential tool, not just a credit management decision for individual brokers.
