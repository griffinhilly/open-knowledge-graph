---
id: price-earnings-valuation
title: Price-to-Earnings Ratio and Relative Valuation
domain: economics
course: financial-economics
prerequisites:
- id: stock-valuation-fundamentals
  type: hard
- id: profit-maximization-microeconomics
  type: soft
- id: dividend-discount-model
  type: soft
builds-toward:
- efficient-market-hypothesis
- market-anomalies-and-puzzles
tags:
- pe-ratio
- relative-valuation
- multiples
- equity
- comparable-companies
stage: formal-systems
status: validated
---
# Price-to-Earnings Ratio and Relative Valuation

## Core Idea
The price-to-earnings (P/E) ratio — stock price divided by earnings per share — is the most widely used equity valuation multiple. Through the Gordon Growth Model it can be shown that P/E = payout ratio / (r − g), so a high P/E reflects high growth expectations, low risk (low r), or generous payout policies. Relative valuation compares a firm's multiples (P/E, price-to-book, EV/EBITDA) to industry peers or historical averages to identify potential overvaluation or undervaluation. While simpler than full DCF, multiples embed assumptions about growth and risk that analysts must make explicit to use them correctly.

## How It's Best Learned
Compare P/E ratios across sectors — technology vs. utilities — to understand why high-growth sectors command higher multiples. Derive the justified P/E from Gordon Growth Model inputs to understand what the multiple implies about market expectations. Apply comparable company analysis to a real firm.

## Common Misconceptions
- A low P/E is not automatically a signal of undervaluation — it may reflect low growth expectations, elevated risk, or structural decline in the industry.
- Comparing P/E ratios across firms with different accounting standards, capital structures, or earnings quality requires careful normalization.

## Explainer

From stock valuation fundamentals, you know a stock's price should equal the present value of its future dividends. The **dividend discount model** (DDM) gives a clean formula for a steadily growing firm: P = D₁ / (r − g), where D₁ is next year's dividend, r is the required return, and g is the constant growth rate. This DDM is the theoretical foundation for understanding why the P/E ratio contains so much information.

Divide both sides by earnings per share (EPS): P/EPS = (D₁/EPS) / (r − g). The ratio D₁/EPS is the **payout ratio** — the fraction of earnings paid as dividends. This gives the justified P/E formula: P/E = payout ratio / (r − g). Read this carefully: a high P/E can reflect three distinct things, and you cannot tell which just by looking at the number. It could mean high expected growth (large g), low required return (small r, because the stock is low-risk), or a generous payout policy. Before concluding that a high P/E stock is overvalued, you must understand which of these drives it. Technology firms often trade at P/Es of 30–40× not because investors are irrational, but because they expect fast earnings growth — a high g dramatically lowers the denominator.

**Relative valuation** is the practical application: instead of computing an intrinsic value from scratch, you compare a firm's multiple to that of peers. If an airline trades at 8× earnings while all other airlines trade at 12×, something requires explanation — either the cheap airline has worse fundamentals (lower growth, higher risk), or it is genuinely undervalued. This **comparable company analysis** is fast and grounded in market reality, but it inherits the market's errors: if an entire sector is overvalued, comparables will tell you all the firms are fairly priced relative to each other. Common multiples beyond P/E include **EV/EBITDA** (enterprise value to earnings before interest, taxes, depreciation, and amortization), which is less sensitive to capital structure and accounting differences, and **price-to-book**, which compares market value to accounting net worth.

The deepest pitfall is that the "E" in P/E is an accounting construct. Earnings per share can be manipulated through revenue recognition timing, one-time charges or gains, and amortization choices. Analysts therefore often use **forward P/E** (based on next year's earnings forecast rather than last year's actuals), **normalized P/E** (based on average earnings over a business cycle), or the **Shiller CAPE** (cyclically adjusted P/E, using 10-year average real earnings) to reduce the noise from a single period's earnings. The ratio is simple; interpreting it correctly is not.
