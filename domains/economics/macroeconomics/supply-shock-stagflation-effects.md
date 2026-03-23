---
id: supply-shock-stagflation-effects
title: Supply Shocks and Stagflation
domain: economics
course: macroeconomics
prerequisites:
- id: as-ad-model
  type: hard
- id: wage-price-dynamics-and-inflation
  type: hard
builds-toward:
- phillips-curve-new-keynesian
tags:
- supply-shock
- stagflation
- inflation
- unemployment
- oil-shocks
stage: advanced
status: validated
---

# Supply Shocks and Stagflation

## Core Idea
A negative supply shock (oil spike, disaster, productivity decline) reduces aggregate supply, shifting AS curve left. Output falls and price level rises simultaneously—stagflation. Central bank faces a dilemma: tighten to reduce inflation (worsening recession) or accommodate (risking accelerating inflation).

## How It's Best Learned
Use 1973-74 oil shock case study: OPEC raised prices, raising production costs globally. AS curve shifts left, pushing up prices and reducing output. Compare policy responses and consequences.

## Common Misconceptions
- Assuming supply shocks are rare.
- Treating all supply shocks symmetrically.
- Forgetting responses depend on expectations.

## Questions

```yaml
- question: "In 1973, OPEC quadrupled oil prices, raising production costs across nearly every industry. A student argues: 'higher costs reduced output, so firms had less to sell, which lowered prices as demand fell.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — this is the correct description of a cost-driven price decline"
    - "Oil was not a significant enough input to affect the aggregate economy"
    - "A negative supply shock shifts the SRAS curve left, raising the price level while reducing output — the opposite of the student's prediction"
    - "The student confused a demand-side shock with a supply-side shock, but both produce the same outcome"
  answer: 2
  explanation: "The student reversed the price direction. In the AS-AD model, a leftward shift of the short-run aggregate supply curve moves the equilibrium to a new intersection that is higher on the price axis (inflation) and lower on the output axis (recession). This is stagflation — simultaneous rising prices and falling output. The student's error is thinking that output declines lower prices; in a supply shock, the price level rises precisely because the supply schedule itself shifted inward, reflecting higher production costs at every output level."

- question: "Why does a negative supply shock create a worse policy dilemma than a negative demand shock?"
  type: multiple-choice
  options:
    - "Supply shocks are always larger in magnitude than demand shocks, making them harder to offset"
    - "Supply shocks affect the financial sector directly, which demand policy cannot reach"
    - "Stimulating demand to fight the recession worsens inflation; tightening to fight inflation worsens the recession — no policy simultaneously restores both output and price stability"
    - "Supply shocks affect the long-run aggregate supply curve, which monetary policy is powerless to shift"
  answer: 2
  explanation: "A demand shock moves output and prices in the same direction, so a single policy response can offset both: a negative demand shock lowers both output and prices, so expansionary policy restores both. A supply shock moves them in opposite directions (output falls, prices rise), creating a genuine dilemma. Tightening monetary policy shifts AD left — it counters inflation but deepens the recession. Easing shifts AD right — it supports output but validates higher prices. The central bank must choose between two evils rather than finding a clean fix."

- question: "A central bank that responds to a negative supply shock by expanding money supply can simultaneously restore the original output level and the original price level."
  type: true-false
  answer: false
  explanation: "This is the core policy dilemma of stagflation. When SRAS shifts left, the new equilibrium has lower output and higher prices. Accommodative monetary policy (expanding money supply) shifts AD right, which can restore output — but does so by validating and potentially entrenching the higher price level, risking further inflation. Tightening restores the price level at the cost of deeper recession. No single AD shift returns the economy to both the original output and original price simultaneously — that would require shifting SRAS back to its original position, which requires reversing the underlying cost shock."

- question: "If workers expect prices to keep rising after a negative supply shock and demand higher nominal wages, this can trigger a wage-price spiral that shifts the SRAS curve further left."
  type: true-false
  answer: true
  explanation: "Wage-price dynamics are a key amplifier of supply shocks. If a supply shock raises prices and workers respond by demanding higher nominal wages (to preserve real purchasing power), firms face even higher production costs — shifting SRAS left again. Higher prices → higher wage demands → higher costs → higher prices: a self-reinforcing spiral. This is exactly what worsened the 1970s stagflation. A central bank that credibly commits to fighting inflation can break this loop by anchoring expectations, preventing the secondary wage-price feedback even if it cannot avoid the initial output loss."

- question: "Explain why a negative supply shock creates a policy dilemma that a negative demand shock does not."
  type: short-answer
  answer: "A negative demand shock moves output and prices in the same direction (both fall), so a single expansionary policy can address both simultaneously — boosting AD restores output and reverses the price decline. A negative supply shock moves them in opposite directions: output falls but prices rise (stagflation). Any policy response faces a trade-off. Expanding monetary policy (shifting AD right) supports output but pushes the already-elevated price level higher, risking entrenched inflation. Tightening (shifting AD left) reduces inflation but worsens the recession. There is no AD shift that cleanly returns both output and the price level to their pre-shock values."
  explanation: "The fundamental asymmetry is directional: demand shocks align the effects on output and prices, so policy can simultaneously counteract both. Supply shocks misalign them. The only way to fully reverse a supply shock without a policy dilemma is to reverse the underlying cost increase — which is outside the reach of conventional monetary or fiscal policy. This is why supply shocks like the 1973 oil embargo produced a decade of difficult tradeoffs between inflation and unemployment, culminating in the painful recession of the early 1980s needed to re-anchor expectations."
```

## Explainer

To understand supply shocks, start from the AS-AD model you already know. The aggregate demand curve slopes downward (higher price levels reduce real purchasing power), and the short-run aggregate supply (SRAS) curve slopes upward (higher prices draw out more production). Their intersection determines equilibrium output and the price level. A **negative supply shock** — an abrupt increase in production costs — shifts the entire SRAS curve to the left. Think of the 1973 OPEC oil embargo: petroleum was an input to nearly every industry, so when its price quadrupled, the cost of producing any given level of output rose sharply. The whole supply schedule shifted inward.

The key consequence is that a leftward AS shift produces a move to a *new* intersection that is simultaneously higher on the price axis and lower on the output axis. This is **stagflation**: stagnation (falling output, rising unemployment) combined with inflation (rising prices). This combination was deeply puzzling to economists trained on the Phillips curve, which implied that inflation and unemployment move in opposite directions. Supply shocks break that relationship by shifting the economy in a direction the Phillips curve framework doesn't anticipate.

This creates a genuine **policy dilemma** for the central bank. Tightening monetary policy (raising interest rates, reducing money supply) shifts aggregate demand left, which would counteract the inflation — but it also further reduces output and pushes unemployment higher. Accommodative policy (lowering rates, expanding money supply) shifts aggregate demand right, supporting output — but validates the higher price level and risks entrenching inflationary expectations. There is no policy response that cleanly restores both the original output level and the original price level simultaneously, which is why supply shocks force painful choices.

The severity of outcomes also depends on **wage-price dynamics**. If workers expect prices to keep rising, they demand nominal wage increases. If those are granted, firms face even higher costs, shifting AS left again — a wage-price spiral. This is why inflation expectations matter so much: a central bank that credibly commits to fighting inflation may be able to prevent the secondary wage-price feedback, even if the initial shock still causes a recession. The 1970s stagflation worsened because expectations became unanchored; the early 1980s recovery required a severe recession to re-anchor them. Understanding supply shocks therefore requires integrating the AS-AD framework with the expectations dynamics you'll encounter in the New Keynesian Phillips curve.
