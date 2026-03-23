---
id: liquidity-preference-theory-keynes
title: Liquidity Preference Theory and Interest Rate Determination
domain: economics
course: macroeconomics
prerequisites:
- id: demand-for-money-keynes
  type: hard
- id: money-supply-and-money-creation
  type: hard
builds-toward:
- is-lm-model
tags:
- interest-rates
- liquidity-preference
- money-supply
- equilibrium
stage: formal-systems
status: validated
---

# Liquidity Preference Theory and Interest Rate Determination

## Core Idea
Liquidity preference theory explains interest rate determination as equilibrium between money supply (controlled by central bank) and money demand. The interest rate adjusts so desired money holdings equal the money supply.

## How It's Best Learned
Use supply-demand diagram for money: money supply is vertical, money demand slopes downward. Shift money demand with income or expectations changes; show equilibrium interest rate adjusts.

## Common Misconceptions
- Assuming money supply is endogenously determined.
- Confusing money market with aggregate supply-demand equilibrium.
- Treating interest rates as purely nominal.

## Questions

```yaml
- question: "The central bank increases the money supply. According to liquidity preference theory, what is the direct chain of events that lowers interest rates?"
  type: multiple-choice
  options:
    - "The government announces lower rates, and expectations adjust immediately"
    - "People find themselves holding more cash than they want at the existing rate, so they buy bonds; higher bond demand raises bond prices, which lowers bond yields (the interest rate)"
    - "Higher money supply raises inflation, which automatically lowers real interest rates"
    - "Banks are required to lend more when reserves increase, which forces competitive rate cuts"
  answer: 1
  explanation: "The transmission mechanism in liquidity preference theory runs through the bond market. When the money supply exceeds desired money holdings, people are 'overloaded' with liquidity — they try to exchange excess cash for bonds. This demand pushes bond prices up, and since bond yields move inversely to prices, interest rates fall. This continues until the new equilibrium is reached where desired money holdings equal the new, larger money supply."

- question: "Keynes argued that monetary policy loses effectiveness in a 'liquidity trap.' Which description is correct?"
  type: multiple-choice
  options:
    - "Banks hold too much liquidity in reserve and refuse to lend to businesses"
    - "A legal cap on money supply prevents the central bank from expanding further"
    - "At very low interest rates, money demand becomes nearly unlimited — additional money injected by the central bank is absorbed as idle cash rather than pushing rates down further"
    - "Consumers spend money so quickly that any monetary injection circulates out of the banking system"
  answer: 2
  explanation: "In the liquidity trap, people widely expect interest rates to rise (bond prices to fall), so they prefer holding cash over bonds. The speculative demand for money becomes nearly infinitely elastic near zero rates — any new money is willingly absorbed without driving rates lower. This is why Keynes argued that in a depression, fiscal policy (government spending) rather than monetary policy was the appropriate tool."

- question: "In Keynes's liquidity preference framework, the interest rate is essentially the price of borrowing money from savers who want a return on their savings."
  type: true-false
  answer: false
  explanation: "This is the classical loanable-funds view, which Keynes explicitly replaced. In Keynes's framework, the interest rate is the price of liquidity — the return required to persuade people to give up cash and hold less-liquid assets like bonds. The key motivation is speculative: people hold money when they expect bond prices to fall (interest rates to rise), not simply to earn a return on past saving."

- question: "In a liquidity trap, fiscal policy may be more effective than monetary policy at stimulating aggregate demand."
  type: true-false
  answer: true
  explanation: "When interest rates are at (or near) zero, the standard monetary transmission mechanism breaks down — new money is absorbed as idle cash without reducing rates further. Investment and spending cannot be stimulated by lower borrowing costs because rates cannot go lower. Fiscal policy (government spending or tax cuts) injects demand directly without relying on the interest rate channel, which is why Keynes advocated it for the Great Depression and why it re-emerged as a live debate after 2008."

- question: "Explain the mechanism by which an increase in the money supply lowers interest rates in the liquidity preference framework."
  type: short-answer
  answer: "An increase in the money supply creates an excess supply of money at the existing interest rate — people hold more cash than they wish to. To reduce their cash holdings, they buy bonds. This increased demand drives bond prices up. Since bond yields (interest rates) move inversely to bond prices, rates fall. This process continues until desired money holdings again equal the (larger) money supply, establishing a new, lower equilibrium interest rate."
  explanation: "The key is that equilibrium is restored through the bond market, not through direct announcement. The central bank never sets rates by fiat in this model — it adjusts the money supply, and market participants respond by buying or selling bonds until desired money holdings match actual money supply. This indirect channel is also why the liquidity trap is so problematic: if bond prices are already high and everyone expects them to fall, the extra money simply sits as cash instead of flowing into bonds."
```

## Explainer

Your prerequisites gave you two building blocks: Keynes's theory of money demand (why people want to hold cash rather than bonds) and how the central bank controls the money supply. Liquidity preference theory assembles these into a model of **how the interest rate itself is determined** — a fundamentally different answer from the classical loanable-funds framework you may have studied, and the foundation for much of Keynesian macroeconomics.

Keynes's central reframing is to treat the interest rate not as the price of saving versus consumption but as the **price of liquidity** — the return required to induce people to part with cash and hold less-liquid assets like bonds. People hold money for three reasons: **transactions demand** (cash needed for everyday spending, which rises with income), **precautionary demand** (a buffer against unexpected expenses), and **speculative demand** (holding cash when you expect bond prices to fall — that is, when you expect interest rates to rise). The speculative motive makes money demand interest-sensitive in a way classical theory ignored: when interest rates are high, bonds look attractive (prices more likely to rise as rates fall), so people want to hold more bonds and less cash. When rates are low, cash looks relatively safe compared to bonds that could lose value if rates rise. This produces a **downward-sloping money demand curve**: as the interest rate rises, desired money holdings fall.

The **money supply** in this framework is set exogenously by the central bank — it is a **vertical line** in the money market diagram (with money quantity on the horizontal axis and the interest rate on the vertical). The equilibrium interest rate is where money supply equals money demand. If the central bank increases the money supply (shifts the vertical line rightward), at the old equilibrium rate there is now an excess supply of money: people hold more cash than they want. They respond by buying bonds, which drives bond prices up — and since bond prices and yields move inversely, the interest rate falls until a new equilibrium is reached. This is the **monetary transmission mechanism**: the central bank injects money → interest rate falls → borrowing costs fall → investment rises → output expands.

The famous failure of this mechanism is the **liquidity trap**. If interest rates are already very low, the speculative demand for money becomes nearly unlimited — people widely expect rates to rise (bond prices to fall) and prefer to hold cash rather than bonds. The money demand curve becomes nearly horizontal near zero rates. In this regime, any additional money injected by the central bank is simply absorbed into idle cash balances without pushing rates down further. Monetary policy loses traction. This was Keynes's argument that fiscal policy — not monetary policy — was the appropriate tool during the Great Depression. The liquidity trap re-emerged as a live policy debate after the 2008 financial crisis, when many central banks cut rates to the zero lower bound and found their usual transmission mechanism weakened. The concept of **quantitative easing** (purchasing long-term assets rather than just short-term bonds) was developed in part as a response to this limitation.
