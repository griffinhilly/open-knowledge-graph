---
id: new-keynesian-framework-overview
title: New Keynesian Macroeconomics Framework
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: real-business-cycle-theory
  type: soft
- id: phillips-curve
  type: hard
builds-toward:
- calvo-pricing-sticky-prices
- monetary-policy-transmission-mechanisms
tags:
- new-keynesian
- price-stickiness
- monetary-policy-effectiveness
stage: expert
status: draft
---

# New Keynesian Macroeconomics Framework

## Core Idea
New Keynesian models combine RBC foundations (agents optimize, rational expectations) with market frictions (sticky prices, monopolistic competition). This framework explains why monetary policy is non-neutral and demand shocks affect output and employment, even with forward-looking agents.

## Questions

```yaml
- question: "The central bank unexpectedly increases the money supply. In the New Keynesian model, what happens to real output in the short run?"
  type: multiple-choice
  options:
    - "Nothing — rational agents anticipate the inflation and fully adjust prices immediately, leaving real output unchanged"
    - "Real output rises temporarily because sticky prices prevent full price adjustment, so the monetary expansion lowers real interest rates and stimulates demand"
    - "Real output rises permanently because the demand expansion permanently shifts the production frontier"
    - "Real output falls because higher expected inflation discourages investment"
  answer: 1
  explanation: "The tempting wrong answer is option 0 — that rational expectations alone neutralize monetary policy, which is the RBC result. NK models keep rational expectations but add Calvo pricing: only a fraction of firms can reset prices each period. Even if agents know money supply increased, firms already locked into old prices cannot immediately raise them, so real interest rates fall and output rises. Over time, as more firms reset, prices fully adjust and output returns to its natural level. Rational expectations and monetary non-neutrality coexist because of price stickiness."

- question: "What is the central role of monopolistic competition in the New Keynesian framework?"
  type: multiple-choice
  options:
    - "It ensures firms are passive price-takers, making supply-side analysis tractable"
    - "It allows firms to set prices as a markup over marginal cost, making price-setting behavior and therefore price stickiness meaningful"
    - "It eliminates the need for sticky prices by giving each firm enough market power to resist price changes"
    - "It provides an alternative to price stickiness as the sole source of monetary non-neutrality"
  answer: 1
  explanation: "In perfect competition, firms are price-takers — there is nothing to be sticky. Monopolistic competition gives each firm a downward-sloping demand curve and the ability to set its own price. This is the prerequisite for Calvo pricing: if firms cannot choose their prices, the concept of a firm being 'unable to reset' is meaningless. Without some market power, the transmission mechanism linking monetary policy to output breaks down entirely."

- question: "The New Keynesian model predicts that monetary policy has permanent effects on real output."
  type: true-false
  answer: false
  explanation: "NK models assign monetary policy only short-run real effects. Because prices are sticky, a monetary expansion temporarily lowers real interest rates and raises output. But as firms gradually reset prices — a process that plays out over several quarters — the price level fully adjusts and output returns to its natural level determined by supply-side factors. Permanent output effects would require a structural change to productive capacity, not a demand-side monetary intervention. Money is neutral in the NK long run."

- question: "Price stickiness and rational expectations can coexist in a single macroeconomic model."
  type: true-false
  answer: true
  explanation: "This is the central innovation of the New Keynesian framework. Before NK models, many economists assumed rational expectations implied monetary policy could not have real effects — if agents fully anticipated a money supply increase, prices would jump immediately and nothing real would change. NK models showed this logic fails: even with fully rational agents, if only a fraction of firms can reset prices each period (Calvo pricing), a nominal expansion still affects real output. Rational expectations and nominal rigidities are conceptually independent."

- question: "Why does monetary policy have real effects in the New Keynesian model even though agents have rational expectations?"
  type: short-answer
  answer: "Because prices are sticky — only a fraction of firms can adjust their prices each period (Calvo pricing). Even if agents correctly anticipate a money supply increase, firms already locked into old nominal prices cannot immediately raise them. The result is lower real interest rates and higher real aggregate demand, temporarily raising output above its natural level. The non-neutrality comes from price stickiness, not from agents being surprised or fooled. Over time, as more firms reset prices, the price level fully adjusts and the real effects dissipate."
  explanation: "This is the key conceptual achievement of New Keynesian economics: reconciling rigorous microfoundations (rational, optimizing agents) with the empirical observation that monetary policy moves real variables. The source of non-neutrality is firmly on the supply side of price adjustment — how frequently firms can reset prices — not on agents' information or expectations."
```

## Explainer

If you have studied real business cycle (RBC) theory, you know its central claim: business cycles can be explained by technology shocks propagated through the optimizing decisions of rational agents, with no role for monetary policy or demand-side forces. And from your work on the Phillips curve, you know the empirical regularity linking inflation and unemployment. The **New Keynesian framework** was built to reconcile these two traditions — keeping the rigorous microfoundations of RBC theory while restoring a meaningful role for monetary policy and demand.

The framework rests on two key departures from the RBC baseline. First, firms operate under **monopolistic competition** rather than perfect competition. Each firm produces a slightly differentiated product and faces a downward-sloping demand curve, giving it some market power. This means firms set prices as a markup over marginal cost rather than being passive price-takers. Second, prices are **sticky** — firms cannot freely adjust their prices every period. The most common specification is Calvo pricing, where each firm faces a random probability of being able to reset its price in any given period. Together, these two frictions transform the model's behavior: when the central bank changes the money supply or interest rate, prices do not adjust immediately, so changes in nominal spending translate into changes in real output and employment.

The canonical three-equation New Keynesian model consists of a **dynamic IS curve** (linking the output gap to the real interest rate and expected future output), a **New Keynesian Phillips Curve** (linking inflation to the output gap and expected future inflation), and a **monetary policy rule** (typically a Taylor rule specifying how the central bank sets interest rates in response to inflation and the output gap). The IS curve says that when real interest rates fall, households substitute future consumption for present consumption (from your Euler equation work), increasing aggregate demand. The Phillips curve says that higher demand pushes up firms' marginal costs, and the fraction of firms that can reset prices will raise them, generating inflation. The monetary policy rule closes the system by describing how the central bank reacts.

The framework's central achievement is explaining **monetary non-neutrality with fully rational agents**. In an RBC model, an increase in the money supply raises all prices proportionally and nothing real changes. In the New Keynesian model, because only a fraction of firms can adjust prices immediately, a monetary expansion lowers real interest rates, stimulates demand, and raises output — money has real effects in the short run. Over time, as more firms reset their prices, the price level fully adjusts and output returns to its natural level. This gives a precise, microfounded answer to how monetary policy works, how long its effects last, and why central banks can stabilize the economy through interest rate adjustments — the intellectual foundation of modern central banking practice.
