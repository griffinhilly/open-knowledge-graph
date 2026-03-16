---
id: golden-rule-capital-accumulation
title: Golden Rule of Capital Accumulation
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: steady-state-analysis-growth
  type: hard
- id: solow-growth-model
  type: soft
- id: constrained-optimization-lagrange
  type: soft
tags:
- welfare
- capital-stock
- consumption-optimization
stage: advanced
status: draft
---

# Golden Rule of Capital Accumulation

## Core Idea
The golden rule determines the optimal steady-state capital stock that maximizes consumption per capita—a normative benchmark for welfare maximization. At the golden-rule level, the marginal product of capital exactly equals the depreciation rate, balancing capital's productivity benefit against the consumption cost of forgone output. Most developed economies accumulate capital beyond the golden-rule level, implying they could increase steady-state consumption by reducing capital investment.

## Explainer

From your study of steady-state analysis in the Solow growth model, you know that the economy converges to a long-run equilibrium where capital per worker, output per worker, and consumption per worker are all constant. The steady state is defined by the condition that investment exactly replaces depreciated capital: sf(k*) = δk*, where s is the savings rate, f(k) is the production function, and δ is the depreciation rate. But nothing in the Solow model says which steady state is best. Different savings rates produce different steady-state capital stocks—and the **golden rule** asks which one maximizes what people actually care about: consumption.

Steady-state consumption per worker equals output minus investment: c* = f(k*) − δk*. To maximize this, take the derivative with respect to k* and set it to zero: f'(k*) = δ. This is the **golden rule condition**—the marginal product of capital equals the depreciation rate. The intuition is straightforward. Adding one more unit of capital per worker produces f'(k) additional output but requires δ units of investment just to replace what depreciates. When f'(k) > δ, the extra output exceeds the maintenance cost, so more capital raises consumption. When f'(k) < δ, the economy is over-capitalized—it is investing so heavily that the maintenance burden on the extra capital exceeds the additional output it generates, and consumption would actually rise if the economy saved less.

The golden rule is a **normative benchmark**, not a prediction of where economies end up. The Solow model's savings rate is exogenous—set by habit, institutions, or policy—and there is no mechanism guaranteeing it equals the golden rule rate. An economy with too little capital (f'(k*) > δ) is **dynamically efficient** but below the golden rule; reaching it requires a temporary sacrifice of consumption to build up capital. An economy with too much capital (f'(k*) < δ) is **dynamically inefficient**—a striking result because it means the economy could increase consumption in every period, both present and future, simply by saving less. This is a rare free lunch in economics: reducing investment raises consumption today and raises steady-state consumption tomorrow because the economy was wasting resources maintaining unproductive capital.

Whether real economies are dynamically efficient is an empirical question with significant policy implications. Abel, Mankiw, Summers, and Zeckhauser (1989) argued that the U.S. and other developed economies are dynamically efficient because the return on capital consistently exceeds the economy's growth rate—a condition equivalent to being below the golden rule. If correct, this means reaching the golden rule would require higher savings, with a transitional cost of reduced consumption for current generations to benefit future ones. This intergenerational tradeoff is precisely what the golden rule highlights: it tells you the destination, but getting there may require sacrifices that no single generation has an incentive to make voluntarily.
