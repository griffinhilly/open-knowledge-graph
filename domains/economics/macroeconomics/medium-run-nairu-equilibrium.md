---
id: medium-run-nairu-equilibrium
title: Medium-Run Equilibrium at the NAIRU
domain: economics
course: macroeconomics
prerequisites:
- id: short-run-sticky-price-equilibrium
  type: hard
- id: natural-rate-hypothesis
  type: hard
builds-toward:
- wage-price-dynamics-and-inflation
tags:
- nairu
- medium-run
- unemployment
- inflation-stability
stage: advanced
status: draft
---

# Medium-Run Equilibrium at the NAIRU

## Core Idea
The medium run (1–3 years) is when prices adjust but not all expectations do. Equilibrium is at the Non-Accelerating Inflation Rate of Unemployment (NAIRU), where inflation is stable. Deviations create wage and price pressures.

## How It's Best Learned
Show Phillips curve relating unemployment to inflation: below NAIRU, wage and price pressures build and raise inflation. Above NAIRU, disinflation occurs. NAIRU can be estimated from historical wage-price data.

## Common Misconceptions
- Assuming NAIRU is constant; estimates vary over time.
- Treating NAIRU as directly observable.
- Forgetting NAIRU is medium-run concept.

## Questions

```yaml
- question: "An economy has an unemployment rate of 3.5%, well below the estimated NAIRU of 5%. A policymaker argues: 'Employment is strong and inflation has been calm recently — there's nothing to worry about.' What does the NAIRU framework predict about this situation?"
  type: multiple-choice
  options:
    - "The policymaker is correct; low unemployment always indicates a healthy economy with stable inflation"
    - "Unemployment below NAIRU creates excess labor demand, raising wages faster than productivity and building inflationary pressure — even if inflation hasn't risen yet"
    - "The economy will automatically return to NAIRU without any inflationary effects since prices are sticky in the medium run"
    - "Below-NAIRU unemployment has no inflation implications unless it persists for more than five years"
  answer: 1
  explanation: "NAIRU is the unemployment rate at which inflation is stable. When unemployment falls below NAIRU, labor markets tighten, workers gain bargaining power, wages rise faster than productivity, and firms pass costs to prices — inflation accelerates. The policymaker's observation that 'inflation has been calm recently' reflects the lag in these dynamics, not their absence. The NAIRU framework predicts that sustained below-NAIRU unemployment will cause inflation to rise over the medium run, even if there is no immediate signal. The calm is temporary; the pressure is building."

- question: "In 1990, economists estimate the U.S. NAIRU at 6%. By 2019, U.S. unemployment falls to 3.5% with inflation remaining near 2%. What is the most appropriate interpretation within the NAIRU framework?"
  type: multiple-choice
  options:
    - "The 1990 estimate was correct, and the 2019 data proves the Phillips curve has broken down permanently"
    - "NAIRU shifted downward over the intervening decades due to structural changes in labor markets, such as improved job matching or changes in union density"
    - "The 2019 unemployment rate of 3.5% must actually be above NAIRU for inflation to remain stable"
    - "NAIRU estimates are arbitrary and should not be used for policy analysis"
  answer: 1
  explanation: "NAIRU is not a fixed constant — it changes over time as the structure of labor markets evolves. The late 2010s U.S. experience, where unemployment fell well below 1990s NAIRU estimates without triggering inflation, forced economists to revise NAIRU downward, attributing the change to factors like improved labor market matching (technology-enabled job search), demographic shifts, and reduced union bargaining power. The correct response is not to abandon the NAIRU concept but to update estimates. That NAIRU varies is one of the core complications in applying this framework to real policy."

- question: "At the NAIRU, inflation may be positive, zero, or negative — what defines NAIRU is that inflation is stable (neither rising nor falling), not that it equals zero."
  type: true-false
  answer: true
  explanation: "NAIRU stands for Non-Accelerating Inflation Rate of Unemployment — it is the rate at which inflation neither accelerates nor decelerates. An economy can be at NAIRU with 3% inflation, with 0% inflation, or even with mild deflation, as long as those rates are stable. The NAIRU equilibrium is about the dynamics of inflation change, not its level. Policymakers who think NAIRU implies zero inflation are misapplying the concept; the central bank's inflation target (often 2%) sets the level, while NAIRU determines the unemployment rate consistent with not drifting away from that target."

- question: "Because NAIRU represents a structural equilibrium of the labor market, policymakers can observe it directly by examining current unemployment and inflation statistics."
  type: true-false
  answer: false
  explanation: "NAIRU is not directly observable — it must be estimated from historical data, and these estimates carry substantial uncertainty. You cannot look at today's unemployment and inflation and simply read off the NAIRU; the relationship involves lags (inflation responds to unemployment gaps with a delay of months), measurement error, and structural changes that shift NAIRU over time. Economists use historical regressions, structural labor market models, and state-space filtering to estimate NAIRU, and the confidence intervals around these estimates are wide. The 1990s consensus estimate of ~6% for the U.S. was later shown to have been too high, illustrating how difficult real-time NAIRU estimation is."

- question: "Why does the NAIRU framework imply that sustaining unemployment below the NAIRU is not a free lunch — and what is the cost of attempting it?"
  type: short-answer
  answer: "When unemployment is held below NAIRU, tight labor markets generate wage growth exceeding productivity gains, which firms pass through as price increases. This accelerates inflation. Once inflation expectations rise and become embedded in wage bargaining — workers demand higher wages to keep pace with expected inflation — the short-run Phillips curve shifts upward. Bringing inflation back down then requires pushing unemployment above NAIRU (causing a recession) for long enough to reduce expectations and slow wage growth. The cost of the 'free lunch' is a more painful disinflation later: the temporary employment gain must be paid back with interest in the form of higher unemployment during the correction."
  explanation: "This dynamic played out in the U.S. in the 1970s, when policymakers repeatedly attempted to push unemployment below NAIRU; inflation ratcheted upward in each cycle. The Volcker disinflation of 1981–82 then required driving unemployment above 10% to break inflationary expectations. The NAIRU framework predicts exactly this asymmetry: deviations below NAIRU are pleasant short-term but costly to reverse, which is why central banks use NAIRU estimates as a guide for preemptive policy tightening rather than waiting for inflation to appear before responding."
```

## Explainer

Your prerequisites position you well for this concept. From short-run sticky-price equilibrium, you know that demand shocks can temporarily push unemployment below or above its natural rate while prices adjust slowly. From the natural rate hypothesis, you know that in the long run, the unemployment rate reverts to its structural level regardless of the inflation rate — money is neutral in the long run. The **NAIRU** (Non-Accelerating Inflation Rate of Unemployment) formalizes the medium-run version of this story: it is the unemployment rate consistent with *stable* inflation. Not zero inflation — just inflation that is neither rising nor falling.

The **Phillips curve** is the tool for understanding how the economy moves toward or away from NAIRU. The short-run Phillips curve shows a negative relationship between unemployment and inflation: when unemployment falls below NAIRU, tight labor markets give workers bargaining power, wages rise faster than productivity, firms pass costs onto prices, and inflation accelerates. When unemployment rises above NAIRU, the opposite occurs — wage growth moderates, price pressures ease, and inflation decelerates. NAIRU is the unemployment rate where these pressures exactly offset: workers' wage demands match the inflation rate firms expect, and actual inflation equals expected inflation. The economy is in a self-sustaining equilibrium.

The **medium run** — roughly 1 to 3 years — is the horizon over which this adjustment plays out. In the short run, firms have committed to prices and workers to wage contracts, so output and employment adjust to demand shocks while prices barely move (sticky prices). In the long run, all contracts adjust fully and money is neutral. The medium run is the interesting case: prices are adjusting, expectations are shifting, and the economy is en route from a short-run disequilibrium back toward NAIRU. Policy operates most powerfully in this window. A central bank that sees unemployment below NAIRU knows inflation is building and must decide whether to tighten now or wait; the cost of delay is that inflation expectations become embedded in wage-setting, shifting the Phillips curve upward and making disinflation more costly.

NAIRU is a theoretical concept, not a directly observable number. Economists estimate it from historical wage-price data, from structural models of labor market turnover, or by looking for the unemployment rate associated with stable inflation across different time periods. These estimates carry substantial uncertainty and change over time. The U.S. NAIRU was widely estimated near 6% in the 1990s; by the late 2010s, unemployment had fallen below 4% without triggering inflation, forcing estimates significantly lower. This variability is not an embarrassing admission of imprecision — it reflects genuine changes in labor market structure (union density, job matching technology, demographic composition) that shift the unemployment rate consistent with price stability. Treating NAIRU as a fixed constant is the single most common error in applying this framework to policy analysis.
