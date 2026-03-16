---
id: enterprise-value-calculation
title: Enterprise Value and Valuation Multiples
domain: economics
course: financial-economics
prerequisites:
- id: free-cash-flow-dcf-valuation
  type: hard
- id: price-earnings-valuation
  type: soft
tags:
- equity-valuation
- multiples
- financial-analysis
stage: formal-systems
status: draft
---

# Enterprise Value and Valuation Multiples

## Core Idea
Enterprise value (EV) = market cap + debt − cash. EV/EBITDA, EV/Sales, and similar multiples normalize valuations across firms, enabling relative comparisons. These multiples are faster to calculate than DCF but require comparable company selection.

## Explainer

From your DCF work, you know how to value a firm by discounting its free cash flows. **Enterprise value** captures the same idea but from the market's perspective — it is the price an acquirer would pay to buy the entire business, taking on its debt but pocketing its cash. The formula EV = market cap + net debt (where net debt = total debt − cash) reflects a simple insight: if you buy all the equity and then have to repay the debts, your total cost is market cap + debt. But the target's cash on hand offsets that cost because you now own it, so you subtract cash. The result is the price of the underlying operating business, stripped of capital structure.

Why does capital structure need to be stripped out? Because two identical businesses that generate the same operating cash flows will have different **P/E ratios** if one is funded with debt and the other with equity — interest expense reduces the earnings of the levered firm, making its P/E higher even though the businesses are equally valuable. **EV/EBITDA** solves this: EBITDA (earnings before interest, taxes, depreciation, and amortization) measures operating profitability before financing costs, so the ratio compares business values to operating performance on an apples-to-apples basis across firms with different capital structures. The **EV/Sales** multiple goes further, useful for early-stage firms with negative EBITDA where profitability ratios are meaningless.

The mechanics of comparable company analysis — "comps" — require careful selection. The right peer group consists of firms that share not just an industry label but similar growth rates, margins, capital intensity, and geographic exposure. A high-growth software company and a mature enterprise software vendor are both "software" but have vastly different multiples because growth and margins differ. Once you select a peer group, you compute the median or mean EV/EBITDA (and other multiples) for the comps, then apply those multiples to the target's EBITDA to derive an implied EV. Add cash and subtract debt to get implied equity value; divide by shares outstanding to get implied share price.

The key conceptual limit of multiples is circularity: they encode whatever the market currently values, including market-wide optimism or pessimism. In a bubble, high multiples beget high multiples across an industry. DCF valuations anchor to fundamentals — cash flows, growth rates, discount rates — and can diverge sharply from multiples during dislocations. In practice, analysts run both: a DCF provides an intrinsic-value anchor, while comps show where the market is currently pricing similar assets. The gap between the two is itself informative — either the market is mispricing the asset, or your DCF assumptions need scrutiny.
