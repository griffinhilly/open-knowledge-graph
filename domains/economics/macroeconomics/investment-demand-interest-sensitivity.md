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
stage: formal-systems
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

## Questions

```yaml
- question: "A central bank raises the nominal interest rate from 5% to 8%. During the same period, inflation rises from 3% to 6%. What is the likely effect on business investment?"
  type: multiple-choice
  options:
    - "Approximately no change, since the real interest rate is unchanged at roughly 2%"
    - "Investment falls significantly, because the nominal interest rate rose by 3 percentage points"
    - "Investment rises, because higher inflation increases the nominal return on capital"
    - "Investment falls initially, then recovers as firms adjust their inflation expectations"
  answer: 0
  explanation: "Investment responds to the real interest rate, not the nominal rate. Real rate ≈ nominal − inflation: initially 5% − 3% = 2%, and after the change 8% − 6% = 2%. Since the real cost of capital is unchanged, the NPV calculation for any given project is unchanged, and aggregate investment demand should not shift. The misconception is to focus on the 3 pp nominal increase, which overstates the tightening. When nominal rate hikes are matched by equal inflation increases, monetary policy is not actually tighter in real terms."

- question: "A firm evaluates a $500,000 equipment investment. At a 4% real interest rate the NPV is slightly positive; at a 7% real interest rate the NPV is negative. This illustrates:"
  type: multiple-choice
  options:
    - "Why the investment demand curve slopes downward — higher real rates reduce the present value of future returns, making marginal projects unprofitable"
    - "That investment is perfectly inelastic with respect to interest rates"
    - "The accelerator principle — investment follows changes in output, not interest rates"
    - "Why monetary policy is ineffective — firms are insensitive to small rate changes"
  answer: 0
  explanation: "This is the microeconomic foundation of downward-sloping investment demand. At 4%, the project's discounted future returns exceed its cost — NPV > 0, invest. At 7%, the same cash flows are discounted more heavily — NPV < 0, don't invest. Every project in the economy faces this same recalculation when rates change. Aggregate investment is the sum of all projects with positive NPV; as rates rise, fewer clear the hurdle and total investment falls. This is also why the IS curve in IS-LM slopes downward."

- question: "A fall in nominal interest rates will always stimulate investment in an economy."
  type: true-false
  answer: false
  explanation: "Investment responds to the real interest rate, not the nominal rate. A fall in nominal rates does not stimulate investment if inflation falls by the same amount — the real rate is unchanged, so NPV calculations are unaffected. For example, if the nominal rate falls from 5% to 3% but inflation falls from 4% to 2%, the real rate remains at 1% and investment demand is unchanged. The Fisher equation (real rate ≈ nominal − inflation) is the relevant input. This is why central banks must manage inflation expectations alongside nominal rates."

- question: "The slope of the IS curve in the IS-LM model depends on how sensitive investment is to changes in the real interest rate — a more interest-elastic investment schedule produces a flatter IS curve."
  type: true-false
  answer: true
  explanation: "The IS curve traces equilibrium output at each interest rate. Lower rates → higher investment → higher aggregate demand → higher output. The size of the output increase depends on how much investment changes when rates fall. If investment is highly elastic (many marginal projects waiting at the threshold), even small rate cuts generate large investment and output increases — a flat IS curve. If investment is inelastic (due to uncertainty or credit constraints), rate changes have small effects — a steep IS curve. This is why estimating investment interest-rate sensitivity is central to evaluating monetary policy effectiveness."

- question: "Why does the investment demand function depend on the real interest rate rather than the nominal interest rate? Use the concept of net present value to explain."
  type: short-answer
  answer: "A firm invests if the NPV of future cash flows — discounted at the cost of capital — is positive. If both revenues and borrowing costs rise with inflation at the same rate, the inflation components cancel out, and what matters is the inflation-adjusted (real) cost of capital. A project returning $110 next year when inflation is 10% offers the same real return as one returning $100 with zero inflation. Using the nominal rate to discount real cash flows overstates the true cost when inflation is positive. The real rate correctly measures the purchasing power given up by investing."
  explanation: "The Fisher equation formalizes this: real rate ≈ nominal rate − inflation. A firm borrowing at 10% nominal when inflation is 8% has a real borrowing cost of ~2% — identical to borrowing at 2% nominal with zero inflation. NPV calculations using nominal rates on nominal cash flows, or real rates on real cash flows, yield identical results; mixing them produces errors. The policy implication is that central banks can stimulate investment by cutting nominal rates or by raising inflation expectations — both lower the real rate. This is why quantitative easing can stimulate investment even when nominal rates are near zero."
```

## Explainer

From net present value, you know how to evaluate whether a project is worth undertaking: discount its expected future cash flows by a required rate of return, and invest if the NPV is positive. That same logic, applied to every firm in the economy simultaneously, generates the **investment demand** relationship. When the interest rate is the opportunity cost of capital, a change in rates shifts the NPV of every prospective project, changing which ones clear the investment hurdle and therefore how much aggregate investment occurs.

Consider a firm evaluating a machine that costs $100,000 today and generates $12,000 per year in profit for 10 years. At a 5% real interest rate, NPV is positive — the project earns more than its cost of capital, so the firm invests. At a 10% real interest rate, the same cash flows have a lower present value, and NPV may turn negative — the project no longer earns enough to justify the cost. Multiply this logic across millions of investment decisions, and the aggregate investment function I(r) is downward-sloping: lower real interest rates render more projects profitable, increasing total investment; higher rates make more projects unviable, reducing it.

The critical input is the **real** interest rate, not the nominal rate. What matters to a firm is the inflation-adjusted cost of borrowing — the purchasing power it gives up. If the nominal rate is 8% but inflation is 5%, the real rate is approximately 3%, and investment decisions should be based on that 3%. This is why monetary policy works through inflation expectations as well as nominal rate changes: the Federal Reserve can lower the real interest rate by raising inflation expectations even if it can't cut nominal rates further. Confusing nominal and real rates leads to systematically wrong predictions about investment behavior.

The investment demand curve is the microeconomic foundation of the IS curve in the IS-LM model — your next topic. In the IS curve, lower interest rates raise investment, which raises aggregate demand, which raises output. The slope of the IS curve depends directly on how sensitive investment is to interest rates: if investment is highly elastic (small rate changes generate large investment changes), the IS curve is relatively flat; if investment is inelastic — perhaps because firms are uncertain or face credit constraints — the IS curve is steep. This is why debates about "the effectiveness of monetary policy" often come down to empirical estimates of investment interest-rate sensitivity: a central bank that lowers rates to stimulate the economy needs investment to respond for the transmission mechanism to work.
