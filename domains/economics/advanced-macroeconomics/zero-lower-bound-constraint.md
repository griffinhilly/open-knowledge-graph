---
id: zero-lower-bound-constraint
title: Zero Lower Bound on Nominal Interest Rates
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: taylor-rule-monetary-policy
  type: hard
- id: interest-rates-and-loanable-funds
  type: soft
builds-toward:
- quantitative-easing-unconventional-policy
tags:
- monetary-constraint
- liquidity-trap
- unconventional-policy
stage: expert
status: validated
---

# Zero Lower Bound on Nominal Interest Rates

## Core Idea
The zero lower bound constraint prevents nominal interest rates from going significantly negative, constraining monetary policy's ability to stimulate demand during severe recessions. When the ZLB binds, central banks cannot reduce real interest rates further through conventional policy and must resort to unconventional measures like quantitative easing. Understanding the ZLB is crucial for analyzing monetary policy effectiveness in deep downturns and explaining the puzzlingly low inflation in many developed economies.

## Questions

```yaml
- question: "The Taylor rule prescribes a nominal interest rate of −4% for a severely depressed economy. The central bank can only cut its policy rate to 0%. What is the direct consequence of this gap?"
  type: multiple-choice
  options:
    - "The central bank can still achieve the prescribed rate by printing money directly"
    - "Real interest rates remain too high to restore full employment through conventional policy"
    - "Fiscal policy is automatically crowded out and becomes less effective"
    - "Inflation expectations rise to close the gap, restoring the real rate to its target"
  answer: 1
  explanation: "When the ZLB binds, the central bank cannot deliver the negative nominal rate the Taylor rule prescribes. Real interest rates (nominal minus expected inflation) may therefore remain above their full-employment target, leaving borrowing and investment too expensive. Option C is precisely backwards: at the ZLB, fiscal policy is *more* effective because the central bank will not raise rates to offset stimulus (no crowding out). Option D is wishful thinking — in a depressed economy, inflation expectations typically fall, which *raises* real rates further."

- question: "At the zero lower bound, what happens to the fiscal policy multiplier compared to normal times?"
  type: multiple-choice
  options:
    - "It shrinks to zero because private spending substitutes one-for-one with government spending"
    - "It is unchanged because monetary policy does not interact with fiscal policy"
    - "It grows larger because the central bank will not raise rates in response to the stimulus"
    - "It shrinks because the government must borrow, crowding out private investment"
  answer: 2
  explanation: "In normal times, fiscal expansion can trigger the central bank to raise rates preemptively, crowding out some private spending (partial offset). At the ZLB, the central bank *wants* more demand and has already cut rates as far as it can — it will not tighten in response to fiscal stimulus. This means government spending generates more additional output than it would in normal times: the ZLB paradoxically makes fiscal policy its most powerful instrument precisely when monetary policy is weakest."

- question: "Once a central bank hits the zero lower bound, it has exhausted most its policy tools and can do hardly anything further to stimulate the economy."
  type: true-false
  answer: false
  explanation: "The ZLB constrains *conventional* monetary policy — cutting the short-term policy rate. But central banks retain unconventional tools: quantitative easing (purchasing long-term assets to compress term premiums and yield spreads), forward guidance (credibly committing to keep rates low for an extended period to shape expectations), and in some cases negative interest rate policy on bank reserves. These tools operate through different transmission channels than the short-term rate. The ZLB marks the end of one toolkit, not all tools."

- question: "At the ZLB, falling inflation expectations can cause real interest rates to rise even though the nominal rate remains fixed at zero."
  type: true-false
  answer: true
  explanation: "This is one of the ZLB's most dangerous dynamics. The real interest rate equals the nominal rate minus expected inflation. If the nominal rate is stuck at zero and inflation expectations fall from, say, 2% to −1%, the real rate rises from −2% to +1% — tightening financial conditions without any central bank action. A contractionary spiral can result: weak demand lowers inflation expectations, raising real rates, which further weakens demand. This is the modern formalization of Keynes's liquidity trap, where conventional monetary easing becomes impossible precisely when it is most needed."

- question: "Why does the existence of physical cash create a lower bound on nominal interest rates, and roughly where does that bound sit?"
  type: short-answer
  answer: "Cash earns a nominal return of exactly zero. If a bank offered deposit rates significantly below zero, depositors could withdraw funds and hold physical currency instead, earning zero rather than a negative rate. This arbitrage puts a floor on how far rates can fall — approximately zero. In practice the floor is slightly below zero (some central banks have implemented small negative rates) because holding large quantities of physical cash is costly and inconvenient, but deep negative rates are not feasible without triggering mass cash hoarding."
  explanation: "The key insight is that cash is a zero-interest-bearing asset that anyone can hold. The ZLB is therefore not an institutional rule or policy choice — it is a consequence of this basic arbitrage. Central banks cannot mandate that people accept negative nominal returns on the safest possible asset. This contrasts with real interest rates, which have no such constraint and can be arbitrarily negative (as they have been in many economies with low nominal rates and positive inflation)."
```

## Explainer

From the Taylor rule, you know that central banks set nominal interest rates in response to inflation and the output gap — raising rates when the economy overheats, cutting them when it slumps. The Taylor rule is a simple, powerful prescription. But it has a hidden assumption: that the central bank can always cut rates as far as the formula says it should. The **zero lower bound** is the point where this assumption breaks down.

The logic behind the bound is straightforward. Cash earns a nominal return of exactly zero. If a bank offered a deposit rate of negative 3%, you could withdraw your money, hold physical currency, and earn a better return by doing literally nothing. This arbitrage means nominal interest rates cannot fall far below zero — the existence of cash puts a floor under them. (In practice, some central banks have pushed rates slightly negative, because holding large amounts of physical cash is costly and inconvenient. But the floor is real: rates cannot go deeply negative without triggering mass cash hoarding.)

The ZLB becomes a crisis when a severe recession calls for rates far below zero. Suppose the Taylor rule prescribes a rate of negative 5%, but the central bank can only cut to zero. The gap between the rate the economy needs and the rate the central bank can deliver is the **ZLB constraint**. With rates stuck at zero, real interest rates (nominal rate minus expected inflation) may still be too high to stimulate borrowing, investment, and spending. Worse, if the weak economy causes inflation expectations to fall, real rates actually *rise* even as nominal rates sit at zero — a contractionary spiral that conventional monetary policy cannot break.

This is the modern version of Keynes's **liquidity trap**: monetary policy loses its primary transmission mechanism. When the ZLB binds, the central bank is "pushing on a string" — it wants to ease conditions further but has exhausted its conventional tool. This is why central banks after 2008 turned to **unconventional policies**: quantitative easing (purchasing long-term assets to compress term premiums), forward guidance (committing to keep rates low for longer to shape expectations), and in some cases negative interest rate policy on bank reserves. Each of these tools works through different channels than the short-term rate, and each has limitations and side effects that conventional rate cuts do not.

The ZLB also has deep implications for fiscal policy. In normal times, a fiscal expansion may be partially offset by higher interest rates (crowding out). But at the ZLB, the central bank will not raise rates in response to fiscal stimulus — it *wants* more demand. This means the fiscal multiplier is larger at the ZLB than in normal times, giving fiscal policy an unusually powerful role precisely when monetary policy is constrained. Understanding when the ZLB binds, and how it transforms the policy landscape, is essential for analyzing any severe recession or deflationary episode in modern macroeconomics.
