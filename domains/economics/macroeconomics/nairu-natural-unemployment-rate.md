---
id: nairu-natural-unemployment-rate
title: 'NAIRU: Non-Accelerating Inflation Rate of Unemployment'
domain: economics
course: macroeconomics
prerequisites:
- id: phillips-curve
  type: hard
- id: inflation-and-price-level
  type: hard
- id: natural-rate-hypothesis
  type: hard
- id: demand-shock-output-inflation-effects
  type: soft
- id: natural-rate-of-unemployment-nairu
  type: soft
- id: supply-shock-stagflation-effects
  type: soft
builds-toward:
- expectations-augmented-phillips-curve-modern
- wage-setting-equilibrium-unemployment
tags:
- unemployment
- inflation
- equilibrium
stage: expert
status: validated
---
# NAIRU: Non-Accelerating Inflation Rate of Unemployment

## Core Idea
The NAIRU is the unemployment rate consistent with stable inflation—below it, inflation accelerates; above it, inflation decelerates. It differs from the natural rate by accounting for institutional and frictional factors that prevent wages from adjusting instantly. The NAIRU is unobservable and must be estimated, making it a key parameter in monetary policy decisions.

## Questions

```yaml
- question: "The Federal Reserve raises interest rates when unemployment falls to 4.5%, believing the NAIRU is 5%. If the true NAIRU is actually 4%, what is the consequence of this policy?"
  type: multiple-choice
  options:
    - "Inflation accelerates, confirming the rate hike was necessary"
    - "The economy reaches full employment at a faster rate"
    - "Unnecessary unemployment is created — the rate hikes suppress demand below the true full-employment level"
    - "No consequence, since NAIRU estimates are always verified by inflation data within one quarter"
  answer: 2
  explanation: "If the true NAIRU is 4% but the Fed believes it's 5%, the Fed will tighten policy when unemployment is between 4% and 5% — a range that is actually compatible with stable inflation. These rate hikes raise borrowing costs, reduce investment and consumption, and create unemployment that would not have occurred had the Fed known the true NAIRU. This is the key policy risk: NAIRU misestimation has real output and employment costs, borne by workers who lose jobs due to unnecessarily tight policy."

- question: "In the late 1990s, the US unemployment rate fell well below prior NAIRU estimates without triggering inflation. Which explanation is most consistent with mainstream macroeconomic interpretation?"
  type: multiple-choice
  options:
    - "The Phillips curve broke down irreversibly in the 1990s and no longer applies"
    - "The NAIRU had declined — likely due to productivity gains and globalization — so prior estimates overstated the inflationary threshold"
    - "Inflation expectations became so well anchored that the NAIRU concept became irrelevant"
    - "Unemployment was being mismeasured, and actual unemployment never fell below the true NAIRU"
  answer: 1
  explanation: "The mainstream interpretation was that the NAIRU itself had shifted lower, not that the NAIRU concept had failed. Rising productivity meant firms could pay higher wages without raising prices (costs per unit fell). Globalization increased competition, holding down prices even as the labor market tightened. These factors shifted the inflation-unemployment tradeoff, meaning the economy could sustain lower unemployment without inflation accelerating. This episode is a key case study in why the NAIRU is time-varying and difficult to estimate in real time."

- question: "The NAIRU is a structural constant of an economy — difficult to measure precisely, but stable over time like a physical parameter."
  type: true-false
  answer: false
  explanation: "The NAIRU is explicitly time-varying and institution-dependent. It changes with unemployment insurance generosity, union bargaining power, minimum wage legislation, matching efficiency in labor markets, and structural shifts in the economy. The 1990s US experience — where the NAIRU appeared to fall from around 6% to below 5% — is a prominent example. Treating NAIRU as a fixed parameter leads to systematic policy errors when the true value drifts, as the Fed discovered."

- question: "The NAIRU cannot be directly measured — it must be inferred from the observed relationship between changes in unemployment and changes in inflation."
  type: true-false
  answer: true
  explanation: "Unlike the actual unemployment rate (measured from household surveys), the NAIRU is a theoretical construct defined by its effect on inflation dynamics. There is no direct instrument that measures it. Econometricians estimate it by fitting models of wage and price dynamics to historical data, looking for the unemployment level consistent with stable inflation. These estimates carry wide confidence intervals and are frequently revised as new data arrive — and are often revised substantially after the fact."

- question: "Why is uncertainty about the NAIRU especially problematic for monetary policy, and what was the reasoning behind the Federal Reserve's shift to average inflation targeting in 2020?"
  type: short-answer
  answer: "If the central bank acts as if the NAIRU is higher than it actually is, it will tighten policy prematurely, creating unnecessary unemployment. The error is asymmetric: moderately overshooting the true NAIRU (allowing unemployment to fall slightly below the true floor) causes only modest inflation, while undershooting (keeping unemployment above the true floor) creates persistently high unemployment with no offsetting benefit. Average inflation targeting acknowledges this asymmetry — rather than pre-emptively raising rates when unemployment approaches a potentially-wrong NAIRU estimate, the Fed commits to tolerating some overshoot and letting unemployment test its floor, accepting that a brief inflation overshoot is less costly than sustained unnecessary unemployment."
  explanation: "The 1990s and 2010s both featured NAIRU estimates that turned out to be too high, leaving unemployment higher than necessary. Average inflation targeting builds in tolerance for the downside case by requiring that past inflation shortfalls be made up, incentivizing the Fed to keep policy accommodative longer rather than tightening based on uncertain NAIRU estimates."
```

## Explainer

From the Phillips curve, you know the empirical relationship: lower unemployment tends to coincide with higher inflation. From the natural rate hypothesis, you know the theoretical reason: when unemployment falls below its natural level, workers gain bargaining power, wages rise faster than productivity, firms pass costs to consumers, and inflation accelerates. The **NAIRU** — Non-Accelerating Inflation Rate of Unemployment — is the unemployment rate at which these pressures exactly cancel out: inflation neither rises nor falls. It is the gravitational center of the labor market.

The distinction between NAIRU and the "natural rate" is subtle but important. The natural rate, as Friedman formulated it, is the equilibrium level set by real factors — the time it takes to find jobs (frictional unemployment), the mismatch between skills demanded and supplied (structural unemployment). The NAIRU is a related but more empirically operationalizable concept: it's defined by its inflation implications rather than by labor market structure. It explicitly incorporates **nominal rigidities** — the fact that wages and prices don't adjust instantly — and institutional factors like the generosity of unemployment insurance, the power of unions, and minimum wage laws. These factors shift the NAIRU without necessarily changing real equilibrium employment.

The central challenge is that the NAIRU is **unobservable**. You can measure actual unemployment; you cannot observe the rate at which inflation would stop accelerating. Economists estimate it — typically using statistical methods that smooth the unemployment series or use the historical relationship between unemployment gaps and inflation changes — but estimates come with substantial uncertainty. The Congressional Budget Office estimates the US NAIRU; the Federal Reserve has its own model-based estimates. Critically, these estimates change over time and are often revised after the fact. In the late 1990s, the US unemployment rate fell well below prior NAIRU estimates without triggering inflation, suggesting the NAIRU had shifted lower — probably due to productivity gains and globalization holding down prices.

This uncertainty has direct implications for monetary policy. A central bank that believes the NAIRU is 5% will raise interest rates when unemployment falls to 4.5%, fearing inflation acceleration. If the true NAIRU is actually 4%, those rate hikes create unnecessary unemployment. The Federal Reserve's 2020 shift to **average inflation targeting** reflected, in part, a recognition that the NAIRU is uncertain and that keeping unemployment low to test its floor has asymmetric benefits: the cost of briefly overshooting the NAIRU is modest inflation, while the cost of underestimating the NAIRU's decline is persistently high unemployment. Getting the NAIRU estimate right — or correctly quantifying one's uncertainty about it — is one of the most consequential empirical questions in applied macroeconomics.
