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
stage: expert
status: validated
---

# Overlapping Generations Models

## Core Idea
OLG models feature agents of different ages living simultaneously; each generation is born, works, saves, retires, and dies. This structure makes intergenerational effects central to the analysis, revealing how current policy affects not just today's households but future generations. OLG models naturally incorporate lifecycle consumption patterns and can show how unfunded government debt shifts the burden to future generations, making them essential for analyzing pensions, social security, and long-term fiscal policy.

## Questions

```yaml
- question: "A government in a Diamond OLG economy cuts taxes today and issues bonds to finance the shortfall. Unlike in the Ramsey infinitely-lived agent model, this policy is likely to reduce the welfare of future generations. What is the key reason Ricardian equivalence fails here?"
  type: multiple-choice
  options:
    - "Future generations are literally different people from the current generation that received the tax cut, so there is no mechanism by which today's households fully offset the future tax burden through increased saving"
    - "Government bonds always crowd out private capital in any macroeconomic model, regardless of agent lifespans"
    - "The young generation over-saves in response to the debt, causing dynamic inefficiency and reducing steady-state output"
    - "OLG models assume bond markets do not exist, so any government deficit must be financed by money creation"
  answer: 0
  explanation: "Ricardian equivalence — the proposition that tax cuts financed by debt have no real effects — relies on the assumption that current households fully internalize future tax liabilities and increase saving to offset them. In an infinitely-lived agent model, the same household pays both the current benefit and the future cost. In an OLG model, the household receiving the tax cut today will be dead when the debt is repaid. Future generations (different agents) bear the repayment burden with no offsetting inheritance of the original benefit. There is no mechanism for complete intergenerational internalization, so debt shifts real resources from future to current generations."

- question: "An OLG economy is at a steady state where the real interest rate r equals 1% but the population growth rate n equals 2%. Which statement is correct?"
  type: multiple-choice
  options:
    - "This violates a fundamental stability condition — no OLG economy can be stable when r < n"
    - "The economy is dynamically inefficient: too much capital has been accumulated, and reducing aggregate saving could raise consumption for all generations simultaneously"
    - "The economy is at the golden rule steady state, where per-capita consumption is maximized"
    - "This outcome can only arise in the infinitely-lived representative agent model, not in OLG, because the Ramsey condition would prevent over-saving"
  answer: 1
  explanation: "When the interest rate falls below the population growth rate (r < n), the economy is dynamically inefficient — it has accumulated more capital than the 'golden rule' level that maximizes steady-state consumption. In this region, reducing the capital stock (consuming more, saving less) would actually increase per-capita output and consumption for all future generations simultaneously, a Pareto improvement. This cannot occur in the Ramsey model because a forward-looking infinitely-lived agent would anticipate the diminishing returns from excessive saving and never over-accumulate. The OLG result arises because no individual agent lives long enough to internalize the full effect of aggregate saving on future wages and interest rates."

- question: "In an overlapping generations model, Ricardian equivalence holds: a household that receives a tax cut today will fully increase saving to offset the future tax burden, leaving real allocations unchanged."
  type: true-false
  answer: false
  explanation: "Ricardian equivalence fails in OLG because the 'household' that benefits and the 'household' that pays are different people separated by time and death. The current young generation receives a tax cut and might save more, but they will not save enough to fully offset future tax burdens borne by generations not yet born — they have no reason to. Even if they leave bequests, perfect intergenerational transfers would require complete bequest motives that fully value future generations' welfare, an assumption the basic OLG model does not make. The failure of Ricardian equivalence is one of the key results that makes OLG models policy-relevant in ways that representative-agent models are not."

- question: "An OLG economy can over-accumulate capital and reach a dynamically inefficient steady state — an outcome that is impossible in the standard infinitely-lived representative-agent model."
  type: true-false
  answer: true
  explanation: "Dynamic inefficiency (r < n) is a genuine possibility in OLG models and has no analog in the Ramsey model. In the Ramsey model, the representative agent optimizes over an infinite horizon and would reduce saving whenever the marginal product of capital falls below the discount-adjusted growth rate. But in OLG, the saving decisions of today's young are driven by their own two-period optimization — they save for retirement, not to maximize aggregate capital efficiency. If the equilibrium savings rate is high enough, the aggregate capital stock can exceed the golden rule level, making everyone worse off. This is not just a theoretical curiosity: empirical estimates suggest some advanced economies may be near or in the dynamically inefficient region."

- question: "Why are OLG models essential for analyzing pay-as-you-go social security, and why does the same analysis not arise in a representative-agent framework?"
  type: short-answer
  answer: "Pay-as-you-go social security transfers current workers' contributions to current retirees. In an OLG model, these are literally different agents: the young pay, the old receive, and the welfare effects on each generation can be traced separately. Whether the program improves aggregate welfare depends on whether the economy is dynamically efficient or not — in an over-accumulated economy, reducing capital by transferring resources from savers (young) to dissavers (old) can actually raise everyone's consumption path. In a representative-agent model, 'the young' and 'the old' are just the same agent at different points in time; the agent fully internalizes the contribution-benefit schedule and the program has no net effect — Ricardian equivalence applies. The genuine distributional conflict between living generations, central to all social security analysis, is structurally absent in the representative-agent setting."
  explanation: "This is why Diamond (1965) and Samuelson (1958) developed OLG models specifically for intergenerational economics. Debates about social security solvency, demographic transitions, and funded vs. unfunded pension systems cannot be meaningfully posed in a representative-agent model because the model's structure already assumes away the distributional conflicts that make these questions interesting. OLG provides the minimal framework in which 'young' and 'old' have distinct interests, making it the workhorse model for public finance questions involving multiple generations."
```

## Explainer

From steady-state growth analysis, you understand how an economy converges to a long-run equilibrium with constant growth rates. From dynamic optimization, you know how to set up and solve intertemporal maximization problems. The **overlapping generations (OLG) model** introduces something neither the Solow model nor the infinitely-lived representative agent model can capture: the fact that people are born, age, and die, and that at any moment multiple generations coexist with different economic interests. This demographic structure turns out to have profound implications for capital accumulation, interest rates, and the effects of government policy.

The simplest OLG model (Diamond, 1965) has two-period lives. In period one, an agent is **young**: they work, earn wages, consume some, and save the rest. In period two, they are **old**: they consume their savings plus interest and then exit the model. At every point in time, a generation of young workers and a generation of old retirees coexist — hence "overlapping." The young generation's savings become the economy's capital stock in the next period, which determines the wage and interest rate facing the next young generation. Using constrained optimization (your Lagrangian tools), each young agent maximizes U(c_young) + βU(c_old) subject to c_young + s = w and c_old = (1+r)s, yielding a savings function s(w, r) that depends on wages and interest rates.

The model's equilibrium links generations through the capital market. The capital stock next period equals this period's aggregate savings: K_{t+1} = s(w_t, r_{t+1}) × L_t, where L is the number of young workers. In steady state, capital per worker is constant, giving a fixed point where savings exactly replace depreciated capital and equip the next (larger, if population is growing) generation of workers. A critical result is that the OLG steady state can be **dynamically inefficient** — the economy may accumulate too much capital, with the interest rate falling below the population growth rate. This is impossible in the infinitely-lived agent model, where a single forward-looking optimizer would never over-save. The inefficiency arises because no agent lives forever to internalize the long-run consequences of aggregate saving decisions.

This dynamic inefficiency is precisely what makes OLG models essential for policy analysis. **Government debt** in an OLG model is not neutral (Ricardian equivalence fails) because current taxpayers and future taxpayers are different people. If the government cuts taxes today and issues bonds, current generations benefit from higher consumption, but future generations bear the repayment burden through higher taxes and a smaller capital stock (since government bonds crowd out private capital). Similarly, **pay-as-you-go social security** transfers resources from the current young to the current old. Whether this improves welfare depends on whether the economy is dynamically efficient or inefficient — in an over-accumulated economy, the transfer can actually make everyone better off by reducing excess capital. These intergenerational tradeoffs are invisible in representative-agent models, which is why OLG remains the workhorse framework for analyzing pensions, public debt sustainability, and demographic transitions like population aging.
