---
id: overlapping-generations-model
title: Overlapping Generations Model
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: dynamic-optimization-macro
  type: hard
- id: consumer-optimum
  type: hard
- id: systems-of-linear-equations
  type: hard
- id: lagrange-multipliers
  type: soft
builds-toward:
- fiscal-multiplier-dynamics
tags:
- demographics
- fiscal-policy
- non-ricardian-effects
- life-cycle
stage: expert
status: draft
---

# Overlapping Generations Model

## Core Idea
Overlapping generations models feature agents who live for multiple periods and face finite horizons, creating non-Ricardian fiscal effects where the timing of taxes matters for consumption and output. Asset prices, savings, and consumption depend on demographics and the age distribution of the population, explaining phenomena like why debt-financed tax cuts stimulate demand and how aging populations affect asset returns. OLG models are workhorses for analyzing fiscal sustainability and generational incidence of policy changes.

## Questions

```yaml
- question: "In an OLG model, the government cuts taxes today and finances the shortfall by issuing bonds. Unlike in the representative-agent (Ramsey) model, this stimulates current consumption. What is the key reason?"
  type: multiple-choice
  options:
    - "Bond-financed tax cuts lower the interest rate, encouraging borrowing and spending"
    - "Today's young generation receives the tax cut but may not live long enough to pay the higher future taxes needed to repay the debt, so they spend more"
    - "The government bond directly adds to physical capital, raising productivity and wages"
    - "The OLG model assumes agents are irrational and do not anticipate future tax increases"
  answer: 1
  explanation: "The key is finite lifetimes. In a representative-agent model, the single infinitely-lived household fully internalizes future debt repayment and saves the entire tax cut, leaving consumption unchanged (Ricardian equivalence). In the OLG model, today's young generation receives the tax cut and faces only part of the future repayment burden — some taxes will fall on generations not yet born. Because these unborn generations cannot offset the stimulus by reducing current saving, the currently living increase consumption. Government debt is net wealth for the currently alive even though it is a future liability in aggregate."

- question: "A standard OLG economy has over-accumulated capital — the interest rate has fallen below the economy's growth rate. Which policy could potentially improve everyone's welfare?"
  type: multiple-choice
  options:
    - "A balanced-budget increase in government spending, which crowds out private investment and reduces the capital stock"
    - "Introducing a pay-as-you-go social security system that transfers resources from the young (workers) to the old (retirees)"
    - "Raising income taxes on workers to reduce consumption and increase saving"
    - "Monetary expansion to lower real interest rates further, encouraging more investment"
  answer: 1
  explanation: "This exploits the OLG result that competitive equilibria can be dynamically inefficient. When r < g (interest rate below growth rate), the economy has over-accumulated capital — everyone is saving too much and could be better off consuming more. Pay-as-you-go social security transfers resources from the young to the old each period, effectively reducing aggregate saving and dissipating the excess capital. In this case, social security raises welfare by correcting the over-accumulation — a result impossible in the representative-agent framework, where equilibria are always Pareto optimal."

- question: "In the OLG model, government debt represents net wealth for the currently living generations even though it is a liability at the aggregate level."
  type: true-false
  answer: true
  explanation: "This is the central non-Ricardian property of OLG models. The currently living hold government bonds as assets (wealth to them). The future taxes needed to repay those bonds will fall partly on generations not yet alive, who cannot reduce their current saving in response. From the perspective of the living, the bonds are genuine wealth — not cancelled out by an offsetting increase in their own saving for future taxes. This is why debt-financed fiscal expansions have real stimulative effects in OLG models."

- question: "In the OLG model, a debt-financed tax cut has no effect on aggregate consumption because rational households save the entire tax cut to pay higher future taxes — just as in the representative-agent model."
  type: true-false
  answer: false
  explanation: "This statement describes Ricardian equivalence, which holds in the representative-agent model but fails in OLG models. OLG breaks Ricardian equivalence because the future taxes needed to service the debt fall partly on future generations not yet alive. Today's young generation saves only to cover their own expected future tax burden, which is less than the full debt. The remainder of the tax cut gets spent. This is precisely why OLG models are used to analyze fiscal stimulus and generational incidence — they capture effects that Ricardian reasoning rules out by construction."

- question: "Why do OLG models generate non-Ricardian fiscal effects, and what feature of human demography is the model capturing that the representative-agent model ignores?"
  type: short-answer
  answer: "OLG models generate non-Ricardian effects because agents have finite lifetimes and new generations are continuously born. When the government borrows today, the repayment burden falls partly on future generations not yet alive — who cannot reduce current saving in response. The representative-agent model assumes a single infinitely-lived household that fully internalizes all future tax liabilities, so debt financing is equivalent to lump-sum taxation. OLG captures the fact that real economies consist of overlapping cohorts with different birth dates, and fiscal policy redistributes across these generations, with effects that a single representative agent cannot replicate."
  explanation: "The key insight is not that agents are irrational — they are fully optimizing in OLG. The difference is purely structural: finite lives mean the future repayment burden is borne by different people than those who received the tax cut. This creates a true redistribution across generations that has real macroeconomic effects. The demographic feature being captured is the continuous birth and death of cohorts, which ensures that aggregate saving never fully offsets government dissaving."
```

## Explainer

From dynamic optimization, you know how to solve an agent's intertemporal consumption problem: maximize lifetime utility subject to a budget constraint, yielding Euler equations that link consumption across periods. The standard approach assumes an **infinitely-lived representative agent** — a single household that lives forever and therefore fully internalizes the future costs of current government borrowing. The **overlapping generations (OLG) model**, introduced by Samuelson and Diamond, makes one critical change: agents have **finite lifetimes**. At any moment, multiple generations coexist — young workers earning income alongside old retirees spending their savings. New generations are continuously born, and old ones die. This seemingly small modification produces fundamentally different macroeconomic predictions.

The simplest OLG setup has two periods: agents work when young and retire when old. A young agent earns wage income, consumes some of it, and saves the rest by purchasing assets (capital or government bonds) to fund retirement consumption. Using your knowledge of Lagrange multipliers and constrained optimization, the young agent's problem yields a familiar Euler equation linking first-period and second-period consumption to the interest rate. But here is the key difference from the infinitely-lived model: when the government cuts taxes today and borrows to finance the shortfall, the **young generation** benefits from lower taxes now and may die before the debt must be repaid through higher future taxes. The burden falls on **future generations** who are not yet alive to adjust their behavior. This breaks **Ricardian equivalence** — the proposition that debt-financed tax cuts have no real effect because rational agents save the tax cut to pay future taxes. In the OLG model, they don't, because the future taxes fall on different people.

This non-Ricardian property makes OLG models essential for analyzing fiscal policy. A debt-financed tax cut genuinely stimulates current consumption because today's young generation spends more without fully accounting for the future repayment burden. Government debt is **net wealth** for the currently living, even though it represents a future liability — because that liability is partially borne by the unborn. The model also naturally captures **demographic effects** on the macroeconomy. When a large cohort (like the baby boomers) moves through their working years, their collective saving drives down interest rates and bids up asset prices. When that cohort retires and begins dissaving, the process reverses — asset prices fall and interest rates rise as the ratio of savers to dissavers shifts. This lifecycle saving mechanism is the foundation of the **asset meltdown hypothesis** and many analyses of pension system sustainability.

The OLG framework also reveals that competitive equilibria can be **dynamically inefficient** — a possibility that never arises with infinitely-lived agents. If the economy saves too much (capital is over-accumulated), the interest rate falls below the growth rate, and everyone could be made better off by reducing saving. Government debt or pay-as-you-go social security can actually improve welfare in this case by transferring resources from young to old, reducing excessive capital accumulation. This result, unique to finite-horizon models, provides a theoretical justification for social security systems and government debt that cannot exist in the representative-agent framework — making OLG models indispensable for any serious analysis of intergenerational fiscal policy.
