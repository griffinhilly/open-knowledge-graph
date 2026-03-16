---
id: overlapping-generations-models
title: Overlapping Generations Models
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: steady-state-analysis-growth
  type: hard
- id: dynamic-optimization-macroeconomics
  type: hard
- id: constrained-optimization-lagrange
  type: soft
builds-toward:
- lifecycle-hypothesis-consumption
- intergenerational-equity-fiscal-policy
tags:
- generations
- lifecycle
- overlapping
stage: formal-systems
status: draft
---

# Overlapping Generations Models

## Core Idea
OLG models feature agents of different ages living simultaneously; each generation is born, works, saves, retires, and dies. This structure makes intergenerational effects central to the analysis, revealing how current policy affects not just today's households but future generations. OLG models naturally incorporate lifecycle consumption patterns and can show how unfunded government debt shifts the burden to future generations, making them essential for analyzing pensions, social security, and long-term fiscal policy.

## Explainer

From steady-state growth analysis, you understand how an economy converges to a long-run equilibrium with constant growth rates. From dynamic optimization, you know how to set up and solve intertemporal maximization problems. The **overlapping generations (OLG) model** introduces something neither the Solow model nor the infinitely-lived representative agent model can capture: the fact that people are born, age, and die, and that at any moment multiple generations coexist with different economic interests. This demographic structure turns out to have profound implications for capital accumulation, interest rates, and the effects of government policy.

The simplest OLG model (Diamond, 1965) has two-period lives. In period one, an agent is **young**: they work, earn wages, consume some, and save the rest. In period two, they are **old**: they consume their savings plus interest and then exit the model. At every point in time, a generation of young workers and a generation of old retirees coexist — hence "overlapping." The young generation's savings become the economy's capital stock in the next period, which determines the wage and interest rate facing the next young generation. Using constrained optimization (your Lagrangian tools), each young agent maximizes U(c_young) + βU(c_old) subject to c_young + s = w and c_old = (1+r)s, yielding a savings function s(w, r) that depends on wages and interest rates.

The model's equilibrium links generations through the capital market. The capital stock next period equals this period's aggregate savings: K_{t+1} = s(w_t, r_{t+1}) × L_t, where L is the number of young workers. In steady state, capital per worker is constant, giving a fixed point where savings exactly replace depreciated capital and equip the next (larger, if population is growing) generation of workers. A critical result is that the OLG steady state can be **dynamically inefficient** — the economy may accumulate too much capital, with the interest rate falling below the population growth rate. This is impossible in the infinitely-lived agent model, where a single forward-looking optimizer would never over-save. The inefficiency arises because no agent lives forever to internalize the long-run consequences of aggregate saving decisions.

This dynamic inefficiency is precisely what makes OLG models essential for policy analysis. **Government debt** in an OLG model is not neutral (Ricardian equivalence fails) because current taxpayers and future taxpayers are different people. If the government cuts taxes today and issues bonds, current generations benefit from higher consumption, but future generations bear the repayment burden through higher taxes and a smaller capital stock (since government bonds crowd out private capital). Similarly, **pay-as-you-go social security** transfers resources from the current young to the current old. Whether this improves welfare depends on whether the economy is dynamically efficient or inefficient — in an over-accumulated economy, the transfer can actually make everyone better off by reducing excess capital. These intergenerational tradeoffs are invisible in representative-agent models, which is why OLG remains the workhorse framework for analyzing pensions, public debt sustainability, and demographic transitions like population aging.
