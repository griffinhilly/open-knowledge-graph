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
- id: euler-equation-consumption
  type: hard
- id: technology-shocks-rbc
  type: soft
builds-toward:
- calvo-pricing-sticky-prices
- phillips-curve-new-keynesian
- dsge-models
tags:
- new-keynesian
- nominal-rigidities
- imperfect-competition
stage: expert
status: validated
---

# New Keynesian Economics Framework

## Core Idea
New Keynesian macroeconomics combines microfounded optimization (from RBC theory) with nominal rigidities and imperfect competition. The framework recognizes that prices and wages do not adjust instantly to clear markets, creating room for monetary policy to affect real variables in the short run. New Keynesian models explain why inflation responds sluggishly to demand shocks, why unemployment fluctuates, and why monetary policy can stabilize the economy—addressing key empirical facts that RBC theory struggles with.

## Questions

```yaml
- question: "In a New Keynesian model, a central bank cuts the nominal interest rate. Inflation expectations are well-anchored. What is the short-run effect on real output, and why?"
  type: multiple-choice
  options:
    - "Real output is unchanged — lower nominal rates just produce proportionally lower prices with no real effect"
    - "Real output increases — because prices are sticky, the real interest rate falls, stimulating demand that translates into higher output rather than immediately higher prices"
    - "Real output decreases — lower nominal rates signal that the central bank expects a recession, reducing confidence"
    - "Real output increases, but only because the central bank also changed the money supply"
  answer: 1
  explanation: "This is the core transmission mechanism of New Keynesian monetary policy. With sticky prices, a cut in the nominal rate lowers the real interest rate (real rate = nominal rate − expected inflation, and inflation expectations are anchored). A lower real rate makes borrowing cheaper and saving less attractive, stimulating consumption and investment via the dynamic IS curve. Because prices cannot adjust instantly, the extra demand shows up as higher real output, not just higher prices. In the long run, as firms gradually reset prices, inflation rises and output returns to potential — but the short-run real effect is real."

- question: "A New Keynesian economist argues that imperfect competition is a necessary ingredient — not just a technical convenience — for nominal rigidities to have macroeconomic effects. What is the logic?"
  type: multiple-choice
  options:
    - "Perfect competition causes deflation, which amplifies the effects of sticky prices"
    - "In perfect competition, firms are price-takers with no discretion over pricing, so a firm that 'cannot adjust its price' faces a non-issue — price stickiness only bites when firms have pricing power"
    - "Imperfect competition allows firms to hold inventories, which cushion demand shocks and create the appearance of real effects"
    - "Perfect competition produces too much output, and nominal rigidities are needed to reduce it to the efficient level"
  answer: 1
  explanation: "In a perfectly competitive market, the market price is determined by the intersection of supply and demand — individual firms have no pricing decision to be sticky *about*. If a price-taking firm 'cannot adjust,' it simply sells whatever the market price is, as before. Nominal rigidities matter only when firms have market power and therefore *set* prices. A monopolistically competitive firm with a downward-sloping demand curve has a pricing decision; if that decision is constrained by menu costs or contracts, it cannot respond to demand shocks by raising prices, and output must absorb the adjustment instead. Imperfect competition is what makes the pricing decision exist in the first place."

- question: "In the New Keynesian framework, monetary policy has real effects in the short run but only nominal effects in the long run."
  type: true-false
  answer: true
  explanation: "This is one of the central results of the New Keynesian model and the key distinction from both RBC theory (no real effects at any horizon) and old Keynesian theory (permanent real effects). In the short run, sticky prices mean demand shocks translate into output changes. Over time, as firms gradually reset their prices (in the Calvo pricing model, a random fraction reprices each period), the price level adjusts, the real interest rate returns to its natural level, and output returns to its potential. The long-run neutrality of money is preserved — only the path differs from the RBC view, not the eventual destination."

- question: "The New Keynesian Phillips Curve states that current inflation depends on past inflation and the current output gap."
  type: true-false
  answer: false
  explanation: "The New Keynesian Phillips Curve (NKPC) is forward-looking: current inflation depends on *expected future inflation* and the current output gap. This is derived from the optimal pricing behavior of firms that can only reset prices infrequently — a firm setting its price today must forecast the entire future path of marginal costs, which depends on expected future demand. The backward-looking specification (inflation depends on past inflation) characterizes the adaptive expectations Phillips curve of the old Keynesian era. The forward-looking nature of the NKPC has important implications: credible central bank commitments to future policy can directly influence current inflation through expectations."

- question: "Why do New Keynesian models require *both* imperfect competition and nominal rigidities to generate real effects of monetary policy? What does each ingredient contribute, and why is neither sufficient alone?"
  type: short-answer
  answer: "Imperfect competition gives firms pricing power — they set prices rather than taking them from the market. Nominal rigidities mean those prices adjust slowly. Both are necessary: without market power, stickiness is irrelevant because firms have no pricing decision to be sticky about. Without stickiness, market power doesn't prevent immediate price adjustment — firms with power can simply reprice instantly when demand changes, eliminating real effects. Together, they create firms that *can* set prices but *don't* adjust them quickly, so demand shocks hit output rather than prices in the short run."
  explanation: "This is the logical core of the New Keynesian synthesis. RBC models have microfounded optimization but no nominal rigidities, producing monetary neutrality. Old Keynesian models have demand-driven output but no microfoundations. New Keynesian models thread the needle: the microfoundations (imperfect competition, intertemporal optimization) justify why firms have a pricing decision, and the rigidities (menu costs, staggered contracts) explain why that decision responds slowly. The interaction is what produces the non-neutrality."
```

## Explainer

From your study of Real Business Cycle theory and the Phillips curve, you have two pieces of the puzzle that New Keynesian economics assembles. RBC theory showed how to build macroeconomic models from microeconomic foundations — optimizing households and firms making intertemporal decisions — but concluded that business cycles are efficient responses to real (technology) shocks, leaving no role for monetary policy. The Phillips curve, meanwhile, documents an empirical relationship between inflation and economic activity that RBC theory cannot explain. New Keynesian economics keeps the microfoundations but adds two ingredients that restore monetary non-neutrality: **imperfect competition** and **nominal rigidities**.

**Imperfect competition** means firms have some market power — they are price setters, not price takers. This matters because in a perfectly competitive market, firms always charge marginal cost and have no discretion over pricing. With monopolistic competition, each firm produces a slightly differentiated product and faces a downward-sloping demand curve, giving it a markup over marginal cost. This setup is necessary for nominal rigidities to matter: if firms were price takers, any individual firm's inability to change its price would be irrelevant because the market would determine the price. With market power, each firm's pricing decision has real consequences. **Nominal rigidities** mean that firms cannot or do not adjust their prices every period — perhaps because of menu costs, information costs, or contractual arrangements. The combination is decisive: firms with market power that cannot adjust prices immediately will respond to changes in demand by changing output rather than price, creating the short-run real effects of monetary policy.

The canonical three-equation New Keynesian model consists of a **dynamic IS curve**, a **New Keynesian Phillips Curve**, and a **monetary policy rule**. The IS curve, derived from household optimization, relates the output gap to the real interest rate — higher real rates reduce consumption and investment, shrinking the gap. It is "dynamic" because today's output depends on expected future output through consumption smoothing. The Phillips Curve, derived from firm optimization under staggered pricing, relates current inflation to expected future inflation and the output gap — firms that get to reset prices set them higher when demand is strong. The monetary policy rule (typically a Taylor rule) describes how the central bank sets the nominal interest rate in response to inflation and the output gap.

This three-equation system captures the essential New Keynesian insight: monetary policy works because it manipulates the real interest rate in an economy where prices adjust sluggishly. When the central bank cuts the nominal rate and inflation expectations are anchored, the real rate falls, stimulating demand through the IS curve. Because prices are sticky, this higher demand translates into higher real output rather than just higher prices — at least in the short run. Over time, as firms gradually reset prices, inflation rises through the Phillips curve, real rates return to their natural level, and output returns to potential. The framework thus explains both why monetary policy has real effects and why those effects are temporary — providing the intellectual foundation for modern central banking.
