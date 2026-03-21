---
id: investment-and-capital-formation
title: Investment Demand and Capital Formation
domain: economics
course: macroeconomics
prerequisites:
- id: net-present-value
  type: hard
- id: capital-accumulation-steady-state
  type: soft
builds-toward:
- aggregate-demand
- demand-shocks-and-multipliers
tags:
- demand
- investment
- capital
stage: advanced
status: draft
---

# Investment Demand and Capital Formation

## Core Idea
Investment I depends on the expected present value of capital's future returns relative to its cost. A lower interest rate makes capital more valuable, increasing desired investment. Firms compare the marginal product of capital to the user cost of capital (which includes interest rates, depreciation, and taxes). Investment is more volatile than consumption because it is forward-looking and sensitive to expectations and interest rates.

## Questions

```yaml
- question: "The interest rate falls from 5% to 3%. How does this most directly affect investment spending?"
  type: multiple-choice
  options:
    - "Investment falls because lower interest rates signal a weak economy with poor profit prospects"
    - "Investment rises because the user cost of capital falls, making previously unprofitable projects viable and raising NPV of long-lived projects"
    - "Investment is unaffected because firms fund investment from retained earnings, not borrowing"
    - "Investment rises only temporarily until firms realize future demand has not actually changed"
  answer: 1
  explanation: "The user cost of capital includes the opportunity cost of deploying funds (the interest rate). A lower rate reduces this opportunity cost, making capital investment relatively more attractive. Additionally, lower discount rates raise the NPV of future cash flows from long-lived investments, turning marginal projects profitable. Option C is wrong — even internally-funded investment uses the interest rate as an opportunity cost (the firm could have put those retained earnings in bonds instead). This user-cost channel is monetary policy's primary transmission mechanism to real investment."

- question: "A firm is deciding whether to build a factory whose revenues will arrive over 20 years. A credible forecast revises expected demand upward by 10% starting in year 5. How should this most likely affect the investment decision?"
  type: multiple-choice
  options:
    - "It has no effect since the revision affects future years, not current profitability"
    - "It increases the NPV of the investment, making it more likely to proceed"
    - "It decreases investment because higher future demand means more competition entering later"
    - "It only matters if the firm can hedge the revenue stream against interest rate risk"
  answer: 1
  explanation: "Investment is a bet on future cash flows. A revision to expected future demand directly increases the NPV of the investment project — the same capital outlay today now produces a larger expected return stream. This illustrates why investment is 'forward-looking': current conditions matter less than the expected trajectory of future returns. This also explains the Keynesian insight about 'animal spirits' — a shift in expectations about future profitability can dramatically alter investment decisions even without any change in current fundamentals."

- question: "Because investment is a small share of GDP (roughly 15–20%), it contributes less to business cycle volatility than consumption does."
  type: true-false
  answer: false
  explanation: "Investment's small GDP share means its contribution to GDP levels is smaller than consumption, but volatility is about percentage swings, not levels. Investment can fall 20%+ during recessions while consumption falls only 2–3%. A 20% fall in a 15% GDP share (−3 percentage points of GDP) is a larger contribution to the GDP decline than a 3% fall in a 70% share (−2.1 percentage points). The 2008–2009 data illustrates this: US business fixed investment fell over 20% while consumer spending fell only 3%, yet investment's swings dominated the recession's depth."

- question: "If firms only cared about current-period profitability rather than expected future returns, investment would be less sensitive to interest rate changes."
  type: true-false
  answer: true
  explanation: "Discounting matters more when cash flows are concentrated in the future. Capital investment yields returns spread over many years; a change in the discount rate (interest rate) has an outsized effect on NPV when future returns are large. If firms only looked at the current period, the interest rate would matter only through current financing costs, not through discounting long future streams. It is precisely the long-run, forward-looking nature of investment that makes it interest-elastic and thus a key channel for monetary policy."

- question: "Explain why investment is more volatile than consumption over the business cycle, using the concept of expectations."
  type: short-answer
  answer: "Consumption is largely determined by current income and stable long-run income expectations — households smooth consumption over their lifetimes. Investment decisions, by contrast, require forecasting demand, input costs, competition, and the regulatory environment over 10–20 years. Small revisions to long-run expectations can flip the sign of an investment project's NPV, reversing large capital commitments. A 10% downgrade to expected future returns from a factory can make a previously attractive project unviable, causing investment to collapse even while current production is unchanged. Because expectations are inherently uncertain and can shift rapidly on news, investment is prone to discrete, large swings that consumption is not."
  explanation: "Keynes captured this with 'animal spirits' — investment can be driven by waves of optimism and pessimism not fully tethered to fundamentals. This forward-looking volatility explains why investment crashes sharply in recessions (firms become pessimistic about future demand) and recovers erratically in expansions (firms require sustained evidence before committing to long-lived projects). Rising interest rates during downturns further suppress investment through the user cost and NPV channels, amplifying the cycle."
```

## Explainer

From your study of net present value, you know how to evaluate whether a future stream of cash flows justifies a present outlay. Firms apply exactly this logic to capital investment. Buying a piece of equipment is worth it if the NPV of its expected future output exceeds its purchase price. The **marginal product of capital (MPK)** — the additional output produced by one more unit of capital — represents the benefit side. The **user cost of capital** represents the cost side: the opportunity cost of tying up funds in capital rather than earning the market return, plus the rate at which the capital depreciates, plus any taxes on capital income. The investment decision rule is simple: invest when MPK > user cost of capital, and stop when they are equal at the margin.

The interest rate enters through the user cost. When interest rates fall, the opportunity cost of deploying funds in capital drops, reducing the user cost. Some investment projects that were marginally unprofitable become viable. More fundamentally, the rate at which future cash flows are discounted falls, raising the NPV of long-lived investment projects. This is why investment spending is **interest-elastic**: it responds more strongly to interest rate changes than consumption does, because investment yields are concentrated in the future (discounting matters more) while consumption is largely a current-period decision. Monetary policy's primary transmission channel to the real economy runs through this relationship.

**Expectations** make investment far more volatile than consumption. A household deciding whether to buy groceries knows its current income with reasonable certainty. A firm deciding whether to build a new factory is betting on demand, input costs, competition, and the regulatory environment over the next 10–20 years. Small revisions to expected future profitability can reverse large capital investment decisions. Keynes famously described investment as driven by **animal spirits** — waves of optimism and pessimism that can shift investment dramatically without any change in "fundamentals." This forward-looking, expectation-sensitive character is why investment is the most volatile component of GDP, collapsing sharply in recessions and recovering erratically.

From your capital accumulation work, you know that investment drives long-run growth by expanding the capital stock. In the short run, investment fluctuations dominate business cycle dynamics because the investment-to-GDP ratio (roughly 15–20% of GDP) swings far more than consumption as a share of income. During the 2008–2009 recession, US business fixed investment fell over 20% while consumer spending fell only 3%. This asymmetry means investment demand shocks — driven by confidence, credit conditions, or expected future profitability — are a primary driver of aggregate demand fluctuations, and stabilizing investment expectations is one of the key channels through which monetary and fiscal policy aim to smooth economic cycles.
