---
id: covered-and-uncovered-interest-parity
title: Interest Rate Parity
domain: economics
course: macroeconomics
prerequisites:
- id: interest-rates-and-loanable-funds
  type: hard
- id: exchange-rate-dynamics
  type: hard
builds-toward:
- exchange-rate-regimes-and-monetary-policy
tags:
- interest-rates
- parity
- exchange-rates
stage: advanced
status: draft
---

# Interest Rate Parity

## Core Idea
Interest rate parity (IRP) requires that the interest rate differential between two countries equals the expected change in the exchange rate: investors must earn the same return in both currencies after accounting for currency depreciation. Covered IRP (using forward contracts) holds almost exactly due to arbitrage; uncovered IRP relies on rational expectations and holds less precisely. IRP links monetary policy across countries in the open economy.

## Explainer

You already know that interest rates are determined in the loanable funds market and that exchange rates are driven by supply and demand for currencies. Interest rate parity is the condition that ties these two markets together in an open economy: if capital can flow freely across borders, investors will move funds toward whatever currency offers a higher return — and their collective behavior will equalize returns across countries after accounting for expected currency movements.

Start with the basic logic. Suppose the U.S. offers a 5% annual interest rate and the eurozone offers 3%. A U.S. investor considering parking money in euros will earn 3% but must also accept whatever happens to the dollar/euro exchange rate over the year. If the euro is expected to appreciate by 2% against the dollar, the euro investment effectively earns 3% + 2% = 5% in dollar terms — matching the domestic rate. If the euro were instead expected to depreciate, the dollar investment would dominate, and investors would sell euros, bidding the euro down until the expected depreciation exactly offset the interest differential. This is the core of **interest rate parity**: the interest differential equals the expected exchange rate change.

**Covered interest parity (CIP)** is the no-arbitrage version. Instead of expecting a future exchange rate, you *lock it in today* using a forward contract. You borrow in dollars, convert to euros at today's spot rate, earn the euro interest rate, and simultaneously agree today to convert your euros back to dollars at the forward rate. CIP says the profit from this round-trip must be zero — otherwise, arbitrageurs with access to forward markets would exploit it indefinitely. Because CIP depends only on observable, contractually fixed prices (spot rate, forward rate, and two interest rates), it holds almost perfectly for comparable assets in liquid markets with no capital controls. Violations of CIP are typically small and fleeting — and when they appear persistently (as they did in the 2008 crisis), it signals stress in the banking system's ability to intermediate capital flows.

**Uncovered interest parity (UIP)** relaxes the forward contract and substitutes the market's *expectation* of the future exchange rate. UIP must therefore hold in expectation rather than by arbitrage, and whether it actually holds is an empirical question. The evidence is mixed: UIP holds reasonably well at very long horizons and for some country pairs, but over short horizons the "forward premium puzzle" documents that high-interest currencies often *appreciate* rather than depreciate as UIP predicts — the opposite of what the theory says. This empirical failure is one of the most studied puzzles in international finance, with explanations ranging from risk premia to peso problems to irrational expectations. The important lesson is that CIP is a near-identity enforced by arbitrage, while UIP is an equilibrium condition enforced only by expectations — and expectations can be wrong for a long time.
