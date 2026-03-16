---
id: time-value-of-money
title: Time Value of Money
domain: economics
course: financial-economics
prerequisites:
- id: interest-rates-and-loanable-funds
  type: hard
- id: scarcity-and-opportunity-cost
  type: soft
- id: exponential-growth-and-decay
  type: soft
- id: exponent-rules-product-power-quotient
  type: soft
builds-toward:
- present-value-and-discounting
- future-value-and-compounding
tags:
- time-value
- discounting
- compounding
- finance-foundations
stage: abstract-reasoning
status: validated
---

# Time Value of Money

## Core Idea
A dollar today is worth more than a dollar in the future because money available now can be invested to earn returns over time. This fundamental principle underpins all of financial economics and reflects both the opportunity cost of capital and the compensation investors require for deferring consumption. The time value of money exists even in a world with zero inflation, because productive investment opportunities are always available. Quantifying this premium is the first step toward pricing any financial asset.

## How It's Best Learned
Start with a concrete question: would you prefer $100 today or $100 in one year? Introduce interest rates to make the tradeoff precise, then work through numerical examples before generalizing to formulas. Connecting to familiar real-world decisions — savings accounts, mortgages, retirement — builds intuition before abstraction.

## Common Misconceptions
- Time value of money is not solely about inflation; it exists even in a zero-inflation world due to opportunity costs and productive investment.
- Confusing nominal and real interest rates when applying the concept across different time horizons distorts present-value calculations.

## Explainer

The time value of money begins with a question you can answer by reasoning from your prerequisite concepts alone: would you rather have $100 today or $100 in one year? The instinct to say "today" is correct, but the reason matters. It is not primarily about inflation eroding purchasing power — as your Core Idea notes, the time value exists even with zero inflation. The real reason is **opportunity cost**: $100 today can be invested immediately to earn a return. Deferring receipt means forgoing that return. If the interest rate is 5%, $100 today grows to $105 in one year; equivalently, a promise of $100 in one year is only worth about $95.24 today. The interest rate is the price of time — it converts between values at different points on a timeline.

This conversion works in two directions. **Compounding** moves money forward in time: $P invested at rate r for n periods becomes P × (1 + r)ⁿ. **Discounting** moves money backward: a future value FV received n periods from now is worth FV / (1 + r)ⁿ today — its **present value**. Your prerequisite in exponential growth and decay gave you the mathematical machinery; what this topic adds is the economic interpretation. The discount factor 1/(1 + r)ⁿ shrinks with every additional period of delay, capturing the fundamental idea that patience has a cost. A dollar promised 20 years from now at a 10% rate is worth only about $0.15 today — most of the future value is consumed by the opportunity cost of waiting.

The interest rate r in these formulas comes from your prerequisite on loanable funds: it is set in credit markets by the supply of savings and the demand for investment funds. This market-determined rate reflects the productive opportunities available in the economy. When you discount future cash flows at the market interest rate, you are asking: "Would an investor with access to all market opportunities be willing to wait for this payment?" If the present value of a future cash flow exceeds its cost today, the investment is worth making — it offers a return above the opportunity cost of capital. This logic, applied to streams of cash flows, is the foundation for every valuation method in financial economics.

**Nominal versus real rates** is the crucial refinement. The market interest rate you observe is the nominal rate — it includes compensation for both the opportunity cost of capital and for expected inflation. The Fisher equation connects them: (1 + nominal) ≈ (1 + real) × (1 + inflation). When inflation is zero, nominal and real rates coincide, which is why the time value exists even without inflation — the real rate is always positive because productive investment opportunities are always available. In practice, discounting nominal cash flows at nominal rates and real cash flows at real rates gives the same answer; mixing them (discounting nominal cash flows at real rates, or vice versa) produces systematic errors in present value calculations. Keeping this distinction clear is the single most common technical discipline required when applying time value of money across different economic environments.
