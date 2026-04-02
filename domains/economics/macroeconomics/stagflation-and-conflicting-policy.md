---
id: stagflation-and-conflicting-policy
title: Stagflation and Policy Conflict
domain: economics
course: macroeconomics
prerequisites:
- id: supply-side-shocks-and-stagflation
  type: hard
- id: expectations-augmented-phillips-curve-modern
  type: hard
- id: supply-shocks-aggregate-disruptions
  type: soft
tags:
- stagflation
- policy
- tradeoff
stage: expert
status: validated
---
# Stagflation and Policy Conflict

## Core Idea
Stagflation—the simultaneous occurrence of high inflation and high unemployment—creates a policy dilemma: expansionary policy reduces unemployment but raises inflation, while contractionary policy reduces inflation but increases unemployment. Successfully managing stagflation requires either eliminating the supply shock, shifting expectations (credibility of inflation targeting), or accepting a difficult tradeoff in the near term.

## Questions

```yaml
- question: "A negative oil supply shock hits the economy, pushing inflation to 8% and unemployment to 9%. The central bank responds with expansionary monetary policy to reduce unemployment. According to the expectations-augmented Phillips curve framework, what is the most likely consequence?"
  type: multiple-choice
  options:
    - "Both unemployment and inflation fall as aggregate demand is restored"
    - "Unemployment falls in the short run, but inflation rises further and expectations may become entrenched at a higher level"
    - "Inflation falls because the expanded money supply dilutes the price impact of the oil shock"
    - "The policy has no effect because supply shocks are immune to demand-side interventions"
  answer: 1
  explanation: "Expansionary policy can reduce unemployment by boosting aggregate demand, but it does so by validating the higher price level. Firms and workers observing persistently high inflation update their expectations upward, shifting the Phillips curve further outward. This is exactly what happened in the 1970s: accommodating the supply shock kept unemployment lower in the short run but entrenched inflation expectations, producing a wage-price spiral. Option A is wrong because the supply shock has not been removed — only demand has been boosted, which helps unemployment but worsens the inflation dimension."

- question: "What makes stagflation uniquely difficult to address compared to a standard recession or a standard inflation episode?"
  type: multiple-choice
  options:
    - "Stagflation occurs so rarely that policymakers lack experience with the appropriate tools"
    - "Both fiscal and monetary policy become ineffective during stagflation due to liquidity traps"
    - "Each available policy instrument improves one problem (inflation or unemployment) while worsening the other, so there is no instrument that addresses both simultaneously"
    - "Stagflation can only be resolved by eliminating the supply shock, which is outside policymakers' control"
  answer: 2
  explanation: "In a standard recession, expansionary policy is unambiguously appropriate. In a standard inflation episode, contractionary policy is appropriate. Stagflation moves the Phillips curve outward — higher inflation and higher unemployment coexist. Expansionary policy reduces unemployment but raises inflation; contractionary policy reduces inflation but deepens the recession. There is a genuine instrument-problem: no single demand-side tool addresses both symptoms. While eliminating the supply shock helps, the policy dilemma exists even if the shock is permanent."

- question: "A central bank with a strong track record of meeting its inflation target faces a lower sacrifice ratio (less unemployment per point of inflation reduction) than a central bank with a weak track record."
  type: true-false
  answer: true
  explanation: "The sacrifice ratio measures the cumulative unemployment cost of reducing inflation by one percentage point. When a central bank has credibility — demonstrated commitment to an inflation target — firms and workers set wages and prices based on the expected low inflation, and the short-run Phillips curve shifts inward without requiring a prolonged recession. Low sacrifice ratios are the payoff of credibility built over time, which is why central bank independence, transparency, and consistent communication are policy priorities. The Volcker disinflation had a high sacrifice ratio partly because credibility had to be established from scratch."

- question: "During stagflation, contractionary monetary policy is the dominant policy tool because tightening reduces both unemployment and inflation simultaneously."
  type: true-false
  answer: false
  explanation: "This is exactly the misconception stagflation exposes. Contractionary policy reduces inflation by cooling aggregate demand, but it does so at the cost of higher unemployment — it deepens the recessionary dimension of stagflation. There is no tool that reduces both simultaneously when the economy faces a negative supply shock. The Volcker disinflation of 1979–82 chose contractionary policy to fight inflation, and it worked — but it produced the deepest US recession since the Great Depression. The policy tradeoff, not a free lunch, is the defining feature of stagflation."

- question: "Why does stagflation create a 'policy dilemma' that a normal recession or normal inflation episode does not, and how does central bank credibility help resolve it over time?"
  type: short-answer
  answer: "In a normal recession, expansionary policy is clearly appropriate — it reduces unemployment without raising inflation above target. In a normal inflation episode, contractionary policy is clearly appropriate — it reduces inflation. Stagflation arises from a negative supply shock that shifts the short-run aggregate supply curve leftward, simultaneously raising prices and reducing output. This moves the economy to a point where both inflation and unemployment are elevated, and the Phillips curve has shifted outward. Any demand-side response trades off: expansionary policy helps unemployment but worsens inflation; contractionary policy helps inflation but worsens unemployment. Credibility resolves the long-run dilemma by anchoring expectations: if firms and workers believe inflation will return to target, they set wages and prices accordingly, and the Phillips curve shifts back inward without requiring a protracted recession."
  explanation: "This explains why modern central banks invest so heavily in communication and institutional independence — the expectation of policy is itself a policy tool. A credible central bank can achieve disinflation with less unemployment (lower sacrifice ratio) because expectations do part of the adjustment work. Without credibility, a central bank must impose deep recession to 'prove' its commitment, as the Volcker Fed demonstrated."
```

## Explainer

To understand why stagflation is so politically painful, recall what you learned about supply-side shocks. A negative supply shock — say, a sudden doubling of oil prices — does two things at once: it raises production costs across the economy (pushing inflation up) and it reduces the capacity to produce output (pushing unemployment up). On the aggregate supply-aggregate demand diagram, the short-run aggregate supply curve shifts leftward, landing the economy at a point with both higher prices and lower output. This is the stagflation corner: the two standard macroeconomic ills occurring simultaneously.

Now invoke the **expectations-augmented Phillips curve**. Under normal conditions, the Phillips curve implies a tradeoff: accept more inflation to get lower unemployment, or tighten policy to bring inflation down at the cost of higher unemployment. Stagflation breaks this tradeoff by moving the entire curve outward — higher inflation coexists with higher unemployment at every point. Policymakers face a genuine dilemma. If they respond to the high unemployment with expansionary fiscal or monetary policy, they validate the higher prices and risk accelerating inflation. If they respond to the high inflation with contractionary policy, they deepen the recession. There is no policy instrument that addresses both problems simultaneously; each tool helps on one dimension and worsens the other.

The 1970s oil shocks illustrated this conflict starkly. The OPEC oil embargoes created stagflation in the United States and Europe. Policymakers who tried to accommodate the supply shock by expanding money supply kept unemployment lower in the short run, but inflation expectations became entrenched — workers and firms began setting wages and prices based on anticipated high inflation, shifting the Phillips curve further outward. The result was a **wage-price spiral** in which inflation remained elevated long after the original shock. By contrast, the Volcker disinflation of 1979–1982 took the contractionary route: sharply raising interest rates crushed inflation at the cost of a deep recession, only gradually reanchoring expectations at lower levels.

The key insight is that long-run resolution depends on expectations management more than on the immediate policy response. A central bank with **credibility** — a demonstrated commitment to an inflation target — can reduce the sacrifice ratio (the unemployment cost of reducing inflation by one percentage point). When firms and workers believe that inflation will return to target, they set prices and wages accordingly, and the short-run Phillips curve shifts back inward without requiring a prolonged recession. This is why modern central banks invest heavily in communication, transparency, and institutional independence: the expectation of policy is itself a tool. Stagflation reveals that macroeconomic stability is a reputation problem as much as an instrument-selection problem.
