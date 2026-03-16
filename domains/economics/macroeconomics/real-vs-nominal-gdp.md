---
id: real-vs-nominal-gdp
title: Real vs. Nominal GDP and the GDP Deflator
domain: economics
course: macroeconomics
prerequisites:
- id: gdp-components
  type: hard
- id: percent-increase-decrease
  type: hard
builds-toward:
- cpi-and-inflation-measurement
- economic-growth-theory
- business-cycles
tags:
- real-gdp
- nominal-gdp
- price-level
- deflator
- inflation-adjustment
stage: abstract-reasoning
status: validated
---

# Real vs. Nominal GDP and the GDP Deflator

## Core Idea
Nominal GDP measures output in current prices, so it rises when either quantities or prices increase. Real GDP holds prices fixed at a base year, isolating true changes in output volume. The GDP deflator is the ratio of nominal to real GDP, multiplied by 100, and serves as a broad price index for the entire economy. Growth in real GDP is the standard measure of whether an economy is actually producing more.

## How It's Best Learned
Start with a two-good, two-period example: compute nominal GDP, real GDP, and the deflator by hand. Then use FRED data to chart nominal vs. real US GDP since 1970 and observe recessions more clearly in the real series.

## Common Misconceptions
- Nominal GDP growth can be positive even during a recession if prices rise fast enough.
- The GDP deflator and CPI are both price indexes but cover different baskets; they often diverge.
- 'Real' does not mean 'inflation-adjusted from today' — it means adjusted relative to the chosen base year.

## Explainer

You know from GDP components that GDP is the total market value of all final goods and services produced in a country in a given period. That phrase "market value" creates a problem for measuring economic progress over time. If total spending rises from $20 trillion to $22 trillion, we cannot tell whether the economy produced more goods and services (a real improvement) or simply charged higher prices for the same output (inflation). **Nominal GDP** records the change in dollar value without distinguishing these two causes. **Real GDP** fixes prices at a reference point — the base year — so that only genuine changes in production volume register as changes in GDP.

The arithmetic is straightforward. Suppose the economy produces only two goods: 10 computers priced at $1,000 each and 100 units of bread priced at $5 each. Nominal GDP = (10 × $1,000) + (100 × $5) = $10,500. Now suppose next year, the economy produces 12 computers and 110 loaves, but prices rise to $1,200 and $6 respectively. Nominal GDP = $15,060 — a 43% increase. But real GDP (using base-year prices) = (12 × $1,000) + (110 × $5) = $12,550 — only a 19.5% increase. The remaining gap is entirely price increases, not output growth. Real GDP is the correct denominator for standard of living comparisons and business cycle analysis.

The **GDP deflator** is derived directly from these two measures: GDP deflator = (Nominal GDP / Real GDP) × 100. It tells you the average price level of all domestically produced output relative to the base year. If the deflator is 115, prices across the economy are on average 15% higher than in the base year. Because the GDP deflator covers the entire domestic output basket — consumption, investment, government spending, and net exports — it differs from the CPI, which covers only the consumer basket. Investment goods, government-purchased items, and exported goods affect the GDP deflator but not the CPI; meanwhile, imports are in the CPI (consumers buy them) but excluded from the GDP deflator (not domestically produced). In practice, the two indexes often move together but diverge when, say, oil prices spike (affects CPI strongly via consumer energy costs but affects the GDP deflator less if oil is imported).

The critical skill is being able to **convert between real and nominal** in either direction. If you have nominal GDP and the deflator, real GDP = (Nominal / Deflator) × 100. If the deflator is 125 and nominal GDP is $25 trillion, real GDP in base-year terms is $20 trillion. Conversely, you can compute the deflator growth rate to get a measure of economy-wide inflation. The growth rate of nominal GDP minus the growth rate of real GDP approximately equals inflation (as measured by the deflator). This approximation — that nominal ≈ real + inflation — appears throughout macroeconomics. It underpins the Fisher equation (nominal interest rate ≈ real rate + inflation) and the distinction between real and nominal wages, interest rates, and exchange rates that you will encounter throughout the rest of macroeconomics.
