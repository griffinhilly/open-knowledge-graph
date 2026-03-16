---
id: equity-valuation-multiples
title: Equity Valuation Using Multiples
domain: economics
course: financial-economics
prerequisites:
- id: price-earnings-valuation
  type: hard
- id: earnings-models-and-forecasting
  type: soft
builds-toward:
- growth-vs-value-investing
tags:
- valuation
- multiples
- equity
stage: formal-systems
status: draft
---

# Equity Valuation Using Multiples

## Core Idea
Multiples-based valuation (P/E, P/B, EV/EBITDA, PEG) values a company by comparing it to similar firms' market prices relative to earnings or book value. These methods are faster than DCF but assume relative valuation accuracy. Multiples must be adjusted for differences in growth rates, risk, and capital structure.

## Explainer

Every valuation multiple is a compressed version of a discounted cash flow model. When you already understand P/E from your prerequisite work, you know that the price-to-earnings ratio captures what the market is willing to pay per dollar of current earnings. What you are learning now is how to use that ratio systematically — by looking at what similar companies trade at — and how to interpret deviations from those benchmarks. The core logic: if two companies are identical in risk, growth, and capital structure, they should trade at identical multiples. If they don't, something must differ, or one is mispriced.

The **P/E ratio** is the most widely used equity multiple. A company earning $5 per share and trading at $100 has a P/E of 20 — investors are paying $20 for each dollar of annual earnings, effectively expressing confidence in future earnings growth. To use this for valuation, you find comparable companies (the "peer group" or "comps"), calculate their median or mean P/E, and apply it to your target company's earnings: estimated value = median comps P/E × target EPS. The obvious challenge is finding genuinely comparable companies. A retail firm with stable earnings in a mature market should not be compared to a high-growth tech company — the latter deserves a higher P/E because earnings are expected to grow much faster.

The **PEG ratio** (P/E divided by earnings growth rate) attempts to adjust for growth: it normalizes P/E by how fast earnings are expected to grow. A company with a P/E of 30 and 30% expected growth has a PEG of 1.0, which market convention sometimes treats as "fairly valued." A PEG below 1 may suggest undervaluation relative to growth. But PEG has real weaknesses — it assumes a linear relationship between P/E and growth that does not hold cleanly in theory or in data. **P/B** (price-to-book) is more useful for capital-intensive industries like banking, where book value is a meaningful proxy for asset value. **EV/EBITDA** (enterprise value to earnings before interest, taxes, depreciation, and amortization) is preferred when comparing companies with different capital structures: because EV includes debt and EBITDA is pre-interest, the ratio is capital-structure-neutral. You can compare a heavily leveraged firm to an unlevered peer more fairly using EV/EBITDA than P/E.

The fundamental limitation of multiples is that they encode the market's current errors. If the entire sector is overvalued — as tech stocks were in 1999 — comps-based valuation will tell you the target is "fairly valued" relative to peers, even though all peers are expensive in absolute terms. Multiples are best understood as a *relative* valuation tool: they tell you how a company looks compared to similar firms right now, not whether any of them are cheap or expensive in an absolute DCF sense. Skilled analysts use multiples as a sanity check on DCF estimates and vice versa — when the two methods diverge sharply, it is a signal to examine assumptions more carefully.
