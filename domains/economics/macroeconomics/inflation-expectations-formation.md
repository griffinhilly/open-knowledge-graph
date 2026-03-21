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

## Questions

```yaml
- question: "Workers in a wage negotiation expect 5% inflation next year and successfully demand 5% wage increases to protect their real purchasing power. Firms, facing higher labor costs, raise their prices by 5% to protect margins. Demand conditions are moderate and there are no supply shocks. What happens to actual inflation?"
  type: multiple-choice
  options:
    - "Inflation remains low because there is no demand-pull or cost-push pressure from real economic conditions"
    - "Inflation rises toward 5% because the wage increases raised costs and firms passed them through — a self-fulfilling cycle"
    - "Inflation falls because higher wages reduce corporate profits, forcing firms to cut prices"
    - "Inflation depends only on the money supply; wage expectations have no independent effect"
  answer: 1
  explanation: "This is the self-fulfilling mechanism at the core of inflation dynamics. Workers expecting 5% inflation demand wages that are 5% higher. Higher wages raise production costs. Firms raise prices to protect margins. The expectation of 5% inflation generates 5% inflation even without any independent demand or supply shock. This is why expected inflation appears directly as a term in the New Keynesian Phillips Curve — it is not merely a forecast error correction, it is a causal force."

- question: "The U.S. Federal Reserve raised interest rates very aggressively in 2022–2023, even as supply-chain pressures began easing. Which concern best explains the urgency of these hikes?"
  type: multiple-choice
  options:
    - "The Fed was worried GDP growth was too fast and needed to be slowed independently of inflation"
    - "The Fed was preventing long-run inflation expectations from becoming unanchored, which would trigger a self-reinforcing wage-price spiral"
    - "The Fed was following adaptive expectations, mechanically updating policy based on past inflation realizations"
    - "The Taylor rule mechanically required these increases regardless of whether expectations were at risk"
  answer: 1
  explanation: "The primary concern was expectations anchoring. If workers and firms began to expect chronic high inflation — updating their long-run expectations upward — the self-fulfilling mechanism would kick in at scale: wages would rise, costs would rise, prices would rise, validating the expectations. This is the 1970s lesson. Acting aggressively early maintains central bank credibility and keeps long-run expectations fixed at the target, preventing the much harder task of breaking entrenched inflation expectations later."

- question: "Under rational expectations, a credible central bank announcement of a lower inflation target can reduce actual inflation before any interest rate changes take effect."
  type: true-false
  answer: true
  explanation: "Under rational expectations, agents use all available information to form forecasts. If a central bank credibly commits to a lower inflation target, workers and firms immediately incorporate this into their wage and price decisions — because they believe the bank will follow through with policy to achieve it. Expected inflation falls, and since expected inflation feeds directly into actual inflation through the wage-price mechanism, actual inflation declines without waiting for the full policy path to play out. Credibility is the mechanism that makes announcements themselves disinflationary."

- question: "Rational expectations means that economic agents correctly predict the future in every period, leaving no room for forecast errors."
  type: true-false
  answer: false
  explanation: "Rational expectations means forecasts are unbiased on average — agents use all available information efficiently and do not make systematic, predictable errors. But it does not mean perfect foresight. Inherently uncertain future events cannot be predicted exactly; random shocks always produce forecast errors. The key distinction is between random (unforeseeable) errors, which rational expectations allows, and systematic errors (e.g., always underestimating inflation), which rational expectations rules out. Adaptive expectations, by contrast, can produce systematic errors during trend changes."

- question: "Explain why inflation expectations are self-fulfilling. What does this imply for the importance of monetary policy credibility?"
  type: short-answer
  answer: "When workers expect inflation, they demand higher wages to maintain real purchasing power. When firms expect higher wages and input costs, they raise prices pre-emptively. Both actions cause the inflation that was expected — the expectation produces the outcome it anticipated. This self-fulfilling property means a central bank whose inflation target is credible has a powerful advantage: anchored expectations keep actual inflation near the target even during temporary shocks, because wages and prices are not reset upward pre-emptively. A bank that loses credibility faces the reverse: unanchored expectations generate inflation that validates and reinforces those expectations, requiring much more contractionary policy — and much more economic pain — to bring inflation back down."
  explanation: "The self-fulfilling mechanism is why the concept of anchoring is central to modern monetary policy. It also explains why fighting inflation after expectations become unmoored is so costly (as the Volcker disinflation demonstrated) versus maintaining credibility continuously."
```

## Explainer

From your study of expectation formation mechanisms, you know that agents must forecast the future when making decisions today. For inflation specifically, this feedback loop is unusually consequential: unlike forecasting tomorrow's weather (where expectations don't affect the weather), inflation expectations *cause* inflation. This self-referential quality makes inflation expectations one of the most important variables in macroeconomics, and understanding how they form is essential to understanding why inflation is so hard to control.

The mechanism is straightforward. Workers negotiating wages ask: what will prices be next year? If they expect 5% inflation, they demand wages 5% higher just to maintain real purchasing power. Firms setting prices ask: what will my costs be next year? If they expect wages (their main input cost) to rise 5%, they raise prices 5% pre-emptively. The result: everyone raising prices by 5% *because* they expected 5% inflation produces exactly 5% inflation — the expectation was self-fulfilling. This is why **expected inflation** appears directly in the New Keynesian Phillips Curve: actual inflation = expected inflation + output-gap term + supply shock. Strip out the expectation component and you cannot account for why inflation persists even when economic slack should be pulling it down.

**Adaptive expectations** model agents as backward-looking: this year's forecast is simply last year's realization (π^e = π_{t−1}). This is computationally simple and plausible for routine periods, but it means agents are always one period behind. In the 1970s, when oil shocks repeatedly surprised adaptive forecasters, the hypothesis came under heavy criticism — it predicted systematic, exploitable errors. **Rational expectations** (RE) replaced it with the more demanding assumption that agents use all available information and form unbiased forecasts on average (π^e = E[π | Ω_t], where Ω_t is the information set). RE does not require that forecasts are perfect — only that errors are random and not predictable from available information. The implication is radical: systematic monetary policy has no real effects because agents anticipate and undo it.

In practice, survey data and financial market instruments (TIPS breakevens, inflation swaps) reveal that expectations fall somewhere between these poles. They are forward-looking but not perfectly rational, slow to update to new information, and heavily influenced by recent experience — exactly what you'd expect when forming expectations is costly and agents use simple heuristics. The critical policy implication is **anchoring**: a central bank whose inflation target is credible keeps long-run inflation expectations fixed even during short-run deviations. When expectations become "unanchored" — when the public stops believing the central bank will achieve its target — inflation becomes much harder to control because the self-fulfilling component of the Phillips Curve activates at scale. The Federal Reserve's aggressive rate hikes in 2022–2023 were precisely a campaign to keep expectations anchored before a 1970s-style wage-price spiral could take hold.
