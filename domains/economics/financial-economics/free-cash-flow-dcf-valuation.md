---
id: free-cash-flow-dcf-valuation
title: Free Cash Flow and DCF Valuation
domain: economics
course: financial-economics
prerequisites:
- id: stock-valuation-fundamentals
  type: hard
- id: present-value-and-discounting
  type: hard
- id: cost-of-equity-capm
  type: hard
builds-toward:
- enterprise-value-calculation
tags:
- equity-valuation
- dcf
- cash-flow
stage: formal-systems
status: draft
---

# Free Cash Flow and DCF Valuation

## Core Idea
Free cash flow (FCF) is cash available after capital expenditures and working capital changes. DCF valuation projects future FCF and discounts at the cost of equity to find intrinsic value, providing a theoretically rigorous equity valuation method.

## How It's Best Learned
Start with a simple 5-year projection and terminal value using a constant growth model. Compare FCF-based values to market prices to identify mispricing.

## Common Misconceptions
- Free cash flow is not the same as net income or accounting earnings.
- Terminal value assumptions heavily influence final valuation and deserve scrutiny.
- Small changes in discount rate or growth assumptions can substantially change valuations.

## Explainer

From present value and discounting, you know that a dollar received in the future is worth less than a dollar today, and the further away it is, the steeper the discount. From CAPM, you know how to estimate the cost of equity — the rate of return shareholders require given the riskiness of the stock. DCF valuation is the application of these ideas to equity: the intrinsic value of a stock is the present value of all future cash flows it will generate, discounted at the appropriate risk-adjusted rate.

The first and most important distinction is between **free cash flow** and accounting earnings. Net income includes non-cash charges (like depreciation) and excludes real cash outflows (like capital expenditures). A company that reports $100M in net income but needs to spend $80M on new equipment and $20M on working capital to sustain its growth has generated nothing for shareholders — it has no free cash flow. **Free cash flow** strips away accounting artifacts and asks: after maintaining and growing the business, how much actual cash is left? FCF = Net Income + Depreciation − Capital Expenditures − Increase in Working Capital. Sometimes it is calculated from operating cash flow (starting from EBITDA or EBIT after taxes) rather than from net income, but the concept is the same: residual cash available to equity holders after all reinvestment needs are met.

A DCF model takes three inputs: (1) projected FCF for a forecast period (typically 5–10 years), (2) a **terminal value** representing all cash flows after the forecast period, and (3) the discount rate (cost of equity from CAPM, or WACC if valuing the whole firm). The terminal value is usually estimated using the **Gordon Growth Model**: TV = FCF_(n+1) / (r − g), where g is the long-run sustainable growth rate. Each year's FCF is then discounted back to today and summed with the discounted terminal value to produce intrinsic value per share.

The unsettling implication is how sensitive the result is to assumptions. A small change in the terminal growth rate g from 3% to 4%, or in the discount rate r from 9% to 8%, can change the valuation by 20–40%. This is not a bug but a feature: it tells you that most of a growing company's value lies in its terminal value — the cash flows beyond the forecast horizon — and small changes in long-run assumptions matter enormously. The discipline of DCF is less about computing a precise number and more about making your assumptions explicit and stress-testing them. A "sensitivity table" showing valuations across a matrix of r and g values is standard practice precisely because no one has high confidence in a single set of inputs.
