---
id: government-spending-multiplier
title: Government Spending Multiplier in Macroeconomic Models
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: fiscal-multiplier
  type: soft
- id: new-keynesian-framework-overview
  type: hard
tags:
- government-spending-multiplier
- demand-stimulus
- fiscal-policy-impact
stage: expert
status: validated
---

# Government Spending Multiplier in Macroeconomic Models

## Core Idea
The government spending multiplier measures the change in aggregate output from a unit increase in government purchases. In New Keynesian models, the multiplier typically lies between 0.5 and 2, depending on monetary policy stance (larger when the central bank keeps interest rates low) and whether the economy is at the ZLB.

## Questions

```yaml
- question: "An economy is operating normally with the central bank following a Taylor rule. The government increases spending by $100 billion. According to the New Keynesian model, what happens to aggregate output?"
  type: multiple-choice
  options:
    - "Output rises by more than $100 billion as spending creates additional rounds of private consumption"
    - "Output rises by exactly $100 billion because each dollar of spending becomes one dollar of output"
    - "Output rises by less than $100 billion because the central bank raises interest rates in response to inflation, crowding out private spending"
    - "Output is unchanged because private saving falls by exactly the amount of government spending"
  answer: 2
  explanation: "Under a Taylor rule, the central bank responds to fiscal-induced inflation by raising nominal interest rates more than one-for-one. This increase in interest rates raises the cost of borrowing and reduces private consumption and investment — the crowding-out effect. The net multiplier is therefore less than 1 (typically 0.5–1.0 in standard calibrations): a dollar of government spending generates less than a dollar of additional output because monetary tightening offsets part of the fiscal impulse. The simple Keynesian cross formula 1/(1-MPC) ignores this monetary feedback entirely."

- question: "In a New Keynesian model, why is the government spending multiplier larger when the economy is at the zero lower bound (ZLB) than under normal conditions?"
  type: multiple-choice
  options:
    - "At the ZLB the government borrows at zero interest rates, eliminating the fiscal cost of spending"
    - "At the ZLB the central bank cannot raise nominal rates, so higher inflation expectations lower the real rate and amplify private spending"
    - "At the ZLB households are financially distressed and spend a higher fraction of any income increase"
    - "The multiplier is fixed at 2.0 at the ZLB by definition in New Keynesian models"
  answer: 1
  explanation: "At the ZLB, the nominal interest rate is stuck at zero, so the central bank cannot tighten in response to fiscal-induced inflation — the crowding-out channel is disabled. Instead, higher inflation expectations cause the real interest rate (nominal minus expected inflation) to fall, which stimulates private consumption and investment. The fiscal and private demand effects now reinforce rather than offset each other, creating a positive feedback loop. Under typical ZLB calibrations, multipliers can reach 1.5–2.0 or higher. This is the state-dependence: the same fiscal policy through the same model produces very different outcomes depending on the monetary regime."

- question: "In the standard New Keynesian model with an active Taylor rule, the government spending multiplier is typically greater than 1."
  type: true-false
  answer: false
  explanation: "This is the common misconception inherited from the simple Keynesian cross. The naive formula 1/(1-MPC) can produce large multipliers, but the New Keynesian model adds a crucial feedback: active monetary policy. When government spending raises output and inflation, the Taylor rule prescribes raising interest rates, which crowds out private spending. Standard calibrations produce multipliers between 0.5 and 1.0 under active monetary policy — less than one dollar of output per dollar of spending. Multipliers greater than 1 require either monetary accommodation (rates held fixed) or the ZLB."

- question: "The government spending multiplier in New Keynesian models depends critically on the monetary policy regime, meaning two economists who agree on the model's structure can reach different conclusions about the size of the multiplier."
  type: true-false
  answer: true
  explanation: "This is the central insight: the multiplier is not a fixed structural parameter but a policy-regime-dependent outcome. An economist assuming the central bank will fully accommodate the fiscal expansion (hold rates fixed) will estimate a large multiplier. An economist assuming an active Taylor rule will estimate a small multiplier. Both can be using the same model with the same MPC and the same parameter values — the disagreement is entirely about the assumed monetary policy response. This explains why economists who agree on theory can disagree sharply on policy: they are implicitly assuming different monetary regimes."

- question: "Two economists both accept the New Keynesian model but disagree sharply about whether a large fiscal stimulus is a good idea. They are not disagreeing about the model's structure. What key assumption drives their disagreement about the multiplier's size?"
  type: short-answer
  answer: "The key assumption is the monetary policy response. If the central bank follows an active Taylor rule, it raises interest rates in response to fiscal-induced inflation, partially offsetting the stimulus through crowding out (multiplier < 1). If the central bank is at the ZLB and cannot raise rates, higher inflation expectations actually lower the real rate and amplify the stimulus (multiplier > 1.5). Disagreement about what the central bank will do — or is constrained to do — produces the disagreement about fiscal effectiveness."
  explanation: "This is one of the most practically important insights in modern macroeconomics. The multiplier debate of the 2009–2010 stimulus period was largely a debate about monetary accommodation. Economists who thought the Fed would eventually tighten were skeptical of large multipliers; economists who thought the ZLB would persist for years predicted larger effects. Both camps used New Keynesian models. The empirical evidence broadly supports larger multipliers at the ZLB and during recessions, consistent with the theory."
```

## Explainer

From the basic fiscal multiplier concept, you know the intuition: government spending injects demand into the economy, and each dollar of spending can generate more (or less) than a dollar of additional output depending on how the rest of the economy responds. In the simplest Keynesian cross model, the multiplier is 1/(1−MPC), where MPC is the marginal propensity to consume. But this undergraduate formula ignores crucial feedback loops that the **New Keynesian framework** takes seriously — most importantly, the response of monetary policy and the role of expectations.

In a standard New Keynesian model, a government spending increase raises aggregate demand, which pushes up output and inflation. If the central bank follows a **Taylor rule**, it responds to higher inflation by raising the nominal interest rate more than one-for-one. This interest rate increase reduces private consumption and investment — the familiar **crowding-out effect**. The net multiplier is therefore less than the naive Keynesian calculation because monetary tightening partially offsets the fiscal stimulus. Under typical calibrations, the multiplier lands between 0.5 and 1.0: a dollar of government spending generates less than a dollar of additional output because private spending contracts.

The picture changes dramatically at the **zero lower bound (ZLB)**. When the nominal interest rate is already at zero, the central bank *cannot* raise rates in response to higher inflation — it is constrained. A fiscal expansion still raises inflation, but now the real interest rate (nominal rate minus expected inflation) actually *falls*, because the nominal rate is stuck at zero while inflation expectations rise. A lower real interest rate stimulates rather than discourages private spending, creating a positive feedback loop: government spending raises demand, which raises inflation expectations, which lowers real rates, which raises private demand, which raises output further. At the ZLB, multipliers can easily exceed 1.5 or even 2.0 — each dollar of government spending generates well more than a dollar of additional output because private spending amplifies rather than offsets the fiscal impulse.

This state-dependence is the central lesson. The multiplier is not a fixed number — it depends critically on the **monetary policy regime**. In normal times with an active Taylor rule, fiscal stimulus is partially self-defeating because it provokes monetary tightening. In a liquidity trap or when the central bank accommodates by holding rates fixed, fiscal policy becomes far more powerful. This explains why economists who agree on the underlying model can disagree sharply about the wisdom of fiscal stimulus: they may be assuming different monetary policy responses. The empirical evidence broadly supports this distinction, with estimated multipliers during recessions and ZLB episodes significantly larger than those during normal expansions.
