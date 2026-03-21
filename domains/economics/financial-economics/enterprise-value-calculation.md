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
stage: advanced
status: draft
---

# Enterprise Value and Valuation Multiples

## Core Idea
Enterprise value (EV) = market cap + debt − cash. EV/EBITDA, EV/Sales, and similar multiples normalize valuations across firms, enabling relative comparisons. These multiples are faster to calculate than DCF but require comparable company selection.

## Questions

```yaml
- question: "Company A and Company B have identical operating businesses with the same EBITDA. Company A is entirely equity-financed; Company B carries significant debt. An analyst compares them using P/E ratios and finds Company B has a much higher P/E. What best explains why this comparison is misleading?"
  type: multiple-choice
  options:
    - "P/E ratios cannot be computed for companies that have debt outstanding"
    - "Interest expense reduces Company B's earnings, making its P/E artificially high even though both businesses are equally valuable. EV/EBITDA would show equal multiples because it measures value relative to pre-financing operating profit"
    - "The analyst should use market cap directly, not P/E, when comparing levered and unlevered firms"
    - "P/E is always more accurate than EV/EBITDA; the analyst should trust the P/E comparison"
  answer: 1
  explanation: "Interest expense is a financing cost, not an operating cost. Company B pays interest, which reduces its net income and raises its P/E (same business value, lower earnings denominator). But this reflects capital structure, not operating performance. EBITDA removes interest before computing the ratio, putting both companies on equal footing regardless of how they are financed. This is why EV/EBITDA is the standard for cross-company comparisons: it isolates the value of the operating business from financing choices."

- question: "A company has a market capitalization of $800M, total debt of $300M, and $100M in cash. What is its enterprise value?"
  type: multiple-choice
  options:
    - "$1,200M — all balance sheet components are added"
    - "$1,100M — market cap plus debt, ignoring cash"
    - "$1,000M — market cap + debt − cash = $800M + $300M − $100M"
    - "$600M — market cap minus net debt ($300M − $100M)"
  answer: 2
  explanation: "EV = market cap + debt − cash = $800M + $300M − $100M = $1,000M. The logic: to acquire the entire company you buy all the equity ($800M) and assume the debt ($300M), but you also receive the company's $100M cash (which offsets your cost). Net acquisition cost = $1,000M. Cash is subtracted — not added — because the acquirer gains it. This is the most commonly confused computation: students who think of cash as 'more value to add' get it backwards — cash you inherit upon acquisition reduces your net cost."

- question: "When calculating enterprise value, a company's cash is added to market cap and debt because cash represents additional value an acquirer captures."
  type: true-false
  answer: false
  explanation: "Cash is SUBTRACTED in the EV formula: EV = market cap + debt − cash. When you acquire a company, you pay the market cap and take on the debt — but you also instantly own the cash. That cash offsets your cost, so it reduces EV. A company with $500M in cash sitting in an otherwise modest business has a lower EV than its market cap + debt would suggest, because the $500M is a financial asset that comes directly to you as the new owner. EV captures the price of the operating business, stripped of excess cash."

- question: "Two companies in the same industry with identical EV/EBITDA multiples are necessarily fairly valued relative to each other."
  type: true-false
  answer: false
  explanation: "EV/EBITDA normalizes for capital structure but not for differences in growth rates, margins, or capital intensity. A high-growth software company and a mature enterprise software vendor might both be labeled 'software,' but the former justifiably commands a premium multiple. Comparable company analysis requires selecting peers that are truly comparable on the dimensions that drive valuation — growth, profitability, competitive position, and capital requirements. Identical multiples between incomparable companies tells you nothing useful about relative fair value."

- question: "Why does the enterprise value formula subtract cash and add debt, rather than treating them symmetrically as balance sheet items?"
  type: short-answer
  answer: "Debt is added because it represents a claim on the business that an acquirer must assume — it is part of the total cost of buying the enterprise. Cash is subtracted because it is an asset the acquirer gains immediately upon purchase, directly offsetting the acquisition cost. The asymmetry reflects the distinction between financial liabilities (debt increases total cost) and financial assets (cash reduces net cost). EV = what you pay (equity + debt) minus what you instantly receive (cash) = the price of the underlying operating business, independent of its financing."
  explanation: "The formula aims to capture only the value of the operating business, stripped of pure financial claims. Cash could be distributed to shareholders today without affecting operations — it is not an operating asset. Debt reduces what equity holders receive. Together, EV strips both out so that two identical businesses with different amounts of cash or different capital structures compare at equal EV, enabling the apples-to-apples analysis that multiples like EV/EBITDA are designed to provide."
```

## Explainer

From your DCF work, you know how to value a firm by discounting its free cash flows. **Enterprise value** captures the same idea but from the market's perspective — it is the price an acquirer would pay to buy the entire business, taking on its debt but pocketing its cash. The formula EV = market cap + net debt (where net debt = total debt − cash) reflects a simple insight: if you buy all the equity and then have to repay the debts, your total cost is market cap + debt. But the target's cash on hand offsets that cost because you now own it, so you subtract cash. The result is the price of the underlying operating business, stripped of capital structure.

Why does capital structure need to be stripped out? Because two identical businesses that generate the same operating cash flows will have different **P/E ratios** if one is funded with debt and the other with equity — interest expense reduces the earnings of the levered firm, making its P/E higher even though the businesses are equally valuable. **EV/EBITDA** solves this: EBITDA (earnings before interest, taxes, depreciation, and amortization) measures operating profitability before financing costs, so the ratio compares business values to operating performance on an apples-to-apples basis across firms with different capital structures. The **EV/Sales** multiple goes further, useful for early-stage firms with negative EBITDA where profitability ratios are meaningless.

The mechanics of comparable company analysis — "comps" — require careful selection. The right peer group consists of firms that share not just an industry label but similar growth rates, margins, capital intensity, and geographic exposure. A high-growth software company and a mature enterprise software vendor are both "software" but have vastly different multiples because growth and margins differ. Once you select a peer group, you compute the median or mean EV/EBITDA (and other multiples) for the comps, then apply those multiples to the target's EBITDA to derive an implied EV. Add cash and subtract debt to get implied equity value; divide by shares outstanding to get implied share price.

The key conceptual limit of multiples is circularity: they encode whatever the market currently values, including market-wide optimism or pessimism. In a bubble, high multiples beget high multiples across an industry. DCF valuations anchor to fundamentals — cash flows, growth rates, discount rates — and can diverge sharply from multiples during dislocations. In practice, analysts run both: a DCF provides an intrinsic-value anchor, while comps show where the market is currently pricing similar assets. The gap between the two is itself informative — either the market is mispricing the asset, or your DCF assumptions need scrutiny.
