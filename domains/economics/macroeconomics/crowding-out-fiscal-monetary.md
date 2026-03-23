---
id: crowding-out-fiscal-monetary
title: Crowding Out
domain: economics
course: macroeconomics
prerequisites:
- id: government-spending-multiplier
  type: hard
- id: interest-rates-and-loanable-funds
  type: hard
- id: monetary-policy-macroeconomics
  type: soft
builds-toward:
- ricardian-equivalence-and-debate
- fiscal-dominance-vs-monetary-independence
tags:
- fiscal-policy
- monetary-policy
- interest-rates
stage: advanced
status: validated
---

# Crowding Out

## Core Idea
Crowding out occurs when expansionary fiscal policy (higher government spending) increases interest rates, reducing private investment and partially offsetting the fiscal stimulus. In the extreme case of complete crowding out, the multiplier is zero because higher government spending entirely displaces private spending. The degree of crowding out depends on monetary policy and the interest elasticity of investment.

## Questions

```yaml
- question: "A government increases spending by $100 billion, financed by borrowing. Simultaneously, the central bank expands the money supply to keep interest rates unchanged. What happens to the crowding-out effect?"
  type: multiple-choice
  options:
    - "Crowding out is amplified because the money supply expansion raises inflation expectations"
    - "Crowding out is eliminated because stable interest rates prevent the reduction in private investment"
    - "Crowding out is unchanged because fiscal and monetary policy operate through separate channels"
    - "Crowding out is partial — monetary policy can only offset half the interest rate effect"
  answer: 1
  explanation: "Crowding out operates through the interest rate channel: government borrowing raises rates, which reduces private investment. If the central bank accommodates the fiscal expansion by expanding the money supply and keeping rates stable, the mechanism is broken. There is no interest rate rise, so no reduction in private investment. This illustrates why fiscal policy effectiveness is inseparable from monetary policy: the same deficit can have a large multiplier effect under monetary accommodation or near-zero multiplier under tight monetary policy."

- question: "Which factor is most important in determining how much private investment is 'crowded out' by a given increase in government borrowing?"
  type: multiple-choice
  options:
    - "The political party in power and its attitude toward business regulation"
    - "The size of the government's existing debt-to-GDP ratio"
    - "How sensitive business investment spending is to changes in the interest rate"
    - "Whether the spending is on infrastructure versus government salaries"
  answer: 2
  explanation: "The interest-elasticity of investment is the critical parameter. If businesses borrow heavily for investment and quickly abandon marginal projects when rates rise, even a small government-induced rise in rates causes a large drop in private spending — strong crowding out. If investment plans are relatively insensitive to borrowing costs (funded from retained earnings, or with long planning horizons), the same interest rate rise barely affects private spending — weak crowding out. This sensitivity, combined with monetary policy behavior, largely determines how much of the fiscal multiplier actually operates."

- question: "Complete crowding out — where every dollar of government spending displaces exactly one dollar of private spending — is the normal outcome of expansionary fiscal policy."
  type: true-false
  answer: false
  explanation: "Complete crowding out is the extreme classical case, which holds only when the economy is already at full capacity (output at potential) and the money supply is fixed. In this scenario, government borrowing competes for a fixed pool of savings, and the interest rate rises until private investment falls by exactly the amount of the government increase. In real economies with idle resources, monetary accommodation, or investment that is not highly interest-sensitive, crowding out is partial — the fiscal multiplier operates, just at reduced strength. Complete crowding out is a theoretical benchmark, not the typical empirical outcome."

- question: "If private investment is highly sensitive to interest rates, an increase in government borrowing will produce stronger crowding-out effects than if investment is relatively insensitive to rates."
  type: true-false
  answer: true
  explanation: "The mechanism runs: government borrowing → higher demand for loanable funds → higher interest rates → reduction in private investment. How much private investment falls depends directly on how responsive investment is to the rate change. High interest-elasticity means a given rate increase causes a large investment drop — strong crowding out. Low interest-elasticity means the same rate increase barely affects investment — weak crowding out. This is why the debate about crowding out ultimately reduces to empirical questions about the interest-sensitivity of investment in specific economic contexts."

- question: "Why is the debate about fiscal policy effectiveness inseparable from assumptions about what monetary policy does?"
  type: short-answer
  answer: "Crowding out works through the interest rate: government borrowing raises rates, which reduces private investment and partially offsets the fiscal stimulus. But whether rates actually rise depends on monetary policy. If the central bank accommodates fiscal expansion by expanding the money supply to keep rates stable, crowding out is eliminated and the full fiscal multiplier operates. If monetary policy is tight (fixed money supply), borrowing competes for a fixed pool of savings and crowding out is maximized. The same fiscal policy can produce very different outcomes depending on the monetary regime."
  explanation: "This interdependence is why the 'fiscal multiplier' is not a fixed number — it varies with the monetary policy regime and the business cycle position. In a liquidity trap (short-term rates at zero), monetary policy may be unable to offset fiscal stimulus, making the multiplier larger. Under normal conditions with an independent inflation-targeting central bank, monetary policy may offset fiscal stimulus to maintain its inflation target, reducing the multiplier toward zero. Understanding crowding out requires understanding the full macro policy mix."
```

## Explainer

You already know two things that combine to produce crowding out. First, from the government spending multiplier, you know that increased government spending stimulates aggregate demand by more than the initial injection — the multiplier works because each round of spending becomes income for someone else. Second, from the loanable funds model, you know that higher government borrowing increases demand for loanable funds, pushing the real interest rate up. Crowding out is what happens when you combine these two effects: the stimulus raises rates, and higher rates discourage private investment, partially undoing the stimulus.

The mechanism runs as follows. The government increases spending and finances it by borrowing — issuing bonds. This additional demand for credit shifts the demand curve in the loanable funds market rightward, raising the real interest rate. Higher interest rates increase the cost of capital for businesses considering new investment projects: factories, equipment, R&D. Projects that were borderline profitable at the old rate become unprofitable at the new rate and are abandoned. Household borrowing for big-ticket purchases also falls. This **reduction in private investment** partially offsets the government's expansionary impulse — the actual increase in aggregate demand is less than the multiplier calculation would predict in isolation.

The degree of crowding out is not fixed — it depends on two parameters. First, **how interest-sensitive is investment?** If businesses borrow heavily for investment and adjust plans readily when rates change, even a small rise in rates causes a large drop in private spending — strong crowding out. If investment plans are largely insensitive to borrowing costs (perhaps because investment is funded from retained earnings), crowding out is weak. Second, **what does monetary policy do?** If the central bank expands the money supply to offset the fiscal shock, keeping interest rates steady, crowding out is eliminated — the fiscal multiplier operates fully. This is why the debate about fiscal effectiveness is inseparable from the debate about monetary accommodation. In the extreme classical case, output is already at potential and savings are fixed, so every dollar of government spending mathematically displaces exactly one dollar of private spending — the multiplier is zero. In the Keynesian case with idle resources and monetary accommodation, the multiplier can operate at full strength. Real economies live between these poles, with the balance depending on monetary regime, business cycle position, and the structure of financial markets.
