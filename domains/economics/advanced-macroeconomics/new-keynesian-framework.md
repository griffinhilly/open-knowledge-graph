---
id: new-keynesian-framework
title: New Keynesian Economics Framework
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: real-business-cycle-theory
  type: hard
- id: phillips-curve
  type: hard
- id: systems-of-linear-equations
  type: hard
- id: optimization-multivariable-basics
  type: soft
builds-toward:
- calvo-pricing-sticky-prices
- phillips-curve-new-keynesian
- dsge-models
tags:
- new-keynesian
- nominal-rigidities
- imperfect-competition
stage: advanced
status: draft
---

# New Keynesian Economics Framework

## Core Idea
New Keynesian macroeconomics combines microfounded optimization (from RBC theory) with nominal rigidities and imperfect competition. The framework recognizes that prices and wages do not adjust instantly to clear markets, creating room for monetary policy to affect real variables in the short run. New Keynesian models explain why inflation responds sluggishly to demand shocks, why unemployment fluctuates, and why monetary policy can stabilize the economy—addressing key empirical facts that RBC theory struggles with.

## Explainer

From your study of Real Business Cycle theory and the Phillips curve, you have two pieces of the puzzle that New Keynesian economics assembles. RBC theory showed how to build macroeconomic models from microeconomic foundations — optimizing households and firms making intertemporal decisions — but concluded that business cycles are efficient responses to real (technology) shocks, leaving no role for monetary policy. The Phillips curve, meanwhile, documents an empirical relationship between inflation and economic activity that RBC theory cannot explain. New Keynesian economics keeps the microfoundations but adds two ingredients that restore monetary non-neutrality: **imperfect competition** and **nominal rigidities**.

**Imperfect competition** means firms have some market power — they are price setters, not price takers. This matters because in a perfectly competitive market, firms always charge marginal cost and have no discretion over pricing. With monopolistic competition, each firm produces a slightly differentiated product and faces a downward-sloping demand curve, giving it a markup over marginal cost. This setup is necessary for nominal rigidities to matter: if firms were price takers, any individual firm's inability to change its price would be irrelevant because the market would determine the price. With market power, each firm's pricing decision has real consequences. **Nominal rigidities** mean that firms cannot or do not adjust their prices every period — perhaps because of menu costs, information costs, or contractual arrangements. The combination is decisive: firms with market power that cannot adjust prices immediately will respond to changes in demand by changing output rather than price, creating the short-run real effects of monetary policy.

The canonical three-equation New Keynesian model consists of a **dynamic IS curve**, a **New Keynesian Phillips Curve**, and a **monetary policy rule**. The IS curve, derived from household optimization, relates the output gap to the real interest rate — higher real rates reduce consumption and investment, shrinking the gap. It is "dynamic" because today's output depends on expected future output through consumption smoothing. The Phillips Curve, derived from firm optimization under staggered pricing, relates current inflation to expected future inflation and the output gap — firms that get to reset prices set them higher when demand is strong. The monetary policy rule (typically a Taylor rule) describes how the central bank sets the nominal interest rate in response to inflation and the output gap.

This three-equation system captures the essential New Keynesian insight: monetary policy works because it manipulates the real interest rate in an economy where prices adjust sluggishly. When the central bank cuts the nominal rate and inflation expectations are anchored, the real rate falls, stimulating demand through the IS curve. Because prices are sticky, this higher demand translates into higher real output rather than just higher prices — at least in the short run. Over time, as firms gradually reset prices, inflation rises through the Phillips curve, real rates return to their natural level, and output returns to potential. The framework thus explains both why monetary policy has real effects and why those effects are temporary — providing the intellectual foundation for modern central banking.
