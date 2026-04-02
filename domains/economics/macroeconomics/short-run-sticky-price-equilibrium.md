---
id: short-run-sticky-price-equilibrium
title: Short-Run Equilibrium with Sticky Prices
domain: economics
course: macroeconomics
prerequisites:
- id: as-ad-model
  type: hard
- id: nominal-rigidities-sticky-prices
  type: hard
builds-toward:
- medium-run-nairu-equilibrium
tags:
- sticky-prices
- short-run
- as-ad
- quantity-adjustment
stage: expert
status: validated
---

# Short-Run Equilibrium with Sticky Prices

## Core Idea
In the short run with sticky prices, output is demand-determined: firms set prices and supply whatever quantity customers demand. Quantity adjustments absorb demand shocks; price changes lag far behind.

## How It's Best Learned
Draw AS-AD diagram with vertical short-run AS (sticky prices) and upward-sloping medium-run AS. Show positive demand shock raises output and price level. Explain firms can't adjust instantly due to menu costs.

## Common Misconceptions
- Assuming prices never change in short run; some adjust quickly, others slowly.
- Confusing sticky with fixed prices.
- Treating short run as fixed calendar period.

## Questions

```yaml
- question: "Government spending increases sharply. A classical model with perfectly flexible prices predicts prices rise immediately and real output stays at potential. What does the sticky-price model predict instead?"
  type: multiple-choice
  options:
    - "Real output falls because higher spending crowds out private investment"
    - "Prices rise immediately because firms always reprice when demand changes"
    - "Real output rises significantly while prices barely change, because firms meet higher demand at their preset prices rather than raising them"
    - "The predictions are identical — sticky and flexible price models agree in the short run"
  answer: 2
  explanation: "With sticky prices, firms have already set prices (menu costs, contracts, etc.) and simply supply whatever quantity is demanded at those prices — output is demand-determined. A rightward shift in aggregate demand moves the economy along the flat short-run AS curve: output rises, price level barely changes. In the classical model, immediate price flexibility would push the economy back to potential output with a higher price level and no real output gain. The sticky-price model is precisely why fiscal and monetary policy can affect real GDP in the short run."

- question: "In the AS-AD diagram with a flat short-run aggregate supply curve, what happens when aggregate demand shifts rightward?"
  type: multiple-choice
  options:
    - "The price level rises sharply and output returns immediately to potential"
    - "Both price level and output rise in equal proportion"
    - "Output rises significantly while the price level is largely unchanged"
    - "Output falls as firms reduce supply to protect profit margins"
  answer: 2
  explanation: "A flat SRAS means firms are price-takers in the short run — they set prices and supply whatever demand arrives. The new equilibrium after a rightward AD shift is found where the shifted AD curve crosses the flat SRAS: higher output, same price level. This is the graphical expression of quantity adjustment dominating price adjustment in the short run. Only over time does SRAS shift upward as wages and other sticky prices eventually adjust."

- question: "Sticky wages are a key reason demand contractions cause recessions: firms cannot quickly reduce wages to maintain production at lower prices, so they instead reduce output and employment."
  type: true-false
  answer: true
  explanation: "Wages are among the stickiest prices in the economy due to contracts, efficiency wage considerations, and fairness norms. When demand falls, a firm facing a rigid wage bill cannot cut costs proportionally to lower prices and maintain output. Instead, it reduces employment and production. This propagates the demand shortfall through the labor market — unemployment rises, consumer spending falls further, deepening the recession. Wage stickiness is the primary transmission mechanism linking sticky prices to employment fluctuations."

- question: "The 'short run' in sticky-price macroeconomics refers to a fixed calendar period — typically one to four quarters — after which prices are assumed to be fully flexible."
  type: true-false
  answer: false
  explanation: "The short run is NOT a calendar period — it is the window during which prices remain predetermined at their preset levels. This duration varies enormously by sector: financial asset prices adjust in milliseconds, airline seat prices in hours, retail goods perhaps in weeks, wage contracts in months to years. The economy as a whole exhibits short-run stickiness because enough prices — especially wages — adjust slowly. This is why 'short run' cannot be pinned to a calendar: it depends on which prices are binding in a given context."

- question: "Why can fiscal and monetary policy affect real output in the short run but not in the long run, according to the sticky-price model? What happens as prices eventually adjust?"
  type: short-answer
  answer: "In the short run, prices are preset, so firms supply whatever is demanded at those prices — output is demand-determined. A positive demand shock (more government spending or easier monetary policy) raises real output. In the long run, prices — especially wages — adjust upward to reflect the higher demand, shifting SRAS upward until the economy returns to potential output. The long-run effect is purely a higher price level with no change in real output. The short run is the transitional window during which price rigidity keeps firms from immediately absorbing demand changes into prices."
  explanation: "The long-run neutrality of money and fiscal policy follows directly from price flexibility: once all prices adjust, relative prices are unchanged and real allocations return to their efficient levels. The short run's policy power comes entirely from the delay in that adjustment. This is why central banks focus on inflation expectations — if prices adjust faster (because people expect inflation and reprice immediately), the short-run window shrinks and policy loses traction."
```

## Explainer

From the AS-AD model, you have the framework: aggregate demand (AD) slopes downward because higher price levels reduce real money balances and thus spending, while the aggregate supply (AS) curve describes how firms respond to changes in the overall price level. From nominal rigidities and sticky prices, you understand why firms do not instantly reprice: menu costs, long-term contracts, customer relationships, and the coordination problem all make rapid price adjustment costly or impractical. Short-run sticky-price equilibrium puts these together into a coherent model of how the economy absorbs demand shocks in the short run.

The key claim is that when prices are sticky, **output is demand-determined**: firms are on their supply curve only in the long run. In the short run, they commit to a price (often set in advance) and then meet whatever demand arrives at that price. Think of a restaurant with a printed menu: when lunch demand unexpectedly surges, the restaurant does not raise its prices mid-service — it runs out of some items, seats more customers, and serves more meals. Output adjusts; the price remains fixed. This is quantity adjustment rather than price adjustment, and it is the defining feature of short-run equilibrium with sticky prices.

In the AS-AD diagram, this corresponds to a **flat short-run AS curve** (or nearly flat): at the prevailing price level, firms supply whatever quantity is demanded. When aggregate demand shifts rightward — say, because government spending increases or consumer confidence improves — the new equilibrium moves along the flat SRAS curve: output rises, but the price level barely moves. This is precisely why fiscal and monetary policy can affect real output in the short run but not the long run. In the long run, prices eventually adjust to reflect the new demand level, the economy returns to its potential output, and the only lasting effect is a higher price level. The short run is the window during which that adjustment has not yet occurred.

The "short run" here is not a calendar period — it is the window during which prices remain predetermined. For some prices (airline seats, financial assets, commodity spot prices), the adjustment is nearly instantaneous and the short run is measured in minutes. For others (wage contracts, lease agreements, administered prices in utilities), the short run can be a year or more. What makes the economy as a whole exhibit short-run stickiness is that enough prices — particularly wages, which are the largest cost for most firms — adjust slowly. When wages are sticky, firms cannot easily cut costs in response to falling demand, so they reduce output and employment instead. This is why demand contractions cause recessions: firms cannot quickly lower wages to maintain production at lower prices, so they lay off workers instead, propagating the demand shortfall through the economy.
