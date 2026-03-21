---
id: aggregate-demand-expenditure-approach
title: 'Aggregate Demand: The Expenditure Approach'
domain: economics
course: macroeconomics
prerequisites:
- id: consumption-function-keynesian
  type: hard
- id: investment-demand-interest-sensitivity
  type: hard
- id: gdp-components
  type: hard
builds-toward:
- short-run-sticky-price-equilibrium
- demand-shock-output-inflation-effects
tags:
- aggregate-demand
- expenditure
- multiplier
- consumption
- investment
stage: formal-systems
status: draft
---

# Aggregate Demand: The Expenditure Approach

## Core Idea
The expenditure approach to aggregate demand emphasizes total spending: AD = C + I + G + (X − M). Demand shifts amplify through the multiplier, though crowding out and supply constraints attenuate effects.

## How It's Best Learned
Build a simple Keynesian model: C = a + b*Y, I = I_0 − d*r, G and X−M exogenous. Solve for equilibrium Y. Show multiplier: each unit autonomous spending raises Y by 1/(1−b).

## Common Misconceptions
- Assuming multiplier is same for all spending types.
- Forgetting multiplier depends on monetary policy response.
- Treating multiplier as time-invariant.

## Questions

```yaml
- question: "The marginal propensity to consume (MPC) is 0.75. The government increases spending by $200 billion. In the simple Keynesian model, what is the total change in GDP?"
  type: multiple-choice
  options:
    - "$200 billion — government spending adds directly to GDP, dollar for dollar"
    - "$150 billion — only the fraction b = 0.75 of the spending circulates"
    - "$800 billion — the multiplier is 1/(1 − 0.75) = 4"
    - "$600 billion — the multiplier applies only to the induced rounds, not the initial injection"
  answer: 2
  explanation: "The Keynesian multiplier is 1/(1 − MPC) = 1/(1 − 0.75) = 4. So $200bn × 4 = $800bn. The initial $200bn enters income directly; recipients spend $150bn (75%), those recipients spend $112.5bn, and so on — a geometric series that sums to $200bn × 4. Option D is a common error: the formula 1/(1−MPC) already includes the initial injection in the total."

- question: "Which factor most directly explains why real-world fiscal multipliers are consistently smaller than the simple formula 1/(1−MPC) predicts?"
  type: multiple-choice
  options:
    - "People don't actually spend exactly the MPC fraction of each income round"
    - "Government cannot accurately measure the MPC in real time"
    - "Crowding out, import leakage, and monetary policy tightening absorb part of the stimulus"
    - "The multiplier formula only applies to tax cuts, not government spending"
  answer: 2
  explanation: "The textbook multiplier 1/(1−MPC) assumes no leakages and no offsetting policy responses. In reality: (1) crowding out — government borrowing raises interest rates, reducing private investment; (2) import leakage — some income is spent on foreign goods rather than domestic output; (3) monetary policy — central banks may raise rates to prevent inflation, contracting interest-sensitive spending. All three attenuate the multiplier below its theoretical value."

- question: "A $100 billion direct government purchase of goods has a larger first-round multiplier impact than a $100 billion tax cut of the same size."
  type: true-false
  answer: true
  explanation: "Direct government purchases inject the full $100bn into GDP immediately — the multiplier is 1/(1−MPC). Tax cuts first pass through households: recipients save fraction (1−MPC) before spending the rest, so only MPC × $100bn enters the spending stream in the first round. The tax cut multiplier is MPC/(1−MPC). With MPC = 0.8, government purchases have a multiplier of 5 vs. 4 for an equivalent tax cut."

- question: "In the simple Keynesian model, increasing government spending always raises GDP by more than the initial increase, regardless of the state of the economy."
  type: true-false
  answer: false
  explanation: "The multiplier greater than 1 assumes spare capacity exists so output can actually increase. Near full employment, supply is constrained: extra demand raises prices rather than real output, attenuating the real GDP effect. Crowding out can reduce private investment, partially or fully offsetting the stimulus. With an active monetary policy (central bank raising rates in response), the effective multiplier can fall below 1 or even to zero. The simple model ignores these constraints."

- question: "Explain in your own words why a rise in government spending increases GDP by more than the initial injection — and what limits this amplification in practice."
  type: short-answer
  answer: "The initial spending becomes income for its recipients, who spend a fraction (MPC) of it, which becomes income for others, who spend MPC of that, and so on — a self-reinforcing chain that sums to 1/(1−MPC) times the original injection. In practice, leakages break the chain: households save part of each income round, some spending flows to imports rather than domestic output, government borrowing may crowd out private investment, and monetary tightening can offset the stimulus."
  explanation: "The circular flow logic is key: spending = income = spending. The multiplier captures the total amplification. The leakages — saving, imports, crowding out, monetary response — are the forces that bring the real-world multiplier well below its theoretical value, often below 1 in full-employment or open economies."
```

## Explainer

From your work on the Keynesian consumption function, you know that household consumption depends on income: C = a + bY, where b is the **marginal propensity to consume** (MPC) — the fraction of each additional dollar of income that households spend rather than save. From GDP components, you know that total output equals total expenditure. The expenditure approach to aggregate demand combines these ideas: total spending in the economy is AD = C + I + G + (X − M), and in equilibrium, actual output adjusts until it equals this planned expenditure. The central insight is that spending creates income, and income generates further spending — a circular flow that amplifies initial disturbances.

The **multiplier** is the formalization of this amplification. Suppose government spending rises by $100 billion. This directly adds $100bn to income. The recipients save fraction (1 − b) and spend fraction b, adding $100b × b to income. Those recipients do the same, adding $100b × b² — and so on. Summing the geometric series gives total income change = $100bn × 1/(1 − b). If b = 0.8, the multiplier is 5: a $100bn spending increase eventually raises GDP by $500bn. The logic is symmetric on the downside — a fall in investment or exports triggers a contractionary multiplier. This is the mechanism behind fiscal policy effectiveness in Keynesian models: government spending is not just worth $1, it is worth the multiplier times $1.

Real-world multipliers are substantially smaller than this simple formula suggests, for several reasons your model needs to accommodate. First, **crowding out**: government borrowing to finance the spending raises interest rates (or expectations of future taxes), which reduces private investment I. The investment component falls even as G rises, partially offsetting the stimulus. Second, if the economy is at or near full capacity, the output response is attenuated and the adjustment is absorbed partly by prices rather than output. Third, an **open economy leakage**: some of the extra income is spent on imports rather than domestic goods, so the multiplier is smaller as the import propensity rises. Fourth, monetary policy response: if the central bank raises rates to prevent inflation, the interest-sensitive components of spending (investment, housing) contract, shrinking the effective multiplier.

The multiplier also differs across types of spending. Transfers (like tax cuts or unemployment benefits) pass through households first, so only fraction b enters the spending stream immediately — the multiplier is b/(1−b). Direct government purchases enter GDP at full value immediately — multiplier is 1/(1−b). This is why economists often argue that direct government expenditure has a larger first-round impact than equivalent tax cuts, though both create long-run income effects of similar magnitude. The time dimension matters too: the full multiplier takes quarters to years to materialize, while the initial impact is just the direct effect. Real-time fiscal multiplier estimates range widely, from near zero in full-employment economies with active monetary policy to above 1.5 in deep recessions when the zero lower bound on interest rates prevents the central bank from offsetting the stimulus.
