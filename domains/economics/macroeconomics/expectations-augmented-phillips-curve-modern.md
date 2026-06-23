---
id: expectations-augmented-phillips-curve-modern
title: The Expectations-Augmented Phillips Curve
domain: economics
course: macroeconomics
prerequisites:
- id: phillips-curve
  type: hard
- id: inflation-expectations-formation
  type: hard
- id: supply-shock-stagflation-effects
  type: soft
- id: nairu-natural-unemployment-rate
  type: hard
builds-toward:
- stagflation-and-conflicting-policy
tags:
- phillips-curve
- inflation
- unemployment
stage: expert
status: validated
---
# The Expectations-Augmented Phillips Curve

## Core Idea
The modern Phillips curve relates inflation to unemployment and inflation expectations: inflation = expected inflation + a function of the output gap. Unlike the original Phillips curve, it accounts for the fact that inflation expectations can shift the entire relationship. The expectations term explains stagflation and why policymakers must manage expectations to control inflation without accepting high unemployment.

## Questions

```yaml
- question: "A central bank repeatedly stimulates the economy to keep unemployment below the natural rate for several consecutive years. According to the expectations-augmented Phillips curve, what is the long-run outcome?"
  type: multiple-choice
  options:
    - "Unemployment stays below the natural rate permanently, because the real economy adapts to the new equilibrium"
    - "Inflation stabilizes at a higher but fixed level, as workers accept the new nominal wage growth"
    - "Both inflation and unemployment rise as workers revise their inflation expectations upward, shifting the Phillips curve up"
    - "The output gap closes automatically as the economy self-corrects, with no lasting inflation impact"
  answer: 2
  explanation: "The expectations-augmented model predicts that holding unemployment below the natural rate requires generating inflation faster than agents expect. Initially this works — the economy is surprised. But workers and firms observe actual inflation and revise πᵉ upward. Each upward revision shifts the entire Phillips curve upward, so maintaining the same low unemployment requires ever-higher inflation. Eventually the policy produces higher inflation without any lasting unemployment gain. Option B (stable higher inflation) would only hold if expectations somehow stopped adapting — which contradicts the model's core premise."

- question: "According to the expectations-augmented Phillips curve, what is true when actual unemployment exactly equals the natural rate of unemployment?"
  type: multiple-choice
  options:
    - "Inflation is zero, because the output gap is closed and there is no inflationary pressure"
    - "Actual inflation equals expected inflation — there is no surprise inflation and no inflation-unemployment tradeoff"
    - "The Phillips curve is vertical, meaning any inflation rate is consistent with the natural rate of unemployment"
    - "The central bank can hold unemployment at the natural rate only by setting the inflation target to zero"
  answer: 1
  explanation: "The equation π = πᵉ + β(u* − u) + shocks shows that when u = u*, the term β(u* − u) = 0, and absent supply shocks, π = πᵉ. Actual inflation equals expected inflation: there is no inflationary surprise and the economy is in a steady state. The natural rate is called NAIRU — the non-accelerating inflation rate of unemployment — precisely because at this rate, inflation neither accelerates nor decelerates. Option A confuses 'no inflationary pressure above expectations' with 'zero inflation': you can have u = u* and stable 3% inflation if πᵉ = 3%."

- question: "The simultaneous rise of inflation and unemployment in the United States during the 1970s (stagflation) is consistent with the predictions of the expectations-augmented Phillips curve."
  type: true-false
  answer: true
  explanation: "Stagflation contradicted the original Phillips curve (which predicted a stable tradeoff), but the expectations-augmented model explains it precisely. After years of expansionary policy, workers revised inflation expectations upward, shifting the Phillips curve upward. Higher πᵉ meant the same unemployment rate was now associated with higher inflation — and attempts to reduce inflation by raising unemployment compounded the problem. Friedman and Phelps predicted this outcome in 1967–68, just before it occurred, providing dramatic validation of the framework."

- question: "A sufficiently credible central bank can permanently hold unemployment below the natural rate by committing to a fixed, predictable inflation target."
  type: true-false
  answer: false
  explanation: "No inflation target, however credible, can permanently hold unemployment below the natural rate. Any sustained unemployment gap (u < u*) generates inflation above expected inflation, causing workers to revise expectations upward, which shifts the curve up again. This process continues — accelerating inflation — until the gap closes. Credibility helps anchor expectations at the target rate, preventing unmooring, but it does not eliminate the natural rate constraint. The natural rate acts as an attractor; deviations require sustained inflationary surprise, and adaptive or rational agents eventually catch on."

- question: "Friedman and Phelps argued that workers care about real wages, not nominal wages. Why does this insight destroy the stable inflation-unemployment tradeoff implied by the original Phillips curve?"
  type: short-answer
  answer: "The original Phillips curve assumed workers would accept lower real wages during low unemployment, allowing firms to hire more and expand output. But if workers care about real wages — purchasing power — they will demand higher nominal wages to compensate once they notice inflation is eroding their pay. When workers correctly anticipate inflation and incorporate it into wage demands, the initial employment boost (from inflation reducing real wages) disappears. Expected inflation enters wage contracts, raising firms' costs and reducing employment, shifting the entire Phillips curve upward."
  explanation: "The key transition is from workers being 'fooled' by nominal wages (the original Phillips curve) to workers forming correct inflation expectations and defending real wages. Once expectations are fully flexible, the only way to hold unemployment below the natural rate is to keep generating inflation faster than people expect — a game that cannot be sustained indefinitely as expectations continuously catch up with reality."
```

## Explainer

You already know the original Phillips curve: the empirical observation that low unemployment tends to accompany high inflation, and vice versa, suggesting a stable policy tradeoff. The expectations-augmented version, developed by Milton Friedman and Edmund Phelps in the late 1960s — just before the data dramatically validated their theory — explains why that original tradeoff was an illusion. The key insight: workers and firms care about **real wages**, not nominal wages. When inflation rises, they will eventually demand higher nominal wages to keep pace. That adjustment process is what destroys the stable inflation-unemployment tradeoff.

The modern equation is: π = πᵉ + β(u* − u) + supply shocks. Here π is actual inflation, **πᵉ is expected inflation**, u is actual unemployment, u* is the natural rate, and the term β(u* − u) represents the effect of the output gap on inflation pressure. Read it in plain language: inflation today equals what people expected it would be, plus any pressure coming from unemployment being below or above the natural rate, plus supply shocks. If unemployment equals the natural rate (u = u*), inflation equals expected inflation exactly. There is no permanent tradeoff — the economy can only hold unemployment below the natural rate temporarily, while it generates surprise inflation that expectations have not yet caught up with.

The stagflation of the 1970s was the decisive empirical proof. Conventional Keynesian models predicted that higher inflation would buy lower unemployment. Instead, both rose simultaneously — unemployment climbed even as inflation accelerated. The expectations-augmented explanation: a decade of expansionary policy had pushed inflation consistently above earlier expectations, causing workers and firms to revise expectations upward. Each upward revision of πᵉ shifted the entire Phillips curve upward, so maintaining the same low unemployment required ever-higher inflation, and eventually not even that was enough. The policy lesson: you can exploit the unemployment-inflation tradeoff only temporarily, and only by generating inflation faster than people anticipate. Once expectations adapt, the curve shifts and the tradeoff disappears.

This reframing makes **expectations management** central to modern monetary policy. Under rational or adaptive expectations, if a central bank consistently targets 2% inflation and is credible, πᵉ anchors near 2%. Then the Phillips curve equation says that as long as unemployment stays near the natural rate and there are no supply shocks, inflation stays near 2% — automatically. A credible inflation target is a self-fulfilling equilibrium. Conversely, if credibility breaks down and expectations become unanchored (as happened in the 1970s), getting inflation back down requires accepting unemployment above the natural rate — a deliberate recession — to convince the public that inflation will fall. The Volcker disinflation of 1981–82 is the canonical case: the Fed raised rates sharply, unemployment hit 10%, but it successfully broke high inflation expectations, pulling the Phillips curve back down to a position where moderate inflation and acceptable unemployment could coexist.
