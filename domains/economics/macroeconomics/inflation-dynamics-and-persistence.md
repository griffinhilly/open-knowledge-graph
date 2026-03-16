---
id: inflation-dynamics-and-persistence
title: Inflation Dynamics and Inflation Persistence
domain: economics
course: macroeconomics
prerequisites:
- id: inflation-and-price-level
  type: hard
- id: phillips-curve
  type: soft
builds-toward:
- phillips-curve-new-keynesian
- natural-rate-of-unemployment-nairu
tags:
- inflation
- monetary-policy
- dynamics
stage: abstract-reasoning
status: draft
---

# Inflation Dynamics and Inflation Persistence

## Core Idea
Inflation is persistent because it depends on expected inflation plus a demand-supply gap: π = π^e + α(Y - Y*). When inflation has been high, expectations of future inflation rise, making it costly to reduce inflation because demand must fall significantly to reverse inflationary expectations. This inertia in inflation explains why central banks must act preemptively and why sudden inflation shocks have large real costs.

## Explainer

From the Phillips curve, you know there is a short-run tradeoff between inflation and unemployment: when the economy runs hot (output above potential, unemployment below natural rate), inflation tends to rise. But a one-time demand boom should produce a one-time burst of higher inflation, not a sustained elevated path. Why does inflation, once it rises, tend to stay elevated for years? The answer is **persistence**: inflation today feeds into inflation tomorrow through expectations.

The core mechanism is the **expectations-augmented Phillips curve**: π = π^e + α(Y − Y*) + ε, where π is actual inflation, π^e is expected inflation, (Y − Y*) is the output gap (actual minus potential output), and ε captures supply shocks. Notice what happens when inflation rises above target. Firms and workers update their expectations upward — after all, they just observed higher inflation, and they expect it to continue. This increase in π^e shifts the entire Phillips curve up: now even at normal output levels (Y = Y*), inflation settles at the new higher level of expected inflation rather than returning to target. The inflation shock has been absorbed into expectations, and expectations perpetuate the inflation.

The policy implication is deeply asymmetric: **it is much easier to let inflation expectations become unanchored than to re-anchor them**. Suppose a supply shock pushes inflation from 2% to 6%. If the central bank tolerates this for long enough, price-setters revise their inflation forecasts to 6%. Now expected inflation is 6%, and keeping actual inflation at 6% requires no special demand pressure — it is the new steady state. To bring inflation back to 2%, the central bank must push the output gap sharply negative (Y << Y*), creating a recession, until 2% inflation becomes credible again and expectations re-anchor. The greater the initial expectation drift, the deeper the required recession. This is the mechanism Volcker exploited in 1979–82: only by driving unemployment to nearly 11% and holding it there could the Fed convince the public that 2% inflation, not 6–10%, was the new permanent regime.

This is why central banks act **preemptively** rather than reactively. A central bank that waits until inflation expectations visibly drift before tightening will face a much larger and more painful disinflation than one that raises rates early, before expectations shift. The cost of fighting entrenched inflation — measured in years of below-potential output and elevated unemployment — is far higher than the cost of preventing it from becoming entrenched in the first place. **Inflation inertia** is not just a theoretical abstraction; it is the organizing fact of post-WWII monetary history.

## How It's Best Learned
Plot U.S. CPI inflation from 1965–1985 alongside the federal funds rate and the unemployment rate. Trace how inflation expectations became embedded after the 1973 and 1979 oil shocks, and how the Volcker disinflation required sustained high unemployment to reverse them. Then compare to the 2021–23 inflation episode to see whether the pattern repeated.
