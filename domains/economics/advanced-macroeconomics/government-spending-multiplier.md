---
id: government-spending-multiplier
title: Government Spending Multiplier in Macroeconomic Models
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: fiscal-multiplier
  type: soft
- id: new-keynesian-framework-overview
  type: hard
tags:
- government-spending-multiplier
- demand-stimulus
- fiscal-policy-impact
stage: advanced
status: draft
---

# Government Spending Multiplier in Macroeconomic Models

## Core Idea
The government spending multiplier measures the change in aggregate output from a unit increase in government purchases. In New Keynesian models, the multiplier typically lies between 0.5 and 2, depending on monetary policy stance (larger when the central bank keeps interest rates low) and whether the economy is at the ZLB.

## Explainer

From the basic fiscal multiplier concept, you know the intuition: government spending injects demand into the economy, and each dollar of spending can generate more (or less) than a dollar of additional output depending on how the rest of the economy responds. In the simplest Keynesian cross model, the multiplier is 1/(1−MPC), where MPC is the marginal propensity to consume. But this undergraduate formula ignores crucial feedback loops that the **New Keynesian framework** takes seriously — most importantly, the response of monetary policy and the role of expectations.

In a standard New Keynesian model, a government spending increase raises aggregate demand, which pushes up output and inflation. If the central bank follows a **Taylor rule**, it responds to higher inflation by raising the nominal interest rate more than one-for-one. This interest rate increase reduces private consumption and investment — the familiar **crowding-out effect**. The net multiplier is therefore less than the naive Keynesian calculation because monetary tightening partially offsets the fiscal stimulus. Under typical calibrations, the multiplier lands between 0.5 and 1.0: a dollar of government spending generates less than a dollar of additional output because private spending contracts.

The picture changes dramatically at the **zero lower bound (ZLB)**. When the nominal interest rate is already at zero, the central bank *cannot* raise rates in response to higher inflation — it is constrained. A fiscal expansion still raises inflation, but now the real interest rate (nominal rate minus expected inflation) actually *falls*, because the nominal rate is stuck at zero while inflation expectations rise. A lower real interest rate stimulates rather than discourages private spending, creating a positive feedback loop: government spending raises demand, which raises inflation expectations, which lowers real rates, which raises private demand, which raises output further. At the ZLB, multipliers can easily exceed 1.5 or even 2.0 — each dollar of government spending generates well more than a dollar of additional output because private spending amplifies rather than offsets the fiscal impulse.

This state-dependence is the central lesson. The multiplier is not a fixed number — it depends critically on the **monetary policy regime**. In normal times with an active Taylor rule, fiscal stimulus is partially self-defeating because it provokes monetary tightening. In a liquidity trap or when the central bank accommodates by holding rates fixed, fiscal policy becomes far more powerful. This explains why economists who agree on the underlying model can disagree sharply about the wisdom of fiscal stimulus: they may be assuming different monetary policy responses. The empirical evidence broadly supports this distinction, with estimated multipliers during recessions and ZLB episodes significantly larger than those during normal expansions.
