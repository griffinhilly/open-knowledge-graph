---
id: earnings-multiple-valuation
title: Price-to-Earnings Multiples and Comparable Company Valuation
domain: economics
course: financial-economics
prerequisites:
- id: price-earnings-valuation
  type: hard
- id: stock-valuation-fundamentals
  type: soft
builds-toward:
- equity-valuation-multiples
tags:
- equity
- valuation
- multiples
- fundamentals
stage: formal-systems
status: draft
---

# Price-to-Earnings Multiples and Comparable Company Valuation

## Core Idea
Earnings multiples (P/E, PEG, EV/EBITDA) provide simple relative valuation by comparing companies to peers. Theoretical P/E depends on growth, risk, and payout ratio: P/E = (payout ratio × (1 + g)) / (r - g). Multiples work best when comparing similar firms, but ignore differences in quality, growth prospects, and risk that drive fundamental value differences.

## How It's Best Learned
Compare valuation multiples across a peer group and create a simple model linking multiples to fundamentals like growth and ROE.

## Explainer

From your prerequisite work on P/E valuation and stock fundamentals, you understand that a stock's intrinsic value depends on the cash flows it is expected to generate and the discount rate that reflects its risk. The dividend discount model gives us P = D/(r - g), where D is the next dividend, r is the required return, and g is the perpetual growth rate. Dividing both sides by earnings E gives the theoretical P/E ratio: P/E = (D/E) / (r - g) = (payout ratio) / (r - g). This formula is the bridge between **relative valuation** (comparing P/E multiples across companies) and **fundamental valuation** (discounting cash flows at a risk-adjusted rate). A stock trading at a higher P/E than peers is either expected to grow faster, has lower risk, or is simply overvalued — the multiple alone cannot distinguish these.

**Comparable company analysis (comps)** is the practical application of this logic. The process begins by assembling a peer group of companies with similar business models, competitive positions, and capital structures. You then compute standardized multiples — P/E (market cap divided by net income), **EV/EBITDA** (enterprise value divided by earnings before interest, taxes, depreciation, and amortization), PEG (P/E divided by expected growth rate) — for each peer and construct a distribution. The subject company's implied value range is derived by applying the peer median or mean multiple to its own earnings. EV/EBITDA is often preferred over P/E because it is capital-structure-neutral: using enterprise value (equity plus net debt) and EBITDA (pre-financing earnings) removes the distortions from different leverage levels, making cross-company comparison cleaner.

The theoretical P/E formula reveals exactly what drives multiple differences across firms. Higher expected growth g raises P/E because future earnings streams are larger. Lower required return r (lower risk, perhaps lower beta) raises P/E because those streams are discounted at a lower rate. A higher payout ratio mechanically raises P/E, though this is partly offset by the growth foregone from paying out rather than reinvesting. The **PEG ratio** — P/E divided by expected growth — is an attempt to control for growth differences, putting high-growth and low-growth firms on the same footing. A PEG below 1 is traditionally interpreted as potentially undervalued (you are paying less than one unit of P/E for each percentage point of growth), though this is a heuristic rather than a rigorous result.

The critical limitation of multiples is that they summarize everything into one number, hiding the underlying drivers. Two firms with identical P/E ratios can have completely different growth prospects, risk profiles, and return-on-equity characteristics that will lead to very different fundamental values. Comps analysis is most reliable when the peer group is genuinely comparable — similar industry economics, growth stage, and risk — and weakest when applied across companies with structural differences. In practice, equity analysts use multiples as a **sanity check** alongside DCF valuation: if the DCF says a stock is worth $50 but every comparable trades at a multiple implying $25, the analyst needs to explain that gap or revisit the DCF assumptions. The two methods triangulate rather than substitute for each other.
