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
- id: financial-analysis-valuation-fundamentals
  type: hard
- id: weighted-average-cost-of-capital
  type: hard
builds-toward:
- enterprise-value-calculation
tags:
- equity-valuation
- dcf
- cash-flow
stage: advanced
status: validated
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

## Questions

```yaml
- question: "A company reports $100M in net income, spends $80M on capital expenditures, and requires $30M in additional working capital to support its growth. What is its approximate free cash flow?"
  type: multiple-choice
  options:
    - "$100M — net income represents the cash earnings available to shareholders"
    - "$20M — free cash flow equals net income minus capital expenditures"
    - "−$10M — free cash flow equals net income minus capex minus the working capital increase"
    - "$50M — after adding back assumed depreciation of roughly $40M to net income"
  answer: 2
  explanation: "FCF = Net Income − Capital Expenditures − Increase in Working Capital = $100M − $80M − $30M = −$10M. Despite reporting $100M in accounting profit, this company generated negative free cash flow — it consumed more cash than it produced for shareholders. Option A conflates accounting earnings with cash; net income includes non-cash charges but excludes capex, which is a real cash outflow. Option B omits working capital changes. This negative FCF is a warning sign that the business requires heavy reinvestment just to sustain its reported earnings."

- question: "An analyst values a high-growth company with DCF and finds that the terminal value accounts for 88% of the total valuation. A skeptical colleague says this means the model is unreliable. How should the analyst respond?"
  type: multiple-choice
  options:
    - "Agree — a terminal value above 70% of total value indicates the discount rate is too low"
    - "A high terminal value fraction is normal for growth companies; the right response is to stress-test terminal growth rate and discount rate assumptions with a sensitivity table"
    - "Reduce the terminal growth rate until the terminal value drops below 50% of total value"
    - "Replace the terminal value with a price-to-earnings multiple to reduce model sensitivity"
  answer: 1
  explanation: "High terminal value fractions (often 70–90%) are normal in DCF analysis, especially for growth companies. Most of a company's value lies beyond the near-term forecast horizon. The appropriate response is not to suppress the terminal value but to acknowledge its sensitivity: show how total value changes across a range of terminal growth rates (g) and discount rates (r). The sensitivity table makes assumptions explicit and reveals the range of plausible outcomes — which is the real point of DCF analysis."

- question: "Increasing the terminal growth rate from 3% to 4% has mainly a minor effect on intrinsic value because it mainly affects cash flows far in the future."
  type: true-false
  answer: false
  explanation: "This is the key counterintuitive result of DCF: because terminal value uses the Gordon Growth Model formula TV = FCF/(r − g), a small increase in g (which appears in the denominator) has a disproportionately large effect. With r = 9% and g = 3%, the denominator is 6% — increasing g to 4% drops the denominator to 5%, a 17% reduction that increases terminal value by 20%. Since terminal value typically constitutes 70–90% of total firm value, this one-point shift in g can change total valuation by 15–35%. Terminal value sensitivity is not a minor issue — it is the central uncertainty in most DCF models."

- question: "Free cash flow is a more reliable basis for equity valuation than net income because it removes non-cash charges and deducts actual reinvestment needs."
  type: true-false
  answer: true
  explanation: "Net income includes depreciation (a non-cash charge that inflates reported earnings relative to cash) but excludes capital expenditures (a real cash outflow that reduces cash available to shareholders). A company spending its entire depreciation charge on capex to maintain assets is generating no economic surplus for shareholders, yet reports positive net income. FCF corrects both distortions: add back non-cash charges, then subtract actual cash reinvestment. The result is the true cash available to equity holders — which is what shareholders ultimately own a claim to."

- question: "Why do DCF analysts typically present a range of valuations rather than a single number, and what does this practice reveal about the nature of the method?"
  type: short-answer
  answer: "DCF valuations are highly sensitive to two assumptions that are inherently uncertain: the terminal growth rate g and the discount rate r. Both appear in the denominator of the terminal value formula (r − g), so small changes produce large valuation swings. A sensitivity table showing intrinsic value across a matrix of g and r values conveys the range of plausible outcomes and makes explicit what the analyst is betting on. This practice reveals that DCF's value is not in computing a precise answer — it is in disciplining your assumptions about long-run growth and risk and stress-testing which assumptions drive most of the value."
  explanation: "A single-point DCF estimate creates false precision. The sensitivity table is the honest representation of what the model can and cannot tell you. It also helps distinguish between cases where valuation is robust across a wide range of assumptions versus cases where it is highly dependent on a narrow set of optimistic inputs."
```

## Explainer

From present value and discounting, you know that a dollar received in the future is worth less than a dollar today, and the further away it is, the steeper the discount. From CAPM, you know how to estimate the cost of equity — the rate of return shareholders require given the riskiness of the stock. DCF valuation is the application of these ideas to equity: the intrinsic value of a stock is the present value of all future cash flows it will generate, discounted at the appropriate risk-adjusted rate.

The first and most important distinction is between **free cash flow** and accounting earnings. Net income includes non-cash charges (like depreciation) and excludes real cash outflows (like capital expenditures). A company that reports $100M in net income but needs to spend $80M on new equipment and $20M on working capital to sustain its growth has generated nothing for shareholders — it has no free cash flow. **Free cash flow** strips away accounting artifacts and asks: after maintaining and growing the business, how much actual cash is left? FCF = Net Income + Depreciation − Capital Expenditures − Increase in Working Capital. Sometimes it is calculated from operating cash flow (starting from EBITDA or EBIT after taxes) rather than from net income, but the concept is the same: residual cash available to equity holders after all reinvestment needs are met.

A DCF model takes three inputs: (1) projected FCF for a forecast period (typically 5–10 years), (2) a **terminal value** representing all cash flows after the forecast period, and (3) the discount rate (cost of equity from CAPM, or WACC if valuing the whole firm). The terminal value is usually estimated using the **Gordon Growth Model**: TV = FCF_(n+1) / (r − g), where g is the long-run sustainable growth rate. Each year's FCF is then discounted back to today and summed with the discounted terminal value to produce intrinsic value per share.

The unsettling implication is how sensitive the result is to assumptions. A small change in the terminal growth rate g from 3% to 4%, or in the discount rate r from 9% to 8%, can change the valuation by 20–40%. This is not a bug but a feature: it tells you that most of a growing company's value lies in its terminal value — the cash flows beyond the forecast horizon — and small changes in long-run assumptions matter enormously. The discipline of DCF is less about computing a precise number and more about making your assumptions explicit and stress-testing them. A "sensitivity table" showing valuations across a matrix of r and g values is standard practice precisely because no one has high confidence in a single set of inputs.
