---
id: bond-portfolio-strategies
title: 'Bond Portfolio Strategies: Ladders and Barbells'
domain: economics
course: financial-economics
prerequisites:
- id: term-structure-of-interest-rates
  type: hard
- id: bond-immunization-liability-matching
  type: soft
tags:
- fixed-income
- portfolio-management
- strategy
stage: formal-systems
status: draft
---

# Bond Portfolio Strategies: Ladders and Barbells

## Core Idea
Bond ladders hold bonds maturing at regular intervals, providing steady income and reinvestment opportunities; barbells concentrate holdings at short and long maturities, betting on yield curve movements. Each strategy offers different risk-return tradeoffs.

## Explainer

From the term structure of interest rates, you know that bonds at different maturities carry different yields, and those yields move in complex, correlated ways as the yield curve shifts and reshapes. From bond immunization, you know that duration is the key measure linking a portfolio's price sensitivity to interest rate changes. Bond portfolio strategy is about applying those insights to construct portfolios that express particular views about yield curve movements, match liability streams, or balance income stability against interest rate risk. The **ladder** and **barbell** are the two archetypal structures, and understanding them clarifies why maturity distribution — not just average duration — matters for fixed income investing.

A **bond ladder** holds bonds maturing at evenly spaced intervals — say, every year for ten years. As each bond matures, the proceeds are reinvested at the current yield for a new ten-year bond, maintaining the ladder structure. This creates a steady cash flow stream (the maturing bond each period) and a simple reinvestment discipline that sidesteps the need to predict yield curve movements. When rates are high, maturing proceeds reinvest at favorable rates; when rates are low, only a fraction of the portfolio turns over in any given period, so the damage is limited. The ladder is effectively **yield curve agnostic**: it captures the average of current and future short-term rates over the holding period, similar to the expectations hypothesis prediction. Investors with regular cash needs — pension funds paying retirees, endowments funding annual grants — often favor ladders for their predictability.

A **barbell** concentrates holdings at opposite ends of the maturity spectrum — heavy in short-term and long-term bonds, with little in the middle. The long end provides high yield and duration exposure (price appreciation if rates fall); the short end provides liquidity and limits reinvestment risk. A barbell and a bullet (concentrated at a single intermediate maturity) can be constructed to have the same **dollar duration** — the same first-order price sensitivity to parallel yield curve shifts — but they will behave very differently when the yield curve **twists** (short and long rates move differently) or **curves** (the middle moves relative to the ends). Barbells outperform bullets when the yield curve flattens (long rates fall relative to short rates) or when it steepens from the short end. Bullets outperform when intermediate yields fall more than the extremes — a "butterfly" move where the middle of the curve rallies.

The comparison illuminates an important concept from bond immunization: **convexity**. A barbell portfolio has higher convexity than a bullet with the same duration. Higher convexity means the portfolio gains more than it loses symmetrically when yields move in either direction — its price increases accelerate as yields fall and decelerate as yields rise. This convexity premium means barbells tend to outperform bullets in volatile rate environments. But convexity is not free: markets typically price it in, so barbells often trade at a yield disadvantage relative to bullets of the same duration. The strategic choice between ladder, barbell, and bullet thus reflects a view on whether volatility is cheap or expensive, whether the yield curve is expected to shift in level or shape, and whether the investor has liquidity or liability-matching constraints that favor one structure over another.
