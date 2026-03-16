---
id: collateral-haircut-valuation
title: Collateral Valuation and Haircuts in Repo Markets
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: leverage-and-margin-trading
  type: soft
builds-toward:
- financial-crisis-contagion
tags:
- repo
- collateral
- leverage
- valuation
stage: formal-systems
status: draft
---

# Collateral Valuation and Haircuts in Repo Markets

## Core Idea
In repo transactions, haircuts discount collateral value to protect the lender against price declines and liquidation costs. Haircuts vary by collateral type and market stress: safe government securities have low haircuts while illiquid assets have high haircuts. During crises, haircuts spike suddenly, forcing rapid deleveraging and asset fire sales, as seen in 2008 when repo haircuts increased sharply.

## Explainer

In a **repurchase agreement** (repo), one party sells a security to another with a promise to buy it back at a higher price on a specified date. Economically, this is a collateralized loan: the seller receives cash now, the buyer holds the security as collateral, and the price difference is the interest. If the seller defaults before the repurchase date, the buyer sells the collateral to recover the loan. From your bond pricing background, you know that bond prices fluctuate with yields, credit spreads, and market liquidity. The buyer therefore faces risk: collateral value might fall below the outstanding loan between default and liquidation, leaving the lender with a loss.

The **haircut** addresses this directly. If a bond is worth $100, the lender might advance only $95 — a 5% haircut — keeping a $5 cushion. The borrower receives only 95% of collateral value as cash, but posts 100% as security. The haircut compensates for two risks: (1) **price risk** — the collateral may decline in value before liquidation can be completed, and (2) **liquidation risk** — the collateral may be hard to sell quickly in stressed conditions without accepting a large discount. US Treasury bills have haircuts near zero because their prices are stable and markets are extremely deep. High-yield corporate bonds or structured credit products carry haircuts of 10–30% or more because their prices can gap down rapidly and thin markets may not absorb large sales without significant price concessions.

The danger lies in the **procyclicality** of haircuts. In calm markets, haircuts are low, enabling high leverage. Using your leverage knowledge: if a haircut is 5%, a borrower can post $100 of collateral and borrow $95, achieving roughly 20:1 leverage — small price moves on the underlying position are amplified enormously into equity. When a crisis hits and asset prices begin falling, lenders suddenly demand much higher haircuts on the same collateral — they perceive sharply higher price and liquidity risk. The borrower must now return cash or post additional collateral to meet the new margin requirement. If they cannot, they are forced to sell assets. When all leveraged institutions simultaneously face higher haircuts — because they all hold similar collateral — they all become forced sellers at once. This drives prices down further, which justifies still-higher haircuts, which forces more selling: the **haircut spiral**.

The 2008 financial crisis illustrated this mechanism in stark relief. Mortgage-backed securities and other structured products were widely used as repo collateral. As housing prices declined and underlying credit quality became uncertain, repo haircuts on these assets rose sharply — in some cases from 2–3% to 20–40% nearly overnight. Borrowers who had been leveraged 20:1 or 30:1 were forced to liquidate massive positions quickly. The cascade of fire sales depressed prices across asset classes as institutions sold their most liquid holdings (Treasuries, equities) to raise cash, transmitting stress far beyond the initial epicenter. This is why collateral haircut dynamics are central to understanding financial crisis contagion: they are the transmission mechanism through which localized credit concerns become system-wide liquidity crises.
