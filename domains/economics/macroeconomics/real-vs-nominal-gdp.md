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
stage: formal-systems
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

## Questions

```yaml
- question: "Country X reports nominal GDP growth of 6% for the year. Inflation as measured by the GDP deflator was 8% over the same period. What happened to real GDP?"
  type: multiple-choice
  options:
    - "Real GDP grew by 14% — the two effects add together"
    - "Real GDP grew by approximately 2%"
    - "Real GDP shrank by approximately 2%"
    - "Real GDP stayed the same — nominal GDP captures all the relevant information"
  answer: 2
  explanation: "Real GDP growth ≈ nominal GDP growth − inflation. Here, 6% − 8% = −2%, meaning the economy actually produced slightly less even though the dollar value of output rose. This is why the distinction matters: nominal GDP can rise during a recession if prices rise fast enough. Country X's economy was shrinking in real terms despite positive nominal growth."

- question: "In year 1 (base year), an economy produces only widgets: 100 units at $5 each. In year 2, it produces 120 widgets at $7 each. What is the GDP deflator in year 2?"
  type: multiple-choice
  options:
    - "100 — because year 1 is the base year and deflators start at 100"
    - "120 — because output quantity grew by 20%"
    - "140 — nominal GDP is $840 and real GDP at base-year prices is $600"
    - "117 — because nominal GDP grew by approximately 17%"
  answer: 2
  explanation: "Nominal GDP (year 2) = 120 × $7 = $840. Real GDP (year 2, using base-year prices) = 120 × $5 = $600. GDP deflator = (840/600) × 100 = 140. Prices are 40% above the base year. Option B confuses quantity growth with the deflator — the deflator measures prices, not output volume."

- question: "If nominal GDP grows by 9% and real GDP grows by 4% over the same period, we can infer that the GDP deflator rose by approximately 5%."
  type: true-false
  answer: true
  explanation: "Nominal GDP growth ≈ real GDP growth + inflation (deflator growth). Rearranging: deflator growth ≈ nominal growth − real growth = 9% − 4% = 5%. This approximation is foundational in macroeconomics and underpins analogous real/nominal distinctions for wages, interest rates, and exchange rates."

- question: "Real GDP adjusts nominal GDP to reflect prices in today's dollars, making historical comparisons more meaningful."
  type: true-false
  answer: false
  explanation: "Real GDP adjusts to base-year prices — not today's prices. The base year is a fixed reference point. 'Real' means 'holding prices constant at the base year,' which removes the distortion of inflation over time, but the prices used are historical, not current. This is a common misreading of the word 'real.'"

- question: "Why can't nominal GDP alone tell us whether an economy is actually producing more goods and services over time?"
  type: short-answer
  answer: "Nominal GDP is measured in current prices, so it rises whenever either output quantities increase OR prices increase. A rise in nominal GDP could reflect genuine growth (more production) or simply inflation (the same production at higher prices) — or both at once. To isolate true changes in production volume, we hold prices fixed at a base year (real GDP), removing the confounding effect of price changes."
  explanation: "A wartime economy with severe shortages but hyperinflation can show rising nominal GDP while citizens are worse off. An economy producing identical output year-over-year shows rising nominal GDP whenever prices rise. Real GDP strips out the price effect so that comparisons across time reflect genuine changes in what the economy produces."
```

## Explainer

You know from GDP components that GDP is the total market value of all final goods and services produced in a country in a given period. That phrase "market value" creates a problem for measuring economic progress over time. If total spending rises from $20 trillion to $22 trillion, we cannot tell whether the economy produced more goods and services (a real improvement) or simply charged higher prices for the same output (inflation). **Nominal GDP** records the change in dollar value without distinguishing these two causes. **Real GDP** fixes prices at a reference point — the base year — so that only genuine changes in production volume register as changes in GDP.

The arithmetic is straightforward. Suppose the economy produces only two goods: 10 computers priced at $1,000 each and 100 units of bread priced at $5 each. Nominal GDP = (10 × $1,000) + (100 × $5) = $10,500. Now suppose next year, the economy produces 12 computers and 110 loaves, but prices rise to $1,200 and $6 respectively. Nominal GDP = $15,060 — a 43% increase. But real GDP (using base-year prices) = (12 × $1,000) + (110 × $5) = $12,550 — only a 19.5% increase. The remaining gap is entirely price increases, not output growth. Real GDP is the correct denominator for standard of living comparisons and business cycle analysis.

The **GDP deflator** is derived directly from these two measures: GDP deflator = (Nominal GDP / Real GDP) × 100. It tells you the average price level of all domestically produced output relative to the base year. If the deflator is 115, prices across the economy are on average 15% higher than in the base year. Because the GDP deflator covers the entire domestic output basket — consumption, investment, government spending, and net exports — it differs from the CPI, which covers only the consumer basket. Investment goods, government-purchased items, and exported goods affect the GDP deflator but not the CPI; meanwhile, imports are in the CPI (consumers buy them) but excluded from the GDP deflator (not domestically produced). In practice, the two indexes often move together but diverge when, say, oil prices spike (affects CPI strongly via consumer energy costs but affects the GDP deflator less if oil is imported).

The critical skill is being able to **convert between real and nominal** in either direction. If you have nominal GDP and the deflator, real GDP = (Nominal / Deflator) × 100. If the deflator is 125 and nominal GDP is $25 trillion, real GDP in base-year terms is $20 trillion. Conversely, you can compute the deflator growth rate to get a measure of economy-wide inflation. The growth rate of nominal GDP minus the growth rate of real GDP approximately equals inflation (as measured by the deflator). This approximation — that nominal ≈ real + inflation — appears throughout macroeconomics. It underpins the Fisher equation (nominal interest rate ≈ real rate + inflation) and the distinction between real and nominal wages, interest rates, and exchange rates that you will encounter throughout the rest of macroeconomics.
