---
id: inflation-expectations-formation
title: Inflation Expectations and Expectation Formation
domain: economics
course: macroeconomics
prerequisites:
- id: expectation-formation-mechanisms
  type: hard
builds-toward:
- inflation-dynamics-and-persistence
- phillips-curve-new-keynesian
tags:
- expectations
- inflation
- behavioral
stage: advanced
status: draft
---

# Inflation Expectations and Expectation Formation

## Core Idea
Agents form expectations about future inflation through different mechanisms: adaptive expectations (π^e = π_{-1}), rational expectations (π^e = E[π|information]), or survey-based expectations. Actual inflation depends partly on expected inflation because wage and price setters incorporate expectations into their decisions. When expected inflation is high, it becomes embedded in wages and prices, making actual inflation harder to reverse.

## Explainer

From your study of expectation formation mechanisms, you know that agents must forecast the future when making decisions today. For inflation specifically, this feedback loop is unusually consequential: unlike forecasting tomorrow's weather (where expectations don't affect the weather), inflation expectations *cause* inflation. This self-referential quality makes inflation expectations one of the most important variables in macroeconomics, and understanding how they form is essential to understanding why inflation is so hard to control.

The mechanism is straightforward. Workers negotiating wages ask: what will prices be next year? If they expect 5% inflation, they demand wages 5% higher just to maintain real purchasing power. Firms setting prices ask: what will my costs be next year? If they expect wages (their main input cost) to rise 5%, they raise prices 5% pre-emptively. The result: everyone raising prices by 5% *because* they expected 5% inflation produces exactly 5% inflation — the expectation was self-fulfilling. This is why **expected inflation** appears directly in the New Keynesian Phillips Curve: actual inflation = expected inflation + output-gap term + supply shock. Strip out the expectation component and you cannot account for why inflation persists even when economic slack should be pulling it down.

**Adaptive expectations** model agents as backward-looking: this year's forecast is simply last year's realization (π^e = π_{t−1}). This is computationally simple and plausible for routine periods, but it means agents are always one period behind. In the 1970s, when oil shocks repeatedly surprised adaptive forecasters, the hypothesis came under heavy criticism — it predicted systematic, exploitable errors. **Rational expectations** (RE) replaced it with the more demanding assumption that agents use all available information and form unbiased forecasts on average (π^e = E[π | Ω_t], where Ω_t is the information set). RE does not require that forecasts are perfect — only that errors are random and not predictable from available information. The implication is radical: systematic monetary policy has no real effects because agents anticipate and undo it.

In practice, survey data and financial market instruments (TIPS breakevens, inflation swaps) reveal that expectations fall somewhere between these poles. They are forward-looking but not perfectly rational, slow to update to new information, and heavily influenced by recent experience — exactly what you'd expect when forming expectations is costly and agents use simple heuristics. The critical policy implication is **anchoring**: a central bank whose inflation target is credible keeps long-run inflation expectations fixed even during short-run deviations. When expectations become "unanchored" — when the public stops believing the central bank will achieve its target — inflation becomes much harder to control because the self-fulfilling component of the Phillips Curve activates at scale. The Federal Reserve's aggressive rate hikes in 2022–2023 were precisely a campaign to keep expectations anchored before a 1970s-style wage-price spiral could take hold.
