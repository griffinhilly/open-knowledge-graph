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
stage: formal-systems
status: draft
---

# Mundell-Fleming Model and Open Economy Macroeconomics

## Core Idea
The Mundell-Fleming model extends the IS-LM framework to an open economy with capital mobility. It shows how fiscal and monetary policy effectiveness depends on the exchange rate regime (fixed versus floating). Under floating rates, monetary policy is powerful but fiscal policy is weak (spending crowds out net exports); under fixed rates, the reverse holds. Capital flows between countries create linkages: higher interest rates in one country attract foreign capital, appreciating the currency and reducing competitiveness.

## Explainer

The IS-LM model you already know determines output and interest rates in a closed economy — one with no trade or capital flows. The Mundell-Fleming model asks: what changes when we open the economy to international trade and financial flows? The answer is dramatic, and it hinges on one additional equation and one crucial institutional choice.

The additional equation is the **balance of payments condition**, which in the simplest version with perfect capital mobility becomes: the domestic interest rate must equal the world interest rate (r = r*). The logic is straightforward — if domestic rates exceeded world rates, foreign capital would flood in seeking higher returns; if domestic rates fell below world rates, capital would flee. With perfectly mobile capital, any deviation is instantly arbitraged away. This single condition — pinning the domestic interest rate to the world rate — fundamentally constrains what monetary and fiscal policy can achieve, but the nature of that constraint depends entirely on whether the country fixes or floats its exchange rate.

Under **floating exchange rates**, the central bank controls the money supply, and the exchange rate adjusts freely. Consider an expansionary monetary policy: the central bank increases the money supply, which would normally lower domestic interest rates. But with perfect capital mobility, capital immediately flows out seeking higher returns abroad, depreciating the domestic currency. The weaker currency makes exports cheaper and imports more expensive, boosting net exports and shifting the IS curve rightward. The result is powerful monetary policy — output rises substantially — but through the exchange rate channel, not the interest rate channel. Now consider fiscal expansion: government spending shifts IS rightward, pushing up domestic interest rates. Capital flows in, the currency appreciates, net exports fall, and the IS curve shifts back leftward. Fiscal policy is rendered impotent — the crowding out occurs not through higher interest rates (as in closed-economy IS-LM) but through a stronger currency that chokes off net exports.

Under **fixed exchange rates**, the results reverse completely. The central bank commits to maintaining a specific exchange rate by buying or selling foreign reserves. Now monetary policy is powerless: any attempt to expand the money supply would lower interest rates and trigger capital outflows, but to defend the fixed rate the central bank must sell foreign reserves and buy domestic currency — undoing the original expansion. Fiscal policy, by contrast, becomes highly effective: government spending raises income, which increases money demand and pushes up interest rates, attracting capital inflows. To prevent the currency from appreciating, the central bank must buy foreign reserves and expand the money supply — automatically accommodating the fiscal expansion. This fundamental asymmetry — the **Mundell-Fleming trilemma** — states that a country cannot simultaneously have free capital mobility, a fixed exchange rate, and an independent monetary policy. It can choose any two, but the third is sacrificed, and this insight remains one of the most important organizing principles in international macroeconomics.
