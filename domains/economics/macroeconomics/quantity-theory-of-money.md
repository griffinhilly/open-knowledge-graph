---
id: quantity-theory-of-money
title: The Quantity Theory of Money
domain: economics
course: macroeconomics
prerequisites:
- id: money-supply-and-money-creation
  type: hard
- id: inflation-and-price-level
  type: hard
builds-toward:
- monetary-policy-tools
- phillips-curve
tags:
- quantity-theory
- MV=PQ
- monetarism
- velocity
- Fisher-equation
stage: formal-systems
status: validated
---

# The Quantity Theory of Money

## Core Idea
The quantity theory of money states that MV = PQ, where M is the money supply, V is the velocity of money (average number of times a unit of currency is spent per period), P is the price level, and Q is real output. If V and Q are constant (or slowly changing), proportional increases in M produce proportional increases in P — money growth causes inflation. Monetarists, led by Milton Friedman, argued that 'inflation is always and everywhere a monetary phenomenon.' The theory is most reliable in the long run and during extreme monetary expansions; in the short run, V and Q vary significantly.

## How It's Best Learned
Apply the equation: if M grows 10%, V is constant, and Q grows 3%, what is the inflation rate? Then examine cases where the theory breaks down (Japan in the 1990s–2000s) when V fell as M expanded.

## Common Misconceptions
- The quantity theory does not say all money growth causes inflation immediately; short-run changes in velocity and output matter.
- Velocity is not constant; it fell sharply in 2009 and 2020, which is why large balance sheet expansions did not generate proportional inflation in those episodes.
- The theory is a long-run framework, not a precise short-run forecasting tool.

## Questions

```yaml
- question: "After the 2008 financial crisis, the Federal Reserve roughly quintupled the monetary base through quantitative easing, yet inflation remained subdued for nearly a decade. Which explanation is most consistent with the quantity theory framework?"
  type: multiple-choice
  options:
    - "The quantity theory was falsified — MV = PQ must be wrong as an equation"
    - "Velocity fell sharply as banks held excess reserves and households demanded more money as a safe asset, offsetting the increase in M"
    - "Real output Q grew fast enough to absorb all the new money with no price impact"
    - "The quantity theory only applies to M1, not the monetary base"
  answer: 1
  explanation: "MV = PQ is an accounting identity — it is always true by definition. The 2008 episode doesn't falsify it; it illustrates that V is not constant. When the Fed created new money, banks largely held it as excess reserves rather than lending it out, and households increased their demand for liquid assets. Velocity collapsed, absorbing the increase in M so that neither P nor Q needed to change proportionally. The monetarist claim that 'money growth causes inflation' depends on V being stable — when V falls, M can increase without proportional price growth."

- question: "If the money supply doubles and velocity halves, what happens to nominal GDP (P × Q)?"
  type: multiple-choice
  options:
    - "Nominal GDP doubles, because the money supply doubled"
    - "Nominal GDP is unchanged, because the doubling of M is exactly offset by the halving of V"
    - "Nominal GDP halves, because velocity determines spending more than money supply"
    - "Real output Q must adjust to compensate, leaving prices unchanged"
  answer: 1
  explanation: "From MV = PQ: if M doubles and V halves, then MV = (2M)(V/2) = MV — nominal GDP (P×Q) is unchanged. The theory predicts inflation from money growth only when V is stable. If velocity moves inversely to money supply — as it did in 2008–09 and 2020 — the increase in M is completely absorbed and nominal GDP need not change."

- question: "The equation MV = PQ is a testable empirical claim that can, in principle, be proven false by data."
  type: true-false
  answer: false
  explanation: "MV = PQ is an accounting identity, not a hypothesis. V is defined as PQ/M — the ratio of nominal GDP to money supply. The equation is therefore true by construction for any observed data; it cannot be falsified. The empirical content comes from the additional assumption that V is stable: if you predict that stable V implies proportional inflation from money growth, that prediction can be tested and can fail. The identity is always true; the stability assumption is what carries the theoretical weight."

- question: "Hyperinflations like those in Weimar Germany and Zimbabwe provide evidence that sustained money growth causes inflation in extreme cases."
  type: true-false
  answer: true
  explanation: "The quantity theory's predictions are most reliable in extreme monetary expansions. In hyperinflations, money is typically printed to finance government deficits at rates far exceeding any plausible increase in real output. V and Q change slowly relative to the explosive growth of M, so the proportionality assumption holds approximately: money growth translates into roughly proportional price increases. The theory is a better guide the more extreme and sustained the monetary expansion."

- question: "Why is MV = PQ described as both an accounting identity and a theory, and what is the difference between those two things?"
  type: short-answer
  answer: "MV = PQ is an identity because velocity V is defined as PQ/M — substituting that definition makes the equation trivially true. No data can falsify an identity. The quantity theory of money adds the empirical claim that V is relatively stable over time, which transforms the identity into a prediction: changes in M will produce roughly proportional changes in P, since Q grows only slowly. This additional assumption can fail — as when velocity collapsed in 2008 and 2020 — and that failure is what gives the theory empirical content."
  explanation: "The distinction matters because critics of the theory sometimes say '2008 disproved MV=PQ' — but the identity was never violated. What failed was the stability-of-V assumption. You cannot disprove an accounting identity with data, but you can disprove the theoretical assumption that V is stable."
```

## Explainer

From money supply and the price level, you know that money is both a medium of exchange and a store of value, and that changes in the price level measure how much purchasing power a unit of currency commands. The **quantity theory of money** provides the simplest possible model linking these two: if there's more money in the economy, prices will be higher. The equation of exchange formalizes this — MV = PQ — and unpacking each term reveals exactly what the theory assumes and where it can fail.

M is the stock of money (however measured — M1, M2, etc.). Q is real output — total goods and services produced. P is the price level. **Velocity** V is the implied residual: the average number of times each unit of currency changes hands in a year. If GDP (P×Q) is $20 trillion and the money supply M is $4 trillion, then V = 5 — on average, each dollar was spent five times during the year. The equation MV = PQ is actually an accounting identity, true by definition. The theory comes from adding an assumption: if V is relatively stable (reflecting stable payments habits) and Q grows at its long-run rate determined by real factors, then proportional changes in M translate proportionally into changes in P.

The monetarist conclusion attributed to Milton Friedman — "inflation is always and everywhere a monetary phenomenon" — follows directly from this assumption. In extreme episodes, the theory's predictions are roughly accurate: hyperinflations in Weimar Germany, Zimbabwe, and Venezuela were accompanied by explosive money growth. The causality runs from money creation (often driven by governments printing money to finance deficits) to proportional price increases. In these extreme cases, V and Q change slowly relative to the pace of money growth, making the theory a useful first approximation.

The theory breaks down in the short run and in episodes where V is unstable. After the 2008 financial crisis, the Federal Reserve roughly quintupled the monetary base through quantitative easing — yet inflation remained subdued for a decade. The reason: velocity collapsed. Banks sat on excess reserves; households and businesses increased their demand for money as a safe asset. More money was created, but it circulated less. The same pattern repeated in 2020. This is not a failure of the accounting identity — MV = PQ is always true — but a failure of the assumption that V is stable. When velocity absorbs the shock, output and prices need not move. The quantity theory's usefulness is therefore context-dependent: a reliable guide to long-run inflation trends and extraordinary monetary events, but an unreliable short-run forecasting tool when velocity behavior is uncertain.
