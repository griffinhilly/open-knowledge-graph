---
id: supply-shocks-aggregate-disruptions
title: Supply Shocks and Their Aggregate Effects
domain: economics
course: macroeconomics
prerequisites:
- id: aggregate-supply-short-run
  type: hard
- id: aggregate-supply-long-run
  type: hard
builds-toward:
- recession-definition-measurement-dating
- trend-and-cycle-decomposition
tags:
- supply-shocks
- stagflation
- prices
stage: formal-systems
status: draft
---

# Supply Shocks and Their Aggregate Effects

## Core Idea
Supply shocks (like oil price increases or productivity declines) shift the aggregate supply curve, directly raising costs and inflation. Unlike demand shocks, supply shocks can cause stagflation—simultaneous increases in inflation and unemployment. The policy response to supply shocks is difficult because demand-management policies that lower unemployment worsen inflation. Supply shocks explain why inflation and unemployment sometimes move together, violating the usual trade-off.

## Questions

```yaml
- question: "A large oil price spike shifts the short-run AS curve leftward. The central bank responds with expansionary monetary policy to restore output to its original level. What is the most likely result?"
  type: multiple-choice
  options:
    - "Output and price level both return to their pre-shock levels"
    - "Output recovers, but the price level rises even further above its post-shock level"
    - "The price level falls back to normal while output partially recovers"
    - "Both output and inflation worsen because monetary policy is ineffective against supply shocks"
  answer: 1
  explanation: "Expansionary monetary policy shifts the AD curve rightward. Starting from the new post-shock equilibrium (higher prices, lower output), rightward AD raises output back toward potential — but it also pushes the price level higher still, compounding the inflationary effect of the supply shock. The policy can restore output or fight inflation, but not both simultaneously. This is the supply-shock policy dilemma: demand-management tools move along the new, less-favorable AS curve rather than restoring the old one."

- question: "Which of the following best distinguishes the policy challenge posed by a negative supply shock from that posed by a negative demand shock?"
  type: multiple-choice
  options:
    - "Supply shocks are temporary while demand shocks are permanent, so supply shocks require no policy response"
    - "A negative demand shock reduces both output and the price level, so stimulating demand restores both; a negative supply shock raises prices while reducing output, so stimulating demand worsens inflation even as it helps output"
    - "Supply shocks affect only the goods sector while demand shocks affect the money market"
    - "Both types of shock require the same contractionary response — reducing money supply to control prices"
  answer: 1
  explanation: "With a negative demand shock, the economy moves to lower output and lower prices. Expansionary policy shifts AD rightward, moving back toward both original targets simultaneously. With a negative supply shock, the new equilibrium has higher prices AND lower output (stagflation). Stimulating demand fights the recession but worsens the inflation; contracting demand fights inflation but deepens the recession. There is no demand-management policy that can fix both simultaneously because the problem is the AS curve itself, not the AD curve."

- question: "A positive supply shock — such as a major productivity improvement — can simultaneously lower the price level and increase real output."
  type: true-false
  answer: true
  explanation: "A positive supply shock shifts the short-run AS curve rightward: at every price level, firms can now produce more. The new equilibrium with the same AD curve sits at higher output and a lower price level — the macroeconomic analog of a 'free lunch.' The U.S. productivity surge of the mid-1990s is the canonical example: rapid output growth with low inflation. This is why supply-side policies that genuinely raise productive capacity are macroeconomically valuable — they shift the AS curve rather than just stimulating demand."

- question: "If a central bank reacts to a negative supply shock by contracting demand enough to fully offset the resulting inflation, unemployment will return to its pre-shock level."
  type: true-false
  answer: false
  explanation: "Contracting demand (shifting AD leftward) does fight the inflation from the supply shock — it moves the equilibrium to a lower price level. But this comes at the cost of further reducing output and raising unemployment. Contractionary policy moves along the new (unfavorable) AS curve to a point with lower prices but even lower output than the initial post-shock equilibrium. To return unemployment to pre-shock levels, you would need expansionary policy — which worsens inflation. The supply shock has moved the AS curve, and no demand-management policy can undo that shift."

- question: "Explain why a negative supply shock creates a policy dilemma that a negative demand shock does not."
  type: short-answer
  answer: "A negative demand shock shifts AD leftward, producing lower output AND lower prices. Expansionary policy shifts AD rightward, restoring both output and the price level toward their original values — the two policy goals move together. A negative supply shock shifts AS leftward, producing lower output AND higher prices simultaneously (stagflation). To restore output, you must stimulate demand — but that pushes prices even higher. To fight inflation, you must contract demand — but that deepens the recession. The two policy goals are now in direct conflict, and no combination of monetary and fiscal policy can restore both simultaneously. Policymakers must choose which problem to prioritize."
  explanation: "The key is understanding that demand-management tools only move the AD curve. With a favorable AS position, AD adjustment can hit both targets. With an unfavorable AS position, you are constrained to points on the new, less-productive supply curve. The only true solution to a negative supply shock is policies that shift AS back rightward — reducing energy costs, improving technology, removing supply bottlenecks — which lie mostly outside conventional monetary and fiscal policy tools."
```

## Explainer

From your study of aggregate supply, you know that the short-run AS curve slopes upward because firms respond to unexpected price increases by expanding output — input costs are temporarily sticky. A **supply shock** is any event that abruptly changes production costs or productive capacity across the whole economy, shifting the AS curve itself rather than moving along it. Negative supply shocks — oil embargoes, pandemics disrupting supply chains, widespread drought — shift the short-run AS curve leftward: at every price level, firms now produce less because their costs have jumped.

The trouble with negative supply shocks is visible immediately on the AS-AD diagram. When AS shifts left, the new equilibrium sits at a higher price level and lower real output simultaneously. This is **stagflation** — the portmanteau of stagnation and inflation — a combination that was considered theoretically impossible under the pre-1970s consensus that inflation and unemployment were always in tension. The 1973 OPEC oil embargo demonstrated the combination was entirely real: the U.S. experienced double-digit inflation alongside a deep recession.

Here is why supply shocks create a policy dilemma that demand shocks do not. When a demand shock reduces output, policymakers can stimulate aggregate demand — cutting interest rates or increasing government spending — to shift AD rightward, restoring both output and the price level. A negative supply shock forces a choice: if you stimulate demand to fight the unemployment, you push the price level even higher; if you contract demand to fight the inflation, you deepen the recession. There is no combination of monetary and fiscal policy that simultaneously restores both objectives. Policy can pick a point on the new, less-favorable AS curve, but it cannot move the curve itself.

**Positive supply shocks** — technological breakthroughs, cheaper energy, productivity gains — are the mirror image. They shift AS rightward, raising output while lowering prices, the macroeconomic analog of a free lunch. The U.S. productivity surge of the mid-1990s is a canonical example: output expanded rapidly while inflation remained low, defying models calibrated on the demand side alone. This contrast — negative shocks force painful tradeoffs, positive shocks relax them — is why supply-side policies that durably raise productive capacity (infrastructure, education, R&D) are macroeconomically valuable beyond their direct effects. Your long-run AS knowledge completes the story: in the long run, the economy self-corrects back to potential output regardless of the shock, but "the long run" can be years of painful adjustment during which the short-run dynamics dominate policy decisions.
