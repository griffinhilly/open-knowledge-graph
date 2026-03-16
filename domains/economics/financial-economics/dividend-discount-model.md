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

## Explainer

From your annuities and perpetuities work, you know how to value an infinite stream of cash flows that grows at a constant rate: PV = C/(r−g). The **dividend discount model** applies that formula directly to stocks by treating dividends as the stream of cash flows and asking: what should an investor pay today for ownership of those future payments?

The logic is clean. A share of stock is a claim on the firm's future dividends. If the firm will pay D₁ next year and dividends grow at a constant rate g forever, the stock is a growing perpetuity: P₀ = D₁/(r−g). The required return r has the same structure as a discount rate in all your present value work — it represents the opportunity cost of capital, which includes both time preference and compensation for risk. A company paying a $3 annual dividend, expected to grow at 3% per year, with a required return of 8%, is worth P₀ = 3/(0.08 − 0.03) = $60. Doubling the growth rate to 6% would raise the price to $100; halving the required return to 4% would raise it to $300. The model immediately shows that stock prices are extremely sensitive to the spread (r − g), which is why even small changes in interest rates or growth expectations move equity markets significantly.

The three levers — **dividend level, growth rate, and required return** — give the model real analytical power. Rearranging gives r = D₁/P₀ + g: the required return equals the **dividend yield** plus the expected growth rate. This decomposition is empirically useful: if you can observe the dividend yield and estimate long-run earnings growth, you can back out what return the market is implicitly demanding. For a mature utility paying a 4% dividend yield with 2% expected growth, the implied required return is 6%. If long-term government bonds yield 4%, the equity risk premium is 2 percentage points.

The **multi-stage DDM** extends this logic for companies that cannot plausibly sustain a single constant growth rate forever. A fast-growing technology firm might grow dividends at 15% for five years as it captures market share, then slow to 5% as competition arrives, then settle at 3% in perpetuity. You handle this by discounting each year of the high-growth period individually (just like an annuity), then applying the Gordon Growth formula to the stable-phase dividend stream to get a terminal value, then discounting that terminal value back to today. In practice, the terminal value typically dominates — it often represents 70–90% of total estimated value — which is why small changes in the assumed terminal growth rate produce enormous swings in estimated stock price. This sensitivity is not a flaw in the model; it reflects the genuine difficulty of forecasting far-future cash flows, and should make you appropriately humble about any single-number stock valuation.
