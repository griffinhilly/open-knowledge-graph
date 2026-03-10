---
id: net-present-value
title: Net Present Value (NPV)
domain: economics
course: financial-economics
prerequisites:
- id: present-value-and-discounting
  type: hard
- id: scarcity-and-opportunity-cost
  type: soft
builds-toward:
- stock-valuation-fundamentals
- dividend-discount-model
tags:
- npv
- investment-decision
- capital-budgeting
- dcf
stage: formal-systems
status: draft
---

# Net Present Value (NPV)

## Core Idea
Net present value (NPV) is the sum of present values of all cash flows from an investment, minus the initial cost: NPV = Σ [CFt / (1+r)^t] − C₀. A positive NPV means the investment creates value above the opportunity cost of capital; a negative NPV destroys value. NPV is the gold standard decision rule in capital budgeting because it correctly accounts for the time value of money, the riskiness of cash flows (through r), and the full stream of future benefits. All discounted cash flow (DCF) valuation of assets is a direct application of this principle.

## How It's Best Learned
Apply NPV to concrete scenarios — a rental property, a new machine, or a corporate acquisition — and vary the discount rate to see how sensitive the decision is. Compare NPV with simpler rules like payback period and IRR to understand why NPV dominates theoretically while simpler rules persist in practice.

## Common Misconceptions
- NPV is not the same as accounting profit — it is a present-value concept that correctly weights the timing of cash flows, which accounting ignores.
- Treating the discount rate as a given rather than a choice is a major source of valuation disagreement; the rate should reflect the project's specific risk.
