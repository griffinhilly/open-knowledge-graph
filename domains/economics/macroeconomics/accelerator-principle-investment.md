---
id: accelerator-principle-investment
title: The Accelerator Principle
domain: economics
course: macroeconomics
prerequisites:
- id: investment-demand-and-interest-rates
  type: hard
- id: business-cycles
  type: soft
builds-toward:
- business-cycles
tags:
- investment
- output
- acceleration
stage: formal-systems
status: draft
---

# The Accelerator Principle

## Core Idea
The accelerator principle states that investment depends on the change in output, not the level of output. Firms expand their capital stock when demand is rising (accelerating), but cut investment sharply during slowdowns. This creates an amplification mechanism: a small deceleration in output growth triggers a large drop in investment, magnifying the downturn.

## Questions

```yaml
- question: "A firm maintains a capital-output ratio of 4. Last year output grew from $200M to $220M. This year output grows from $220M to $228M. What happens to the firm's gross investment this year compared to last year?"
  type: multiple-choice
  options:
    - "It stays the same — output is still growing, so investment continues at the same rate"
    - "It increases — the higher output level requires more total capital stock"
    - "It falls — slower output growth means less new capital is needed, even though output is still rising"
    - "It falls to zero — investment only occurs when output growth is accelerating"
  answer: 2
  explanation: "Last year: ΔY = $20M, so new investment = 4 × $20M = $80M. This year: ΔY = $8M, so new investment = 4 × $8M = $32M. Investment fell by 60% even though output is still growing — it just grew more slowly. The accelerator formula I = v·ΔY makes this mechanical: investment tracks the *change* in output, not the level. A deceleration (smaller positive ΔY) directly reduces investment even when output and output level are both rising."

- question: "GDP growth slows from 4% to 2% — output is still rising, just less quickly. According to the accelerator principle, what happens to business investment in new capital?"
  type: multiple-choice
  options:
    - "Investment grows at 2% — it tracks the growth rate of output"
    - "Investment falls sharply — it depends on ΔY, so halving the growth rate roughly halves new capital spending needed above replacement"
    - "Investment is unaffected — the accelerator only responds to output actually falling, not slowing"
    - "Investment rises — firms rush to build capacity before the anticipated further slowdown"
  answer: 1
  explanation: "The accelerator predicts I ∝ ΔY. If output growth halves (same capital-output ratio), desired new capital roughly halves. Note this can mean a 50%+ fall in net investment even though the economy is still expanding. This is the amplification mechanism: modest output fluctuations translate into violent investment swings. Recessions often begin not with output falling but with growth slowing — and investment collapses in response, reducing aggregate demand further, which is the self-reinforcing cycle the multiplier-accelerator model captures."

- question: "According to the accelerator principle, a firm will increase its investment whenever its output level is high relative to competitors."
  type: true-false
  answer: false
  explanation: "The accelerator principle says investment depends on the *change* in output (ΔY), not the *level*. A firm with high but stable output already possesses the capital stock it needs to serve current demand; desired net investment is zero (only replacement for depreciation continues). New investment is triggered by rising output — when the firm needs to expand its capital stock to serve growing demand. A firm with high, stable output has no accelerator-driven incentive to invest more."

- question: "The accelerator principle predicts that investment will be substantially more volatile over the business cycle than output itself."
  type: true-false
  answer: true
  explanation: "Because investment I = v·ΔY depends on changes in output, and output changes are modest fractions of GDP, even small percentage swings in output produce large percentage swings in investment. In the numerical example from the Explainer, a 50% reduction in the output growth rate cut investment by 60%. Real-world data confirms this: GDP fluctuations of 2-4% accompany investment swings of 20-30%. Investment in machinery, equipment, and structures is consistently the most cyclically volatile major component of GDP."

- question: "A factory's output holds perfectly flat for two consecutive years. According to the accelerator principle, what happens to its investment in new capacity, and why?"
  type: short-answer
  answer: "Net investment in new capacity falls to zero. The accelerator formula gives I = v·ΔY = v·0 = 0 when output is flat. The factory already has the capital stock it needs to produce at its current level; since demand is not growing, no additional capacity is required. Only replacement investment (to offset depreciation on the existing capital stock) continues. This illustrates the principle's key implication: even a plateau — not a decline, just stable output — causes new investment to collapse. Firms add capital only when they expect to need more of it."
  explanation: "The policy implication is significant: policymakers who want to stimulate investment cannot simply keep output high; they must ensure output is rising. A stabilized economy at a high level generates no accelerator-driven investment. This is why recovery from recessions often requires sustained GDP growth — not just a return to pre-recession levels — to reignite capital spending."
```

## Explainer

From your study of investment demand, you know that investment is the flow of spending that adds to the capital stock. The accelerator principle provides the key insight into *why* firms invest: not because output is high, but because output is *growing*. The logic comes from a simple relationship — firms want to hold a capital stock roughly proportional to their output (to serve demand). If desired capital is K* = v·Y (where v is the capital-output ratio), then desired investment is the change in the capital stock: I = v·ΔY. Output growth requires new capital; stable output requires only replacement investment (to offset depreciation); and declining output means the existing capital stock is already more than sufficient, so firms cut new investment to near zero.

A numerical example makes the amplification vivid. Suppose a firm wants a capital-output ratio of 3 — $3 of capital to produce $1 of output per year. If output grows from $100 to $110, the firm needs $30 of new capital (to go from $300 to $330). This requires $30 of gross investment (plus depreciation). Now output slows from $110 to $115 — growth continues, but at half the previous rate. Desired capital rises from $330 to $345, requiring only $15 of new investment. Investment falls by half even though output is still rising. If output merely holds flat at $115, desired investment falls to zero (plus replacement only). A plateau in output growth — not a recession, just a slowdown — causes investment to collapse.

This is the **acceleration effect**: investment is highly volatile relative to output because it responds to the *change* in output, which is itself volatile. Business cycle fluctuations in GDP are modest (a few percent), but investment swings of 20–30% are common because the acceleration mechanism magnifies small output changes into large investment changes. Your prior study of business cycles is relevant here: the accelerator is one of the key internal propagation mechanisms that makes downturns self-reinforcing. When output slows, investment falls; the fall in investment reduces aggregate demand further, slowing output more; which further reduces investment. This **multiplier-accelerator interaction** (combined with the Keynesian multiplier that amplifies spending changes into output changes) was the basis for the first mathematical models of endogenous business cycles developed by Harrod, Samuelson, and Hicks in the 1930s–1950s.

The accelerator also explains why investment in long-lived capital goods — machinery, buildings, software — is the most cyclically volatile component of GDP. Consumer spending on non-durables is relatively stable because consumption tracks income. But firms facing uncertain demand become very cautious about locking in new capital commitments during downturns, since unused capital is costly and lumpy investments are hard to reverse. This **irreversibility** makes the accelerator asymmetric in practice: firms are quick to cut investment when growth slows, but cautious about ramping it back up until they are confident the recovery is sustained.
