---
id: time-inconsistency-monetary-policy
title: Time Inconsistency in Monetary Policy
domain: economics
course: macroeconomics
prerequisites:
- id: rational-expectations-macro
  type: hard
builds-toward:
- central-bank-credibility-expectations
tags:
- time-inconsistency
- inflation-bias
- credibility
- policy
stage: advanced
status: draft
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

## Explainer

You already know from rational expectations that people form beliefs about policy systematically and don't make predictable mistakes. Time inconsistency builds directly on this: it explains why a central bank that *wants* low inflation might still produce too much of it — not because policymakers are incompetent, but because of the strategic environment they're trapped in.

Start with the incentive structure. Suppose wage contracts are signed based on an expected inflation rate of 2%, and the central bank has announced a 2% target. Now, once those wages are locked in, the bank has a temptation: if it creates surprise inflation — say, 4% — real wages fall, employment rises, and output expands in the short run. The bank gets the output gain "for free" because the inflation wasn't expected. This is the **inflation surprise gain**, and it's the source of the whole problem. The bank's announced policy (2%) and its preferred action once wages are set (4%) are different. That divergence is **time inconsistency**: the policy that is optimal to *announce* is not the policy that is optimal to *execute* after others have committed to their plans.

Rational agents see through this immediately. Because workers and firms know the bank has the temptation to inflate, they refuse to set wages at 2%. They anticipate the bank will deviate, so they build in 4% (or whatever the bank's temptation level is). Now the bank faces a grim arithmetic: if it delivers 4% as expected, there is no surprise and no output gain — just higher inflation. If it instead delivers 2%, it surprises markets the other way, causing a contraction. The Nash equilibrium of this game is an **inflation bias**: stable, elevated inflation with no output benefit. The rational-expectations machinery you studied delivers this result with unusual clarity — precisely because agents don't get fooled on average, the government can't exploit the money illusion indefinitely.

The solutions all amount to changing the game, not just the players. **Central bank independence** removes the elected government's ability to instruct the bank to inflate before elections, reducing the short-run output temptation. **Inflation targeting** — combined with transparency about the target — allows the public to observe when the bank deviates, making cheating costly to its reputation. **Conservative central bankers** (the Rogoff solution) appoints decision-makers who dislike inflation more than the median voter, shifting the bank's objective away from the temptation. What these solutions share is that they make the low-inflation commitment *credible* rather than merely announced. The problem doesn't disappear because someone says "I promise." It diminishes when the institutional structure makes deviation costly — and when a track record of non-deviation has been built up over time.


