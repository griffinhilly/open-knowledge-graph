---
id: fiscal-multiplier
title: The Fiscal Multiplier
domain: economics
course: macroeconomics
prerequisites:
- id: fiscal-policy-macroeconomics
  type: hard
- id: gdp-components
  type: soft
- id: geometric-series
  type: soft
- id: interest-rates-and-loanable-funds
  type: soft
- id: infinite-series
  type: soft
- id: convergence-rigorous-series
  type: soft
builds-toward:
- is-lm-model
tags:
- multiplier
- marginal-propensity-to-consume
- MPC
- crowding-out
- Keynesian
stage: abstract-reasoning
status: validated
---
# The Fiscal Multiplier

## Core Idea
The fiscal multiplier measures how much total GDP changes per dollar of government spending. If the government spends $1, that $1 becomes someone's income, a fraction of which is re-spent (determined by the marginal propensity to consume, MPC), generating further rounds of spending. The simple Keynesian multiplier is 1 / (1 − MPC). In practice, multipliers are smaller due to crowding out (government borrowing raises interest rates, reducing private investment), import leakages, and Ricardian equivalence (households save anticipated future tax increases). Multipliers are typically larger during recessions when monetary policy is constrained.

## How It's Best Learned
Compute the simple multiplier for MPC = 0.8 (multiplier = 5), then explain why real-world estimates are 0.5–2. Discuss why tax-cut multipliers are generally smaller than spending multipliers.

## Common Misconceptions
- The multiplier is not fixed; it depends on the business cycle position, exchange rate regime, and whether monetary policy offsets fiscal expansion.
- A multiplier below 1 does not mean fiscal policy is counterproductive — it still means positive (if diminished) stimulus.
- Ricardian equivalence assumes fully rational, forward-looking households with access to credit — a strong assumption rarely fully satisfied.

## Explainer

You know from your study of GDP components that output equals consumption + investment + government spending + net exports. When the government spends an additional dollar on, say, road construction, that directly adds $1 to GDP as government spending. But the story does not end there. The construction workers who receive that dollar as wages do not put it all under a mattress — they spend a fraction of it at restaurants, on rent, on clothes. That spending becomes income for others, who in turn spend a fraction, and so on. The question is how large this cascade of secondary spending becomes relative to the initial government outlay.

This is exactly a **geometric series** — a concept you may have encountered in mathematics. If the **marginal propensity to consume (MPC)** is 0.8, consumers spend 80 cents of each extra dollar of income and save 20 cents. The first round of government spending generates $1 of income. Recipients spend $0.80, which becomes income for others. Those people spend $0.80 × 0.80 = $0.64, which becomes income again. The total is 1 + 0.8 + 0.64 + 0.512 + ... = 1/(1 − 0.8) = 5. This is the **simple Keynesian multiplier**: 1/(1 − MPC). With MPC = 0.8, $1 of government spending produces $5 of total GDP — the government's dollar gets recycled through the economy five times. The multiplier amplifies the initial impulse.

The simple multiplier of 5 is a theoretical ceiling, not an empirical prediction. Real-world estimates range from roughly 0.5 to 2, and the gap from theory to practice comes from several leakages and offsets. First, **crowding out**: government borrowing competes for a fixed pool of savings in the loanable funds market, raising interest rates and reducing private investment. Some of the GDP gain from government spending is offset by reduced private capital formation. Second, **import leakage**: in an open economy, some of each dollar of income is spent on imported goods, which adds to foreign GDP rather than domestic GDP. Third, **Ricardian equivalence**: if households are forward-looking and rational, they recognize that government borrowing today implies higher taxes tomorrow, so they increase saving now to prepare for that future tax bill — partially neutralizing the stimulus. Each of these forces reduces the effective multiplier below the simple Keynesian formula.

Multipliers are not constant — they vary systematically with economic conditions. They tend to be **larger during recessions**, especially when the economy is operating well below potential and monetary policy is constrained (the **zero lower bound** on interest rates). In normal times, central banks can offset fiscal expansion by raising rates, which crowds out investment and keeps total spending from rising much. At the zero lower bound, that offset disappears, so the fiscal impulse propagates more fully. This is why the debate over fiscal stimulus intensifies during deep downturns: proponents point to larger multiplier estimates in constrained environments; skeptics point to long-run debt sustainability and crowding-out risks. Understanding the multiplier means understanding not just the arithmetic, but the equilibrium forces that shape whether the cascade of spending amplifies or dissipates.
