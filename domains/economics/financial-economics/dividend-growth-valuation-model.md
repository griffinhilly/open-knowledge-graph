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

## Explainer

The dividend discount model you already know establishes the foundational principle: a stock's intrinsic value equals the present value of all future dividends. The practical challenge is that "all future dividends" extends to infinity and requires forecasting dividends year by year indefinitely. The **Gordon Growth Model** solves this by making one simplifying assumption: dividends grow at a constant rate g forever. With that assumption, the infinite sum of discounted dividends collapses into the elegant closed form P = D₁ / (r − g), where D₁ is the next dividend, r is the required rate of return, and g is the perpetual growth rate. This is simply the formula for a perpetuity growing at rate g — a mathematical result you can derive by summing the geometric series.

The model's sensitivity to its inputs is its most important practical lesson. Because g is subtracted from r in the denominator, small changes in either produce large changes in price. If a stock has r = 10% and g = 7%, the denominator is 3% and a 1% increase in g cuts the denominator to 2% — a 50% increase in the model price. This explains why growth stock valuations are so volatile: investors are extremely sensitive to revisions in long-run growth expectations. It also reveals the model's built-in requirement: g must be strictly less than r, or the formula produces a nonsensical negative or infinite price. Economically, no firm can grow faster than the economy indefinitely — this constraint grounds the model in macroeconomic reality.

The **sustainable growth rate** you studied provides the theoretically grounded estimate of g. A firm can only grow as fast as it can reinvest earnings, so g = ROE × retention ratio (equivalently, g = ROE × (1 − payout ratio)). This connects the valuation model to the firm's actual operating decisions: a firm that pays out 80% of earnings has a retention ratio of 20%, and if its ROE is 15%, it can sustainably grow at 3%. Trying to price a stock with a higher assumed growth rate than this suggests either the firm will need to issue equity (diluting shareholders) or the assumption is unrealistic.

**Two-stage models** extend the framework to fit real company life cycles. A young technology company might grow earnings at 20% annually for ten years, then settle into a stable 4% growth rate as competition intensifies and the business matures. You value it by discounting the first ten years of dividends explicitly (like any finite stream of cash flows) and then adding the terminal value — the Gordon Growth Model applied at the end of the high-growth phase, discounted back to today. This two-stage structure is the dominant approach in professional equity valuation: use explicit forecasts for the near term where you have visibility, and anchor the terminal value on a sustainable long-run growth rate that cannot exceed nominal GDP growth.
