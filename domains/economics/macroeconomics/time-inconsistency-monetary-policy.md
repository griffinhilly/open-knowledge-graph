---
id: time-inconsistency-monetary-policy
title: Time Inconsistency in Monetary Policy
domain: economics
course: macroeconomics
prerequisites:
- id: rational-expectations-macro
  type: hard
- id: exchange-rate-regimes-and-monetary-policy
  type: soft
- id: stagflation-and-conflicting-policy
  type: soft
builds-toward:
- central-bank-credibility-expectations
tags:
- time-inconsistency
- inflation-bias
- credibility
- policy
stage: expert
status: validated
---
# Time Inconsistency in Monetary Policy

## Core Idea
Time inconsistency arises because central banks have incentive to create surprise inflation (boosting short-run output) even though everyone knows this. Rational agents anticipate this, embedding higher inflation into expectations, leaving higher inflation but no output gain (inflation bias). Solutions include independence and inflation targeting.

## How It's Best Learned
Use game-theoretic example: central bank announces 2% target. If public believes it, wage-setters expect 2%, and bank can create surprise inflation. But rational agents anticipate, embed higher inflation into expectations. Bank must choose between accepting higher inflation or tight policy.

## Common Misconceptions
- Assuming time inconsistency implies always high inflation.
- Treating independence as sufficient solution.
- Forgetting problem diminishes when inflation stable and credible.

## Questions

```yaml
- question: "A central bank announces a 2% inflation target. Wage contracts are signed based on 2% expected inflation. The bank now faces a choice: deliver 2% as promised, or deviate to 4% to gain a short-run output boost. If wage-setters are rational and understand the bank's incentives, what is the equilibrium outcome?"
  type: multiple-choice
  options:
    - "2% inflation, as rational agents trust the announced commitment and the bank delivers on it"
    - "4% inflation with a short-run output gain, as the bank exploits the surprise to boost employment"
    - "Higher inflation with no output gain, as rational agents anticipate the deviation and set wages accordingly"
    - "Deflation, as the bank overcorrects to re-establish credibility after missing its target"
  answer: 2
  explanation: "This is the inflation bias result. Rational wage-setters anticipate that the bank has an incentive to deviate, so they refuse to set wages at 2% — they embed the bank's temptation level (4% or whatever it is) into their expectations. The bank then faces a grim choice: deliver 4% as expected (no surprise, no output gain) or deliver 2% and cause a contraction. The Nash equilibrium is elevated, stable inflation with no output benefit — the worst of both worlds. The key is that rational expectations neutralize the policy temptation."

- question: "Which of the following institutional arrangements best addresses the root cause of time inconsistency in monetary policy?"
  type: multiple-choice
  options:
    - "Requiring the central bank governor to publicly pledge low inflation at each meeting, creating reputational accountability"
    - "Giving the central bank legal independence from the government and a clear inflation target, making deviation costly and observable"
    - "Requiring unanimous board votes before any rate change, slowing the bank's ability to create surprise inflation"
    - "Publishing detailed meeting minutes so the public can monitor the bank's reasoning, reducing information asymmetry"
  answer: 1
  explanation: "Time inconsistency is a structural problem: the bank's optimal policy after others have committed differs from what it would optimally announce. Promises and transparency (options A and D) help at the margin but don't change the underlying incentive structure. Independence combined with a transparent target changes the game: deviation becomes publicly observable and costly to the bank's institutional reputation and mandate. This is the Kydland-Prescott / Barro-Gordon insight — solutions must alter incentives, not just intentions."

- question: "In the time-inconsistency equilibrium, rational agents end up with higher inflation but no better employment outcomes than if the central bank had simply committed credibly to its announced low-inflation target."
  type: true-false
  answer: true
  explanation: "This is the inflation bias result. Because rational agents anticipate the bank's temptation, they set wages and prices at the higher expected inflation level. When the bank delivers that higher inflation, there is no element of surprise, so there is no real wage reduction, no employment boost — just higher inflation than society actually wants. If the bank could credibly commit to 2%, agents would set wages at 2%, and the bank would deliver 2% — everyone is better off. The equilibrium inflation is a pure loss from the inability to commit."

- question: "Time inconsistency in monetary policy can be fully resolved if central bank governors publicly promise to maintain low inflation and are credible, charismatic communicators."
  type: true-false
  answer: false
  explanation: "This misses the structural nature of the problem. Time inconsistency is not a failure of communication or sincerity — it is a strategic trap. Even a governor who genuinely wants low inflation faces the temptation to deviate once wages are set, and rational agents know this. Promises are cheap: what matters is whether deviation is costly. Only institutional changes (independence, inflation targeting with accountability, conservative central bankers whose preferences genuinely differ) alter the incentive structure. Credibility is earned through demonstrated commitment backed by institutions, not through rhetoric."

- question: "Explain why a central bank that genuinely wants low inflation might still produce an inflation bias, even if all actors are fully rational."
  type: short-answer
  answer: "The problem is dynamic inconsistency between what the bank wants to announce and what it wants to do once others have committed. Once wage contracts are signed based on a low-inflation announcement, the bank faces a temptation: creating surprise inflation reduces real wages, boosts employment, and raises output in the short run — benefits the bank values. Rational agents foresee this temptation and refuse to believe the announcement, instead setting wages at the higher level the bank will actually deliver. The bank cannot credibly commit to low inflation without institutional constraints that make deviation costly, so the equilibrium is elevated inflation with no output gain."
  explanation: "The key insight is that the bank's optimal policy changes depending on whether others have already committed. Before wages are set, the bank prefers to announce 2% (signaling low inflation expectations) and deliver 2%. After wages are set at 2%, the bank prefers to deliver 4% (exploiting the temporary real wage reduction). Rational agents solve this game and embed the higher expected inflation into their contracts, producing inflation bias as the only time-consistent equilibrium."
```

## Explainer

You already know from rational expectations that people form beliefs about policy systematically and don't make predictable mistakes. Time inconsistency builds directly on this: it explains why a central bank that *wants* low inflation might still produce too much of it — not because policymakers are incompetent, but because of the strategic environment they're trapped in.

Start with the incentive structure. Suppose wage contracts are signed based on an expected inflation rate of 2%, and the central bank has announced a 2% target. Now, once those wages are locked in, the bank has a temptation: if it creates surprise inflation — say, 4% — real wages fall, employment rises, and output expands in the short run. The bank gets the output gain "for free" because the inflation wasn't expected. This is the **inflation surprise gain**, and it's the source of the whole problem. The bank's announced policy (2%) and its preferred action once wages are set (4%) are different. That divergence is **time inconsistency**: the policy that is optimal to *announce* is not the policy that is optimal to *execute* after others have committed to their plans.

Rational agents see through this immediately. Because workers and firms know the bank has the temptation to inflate, they refuse to set wages at 2%. They anticipate the bank will deviate, so they build in 4% (or whatever the bank's temptation level is). Now the bank faces a grim arithmetic: if it delivers 4% as expected, there is no surprise and no output gain — just higher inflation. If it instead delivers 2%, it surprises markets the other way, causing a contraction. The Nash equilibrium of this game is an **inflation bias**: stable, elevated inflation with no output benefit. The rational-expectations machinery you studied delivers this result with unusual clarity — precisely because agents don't get fooled on average, the government can't exploit the money illusion indefinitely.

The solutions all amount to changing the game, not just the players. **Central bank independence** removes the elected government's ability to instruct the bank to inflate before elections, reducing the short-run output temptation. **Inflation targeting** — combined with transparency about the target — allows the public to observe when the bank deviates, making cheating costly to its reputation. **Conservative central bankers** (the Rogoff solution) appoints decision-makers who dislike inflation more than the median voter, shifting the bank's objective away from the temptation. What these solutions share is that they make the low-inflation commitment *credible* rather than merely announced. The problem doesn't disappear because someone says "I promise." It diminishes when the institutional structure makes deviation costly — and when a track record of non-deviation has been built up over time.


