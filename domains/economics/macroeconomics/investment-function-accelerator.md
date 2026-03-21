---
id: investment-function-accelerator
title: The Investment Function and Accelerator Principle
domain: economics
course: macroeconomics
prerequisites:
- id: gdp-components
  type: soft
builds-toward:
- investment-demand-interest-sensitivity
- business-cycles
tags:
- investment
- accelerator
- capital
- dynamics
stage: abstract-reasoning
status: draft
---

# The Investment Function and Accelerator Principle

## Core Idea
The accelerator principle states that investment depends on the rate of change of output, not the level. Growing economies need more capital; slowing economies disinvest even if output remains positive.

## How It's Best Learned
Use numerical examples: if firms maintain capital-to-output ratio of 2:1 and output grows 10% in year 1, they need 10% more capital. If growth slows to 5% in year 2, investment falls despite rising output.

## Common Misconceptions
- Assuming investment responds only to output levels.
- Forgetting accelerator works in reverse.
- Treating accelerator as deterministic.

## Questions

```yaml
- question: "In Year 1, an economy's output grows from $100 to $110. In Year 2, output grows from $110 to $118. Firms maintain a capital-to-output ratio of 2. According to the accelerator principle, what happens to investment in Year 2 compared to Year 1?"
  type: multiple-choice
  options:
    - "Investment rises, because output is higher in Year 2 than Year 1"
    - "Investment stays the same, because the capital-to-output ratio has not changed"
    - "Investment falls, because the rate of output growth slowed from $10 to $8"
    - "Investment rises, because the economy is still expanding and needs more capital"
  answer: 2
  explanation: "Year 1 output grew by $10, requiring $20 in new capital (2×$10). Year 2 output grew by only $8, requiring only $16 in new capital (2×$8). Investment fell by $4 even though output is still rising. This is the core of the accelerator: investment responds to the rate of change of output, not the level. A deceleration in growth — not a recession — is sufficient to cause investment to fall."

- question: "Why does a mere slowdown in GDP growth — not an actual decline in output — cause investment spending to fall sharply?"
  type: multiple-choice
  options:
    - "When growth slows, interest rates rise automatically, making borrowing for capital more expensive"
    - "Investment expands the capital stock to meet growing demand; if output grows more slowly, the required addition to capital stock shrinks, so firms invest less"
    - "Firms interpret slower growth as evidence of lower future profits and preemptively cut all capital spending"
    - "Slower growth reduces consumer confidence, which directly causes firms to reduce their investment plans"
  answer: 1
  explanation: "The mechanism is purely about the desired capital stock. Firms target a fixed ratio of capital to output. When output grows by $10, they need $20 more capital (at a 2:1 ratio). When output grows by only $5, they need only $10 more capital. Investment spending is the rate at which the capital stock is being added to — so if the desired addition shrinks, investment shrinks, even though output is still positive and growing. No interest rate change or confidence shock is required."

- question: "According to the accelerator principle, investment can fall even while output is still rising, if the rate of output growth decelerates."
  type: true-false
  answer: true
  explanation: "This is the key non-intuitive result of the accelerator. Because investment tracks the change in output (not the level), any slowdown in the pace of growth reduces the gap between current and desired capital stock, reducing the need for new investment. A mere deceleration — from 10% growth to 5% growth, for instance — cuts investment in half under a simple accelerator model, even though the economy is still expanding."

- question: "An economy experiencing positive GDP growth will necessarily see rising business investment, since firms need more capital to meet growing demand."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about the accelerator. Investment depends on the rate of change of output, not the level. If output is growing at 8% this year versus 12% last year, firms need less additional capital than last year — so investment falls despite positive growth. The economy is still expanding, but at a slower rate, and that slowdown is enough to push investment down."

- question: "In your own words, explain why the accelerator principle makes investment the most volatile component of GDP and helps drive business cycles."
  type: short-answer
  answer: "Investment depends on the rate of change of output — so small fluctuations in the growth rate produce large swings in investment. If growth merely slows (but remains positive), investment can collapse, reducing aggregate demand, which slows growth further, which reduces investment further. This self-reinforcing dynamic amplifies small economic fluctuations into larger cycles. A slowdown becomes a potential recession not because of any single shock, but because the accelerator turns a deceleration in growth into a sharp drop in investment."
  explanation: "The amplification effect is the macroeconomic punchline. Investment is volatile because it responds to the second derivative of output, not the first. Even small changes in the growth rate ripple into large changes in investment, which then feed back into aggregate demand and output, deepening the cycle in both directions."
```

## Explainer

From your study of GDP components you know that investment is one of the most volatile components of aggregate expenditure. The **accelerator principle** explains why: investment is not driven by the level of output but by the *change* in output. This distinction is counterintuitive at first but becomes clear once you think about what investment is actually for — it is the act of expanding the capital stock to meet demand. If demand is not growing, there is no need to add capital.

Here is the core logic. Suppose firms maintain a target **capital-to-output ratio** — say, $2 of capital for every $1 of annual output (a ratio of 2). If output is $100, the desired capital stock is $200. If output rises to $110, the desired capital stock rises to $220. Firms must invest $20 to close the gap. Notice: investment of $20 is 20% of the *change* in output ($10), not of the output level itself. In the next year, if output grows again to $125, desired capital rises to $250, requiring $30 more investment. Investment rose because the *rate of growth* of output rose. Now suppose growth slows: output rises from $125 to $130. Desired capital goes from $250 to $260 — firms still invest, but only $10. Output is still rising, but investment *fell* because the pace of growth decelerated. This is the accelerator in action.

The amplification effect is the macroeconomic punchline. Because investment responds to the *rate of change* of output, small fluctuations in the growth rate of GDP produce large swings in investment. A mere slowdown (not a recession) is enough to cause investment to fall sharply, which then reduces aggregate demand further, which can slow growth even more. This creates the self-reinforcing dynamic that makes investment the most volatile component of GDP and a key driver of business cycles. The accelerator is one explanation for why downturns can deepen quickly: as soon as growth decelerates, investment collapses, amplifying the slowdown into a potential recession.

The accelerator principle also works in reverse and has important caveats in practice. During a recovery, as output growth picks up, the desired capital stock expands rapidly, triggering a surge in investment that can overshoot. In reality, the accelerator is a tendency rather than a mechanical law: firms face financing constraints, adjustment costs, and uncertainty about whether demand growth is permanent or temporary. They therefore smooth their investment rather than instantly closing the gap to the desired capital stock. These frictions are captured in more elaborate **flexible accelerator** models, where the adjustment to desired capital stock is partial each period. But the basic insight — that investment is inherently tied to the second derivative of output, not the level — is one of the most important dynamics in macroeconomics.
