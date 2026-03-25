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
- id: earnings-multiple-valuation
  type: soft
- id: equity-valuation-growth-phases
  type: soft
builds-toward:
- growth-vs-value-investing
tags:
- valuation
- multiples
- equity
stage: formal-systems
status: validated
---
# Equity Valuation Using Multiples

## Core Idea
Multiples-based valuation (P/E, P/B, EV/EBITDA, PEG) values a company by comparing it to similar firms' market prices relative to earnings or book value. These methods are faster than DCF but assume relative valuation accuracy. Multiples must be adjusted for differences in growth rates, risk, and capital structure.

## Questions

```yaml
- question: "Company A is a slow-growing retailer with 5% annual earnings growth. Company B is a high-growth tech firm with 35% annual earnings growth. Both earn $2 per share. Company A trades at P/E = 12 and Company B at P/E = 45. A junior analyst says Company B is overvalued relative to Company A because its P/E is nearly 4× higher. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — a higher P/E always indicates overvaluation relative to a lower P/E"
    - "The analyst should compare EV/EBITDA instead of P/E since both companies are in different industries"
    - "P/E ratios are only comparable between companies with similar growth rates, risk, and capital structure; Company B's higher P/E may be justified by its much faster earnings growth"
    - "The analyst is correct only if both companies have the same dividend payout ratio"
  answer: 2
  explanation: "Investors pay a premium P/E for companies expected to grow earnings faster, because a dollar of earnings today from a high-growth firm represents far more future earnings than a dollar from a stable firm. Comparing P/E across companies with 5% vs 35% growth without adjustment is apples-to-oranges. The PEG ratio attempts to normalize for this — Company A has PEG = 12/5 = 2.4, Company B has PEG = 45/35 ≈ 1.3, suggesting Company B is actually cheaper on a growth-adjusted basis. Comparability of peers is the foundational assumption of multiples-based valuation."

- question: "Why do analysts prefer EV/EBITDA over P/E when comparing a highly leveraged company to a nearly debt-free competitor in the same industry?"
  type: multiple-choice
  options:
    - "Because EBITDA is always larger than earnings, making the ratio easier to calculate"
    - "Because EV includes debt and EBITDA is pre-interest, so the ratio is capital-structure-neutral; P/E is distorted by how the company is financed"
    - "Because EV/EBITDA is calculated from market data while P/E requires accounting earnings, which can be manipulated"
    - "Because P/E only works for companies that pay dividends, while EV/EBITDA works for all companies"
  answer: 1
  explanation: "P/E compares equity market cap to net earnings (post-interest). A highly leveraged firm pays more interest, reducing net earnings and inflating P/E — making it look expensive even if its underlying business is equally productive. EV (enterprise value = market cap + net debt) captures the value of the whole business to all capital providers. EBITDA is pre-interest, so it represents operating cash flow before financing decisions. Together, EV/EBITDA lets you compare how the market values underlying business operations independent of financing choices — essential when capital structures differ."

- question: "If every company in a sector has its P/E ratio inflated by speculative enthusiasm, using comps-based valuation will still show a target company as 'fairly valued' relative to its peers, even though it may be expensive in absolute terms."
  type: true-false
  answer: true
  explanation: "This is the fundamental limitation of relative valuation: multiples tell you how a company looks *compared to* similar firms right now, not whether any of those firms are cheap or expensive in an absolute sense. During the dot-com bubble, tech companies with enormous P/E ratios could be 'fairly valued' by comps analysis — because all their comps were equally overvalued. The relative signal was neutral even while DCF analysis would have shown large overvaluation. This is why skilled analysts use multiples alongside intrinsic-value methods, not instead of them."

- question: "A PEG ratio below 1 is a reliable signal that a stock is undervalued, since it indicates the market is pricing the stock below what its growth rate justifies."
  type: true-false
  answer: false
  explanation: "PEG is a rule-of-thumb heuristic, not a rigorous valuation measure. It assumes a linear relationship between P/E and growth rate that doesn't hold in theory or empirical data. Companies with very high growth rates often deserve P/E multiples more than proportional to their growth (non-linearity of value), while very low-quality growth may deserve less. PEG also ignores risk, dividend yield, and the sustainability of forecast growth. A PEG below 1 is interesting evidence but not a reliable trigger — the growth rate itself must be validated, and quality and risk must be considered."

- question: "Why do experienced analysts use both multiples-based valuation and DCF analysis rather than relying on one method alone? What does each method tell you that the other doesn't?"
  type: short-answer
  answer: "Multiples (relative valuation) show how the market currently prices similar companies — they are fast, grounded in observable market prices, and capture current investor sentiment. DCF (intrinsic value) projects future cash flows and discounts them to present value, giving an independent estimate of what the business is worth regardless of what the market thinks now. When the two methods agree, confidence in the valuation is higher. When they diverge significantly, it is a signal to reexamine assumptions — either the DCF inputs are off, or the market (and therefore the comps) is mispricing the sector."
  explanation: "Multiples alone can validate irrational market pricing. DCF alone can be wrong if its assumptions are flawed. Together they triangulate: a company that looks cheap by both measures is a stronger buy case than one that is cheap by only one. This is the practitioner insight the topic builds toward."
```

## Explainer

Every valuation multiple is a compressed version of a discounted cash flow model. When you already understand P/E from your prerequisite work, you know that the price-to-earnings ratio captures what the market is willing to pay per dollar of current earnings. What you are learning now is how to use that ratio systematically — by looking at what similar companies trade at — and how to interpret deviations from those benchmarks. The core logic: if two companies are identical in risk, growth, and capital structure, they should trade at identical multiples. If they don't, something must differ, or one is mispriced.

The **P/E ratio** is the most widely used equity multiple. A company earning $5 per share and trading at $100 has a P/E of 20 — investors are paying $20 for each dollar of annual earnings, effectively expressing confidence in future earnings growth. To use this for valuation, you find comparable companies (the "peer group" or "comps"), calculate their median or mean P/E, and apply it to your target company's earnings: estimated value = median comps P/E × target EPS. The obvious challenge is finding genuinely comparable companies. A retail firm with stable earnings in a mature market should not be compared to a high-growth tech company — the latter deserves a higher P/E because earnings are expected to grow much faster.

The **PEG ratio** (P/E divided by earnings growth rate) attempts to adjust for growth: it normalizes P/E by how fast earnings are expected to grow. A company with a P/E of 30 and 30% expected growth has a PEG of 1.0, which market convention sometimes treats as "fairly valued." A PEG below 1 may suggest undervaluation relative to growth. But PEG has real weaknesses — it assumes a linear relationship between P/E and growth that does not hold cleanly in theory or in data. **P/B** (price-to-book) is more useful for capital-intensive industries like banking, where book value is a meaningful proxy for asset value. **EV/EBITDA** (enterprise value to earnings before interest, taxes, depreciation, and amortization) is preferred when comparing companies with different capital structures: because EV includes debt and EBITDA is pre-interest, the ratio is capital-structure-neutral. You can compare a heavily leveraged firm to an unlevered peer more fairly using EV/EBITDA than P/E.

The fundamental limitation of multiples is that they encode the market's current errors. If the entire sector is overvalued — as tech stocks were in 1999 — comps-based valuation will tell you the target is "fairly valued" relative to peers, even though all peers are expensive in absolute terms. Multiples are best understood as a *relative* valuation tool: they tell you how a company looks compared to similar firms right now, not whether any of them are cheap or expensive in an absolute DCF sense. Skilled analysts use multiples as a sanity check on DCF estimates and vice versa — when the two methods diverge sharply, it is a signal to examine assumptions more carefully.
