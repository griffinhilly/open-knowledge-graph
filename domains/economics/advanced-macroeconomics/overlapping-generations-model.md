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
stage: advanced
status: draft
---

# Overlapping Generations Model

## Core Idea
Overlapping generations models feature agents who live for multiple periods and face finite horizons, creating non-Ricardian fiscal effects where the timing of taxes matters for consumption and output. Asset prices, savings, and consumption depend on demographics and the age distribution of the population, explaining phenomena like why debt-financed tax cuts stimulate demand and how aging populations affect asset returns. OLG models are workhorses for analyzing fiscal sustainability and generational incidence of policy changes.

## Explainer

From dynamic optimization, you know how to solve an agent's intertemporal consumption problem: maximize lifetime utility subject to a budget constraint, yielding Euler equations that link consumption across periods. The standard approach assumes an **infinitely-lived representative agent** — a single household that lives forever and therefore fully internalizes the future costs of current government borrowing. The **overlapping generations (OLG) model**, introduced by Samuelson and Diamond, makes one critical change: agents have **finite lifetimes**. At any moment, multiple generations coexist — young workers earning income alongside old retirees spending their savings. New generations are continuously born, and old ones die. This seemingly small modification produces fundamentally different macroeconomic predictions.

The simplest OLG setup has two periods: agents work when young and retire when old. A young agent earns wage income, consumes some of it, and saves the rest by purchasing assets (capital or government bonds) to fund retirement consumption. Using your knowledge of Lagrange multipliers and constrained optimization, the young agent's problem yields a familiar Euler equation linking first-period and second-period consumption to the interest rate. But here is the key difference from the infinitely-lived model: when the government cuts taxes today and borrows to finance the shortfall, the **young generation** benefits from lower taxes now and may die before the debt must be repaid through higher future taxes. The burden falls on **future generations** who are not yet alive to adjust their behavior. This breaks **Ricardian equivalence** — the proposition that debt-financed tax cuts have no real effect because rational agents save the tax cut to pay future taxes. In the OLG model, they don't, because the future taxes fall on different people.

This non-Ricardian property makes OLG models essential for analyzing fiscal policy. A debt-financed tax cut genuinely stimulates current consumption because today's young generation spends more without fully accounting for the future repayment burden. Government debt is **net wealth** for the currently living, even though it represents a future liability — because that liability is partially borne by the unborn. The model also naturally captures **demographic effects** on the macroeconomy. When a large cohort (like the baby boomers) moves through their working years, their collective saving drives down interest rates and bids up asset prices. When that cohort retires and begins dissaving, the process reverses — asset prices fall and interest rates rise as the ratio of savers to dissavers shifts. This lifecycle saving mechanism is the foundation of the **asset meltdown hypothesis** and many analyses of pension system sustainability.

The OLG framework also reveals that competitive equilibria can be **dynamically inefficient** — a possibility that never arises with infinitely-lived agents. If the economy saves too much (capital is over-accumulated), the interest rate falls below the growth rate, and everyone could be made better off by reducing saving. Government debt or pay-as-you-go social security can actually improve welfare in this case by transferring resources from young to old, reducing excessive capital accumulation. This result, unique to finite-horizon models, provides a theoretical justification for social security systems and government debt that cannot exist in the representative-agent framework — making OLG models indispensable for any serious analysis of intergenerational fiscal policy.
