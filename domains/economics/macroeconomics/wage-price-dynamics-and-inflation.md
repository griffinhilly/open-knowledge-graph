---
id: wage-price-dynamics-and-inflation
title: Wage-Price Dynamics and the Inflation Process
domain: economics
course: macroeconomics
prerequisites:
- id: medium-run-nairu-equilibrium
  type: hard
- id: phillips-curve
  type: soft
builds-toward:
- supply-shock-stagflation-effects
tags:
- wages
- prices
- inflation
- expectations
- wage-price-spiral
stage: advanced
status: validated
---

# Wage-Price Dynamics and the Inflation Process

## Core Idea
Wage-price dynamics describe how wages and prices interact. When unemployment falls below NAIRU, labor scarcity drives wages up; firms pass increases into prices, creating inflation. If expectations embed higher inflation, a wage-price spiral develops.

## How It's Best Learned
Trace a wage-price spiral: tight labor → wage demands rise → firms raise prices → inflation expectations rise → workers demand higher wages. Show how central bank credibility interrupts the spiral.

## Common Misconceptions
- Assuming instant wage-price adjustment; lags from contracts are significant.
- Treating inflation expectations as unchanging.
- Confusing cost-push with demand-pull inflation.

## Questions

```yaml
- question: "Unemployment falls below NAIRU, and wages rise 5%. A year later, inflation is running at 4%. Workers observe the price increases and revise their inflation expectations upward, believing elevated inflation is now permanent. What is the most likely next step in the dynamic?"
  type: multiple-choice
  options:
    - "The spiral automatically corrects as firms lower prices to regain competitiveness against foreign producers."
    - "Workers demand nominal wage increases exceeding 4% in the next contract cycle to protect real wages, potentially driving another round of price increases — a self-reinforcing wage-price spiral."
    - "The central bank's published inflation target automatically prevents workers from embedding higher inflation into wage demands."
    - "Higher wages reduce consumer purchasing power, cooling demand and halting inflation without further policy action."
  answer: 1
  explanation: "The spiral becomes self-sustaining when inflation expectations become unanchored. Once workers believe higher inflation is permanent, they demand nominal wage increases above the current inflation rate to prevent real wage erosion. Firms, facing higher labor costs, raise prices again. This validates workers' expectations and triggers the next round of wage demands. The central bank's target (option C) only anchors expectations if workers believe the bank will act — mere publication of a target is insufficient. Option D confuses the direction: higher nominal wages, if matched by price increases, leave real wages unchanged and do not cool demand."

- question: "A credible central bank preemptively raises interest rates when unemployment falls modestly below NAIRU, before inflation accelerates significantly. How does this preemptive action interrupt the wage-price spiral?"
  type: multiple-choice
  options:
    - "Higher interest rates directly reduce nominal wages by lowering firm profits and wage-setting power."
    - "Workers and firms, believing the central bank will cool demand sufficiently to return unemployment toward NAIRU, refrain from embedding higher inflation into wage and price expectations — so the spiral never becomes self-sustaining."
    - "Interest rate increases directly compensate workers for anticipated inflation, reducing their incentive to demand higher wages."
    - "Preemptive action only matters after a spiral has started; credibility cannot prevent one from beginning."
  answer: 1
  explanation: "Central bank credibility operates through expectations. If workers and firms believe the bank will act decisively — raising rates enough to slow demand and push unemployment back toward NAIRU — they anticipate that any wage-price spiral will be cut short. Rationally, they moderate their wage and price demands, keeping expectations anchored near the target. The spiral requires unanchored expectations to become self-sustaining; credibility prevents unanchoring. This is why well-established inflation-targeting regimes can achieve lower average inflation with less variability than less credible regimes — the threat of action is itself disinflationary."

- question: "Demand-pull inflation and cost-push inflation are driven by the same underlying mechanism: excess money supply pushing prices up across the economy."
  type: true-false
  answer: false
  explanation: "These are distinct mechanisms with different policy implications. Demand-pull inflation originates in the labor market: unemployment below NAIRU creates wage pressure that firms pass into prices, as described in this topic. Cost-push inflation originates on the supply side: an exogenous increase in production costs (energy prices, supply disruptions, import prices) directly raises firms' costs and forces them to choose between absorbing the squeeze or raising prices — independent of any labor market tightening. Both can coexist and interact, but they require different policy responses. Demand-pull calls for cooling demand; cost-push creates a dilemma because demand cooling would add unemployment without addressing the cost shock."

- question: "Because wages in many industries are set by multi-year contracts, the inflationary effect of unemployment falling below NAIRU may not fully materialize for months or years after the labor market tightens."
  type: true-false
  answer: true
  explanation: "This lag structure is a defining feature of wage-price dynamics. When unemployment drops below NAIRU today, only workers whose contracts are expiring soon can immediately negotiate higher wages; workers under existing multi-year contracts must wait. As contracts roll over in subsequent months and years, more workers can demand catch-up wage increases, gradually building the inflationary pressure into the price level. This lag means the Phillips curve relationship operates with delay: policymakers who wait for measured inflation to rise before tightening policy may already be behind the curve, responding to wage pressures that were locked in months earlier."

- question: "Why are unanchored inflation expectations necessary for a wage-price spiral to become self-sustaining? What role does central bank credibility play in preventing this outcome?"
  type: short-answer
  answer: "A single round of wage increases feeding into price increases does not constitute a spiral — it is a level adjustment that can stop after one round if everyone believes inflation will return to normal. The spiral becomes self-sustaining only when workers and firms embed expected future inflation into their wage and price decisions: workers demand wages above current inflation to stay ahead, firms set prices above current costs to stay ahead, and each round validates the other's expectations. Central bank credibility interrupts this by making low-inflation expectations self-fulfilling: if workers believe the bank will tighten aggressively enough to restore NAIRU, they have no reason to demand excess wage increases, firms have no reason to set prices aggressively, and the spiral never forms. Credibility means the bank's commitment is believed in advance, not just demonstrated after the fact."
  explanation: "The spiral is essentially a coordination failure: if everyone expects low inflation and acts on that expectation, inflation stays low; if everyone expects high inflation and acts on it, inflation accelerates. Central bank credibility selects the low-inflation equilibrium by making the bank's response predictable and decisive. Loss of credibility — through delayed action, inconsistent targets, or political interference — tips the economy toward the high-inflation coordination equilibrium, and breaking out of it typically requires a painful recession to demonstrate resolve."
```

## Explainer

To understand wage-price dynamics, start from the NAIRU framework you already know. When unemployment falls below the non-accelerating-inflation rate, firms are competing for a shrinking pool of workers. To attract and retain employees, they raise wages. So far this is just a tight labor market. The inflationary spiral begins when those higher wages feed forward into prices: firms facing higher labor costs must either accept lower profit margins or raise the prices they charge customers. Most competitive firms do the latter, so a broad wage increase translates into a broad price increase.

Here is where expectations become decisive. If workers and firms treat the price increase as a one-time adjustment, the spiral stops. But if workers observe rising prices and conclude that the cost of living is permanently higher, they demand still-higher wages in the next contract negotiation — and the cycle begins again. This self-reinforcing mechanism is the **wage-price spiral**: each round of wage increases drives price increases, which drive further wage demands. The spiral is not automatic; it depends on whether inflation expectations become **unanchored** from the central bank's target.

The **inflation process** has a meaningful lag structure that distinguishes it from instantaneous price adjustment. Wages in many industries are set by multi-year contracts, so even when unemployment drops below NAIRU today, the wage response may not fully materialize for months or years as existing contracts expire and new ones are negotiated. Similarly, firms may absorb higher costs briefly before passing them through to prices. This lag means the Phillips curve relationship — lower unemployment predicts higher inflation — operates with delay, and policymakers must anticipate rather than react.

Central bank credibility is the mechanism that can interrupt the spiral before it becomes self-sustaining. If households and firms believe the central bank will raise interest rates aggressively enough to cool demand and return unemployment toward NAIRU, they may refrain from embedding higher inflation into wage and price-setting expectations. In this case, expectations remain anchored and the initial wage-price pressure dissipates without a full spiral. But if the central bank delays action or is perceived as insufficiently committed to its inflation target, expectations de-anchor, the spiral takes hold, and restoring price stability requires a much more painful demand contraction — a recession deep enough to re-establish that higher unemployment will discipline wage demands.

Finally, it is worth distinguishing this **demand-pull** story (unemployment below NAIRU pulls wages and prices up) from **cost-push** inflation, where a supply shock — say, an energy price spike — raises firms' production costs directly, before any labor market tightening. Cost-push shocks force an uncomfortable trade-off: letting prices rise to accommodate the shock, or suppressing demand to hold prices down at the cost of higher unemployment. Demand-pull and cost-push are not always cleanly separable in practice, but the distinction matters for policy because the appropriate response differs.
