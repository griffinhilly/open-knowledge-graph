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
- id: liquidity-preference-theory-keynes
  type: soft
builds-toward:
- exchange-rate-regimes-and-monetary-policy
tags:
- interest-rates
- parity
- exchange-rates
stage: advanced
status: validated
---
# Interest Rate Parity

## Core Idea
Interest rate parity (IRP) requires that the interest rate differential between two countries equals the expected change in the exchange rate: investors must earn the same return in both currencies after accounting for currency depreciation. Covered IRP (using forward contracts) holds almost exactly due to arbitrage; uncovered IRP relies on rational expectations and holds less precisely. IRP links monetary policy across countries in the open economy.

## Questions

```yaml
- question: "The U.S. interest rate is 6% and Japan's is 1%. An investor has two options: (A) invest in U.S. assets at 6%, or (B) convert dollars to yen, earn 1% in Japan, and lock in today's forward exchange rate to convert back. Under covered interest parity, what should the relationship between these options be?"
  type: multiple-choice
  options:
    - "Option A earns more because the U.S. rate is higher"
    - "Both options yield the same return after accounting for the forward rate adjustment, because any difference is eliminated by arbitrage"
    - "Option B earns more because Japan's lower rate signals a stronger yen appreciation"
    - "The comparison is invalid because forward contracts introduce credit risk that makes returns incomparable"
  answer: 1
  explanation: "Under CIP, the forward exchange rate adjusts so that the dollar return from the round-trip in yen (earn 1% + gain from forward premium) exactly equals 6%. If it didn't, arbitrageurs would borrow in the low-return currency, invest in the high-return one, and lock in the forward rate for a riskless profit — and their trading would push the forward rate back into alignment. CIP is a no-arbitrage condition: any deviation is a riskless profit opportunity and gets eliminated almost instantly in liquid markets. The forward rate is the mechanism of equalization."

- question: "Why does uncovered interest parity (UIP) fail empirically more often than covered interest parity (CIP)?"
  type: multiple-choice
  options:
    - "CIP applies only to major currency pairs; UIP applies to all currencies including emerging markets where it frequently fails"
    - "CIP involves contractually locked-in forward rates, so any deviation is a riskless arbitrage profit that traders eliminate instantly; UIP relies on exchange rate expectations that can be systematically wrong"
    - "CIP uses spot exchange rates, which are more liquid and therefore more accurately priced than the future rates UIP depends on"
    - "UIP assumes rational investors; CIP does not, making CIP hold regardless of investor behavior"
  answer: 1
  explanation: "CIP is enforced by riskless arbitrage. With observable spot rates, forward rates, and two interest rates, any CIP deviation can be locked in immediately for a guaranteed profit — it gets traded away. UIP substitutes the expected future spot rate for the forward rate, and expectations can be wrong — and may be systematically wrong for extended periods. The famous 'forward premium puzzle' shows that currencies with higher interest rates often appreciate rather than depreciate (the opposite of UIP's prediction), generating persistent carry trade profits. This systematic failure reflects risk premia, peso problems, or behavioral factors that CIP arbitrage does not face."

- question: "If a country raises its interest rate, uncovered interest parity predicts that its currency will depreciate over the period that the higher rate is in effect."
  type: true-false
  answer: true
  explanation: "UIP requires that the expected return to investing in either currency be equal. If Country A raises its interest rate above Country B's, investors will move capital to A, bidding up A's currency — but UIP predicts this appreciation already happened or will happen immediately, after which the currency is expected to depreciate back toward its original level at a rate equal to the interest differential. In the UIP framework, the higher interest rate is the reward for holding a currency expected to depreciate, not an ongoing advantage. This is why UIP predicts depreciation for high-rate currencies — the gains must be offset by currency loss."

- question: "Persistent violations of covered interest parity in liquid, major-currency markets indicate that investors have incorrect expectations about future exchange rates."
  type: true-false
  answer: false
  explanation: "CIP has nothing to do with exchange rate expectations — it uses forward rates, which are contractually fixed prices, not forecasts. A CIP deviation is a riskless arbitrage opportunity available right now with known, locked-in payoffs. Persistent CIP violations therefore do not reflect forecast errors but rather a breakdown in the ability of arbitrageurs to implement the trade — typically due to balance sheet constraints, counterparty credit risk, or funding liquidity stress in the banking system. The CIP violations that appeared in the 2008 financial crisis and the 2020 COVID shock reflected banks' inability to freely intermediate the trade, not mistaken expectations."

- question: "Explain the key difference between covered and uncovered interest parity in terms of what 'enforces' each condition. Why is CIP nearly always satisfied in liquid markets while UIP often fails?"
  type: short-answer
  answer: "CIP is a no-arbitrage condition enforced by riskless, immediate trading. Using a forward contract eliminates all exchange rate uncertainty: you lock in the conversion rate today, so the round-trip return is calculable in advance with no risk. Any deviation can be exploited for guaranteed profit, so arbitrageurs eliminate it quickly in liquid markets. UIP is an equilibrium condition enforced only by investor expectations about future spot rates. There is no riskless trade to enforce it — if your expectation is wrong, you lose. Expectations can be systematically biased (risk premia, peso problems), and no one can force the exchange rate to move as predicted. The result: CIP is near-perfect in liquid markets; UIP holds at best approximately and often fails over short horizons."
  explanation: "This distinction generalizes beyond currency markets: any condition enforced by observable, riskless arbitrage (like the law of one price for identical goods in frictionless markets) will hold tightly, while conditions enforced only by rational expectations will hold loosely and fail whenever expectations are distorted by risk, uncertainty, or behavioral biases. Understanding which type of condition you are dealing with is the key to predicting when parity relationships will hold."
```

## Explainer

You already know that interest rates are determined in the loanable funds market and that exchange rates are driven by supply and demand for currencies. Interest rate parity is the condition that ties these two markets together in an open economy: if capital can flow freely across borders, investors will move funds toward whatever currency offers a higher return — and their collective behavior will equalize returns across countries after accounting for expected currency movements.

Start with the basic logic. Suppose the U.S. offers a 5% annual interest rate and the eurozone offers 3%. A U.S. investor considering parking money in euros will earn 3% but must also accept whatever happens to the dollar/euro exchange rate over the year. If the euro is expected to appreciate by 2% against the dollar, the euro investment effectively earns 3% + 2% = 5% in dollar terms — matching the domestic rate. If the euro were instead expected to depreciate, the dollar investment would dominate, and investors would sell euros, bidding the euro down until the expected depreciation exactly offset the interest differential. This is the core of **interest rate parity**: the interest differential equals the expected exchange rate change.

**Covered interest parity (CIP)** is the no-arbitrage version. Instead of expecting a future exchange rate, you *lock it in today* using a forward contract. You borrow in dollars, convert to euros at today's spot rate, earn the euro interest rate, and simultaneously agree today to convert your euros back to dollars at the forward rate. CIP says the profit from this round-trip must be zero — otherwise, arbitrageurs with access to forward markets would exploit it indefinitely. Because CIP depends only on observable, contractually fixed prices (spot rate, forward rate, and two interest rates), it holds almost perfectly for comparable assets in liquid markets with no capital controls. Violations of CIP are typically small and fleeting — and when they appear persistently (as they did in the 2008 crisis), it signals stress in the banking system's ability to intermediate capital flows.

**Uncovered interest parity (UIP)** relaxes the forward contract and substitutes the market's *expectation* of the future exchange rate. UIP must therefore hold in expectation rather than by arbitrage, and whether it actually holds is an empirical question. The evidence is mixed: UIP holds reasonably well at very long horizons and for some country pairs, but over short horizons the "forward premium puzzle" documents that high-interest currencies often *appreciate* rather than depreciate as UIP predicts — the opposite of what the theory says. This empirical failure is one of the most studied puzzles in international finance, with explanations ranging from risk premia to peso problems to irrational expectations. The important lesson is that CIP is a near-identity enforced by arbitrage, while UIP is an equilibrium condition enforced only by expectations — and expectations can be wrong for a long time.
