---
id: business-cycles
title: Business Cycles
domain: economics
course: macroeconomics
prerequisites:
- id: as-ad-model
  type: hard
- id: real-vs-nominal-gdp
  type: hard
- id: types-of-unemployment
  type: soft
builds-toward:
- fiscal-policy-macroeconomics
- monetary-policy-tools
tags:
- business-cycle
- recession
- expansion
- peak
- trough
- NBER
stage: formal-systems
status: validated
---

# Business Cycles

## Core Idea
Business cycles are the recurring fluctuations in economic activity around a long-run growth trend, characterized by alternating periods of expansion (rising real GDP) and contraction (falling real GDP). Key phases are peak, recession, trough, and recovery. The National Bureau of Economic Research (NBER) officially dates US recessions using a broad set of indicators. Cycles arise from demand shocks (financial crises, confidence collapses), supply shocks (oil embargoes), and can be amplified by multiplier and accelerator mechanisms.

## How It's Best Learned
Chart US real GDP growth from 1950 to present and identify NBER-dated recessions. For each major recession, identify the primary shock: oil (1973, 1979), financial crisis (2008), pandemic (2020). Compare depth and duration.

## Common Misconceptions
- A recession is not simply two negative quarters of GDP growth — the NBER uses a broader definition.
- Business cycles are not perfectly regular or predictable; their frequency and amplitude vary widely.
- Recessions are not necessarily caused by policy mistakes; external shocks play a major role.

## Explainer

From your prerequisite on the AS-AD model, you know that aggregate output and the price level are jointly determined by where aggregate demand (AD) meets aggregate supply (AS). Shifts in either curve move the economy to a new equilibrium. Business cycles are what you observe when you track this equilibrium over time: the economy moves persistently above or below its long-run potential output, often for months or years, before returning. The AS-AD model provides the mechanics of how shocks affect the economy in a single period; business cycle analysis adds the time dimension — why do these deviations persist, and what regularities characterize the fluctuations?

A business cycle is divided into four phases. The **peak** is the highest point before a downturn begins. **Contraction** (or recession) is the period of falling real GDP and rising unemployment. The **trough** is the lowest point before recovery. **Expansion** is the period of rising real GDP, usually accompanied by falling unemployment, that follows the trough and eventually reaches a new peak. From your real vs nominal GDP prerequisite, you know it is real GDP — not nominal — that defines these phases: a country experiencing 10% inflation with 0% real growth is not expanding in the cycle sense even though nominal GDP is rising. The NBER dates US recessions using a broad set of real indicators — employment, real income, industrial production — not any single series.

The driving forces come in two varieties that generate very different macroeconomic patterns. **Demand shocks** shift the AD curve: a financial crisis destroys household wealth and freezes credit (2008); a pandemic halts consumption and investment (2020); a confidence collapse reduces spending across the board. In the AS-AD diagram, a negative demand shock moves AD left, reducing both output and inflation — the stagflation-free recession. **Supply shocks** shift the AS curve: an oil embargo raises production costs for the entire economy (1973, 1979), shifting AS left and producing the unusual combination of falling output and rising prices — **stagflation** — that stumped policymakers who were accustomed to treating inflation and unemployment as a tradeoff rather than simultaneous problems.

Shocks don't simply revert instantly; they are amplified by internal dynamics. The **multiplier mechanism** explains persistence: an initial drop in spending reduces income for downstream businesses and workers, who then also spend less, further reducing income — the shock ripples through the spending chain and multiplies into a larger contraction. The **accelerator mechanism** operates on investment: firms invest based on expected future demand, so when current demand falls, investment collapses disproportionately. A firm that was investing to expand capacity has no reason to do so if sales are weak — the investment decline amplifies the GDP fall far beyond what consumer spending alone would predict. These feedback effects explain why recessions are typically deeper and longer than the initial shock would imply in a simple static model.

The empirical **stylized facts** about business cycles provide structure that any serious theory must match. Consumption is less volatile than GDP; investment is far more volatile. Employment is procyclical but **lagging**: firms are slow to hire and slow to fire, so unemployment keeps rising for months after GDP has bottomed out. This lag is why unemployment is sometimes called a lagging indicator — it is politically and psychologically salient, but it measures where the cycle was, not where it is. Interest rates are typically countercyclical in recessions as central banks ease policy. Understanding leading, coincident, and lagging indicators is essential for interpreting economic data in real time — and for understanding why policymakers are often still responding to the previous downturn when the recovery has already begun.
