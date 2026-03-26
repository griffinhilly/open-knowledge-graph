---
id: stock-valuation-fundamentals
title: Stock Valuation Fundamentals
domain: economics
course: financial-economics
prerequisites:
- id: net-present-value
  type: hard
- id: market-equilibrium
  type: soft
builds-toward:
- dividend-discount-model
- price-earnings-valuation
- risk-and-return-tradeoff
tags:
- equity-valuation
- intrinsic-value
- dcf
- stocks
stage: formal-systems
status: validated
---

# Stock Valuation Fundamentals

## Core Idea
The intrinsic value of a stock is the present value of all cash flows it will generate for shareholders — dividends, buybacks, and ultimately liquidation proceeds. Unlike bonds, stocks carry no fixed maturity or promised cash flows, so valuation requires estimating uncertain future earnings and growth rates. The three main valuation approaches are discounted cash flow (DCF) models (theoretically rigorous), relative valuation using multiples like P/E (practical and widely used), and asset-based approaches. The gap between estimated intrinsic value and the current market price defines the investment thesis for active managers.

## How It's Best Learned
Start with the simplest case — a stock paying a constant, perpetual dividend — then relax assumptions to allow growth and varying payouts. Compare DCF outputs to actual market prices for real companies and understand what growth rates the market is implicitly pricing in.

## Common Misconceptions
- Market price and intrinsic value are not the same thing — whether they converge quickly, slowly, or never is exactly what the efficient markets debate is about.
- Stock valuation is inherently uncertain and model-dependent; different analysts with the same facts can reach widely different values by varying growth rate and discount rate assumptions.

## Questions

```yaml
- question: "Which of the following best describes the intrinsic value of a stock according to discounted cash flow theory?"
  type: multiple-choice
  options:
    - "The current market price of the stock on an exchange"
    - "The book value of the company's assets minus its liabilities"
    - "The present value of all future cash flows the stock will generate for shareholders"
    - "The stock's earnings per share multiplied by the industry-average P/E ratio"
  answer: 2
  explanation: "DCF theory defines intrinsic value as the present value of all future cash flows attributable to shareholders — dividends, buybacks, and terminal value. Market price is what the stock trades for today, which may differ from intrinsic value. Book value is an accounting measure, not a forward-looking cash flow concept. P/E multiples are a relative valuation shortcut, not the theoretical definition of intrinsic value."

- question: "If two analysts use the same earnings forecasts and the same DCF model but reach very different intrinsic value estimates, they should have made a calculation error."
  type: true-false
  answer: false
  explanation: "Small differences in discount rate or long-term growth rate assumptions produce dramatically different valuations because these inputs affect a perpetuity-like calculation. A 1 percentage point change in the discount rate or terminal growth rate can shift estimated intrinsic value by 30-50%. This is a feature of the math, not an error — it reflects the genuine uncertainty in stock valuation and why 'valuation is an art as much as a science.'"

- question: "Why does stock valuation require estimating future cash flows rather than simply observing them, unlike bond valuation?"
  type: short-answer
  answer: "Stocks have no fixed maturity date, no promised coupon payments, and no guaranteed principal repayment. Future dividends and earnings depend on uncertain business performance. Bond cash flows (coupons and face value) are contractually specified, making them straightforward to discount. For stocks, the analyst must forecast what the business will earn and pay out, which introduces significant uncertainty."
  explanation: "Bonds are contracts: the issuer promises specific cash flows on specific dates, and the only uncertainty is default risk. Stocks are residual claims on a business's future profitability — there are no guaranteed payments. The entire valuation problem for stocks is forecasting uncertain future earnings and growth rates, which is why reasonable analysts using the same framework can reach very different values."
```

## Explainer

You already understand present value: a dollar received in the future is worth less than a dollar today because you could have invested that dollar in the meantime. Stock valuation applies this idea directly. A share of stock is a claim on a portion of a company's future cash flows — primarily dividends, share buybacks, and ultimately whatever the firm would return to shareholders if it were wound down. The intrinsic value of a share is the present value of all those future cash flows, discounted at a rate that reflects their riskiness.

The simplest version of this is the Gordon Growth Model (dividend discount model with constant growth): V = D₁ / (r - g), where D₁ is next year's dividend, r is the required return, and g is the constant growth rate. If a company will pay a $2 dividend next year and dividends grow at 3% forever, and you require a 9% return, the stock is worth $2 / (0.09 - 0.03) = $33.33. This formula is elegant but fragile — the denominator r - g is small, so tiny changes in either input produce large changes in value. This sensitivity is why stock valuation is inherently uncertain even with a precise framework.

In practice, analysts use a multi-stage DCF model: they project specific cash flows for a near-term period (often 5-10 years), then add a terminal value for everything beyond that horizon. The terminal value typically uses a perpetuity formula and accounts for the bulk of the estimated value — often 60-80% of the total. Because the terminal value depends on assumptions about the long-run growth rate and discount rate, getting those assumptions slightly wrong has enormous consequences.

Relative valuation offers a practical alternative. Instead of modeling cash flows directly, you compare the stock's price-to-earnings (P/E) ratio, price-to-book, or enterprise value-to-EBITDA to those of comparable companies or to historical averages. The logic is that if Company A trades at 15x earnings and comparable Company B trades at 20x earnings with similar growth and risk, B may be overvalued relative to A. Multiples are fast and grounded in what real investors are actually paying — but they inherit whatever mispricing exists in the comparable companies.

The key insight from your prerequisite work on market equilibrium: market price and intrinsic value are not the same thing. In efficient markets, they converge quickly as informed investors trade on mispricings. In less efficient markets, or for less liquid stocks, they can diverge for extended periods. The investment thesis for any active manager — buying a stock they believe is undervalued — is fundamentally a claim that they have a more accurate estimate of intrinsic value than the current market price reflects.
