---
id: currency-derivatives-and-hedging
title: Currency Derivatives and Foreign Exchange Hedging
domain: economics
course: financial-economics
prerequisites:
- id: forward-pricing-cost-of-carry
  type: hard
- id: covered-and-uncovered-interest-parity
  type: hard
tags:
- fx
- hedging
- derivatives
stage: advanced
status: draft
---

# Currency Derivatives and Foreign Exchange Hedging

## Core Idea
Currency hedging protects against exchange rate fluctuations using forwards, futures, options, and swaps. Forward contracts lock in exchange rates using covered interest rate parity. Option-based hedges protect against adverse moves while preserving upside. The choice between hedging tools depends on cost, accounting treatment, and risk tolerance.

## Explainer

You know from covered interest rate parity (CIP) that forward exchange rates are not forecasts of the future spot rate — they are prices derived from the no-arbitrage relationship between spot rates and interest rate differentials. Specifically, the forward rate F = S × (1 + r_d)/(1 + r_f), where S is the current spot rate and r_d, r_f are domestic and foreign interest rates. This pricing relationship is the foundation of **currency hedging**: because you can lock in a future exchange rate through a forward contract at a known, arbitrage-free price, you can eliminate currency exposure from a future cash flow.

Consider a US exporter expecting to receive €1 million in three months. If the euro depreciates by the time payment arrives, the dollar value of that receivable shrinks. A **currency forward** solves this: enter a forward contract to sell €1 million in three months at today's three-month forward rate. Whatever the spot rate turns out to be at settlement, the exporter receives the locked-in forward rate. The hedge converts uncertain future foreign-currency cash flows into a certain domestic-currency amount — the uncertainty is not reduced in the world, but it is transferred to the counterparty. The cost of this certainty is embedded in the forward-spot differential, which CIP tells you equals the interest rate differential.

**Currency options** offer a different risk profile. A **put option** on euros gives the holder the right — but not the obligation — to sell euros at the strike price. If the euro falls below the strike, the put pays off; if the euro stays high, the holder simply lets the option expire and benefits from the favorable spot rate. This asymmetric payoff is the key distinction from a forward: the forward eliminates all exchange rate risk (good and bad), while the put eliminates only downside risk. The price of this asymmetry is the **option premium**, paid upfront regardless of whether the option is exercised. Firms with uncertain foreign-currency cash flows (they might receive €1 million, or maybe less, depending on sales) often prefer options over forwards for this reason.

The choice among hedging instruments — forward, futures, option, swap, or a combination — depends on several practical factors. **Forwards** are customizable in amount and maturity (OTC contracts) but carry counterparty credit risk. **Currency futures** are exchange-traded and thus standardized and marked to market daily, eliminating counterparty risk but introducing basis risk if the maturity and amount don't match perfectly. **Cross-currency swaps** exchange principal and interest cash flows in two currencies and are suited for longer-horizon exposures like foreign-currency debt. Accounting treatment also matters: hedges that qualify for hedge accounting under IFRS or US GAAP allow gains and losses to offset the hedged item in the income statement rather than creating earnings volatility — so treasurers often structure hedges to satisfy accounting as much as to minimize risk economically.
