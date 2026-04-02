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
- id: hedging-with-derivatives
  type: soft
- id: optimal-hedge-ratio-calculation
  type: soft
- id: interest-rate-swaps-mechanics
  type: soft
tags:
- fx
- hedging
- derivatives
stage: expert
status: validated
---
# Currency Derivatives and Foreign Exchange Hedging

## Core Idea
Currency hedging protects against exchange rate fluctuations using forwards, futures, options, and swaps. Forward contracts lock in exchange rates using covered interest rate parity. Option-based hedges protect against adverse moves while preserving upside. The choice between hedging tools depends on cost, accounting treatment, and risk tolerance.

## Questions

```yaml
- question: "A US technology firm has won a contract to supply services to a European client, with payment of up to €2 million in six months — but the actual amount depends on acceptance testing and may be anywhere from €0 to €2 million. Which hedging instrument is most appropriate?"
  type: multiple-choice
  options:
    - "A forward contract to sell exactly €2 million in six months, locking in the full expected payment"
    - "A currency put option on up to €2 million, providing downside protection while accommodating uncertainty in the actual amount received"
    - "A cross-currency swap exchanging euro principal for dollar principal over six months"
    - "No hedge is possible because uncertain receivables cannot be hedged"
  answer: 1
  explanation: "When the amount of a foreign-currency cash flow is uncertain, a forward contract is problematic: if the firm over-hedges (contracts to sell more euros than it receives), it faces an obligation to deliver euros it doesn't have. A currency put option avoids this because it is a right, not an obligation — if the firm receives less than expected, it simply exercises the option for the actual amount received. The put provides downside protection against euro depreciation while preserving flexibility. The option premium is the cost of this flexibility."

- question: "A US company enters a forward contract to sell €5 million at 1.10 USD/EUR in 3 months. At settlement, the spot rate is 1.20 USD/EUR. What is the economic consequence for the company?"
  type: multiple-choice
  options:
    - "The company profits because the forward rate exceeded the original spot rate"
    - "The company must sell €5 million at 1.10, receiving $5.5M instead of the $6.0M available at the market rate — a foregone gain of $500,000"
    - "The forward contract is automatically cancelled because market conditions changed"
    - "The company can choose whether to honor the forward contract based on which rate is more favorable"
  answer: 1
  explanation: "A forward contract is an obligation, not an option. The company is contractually bound to sell €5 million at 1.10 regardless of the market rate. At 1.20, it receives $5.5M instead of $6.0M — a foregone gain of $500,000. This is the fundamental tradeoff of forward hedging: it eliminates both the downside risk (euro falling below 1.10) AND the upside potential (euro rising above 1.10). The hedge converts a risky cash flow into a certain one, transferring both types of risk to the counterparty."

- question: "Currency forward rates serve as the market's best forecast of where the spot exchange rate will be at the contract's maturity date."
  type: true-false
  answer: false
  explanation: "This is a persistent misconception. Forward rates are not forecasts — they are arbitrage-free prices derived from covered interest rate parity: F = S × (1 + r_d)/(1 + r_f). The forward rate reflects the current spot rate adjusted for the interest rate differential between the two currencies. If a currency has higher domestic interest rates, its forward rate will be at a discount (lower than spot) to prevent risk-free arbitrage, not because the market expects the currency to weaken. Empirically, forward rates are poor predictors of future spot rates."

- question: "A currency put option is more valuable than a forward contract for the same notional amount and maturity because the option provides asymmetric payoff — downside protection without forgoing upside potential."
  type: true-false
  answer: true
  explanation: "The put option's asymmetric payoff — it pays off when the currency falls below the strike but allows the holder to benefit from appreciation — is more valuable than the symmetric payoff of a forward. The forward transfers risk at zero upfront cost because it merely locks in the arbitrage-free forward rate; any gain from the forward being 'right' is offset by the loss from it being 'wrong.' The option provides insurance: the worst case is limited to the premium paid plus any depreciation above the strike. This one-sided risk reduction is worth paying for, reflected in the option premium."

- question: "Explain why covered interest rate parity (CIP) determines forward exchange rates, and what would happen if forward rates deviated significantly from CIP."
  type: short-answer
  answer: "CIP states that the return from investing domestically must equal the return from converting to a foreign currency, investing at the foreign rate, and locking in the exchange rate back via a forward contract. Algebraically: F = S × (1 + r_d)/(1 + r_f). If the forward rate deviated from this, arbitrageurs could earn a risk-free profit: borrow in the low-rate currency, invest in the high-rate currency, and use a forward contract to convert back, pocketing the difference with no risk. This arbitrage would immediately drive the forward rate back toward the CIP-implied price. The forward rate is therefore not a prediction of the future spot rate — it is the price at which arbitrage is unprofitable."
  explanation: "This no-arbitrage logic is fundamental to derivatives pricing. CIP violations have been documented empirically during the 2008 financial crisis and after, when counterparty risk and dollar funding constraints made arbitrage risky or impossible for a period. In normal markets, CIP holds to tight tolerances for major currency pairs."
```

## Questions

```yaml
- question: "A US importer must pay €1 million in 3 months. The spot rate is 1.10 USD/EUR; the 3-month forward rate is 1.08 USD/EUR. A bank analyst forecasts the euro will fall to 1.07. Should the importer enter the forward contract based on this forecast?"
  type: multiple-choice
  options:
    - "Yes — the forward rate of 1.08 is above the forecast spot of 1.07, so the forward locks in a favorable rate compared to the expected outcome"
    - "No — the forward rate is not a forecast; it is an arbitrage-free price set by interest rate differentials. The hedging decision should be based on the importer's risk tolerance, not whether the forward is above or below a spot rate forecast"
    - "Yes — forward rates always predict future spot rates better than bank analysts, so the importer should trust the forward"
    - "No — importers should only use options, never forwards, because forwards carry counterparty credit risk"
  answer: 1
  explanation: "The covered interest rate parity (CIP) relationship tells us that forward rates are *not* forecasts — they are determined by the no-arbitrage condition F = S × (1 + r_d)/(1 + r_f). The forward rate reflects the interest rate differential between currencies, not the market's consensus expectation of where the spot rate will be. A decision to hedge using a forward should be based on whether the importer wants to eliminate the currency uncertainty in its cash flows — a risk management question — not on a comparison of the forward rate to a spot rate forecast."

- question: "A US exporter expects to receive between €500,000 and €1,000,000 in 6 months — the exact amount depends on whether a large order is confirmed. Which hedging instrument is most appropriate?"
  type: multiple-choice
  options:
    - "A currency forward for €1 million — locks in the maximum amount at today's forward rate"
    - "A put option on €1 million — provides downside protection if the euro depreciates while allowing flexibility if the full amount is not received"
    - "A cross-currency swap for 6 months — best suited to trade receivables with uncertain amounts"
    - "No hedge is possible when the amount is uncertain"
  answer: 1
  explanation: "When cash flow amounts are uncertain, options are preferred over forwards. A forward obligates the exporter to deliver exactly €1 million at the locked-in rate — if only €500K materializes, the exporter would be short €500K and must buy euros at the spot rate to deliver, potentially at a loss. A put option gives the *right* (not obligation) to sell euros at the strike price; if the full €1 million is received and the euro has appreciated, the exporter simply lets the option expire and benefits from the favorable spot rate. The cost is the option premium. Option A illustrates the classic over-hedging risk of forwards when notional amounts are uncertain."

- question: "The three-month forward exchange rate between USD and EUR is determined by the no-arbitrage relationship between the spot rate and the interest rate differential between the two currencies, not by market expectations of where the spot rate will be in three months."
  type: true-false
  answer: true
  explanation: "This is the covered interest rate parity (CIP) result: F = S × (1 + r_USD)/(1 + r_EUR). If the forward rate deviated from this, risk-free arbitrage profits would be available by borrowing in one currency, converting at spot, investing in the other, and locking in the return at the forward rate. This arbitrage keeps forward rates anchored to the interest differential. CIP holds reliably in developed-market currency pairs, unlike uncovered interest rate parity (UIP), which predicts actual future spot rates but fails empirically."

- question: "Buying a currency put option on a foreign-currency receivable provides the same complete elimination of exchange rate risk as entering a currency forward contract."
  type: true-false
  answer: false
  explanation: "A forward eliminates *all* exchange rate risk — both adverse and favorable movements. If the foreign currency appreciates, the exporter loses that upside gain because they're committed to the forward rate. A put option only eliminates *downside* risk: if the currency falls below the strike, the put pays off; if it rises, the holder lets the option expire and benefits from the favorable spot rate. This asymmetric payoff — protection without surrendering upside — is precisely what distinguishes options from forwards, and precisely why options carry an upfront premium. The forward is a risk transfer; the option is a risk elimination on one side only."

- question: "Explain why a currency forward contract is said to 'transfer' currency risk rather than 'eliminate' it from the world, and what this means for the cost of hedging."
  type: short-answer
  answer: "A forward contract shifts the currency risk from the hedger to the counterparty (typically a bank or another corporate with offsetting exposure). The uncertainty about the future spot rate still exists in the world — it is simply borne by someone else. The hedger converts an uncertain future foreign-currency cash flow into a certain domestic-currency amount. The 'cost' of this transfer is embedded in the forward-spot differential (determined by the interest rate differential via CIP) and any bid-ask spread. If the hedger's home currency interest rate is lower than the foreign rate, the forward rate will be at a premium (the hedge costs something in expectation); if higher, the forward is at a discount. This is not a fee but a fair price reflecting the opportunity cost of locking in versus remaining exposed."
  explanation: "Students often conflate 'hedging eliminates risk' with 'hedging destroys risk.' The distinction matters because it clarifies that forward pricing is not arbitrary — it is the equilibrium price at which someone else is willing to bear the risk the hedger no longer wants. This also explains why hedging is not free even when there is no explicit fee: the cost is embedded in the forward premium or discount."
```

## Explainer

You know from covered interest rate parity (CIP) that forward exchange rates are not forecasts of the future spot rate — they are prices derived from the no-arbitrage relationship between spot rates and interest rate differentials. Specifically, the forward rate F = S × (1 + r_d)/(1 + r_f), where S is the current spot rate and r_d, r_f are domestic and foreign interest rates. This pricing relationship is the foundation of **currency hedging**: because you can lock in a future exchange rate through a forward contract at a known, arbitrage-free price, you can eliminate currency exposure from a future cash flow.

Consider a US exporter expecting to receive €1 million in three months. If the euro depreciates by the time payment arrives, the dollar value of that receivable shrinks. A **currency forward** solves this: enter a forward contract to sell €1 million in three months at today's three-month forward rate. Whatever the spot rate turns out to be at settlement, the exporter receives the locked-in forward rate. The hedge converts uncertain future foreign-currency cash flows into a certain domestic-currency amount — the uncertainty is not reduced in the world, but it is transferred to the counterparty. The cost of this certainty is embedded in the forward-spot differential, which CIP tells you equals the interest rate differential.

**Currency options** offer a different risk profile. A **put option** on euros gives the holder the right — but not the obligation — to sell euros at the strike price. If the euro falls below the strike, the put pays off; if the euro stays high, the holder simply lets the option expire and benefits from the favorable spot rate. This asymmetric payoff is the key distinction from a forward: the forward eliminates all exchange rate risk (good and bad), while the put eliminates only downside risk. The price of this asymmetry is the **option premium**, paid upfront regardless of whether the option is exercised. Firms with uncertain foreign-currency cash flows (they might receive €1 million, or maybe less, depending on sales) often prefer options over forwards for this reason.

The choice among hedging instruments — forward, futures, option, swap, or a combination — depends on several practical factors. **Forwards** are customizable in amount and maturity (OTC contracts) but carry counterparty credit risk. **Currency futures** are exchange-traded and thus standardized and marked to market daily, eliminating counterparty risk but introducing basis risk if the maturity and amount don't match perfectly. **Cross-currency swaps** exchange principal and interest cash flows in two currencies and are suited for longer-horizon exposures like foreign-currency debt. Accounting treatment also matters: hedges that qualify for hedge accounting under IFRS or US GAAP allow gains and losses to offset the hedged item in the income statement rather than creating earnings volatility — so treasurers often structure hedges to satisfy accounting as much as to minimize risk economically.
