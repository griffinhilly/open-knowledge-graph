---
id: capital-flows-equilibrium
title: International Capital Flows and Equilibrium
domain: economics
course: macroeconomics
prerequisites:
- id: current-account-definition-measurement
  type: hard
- id: international-capital-flows
  type: soft
builds-toward:
- mundell-fleming-extended
tags:
- capital-flows
- interest-rates
- international-investment
- equilibrium
stage: abstract-reasoning
status: draft
---

# International Capital Flows and Equilibrium

## Core Idea
International capital flows are motivated by interest rate differentials and risk considerations. Capital flows adjust to equalize risk-adjusted returns across countries. Equilibrium requires expected return on domestic assets equals expected return on foreign assets (adjusted for exchange risk).

## How It's Best Learned
Set up uncovered interest rate parity: r_domestic ≈ r_foreign + expected depreciation. Show if US rate exceeds German, investors expect dollar depreciation. If not, capital flows to US until returns equalize.

## Common Misconceptions
- Assuming capital flows respond instantly.
- Treating interest rate parity as a law.
- Forgetting expectations matter.

## Explainer

From your work on the current account, you know that a country's external position reflects how much it's borrowing from or lending to the rest of the world. The **capital account** (or financial account) is the flip side: every dollar borrowed must have a corresponding capital inflow, and every dollar lent out corresponds to a capital outflow. What determines which direction capital flows? In a world of mobile capital, the answer is relative returns — adjusted for risk and expected exchange rate movements.

The fundamental equilibrium condition is **uncovered interest rate parity (UIP)**: in equilibrium, the expected return on domestic assets must equal the expected return on foreign assets, once you account for expected exchange rate changes. If the US interest rate is 5% and the German rate is 2%, the gap doesn't persist as a free lunch. Investors will rush to US assets, buying dollars and selling euros. This drives the dollar up — and because an appreciated dollar is expected to depreciate back toward fundamentals over time, that expected depreciation is exactly the 3% gap. Equilibrium is reached when: r_domestic ≈ r_foreign + expected depreciation of domestic currency.

The dynamics of adjustment are crucial to understand. When the US rate rises relative to Germany's, capital initially flows *to* the US — investors sell euros, buy dollars, and purchase US bonds. This flow appreciates the dollar immediately (the "overshooting" phenomenon). The dollar has now appreciated *past* its long-run equilibrium, so it's expected to depreciate going forward, which is precisely what makes US and German assets equally attractive again. The equilibrium isn't that capital flows stop — it's that the exchange rate has moved enough to make the expected returns equal, so there's no further incentive for net flows.

In practice, several things complicate this clean picture. **Capital flows are lumpy, not continuous**: institutional investors rebalance periodically, creating discrete adjustment episodes rather than smooth convergence. **Risk premiums** matter — a country with default risk or political instability must offer higher interest rates just to attract the same capital, even after adjusting for expected depreciation. **Capital controls** in emerging markets can sever the parity condition entirely for periods of time. And **expectations are endogenous**: if investors believe a currency will depreciate, they demand a premium that can make that belief self-fulfilling. Understanding capital flow equilibrium means holding all these moving parts together: interest rates, exchange rates, expectations, and the risk environment all interact simultaneously.

