---
id: investment-demand-and-interest-rates
title: Investment Demand and Interest Rates
domain: economics
course: macroeconomics
prerequisites:
- id: interest-rates-and-loanable-funds
  type: hard
- id: profit-maximization-microeconomics
  type: soft
- id: present-value-and-discounting
  type: hard
- id: investment-function-accelerator
  type: soft
builds-toward:
- tobin-q-theory-investment
- accelerator-principle-investment
- crowding-out-and-fiscal-effects
tags:
- investment
- interest-rates
- capital
stage: formal-systems
status: validated
---
# Investment Demand and Interest Rates

## Core Idea
Investment spending depends on the expected rate of return on capital relative to the cost of borrowing (the interest rate). Firms invest more when real interest rates are low and expected profits are high. The investment demand curve slopes downward: lower interest rates stimulate investment, increasing aggregate demand and output in the short run.

## Questions

```yaml
- question: "A firm is evaluating a machine that costs $100,000 today and will generate $12,000/year for 10 years. At an 8% interest rate the project is unprofitable; at 3% it becomes profitable. What does this illustrate about the role of interest rates in investment decisions?"
  type: multiple-choice
  options:
    - "Higher interest rates make future revenues larger in present-value terms, so projects become more attractive"
    - "The interest rate acts as a discount rate: it reduces the present value of future profits, making marginal projects viable or unviable depending on its level"
    - "Interest rates only matter if the firm is borrowing money; firms using retained earnings are unaffected"
    - "The decision depends only on the total undiscounted revenue ($120,000) versus cost ($100,000), which is always profitable regardless of rates"
  answer: 1
  explanation: "The interest rate is the discount rate that converts future earnings into present value. A higher rate shrinks the present value of the same income stream — a $12,000 annuity is worth less at 8% than at 3%. This is why investment demand slopes downward with respect to interest rates: many marginal projects are profitable at low rates and unprofitable at high rates. Option C is wrong because even firms using retained earnings face an opportunity cost — those funds could earn the market rate of return if lent out instead."

- question: "The interest rate enters investment decisions through two distinct channels. Which answer correctly identifies both?"
  type: multiple-choice
  options:
    - "It raises firm costs and it reduces consumer spending, both of which shrink investment"
    - "It acts as the discount rate on future profits AND as the opportunity cost of capital deployed in the project"
    - "It affects only the cost of debt financing; equity-financed firms are not affected by rate changes"
    - "It changes the expected level of future profits AND the current price of capital goods"
  answer: 1
  explanation: "The interest rate does double duty in investment analysis: (1) it is the discount rate that determines the present value of expected future revenues — a higher rate means future profits are worth less today; (2) it represents the opportunity cost of capital, since funds used to invest can't be lent at the prevailing rate. Both channels mean that higher interest rates depress investment. Option D is partially plausible but wrong: expected future profits are not determined by the interest rate, and capital goods prices are a separate input-cost variable."

- question: "Very low interest rates guarantee an increase in business investment spending because firms' borrowing costs are reduced."
  type: true-false
  answer: false
  explanation: "Low rates lower the cost of borrowing, but investment also depends on the expected rate of return — the numerator of the present-value calculation. If firms expect weak future demand, the projected revenue stream is small regardless of the discount rate, and investment remains depressed. This is the 'pushing on a string' problem: expansionary monetary policy can fail when pessimistic profit expectations dominate. Low rates are necessary but not sufficient for investment recovery, which is why fiscal policy (which directly affects aggregate demand and expected revenues) is sometimes needed when monetary policy alone is ineffective."

- question: "An investment tax credit that reduces the effective cost of capital goods shifts the investment demand curve rightward, meaning more investment occurs at every interest rate level."
  type: true-false
  answer: true
  explanation: "The investment demand curve shifts when the expected rate of return changes independently of the interest rate. A tax credit lowers the effective cost of capital — the same machine now requires less after-tax outlay — which raises the net present value of any given investment project. This makes projects that were marginally unprofitable now profitable, increasing investment at every interest rate. The curve shifts right. This is distinct from a movement along the curve (which is caused by an interest rate change), and it's why tax policy can stimulate investment even when the central bank has already lowered rates."

- question: "Why is investment spending said to be especially sensitive to interest rate changes compared to, say, consumption spending? Explain the mechanism."
  type: short-answer
  answer: "Investment is especially sensitive because the interest rate affects it through two compounding channels simultaneously: it acts as the discount rate that converts future profits into present value, AND as the opportunity cost of deploying capital. A small rate change can flip many marginal projects from unprofitable to profitable (or vice versa), because the rate applies to every year of a multi-year income stream. Consumption, by contrast, is mostly a function of current income and is affected by rates mainly through the wealth effect and borrowing costs on durable goods — a narrower and often weaker channel."
  explanation: "The double role of interest rates in investment — as discount rate and as opportunity cost — means a given rate change has amplified effect relative to its impact on consumption. Moreover, investment involves committing to long-duration projects, so the discount rate effect compounds over many years of future cash flows. The sensitivity is further amplified because many firms operate near the margin of profitability on investment projects, making the rate level a threshold variable that triggers or blocks large spending decisions."
```

## Explainer

You've studied present value and discounting, which gives you the essential tool for understanding investment decisions. When a firm considers investing — buying a machine, building a factory, or hiring workers to expand capacity — it is trading a certain cost today for an uncertain stream of future profits. The fundamental question is whether those future profits, discounted back to the present, exceed the upfront cost. The **interest rate** enters this calculation twice: as the discount rate that converts future profits into present value, and as the opportunity cost of capital (funds used for investment can't be lent at the prevailing rate). This double role is why investment is so sensitive to interest rate changes.

Think about a firm evaluating a machine that costs $100,000 today and will generate $12,000 per year in net revenue for ten years. At a 5% interest rate, the present value of that income stream is approximately $92,600 — less than the cost, so the investment is not worthwhile. At a 3% interest rate, the present value rises to approximately $102,200 — now the investment is marginally profitable. Small changes in the interest rate flip the investment decision. Aggregate across thousands of firms considering similar marginal projects, and you get the **investment demand curve**: a downward-sloping relationship between the real interest rate and the total quantity of investment spending in the economy. When the central bank lowers interest rates, it simultaneously makes existing investment projects profitable and pulls new projects above the threshold.

This link between interest rates and investment is the primary transmission channel through which monetary policy affects the real economy. When the central bank raises rates to fight inflation, it raises the discount rate on future profits and the cost of borrowing — investment falls, aggregate demand contracts, and eventually output and inflation cool. The channel works in reverse when rates are cut to stimulate activity. This is also why **business confidence and profit expectations** matter so much: the numerator of the investment calculation is expected future profits. Even very low interest rates won't stimulate much investment if firms expect demand to be weak. This is the foundation of the "pushing on a string" problem — expansionary monetary policy can fail if pessimistic expectations dominate.

The investment demand curve shifts when anything changes expected returns independently of the interest rate. Technological progress that raises the productivity of capital shifts the curve right — each machine now generates more revenue, so investment is worthwhile at higher interest rates than before. Tax policy matters directly: an investment tax credit effectively lowers the cost of capital, while accelerated depreciation allows firms to deduct the cost of investment faster, raising the present value of the tax savings. Business cycle dynamics create an important amplification mechanism: when demand is strong, firms invest more to expand capacity, which raises income and demand further. This is the **accelerator principle** — investment responds not just to the level of output but to changes in output — which you'll explore in subsequent topics.
