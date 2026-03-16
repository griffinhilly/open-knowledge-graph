---
id: okun-law
title: Okun's Law
domain: economics
course: macroeconomics
prerequisites:
- id: gdp-and-national-income
  type: hard
- id: unemployment-measurement
  type: hard
builds-toward:
- output-gap-macroeconomic
- business-cycles
tags:
- employment
- output
- cyclical-relationships
stage: abstract-reasoning
status: draft
---

# Okun's Law

## Core Idea
Okun's Law quantifies the empirical relationship between changes in the unemployment rate and the growth rate of real GDP: for every 1% that unemployment rises above its natural rate, GDP falls roughly 2-3% below potential output. This relationship captures how labor market slack moves with macroeconomic slack.

## How It's Best Learned
Start with the historical data scatter plot of unemployment changes versus GDP growth rates across business cycles. Estimate the coefficient empirically to see why the relationship is called a 'law.' Discuss why the relationship varies across countries and time periods.

## Common Misconceptions
- The relationship is mechanically precise rather than an empirical regularity that varies. - Okun's Law implies causation (unemployment causes low growth) rather than showing they move together. - The law holds perfectly during all types of recessions, when actually it weakens during financial crises.

## Explainer

From your study of GDP measurement, you know that real GDP captures the economy's total output, and from unemployment measurement, you know that the unemployment rate tracks the share of the labor force actively seeking work but unable to find it. These two concepts are obviously connected — a thriving economy needs workers — but the *quantitative* relationship between them is not obvious from first principles. Arthur Okun's empirical discovery in 1962 was that this relationship is remarkably stable: for every 1 percentage point that the unemployment rate rises *above its natural rate*, real GDP falls roughly 2-3% *below its potential*. This is **Okun's Law** — a rule of thumb, not a theorem, but one of the most useful empirical regularities in macroeconomics.

To understand why the coefficient is around 2-3 (not 1), you need to decompose what happens when output falls. A 1% drop in GDP does not translate directly into a 1% rise in unemployment for several reasons. First, firms reduce hours before laying off workers — labor input falls partly through **reduced hours** rather than reduced employment. Second, some workers exit the labor force entirely during downturns ("discouraged workers"), so unemployment rises by less than employment falls. Third, firms **hoard labor**: they keep workers on payroll during mild downturns rather than bearing the costs of layoffs and rehiring, accepting lower output per worker. Each of these mechanisms creates a wedge between output changes and unemployment changes, which is why the Okun coefficient exceeds 1. The 2-3 multiplier captures all these mechanisms combined.

There are two formulations of Okun's Law. The **gap version** relates the level of the output gap (actual GDP minus potential GDP, as a percentage) to the unemployment gap (actual unemployment minus the natural rate): (Y - Y*)/Y* ≈ -c · (u - u*), where c is the Okun coefficient and u* is the natural rate of unemployment. The **first-difference version** relates *changes* in unemployment to the *growth rate* of output: Δu ≈ -0.5 · (gY - gY*), where gY is actual growth and gY* is potential growth (roughly 2-3% for the US economy). The first-difference version is more directly observable and is what Okun originally estimated. It predicts that the economy must grow above its potential growth rate — above roughly 2-3% per year for the US — just to prevent unemployment from rising, because productivity growth and labor force growth keep expanding the supply of labor even when the economy is growing at trend.

Okun's Law is an empirical regularity, not a structural relationship, and it varies across countries and time periods. Countries with more rigid labor markets (strong employment protection, higher firing costs) tend to have *lower* Okun coefficients — firms adjust to downturns through hours and wages rather than layoffs, so unemployment moves less per unit of output lost. During financial crises, Okun's Law has historically underperformed: the output losses are large but the unemployment response is sometimes larger than the coefficient predicts, possibly because financial distress triggers unusual hiring freezes and firm exit. The law also breaks down during "jobless recoveries" — periods where output grows at trend but unemployment remains elevated, suggesting that hiring behavior is more complex than the simple Okun relationship captures. Used appropriately, Okun's Law is an invaluable tool for translating between the labor market and output perspectives on the business cycle — a bridge between the two sides of your macroeconomics training.
