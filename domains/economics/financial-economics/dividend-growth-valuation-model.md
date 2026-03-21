---
id: dividend-growth-valuation-model
title: Dividend Growth Valuation Models
domain: economics
course: financial-economics
prerequisites:
- id: dividend-discount-model
  type: hard
- id: sustainable-growth-rate
  type: hard
tags:
- equity-valuation
- dividends
- growth
stage: formal-systems
status: draft
---

# Dividend Growth Valuation Models

## Core Idea
The Gordon growth model prices stock as P = D₁ / (r − g), where D₁ is next dividend, r is required return, and g is perpetual growth. Two-stage models allow high growth in early years, then stable growth thereafter, accommodating real company life cycles.

## How It's Best Learned
Estimate sustainable growth rate from payout ratio and ROE. Compare model predictions to market prices and assess sensitivity to growth and return assumptions.

## Questions

```yaml
- question: "Stock X has r=12%, g=8%, D₁=$2, giving a Gordon Growth Model price of $50. Analysts revise g upward from 8% to 10%. The new model price is:"
  type: multiple-choice
  options:
    - "$100 — the denominator halved from 4% to 2%, doubling the price"
    - "$60 — the price increases by the same percentage as the growth rate increase"
    - "$50 — growth revisions affect future dividends but not the current model price"
    - "$25 — higher growth increases risk, which raises r and lowers the price"
  answer: 0
  explanation: "P = D₁ / (r - g) = $2 / (0.12 - 0.10) = $2 / 0.02 = $100. The denominator fell from 0.04 to 0.02 — halved — so the price doubled. This illustrates the extreme sensitivity of the Gordon model to growth assumptions. A 2 percentage point change in g produced a 100% change in price. This is why growth stocks are so volatile: investors react sharply to any revision in long-run growth expectations."

- question: "A company has r=8% and g=9%. Applying the Gordon Growth Model gives P = D₁/(0.08-0.09) = -D₁/0.01, a negative price. The correct interpretation is:"
  type: multiple-choice
  options:
    - "The stock has negative value — investors should demand payment to hold it"
    - "The model is inapplicable because g must be strictly less than r for the perpetuity formula to converge"
    - "The formula requires absolute values; the correct price is D₁/0.01"
    - "The negative sign indicates the stock is overvalued relative to intrinsic value"
  answer: 1
  explanation: "The Gordon Growth Model is derived from a geometric series that only converges when g < r. When g ≥ r, the sum of discounted future dividends is infinite (or undefined), reflecting the economically impossible claim that the firm grows faster than the required return forever. No firm can sustain g ≥ r indefinitely — it would eventually exceed the size of the entire economy. The model's constraint g < r is not a mathematical quirk but an economic requirement."

- question: "In the Gordon Growth Model, a firm with a higher sustainable growth rate will always command a higher stock price, all else equal."
  type: true-false
  answer: false
  explanation: "This is true only when g < r and D₁ is held constant — but D₁ is not independent of g. Higher growth requires more reinvestment, which means a lower payout ratio and thus a lower current dividend D₁. The two effects partially offset: higher g raises the price through the denominator but lowers it through D₁. Additionally, if g rises toward r, the denominator approaches zero and the price formula breaks down. The full relationship requires the sustainable growth rate identity (g = ROE × retention) to assess the net effect."

- question: "The Gordon Growth Model can value any publicly traded stock, provided you use accurate near-term dividend forecasts for the next few years."
  type: true-false
  answer: false
  explanation: "The Gordon Growth Model requires a single constant perpetual growth rate — it assumes dividends grow at rate g forever from the very next period. It cannot accommodate a high near-term growth phase followed by slower long-run growth. For companies with variable growth (most real companies), two-stage or multi-stage models are required: explicitly forecast dividends for the high-growth period, then apply the Gordon model as a terminal value at the point where growth stabilizes. Using Gordon for fast-growing companies produces wildly optimistic valuations."

- question: "Why must the growth rate g be strictly less than the required return r in the Gordon Growth Model? What does violating this constraint mean economically?"
  type: short-answer
  answer: "The model is derived from an infinite geometric series with ratio (1+g)/(1+r). This series only converges when the ratio is less than 1, i.e., when g < r. Economically, g > r would mean the firm's dividends grow faster than investors' required return forever — implying the firm eventually becomes infinitely large relative to the economy, which is impossible. No firm can sustainably grow faster than the overall economy indefinitely, so any assumed g must eventually be bounded below nominal GDP growth."
  explanation: "The constraint is both mathematical (series convergence) and economic (no firm can grow faster than the economy forever). In practice, analysts use nominal GDP growth as a ceiling for terminal growth rates in two-stage models. Violations of the constraint often reveal that a near-term high-growth rate has been mistakenly applied as a perpetual rate — the most common misuse of the Gordon model."
```

## Explainer

The dividend discount model you already know establishes the foundational principle: a stock's intrinsic value equals the present value of all future dividends. The practical challenge is that "all future dividends" extends to infinity and requires forecasting dividends year by year indefinitely. The **Gordon Growth Model** solves this by making one simplifying assumption: dividends grow at a constant rate g forever. With that assumption, the infinite sum of discounted dividends collapses into the elegant closed form P = D₁ / (r − g), where D₁ is the next dividend, r is the required rate of return, and g is the perpetual growth rate. This is simply the formula for a perpetuity growing at rate g — a mathematical result you can derive by summing the geometric series.

The model's sensitivity to its inputs is its most important practical lesson. Because g is subtracted from r in the denominator, small changes in either produce large changes in price. If a stock has r = 10% and g = 7%, the denominator is 3% and a 1% increase in g cuts the denominator to 2% — a 50% increase in the model price. This explains why growth stock valuations are so volatile: investors are extremely sensitive to revisions in long-run growth expectations. It also reveals the model's built-in requirement: g must be strictly less than r, or the formula produces a nonsensical negative or infinite price. Economically, no firm can grow faster than the economy indefinitely — this constraint grounds the model in macroeconomic reality.

The **sustainable growth rate** you studied provides the theoretically grounded estimate of g. A firm can only grow as fast as it can reinvest earnings, so g = ROE × retention ratio (equivalently, g = ROE × (1 − payout ratio)). This connects the valuation model to the firm's actual operating decisions: a firm that pays out 80% of earnings has a retention ratio of 20%, and if its ROE is 15%, it can sustainably grow at 3%. Trying to price a stock with a higher assumed growth rate than this suggests either the firm will need to issue equity (diluting shareholders) or the assumption is unrealistic.

**Two-stage models** extend the framework to fit real company life cycles. A young technology company might grow earnings at 20% annually for ten years, then settle into a stable 4% growth rate as competition intensifies and the business matures. You value it by discounting the first ten years of dividends explicitly (like any finite stream of cash flows) and then adding the terminal value — the Gordon Growth Model applied at the end of the high-growth phase, discounted back to today. This two-stage structure is the dominant approach in professional equity valuation: use explicit forecasts for the near term where you have visibility, and anchor the terminal value on a sustainable long-run growth rate that cannot exceed nominal GDP growth.
