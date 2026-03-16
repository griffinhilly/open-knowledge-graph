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
stage: advanced
status: draft
---

# Overlapping Generations Model

## Core Idea
The OLG model assumes finite-lived agents with overlapping cohorts existing in every period. This creates realistic heterogeneity in asset holdings and savings by age. Capital accumulation depends on the balance between young savers and old dissavers, and can exhibit path dependence absent in infinite-horizon models.

## Explainer

The infinite-horizon representative agent model — the workhorse of modern macroeconomics — assumes a single agent who lives forever and optimizes over an infinite future. This is analytically convenient but obscures something fundamental: in reality, people are born, age, and die, and at any point in time the economy contains young workers accumulating savings alongside retirees drawing them down. The **overlapping generations (OLG) model**, introduced by Paul Samuelson and Peter Diamond, takes this demographic structure seriously.

In the simplest two-period OLG model, agents live for two periods: youth and old age. When young, they work, earn wages, consume some, and save the rest. When old, they consume their savings plus interest and then exit the economy. Crucially, a new cohort of young agents is born every period, overlapping with the current old generation. Capital in the economy is simply the aggregate savings of the current young generation, which becomes the capital stock available for production in the next period. From the Bellman equation you studied, you know how to set up dynamic optimization problems recursively; in the OLG model, each agent solves a finite-horizon version, choosing savings to maximize lifetime utility across their two periods subject to wage income when young and capital income when old.

The OLG model generates several results that are impossible in the infinite-horizon framework. First, the competitive equilibrium can be **dynamically inefficient** — the economy may accumulate too much capital, driving the rate of return below the growth rate. In an infinite-horizon model, a forward-looking agent would never let this happen, but in the OLG model, each generation saves without coordinating with future generations, and overaccumulation can result. This opens a role for government policy: a pay-as-you-go social security system can improve welfare by transferring resources from the young (who are oversaving) to the old, effectively substituting intergenerational transfers for excessive capital accumulation.

Second, the OLG model naturally generates **heterogeneity** in wealth and consumption by age — young agents are poor and borrowing-constrained, middle-aged agents are high earners and savers, and the old are dissavers living off accumulated wealth. This life-cycle variation in behavior means that demographic shifts (baby booms, aging populations) have first-order effects on aggregate savings, interest rates, and capital accumulation — effects that a representative-agent model cannot capture. The OLG framework is therefore essential for analyzing pension reform, the macroeconomic consequences of population aging, and any policy whose burden falls differently on different generations.
