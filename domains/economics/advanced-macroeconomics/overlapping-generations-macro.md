---
id: overlapping-generations-macro
title: Overlapping Generations Model
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: bellman-equation-dynamic-programming
  type: hard
- id: euler-equation-intertemporal-choice
  type: soft
tags:
- overlapping-generations
- heterogeneous-agents
- demographic-structure
stage: expert
status: draft
---

# Overlapping Generations Model

## Core Idea
The OLG model assumes finite-lived agents with overlapping cohorts existing in every period. This creates realistic heterogeneity in asset holdings and savings by age. Capital accumulation depends on the balance between young savers and old dissavers, and can exhibit path dependence absent in infinite-horizon models.

## Questions

```yaml
- question: "In the Diamond OLG model, why can the competitive equilibrium be dynamically inefficient — a result that is impossible in the infinite-horizon representative agent model?"
  type: multiple-choice
  options:
    - "Young agents in the OLG model discount the future too heavily, systematically undersaving and leaving the capital stock too low"
    - "Each generation saves without coordinating with future generations, allowing overaccumulation of capital that depresses the return below the growth rate"
    - "The central bank in the OLG framework sets nominal interest rates below the market-clearing level, distorting savings incentives"
    - "The OLG model assumes no financial markets for risk-sharing between generations, preventing efficient capital allocation"
  answer: 1
  explanation: "Dynamic inefficiency (overaccumulation) occurs when the economy accumulates so much capital that the real interest rate falls below the growth rate. In an infinite-horizon model, a forward-looking agent sees this and reduces saving — overaccumulation is self-correcting. In the OLG model, each generation saves only to fund its own retirement, without considering the effect on future generations' capital stock. No individual cohort has the incentive to reduce its savings to fix the economy-wide overaccumulation. The result is a coordination failure across generations."

- question: "A government introduces a pay-as-you-go social security system in an OLG economy that is dynamically inefficient. The policy taxes the young and transfers the revenue to the old. This policy:"
  type: multiple-choice
  options:
    - "Reduces welfare for all generations, since forced transfers prevent households from achieving their individually optimal savings plans"
    - "Can improve welfare for all generations by reducing the overaccumulated capital stock and raising the rate of return on remaining capital"
    - "Has no effect because rational agents exactly offset the transfer by adjusting their private savings (Ricardian equivalence applies)"
    - "Benefits current retirees but harms all future generations by reducing the capital available for their retirement savings"
  answer: 1
  explanation: "In a dynamically inefficient OLG economy, too much capital drives the return below the growth rate — everyone would be better off with less capital and more current consumption. A PAYGO social security system effectively transfers resources from young savers (who are oversaving from society's perspective) to the old, reducing aggregate capital accumulation. If the economy was in the dynamically inefficient region, this improves the welfare of every generation, including future ones, because the higher return on the smaller capital stock more than compensates. This is a genuine Pareto improvement — the kind of result that cannot arise in a representative-agent model."

- question: "The standard infinite-horizon representative agent model can generate dynamic inefficiency (capital overaccumulation) under the right parameter values, just as the OLG model can."
  type: true-false
  answer: false
  explanation: "Dynamic inefficiency is structurally impossible in the infinite-horizon model. A single infinitely-lived, forward-looking agent observing the interest rate fall below the growth rate would immediately reduce savings to exploit the inefficiency — the model is internally self-correcting. Dynamic inefficiency in the OLG model is not a parameter choice but a structural result of the finite-lived, overlapping demographic structure: generations cannot coordinate across time, so the self-correcting mechanism is absent. This is one reason the OLG model is qualitatively different from, not merely a special case of, the infinite-horizon model."

- question: "In an OLG model, an unusually large young cohort (a baby boom generation) tends to increase aggregate savings and can drive down the real interest rate as this cohort passes through its working years."
  type: true-false
  answer: true
  explanation: "In the OLG model, capital is the aggregate savings of the current young generation, which becomes next period's capital stock. A large cohort of young workers saves more in absolute terms, increasing the capital supply and driving down the return on capital. This demographic-driven capital accumulation is a major mechanism through which population dynamics affect macroeconomic variables — an effect invisible to the representative-agent framework. The aging of baby boom generations in real economies has been linked empirically to changes in real interest rates along exactly this channel."

- question: "Explain why the overlapping generations model is more appropriate than the infinite-horizon representative agent model for analyzing the macroeconomic consequences of an aging population or pension reform."
  type: short-answer
  answer: "The OLG model captures demographic heterogeneity that the representative-agent model suppresses by assumption. In the OLG framework, young workers and retirees coexist in every period, and their behavior differs systematically: the young save, the old dissave. A shift in the age distribution — more retirees, fewer workers — directly changes the ratio of dissavers to savers, affecting the aggregate savings rate, capital stock, and interest rates. Pension reform redistributes resources between cohorts, which also changes savings behavior in ways that depend on the recipient's life stage. The representative agent, being a single infinitely-lived agent, has no concept of retirement, age-specific savings motives, or intergenerational transfers, so these questions are unanswerable within that framework."
  explanation: "The OLG model's key advantage is not realism for its own sake but capturing first-order mechanisms — life-cycle savings, demographic structure, and intergenerational transfers — that the infinite-horizon model abstracts away. Analyzing pension reform with a representative-agent model would be like analyzing a relay race by studying a single runner: the coordination and handoff problem, which is the whole point, would be invisible."
```

## Explainer

The infinite-horizon representative agent model — the workhorse of modern macroeconomics — assumes a single agent who lives forever and optimizes over an infinite future. This is analytically convenient but obscures something fundamental: in reality, people are born, age, and die, and at any point in time the economy contains young workers accumulating savings alongside retirees drawing them down. The **overlapping generations (OLG) model**, introduced by Paul Samuelson and Peter Diamond, takes this demographic structure seriously.

In the simplest two-period OLG model, agents live for two periods: youth and old age. When young, they work, earn wages, consume some, and save the rest. When old, they consume their savings plus interest and then exit the economy. Crucially, a new cohort of young agents is born every period, overlapping with the current old generation. Capital in the economy is simply the aggregate savings of the current young generation, which becomes the capital stock available for production in the next period. From the Bellman equation you studied, you know how to set up dynamic optimization problems recursively; in the OLG model, each agent solves a finite-horizon version, choosing savings to maximize lifetime utility across their two periods subject to wage income when young and capital income when old.

The OLG model generates several results that are impossible in the infinite-horizon framework. First, the competitive equilibrium can be **dynamically inefficient** — the economy may accumulate too much capital, driving the rate of return below the growth rate. In an infinite-horizon model, a forward-looking agent would never let this happen, but in the OLG model, each generation saves without coordinating with future generations, and overaccumulation can result. This opens a role for government policy: a pay-as-you-go social security system can improve welfare by transferring resources from the young (who are oversaving) to the old, effectively substituting intergenerational transfers for excessive capital accumulation.

Second, the OLG model naturally generates **heterogeneity** in wealth and consumption by age — young agents are poor and borrowing-constrained, middle-aged agents are high earners and savers, and the old are dissavers living off accumulated wealth. This life-cycle variation in behavior means that demographic shifts (baby booms, aging populations) have first-order effects on aggregate savings, interest rates, and capital accumulation — effects that a representative-agent model cannot capture. The OLG framework is therefore essential for analyzing pension reform, the macroeconomic consequences of population aging, and any policy whose burden falls differently on different generations.
