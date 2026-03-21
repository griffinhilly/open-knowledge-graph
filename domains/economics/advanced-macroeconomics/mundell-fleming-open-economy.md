---
id: mundell-fleming-open-economy
title: Mundell-Fleming Model and Open Economy Macroeconomics
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: is-lm-model
  type: hard
- id: open-economy-macroeconomics
  type: hard
- id: systems-of-linear-equations
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- exchange-rate-dynamics
- balance-of-payments-capital-flows
tags:
- mundell-fleming
- open-economy
- exchange-rates
stage: advanced
status: draft
---

# Mundell-Fleming Model and Open Economy Macroeconomics

## Core Idea
The Mundell-Fleming model extends the IS-LM framework to an open economy with capital mobility. It shows how fiscal and monetary policy effectiveness depends on the exchange rate regime (fixed versus floating). Under floating rates, monetary policy is powerful but fiscal policy is weak (spending crowds out net exports); under fixed rates, the reverse holds. Capital flows between countries create linkages: higher interest rates in one country attract foreign capital, appreciating the currency and reducing competitiveness.

## Questions

```yaml
- question: "Under a floating exchange rate with perfect capital mobility, a government increases spending significantly on infrastructure. What does the Mundell-Fleming model predict will happen to national output?"
  type: multiple-choice
  options:
    - "Output rises substantially — the fiscal multiplier works as in the standard closed-economy IS-LM model"
    - "Output rises slightly — some interest rate crowding out partially offsets the stimulus, as in the closed economy"
    - "Output is largely unchanged — the currency appreciates, reducing net exports by approximately as much as government spending increased"
    - "Output falls — the currency appreciation more than offsets the spending increase, creating a net contractionary effect"
  answer: 2
  explanation: "Under floating rates, fiscal expansion shifts IS rightward, initially raising income and interest rates. The higher rates attract capital inflows, appreciating the currency. The stronger currency makes exports more expensive and imports cheaper, reducing net exports — shifting IS back leftward. With perfect capital mobility, this process is essentially complete: the IS curve returns near its original position at the world interest rate, leaving output largely unchanged. The crowding-out mechanism operates through the exchange rate rather than interest rates, unlike the closed-economy case."

- question: "A country with a fixed exchange rate and perfect capital mobility tries to stimulate the economy via open market bond purchases, expanding the money supply. What ultimately happens?"
  type: multiple-choice
  options:
    - "The money supply expansion is sustained and output rises as domestic interest rates fall below world rates"
    - "Capital inflows allow the central bank to permanently expand the money supply while holding the exchange rate fixed"
    - "Capital outflows (as domestic rates fall below world rates) force the central bank to sell foreign reserves and contract the money supply, fully reversing the original expansion"
    - "Inflation quickly erodes the real money supply back to its original level, neutralizing the stimulus"
  answer: 2
  explanation: "With a fixed exchange rate and perfect capital mobility, any attempt to expand the money supply causes domestic interest rates to briefly fall below world rates. Capital immediately flows out seeking higher returns abroad. To defend the fixed exchange rate and prevent depreciation, the central bank must sell foreign reserves and buy domestic currency — contracting the money supply back to its original level. Monetary policy is completely impotent: any expansion is automatically undone by the balance of payments adjustment required to maintain the peg."

- question: "Under the Mundell-Fleming model with fixed exchange rates and perfect capital mobility, fiscal expansion is more powerful than in a closed economy because the central bank must expand the money supply to defend the exchange rate peg."
  type: true-false
  answer: true
  explanation: "Fiscal expansion raises domestic interest rates, attracting capital inflows. To prevent currency appreciation, the central bank must buy foreign reserves (selling domestic currency) — which expands the money supply. This automatic monetary accommodation reinforces the fiscal expansion: both IS and LM shift rightward simultaneously, amplifying the fiscal multiplier beyond the closed-economy case. Fixed exchange rate regimes effectively make monetary policy subordinate to the exchange rate target, leaving fiscal policy as the dominant stabilization tool."

- question: "Under the Mundell-Fleming model, a country with free capital mobility can independently set its exchange rate target and domestic interest rate simultaneously while also conducting independent monetary policy."
  type: true-false
  answer: false
  explanation: "This violates the Mundell-Fleming trilemma (impossible trinity): a country cannot simultaneously maintain free capital mobility, a fixed exchange rate, and an independent monetary policy. Free capital mobility arbitrages away interest rate differentials — forcing domestic rates toward the world rate. A fixed exchange rate requires the central bank to intervene in currency markets, which endogenously determines the money supply. Only two of the three can hold at once. This constraint is one of the most robust organizing principles in international macroeconomics."

- question: "Explain why fiscal policy is ineffective under floating exchange rates but effective under fixed exchange rates in the Mundell-Fleming model. What mechanism creates this reversal?"
  type: short-answer
  answer: "Under floating rates, fiscal expansion raises domestic interest rates, attracting capital inflows that appreciate the currency. The stronger currency reduces net exports — a form of crowding out operating through the exchange rate. With perfect capital mobility, this crowding out is complete, leaving output unchanged. Under fixed rates, the same fiscal expansion attracts capital inflows, but the central bank must intervene to prevent appreciation by buying foreign reserves and expanding the money supply. This automatic monetary accommodation amplifies the fiscal multiplier rather than neutralizing it. The reversal occurs because the exchange rate regime determines whether capital-flow-driven pressure is absorbed by currency adjustment (floating, where it crowds out net exports) or by money supply expansion (fixed, where it reinforces the stimulus)."
  explanation: "This symmetry is the core of Mundell-Fleming: whatever policy is powerful under one exchange rate regime is weak under the other. The institutional choice of exchange rate regime fundamentally reshapes the transmission mechanism of macroeconomic policy."
```

## Explainer

The IS-LM model you already know determines output and interest rates in a closed economy — one with no trade or capital flows. The Mundell-Fleming model asks: what changes when we open the economy to international trade and financial flows? The answer is dramatic, and it hinges on one additional equation and one crucial institutional choice.

The additional equation is the **balance of payments condition**, which in the simplest version with perfect capital mobility becomes: the domestic interest rate must equal the world interest rate (r = r*). The logic is straightforward — if domestic rates exceeded world rates, foreign capital would flood in seeking higher returns; if domestic rates fell below world rates, capital would flee. With perfectly mobile capital, any deviation is instantly arbitraged away. This single condition — pinning the domestic interest rate to the world rate — fundamentally constrains what monetary and fiscal policy can achieve, but the nature of that constraint depends entirely on whether the country fixes or floats its exchange rate.

Under **floating exchange rates**, the central bank controls the money supply, and the exchange rate adjusts freely. Consider an expansionary monetary policy: the central bank increases the money supply, which would normally lower domestic interest rates. But with perfect capital mobility, capital immediately flows out seeking higher returns abroad, depreciating the domestic currency. The weaker currency makes exports cheaper and imports more expensive, boosting net exports and shifting the IS curve rightward. The result is powerful monetary policy — output rises substantially — but through the exchange rate channel, not the interest rate channel. Now consider fiscal expansion: government spending shifts IS rightward, pushing up domestic interest rates. Capital flows in, the currency appreciates, net exports fall, and the IS curve shifts back leftward. Fiscal policy is rendered impotent — the crowding out occurs not through higher interest rates (as in closed-economy IS-LM) but through a stronger currency that chokes off net exports.

Under **fixed exchange rates**, the results reverse completely. The central bank commits to maintaining a specific exchange rate by buying or selling foreign reserves. Now monetary policy is powerless: any attempt to expand the money supply would lower interest rates and trigger capital outflows, but to defend the fixed rate the central bank must sell foreign reserves and buy domestic currency — undoing the original expansion. Fiscal policy, by contrast, becomes highly effective: government spending raises income, which increases money demand and pushes up interest rates, attracting capital inflows. To prevent the currency from appreciating, the central bank must buy foreign reserves and expand the money supply — automatically accommodating the fiscal expansion. This fundamental asymmetry — the **Mundell-Fleming trilemma** — states that a country cannot simultaneously have free capital mobility, a fixed exchange rate, and an independent monetary policy. It can choose any two, but the third is sacrificed, and this insight remains one of the most important organizing principles in international macroeconomics.
