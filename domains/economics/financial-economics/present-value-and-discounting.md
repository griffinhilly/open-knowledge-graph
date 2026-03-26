---
id: present-value-and-discounting
title: Present Value and Discounting
domain: economics
course: financial-economics
prerequisites:
- id: time-value-of-money
  type: hard
- id: exponential-functions-and-graphs
  type: soft
- id: geometric-series
  type: soft
builds-toward:
- net-present-value
- bond-pricing
- dividend-discount-model
tags:
- present-value
- discounting
- cash-flows
stage: formal-systems
status: validated
---

# Present Value and Discounting

## Core Idea
Present value (PV) is the current worth of a future sum of money, found by discounting it at an appropriate rate: PV = FV / (1+r)^t. Discounting is the inverse of compounding — it translates future cash flows into today's dollars. The discount rate reflects both time preference and the riskiness of the cash flows, so riskier cash flows carry higher discount rates and are worth less in present value terms. All of asset pricing — bonds, stocks, real estate — reduces to applying this formula to a stream of uncertain future payments.

## How It's Best Learned
Practice discounting single cash flows at varying rates and horizons to build intuition about sensitivity. Compare PV results at discount rates of 2%, 5%, and 10% for a payment 20 years away to see how dramatically the rate matters. Work backwards from FV to PV and forwards from PV to FV to solidify the inverse relationship.

## Common Misconceptions
- The discount rate is not simply the inflation rate — even real (inflation-adjusted) cash flows must be discounted for time preference and risk.
- Applying an annual rate to monthly periods without adjustment is a frequent and consequential arithmetic error.

## Questions

```yaml
- question: "If the annual discount rate rises from 5% to 10%, what happens to the present value of $1,000 received exactly 20 years from now?"
  type: multiple-choice
  options: ["PV falls slightly, by about 10-15%", "PV is halved, because the rate doubled", "PV falls dramatically, by roughly 60%", "PV is unchanged because the future cash flow is fixed at $1,000"]
  answer: 2
  explanation: "At 5%: PV = 1000 / 1.05^20 ≈ $377. At 10%: PV = 1000 / 1.10^20 ≈ $149. That is a drop of about $228, or roughly 60%. This illustrates the extreme sensitivity of long-horizon present values to the discount rate — a consequence of exponential discounting. Doubling the rate does not halve PV because the relationship is exponential, not linear."

- question: "The discount rate used to compute present value mainly needs to account for expected inflation; there is no reason to adjust for risk."
  type: true-false
  answer: false
  explanation: "The discount rate has (at least) three components: time preference (people prefer money now even with no inflation), expected inflation (a dollar loses purchasing power over time), and a risk premium (uncertain cash flows are worth less than certain ones). Even after adjusting for inflation using real cash flows, you must still discount for time preference and risk. Ignoring the risk component leads to systematically overvaluing risky assets."

- question: "Explain in economic terms why $1,000 promised 30 years from now is worth less than $1,000 today, even if inflation is zero and there is no default risk."
  type: short-answer
  answer: "$1,000 today can be invested to earn a real return over 30 years, growing substantially in real purchasing power. Waiting 30 years means forgoing that compounding — the opportunity cost is the future wealth the money would have accumulated. This time preference (preferring consumption sooner rather than later) is real even without inflation or default risk, and it is captured by the real risk-free discount rate."
  explanation: "Discounting is the inverse of compounding. If you can earn a 3% real return, $1,000 today becomes roughly $2,427 in 30 years. Equivalently, a promise of $1,000 in 30 years is worth only about $412 today — you would need to invest $412 now at 3% to have $1,000 in 30 years. The discount rate does not require inflation to be positive; even in a zero-inflation world, capital is productive and time has value."
```

## Explainer

From your study of the time value of money, you know that $1 today is worth more than $1 in the future — money has time value because it can be invested to grow. Present value and discounting formalize this intuition: they provide a precise way to translate future cash flows into today's dollars so that cash flows arriving at different times can be compared on a common footing.

The core formula is simple: PV = FV / (1 + r)^t, where FV is the future cash flow, r is the discount rate per period, and t is the number of periods. This is exactly the inverse of the compounding formula FV = PV × (1 + r)^t that you already know. Discounting asks: if I would end up with FV dollars in t years, how much would I need today — invested at rate r — to arrive at that number? The answer is PV. Every present value calculation is secretly a question about compound growth run in reverse.

The discount rate r is doing substantial work in this formula, and its components matter. It must compensate for at least three things: time preference (rational people prefer earlier consumption, even in a world without inflation), expected inflation (a dollar in the future buys less), and risk (uncertain cash flows are worth less than certain ones of the same nominal size). When you discount a real (inflation-adjusted) cash flow, inflation drops out, but time preference and risk remain. A riskier cash flow — say, a startup's projected revenue versus a government bond coupon — commands a higher discount rate and therefore has a lower present value, all else equal. This is why risky assets must offer higher expected returns.

The exponential structure of discounting has a counterintuitive implication: the discount rate matters enormously for long-horizon cash flows and much less for near-term ones. Discounting $1,000 at 5% vs. 10% for 1 year gives $952 vs. $909 — a modest difference. Do the same for 30 years and you get $231 vs. $57 — a factor of four. This sensitivity is why small changes in the discount rate used to value long-lived assets (infrastructure, pension liabilities, forests) produce enormous changes in assessed value, and why the choice of discount rate is often the central contested assumption in policy debates about climate change or long-term investment.

To use the formula correctly, be precise about matching the discount rate to the period length. An annual rate of 12% is not the same as a monthly rate of 1% compounded — well, the monthly rate gives (1.01)^12 ≈ 1.1268, slightly different. Always convert rates to match the compounding period of your cash flows. This seemingly minor detail produces real errors in mortgage pricing, bond valuation, and capital budgeting if ignored. The mechanics of present value are simple; the discipline of applying them consistently is where most mistakes occur.
