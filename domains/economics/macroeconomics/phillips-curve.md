---
id: phillips-curve
title: The Phillips Curve
domain: economics
course: macroeconomics
prerequisites:
- id: as-ad-model
  type: hard
- id: types-of-unemployment
  type: hard
- id: inflation-and-price-level
  type: hard
- id: quantity-theory-of-money
  type: soft
- id: scatterplots-and-correlation
  type: soft
builds-toward: []
tags:
- Phillips-curve
- inflation-unemployment
- NAIRU
- stagflation
- expectations
stage: abstract-reasoning
status: validated
---
# The Phillips Curve

## Core Idea
The Phillips curve depicts an empirical inverse relationship between inflation and unemployment: when unemployment is low, wage and price pressures are high, and vice versa. In the 1960s this appeared to offer policymakers a stable trade-off. The stagflation of the 1970s — high inflation and high unemployment simultaneously — challenged this view. Friedman and Phelps argued the short-run Phillips curve shifts with expected inflation, so there is no long-run trade-off at any unemployment below the natural rate; the long-run Phillips curve is vertical. Modern variants incorporate supply shocks and inflation expectations anchoring by central banks.

## How It's Best Learned
Plot US inflation and unemployment data from 1960–2023 and observe the breakdown of the stable trade-off. Trace how the curve shifted up in the 1970s as expectations became unanchored, and back down after Volcker's disinflation in 1981–1983.

## Common Misconceptions
- The original Phillips curve was derived from wage data, not price data; the inflation-unemployment version came later.
- The long-run vertical curve does not say policy cannot affect unemployment temporarily, only that sustained low unemployment below the natural rate generates accelerating inflation.
- The 2010s (low unemployment, low inflation) suggested a flatter curve, challenging traditional NAIRU estimates.

## Questions

```yaml
- question: "According to the expectations-augmented Phillips curve, what is the long-run outcome when a central bank persistently tries to hold unemployment below the natural rate?"
  type: multiple-choice
  options: ["Unemployment permanently stays below the natural rate with inflation stabilizing at a higher level", "Unemployment falls in the short run but returns to the natural rate as inflation expectations rise, requiring ever-higher inflation to sustain the gap", "Inflation falls because a tighter labor market raises productivity", "The natural rate of unemployment gradually decreases to match the lower unemployment target"]
  answer: 1
  explanation: "In the short run, surprise inflation can reduce real wages and stimulate hiring, pushing unemployment below the natural rate. But workers and firms update their inflation expectations upward, shifting the short-run Phillips curve up. To maintain unemployment below the natural rate, the central bank must generate even higher surprise inflation — leading to accelerating inflation. Eventually the economy returns to the natural rate, but at a permanently higher inflation rate. This is the Friedman-Phelps result."

- question: "The long-run Phillips curve is downward-sloping, confirming that policymakers can permanently trade higher inflation for lower unemployment."
  type: true-false
  answer: false
  explanation: "The long-run Phillips curve is vertical at the natural rate of unemployment (NAIRU). Once inflation expectations fully adjust to any sustained monetary policy, the real wage and employment effects vanish. Lower unemployment is achievable only temporarily through *surprise* inflation; once expected, the inflation produces no employment benefit. Friedman and Phelps established this independently in 1968, and the 1970s stagflation provided striking empirical support."

- question: "Why did the stagflation of the 1970s constitute a challenge to the original Phillips curve framework?"
  type: short-answer
  answer: "The original Phillips curve implied that high inflation and high unemployment could not coexist — the trade-off ran in one direction. Stagflation — simultaneously high inflation and high unemployment — directly violated this prediction. The breakdown occurred because supply shocks (OPEC oil embargoes) shifted costs upward independently of demand, and because years of accommodative monetary policy had unanchored inflation expectations, shifting the short-run Phillips curve upward."
  explanation: "This episode drove macroeconomists to incorporate supply-side factors and inflation expectations explicitly into the framework. It also highlighted the policy danger of treating the Phillips curve as a stable menu of choices: by exploiting the trade-off, policymakers unanchored expectations and ended up with the worst of both worlds. The modern New Keynesian Phillips curve addresses this through forward-looking expectations and the role of central bank credibility."
```

## Explainer

You know from the AS-AD model that aggregate demand expansions can reduce unemployment in the short run, and from studying inflation that sustained excess demand generates price pressure. The Phillips curve makes this connection explicit and empirical: it describes the observed inverse relationship between the inflation rate and the unemployment rate. A.W. Phillips documented this pattern in UK wage data from 1861–1957, and the relationship was quickly extended to price inflation and generalized internationally. By the early 1960s, the curve appeared to offer policymakers a stable menu: accept more inflation to buy lower unemployment, or tighten policy to reduce inflation at the cost of higher unemployment.

The intellectual crisis came in the late 1960s, before the 1970s made it undeniable. Milton Friedman and Edmund Phelps independently argued in 1968 that the apparent trade-off was temporary and would collapse once expectations adjusted. Their argument: the short-run curve traces a relationship between *unexpected* inflation and unemployment. If the central bank tries to hold unemployment below the natural rate — the rate consistent with stable expectations — it must generate ongoing inflation surprises. But workers and firms learn and update their expectations. Once expected inflation rises, the short-run curve shifts up, returning unemployment to the natural rate. The only way to sustain low unemployment is to constantly outrun expectations with ever-higher inflation. In the long run, therefore, the only stable outcome is unemployment at the natural rate (NAIRU — Non-Accelerating Inflation Rate of Unemployment), at whatever inflation rate monetary policy chooses. This gives a vertical long-run Phillips curve.

The 1970s made this theory viscerally real. OPEC oil embargoes in 1973 and 1979 delivered adverse supply shocks — stagflation — that the original demand-side framework could not explain. Costs rose independently of demand, pushing up inflation while simultaneously raising unemployment. The short-run curve had shifted upward. Meanwhile, a decade of accommodative monetary policy had unanchored inflation expectations, making the situation self-reinforcing. The cure — Paul Volcker's sharp monetary tightening in 1979–1983 — deliberately raised unemployment sharply to wring out inflationary expectations, tracing a movement up-and-left along a new, lower short-run curve.

The modern version of the Phillips curve, embedded in New Keynesian models, is written as: π = π^e + α(y − y*) + supply shocks, where π^e is expected inflation (now typically forward-looking), y − y* is the output gap (or equivalently the negative of the unemployment gap), and supply shocks shift the curve directly. Central bank credibility plays a crucial role: if households and firms believe the central bank will maintain low inflation, their inflation expectations remain anchored near the target, and supply shocks produce less persistent inflation because expectations don't spiral upward.

The 2010s added a new empirical puzzle: US unemployment fell well below traditional NAIRU estimates with minimal inflation, suggesting the curve had flattened. Possible explanations include globalization dampening domestic wage pressure, the rise of temporary and gig employment, and anchored expectations doing heavy lifting. This ongoing debate illustrates why the Phillips curve remains one of the most contested empirical relationships in macroeconomics — the underlying logic is sound, but the precise shape, slope, and stability of the curve continue to evolve with the data.
