---
id: residual-income-eva-valuation
title: Residual Income and Economic Value Added (EVA)
domain: economics
course: financial-economics
prerequisites:
- id: cost-of-equity-capm
  type: hard
- id: stock-valuation-fundamentals
  type: hard
tags:
- equity-valuation
- eva
- performance-measurement
stage: advanced
status: draft
---

# Residual Income and Economic Value Added (EVA)

## Core Idea
Residual income (net income − equity charge) captures value creation beyond the cost of equity. EVA = NOPAT − (WACC × invested capital) measures true economic profit. Valuation equals book value plus the present value of future residual income.

## How It's Best Learned
Calculate EVA for a company and compare to its market premium (market cap − book value). Use residual income projections to value high-growth and mature firms.

## Questions

```yaml
- question: "A company reports $10 million in net income. Its book equity is $100 million and its cost of equity (from CAPM) is 12%. Which statement best describes the economic value created for shareholders that year?"
  type: multiple-choice
  options:
    - "The company created $10 million in value because it is profitable"
    - "The company destroyed $2 million in economic value, because net income of $10M falls short of the $12M equity charge shareholders required"
    - "Value creation cannot be assessed from net income and cost of equity alone — you also need the market price"
    - "The company created $10 million in value and also has a residual income surplus of $2 million above requirements"
  answer: 1
  explanation: "Residual income = Net Income − (cost of equity × book equity) = $10M − (0.12 × $100M) = $10M − $12M = −$2M. Despite reporting positive net income, the firm earned less than shareholders required to compensate for risk. They would have been better off investing $100M elsewhere at the required 12% return. Positive accounting profit is not sufficient for value creation — you must earn more than the cost of the capital deployed. This is the central insight of residual income analysis."

- question: "A firm's stock trades at exactly book value — its price-to-book ratio is 1.0. What does the residual income valuation model say about market expectations for this firm?"
  type: multiple-choice
  options:
    - "The market expects the firm to become unprofitable within a few years"
    - "The market expects the firm to earn exactly its cost of equity capital — generating zero residual income indefinitely, so no premium or discount beyond book value is warranted"
    - "The firm is undervalued because any profitable firm should trade above book value"
    - "The market expects the firm to pay out all earnings as dividends, leaving no retained earnings to grow book value"
  answer: 1
  explanation: "The residual income model says V₀ = B₀ + PV(future residual income). If V₀ = B₀ (P/B = 1), then PV(future residual income) = 0, meaning markets expect the firm to earn exactly its cost of equity — no more, no less — forever. A firm trading below book value is priced for negative residual income (it will earn less than its equity cost); above book value, for positive residual income. The entire market premium over book value is explained by expected future economic profits."

- question: "A company can report positive net income every year and still destroy shareholder value over the long run."
  type: true-false
  answer: true
  explanation: "True. If a firm consistently earns 8% on equity when its cost of equity is 12%, it reports positive accounting earnings but destroys economic value year after year — shareholders would have been better off putting that capital elsewhere. Residual income captures this: RI = NI − (rₑ × Book Equity) is negative whenever return on equity falls below the required rate. Positive net income is a necessary but not sufficient condition for value creation."

- question: "EVA (Economic Value Added) uses the cost of equity as its hurdle rate, whereas residual income uses the WACC — making EVA the equity-focused measure and residual income the whole-firm measure."
  type: true-false
  answer: false
  explanation: "False — the relationship is reversed. Residual income = Net Income − (rₑ × Book Equity) and is computed from the equity perspective, using only the equity cost. EVA = NOPAT − (WACC × Invested Capital), where WACC incorporates both debt and equity costs weighted by capital structure, and NOPAT is the pre-financing operating profit. EVA is therefore the whole-firm measure; residual income in its standard definition is the equity-only measure."

- question: "Why does the residual income model anchor intrinsic value to book equity plus the present value of future residual incomes, rather than simply discounting future earnings or dividends?"
  type: short-answer
  answer: "Book equity represents the capital already invested in the firm — it is observable and provides a concrete starting point. The question for valuation is not what the firm earns in absolute terms, but how much it earns in excess of what investors could earn elsewhere on that same capital. Residual income isolates this excess: RI = NI − (rₑ × Book Equity). By anchoring to book value, the model accounts for the starting capital base and asks only whether the firm earns above or below its cost of equity going forward. Every dollar of market premium above book value must be justified by positive expected future residual income, making the model especially useful for firms with volatile dividends or negative near-term free cash flows."
  explanation: "This makes the residual income model particularly robust for financial firms (where DCF is awkward due to the nature of cash flows) and growth companies with no dividends. It decomposes the market premium by identifying which years and business segments are expected to earn above-normal returns, providing diagnostic insight unavailable from simpler valuation approaches."
```

## Explainer

From your study of stock valuation fundamentals and the CAPM, you know that equity has a cost. Equity investors bear risk and expect compensation — the required return on equity (rₑ) from the CAPM is not free money; it is the minimum return shareholders demand before they would have been better off investing elsewhere. A firm that reports positive net income has not necessarily created value for its shareholders. If net income is $5 million but equity investors required $7 million to compensate for risk, the firm has actually destroyed $2 million in economic value. **Residual income** makes this explicit: RI = Net Income − (rₑ × Book Equity). It is what remains after charging earnings for the cost of the capital that generated them.

**Economic Value Added (EVA)** extends the same logic to the full firm, not just equity holders. EVA = NOPAT − (WACC × Invested Capital), where NOPAT is net operating profit after tax (the after-tax operating profit before financing costs) and Invested Capital is the total capital employed in the business (debt plus equity). WACC — the weighted average cost of capital you learned from stock valuation — is the hurdle rate for the whole enterprise. If NOPAT exceeds the capital charge, the firm has created economic profit; if not, it has consumed economic value even if accounting profit is positive. This is why EVA became popular as a performance metric in the 1990s: it aligns managerial incentives with genuine value creation rather than accounting manipulation.

The connection to valuation is elegant. The **Residual Income Valuation model** says that the intrinsic value of equity equals its current book value plus the present value of all future residual incomes: V₀ = B₀ + Σ [RIₜ / (1 + rₑ)^t]. The intuition is clean: a firm worth exactly its book value creates zero residual income perpetually — it earns exactly its cost of capital, no more. Every dollar of market premium over book value (the P/B ratio above 1) is justified by positive expected future residual income. A firm trading at three times book value is priced to earn positive economic profits for many years into the future.

This framework resolves a practical challenge with dividend discount or DCF models for firms that pay no dividends or have volatile free cash flows. Many growth companies reinvest aggressively — their dividends are zero and their near-term free cash flows are negative, making traditional models awkward. But their book values are observable and their accounting earnings are measurable. The residual income model anchors valuation to the balance sheet and asks only whether earnings are sufficient to justify the equity capital deployed. This makes it particularly useful for valuing financial firms (banks, insurance companies) and early-stage growth companies, and for decomposing where a firm's market-to-book premium actually comes from — which years and business activities are expected to generate above-normal returns.
