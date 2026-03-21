---
id: search-matching-unemployment
title: Search and Matching Models of Unemployment
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: types-of-unemployment
  type: hard
- id: dynamic-optimization-macroeconomics
  type: hard
builds-toward:
- wage-dynamics-labor-frictions
tags:
- unemployment
- search
- matching
stage: advanced
status: draft
---

# Search and Matching Models of Unemployment

## Core Idea
Search and matching models recognize that finding jobs and workers takes time. Workers search among job opportunities; firms search among worker applicants; matches occur only after search. This friction creates unemployment even when jobs exist and workers want to work. The model generates realistic unemployment dynamics: workers do not instantly find jobs, firms do not instantly fill vacancies, and job separation creates frictional unemployment. Matching functions describe how worker and firm searches translate into employment relationships.

## Questions

```yaml
- question: "In a search and matching model, if the government raises unemployment insurance benefits substantially, what is the primary predicted effect on unemployment?"
  type: multiple-choice
  options:
    - "Unemployment falls because workers have more resources to conduct a thorough job search"
    - "Unemployment is unchanged because benefits only redistribute income without affecting search behavior"
    - "Unemployment rises because workers with better outside options search longer before accepting a match"
    - "Unemployment falls because firms post more vacancies when they know workers are financially supported"
  answer: 2
  explanation: "In search and matching theory, the value of being unemployed depends on income flows while searching. Higher benefits raise the value of unemployment, improving workers' outside option in Nash bargaining and making them more selective — they hold out longer before accepting a match. This reduces the flow of workers into employment, raising steady-state unemployment. This is a structural prediction of the model about how search incentives respond to the outside option, not simply moral hazard. Option A ignores the effect on acceptance thresholds; option D misidentifies which side of the market is affected."

- question: "An economy experiences the Beveridge curve shifting outward (farther from the origin). Compared to a movement along the Beveridge curve, what does this shift indicate?"
  type: multiple-choice
  options:
    - "A cyclical downturn where fewer firms are posting vacancies"
    - "A reduction in matching efficiency — the same levels of unemployment and vacancies are producing fewer new employment relationships"
    - "An increase in labor market tightness, signaling a strong labor market"
    - "More workers entering the labor force, which moves the curve by changing the unemployment rate"
  answer: 1
  explanation: "The Beveridge curve traces the cyclical relationship between unemployment and vacancies — movements along it reflect business cycle fluctuations. An outward shift means higher unemployment at any given vacancy rate, indicating structural deterioration: the matching function itself has become less efficient. This arises from skills mismatches (vacancies require skills the unemployed don't have), geographic barriers, or information frictions. The 2009–2012 US period showed a notable Beveridge curve outward shift, suggesting structural as well as cyclical unemployment."

- question: "In the search and matching framework, it is possible for an economy to simultaneously have many unemployed workers actively searching and many unfilled job vacancies — this coexistence is a feature, not a contradiction."
  type: true-false
  answer: true
  explanation: "This coexistence is the defining feature of frictional unemployment in search models. Workers and vacancies exist on two sides of a matching market but do not instantly find each other — search takes time, and not every pairing produces an acceptable match. The matching function M(u, v) converts search activity into new employment relationships, but with diminishing returns. The simultaneous presence of unemployment and vacancies is the empirical regularity (the Beveridge curve) that motivates the search framework, and it persists even in steady state."

- question: "In the search and matching model, wages are set by competitive market clearing: the market wage adjusts until labor supply equals labor demand, just as in a frictionless Walrasian market."
  type: true-false
  answer: false
  explanation: "This is the key departure from the Walrasian framework. In search and matching models, there is no centralized auction where prices clear the market, because workers and firms must search to find each other. Wages are instead determined by Nash bargaining between a matched worker-firm pair over the surplus from their match — the joint gain from forming the employment relationship rather than continuing to search. The wage depends on the worker's outside option (which improves when labor market tightness is high) and the firm's outside option, making wages endogenously dependent on market conditions."

- question: "Why do unemployment and vacancies coexist in the search and matching model, and what is the economic significance of the labor market tightness ratio θ = v/u?"
  type: short-answer
  answer: "Unemployment and vacancies coexist because matching is costly and time-consuming — workers search among job opportunities and firms search among applicants, and matches occur only after search succeeds. This friction means there is always a stock of searching workers (unemployment) and unfilled positions (vacancies) simultaneously, even in steady state. The tightness ratio θ = v/u captures the relative scarcity of workers versus jobs: high θ means vacancies outnumber unemployed, so workers find jobs quickly but firms fill vacancies slowly; low θ means the reverse. Because θ determines job-finding and vacancy-filling rates, it governs the value of searching for both parties and therefore endogenously determines wages through Nash bargaining."
  explanation: "The tightness ratio θ is the sufficient statistic for the state of the labor market in the model. It determines how long it takes both sides to find a match, and through this, it determines the value of being employed versus unemployed for workers and the profitability of posting a vacancy for firms. Policy interventions — unemployment insurance, hiring subsidies, firing costs — all work by changing search incentives or value functions in ways that shift equilibrium tightness. This is why search models are the standard tool for evaluating labor market policies."
```

## Explainer

From your study of the types of unemployment, you know that frictional unemployment exists because workers and jobs do not connect instantly. Search and matching models formalize this intuition by treating the labor market not as a frictionless auction but as a process where workers and firms must spend time and resources finding each other. The central insight is that unemployment and vacancies coexist — there are open jobs and jobless workers simultaneously — because the matching process is slow, costly, and uncertain.

The workhorse of the framework is the **matching function**, typically written as M(u, v), where u is the number of unemployed workers searching and v is the number of vacant positions. This function, analogous to a production function, converts search inputs into new employment relationships. A common specification is the Cobb-Douglas form M = Au^α v^(1−α), which captures two key properties: more searchers on either side of the market produce more matches, but with diminishing returns. The ratio θ = v/u, called **labor market tightness**, summarizes how easy it is for workers to find jobs versus how easy it is for firms to fill vacancies. When θ is high (many vacancies relative to unemployed workers), workers find jobs quickly but firms struggle to hire.

Building on your knowledge of dynamic optimization, these models set up the problem in continuous time with forward-looking agents. Workers compare the value of being employed (earning a wage minus the risk of job destruction) against the value of being unemployed (receiving unemployment benefits plus the option value of future job offers). Firms compare the value of a filled position (profit from the match minus wages) against the cost of posting a vacancy. The **Beveridge curve** — the empirical negative relationship between unemployment and vacancies — emerges naturally: when the economy is strong, vacancies are plentiful and unemployment is low, and vice versa. Shifts in the Beveridge curve signal changes in matching efficiency itself, such as skills mismatches or geographic barriers.

Once a worker and firm meet, they must agree on a wage. The standard approach uses **Nash bargaining**: the surplus from the match (the combined gain to both parties from forming the employment relationship rather than continuing to search) is split according to bargaining power. This means wages depend not just on productivity but on labor market conditions — when tightness is high, workers have more bargaining power because their outside option (finding another job) is better. The model thus generates endogenous wages, unemployment, and vacancies simultaneously, providing a unified framework for analyzing policies like unemployment insurance, hiring subsidies, and firing costs through their effects on search incentives and matching efficiency.
