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
