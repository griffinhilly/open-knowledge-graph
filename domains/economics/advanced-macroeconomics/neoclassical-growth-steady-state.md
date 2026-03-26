---
id: neoclassical-growth-steady-state
title: Steady-State Growth and Balanced Growth Path
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: solow-growth-model
  type: hard
- id: constrained-optimization-lagrange
  type: soft
- id: systems-of-first-order-linear-odes
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- endogenous-growth-theory
- ramsey-cass-koopmans-model
tags:
- steady-state
- capital
- long-run-equilibrium
stage: expert
status: validated
---

# Steady-State Growth and Balanced Growth Path

## Core Idea
In neoclassical growth, economies converge to a steady state where capital stock is constant and output grows at the exogenous technology rate. Steady-state capital satisfies s·f(k*) = (δ + n + g)k*, where n is population growth and g is productivity growth.

## Questions

```yaml
- question: "A government implements policies that permanently raise the national savings rate from 20% to 30%. According to the neoclassical (Solow) growth model, what is the long-run effect?"
  type: multiple-choice
  options:
    - "Both the level and the growth rate of output per worker permanently increase"
    - "The level of output per worker rises to a new, higher steady state, but the long-run growth rate of output per worker remains g"
    - "There is no effect because the savings rate does not affect capital accumulation in the long run"
    - "Output per worker grows faster permanently because more investment means more capital every period"
  answer: 1
  explanation: "A higher savings rate shifts the investment curve upward, raising the steady-state capital per effective worker k* — so the level of output per worker permanently increases. However, once the economy converges to its new k*, capital per effective worker stops growing, and output per worker grows only at the exogenous technology rate g. The savings rate affects levels but not long-run growth rates. Option D describes the transitional dynamics (the economy grows faster than g temporarily while converging), but confuses the transition with the long-run rate."

- question: "Why does the neoclassical growth model guarantee that an economy below its steady-state capital stock will converge toward k* rather than oscillate or diverge?"
  type: multiple-choice
  options:
    - "The government enforces a savings rate that keeps investment constant regardless of capital"
    - "The production function's concavity (diminishing returns to capital) ensures that investment exceeds break-even when k < k*, and break-even exceeds investment when k > k*"
    - "Population growth automatically adjusts to keep capital per worker constant"
    - "The eigenvalues of the linearized system are positive, ensuring monotonic growth"
  answer: 1
  explanation: "Convergence follows directly from diminishing returns. When k < k*, the marginal product of capital is high, so the investment curve s·f(k) exceeds the break-even line (δ+n+g)k, and k rises. When k > k*, diminishing returns mean the marginal product has fallen; investment falls below break-even, and k falls back. The concavity of f(k) creates a stable crossing point. Linearizing around k* yields a negative eigenvalue — confirming local asymptotic stability. Option D has the sign wrong: a negative eigenvalue means stable convergence, not positive."

- question: "In the Solow model, a country that permanently increases its savings rate will eventually achieve a higher long-run growth rate of output per worker than a country with a lower savings rate."
  type: true-false
  answer: false
  explanation: "This is the Solow model's most counterintuitive — and most debated — result. The long-run growth rate of output per worker is pinned at g, the rate of exogenous technological progress, regardless of the savings rate. A higher savings rate raises the steady-state level of output per worker (a one-time level effect), but once the economy converges to its new k*, per-capita growth returns to g. Two countries with identical g but different savings rates will grow at the same long-run rate but with different income levels. Only endogenous growth models can escape this conclusion."

- question: "At the steady state k*, capital per effective worker is constant, even though total output Y and the capital stock K are both growing over time."
  type: true-false
  answer: true
  explanation: "This is the definition of the balanced growth path. 'Effective worker' means worker × technology level (A·L). Along the balanced growth path, technology A grows at rate g, population L grows at rate n, so effective labor A·L grows at rate n+g. Total capital K grows at the same rate n+g, keeping the ratio k = K/(A·L) constant. Output Y also grows at n+g for the same reason. The 'steady state' is not static — it is a constant ratio in rescaled units, while all levels grow."

- question: "Explain why the Solow model predicts that only exogenous technological progress can drive sustained per-capita output growth in the long run, and what role capital accumulation plays."
  type: short-answer
  answer: "Capital accumulation cannot sustain long-run per-capita growth because of diminishing returns: each additional unit of capital adds less output than the previous one. As capital accumulates, the marginal product of capital falls, and eventually the output gained from new investment just offsets depreciation and dilution from population growth — no net addition to k occurs. This is the steady state. Without technological progress (g = 0), per-capita output converges to a fixed level. Technological progress escapes this trap by continuously raising the productivity of each unit of capital and labor, shifting up the production function and allowing output per worker to grow indefinitely at rate g. Capital deepening can lift the level of output but cannot change the growth rate once the economy is near its steady state."
  explanation: "This result is the Solow model's central policy implication and its central controversy: if only technology drives long-run growth, and technology is exogenous, then standard policies affecting savings or investment cannot permanently raise growth rates. Endogenous growth theory, starting with Romer (1990), tried to make technological progress itself a function of investment in R&D and human capital."
```

## Questions

```yaml
- question: "Country A permanently raises its savings rate from 20% to 30% of GDP. According to the Solow model, what is the long-run effect on the growth rate of output per worker?"
  type: multiple-choice
  options:
    - "The growth rate permanently increases, because higher saving means faster capital accumulation indefinitely"
    - "The growth rate temporarily rises during the transition to the new steady state, but returns to the exogenous technology growth rate g in the long run"
    - "The growth rate permanently falls, because higher saving reduces consumption and thus aggregate demand"
    - "There is no effect at all — the savings rate has no influence on either growth or income levels"
  answer: 1
  explanation: "This is the Solow model's most important and counterintuitive prediction. A higher savings rate shifts the investment curve upward, raising k* and the level of output per worker — but not the long-run growth rate. During transition, the economy grows faster as it accumulates capital toward the new, higher k*. Once there, diminishing returns ensure that investment again exactly equals break-even investment, and growth returns to g. Only exogenous technological progress drives sustained per-capita growth. Students who answer A confuse a one-time level increase (moving to a higher k*) with a permanent change in the growth rate."

- question: "An economy is currently below its steady-state capital stock k*. What causes it to grow faster than its long-run balanced growth path rate during this period?"
  type: multiple-choice
  options:
    - "Higher saving — below-k* economies typically have higher savings rates, boosting investment"
    - "Diminishing returns working in reverse — when capital is scarce, its marginal product is high, so investment yields disproportionately large output gains"
    - "The exogenous technology growth rate g is higher when capital is scarce"
    - "Higher depreciation below k* reduces break-even investment, freeing resources for growth"
  answer: 1
  explanation: "The convergence mechanism is entirely due to the concavity of the production function. When k is low (below k*), the marginal product of capital is high — each unit of new capital adds a lot to output. Investment exceeds break-even, so k rises. As k approaches k*, diminishing returns reduce the marginal product until it exactly equals break-even investment. This is why conditional convergence — poorer countries growing faster than richer ones with similar fundamentals — is a testable prediction of the Solow model, and why it follows from diminishing returns rather than any change in savings behavior."

- question: "In the Solow model, a permanently higher savings rate raises the long-run steady-state level of output per worker but does not permanently raise the growth rate of output per worker."
  type: true-false
  answer: true
  explanation: "This is the central result of neoclassical growth theory. The savings rate determines k* (and thus the level of output per effective worker at steady state) but not the growth rate along the balanced growth path. Once the economy reaches k*, the growth rate of output per worker is g — the exogenous rate of technological progress — regardless of the savings rate. Policy can affect whether an economy is richer or poorer in steady state, but only technological progress can sustain permanently rising living standards."

- question: "An economy that has accumulated more capital than k* (its steady-state capital stock) will continue to grow faster than the balanced growth path rate as it adjusts."
  type: true-false
  answer: false
  explanation: "When k > k*, break-even investment (δ + n + g)k exceeds actual investment s·f(k) because diminishing returns have made capital less productive. The capital stock per effective worker is *falling*, not rising — the economy is decumulating capital back toward k*. Growth in output per worker is therefore *below* the balanced growth path rate, not above it. The steady state is a two-sided attractor: economies below k* grow faster than g (converging upward), and economies above k* grow slower than g (converging downward)."

- question: "Why does the Solow model predict that only technological progress can sustain long-run growth in output per worker, while a permanently higher savings rate cannot?"
  type: short-answer
  answer: "The answer lies in diminishing returns to capital. As the capital stock per effective worker rises, each additional unit of capital produces less additional output. Eventually, the output gain from new investment exactly equals the break-even investment needed to maintain the capital stock (replacing depreciation and equipping new workers and new-technology-efficiency units). From that point, additional saving cannot raise growth — it only maintains the capital stock at k*. Technological progress, by contrast, shifts the production function upward continuously, meaning each unit of capital at any stock level now produces more output than before. This prevents the marginal product from falling to break-even permanently, sustaining growth in output per worker indefinitely at rate g."
  explanation: "Students who say 'diminishing returns' without explaining why technological progress escapes them are only halfway there. The key is that technological progress shifts the production function itself — it's not capital deepening but capital-augmenting efficiency growth, which changes the level at which diminishing returns bite."
```

## Explainer

From the Solow growth model, you already know the fundamental equation of capital accumulation: the change in capital per effective worker equals investment minus break-even investment, or Δk = s·f(k) − (δ + n + g)k. The **steady state** is the point where these two forces exactly balance — where new investment precisely replaces the capital that is lost to depreciation (δ), diluted by population growth (n), and rendered less significant by technological progress (g). At this point, k* is constant, and the economy settles into a **balanced growth path** where output per worker grows at rate g and total output grows at rate n + g.

The steady state is not just a theoretical convenience — it is an **attractor**. To see why, consider what happens away from k*. If k < k* (the economy has less capital than its steady-state level), then s·f(k) > (δ + n + g)k — investment exceeds break-even, so capital per effective worker is rising. The economy grows faster than its long-run rate as it accumulates capital. Conversely, if k > k* (perhaps due to a temporary investment boom), break-even investment exceeds actual investment, and k falls back toward k*. This convergence is guaranteed by the **concavity of the production function** — diminishing returns to capital mean that the marginal product of capital is high when capital is scarce and low when capital is abundant. From your knowledge of differential equations and eigenvalue analysis, you can formalize this: linearizing around k*, the system has a negative eigenvalue, confirming local stability.

The steady-state condition s·f(k*) = (δ + n + g)k* reveals what determines long-run living standards. A higher savings rate s shifts the investment curve upward, raising k* and output per effective worker — but with diminishing returns, each successive increase in s buys less additional output. Higher population growth n or depreciation δ raises the break-even investment line, lowering k*. Crucially, the long-run **growth rate** of output per worker is pinned at g regardless of s, n, or δ. This is the Solow model's most striking — and controversial — prediction: policy can affect the **level** of income but not its **growth rate** in the long run. Only exogenous technological progress drives sustained per-capita growth.

The **balanced growth path** is the steady state expressed in levels rather than ratios. Along this path, output Y grows at rate n + g, capital K grows at rate n + g (maintaining a constant capital-output ratio), consumption C grows at rate n + g, and real wages grow at rate g while the interest rate (marginal product of capital) is constant. These "Kaldor facts" — constant capital-output ratio, constant factor shares, steady growth in output per worker — broadly match long-run data for developed economies, which is a key reason the neoclassical framework remains central to growth economics. The steady state also provides the baseline against which richer models — with optimizing savings (Ramsey), human capital, or endogenous innovation — are constructed and evaluated.
