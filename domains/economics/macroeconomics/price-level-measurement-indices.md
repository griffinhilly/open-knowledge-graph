---
id: price-level-measurement-indices
title: Price Level Measurement and Price Indices
domain: economics
course: macroeconomics
prerequisites:
- id: cpi-and-inflation-measurement
  type: hard
- id: gdp-components
  type: soft
builds-toward:
- inflation-dynamics-and-persistence
- nominal-and-real-macroeconomic-variables
tags:
- measurement
- inflation
- price-level
stage: abstract-reasoning
status: draft
---

# Price Level Measurement and Price Indices

## Core Idea
Alternative price indices measure inflation differently: the Consumer Price Index (CPI) tracks prices paid by households; the Producer Price Index (PPI) tracks input costs; the GDP deflator reflects prices of all domestically produced goods. Each uses different weights and baskets, so inflation rates can diverge. The choice of index affects policy decisions and wealth redistribution through nominal contracts.

## Explainer

You've studied the CPI as the primary measure of inflation for households. But CPI is one of several price indices, each designed to answer a slightly different question about how prices in the economy are changing. Understanding the differences — what each measures, how the basket is constructed, and what each gets wrong — matters because the index chosen affects everything from policy decisions to legal contracts to the perception of living standards over time.

The **Consumer Price Index (CPI)** tracks the cost of a fixed basket of goods and services purchased by a typical urban household. The basket includes food, housing, transportation, medical care, and other categories, weighted by their share of household spending in a reference period. Because the basket is fixed, CPI uses a **Laspeyres formula**: it asks "what would the reference basket cost today compared to the base period?" This design has a known bias: when prices of some goods rise, consumers substitute toward cheaper alternatives, but the fixed basket doesn't reflect this substitution. CPI therefore tends to overstate the true cost of maintaining a given standard of living. The **chained CPI** (C-CPI-U) corrects for this by using an average of current and prior period weights, allowing the basket to evolve with actual spending patterns.

The **Producer Price Index (PPI)** measures prices at an earlier stage of production — what manufacturers pay for inputs or what producers receive for output, before goods reach the retail level. PPI often leads CPI by several months: when input costs rise for producers, those increases typically flow through to consumer prices with a lag. This makes PPI a useful **leading indicator** of future consumer inflation. The **GDP deflator** takes a different approach entirely: rather than a fixed basket, it covers all domestically produced final goods and services in proportion to their share of GDP, and it automatically adjusts its weights as the composition of output changes. Unlike CPI, the GDP deflator excludes imported goods and includes investment goods and government services that households don't purchase directly.

The choice of index has real distributional consequences because different households face different price baskets. The standard CPI reflects spending patterns of an average urban consumer, but elderly households spend proportionally more on medical care and housing — categories that have inflated faster than the overall CPI. Adjusting Social Security benefits by CPI may therefore undercompensate retirees for their actual cost-of-living increases. The **PCE deflator** (Personal Consumption Expenditures) is the Federal Reserve's preferred inflation measure: it uses a chain-weighted formula, covers a broader range of expenditures including those paid on behalf of consumers (like employer-sponsored health insurance), and tends to run somewhat below CPI. When the Fed says it targets 2% inflation, it means 2% PCE inflation — a point that frequently causes confusion when the media reports CPI figures instead.
