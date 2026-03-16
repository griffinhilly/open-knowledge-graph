---
id: interest-rates-and-loanable-funds
title: Interest Rates and the Loanable Funds Market
domain: economics
course: macroeconomics
prerequisites:
- id: money-and-its-functions
  type: hard
- id: supply-and-demand-basics
  type: hard
- id: market-equilibrium
  type: hard
- id: money-supply-and-money-creation
  type: soft
builds-toward:
- is-lm-model
- fiscal-multiplier
tags:
- interest-rate
- loanable-funds
- saving
- investment
- crowding-out
stage: abstract-reasoning
status: validated
---
# Interest Rates and the Loanable Funds Market

## Core Idea
The loanable funds model treats the interest rate as the price that equilibrates saving (supply of funds) and investment (demand for funds). Households and government savings supply funds; businesses borrow to invest. The real interest rate — the nominal rate adjusted for expected inflation — is the relevant variable for economic decisions. Government budget deficits reduce national saving, shifting the supply of loanable funds left, raising real interest rates, and 'crowding out' private investment. This model is a classical view; the Keynesian IS-LM framework embeds a more dynamic treatment.

## How It's Best Learned
Draw supply and demand for loanable funds. Then trace the effects of: (1) government deficit increase, (2) increase in consumer confidence, (3) technological boom raising investment returns. In each case identify what shifts and how the equilibrium interest rate changes.

## Common Misconceptions
- The loanable funds model assumes full employment; in a recession with slack, crowding out is less severe.
- The nominal interest rate and real interest rate can diverge substantially during inflation; decisions should be based on real rates.
- Saving and investment are equal ex post by accounting identity, but the model shows how they are brought into equality through interest rate adjustment.

## Questions

```yaml
- question: "The government increases its budget deficit sharply. In the loanable funds model, the most direct effect is:"
  type: multiple-choice
  options:
    - "An increase in the supply of loanable funds, lowering the real interest rate"
    - "A decrease in the supply of loanable funds, raising the real interest rate and crowding out private investment"
    - "An increase in the demand for loanable funds, lowering the real interest rate"
    - "No effect, because the central bank controls interest rates, not the government"
  answer: 1
  explanation: "Government dissaving (a deficit) reduces national saving — the government is borrowing from the pool of loanable funds rather than contributing to it. This shifts the supply curve left, raising the equilibrium real interest rate. Higher rates make private investment more expensive, reducing it — the crowding-out effect. The central bank sets the nominal policy rate, but the loanable funds model focuses on the real rate determined by saving and investment flows."

- question: "If the nominal interest rate is 7% and expected inflation is 4%, economic decisions about borrowing and lending should be based on a 7% interest rate."
  type: true-false
  answer: false
  explanation: "The relevant rate for real economic decisions is the real interest rate — approximately nominal rate minus expected inflation, so about 3% here. Borrowers repay in future dollars that are worth less due to inflation, so the real burden of debt is lower than the nominal rate suggests. Lenders likewise earn less in purchasing-power terms. Basing decisions on the nominal rate would overstate the true cost of borrowing and the true return to saving."

- question: "In the loanable funds model, saving and investment must be equal in equilibrium. What mechanism brings them into equality when they start out unequal?"
  type: short-answer
  answer: "The real interest rate adjusts. If desired saving exceeds desired investment, excess supply pushes the rate down, discouraging saving and encouraging more investment until they equate. The reverse happens when investment demand exceeds saving."
  explanation: "The interest rate functions as the price in the market for loanable funds — it coordinates the decisions of savers and investors. Unlike the ex-post accounting identity (S = I by definition in a closed economy), the model describes the equilibrating process: how mismatches between desired saving and desired investment are resolved through price adjustment. This is the classic supply-and-demand mechanism applied to capital."
```

## Explainer

You already know how supply and demand work in a goods market: a price adjusts to equate the quantity supplied with the quantity demanded. The loanable funds model applies the exact same logic to the market for borrowable money. The 'price' in this market is the real interest rate — the nominal rate adjusted for expected inflation. Savers supply funds (the upward-sloping supply curve) because higher rates reward waiting. Borrowers demand funds (the downward-sloping demand curve) because lower rates make investment projects profitable. The equilibrium real interest rate is where these curves cross.

Who are the suppliers and demanders of loanable funds? On the supply side: households save part of their income, and any government surplus adds to national saving. On the demand side: businesses borrow to finance investment in plant, equipment, and inventory; sometimes the government borrows to fund deficits. The supply curve slopes upward because higher rates induce more saving; the demand curve slopes downward because higher rates make fewer investment projects financially viable (a project must earn at least as much as the cost of financing it).

The crowding-out effect is the central policy application of this model. When the government runs a deficit, it must borrow — it enters the loanable funds market on the demand side or, equivalently, reduces national saving (negative public saving offsets private saving). Either way, the supply of loanable funds shrinks, the interest rate rises, and private investment falls. The government is 'crowding out' private investment by competing for the same pool of savings. The size of this effect is contested — it is most pronounced when the economy is at full employment and every dollar the government borrows is a dollar no longer available to businesses.

The real vs. nominal distinction is critical and often confused. The nominal interest rate is the number quoted in loan contracts and savings accounts — it is the rate you see. The real rate is what actually matters for saving and investment decisions, because it measures the purchasing-power return to saving and the purchasing-power cost of borrowing. If inflation is running at 5%, a 7% nominal return is only a 2% real return. Economic decisions — whether to build a factory, whether to save for retirement — depend on real rates, not nominal ones. The loanable funds model is explicitly a model of real interest rate determination.

One important caveat: the loanable funds model assumes the economy is at full employment. In a deep recession, with idle workers and capital, the crowding-out story weakens — government borrowing may draw on resources that would otherwise sit unused, rather than displacing private investment. This is why Keynesian economists, working in the IS-LM framework, give a more nuanced picture of fiscal policy at different stages of the business cycle. The loanable funds model is the right starting point for long-run analysis; the IS-LM model extends it to handle short-run fluctuations.

