---
id: ak-growth-model-capital-accumulation
title: AK Model and Linear Production Functions
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: endogenous-growth-theory
  type: hard
tags:
- ak-model
- constant-returns-to-capital
- scale-effects
stage: expert
status: draft
---

# AK Model and Linear Production Functions

## Core Idea
The AK model assumes a linear production function Y = A·K with constant returns to capital and no diminishing returns. This generates perpetual growth: if agents save a constant fraction of output, capital and consumption grow at a constant rate indefinitely without requiring exogenous technological progress.

## Questions

```yaml
- question: "In the AK model, a government policy permanently raises the national savings rate. What is the long-run effect on the growth rate of output per worker?"
  type: multiple-choice
  options:
    - "No effect on the growth rate — savings rates only affect the level of income, not the long-run growth rate"
    - "A temporary increase in the growth rate until the economy converges to a new steady state"
    - "A permanent increase in the growth rate, because higher savings translates directly into faster capital accumulation indefinitely"
    - "A permanent decrease in the growth rate, because higher savings crowds out consumption and reduces aggregate demand"
  answer: 2
  explanation: "In the AK model, the growth rate equals sA − δ, so a permanent increase in s raises the growth rate permanently. This is the sharpest contrast with the Solow model (option A), where saving affects only the *level* of income in the long run — the growth rate returns to zero (or the exogenous technology growth rate). The AK model breaks this result by eliminating diminishing returns, so each saved unit of output generates the same return as the last, sustaining constant growth indefinitely."

- question: "Which of the following is the minimum theoretical ingredient required for endogenous sustained growth in the AK framework?"
  type: multiple-choice
  options:
    - "Exogenous technological progress that increases productivity over time"
    - "Constant or non-diminishing returns to the accumulable factor (capital)"
    - "A sufficiently high initial capital stock that crosses a threshold"
    - "Government intervention to correct market failures in R&D"
  answer: 1
  explanation: "The AK insight is purely structural: as long as the marginal product of capital does not fall toward zero as capital accumulates, growth can be self-sustaining. Exogenous technological progress (option A) is exactly what the model dispenses with — it shows you don't need it if returns are constant. The other options add mechanisms not required by the basic logic. The AK model demonstrates the minimum condition: no diminishing returns to K."

- question: "In the AK model, countries with permanently different savings rates will have permanently different growth rates."
  type: true-false
  answer: true
  explanation: "With growth rate = sA − δ, any permanent difference in s (savings rate) or A (productivity) translates into a permanent difference in growth rates. This implies no convergence between rich and poor countries — a sharp contrast with the Solow model, where all countries converge to the same steady-state growth rate regardless of initial conditions or savings rates. Whether this prediction matches the data is debated, but it follows directly from the model's structure."

- question: "The AK model predicts that poor countries will eventually catch up to rich ones because continued capital accumulation will eventually face diminishing returns."
  type: true-false
  answer: false
  explanation: "The AK model specifically assumes away diminishing returns — the production function Y = AK is linear in K, so the marginal product of capital is the constant A at all levels of K. There is no convergence mechanism. Poorer countries grow at exactly the same rate as richer ones if they share the same s and A, and countries with lower s or A grow more slowly forever. The convergence prediction belongs to the Solow model, not the AK model."

- question: "Why does the Solow model predict that long-run growth per worker eventually stops (absent exogenous technology), while the AK model does not?"
  type: short-answer
  answer: "The Solow model has a diminishing marginal product of capital: each additional unit of capital adds less output than the last. As capital accumulates, the extra output from saving falls until it just covers depreciation — at that point, net investment is zero and growth stops. The AK model assumes the marginal product of capital is constant (equal to A), so no matter how much capital accumulates, each additional unit still generates the same additional output. Investment never stops being productive enough to outpace depreciation, so growth continues indefinitely at rate sA − δ."
  explanation: "This is the core intuition of endogenous growth theory. The Solow model's diminishing returns create a gravitational pull back to zero growth. The AK model's linearity breaks that pull. Economically, the constant A can be justified by interpreting K broadly to include human capital, knowledge, and institutional capacity — factors that may not exhibit diminishing returns at the aggregate level even if physical capital alone does."
```

## Explainer

The Solow model, which you encountered earlier in your study of endogenous growth theory's motivations, has a famous limitation: long-run growth in output per worker eventually stops unless technology improves exogenously. The reason is **diminishing returns to capital** — each additional unit of capital produces less additional output than the last. As an economy accumulates more machines, factories, and infrastructure, the marginal product of capital falls, investment just barely covers depreciation, and growth grinds to a halt. The AK model asks: what if diminishing returns never set in?

The **AK production function** is strikingly simple: Y = A·K, where A is a positive constant representing productivity and K is the broad capital stock. Output is directly proportional to capital with no diminishing returns — double the capital and you exactly double output. This linearity is the model's defining feature. The "A" captures not just physical productivity but also human capital, knowledge, and organizational capacity embedded in the capital stock. Under this interpretation, K is not just machines but the entire stock of productive assets including education, R&D, and institutional capacity. Because these forms of capital generate positive externalities (a more educated workforce raises everyone's productivity), the aggregate production function can exhibit constant returns to capital even if individual firms face diminishing returns.

The growth implications are dramatic. With a constant savings rate *s* and depreciation rate *δ*, the growth rate of capital (and therefore output) is simply *sA − δ*. As long as *sA > δ* — as long as the return to saving exceeds what depreciation destroys — the economy grows at a constant, positive rate forever. There is no convergence to a steady state, no need for exogenous technological progress, and no prediction that poor countries will catch up to rich ones. The growth rate depends on the savings rate and the productivity parameter, both of which can differ permanently across countries. This is a sharp contrast with the Solow model, where the savings rate affects the *level* of income but not the long-run growth rate.

The AK model is powerful because it demonstrates the minimum theoretical ingredient needed for endogenous growth: eliminate diminishing returns to the accumulable factor. But this simplicity is also its weakness. The model predicts that countries with higher savings rates grow permanently faster — an extreme prediction that fits some cross-country data but not all. It also lacks a mechanism for explaining *why* A differs across countries or how policy might change it. More sophisticated endogenous growth models (Romer, Lucas) build on the AK insight by modeling the micro-foundations of knowledge creation and human capital accumulation explicitly. The AK model remains valuable as the cleanest illustration of the core logic: sustained growth requires that the engine of accumulation never runs into diminishing returns.
