---
id: current-account-sustainability-intertemporal
title: Current Account Sustainability
domain: economics
course: macroeconomics
prerequisites:
- id: balance-of-payments
  type: hard
- id: euler-equation-intertemporal-choice
  type: soft
builds-toward:
- twin-deficits-and-capital-flows
tags:
- current-account
- sustainability
- international
stage: advanced
status: draft
---

# Current Account Sustainability

## Core Idea
A country's current account reflects the difference between national saving and investment; persistent deficits mean borrowing from abroad. A current account deficit is sustainable if the economy is growing faster than the real interest rate, making the debt burden shrink relative to income. Large deficits financed by capital inflows can become unsustainable if foreign confidence deteriorates or if underlying imbalances (low saving, high investment) persist.

## Questions

```yaml
- question: "Country A has a current account deficit of 8% of GDP, a real growth rate of 5%, and a real interest rate on its external debt of 2%. Country B has a current account deficit of 3% of GDP, a growth rate of 1%, and a real interest rate of 4%. Which country's deficit is more likely to be sustainable?"
  type: multiple-choice
  options:
    - "Country B, because a smaller deficit always signals greater sustainability"
    - "Country A, because its real growth rate exceeds its real interest rate, so the external debt-to-GDP ratio shrinks over time even with a persistent deficit"
    - "Country B, because real interest rates above 3% indicate creditor concern about repayment"
    - "Both are equally unsustainable since any persistent current account deficit implies growing foreign debt"
  answer: 1
  explanation: "The key diagnostic is the comparison of r (real interest rate) and g (real growth rate), not the raw deficit size. For Country A, g = 5% > r = 2%, meaning the economy is growing faster than the interest burden — the external debt-to-GDP ratio will shrink over time even without fully closing the deficit. Country B faces r = 4% > g = 1%, meaning the debt ratio is growing even before new borrowing; stabilizing it requires a primary surplus. A large deficit can be sustainable if g > r; a small deficit may be unsustainable if r > g."

- question: "Country X runs a large current account deficit financed mainly by short-term portfolio capital flows (bonds and equities purchased by foreign investors). Country Y runs the same-sized deficit financed mainly by foreign direct investment (factories and long-term assets). Which country is more vulnerable to a sudden stop?"
  type: multiple-choice
  options:
    - "Country X, because short-term portfolio flows can reverse rapidly if investor sentiment shifts, whereas FDI is illiquid and committed long-term"
    - "Country Y, because FDI gives foreign entities ownership of domestic assets, creating political risk"
    - "Both equally — the deficit size determines vulnerability, not the composition of financing"
    - "Country X is less vulnerable because liquid markets allow faster adjustment when deficits need to close"
  answer: 0
  explanation: "The composition of capital inflows is as important as their size. Short-term portfolio flows can be reversed in hours or days as investors sell bonds and equities — this is 'hot money.' When global risk appetite shifts or country-specific doubts arise, these flows can stop suddenly, forcing an abrupt current account adjustment (devaluation, austerity). FDI is embedded in physical assets and ongoing business operations; foreign companies cannot easily liquidate a factory and leave. The Southeast Asian crisis of 1997 illustrated this: countries with high short-term debt were devastated by sudden stops, while FDI-heavy economies were more resilient."

- question: "A current account deficit financed by foreign borrowing used to build productive infrastructure can be sustainable if the resulting economic growth rate exceeds the real interest rate on the borrowed funds."
  type: true-false
  answer: true
  explanation: "This is the intertemporal sustainability condition applied to its most favorable case. The US in the 19th century ran persistent current account deficits as European capital financed railroad and industrial expansion. The resulting productivity growth generated incomes that eventually repaid the debt. The CA = S − I identity shows a deficit means investment exceeds saving; if investment is productive, the future output it generates provides the repayment capacity. The formal condition g > r ensures the debt-to-GDP ratio is self-correcting without requiring a primary surplus."

- question: "A country with a current account deficit is always consuming beyond its means, which is a sign of economic weakness."
  type: true-false
  answer: false
  explanation: "A current account deficit means CA = S − I < 0, i.e., investment exceeds saving. This can reflect high investment (building productive capacity, not excess consumption) rather than low saving. A deficit is a sign of excess consumption if S is low and not offset by productive I; it is a sign of economic dynamism if I is high and generating future returns. The US, Australia, and many fast-growing emerging economies have run persistent deficits while remaining creditworthy. The relevant question is always: what is the deficit financing? Consumption-driven deficits with low growth are concerning; investment-driven deficits in high-growth economies may be entirely benign."

- question: "What is a 'sudden stop,' and why can it render a current account position that appears mathematically sustainable — by the r-versus-g criterion — practically unsustainable?"
  type: short-answer
  answer: "A sudden stop is an abrupt reversal of capital inflows: foreign lenders or investors stop rolling over loans and refuse to extend new credit, forcing the borrowing country to immediately close or dramatically shrink its current account deficit. Even if g > r makes the long-run debt trajectory technically sustainable, the country still needs to continuously attract foreign financing to fund its deficit. If creditor confidence collapses — due to political instability, contagion from other crises, or a shift in global risk appetite — the financing dries up before the long-run arithmetic can play out. The country is then forced into a painful adjustment: devaluation, import compression, and recession."
  explanation: "The Southeast Asian crises of 1997–98 are the canonical example. Countries like Thailand and South Korea had defensible debt ratios and reasonable growth outlooks, yet faced devastating sudden stops when short-term foreign borrowing was not renewed. The lesson is that sustainability is not just a property of the debt trajectory — it depends on maintaining creditor confidence, which can be fragile and self-fulfilling. A country that looks sustainable can become unsustainable the moment enough creditors believe it is, creating a coordination failure."
```

## Explainer

From the balance of payments, you know that the current account measures a country's net flows of goods, services, and income with the rest of the world, and that a current account deficit is exactly financed by a capital account surplus — the country is borrowing from abroad. This accounting identity is the starting point: CA = S − I, where S is national saving and I is domestic investment. A current account deficit means investment exceeds saving; the gap is filled by foreign capital inflows. The sustainability question asks: can this persist?

The intertemporal approach borrows the logic from the Euler equation and optimal consumption smoothing. A household can borrow today if its future income will be high enough to repay the debt. A country is analogous: borrowing to finance productive investment (building infrastructure, expanding manufacturing capacity) generates the future income needed to service the external debt. This is the **good deficit** scenario — the US ran large current account deficits in the 19th century as foreign capital financed railroad and industrial expansion, and the debt was eventually paid down from the resulting growth. By contrast, borrowing to finance current consumption rather than productive investment does not generate future repayment capacity and is harder to sustain.

The formal sustainability condition emerges from the debt dynamics equation. If d is the external debt-to-GDP ratio, r is the real interest rate on that debt, and g is the real growth rate of the economy, then the debt ratio grows by approximately (r − g)d plus any new borrowing. If g > r, the economy is growing faster than the interest burden, so even a persistent current account deficit will cause the debt ratio to shrink over time — sustainability is assured as long as the primary balance remains manageable. If r > g, the debt ratio grows without additional borrowing, requiring a primary surplus to stabilize it. The comparison of r versus g is thus the critical diagnostic for sustainability.

However, the formal condition is necessary but not sufficient. **Sudden stops** can render a technically sustainable position unsustainable in practice. If foreign lenders become nervous about a country's ability to repay — due to political instability, a shift in global risk appetite, or contagion from other crises — they may stop rolling over loans, forcing an abrupt and painful current account adjustment. This is what happened across Southeast Asia in 1997: current account deficits that looked manageable by growth-versus-interest-rate calculations became impossible to sustain when foreign capital dried up overnight. The composition of financing matters too: deficits financed by foreign direct investment (long-term productive capital) are far more stable than deficits financed by short-term portfolio flows or bank lending, which can reverse rapidly. Assessing current account sustainability therefore requires not just arithmetic but judgment about the confidence of foreign creditors and the quality of the underlying investment being financed.
