---
id: cpi-and-inflation-measurement
title: CPI and Inflation Measurement
domain: economics
course: macroeconomics
prerequisites:
- id: real-vs-nominal-gdp
  type: hard
- id: percent-increase-decrease
  type: hard
builds-toward:
- inflation-and-price-level
- phillips-curve
tags:
- cpi
- inflation
- price-index
- consumer-prices
- measurement
stage: abstract-reasoning
status: validated
---

# CPI and Inflation Measurement

## Core Idea
The Consumer Price Index (CPI) measures the cost of a fixed basket of goods and services representative of a typical household's purchases. Inflation is the percentage change in the CPI over time. The CPI is used to adjust wages, Social Security benefits, and tax brackets for inflation, making its accuracy consequential. Alternative measures include core CPI (excluding food and energy), PPI (producer price index), and PCE deflator (used by the Federal Reserve).

## How It's Best Learned
Calculate a simple two-good CPI by hand across three periods. Then examine the actual BLS CPI basket weights and consider which items might make the index unrepresentative for different demographic groups.

## Common Misconceptions
- The CPI overstates true inflation due to substitution bias (consumers switch away from goods that rise in price), quality improvements, and new goods.
- CPI and inflation are often used interchangeably, but CPI is the index level; inflation is its rate of change.
- Deflation (falling CPI) can be economically harmful despite sounding like prices falling.

## Explainer

You already know from real vs. nominal GDP that separating price changes from quantity changes is essential for measuring economic output. The same distinction applies when measuring what households actually experience. The **Consumer Price Index (CPI)** is a fixed-basket price index designed specifically to track the cost of living for a typical urban consumer. The Bureau of Labor Statistics surveys households to determine a representative market basket — how much housing, food, transportation, medical care, and other categories the average household buys — then tracks how the cost of that fixed basket changes over time.

The construction is mechanical but important to understand precisely. The BLS defines a base period, collects prices of each item in the basket, then reprices the same basket each subsequent period. If the basket cost $1,000 in the base year and costs $1,035 now, the CPI is 103.5. **Inflation** is the percentage change in the CPI over a period: (CPI_t − CPI_{t−1}) / CPI_{t−1} × 100. A CPI of 103.5 followed by a CPI of 106 implies roughly 2.4% inflation over that period. This percentage change is what economists, policymakers, and headlines mean when they say "inflation is 2.4%." The index level itself is rarely cited.

The CPI's fixed-basket design introduces a systematic upward bias in measured inflation relative to the true cost-of-living change. The deepest source is **substitution bias**: the index holds quantities fixed, but real consumers substitute toward relatively cheaper goods when prices rise. If beef prices spike, consumers buy more chicken — but the CPI basket keeps buying the same beef. The index therefore overstates the cost of maintaining a constant living standard. A second bias is **quality change**: new goods are typically better than old goods at the same nominal price. If a new laptop costs the same as last year's but performs twice as fast, the CPI treats this as no price change when the true cost per unit of computing power has fallen. The BLS applies hedonic adjustments to partially correct for this in some categories (electronics, vehicles), but coverage is incomplete.

These biases matter practically because the CPI is the escalator for major government programs. Social Security benefits, federal income tax brackets, and many wage contracts are indexed to CPI. If the CPI overstates inflation by 0.5 percentage points per year — a commonly cited estimate — Social Security payments grow slightly faster than the true cost of living each year, a politically charged implication. Alternative measures address different dimensions of this problem. **Core CPI** strips out food and energy, which are volatile, to reveal the underlying trend. The **PCE deflator** (Personal Consumption Expenditures) is the Federal Reserve's preferred inflation measure; it uses a chain-weighted basket that updates spending shares each period, largely eliminating substitution bias, and tends to run 0.2–0.5 percentage points below CPI inflation as a result.
