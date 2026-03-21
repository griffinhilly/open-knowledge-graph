---
id: fiscal-multipliers-macro
title: Fiscal Multipliers in Macroeconomic Models
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: fiscal-multiplier
  type: hard
- id: dsge-models
  type: hard
builds-toward:
- ricardian-equivalence
- government-debt-fiscal-sustainability
tags:
- fiscal-policy
- multipliers
- demand
stage: advanced
status: draft
---

# Fiscal Multipliers in Macroeconomic Models

## Core Idea
Fiscal multipliers measure how much output increases when government spending rises by one unit. In Keynesian models with slack and sticky prices, multipliers exceed one (government spending creates additional private demand); in neoclassical models with full employment and Ricardian equivalence, multipliers equal zero (higher government spending crowds out private spending). Modern DSGE models show multipliers depend on monetary policy stance, whether the economy is at the zero lower bound, and household expectations, explaining variation in multiplier estimates across periods and countries.

## Questions

```yaml
- question: "An economy is operating near full employment with inflation above target and the central bank actively raising interest rates. The government announces a large fiscal stimulus package. Under these conditions, the fiscal multiplier is most likely:"
  type: multiple-choice
  options:
    - "Greater than 1, because each dollar of spending generates multiple rounds of private demand"
    - "Near zero or negative, because the central bank will raise rates further, crowding out private investment"
    - "Exactly 1, because every dollar of government spending adds exactly one dollar of GDP"
    - "Greater than 1, because liquidity-constrained households will spend transfers immediately"
  answer: 1
  explanation: "When the central bank is actively tightening, it will respond to fiscal expansion by raising interest rates more aggressively, crowding out private investment and partially or fully offsetting the fiscal stimulus. In an economy near full employment, neoclassical effects dominate: Ricardian households save more to cover anticipated future taxes, and higher interest rates choke off investment. Options A and D describe Keynesian scenarios that require slack and near-ZLB conditions; option C (multiplier = 1) ignores both the Ricardian offset and the monetary offset."

- question: "An economy is stuck at the zero lower bound — the central bank cannot cut rates further. The government increases spending by $100 billion. What is the most important reason the fiscal multiplier is especially large in this situation?"
  type: multiple-choice
  options:
    - "At the ZLB, governments can borrow at zero interest rates, making fiscal expansion costless"
    - "Households near the ZLB hold more cash, which they immediately spend when transferred"
    - "The central bank cannot raise interest rates to offset the stimulus, shutting down the crowding-out channel"
    - "Government spending directly creates jobs, which is the only effective stimulus at the ZLB"
  answer: 2
  explanation: "Normally, fiscal expansion raises output and prices, prompting the central bank to raise interest rates, which crowds out private investment and partially cancels the stimulus. At the ZLB, the central bank is constrained — it cannot raise rates in response — so the crowding-out channel is disabled. Fiscal stimulus gets full traction without monetary offset, producing multipliers estimated between 1.5 and 3.0 in some studies. Option A confuses financing cost with multiplier size; option D is a partial truth but not the key mechanism distinguishing ZLB from normal conditions."

- question: "The size of the fiscal multiplier depends on whether the central bank accommodates the fiscal expansion or raises interest rates in response."
  type: true-false
  answer: true
  explanation: "This is precisely why empirical multiplier estimates vary so widely. A fiscal expansion accompanied by monetary accommodation (or constrained at the ZLB) gets full traction and produces a large multiplier. The same fiscal expansion during a period when the central bank actively tightens will produce a near-zero multiplier, as monetary offset cancels the demand injection. The multiplier is not a fixed property of fiscal policy — it is a function of the monetary policy environment."

- question: "In a real business cycle model with Ricardian households and flexible prices, an increase in government spending generates a multiplier greater than one because the new spending stimulates additional rounds of private demand."
  type: true-false
  answer: false
  explanation: "This reverses the neoclassical prediction. Ricardian households internalize the government's budget constraint: they know that today's spending implies higher future taxes, so they reduce their own consumption by the present value of those taxes. This fully offsets the government demand increase, producing a multiplier near zero. On top of this, higher government demand for goods and labor raises real wages and interest rates, crowding out private investment. The multiplier chain that Keynesians describe requires either sticky prices or liquidity-constrained households — neither of which exists in the standard RBC model."

- question: "Why does the presence of liquidity-constrained households increase the fiscal multiplier?"
  type: short-answer
  answer: "Ricardian (unconstrained) households neutralize fiscal stimulus by increasing savings to offset anticipated future tax liabilities — so government spending is crowded out dollar-for-dollar. Liquidity-constrained households cannot borrow against future income; they simply spend whatever current income they receive. When government spending reaches these households — through wages on public projects, transfers, or contracts — they spend it immediately, generating the successive rounds of spending that create a multiplier above zero. The higher the fraction of constrained households, the larger the aggregate multiplier."
  explanation: "This is the key micro-foundation for Keynesian multipliers. Ricardian equivalence breaks down when some agents face binding borrowing constraints, making current fiscal transfers stimulative in a way that lump-sum tax cuts to wealthy forward-looking households are not. This is why the composition of fiscal policy — who receives the spending — affects multiplier size as much as the total amount."
```

## Explainer

You already understand the basic fiscal multiplier from introductory macroeconomics — the idea that a dollar of government spending can generate more than a dollar of output through successive rounds of spending. And from your work with DSGE models, you know how to build economies with optimizing agents, market clearing, and explicit microfoundations. The advanced treatment of fiscal multipliers brings these together by asking: under what precise conditions does government spending boost output, and when does it simply displace private activity?

The **neoclassical benchmark** is the sharpest starting point. In a standard real business cycle model with flexible prices, full employment, and Ricardian households (who internalize the government's budget constraint), an increase in government spending produces a multiplier near zero or even negative. The logic is straightforward: government spending must be financed by taxes, either now or later. Forward-looking households recognize that future taxes will rise, reduce their consumption accordingly, and the private demand reduction offsets the government demand increase. Meanwhile, higher government demand for goods and labor bids up wages and interest rates, **crowding out** private investment. In this world, fiscal policy simply reshuffles who spends, not how much is spent in total.

The **New Keynesian framework** breaks this result through two key frictions. First, sticky prices mean that increased government demand does not immediately bid up all prices — instead, firms respond by producing more output, so real GDP rises. Second, some households may be **liquidity-constrained** (they cannot borrow against future income and simply spend whatever they earn). When government spending puts income into these households' pockets — through wages on public projects, transfers, or contracts — they spend it immediately, creating the multiplier chain that Ricardian households would neutralize. The more constrained households there are in the economy, the larger the multiplier.

The most important modern insight is that the multiplier is **state-dependent** — it varies dramatically with economic conditions. At the **zero lower bound** (ZLB), where the central bank cannot cut interest rates further, fiscal multipliers can be very large (estimates range from 1.5 to 3.0). Normally, fiscal expansion raises interest rates, which crowds out private spending. But at the ZLB, rates cannot rise in response, so the crowding-out channel is shut off and fiscal stimulus gets full traction. Conversely, when the central bank is actively tightening, fiscal expansion triggers offsetting monetary contraction, and the multiplier shrinks toward zero. This state-dependence explains why empirical multiplier estimates vary so widely across studies: researchers measuring multipliers during recessions (high slack, near-ZLB rates, many constrained households) get large numbers, while those measuring during expansions (low slack, active monetary offset) get small ones. The multiplier is not a fixed number — it is a function of the macroeconomic environment.
