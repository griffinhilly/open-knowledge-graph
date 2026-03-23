---
id: financial-accelerator-mechanism
title: Financial Accelerator and Credit Constraints
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: information-asymmetry
  type: soft
- id: new-keynesian-framework-overview
  type: soft
tags:
- financial-accelerator
- credit-constraints
- financial-frictions
stage: expert
status: draft
---

# Financial Accelerator and Credit Constraints

## Core Idea
The financial accelerator amplifies shocks through credit markets: when net worth falls, borrowers appear riskier, widening credit spreads. Higher borrowing costs reduce investment and entrepreneurship, worsening the initial shock. Asset price declines feed back to reduce net worth, creating a negative feedback loop.

## Questions

```yaml
- question: "A moderate decline in housing prices causes a much larger-than-expected drop in business investment. Which mechanism best explains this amplification?"
  type: multiple-choice
  options:
    - "Lower housing prices reduce consumer confidence, directly reducing spending"
    - "Falling asset values reduce firms' net worth, raising the external finance premium and cutting investment, which further depresses asset values"
    - "Banks reduce lending because regulators tighten capital requirements during downturns"
    - "Lower housing prices reduce construction employment, which reduces aggregate demand through the multiplier"
  answer: 1
  explanation: "The financial accelerator operates through the net worth channel: falling asset prices erode collateral and net worth, making borrowers appear riskier. Lenders widen credit spreads, raising the cost of external funds. Higher borrowing costs reduce investment, which depresses economic activity and asset prices further — each round amplifying the initial shock. Options A, C, and D are real effects but are not the financial accelerator mechanism; they describe demand-side multiplier effects or regulatory responses, not the credit-market feedback loop."

- question: "The financial accelerator is symmetric — it amplifies downturns but not expansions."
  type: true-false
  answer: false
  explanation: "The financial accelerator amplifies both contractions and expansions. During booms, rising asset prices increase net worth, lower credit spreads, encourage borrowing and investment, and push asset prices higher still. This symmetric amplification is why the mechanism contributes to boom-bust cycles. The asymmetry in public perception (the accelerator is most visible in crises) does not mean it is absent during expansions — it actively inflates the boom that precedes the bust."

- question: "A borrower's net worth increases substantially due to rising collateral values. According to the financial accelerator framework, the external finance premium will rise."
  type: true-false
  answer: false
  explanation: "The external finance premium moves inversely with net worth. When net worth rises — because collateral is worth more and the borrower has more 'skin in the game' — lenders face less risk, and the premium they charge above the risk-free rate falls. Credit becomes cheaper and more accessible. This is the mechanism by which rising asset prices during booms stimulate further borrowing and investment, completing the upward feedback loop."

- question: "Why is the mechanism called a financial 'accelerator' rather than a financial 'creator' of shocks?"
  type: short-answer
  answer: "The financial accelerator does not generate the original shock — it amplifies and propagates shocks that originate elsewhere (productivity declines, commodity price swings, etc.). A 1% drop in productivity might cause a 3% drop in investment once the accelerator is operating. The mechanism takes small or moderate disturbances and turns them into larger, more persistent downturns (or booms) by feeding back through credit markets. Without the financial frictions, the same shock would produce a smaller, shorter-lived effect."
  explanation: "This distinction is important for policy. If the financial system were merely a passive reflector of real shocks, there would be little value in financial regulation. But because it actively amplifies shocks, macroprudential policy — limiting leverage buildup during booms — can reduce the fuel available to the accelerator and dampen future cycles. The 2008 crisis was a canonical demonstration: what began as a housing correction became a global financial crisis because the accelerator was operating at full force."

- question: "During the 2008 financial crisis, a bank's balance sheet deteriorates as mortgage-backed securities fall in value. Walking through the financial accelerator logic, what happens next?"
  type: multiple-choice
  options:
    - "The bank lowers interest rates to attract more deposits and restore its balance sheet"
    - "The bank's reduced net worth raises its cost of funding, causing it to cut lending, which depresses economic activity and asset prices further"
    - "The bank sells profitable assets to offset losses, restoring net worth without macroeconomic consequences"
    - "The bank's losses are absorbed by deposit insurance, breaking the accelerator feedback loop"
  answer: 1
  explanation: "When a bank's net worth falls (assets worth less than expected), it faces a higher external finance premium on its own borrowing and becomes more cautious about lending. Reduced credit availability raises borrowing costs for firms and households, cutting investment and spending. This depresses asset prices further, eroding net worth again — completing the feedback loop. Options C and D might partially help but don't break the mechanism: fire-sale asset sales can depress prices further (amplifying), and deposit insurance doesn't directly address the bank's willingness to extend new credit."
```

## Explainer

From your study of information asymmetry, you know that lenders cannot perfectly observe borrowers' actions or project quality, creating a fundamental wedge between the cost of internal and external funds. The **financial accelerator** is the mechanism by which this wedge amplifies and propagates economic shocks, turning what might be a mild downturn into a deep recession. The concept, developed primarily by Bernanke, Gertler, and Gilchrist, explains why financial markets do not merely reflect real economic conditions but actively worsen them.

The starting point is the **external finance premium** — the extra cost a borrower pays over the risk-free rate to compensate lenders for the information problems inherent in lending. This premium depends critically on the borrower's **net worth**: the value of assets minus liabilities. When a firm or household has substantial net worth, they can post collateral and have more "skin in the game," reducing the lender's exposure to default. The external finance premium falls, and credit flows freely. But when net worth declines — because asset prices drop, profits fall, or debts increase — lenders face greater risk and charge higher spreads. Credit tightens precisely when borrowers need it most.

The amplification arises from the feedback loop between asset prices, net worth, and borrowing conditions. Consider a negative productivity shock that reduces profits and lowers the value of firms' assets. Lower asset values reduce net worth, which raises the external finance premium, which increases the cost of investment. Reduced investment further depresses economic activity and asset prices, which further erodes net worth. Each round of the cycle amplifies the original shock. This is why the mechanism is called an "accelerator" — it does not create shocks, but it makes them larger and more persistent than they would be in a frictionless economy. A 1% decline in productivity might produce a 3% decline in investment once the financial accelerator is operating.

The mechanism also works in reverse during booms: rising asset prices increase net worth, lower credit spreads, stimulate borrowing and investment, and drive asset prices higher still. This symmetry means the financial accelerator amplifies both expansions and contractions, contributing to boom-bust cycles. The 2008 financial crisis was a dramatic illustration: falling house prices destroyed household and bank balance sheets, credit spreads skyrocketed, lending froze, and the resulting collapse in spending fed back into further asset price declines. Understanding this mechanism is essential for designing macroprudential policy — regulations that aim to prevent excessive leverage buildup during booms so that the accelerator has less fuel when the inevitable downturn arrives.
