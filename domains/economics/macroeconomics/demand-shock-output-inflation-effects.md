---
id: demand-shock-output-inflation-effects
title: 'Demand Shocks: Effects on Output and Inflation'
domain: economics
course: macroeconomics
prerequisites:
- id: okuns-law-unemployment-output-relation
  type: hard
- id: aggregate-demand-expenditure-approach
  type: hard
builds-toward:
- phillips-curve
tags:
- demand-shock
- output
- inflation
- unemployment
- multiplier
stage: formal-systems
status: draft
---

# Demand Shocks: Effects on Output and Inflation

## Core Idea
A positive demand shock increases output in the short run (sticky prices); firms respond by increasing production. If sustained, it tightens the labor market, pushing unemployment below NAIRU and triggering wage-price increases. In the long run, inflation rises while output returns to potential.

## How It's Best Learned
Trace demand shock through AS-AD diagram and Phillips curve. Positive shock shifts AD right, raising output and lowering unemployment below NAIRU. This creates inflation pressure. Show policy trade-off.

## Common Misconceptions
- Assuming demand shocks have permanent output effects.
- Treating inflation as purely demand-driven.
- Forgetting lag from shock to inflation (1-2 years).

## Questions

```yaml
- question: "The government announces a large stimulus package. A commentator says 'This will permanently increase output by creating jobs.' What's wrong with this claim?"
  type: multiple-choice
  options:
    - "Demand stimulus packages never raise output, even in the short run"
    - "The output increase is temporary — once the labor market tightens and inflation rises, real output returns to potential"
    - "Fiscal stimulus only works through monetary channels, not directly through spending"
    - "Output gains from demand shocks are permanent as long as unemployment stays below NAIRU"
  answer: 1
  explanation: "The common misconception is that demand shocks produce permanent output gains. In the short run, sticky prices allow output to rise above potential. But as unemployment falls below NAIRU, the wage-price spiral pushes prices up, eroding real demand and returning output to its potential level. The permanent legacy is a higher price level (or sustained inflation), not higher real output. The commentator is confusing the short-run effect with the long-run equilibrium."

- question: "Six months after a large positive demand shock, a central bank observes rising inflation but output still above potential. Why hasn't output returned to potential yet?"
  type: multiple-choice
  options:
    - "The shock was too small to have a lasting effect on the labor market"
    - "There is a 1-2 year lag between the initial shock and full price adjustment because the wage-price spiral takes time to work through contracts and bargaining"
    - "Inflation always rises immediately with demand because prices are flexible"
    - "Output above potential and rising inflation cannot coexist — the central bank's data is wrong"
  answer: 1
  explanation: "Price adjustment is slow: workers have nominal wage contracts, firms have menu costs, and bargaining takes time. First, unemployment falls below NAIRU; then workers gain bargaining power and push for wage increases; then firms pass through higher labor costs in higher prices. This full cycle typically takes 1-2 years after the initial shock. Rising inflation while output is still above potential is exactly the expected mid-adjustment picture."

- question: "In the long run, a sustained positive demand shock that is not offset by monetary policy results in a permanently higher price level but output returning to its potential."
  type: true-false
  answer: true
  explanation: "True. The long-run result is the classic AS-AD prediction: AD shifting right raises output temporarily (short run, sticky prices), but as prices fully adjust, the economy returns to potential output (long-run aggregate supply is vertical at potential). The cost is a permanently higher price level. For a persistent shock, the inflation rate itself may be permanently higher, not just the price level."

- question: "A positive demand shock permanently reduces unemployment, because the increased output creates lasting new jobs."
  type: true-false
  answer: false
  explanation: "False. The unemployment reduction is temporary. Once unemployment falls below NAIRU, inflation accelerates. Rising inflation erodes the real purchasing power of the original demand stimulus — higher prices reduce real government spending, household purchasing power, and net exports — pushing output back toward potential and unemployment back toward NAIRU. The shock buys temporary employment gains at the cost of lasting inflation, not permanent employment gains."

- question: "Explain why a positive demand shock raises output in the short run but results only in higher inflation in the long run."
  type: short-answer
  answer: "In the short run, wages and prices are sticky — contracts and menu costs prevent immediate price increases, so firms respond to higher demand by increasing production. Output rises above potential. Over time, the tight labor market (unemployment below NAIRU) gives workers bargaining power to push wages up. Higher wages raise firms' costs, which they pass through as higher prices. As the price level rises, real demand falls back toward potential and output returns to its sustainable level. The lasting result is a higher price level, not higher real output."
  explanation: "The short-run/long-run distinction is about speed of price adjustment. In the short run, quantity adjusts to demand changes because prices are sticky. In the long run, prices fully adjust and quantity returns to potential. Understanding this is the foundation of AS-AD analysis and the Phillips curve."
```

## Explainer

A **demand shock** is anything that shifts the aggregate demand for goods and services in the economy — a burst of consumer confidence, a fiscal stimulus package, a surge in export demand, or a sharp rise in business investment. From your study of aggregate demand and the expenditure approach, you know that AD is the sum of consumption, investment, government spending, and net exports. When any of these components rises unexpectedly and persistently, the economy faces a rightward shift in the AD curve. The question is what happens to output and inflation in response — and the answer depends critically on whether we are looking at the short run or the long run.

In the **short run**, wages and prices are sticky: workers have nominal wage contracts, firms have menu costs, and adjustment takes time. When demand rises, firms cannot immediately raise prices to clear the market, so they respond by increasing production. Output rises above its **potential** level — the level consistent with normal capacity utilization and the **NAIRU** (the unemployment rate at which inflation is stable). Okun's Law, which you have already studied, tells you what this output gap implies: output above potential means unemployment falls below NAIRU. Firms are hiring more workers than their "natural" level, and the economy is running hot.

The labor market tightening then triggers the inflation dynamic. When unemployment falls below NAIRU, workers gain bargaining power and push for higher wages. Firms facing higher labor costs pass them through in higher output prices. This is the **wage-price spiral** — wages chase prices, prices chase wages — and it is the channel through which a demand shock that initially only raised output eventually raises inflation as well. The **Phillips curve** (which you are building toward) formalizes this relationship: inflation rises when unemployment falls below NAIRU by an amount proportional to the gap. Crucially, this process takes time — typically one to two years after the initial shock — which is why monetary policy acts with long and variable lags.

In the **long run**, markets fully adjust. The economy cannot sustainably produce above potential — capital depreciates, workers demand rest, and the supply of productive inputs is ultimately bounded. As inflation rises, it erodes the real purchasing power of the original demand stimulus: higher prices reduce the real value of government spending, household purchasing power, and net exports. AD shifts back toward potential output. The long-run result of a permanent positive demand shock that goes unaddressed by policy is: output returns to potential, but **the price level is permanently higher** (or, for a persistent shock, the **inflation rate** is permanently higher). The demand shock bought temporary output gains at the cost of lasting inflation — the classic short-run/long-run tradeoff at the heart of macroeconomic stabilization policy.
