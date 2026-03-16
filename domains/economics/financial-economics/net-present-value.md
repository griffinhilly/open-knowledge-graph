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
stage: abstract-reasoning
status: validated
---

# Net Present Value (NPV)

## Core Idea
Net present value (NPV) is the sum of present values of all cash flows from an investment, minus the initial cost: NPV = Σ [CFt / (1+r)^t] − C₀. A positive NPV means the investment creates value above the opportunity cost of capital; a negative NPV destroys value. NPV is the gold standard decision rule in capital budgeting because it correctly accounts for the time value of money, the riskiness of cash flows (through r), and the full stream of future benefits. All discounted cash flow (DCF) valuation of assets is a direct application of this principle.

## How It's Best Learned
Apply NPV to concrete scenarios — a rental property, a new machine, or a corporate acquisition — and vary the discount rate to see how sensitive the decision is. Compare NPV with simpler rules like payback period and IRR to understand why NPV dominates theoretically while simpler rules persist in practice.

## Common Misconceptions
- NPV is not the same as accounting profit — it is a present-value concept that correctly weights the timing of cash flows, which accounting ignores.
- Treating the discount rate as a given rather than a choice is a major source of valuation disagreement; the rate should reflect the project's specific risk.

## Explainer

From present value and discounting, you know that a dollar received in the future is worth less than a dollar today — by the factor 1/(1+r)^t, where r is the opportunity cost of capital. From scarcity and opportunity cost, you know that every resource committed to one use has an implicit cost: the best forgone alternative. NPV combines these: it asks whether an investment earns more than the opportunity cost of the capital committed to it. If you could earn r on equally risky investments elsewhere, does this project beat that benchmark? NPV = 0 means it exactly matches the benchmark; NPV > 0 means it outperforms.

The formula makes this precise: NPV = −C₀ + CF₁/(1+r) + CF₂/(1+r)² + ⋯ + CFₜ/(1+r)ᵀ. Each future cash flow is discounted back to present value, and the initial cost C₀ is subtracted. The sign convention matters: C₀ is negative (cash out today) and future CFt are positive (cash in later). The sum converts an uneven stream of future cash flows into a single present-day number that can be directly compared to the investment cost. If the sum of discounted inflows exceeds the outlay, the project creates value above the cost of capital — it should be accepted.

Consider a machine that costs $10,000 and generates $4,000 in cost savings for each of 3 years. At r = 10%: PV of savings = 4000/1.1 + 4000/1.21 + 4000/1.331 = 3636 + 3306 + 3005 = $9,947. NPV = $9,947 − $10,000 = −$53. The project fails by $53 — it earns just under 10%. At r = 9%, NPV is positive; at r = 10%, negative. This sensitivity illustrates the central role of the discount rate: the accept/reject decision can flip entirely based on r. This is why valuation disagreements in practice almost always trace back to disagreements about the discount rate, not the cash flow forecast.

NPV is the theoretically correct decision rule because it avoids the pitfalls of simpler alternatives. The **payback period** — how quickly the investment is recovered — ignores cash flows after payback and ignores the time value of money: $4,000 received in year 1 and $4,000 received in year 10 are treated identically. The **internal rate of return (IRR)** — the discount rate that sets NPV to zero — is the rate the project earns, and it works fine for simple projects. But IRR has ranking problems when comparing projects of different scales or durations, and it can produce multiple solutions when cash flows change sign. NPV ranks projects consistently with maximizing total wealth and handles all these cases correctly.

The discount rate r is not a neutral technical parameter — it is a judgment about risk. For a risk-free project (government bond), r is the risk-free rate. For a corporate project, r should reflect the risk of that specific project's cash flows: more volatile cash flows warrant a higher r because investors require a higher return to bear that risk. In corporate finance, r is typically the **weighted average cost of capital (WACC)** — a blend of the firm's cost of equity and cost of debt. But WACC applies to the average project, not to an unusually risky or unusually safe one. Using the wrong discount rate systematically accepts bad projects (too low r) or rejects good ones (too high r). Mastering NPV means mastering the judgment behind r, not just the arithmetic.
