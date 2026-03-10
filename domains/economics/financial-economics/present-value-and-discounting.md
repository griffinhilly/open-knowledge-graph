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
status: draft
---

# Present Value and Discounting

## Core Idea
Present value (PV) is the current worth of a future sum of money, found by discounting it at an appropriate rate: PV = FV / (1+r)^t. Discounting is the inverse of compounding — it translates future cash flows into today's dollars. The discount rate reflects both time preference and the riskiness of the cash flows, so riskier cash flows carry higher discount rates and are worth less in present value terms. All of asset pricing — bonds, stocks, real estate — reduces to applying this formula to a stream of uncertain future payments.

## How It's Best Learned
Practice discounting single cash flows at varying rates and horizons to build intuition about sensitivity. Compare PV results at discount rates of 2%, 5%, and 10% for a payment 20 years away to see how dramatically the rate matters. Work backwards from FV to PV and forwards from PV to FV to solidify the inverse relationship.

## Common Misconceptions
- The discount rate is not simply the inflation rate — even real (inflation-adjusted) cash flows must be discounted for time preference and risk.
- Applying an annual rate to monthly periods without adjustment is a frequent and consequential arithmetic error.
