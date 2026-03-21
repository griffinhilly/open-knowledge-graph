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

## Questions

```yaml
- question: "A technology company trades at a P/E ratio of 45, while a utility company trades at a P/E of 14. An analyst concludes the tech company is severely overvalued. What critical information is missing from this comparison?"
  type: multiple-choice
  options:
    - "The names of the companies and the year the ratio was calculated"
    - "The expected earnings growth rate and required return for each company — a high P/E may be fully justified by high growth expectations or lower risk"
    - "Whether the utility company pays dividends"
    - "The total number of shares outstanding for each company"
  answer: 1
  explanation: "From the justified P/E formula (P/E = payout ratio / (r − g)), a high P/E can reflect high expected growth (large g), low required return (small r), or generous payout policy — none of which imply overvaluation. Technology companies often have high growth expectations that mathematically justify high multiples. Comparing raw P/E across sectors without examining the underlying growth and risk assumptions confuses the symptom (high multiple) with the diagnosis (overvaluation)."

- question: "According to the Gordon Growth Model derivation of the justified P/E, which of the following changes would cause a stock's P/E ratio to increase, all else equal?"
  type: multiple-choice
  options:
    - "An increase in the required rate of return r"
    - "A decrease in the expected earnings growth rate g"
    - "A decrease in the payout ratio"
    - "An increase in the expected earnings growth rate g"
  answer: 3
  explanation: "The justified P/E = payout ratio / (r − g). Increasing g reduces the denominator (r − g), which increases the ratio. This is why high-growth firms command high P/E multiples — the market is pricing in rapid future earnings growth. Conversely, increasing r (higher required return, implying more risk) raises the denominator and reduces the P/E. Understanding this formula explains most sector-level P/E differences without invoking irrationality."

- question: "A stock with a low P/E ratio is always a better investment than one with a high P/E ratio, because you are paying less for each dollar of earnings."
  type: true-false
  answer: false
  explanation: "False. A low P/E may reflect low growth expectations, elevated risk, or structural industry decline — not undervaluation. From the justified P/E formula, a low P/E arises when r is high (risky company) or g is low (slow-growing or declining company). These are reasons to demand a lower price, not signals of a bargain. 'Value traps' — cheap stocks that stay cheap because fundamentals are genuinely poor — are the graveyard of investors who use P/E in isolation without examining what drives the multiple."

- question: "The P/E ratio alone cannot determine whether a stock is overvalued or undervalued — that judgment requires understanding what growth and risk assumptions would justify the current multiple."
  type: true-false
  answer: true
  explanation: "True. The justified P/E formula (P/E = payout ratio / (r − g)) shows that the correct P/E depends on growth expectations and required return, which differ across firms, sectors, and time periods. A P/E of 30 may be undervalued for a company with 20% annual earnings growth, and a P/E of 10 may be overvalued for a company in structural decline. Valuation requires comparing the actual P/E to what the fundamentals justify — the multiple alone conveys nothing without context."

- question: "Why can a high P/E ratio be fully rational and not indicate overvaluation? Use the Gordon Growth Model derivation to explain."
  type: short-answer
  answer: "The justified P/E derived from the Gordon Growth Model is P/E = payout ratio / (r − g). A high P/E is rational when the expected growth rate g is high (a large g shrinks the denominator, producing a high P/E) or when the required return r is low (less risk demands less return, also shrinking the denominator). A technology company with high expected annual earnings growth will have a high justified P/E; paying 40× earnings for it may be fair value, not speculation. Overvaluation occurs when the actual P/E exceeds what growth and risk can justify — not simply when the P/E is numerically high."
  explanation: "The formula reveals the P/E as a compressed summary of growth and risk assumptions. The error of treating high P/E as overvaluation ignores that different companies have different growth trajectories and risk profiles. The right question is always: what growth rate and risk level would justify this P/E, and are those inputs reasonable given what I know about the company?"
```

## Explainer

From stock valuation fundamentals, you know a stock's price should equal the present value of its future dividends. The **dividend discount model** (DDM) gives a clean formula for a steadily growing firm: P = D₁ / (r − g), where D₁ is next year's dividend, r is the required return, and g is the constant growth rate. This DDM is the theoretical foundation for understanding why the P/E ratio contains so much information.

Divide both sides by earnings per share (EPS): P/EPS = (D₁/EPS) / (r − g). The ratio D₁/EPS is the **payout ratio** — the fraction of earnings paid as dividends. This gives the justified P/E formula: P/E = payout ratio / (r − g). Read this carefully: a high P/E can reflect three distinct things, and you cannot tell which just by looking at the number. It could mean high expected growth (large g), low required return (small r, because the stock is low-risk), or a generous payout policy. Before concluding that a high P/E stock is overvalued, you must understand which of these drives it. Technology firms often trade at P/Es of 30–40× not because investors are irrational, but because they expect fast earnings growth — a high g dramatically lowers the denominator.

**Relative valuation** is the practical application: instead of computing an intrinsic value from scratch, you compare a firm's multiple to that of peers. If an airline trades at 8× earnings while all other airlines trade at 12×, something requires explanation — either the cheap airline has worse fundamentals (lower growth, higher risk), or it is genuinely undervalued. This **comparable company analysis** is fast and grounded in market reality, but it inherits the market's errors: if an entire sector is overvalued, comparables will tell you all the firms are fairly priced relative to each other. Common multiples beyond P/E include **EV/EBITDA** (enterprise value to earnings before interest, taxes, depreciation, and amortization), which is less sensitive to capital structure and accounting differences, and **price-to-book**, which compares market value to accounting net worth.

The deepest pitfall is that the "E" in P/E is an accounting construct. Earnings per share can be manipulated through revenue recognition timing, one-time charges or gains, and amortization choices. Analysts therefore often use **forward P/E** (based on next year's earnings forecast rather than last year's actuals), **normalized P/E** (based on average earnings over a business cycle), or the **Shiller CAPE** (cyclically adjusted P/E, using 10-year average real earnings) to reduce the noise from a single period's earnings. The ratio is simple; interpreting it correctly is not.
