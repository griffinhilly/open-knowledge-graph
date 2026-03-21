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
stage: formal-systems
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

## Questions

```yaml
- question: "In a hypothetical economy with perfectly stable prices (zero inflation), a bank still charges 3% annual interest on loans. A student argues this must be a mistake — with no inflation, interest rates should be zero. Is the student right?"
  type: multiple-choice
  options:
    - "Yes — interest rates exist only to compensate lenders for the loss of purchasing power caused by inflation"
    - "Partly — the rate should be close to zero, but banks add a small administrative fee"
    - "No — even with zero inflation, a positive real interest rate is justified because productive investment opportunities exist; borrowers can earn returns by deploying the funds"
    - "No — interest rates in zero-inflation economies exist solely to compensate for default risk"
  answer: 2
  explanation: "This directly tests the core insight: time value of money is NOT primarily about inflation. Even with zero inflation, money today is more valuable than the same amount in the future because it can be invested immediately to earn a return. The 3% rate reflects the opportunity cost of capital — the real return available from productive investment. If a lender gives up $100 today, they forgo the returns that $100 could have earned. A borrower who can earn 10% by investing the loan proceeds can afford to pay 3% interest and still come out ahead. Inflation is a separate consideration layered on top of this fundamental principle."

- question: "A project promises to return $1,000 in 5 years. At a 10% annual discount rate, its present value is approximately $621. This calculation tells you:"
  type: multiple-choice
  options:
    - "An investor should be willing to pay up to $1,000 today to receive $1,000 in 5 years"
    - "The project earns a 10% return on an investment of $621"
    - "An investor who has access to 10% market returns values receiving $1,000 in 5 years as equivalent to having $621 today"
    - "The investor profits $379 by investing in this project"
  answer: 2
  explanation: "Present value answers the question: given access to market returns of 10%, how much would I pay today for this future cash flow? $621 invested at 10% for 5 years grows to $621 × (1.10)^5 ≈ $1,000. So the future payment and the current sum are exactly equivalent from the investor's perspective — they offer the same outcome. This is the core logic of discounting: translating future cash flows into today's terms using the opportunity cost of capital as the conversion rate."

- question: "Discounting nominal cash flows at a real interest rate produces a correct present value calculation."
  type: true-false
  answer: false
  explanation: "Mixing nominal and real is a systematic error. Nominal cash flows already include expected inflation (they are in future dollars, not today's dollars). A real interest rate strips out inflation from the discount rate. Discounting nominal cash flows at the real rate double-counts inflation: the cash flows haven't been adjusted for inflation, but the discount rate has — the result is artificially high present values. The correct approach is either (nominal cash flows) / (nominal discount rate) or (real cash flows) / (real discount rate). Both produce identical answers when done correctly."

- question: "The time value of money arises primarily because inflation erodes the purchasing power of future dollars."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about time value of money. Inflation is a real phenomenon that affects the nominal interest rate, but it is not the source of time value. The foundational reason is opportunity cost: a dollar today can be invested immediately to earn a real return. Even in a world with zero inflation, productive investment opportunities exist — a business can earn returns on capital, a lender can earn a real interest rate. Time value exists because of these productive opportunities, independently of whether prices are rising."

- question: "Why does a dollar today have more value than a dollar one year from now, even in a world with no inflation?"
  type: short-answer
  answer: "Because the dollar today can be invested immediately to earn a real return over the year. Productive investment opportunities — businesses generating output, loans earning interest — exist regardless of whether prices are stable or rising. Deferring receipt means forgoing those returns. The interest rate in a zero-inflation world is the real interest rate, reflecting the opportunity cost of capital: what the dollar could have earned if received and deployed today rather than in the future."
  explanation: "The distinction matters enormously in practice. If time value were only about inflation, then in a deflationary environment (falling prices), money in the future would be worth more than money today — but this doesn't follow. Real interest rates remain positive even in deflation because real productive opportunities persist. The interest rate is the price of time, and that price is set by the supply of savings and the demand for investment capital, not by the price level."
```

## Explainer

The time value of money begins with a question you can answer by reasoning from your prerequisite concepts alone: would you rather have $100 today or $100 in one year? The instinct to say "today" is correct, but the reason matters. It is not primarily about inflation eroding purchasing power — as your Core Idea notes, the time value exists even with zero inflation. The real reason is **opportunity cost**: $100 today can be invested immediately to earn a return. Deferring receipt means forgoing that return. If the interest rate is 5%, $100 today grows to $105 in one year; equivalently, a promise of $100 in one year is only worth about $95.24 today. The interest rate is the price of time — it converts between values at different points on a timeline.

This conversion works in two directions. **Compounding** moves money forward in time: $P invested at rate r for n periods becomes P × (1 + r)ⁿ. **Discounting** moves money backward: a future value FV received n periods from now is worth FV / (1 + r)ⁿ today — its **present value**. Your prerequisite in exponential growth and decay gave you the mathematical machinery; what this topic adds is the economic interpretation. The discount factor 1/(1 + r)ⁿ shrinks with every additional period of delay, capturing the fundamental idea that patience has a cost. A dollar promised 20 years from now at a 10% rate is worth only about $0.15 today — most of the future value is consumed by the opportunity cost of waiting.

The interest rate r in these formulas comes from your prerequisite on loanable funds: it is set in credit markets by the supply of savings and the demand for investment funds. This market-determined rate reflects the productive opportunities available in the economy. When you discount future cash flows at the market interest rate, you are asking: "Would an investor with access to all market opportunities be willing to wait for this payment?" If the present value of a future cash flow exceeds its cost today, the investment is worth making — it offers a return above the opportunity cost of capital. This logic, applied to streams of cash flows, is the foundation for every valuation method in financial economics.

**Nominal versus real rates** is the crucial refinement. The market interest rate you observe is the nominal rate — it includes compensation for both the opportunity cost of capital and for expected inflation. The Fisher equation connects them: (1 + nominal) ≈ (1 + real) × (1 + inflation). When inflation is zero, nominal and real rates coincide, which is why the time value exists even without inflation — the real rate is always positive because productive investment opportunities are always available. In practice, discounting nominal cash flows at nominal rates and real cash flows at real rates gives the same answer; mixing them (discounting nominal cash flows at real rates, or vice versa) produces systematic errors in present value calculations. Keeping this distinction clear is the single most common technical discipline required when applying time value of money across different economic environments.
