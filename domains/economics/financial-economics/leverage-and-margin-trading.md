---
id: leverage-and-margin-trading
title: Leverage and Margin Trading
domain: economics
course: financial-economics
prerequisites:
- id: risk-and-return-tradeoff
  type: hard
- id: futures-and-forward-contracts
  type: soft
builds-toward:
- value-at-risk-measurement
tags:
- leverage
- margin
- risk
stage: formal-systems
status: draft
---

# Leverage and Margin Trading

## Core Idea
Leverage amplifies returns and losses by using borrowed capital to increase exposure beyond available funds. Margin requirements limit borrowing; marked-to-market margin calls force liquidation if losses exceed buffers. Leverage magnifies both gains in bull markets and losses in downturns, creating systemic fragility during stress periods.

## Explainer

From your risk-and-return tradeoff work, you know that higher expected returns require bearing more risk. Leverage is the mechanism by which an investor deliberately amplifies both — borrowing money to take a position larger than their own capital would allow. Understanding leverage precisely means tracking what happens to your equity (the money you actually own) as the asset value moves.

Consider a simple example. You have $10,000 and buy $20,000 of stock by borrowing $10,000. Your **leverage ratio** is 2:1 — $2 of exposure for every $1 of equity. If the stock rises 10%, you now hold $22,000 in stock and still owe $10,000, leaving equity of $12,000 — a 20% gain on your original $10,000. Your return is double the unleveraged return. If the stock falls 10%, the stock is worth $18,000, you still owe $10,000, and your equity is $8,000 — a 20% loss. The leverage ratio multiplies both gains and losses by the same factor. More precisely, the return on equity equals the asset return multiplied by the leverage ratio, minus the borrowing cost (interest on the loan). Leverage only adds expected value if the asset's expected return exceeds the borrowing rate, which is why it is not free money.

**Margin requirements** are the institutional mechanism that limits leverage in practice. A broker requiring 50% initial margin means you must provide at least half the position's value in equity — so a $20,000 position requires $10,000 of your own capital, capping your leverage at 2:1. A **maintenance margin** (typically 25–30%) defines the floor: if your equity falls below this fraction of the position's value, you receive a **margin call** — a demand to deposit additional funds or have positions liquidated immediately. This is where leverage creates systemic fragility. When prices fall, leveraged investors receive margin calls simultaneously, forcing them to sell into the falling market, depressing prices further, triggering more margin calls — a cascade. The 2008 financial crisis amplified the damage of mortgage losses precisely because financial institutions held those assets with extreme leverage, so small declines in housing prices wiped out their equity entirely.

**Marked to market** means your equity is recalculated continuously as asset prices change — there is no grace period to wait out a temporary drawdown. A leveraged investor who is fundamentally correct about long-term value can still be forced out of a position by short-term volatility if they lack the capital buffer to survive the margin call. This is the classic distinction between being wrong about value and being wrong about timing, and it explains why even sophisticated investors with accurate long-run views sometimes go bankrupt: they are right eventually, but leverage forced liquidation before "eventually" arrived.
