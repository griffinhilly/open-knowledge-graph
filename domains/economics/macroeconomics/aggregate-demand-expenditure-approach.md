---
id: aggregate-demand-expenditure-approach
title: 'Aggregate Demand: The Expenditure Approach'
domain: economics
course: macroeconomics
prerequisites:
- id: consumption-function-keynesian
  type: hard
- id: investment-demand-interest-sensitivity
  type: hard
- id: gdp-components
  type: hard
builds-toward:
- short-run-sticky-price-equilibrium
- demand-shock-output-inflation-effects
tags:
- aggregate-demand
- expenditure
- multiplier
- consumption
- investment
stage: formal-systems
status: draft
---

# Aggregate Demand: The Expenditure Approach

## Core Idea
The expenditure approach to aggregate demand emphasizes total spending: AD = C + I + G + (X − M). Demand shifts amplify through the multiplier, though crowding out and supply constraints attenuate effects.

## How It's Best Learned
Build a simple Keynesian model: C = a + b*Y, I = I_0 − d*r, G and X−M exogenous. Solve for equilibrium Y. Show multiplier: each unit autonomous spending raises Y by 1/(1−b).

## Common Misconceptions
- Assuming multiplier is same for all spending types.
- Forgetting multiplier depends on monetary policy response.
- Treating multiplier as time-invariant.

## Explainer

From your work on the Keynesian consumption function, you know that household consumption depends on income: C = a + bY, where b is the **marginal propensity to consume** (MPC) — the fraction of each additional dollar of income that households spend rather than save. From GDP components, you know that total output equals total expenditure. The expenditure approach to aggregate demand combines these ideas: total spending in the economy is AD = C + I + G + (X − M), and in equilibrium, actual output adjusts until it equals this planned expenditure. The central insight is that spending creates income, and income generates further spending — a circular flow that amplifies initial disturbances.

The **multiplier** is the formalization of this amplification. Suppose government spending rises by $100 billion. This directly adds $100bn to income. The recipients save fraction (1 − b) and spend fraction b, adding $100b × b to income. Those recipients do the same, adding $100b × b² — and so on. Summing the geometric series gives total income change = $100bn × 1/(1 − b). If b = 0.8, the multiplier is 5: a $100bn spending increase eventually raises GDP by $500bn. The logic is symmetric on the downside — a fall in investment or exports triggers a contractionary multiplier. This is the mechanism behind fiscal policy effectiveness in Keynesian models: government spending is not just worth $1, it is worth the multiplier times $1.

Real-world multipliers are substantially smaller than this simple formula suggests, for several reasons your model needs to accommodate. First, **crowding out**: government borrowing to finance the spending raises interest rates (or expectations of future taxes), which reduces private investment I. The investment component falls even as G rises, partially offsetting the stimulus. Second, if the economy is at or near full capacity, the output response is attenuated and the adjustment is absorbed partly by prices rather than output. Third, an **open economy leakage**: some of the extra income is spent on imports rather than domestic goods, so the multiplier is smaller as the import propensity rises. Fourth, monetary policy response: if the central bank raises rates to prevent inflation, the interest-sensitive components of spending (investment, housing) contract, shrinking the effective multiplier.

The multiplier also differs across types of spending. Transfers (like tax cuts or unemployment benefits) pass through households first, so only fraction b enters the spending stream immediately — the multiplier is b/(1−b). Direct government purchases enter GDP at full value immediately — multiplier is 1/(1−b). This is why economists often argue that direct government expenditure has a larger first-round impact than equivalent tax cuts, though both create long-run income effects of similar magnitude. The time dimension matters too: the full multiplier takes quarters to years to materialize, while the initial impact is just the direct effect. Real-time fiscal multiplier estimates range widely, from near zero in full-employment economies with active monetary policy to above 1.5 in deep recessions when the zero lower bound on interest rates prevents the central bank from offsetting the stimulus.
