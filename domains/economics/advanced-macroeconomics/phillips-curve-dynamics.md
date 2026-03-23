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
stage: expert
status: validated
---

# Phillips Curve Dynamics in Modern Models

## Core Idea
The modern Phillips curve relates inflation to expected future inflation and current economic slack, with the slope reflecting nominal rigidities and firms' pricing behavior. This forward-looking specification—derived from New Keynesian models—shows that inflation depends on firms' expectations about future demand and costs, not just current conditions. The Phillips curve forms a key constraint on monetary policy trade-offs and crucially depends on the anchoring of inflation expectations.

## Questions

```yaml
- question: "An economy has experienced 5% annual inflation for three years. Despite a significant economic slowdown and rising unemployment, inflation stays persistently elevated. According to the New Keynesian Phillips Curve, what is the primary explanation?"
  type: multiple-choice
  options:
    - "The output gap has not yet become negative enough — the slowdown is insufficient to reduce inflation."
    - "Inflation expectations have become unanchored — firms set prices today based on expected future high inflation, which enters the NKPC directly and drives current inflation regardless of economic slack."
    - "Nominal rigidities have disappeared after years of high inflation, making the NKPC slope steeper and inflation more persistent."
    - "Monetary policy operates with a lag — the central bank's interest rate increases have not yet worked through the economy."
  answer: 1
  explanation: "This is the unanchored expectations dynamic. In the NKPC (π_t = βE_t[π_{t+1}] + κx_t), expected future inflation directly drives current inflation — it enters with a coefficient close to 1. If agents believe inflation will remain high, firms set higher prices today to avoid being stuck below future prices; workers demand higher wages anticipating future price increases. Slack reduces inflation only through κx_t, which may be small. Unanchored expectations can sustain high inflation even with substantial economic weakness — precisely the dilemma Volcker faced in 1979-1982."

- question: "Empirically, the slope coefficient κ in the NKPC appears to be quite small in advanced economies. What is the most important monetary policy implication of a flat Phillips curve?"
  type: multiple-choice
  options:
    - "Small κ means monetary policy is very powerful — small interest rate changes produce large inflation reductions."
    - "Small κ means inflation responds weakly to changes in economic slack — the central bank must engineer large recessions to reduce inflation by even a modest amount."
    - "Small κ means inflation is driven purely by expectations, so the central bank can achieve any target simply by announcing it."
    - "Small κ means the NKPC is unreliable and should be replaced by the original backward-looking Phillips curve."
  answer: 1
  explanation: "κ captures how strongly inflation responds to changes in the output gap or marginal cost. A small κ means even substantial economic slack produces only modest inflation reduction through the demand channel. This explains why the post-2008 Great Recession, which created enormous slack, produced only mild disinflation — the Phillips curve was very flat. The practical implication is that controlling inflation through demand management is costly when κ is small; expectations anchoring becomes the critical lever, making central bank credibility more, not less, important."

- question: "The New Keynesian Phillips Curve is fundamentally forward-looking: current inflation depends primarily on expectations of future inflation rather than on past inflation rates."
  type: true-false
  answer: true
  explanation: "This is the defining departure of the NKPC from the expectations-augmented Phillips curve. In the NKPC, current inflation is driven by expected future inflation E_t[π_{t+1}] — firms set prices based on where they expect prices to go, not where they have been. This forward-looking structure emerges from the Calvo model of staggered price setting: a firm adjusting its price today must set it optimally for the entire future period until it can adjust again. In contrast, the earlier expectations-augmented Phillips curve used lagged inflation as a proxy for expectations — a fundamentally different mechanism."

- question: "If a central bank engineers a recession by raising interest rates, inflation will fall quickly and significantly regardless of whether inflation expectations are anchored or unanchored."
  type: true-false
  answer: false
  explanation: "When expectations are unanchored, the recession's disinflationary effect through the output gap (κx_t) must fight against the upward pressure from high expected future inflation (βE_t[π_{t+1}]). If agents believe inflation will stay high, firms continue setting high prices even as demand falls. Reducing inflation requires either making the recession deep enough to overwhelm the expectations component, or convincing agents that future inflation will be lower. The Volcker disinflation required unemployment near 11% precisely because expectations were badly unanchored; a credible central bank could achieve the same disinflation with far less economic pain."

- question: "Why do central banks guard their inflation-fighting credibility so intensely, even during periods of stable, low inflation?"
  type: short-answer
  answer: "Because the NKPC shows that inflation depends primarily on expected future inflation. If agents believe the central bank will keep inflation near target, E_t[π_{t+1}] stays anchored, and inflation fluctuations remain small and easily corrected. But credibility, once lost, is expensive to rebuild — re-anchoring expectations requires a recession severe enough to convince agents the central bank will follow through. Maintaining credibility in good times prevents the far larger cost of rebuilding it later."
  explanation: "Volcker's 1979-1982 tightening is the canonical example: decades of accommodating inflation had unanchored expectations, and re-anchoring required driving unemployment to nearly 11%. A central bank that had maintained credibility throughout would never have faced that dilemma. The NKPC makes the mechanism precise: credibility directly controls the E_t[π_{t+1}] term, which enters current inflation with a coefficient close to 1. Credibility is not a soft institutional virtue — it is a direct input into the inflation equation."
```

## Explainer

The original Phillips curve you studied — a negative relationship between inflation and unemployment — was an empirical regularity that broke down in the 1970s when high inflation and high unemployment coexisted (stagflation). Friedman and Phelps had already predicted this: once workers and firms adjust their inflation expectations upward, the short-run tradeoff between inflation and unemployment shifts, and there is no permanent tradeoff to exploit. The modern New Keynesian Phillips Curve (NKPC) incorporates this lesson by making expectations the central driver of inflation dynamics.

The NKPC takes the form: **π_t = βE_t[π_{t+1}] + κx_t**, where π is inflation, E_t[π_{t+1}] is expected future inflation, x is the output gap (or marginal cost), β is a discount factor close to 1, and κ is the slope parameter. This equation emerges from the microeconomics of **staggered price setting** — the Calvo model where each period only a fraction of firms can adjust their prices. A firm that gets the chance to reset its price must think ahead: it sets a price that is optimal not just for today but for the entire expected duration until it can adjust again. If the firm expects higher inflation in the future, it sets a higher price today to avoid being stuck below its competitors. This forward-looking behavior is what makes the NKPC fundamentally different from the backward-looking, expectations-augmented Phillips curve.

The slope parameter κ encodes the **degree of nominal rigidity** in the economy. When prices are very sticky (few firms adjust each period), κ is small, and inflation responds weakly to the output gap — the central bank must engineer large output fluctuations to move inflation. When prices are flexible (many firms adjust frequently), κ is large, and inflation responds readily to demand conditions. Empirically, κ appears to be quite small in advanced economies, which explains why the Phillips curve has looked "flat" in recent decades: large swings in unemployment during the Great Recession produced only modest declines in inflation.

The critical policy implication involves **expectations anchoring**. If the central bank is credible — agents believe it will keep inflation near target — then E_t[π_{t+1}] stays close to the target, and inflation fluctuations are small and transient. The Phillips curve becomes a constraint the central bank can work with. But if credibility erodes and expectations become **unanchored**, the feedback loop turns vicious: higher expected inflation causes higher actual inflation (firms set higher prices today expecting higher costs tomorrow), which further raises expectations. This self-fulfilling dynamic explains why central banks guard their inflation-fighting credibility so fiercely, and why re-anchoring expectations after a period of high inflation — as Volcker did in the early 1980s — requires a costly recession to convince agents that the central bank will follow through on its commitment.
