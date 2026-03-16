---
id: phillips-curve-dynamics
title: Phillips Curve Dynamics in Modern Models
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: phillips-curve
  type: hard
- id: new-keynesian-model-baseline
  type: hard
- id: rational-expectations-macro
  type: soft
- id: differential-equations-intro
  type: soft
- id: probability-axioms
  type: soft
- id: time-series-basics-econometrics
  type: soft
builds-toward:
- taylor-rule-monetary-policy
tags:
- inflation
- unemployment
- expectations
- price-setting
stage: advanced
status: draft
---

# Phillips Curve Dynamics in Modern Models

## Core Idea
The modern Phillips curve relates inflation to expected future inflation and current economic slack, with the slope reflecting nominal rigidities and firms' pricing behavior. This forward-looking specification—derived from New Keynesian models—shows that inflation depends on firms' expectations about future demand and costs, not just current conditions. The Phillips curve forms a key constraint on monetary policy trade-offs and crucially depends on the anchoring of inflation expectations.

## Explainer

The original Phillips curve you studied — a negative relationship between inflation and unemployment — was an empirical regularity that broke down in the 1970s when high inflation and high unemployment coexisted (stagflation). Friedman and Phelps had already predicted this: once workers and firms adjust their inflation expectations upward, the short-run tradeoff between inflation and unemployment shifts, and there is no permanent tradeoff to exploit. The modern New Keynesian Phillips Curve (NKPC) incorporates this lesson by making expectations the central driver of inflation dynamics.

The NKPC takes the form: **π_t = βE_t[π_{t+1}] + κx_t**, where π is inflation, E_t[π_{t+1}] is expected future inflation, x is the output gap (or marginal cost), β is a discount factor close to 1, and κ is the slope parameter. This equation emerges from the microeconomics of **staggered price setting** — the Calvo model where each period only a fraction of firms can adjust their prices. A firm that gets the chance to reset its price must think ahead: it sets a price that is optimal not just for today but for the entire expected duration until it can adjust again. If the firm expects higher inflation in the future, it sets a higher price today to avoid being stuck below its competitors. This forward-looking behavior is what makes the NKPC fundamentally different from the backward-looking, expectations-augmented Phillips curve.

The slope parameter κ encodes the **degree of nominal rigidity** in the economy. When prices are very sticky (few firms adjust each period), κ is small, and inflation responds weakly to the output gap — the central bank must engineer large output fluctuations to move inflation. When prices are flexible (many firms adjust frequently), κ is large, and inflation responds readily to demand conditions. Empirically, κ appears to be quite small in advanced economies, which explains why the Phillips curve has looked "flat" in recent decades: large swings in unemployment during the Great Recession produced only modest declines in inflation.

The critical policy implication involves **expectations anchoring**. If the central bank is credible — agents believe it will keep inflation near target — then E_t[π_{t+1}] stays close to the target, and inflation fluctuations are small and transient. The Phillips curve becomes a constraint the central bank can work with. But if credibility erodes and expectations become **unanchored**, the feedback loop turns vicious: higher expected inflation causes higher actual inflation (firms set higher prices today expecting higher costs tomorrow), which further raises expectations. This self-fulfilling dynamic explains why central banks guard their inflation-fighting credibility so fiercely, and why re-anchoring expectations after a period of high inflation — as Volcker did in the early 1980s — requires a costly recession to convince agents that the central bank will follow through on its commitment.
