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
stage: formal-systems
status: validated
---

# Inflation Dynamics and Inflation Persistence

## Core Idea
Inflation is persistent because it depends on expected inflation plus a demand-supply gap: π = π^e + α(Y - Y*). When inflation has been high, expectations of future inflation rise, making it costly to reduce inflation because demand must fall significantly to reverse inflationary expectations. This inertia in inflation explains why central banks must act preemptively and why sudden inflation shocks have large real costs.

## Questions

```yaml
- question: "A large oil price shock pushes inflation from 2% to 7% and persists for two years. The oil price then falls back to its original level. According to the expectations-augmented Phillips curve, why might inflation not automatically return to 2%?"
  type: multiple-choice
  options:
    - "Oil prices have a permanent multiplier effect on the price level, locking in a new equilibrium permanently"
    - "If inflation expectations rose during those two years, the Phillips curve has shifted up, and inflation persists at the new expected level even at normal output"
    - "The economy must run above potential output long enough to reverse the original supply shock"
    - "Central banks cannot reduce inflation caused by supply shocks — only demand shocks are reversible"
  answer: 1
  explanation: "The key mechanism is the expectations channel. Once firms and workers experience two years of 7% inflation, they revise their expectations upward. In the equation π = π^e + α(Y − Y*), if π^e rises to 7%, then even when Y = Y* (output at potential, no demand pressure), actual inflation settles at 7% — not 2%. The original oil shock is gone, but it has left its mark in shifted expectations. Returning to 2% requires driving Y below Y* (a recession) until price-setters revise their forecasts back down. The supply shock caused the initial rise; expectations cause the persistence."

- question: "Why did the Volcker disinflation (1979–82) require sustained high unemployment rather than simply announcing a new 2% inflation target?"
  type: multiple-choice
  options:
    - "The Fed lacked legal authority to announce inflation targets, so only unemployment could signal policy intent"
    - "Unemployment is the only instrument available to the Federal Reserve under the Federal Reserve Act"
    - "Inflation expectations had become anchored at high levels; only a demonstrated period of below-potential output would convince price-setters to revise their forecasts downward"
    - "The 2% target was technically unachievable without first achieving zero unemployment"
  answer: 2
  explanation: "By 1979, inflation expectations were entrenched at 6–10% because the Fed had repeatedly tolerated high inflation. A mere announcement of a 2% target was not credible — price-setters had learned to distrust such promises. The only way to re-anchor expectations was to demonstrate commitment through costly action: driving unemployment to nearly 11% and holding it there for years showed that the Fed was willing to bear real economic pain to achieve price stability. Once firms and workers observed sustained low inflation over time, they revised their forecasts downward, re-anchoring expectations. The announcement alone couldn't do this; the prolonged recession could."

- question: "In the expectations-augmented Phillips curve, if expected inflation rises, inflation can remain elevated even when output returns to its potential level."
  type: true-false
  answer: true
  explanation: "This follows directly from π = π^e + α(Y − Y*). When Y = Y* (output gap = 0), actual inflation equals expected inflation: π = π^e. If expected inflation is 7%, actual inflation is 7% at potential output — there is no automatic return to 2%. The output gap term α(Y − Y*) captures demand pressure, but it is zero when output is at potential. Only a negative output gap (Y < Y*) can push actual inflation below expected inflation and thereby create the conditions for expectations to revise downward."

- question: "Once the supply shock that caused a surge in inflation has passed, inflation will return to its previous level even if the central bank does hardly anything."
  type: true-false
  answer: false
  explanation: "This is the core misconception that inflation persistence contradicts. If price-setters have updated their inflation expectations upward during the inflationary episode, those expectations persist even after the original shock passes. Removing the shock eliminates one source of upward pressure, but it does not reverse the expectation shift. Actual inflation remains elevated at the new expected level until the central bank actively drives output below potential — accepting a recession — to force expectations back down. Doing nothing after a shock can lock in permanently higher inflation."

- question: "Why does the expectations-augmented Phillips curve imply that fighting entrenched inflation is more costly than preventing inflation from becoming entrenched in the first place?"
  type: short-answer
  answer: "Once expectations become unanchored — revised upward from the 2% target — every percentage point of expected inflation that must be reversed requires driving output below potential by enough to force actual inflation below expected inflation for long enough to shift forecasts back down. The higher and more entrenched expectations are, the deeper and longer the required recession. Preventing entrenchment (by tightening early, before expectations move) requires only a modest demand restriction to cap the initial inflation rise. The asymmetry is: an ounce of prevention requires a small negative output gap; a pound of cure requires a large sustained recession. Volcker's disinflation — nearly 11% unemployment for years — quantifies the cure; proactive early tightening represents the prevention."
  explanation: "This asymmetry is why central banks with credible inflation targets tend to raise rates preemptively when inflation threatens to exceed target, rather than waiting. The logic is not that early tightening is costless — it is that the cost of late tightening grows exponentially with the degree of expectation drift. A 1% overshoot held for a few months is cheap to reverse; a 5% overshoot held for two years is the Volcker scenario."
```

## Explainer

From the Phillips curve, you know there is a short-run tradeoff between inflation and unemployment: when the economy runs hot (output above potential, unemployment below natural rate), inflation tends to rise. But a one-time demand boom should produce a one-time burst of higher inflation, not a sustained elevated path. Why does inflation, once it rises, tend to stay elevated for years? The answer is **persistence**: inflation today feeds into inflation tomorrow through expectations.

The core mechanism is the **expectations-augmented Phillips curve**: π = π^e + α(Y − Y*) + ε, where π is actual inflation, π^e is expected inflation, (Y − Y*) is the output gap (actual minus potential output), and ε captures supply shocks. Notice what happens when inflation rises above target. Firms and workers update their expectations upward — after all, they just observed higher inflation, and they expect it to continue. This increase in π^e shifts the entire Phillips curve up: now even at normal output levels (Y = Y*), inflation settles at the new higher level of expected inflation rather than returning to target. The inflation shock has been absorbed into expectations, and expectations perpetuate the inflation.

The policy implication is deeply asymmetric: **it is much easier to let inflation expectations become unanchored than to re-anchor them**. Suppose a supply shock pushes inflation from 2% to 6%. If the central bank tolerates this for long enough, price-setters revise their inflation forecasts to 6%. Now expected inflation is 6%, and keeping actual inflation at 6% requires no special demand pressure — it is the new steady state. To bring inflation back to 2%, the central bank must push the output gap sharply negative (Y << Y*), creating a recession, until 2% inflation becomes credible again and expectations re-anchor. The greater the initial expectation drift, the deeper the required recession. This is the mechanism Volcker exploited in 1979–82: only by driving unemployment to nearly 11% and holding it there could the Fed convince the public that 2% inflation, not 6–10%, was the new permanent regime.

This is why central banks act **preemptively** rather than reactively. A central bank that waits until inflation expectations visibly drift before tightening will face a much larger and more painful disinflation than one that raises rates early, before expectations shift. The cost of fighting entrenched inflation — measured in years of below-potential output and elevated unemployment — is far higher than the cost of preventing it from becoming entrenched in the first place. **Inflation inertia** is not just a theoretical abstraction; it is the organizing fact of post-WWII monetary history.

## How It's Best Learned
Plot U.S. CPI inflation from 1965–1985 alongside the federal funds rate and the unemployment rate. Trace how inflation expectations became embedded after the 1973 and 1979 oil shocks, and how the Volcker disinflation required sustained high unemployment to reverse them. Then compare to the 2021–23 inflation episode to see whether the pattern repeated.
