---
id: dividend-discount-model
title: Dividend Discount Model (DDM)
domain: economics
course: financial-economics
prerequisites:
- id: stock-valuation-fundamentals
  type: hard
- id: annuities-and-perpetuities
  type: hard
- id: geometric-series
  type: soft
builds-toward:
- price-earnings-valuation
- capital-asset-pricing-model
tags:
- ddm
- gordon-growth-model
- equity-valuation
- dividends
stage: formal-systems
status: validated
---

# Dividend Discount Model (DDM)

## Core Idea
The dividend discount model values a stock as the present value of all future dividends. The Gordon Growth Model simplifies this for constant dividend growth: P₀ = D₁/(r−g), where D₁ is next year's dividend, r is the required return, and g is the constant perpetual growth rate. This is a growing perpetuity formula applied to equity. The model reveals the three levers of stock value: dividend level, growth rate, and required return (which encodes risk). Extensions include multi-stage DDM for companies whose growth is expected to decelerate from a high initial rate to a stable long-run rate.

## How It's Best Learned
Apply the Gordon Growth Model to a stable dividend-paying utility or consumer staples company, where constant-growth is plausible. Extend to a two-stage model for a faster-growing firm. Verify that the model's implied growth rate for a market index is reasonable compared to historical GDP growth.

## Common Misconceptions
- The DDM cannot be applied naively to companies that pay no dividends — the model must be adapted to use free cash flow to equity instead.
- Assuming constant dividend growth forever is unrealistic for most firms; the choice of terminal growth rate in multi-stage models dominates the resulting valuation.

## Questions

```yaml
- question: "A stable company pays a $4 annual dividend. The required return is 10% and dividends are expected to grow at 6% perpetually, so the stock is currently priced at $100. If the required return rises to 12% while growth stays at 6%, the new price is:"
  type: multiple-choice
  options:
    - "$80 — price falls modestly because the discount rate rose slightly"
    - "$66.67 — price falls significantly because the spread (r−g) doubled from 4% to 6%"
    - "$50 — price falls by half because the required return doubled from 6%"
    - "$133 — price rises because higher required returns attract more investors"
  answer: 1
  explanation: "P₀ = D₁/(r−g). Original: $4/(0.10−0.06) = $4/0.04 = $100. New: $4/(0.12−0.06) = $4/0.06 = $66.67. The spread (r−g) doubled from 4% to 6%, cutting the price by one-third — a dramatic change from just a 2-percentage-point rise in interest rates. This illustrates the model's core insight: stock prices are extremely sensitive to the spread, not just to absolute levels. Option A underestimates the sensitivity; option C incorrectly uses the full required return as the denominator."

- question: "In a two-stage DDM for a fast-growing company, an analyst finds that years 1–5 of high-growth dividends are worth $15 per share today, and the terminal value discounted to today is $85. What does this imply about the valuation?"
  type: multiple-choice
  options:
    - "The model is reliable because both stages contribute substantially, providing a check on each other"
    - "The valuation is dominated by the terminal value, making it highly sensitive to the assumed long-run growth rate"
    - "The high-growth phase is being underestimated — early dividends should contribute more than 15% of value"
    - "The terminal growth rate is implausibly high, since terminal values above $50 are unusual"
  answer: 1
  explanation: "Terminal value represents 85% of total estimated value — which is typical, often ranging from 70–90%. This is the critical insight about multi-stage DDMs: the far-future stable-growth assumptions dominate the output. A small change in the terminal growth rate (say from 3% to 4%) can swing the terminal value by 30–50%, completely swamping the carefully estimated near-term dividends. This is not a flaw in the model — it reflects the genuine difficulty of forecasting far-future cash flows — but it demands humility about any single-number stock valuation."

- question: "According to the Gordon Growth Model, rising interest rates cause stock prices to rise because investors earn higher returns."
  type: true-false
  answer: false
  explanation: "Rising interest rates raise the required return r, which is in the denominator of P₀ = D₁/(r−g). A larger denominator means a lower price. Higher interest rates make stocks less valuable by widening the spread, not more. This is why equity markets typically fall when central banks raise rates. The confusion arises from conflating 'investors earn higher returns on bonds' with 'stocks become more valuable' — in fact, stocks must reprice lower to offer competitive expected returns relative to now-higher bond yields."

- question: "The assumed terminal growth rate in a multi-stage DDM is the single most important input, often accounting for 70–90% of the estimated stock value."
  type: true-false
  answer: true
  explanation: "Because the terminal value captures all cash flows beyond the explicit forecast period — in perpetuity — and is discounted back only once, it dominates the valuation. A company might have carefully estimated dividends for five years, but if the terminal growth rate assumption changes by even 1 percentage point, the terminal value changes substantially, easily overwhelming the near-term dividends. This is why the terminal growth rate deserves more analytical scrutiny than any other model input."

- question: "Why are stock prices so sensitive to small changes in interest rates, according to the logic of the dividend discount model?"
  type: short-answer
  answer: "Stock price in the Gordon Growth Model depends on the spread (r−g), not on r alone. Because the spread is typically small (4–6 percentage points), even a 1-point change in r represents a 20–25% change in the denominator, producing a proportionally large change in price. For example, if r=9% and g=5%, the spread is 4% and a $4 dividend implies a $100 stock. If r rises to 10%, the spread is 5% and the same dividend implies only $80 — a 20% drop from a 1-point rate move."
  explanation: "The mathematical intuition is that the denominator (r−g) is the key lever and it is usually small. Small absolute changes in a small number produce large percentage changes. This is intrinsic to the perpetuity formula and explains why central bank policy announcements move equity markets so dramatically — even expected rate changes are priced in immediately because their effect on the spread is large relative to the spread's current size."
```

## Explainer

From your annuities and perpetuities work, you know how to value an infinite stream of cash flows that grows at a constant rate: PV = C/(r−g). The **dividend discount model** applies that formula directly to stocks by treating dividends as the stream of cash flows and asking: what should an investor pay today for ownership of those future payments?

The logic is clean. A share of stock is a claim on the firm's future dividends. If the firm will pay D₁ next year and dividends grow at a constant rate g forever, the stock is a growing perpetuity: P₀ = D₁/(r−g). The required return r has the same structure as a discount rate in all your present value work — it represents the opportunity cost of capital, which includes both time preference and compensation for risk. A company paying a $3 annual dividend, expected to grow at 3% per year, with a required return of 8%, is worth P₀ = 3/(0.08 − 0.03) = $60. Doubling the growth rate to 6% would raise the price to $100; halving the required return to 4% would raise it to $300. The model immediately shows that stock prices are extremely sensitive to the spread (r − g), which is why even small changes in interest rates or growth expectations move equity markets significantly.

The three levers — **dividend level, growth rate, and required return** — give the model real analytical power. Rearranging gives r = D₁/P₀ + g: the required return equals the **dividend yield** plus the expected growth rate. This decomposition is empirically useful: if you can observe the dividend yield and estimate long-run earnings growth, you can back out what return the market is implicitly demanding. For a mature utility paying a 4% dividend yield with 2% expected growth, the implied required return is 6%. If long-term government bonds yield 4%, the equity risk premium is 2 percentage points.

The **multi-stage DDM** extends this logic for companies that cannot plausibly sustain a single constant growth rate forever. A fast-growing technology firm might grow dividends at 15% for five years as it captures market share, then slow to 5% as competition arrives, then settle at 3% in perpetuity. You handle this by discounting each year of the high-growth period individually (just like an annuity), then applying the Gordon Growth formula to the stable-phase dividend stream to get a terminal value, then discounting that terminal value back to today. In practice, the terminal value typically dominates — it often represents 70–90% of total estimated value — which is why small changes in the assumed terminal growth rate produce enormous swings in estimated stock price. This sensitivity is not a flaw in the model; it reflects the genuine difficulty of forecasting far-future cash flows, and should make you appropriately humble about any single-number stock valuation.
