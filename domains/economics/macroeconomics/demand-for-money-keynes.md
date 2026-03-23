---
id: demand-for-money-keynes
title: Keynes's Demand for Money
domain: economics
course: macroeconomics
prerequisites:
- id: money-and-its-functions
  type: hard
builds-toward:
- liquidity-preference-theory-keynes
- is-lm-model
tags:
- money-demand
- keynes
- liquidity
- motives
stage: formal-systems
status: draft
---

# Keynes's Demand for Money

## Core Idea
Keynes identified three motives for holding money: transactions (regular purchases), precautionary (unexpected expenses), and speculative (avoiding capital losses when rates are expected to rise). Money demand increases with income and decreases with interest rates.

## How It's Best Learned
Illustrate each motive with concrete examples. Show how total money demand combines all three components.

## Common Misconceptions
- Assuming all money demand is for transactions.
- Treating money demand as purely exogenous.
- Confusing money demand with credit demand.

## Questions

```yaml
- question: "Interest rates in the economy rise unexpectedly. According to Keynes's theory, what happens to speculative money demand?"
  type: multiple-choice
  options:
    - "It increases — higher rates signal economic growth and people want more liquidity"
    - "It decreases — bonds now offer higher yields and potential capital gains, making money costly to hold"
    - "It stays the same — speculative demand depends on income, not interest rates"
    - "It increases — people want to hold cash to deploy it when rates eventually fall"
  answer: 1
  explanation: "When rates rise, bonds become more attractive relative to money: they offer high current yield and, if rates are expected to stabilize or fall, prospective capital gains as bond prices recover. Money earns nothing, so the opportunity cost of holding money rises with the interest rate. Speculative demand for money therefore falls as rates rise — this is the downward-sloping liquidity preference curve. Option 3 sounds plausible but is incorrect: if rates have risen and are expected to fall, you want to hold bonds (to capture both yield and capital gain) not money."

- question: "A business keeps a buffer of cash on hand specifically to cover unexpected equipment repairs and emergency expenses. This best illustrates which Keynesian motive?"
  type: multiple-choice
  options:
    - "Transactions motive"
    - "Speculative motive"
    - "Precautionary motive"
    - "Liquidity preference"
  answer: 2
  explanation: "The precautionary motive covers money held as a buffer against unexpected expenses — emergencies, unplanned costs, contingencies. The transactions motive covers routine, predictable purchases. The speculative motive covers money held as an alternative to bonds to avoid capital losses. 'Liquidity preference' names the overall money demand function, not a specific motive. The scenario describes contingency-based holding, not routine spending or a bet on interest rates."

- question: "If an individual expects interest rates to rise in the future, Keynes's theory says they should hold more bonds now to capture the higher future yields."
  type: true-false
  answer: false
  explanation: "This is the key misconception about the speculative motive. When rates are expected to rise, existing bond prices will fall — bonds and interest rates move inversely. Holding bonds in anticipation of rising rates means suffering capital losses that could exceed the interest earned. The rational response is to hold money instead — preserving nominal value — until rates stabilize or peak. Higher future yields apply to newly issued bonds; what you currently hold will fall in price. This is why expected rate increases drive up speculative money demand."

- question: "Keynes's speculative motive implies that money demand and the interest rate are inversely related."
  type: true-false
  answer: true
  explanation: "When interest rates are low (or expected to rise), bonds are risky and unattractive — speculative demand for money is high. When rates are high (or expected to fall), bonds offer both yield and capital gains — money is relatively unattractive, so speculative demand falls. This inverse relationship is what gives the liquidity preference curve its downward slope, connecting the money market to interest rate determination and forming the basis of the LM curve."

- question: "Why is the speculative motive considered Keynes's most original contribution to understanding money demand? What problem does it solve that the transactions and precautionary motives don't address?"
  type: short-answer
  answer: "The transactions and precautionary motives explain why people need money to function — routine purchases and contingencies. But these motives would make money demand largely determined by income, with no clear link to interest rates. The speculative motive introduces the bond-vs-money trade-off: money demand also falls as rates rise because higher rates make bonds more attractive relative to holding idle cash. This is what gives monetary policy traction — changing the money supply shifts the interest rate until people willingly hold the new quantity. Without the speculative motive, there is no clear mechanism connecting money supply to interest rates."
  explanation: "The speculative motive is the hinge of Keynesian monetary theory. It explains why the liquidity preference curve slopes downward (not vertical), why interest rates are determined in the money market, and why central bank policy can influence rates by changing the money supply. The other two motives are about necessity; the speculative motive is about portfolio choice — and that's what makes it theoretically powerful."
```

## Explainer

From your work on money's functions, you know that money serves as a medium of exchange, a store of value, and a unit of account. These functions naturally give rise to distinct reasons why individuals and businesses want to hold money balances rather than converting them into interest-bearing assets. Keynes was the first to systematically decompose money demand into its component motivations, and that decomposition remains the foundation of monetary economics.

The **transactions motive** is the most intuitive: people need money on hand to make routine purchases. Even if income arrives weekly or monthly, spending is continuous — you need cash to pay for groceries on Tuesday even if your paycheck doesn't arrive until Friday. The quantity of money demanded for this purpose rises roughly proportionally with income: more income means more purchases, which means larger cash buffers. The **precautionary motive** is an extension of the transactions motive: people also hold extra money as a buffer against unexpected expenses — a medical bill, a car repair, an emergency. This demand also rises with income, partly because higher-income individuals have more at stake and partly because their expenditure patterns are more variable.

The **speculative motive** is Keynes's most original contribution and his most lasting insight about why interest rates affect money demand. The alternative to holding money is holding bonds, which pay interest but also fluctuate in price. Bond prices move inversely with interest rates: when rates rise, existing bond prices fall. If you expect interest rates to rise in the future, holding bonds is risky — you'll suffer a capital loss that could exceed the interest earned. In that case, it makes sense to hold money instead, preserving your nominal value while you wait for rates to stabilize. Conversely, when interest rates are high (expected to fall), bonds offer both high current yield and prospective capital gains, so money becomes costly to hold relative to bonds. The speculative demand for money therefore falls as the interest rate rises — a downward-sloping relationship in the money demand function.

Combining all three motives gives total money demand as Mᵈ = L(Y, i), increasing in income Y and decreasing in the nominal interest rate i. This function — the **liquidity preference** curve — is the demand side of the money market. Its interaction with the money supply determines the equilibrium interest rate, which is the core mechanism through which monetary policy affects the real economy in the Keynesian framework and the building block of the LM curve in the IS-LM model you'll study next. The critical insight is that money is not demanded just for transactions; it is held because it offers liquidity — the ability to act quickly in an uncertain world — and the price of that liquidity is the foregone interest on bonds.
