---
id: mundell-fleming-extended
title: Mundell-Fleming Model with Capital Mobility
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: open-economy-macroeconomics
  type: hard
- id: exchange-rates-macroeconomics
  type: hard
builds-toward:
- capital-flows-balance-of-payments
tags:
- open-economy
- exchange-rates
- capital-flows
- trilemma
stage: expert
status: draft
---

# Mundell-Fleming Model with Capital Mobility

## Core Idea
The extended Mundell-Fleming model incorporates perfect capital mobility and flexible exchange rates into the IS-LM framework for open economies. It reveals the policy trilemma: countries cannot simultaneously maintain fixed exchange rates, independent monetary policy, and perfect capital mobility. The model shows that monetary policy is potent in floating regimes but ineffective in fixed regimes, while fiscal policy effectiveness reverses depending on capital mobility and exchange-rate regime.

## Questions

```yaml
- question: "Under floating exchange rates with perfect capital mobility, a government significantly increases fiscal spending. What ultimately happens to output?"
  type: multiple-choice
  options:
    - "Output rises substantially as the fiscal multiplier works through the economy"
    - "Output rises then partially reverses as higher interest rates crowd out private investment"
    - "Output is approximately unchanged because capital inflows appreciate the currency, crowding out net exports by the same amount"
    - "Output falls because the appreciation makes domestic goods uncompetitive internationally"
  answer: 2
  explanation: "This is the key counterintuitive result of Mundell-Fleming under floating rates. Fiscal expansion shifts IS right, raising the interest rate above the world rate. With perfect capital mobility, this attracts massive capital inflows, appreciating the exchange rate. The stronger currency makes exports more expensive and imports cheaper, shifting IS back left (net exports fall). The appreciation fully offsets the fiscal stimulus, leaving output roughly unchanged. The exchange rate crowds out net exports by exactly the amount government spending adds. This is why floating exchange rates are said to 'insulate' the economy from fiscal shocks."

- question: "A country maintains a fixed exchange rate and perfect capital mobility. The central bank tries to expand the money supply to stimulate growth. What happens?"
  type: multiple-choice
  options:
    - "Output expands because the money supply increase lowers interest rates and stimulates investment"
    - "Output expands temporarily until the exchange rate depreciates, at which point the central bank must intervene"
    - "The money supply expansion is automatically reversed as the central bank defends the peg, leaving output unchanged"
    - "Output contracts because capital outflows reduce domestic investment"
  answer: 2
  explanation: "Under fixed exchange rates, the central bank surrenders monetary independence. An LM expansion lowers the domestic interest rate below the world rate, triggering capital outflows and depreciation pressure. To defend the peg, the central bank must sell foreign reserves and buy domestic currency, contracting the money supply and shifting LM back to its original position. The expansion is fully reversed. This is why the Mundell-Fleming model shows that monetary policy is completely ineffective under fixed exchange rates with perfect capital mobility — the very act of defending the peg undoes any monetary stimulus."

- question: "Under fixed exchange rates with perfect capital mobility, fiscal policy is effective at raising output."
  type: true-false
  answer: true
  explanation: "This is the 'flip' result of Mundell-Fleming: the effectiveness of fiscal and monetary policy reverses depending on the exchange rate regime. Under fixed rates, fiscal expansion shifts IS right, raising the interest rate above the world rate and attracting capital inflows. The inflows create appreciation pressure; to defend the peg, the central bank buys foreign reserves and expands the money supply (shifts LM right), reinforcing the output expansion. Instead of being crowded out, the fiscal stimulus is amplified by the automatic monetary accommodation required to maintain the peg."

- question: "The impossible trinity states that a country can simultaneously maintain a fixed exchange rate, independent monetary policy, and perfect capital mobility."
  type: true-false
  answer: false
  explanation: "The impossible trinity (policy trilemma) states the opposite: these three goals are mutually incompatible and a country can achieve at most two. With perfect capital mobility, capital flows enforce interest rate parity — any deviation from the world rate triggers flows that undermine either the exchange rate peg or the domestic money supply. To maintain a fixed rate AND independent monetary policy, a country must restrict capital flows (as China has done). To maintain a fixed rate AND capital mobility, it must surrender monetary independence (as Eurozone members have done). To maintain capital mobility AND independent monetary policy, it must allow the exchange rate to float (as the US and UK do)."

- question: "Explain why fiscal policy is ineffective under floating exchange rates but effective under fixed exchange rates, according to the Mundell-Fleming model."
  type: short-answer
  answer: "Under floating rates, fiscal expansion raises income and the interest rate. With perfect capital mobility, higher domestic rates attract capital inflows that appreciate the exchange rate. The appreciation makes exports more expensive and imports cheaper, reducing net exports by the same amount that government spending increased — the fiscal stimulus is fully crowded out through the exchange rate, not interest rates. Under fixed rates, the same fiscal expansion attracts capital inflows and appreciation pressure; but now the central bank must intervene to defend the peg by buying foreign reserves and expanding the money supply. This monetary expansion reinforces the original fiscal stimulus rather than offsetting it. The exchange rate regime determines whether the central bank's defensive response amplifies or neutralizes the fiscal shock."
  explanation: "The key mechanism is the 'exchange rate valve': under floating rates, the exchange rate absorbs the shock (appreciation crowds out net exports); under fixed rates, the money supply must absorb the shock instead (monetary expansion accommodates the fiscal stimulus). Understanding this reveals why international monetary arrangements — not just domestic policy choices — determine policy effectiveness."
```

## Explainer

From open-economy macroeconomics, you understand that trade flows, capital flows, and exchange rates connect domestic and foreign economies. From your study of exchange rate determination, you know that exchange rates adjust to equalize returns on domestic and foreign assets. The **Mundell-Fleming model** extends the familiar IS-LM framework to an open economy, adding a third relationship — the balance of payments — that links the domestic interest rate to the world interest rate through international capital flows.

The model has three curves. The **IS curve** represents goods market equilibrium, but now includes net exports, which depend on the exchange rate: a weaker (depreciated) domestic currency makes exports cheaper and imports more expensive, boosting net exports and shifting IS right. The **LM curve** represents money market equilibrium, just as in the closed-economy case. The third curve, the **BP (balance of payments) line**, represents external balance. Under perfect capital mobility — the assumption that financial capital moves freely and instantaneously across borders — the BP line is horizontal at the world interest rate. Any domestic interest rate above the world rate attracts massive capital inflows; any rate below triggers outflows. The domestic interest rate is effectively pinned to the world rate.

This pinning produces the model's most striking results. Under **floating exchange rates**, monetary expansion shifts LM right, pushing the domestic interest rate temporarily below the world rate. Capital flees the country, causing the currency to depreciate. The weaker currency boosts net exports, shifting IS right until the interest rate returns to the world level — but at a higher level of output. Monetary policy is highly effective because the exchange rate does the heavy lifting. Fiscal expansion, by contrast, shifts IS right and pushes the interest rate temporarily above the world rate. Capital flows in, the currency appreciates, and the stronger currency chokes off net exports, shifting IS back left. Output barely changes. Fiscal policy is ineffective under floating rates with perfect capital mobility because exchange rate appreciation **crowds out** net exports by exactly the amount fiscal spending adds.

Under **fixed exchange rates**, the results flip. The central bank must intervene in currency markets to maintain the peg, buying or selling foreign reserves. A monetary expansion that pushes the interest rate below the world rate triggers capital outflows and currency depreciation pressure. To defend the peg, the central bank sells foreign reserves and buys domestic currency, contracting the money supply and shifting LM back. Monetary policy is completely neutralized. Fiscal expansion, however, works: the IS shift raises the interest rate, attracting capital inflows and appreciation pressure. To defend the peg, the central bank buys foreign reserves and expands the money supply, reinforcing the output expansion. This asymmetry is the essence of the **impossible trinity** (or policy trilemma): with perfect capital mobility, a country must choose between exchange rate stability and monetary policy independence — it cannot have both simultaneously.
