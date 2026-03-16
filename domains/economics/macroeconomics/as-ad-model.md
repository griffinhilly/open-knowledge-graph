---
id: as-ad-model
title: The AS-AD Model
domain: economics
course: macroeconomics
prerequisites:
- id: aggregate-demand
  type: hard
- id: aggregate-supply-short-run
  type: hard
- id: aggregate-supply-long-run
  type: hard
- id: inflation-and-price-level
  type: soft
builds-toward:
- fiscal-policy-macroeconomics
- monetary-policy-tools
- business-cycles
- phillips-curve
tags:
- AS-AD
- macroeconomic-equilibrium
- output-gaps
- price-level
- stabilization
stage: abstract-reasoning
status: validated
---
# The AS-AD Model

## Core Idea
The Aggregate Supply–Aggregate Demand (AS-AD) model describes the simultaneous determination of the price level and real GDP in the short and long run. Short-run equilibrium occurs where AD intersects SRAS; long-run equilibrium requires that intersection to also lie on LRAS (at potential output). Demand shocks (AD shifts) and supply shocks (SRAS shifts) produce different combinations of output and price-level changes, helping explain why some economic downturns are accompanied by high inflation (stagflation) and others are not.

## How It's Best Learned
Practice the four standard shock scenarios: (1) positive demand shock, (2) negative demand shock, (3) adverse supply shock, (4) favorable supply shock. For each, identify what happens to the price level and real GDP in the short run and what the self-correction path is.

## Common Misconceptions
- The AS-AD model is not the same as a supply-and-demand model of a single market; axes are price level (not a single price) and real GDP (not quantity of one good).
- A supply shock that raises prices is not the same as demand-pull inflation.
- Reaching long-run equilibrium is automatic in theory but may require active policy in practice.

## Questions

```yaml
- question: "An oil price spike shifts SRAS leftward. What happens to output and price level in the short run?"
  type: multiple-choice
  options:
    - "Output rises, price level falls"
    - "Output falls, price level rises"
    - "Output falls, price level falls"
    - "Output rises, price level rises"
  answer: 1
  explanation: "An adverse supply shock raises production costs, shifting SRAS left. The new intersection of AD and SRAS is at lower real GDP and a higher price level — stagflation. This is distinct from a demand shock, which moves output and price level in the same direction."

- question: "A positive demand shock (AD shifts right) permanently raises real GDP above its long-run potential level."
  type: true-false
  answer: false
  explanation: "LRAS is vertical at potential output — it is determined by the productive capacity of the economy (labor, capital, technology), not by the price level. A demand shock raises output in the short run, but as wages and input prices adjust upward, SRAS shifts left until output returns to potential at a higher price level. Real GDP reverts; only the price level is permanently higher."

- question: "After a negative demand shock, how does the economy self-correct without policy intervention, and what happens to the price level during this process?"
  type: short-answer
  answer: "Below-potential output means unemployment rises and workers accept lower wages. Lower labor costs shift SRAS rightward over time. The economy moves back toward potential output, but at a lower price level than before the shock. Self-correction is slow — wages are sticky downward — which is why many economists argue for active stabilization policy."
  explanation: "The self-correction mechanism operates through the labor market: a recession creates slack, reducing wage pressure, which lowers firms' costs and induces more production. This takes time because nominal wages are slow to fall. Recognizing this dynamic is why the short-run vs. long-run distinction in the AS-AD model matters for policy."
```

## Explainer

You have already studied supply and demand in a single market — but that framework analyzes one price and one quantity. The AS-AD model lifts this to the entire economy, replacing "price" with "price level" (an index like the CPI) and "quantity" with "real GDP." The shape of the curves follows different logic than single-market S&D, so resist the temptation to treat it the same way.

The **Aggregate Demand (AD)** curve slopes downward, but not for the same reason as a firm's demand curve. Higher price levels reduce real wealth (the real balance effect), raise interest rates (the interest rate effect), and make domestic goods more expensive relative to foreign goods (the exchange rate effect). All three reduce spending, so higher price levels are associated with lower real GDP demanded. Shifts in AD come from changes in any of its components: consumption, investment, government spending, or net exports.

The **Short-Run Aggregate Supply (SRAS)** curve slopes upward because input prices (especially wages) are sticky in the short run. When the price level rises but wages haven't yet adjusted, firms' profit margins widen and they produce more. Shifts in SRAS come from changes in input costs (oil prices, wages) or supply shocks. The **Long-Run Aggregate Supply (LRAS)** curve is vertical at potential output because, in the long run, all prices are flexible and the economy produces at its capacity regardless of the price level.

The key scenarios to master are demand shocks versus supply shocks. A **positive demand shock** (say, a stimulus check) shifts AD right: output rises and price level rises in the short run. In the long run, wages catch up, SRAS shifts left, and output returns to potential at a permanently higher price level. A **negative supply shock** (an oil embargo) shifts SRAS left: output falls *and* price level rises simultaneously — this is **stagflation**, the nightmare combination that stumped policymakers in the 1970s. Notice that demand-side policies can fix the output gap or the price level, but not both at once when the problem originates on the supply side.

Self-correction provides a theoretical anchor: if policy does nothing, wages eventually adjust and SRAS drifts back to restore potential output. But "eventually" can mean years of high unemployment. The AS-AD model frames the central debate in macroeconomic policy: how long is the long run, and how much pain is acceptable while waiting for it?
