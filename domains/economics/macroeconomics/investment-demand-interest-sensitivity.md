---
id: investment-demand-interest-sensitivity
title: Investment Demand and Interest Rate Sensitivity
domain: economics
course: macroeconomics
prerequisites:
- id: real-vs-nominal-gdp
  type: soft
- id: net-present-value
  type: soft
builds-toward:
- is-lm-model
tags:
- investment
- interest-rates
- capital-formation
- user-cost
stage: abstract-reasoning
status: draft
---

# Investment Demand and Interest Rate Sensitivity

## Core Idea
Investment spending is inversely related to the real interest rate: higher rates raise the user cost of capital, lowering present value of future returns and discouraging capital formation.

## How It's Best Learned
Use project-based examples: evaluate a machine with expected returns at different real interest rates; as rates rise, NPV falls and project becomes unprofitable. Connect to aggregate investment.

## Common Misconceptions
- Confusing nominal and real interest rates.
- Assuming interest elasticity is stable.
- Overlooking the lag in monetary transmission.

## Explainer

From net present value, you know how to evaluate whether a project is worth undertaking: discount its expected future cash flows by a required rate of return, and invest if the NPV is positive. That same logic, applied to every firm in the economy simultaneously, generates the **investment demand** relationship. When the interest rate is the opportunity cost of capital, a change in rates shifts the NPV of every prospective project, changing which ones clear the investment hurdle and therefore how much aggregate investment occurs.

Consider a firm evaluating a machine that costs $100,000 today and generates $12,000 per year in profit for 10 years. At a 5% real interest rate, NPV is positive — the project earns more than its cost of capital, so the firm invests. At a 10% real interest rate, the same cash flows have a lower present value, and NPV may turn negative — the project no longer earns enough to justify the cost. Multiply this logic across millions of investment decisions, and the aggregate investment function I(r) is downward-sloping: lower real interest rates render more projects profitable, increasing total investment; higher rates make more projects unviable, reducing it.

The critical input is the **real** interest rate, not the nominal rate. What matters to a firm is the inflation-adjusted cost of borrowing — the purchasing power it gives up. If the nominal rate is 8% but inflation is 5%, the real rate is approximately 3%, and investment decisions should be based on that 3%. This is why monetary policy works through inflation expectations as well as nominal rate changes: the Federal Reserve can lower the real interest rate by raising inflation expectations even if it can't cut nominal rates further. Confusing nominal and real rates leads to systematically wrong predictions about investment behavior.

The investment demand curve is the microeconomic foundation of the IS curve in the IS-LM model — your next topic. In the IS curve, lower interest rates raise investment, which raises aggregate demand, which raises output. The slope of the IS curve depends directly on how sensitive investment is to interest rates: if investment is highly elastic (small rate changes generate large investment changes), the IS curve is relatively flat; if investment is inelastic — perhaps because firms are uncertain or face credit constraints — the IS curve is steep. This is why debates about "the effectiveness of monetary policy" often come down to empirical estimates of investment interest-rate sensitivity: a central bank that lowers rates to stimulate the economy needs investment to respond for the transmission mechanism to work.
