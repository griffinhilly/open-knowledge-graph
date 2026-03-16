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
stage: formal-systems
status: draft
---

# Search and Matching Models of Unemployment

## Core Idea
Search and matching models recognize that finding jobs and workers takes time. Workers search among job opportunities; firms search among worker applicants; matches occur only after search. This friction creates unemployment even when jobs exist and workers want to work. The model generates realistic unemployment dynamics: workers do not instantly find jobs, firms do not instantly fill vacancies, and job separation creates frictional unemployment. Matching functions describe how worker and firm searches translate into employment relationships.

## Explainer

From your study of the types of unemployment, you know that frictional unemployment exists because workers and jobs do not connect instantly. Search and matching models formalize this intuition by treating the labor market not as a frictionless auction but as a process where workers and firms must spend time and resources finding each other. The central insight is that unemployment and vacancies coexist — there are open jobs and jobless workers simultaneously — because the matching process is slow, costly, and uncertain.

The workhorse of the framework is the **matching function**, typically written as M(u, v), where u is the number of unemployed workers searching and v is the number of vacant positions. This function, analogous to a production function, converts search inputs into new employment relationships. A common specification is the Cobb-Douglas form M = Au^α v^(1−α), which captures two key properties: more searchers on either side of the market produce more matches, but with diminishing returns. The ratio θ = v/u, called **labor market tightness**, summarizes how easy it is for workers to find jobs versus how easy it is for firms to fill vacancies. When θ is high (many vacancies relative to unemployed workers), workers find jobs quickly but firms struggle to hire.

Building on your knowledge of dynamic optimization, these models set up the problem in continuous time with forward-looking agents. Workers compare the value of being employed (earning a wage minus the risk of job destruction) against the value of being unemployed (receiving unemployment benefits plus the option value of future job offers). Firms compare the value of a filled position (profit from the match minus wages) against the cost of posting a vacancy. The **Beveridge curve** — the empirical negative relationship between unemployment and vacancies — emerges naturally: when the economy is strong, vacancies are plentiful and unemployment is low, and vice versa. Shifts in the Beveridge curve signal changes in matching efficiency itself, such as skills mismatches or geographic barriers.

Once a worker and firm meet, they must agree on a wage. The standard approach uses **Nash bargaining**: the surplus from the match (the combined gain to both parties from forming the employment relationship rather than continuing to search) is split according to bargaining power. This means wages depend not just on productivity but on labor market conditions — when tightness is high, workers have more bargaining power because their outside option (finding another job) is better. The model thus generates endogenous wages, unemployment, and vacancies simultaneously, providing a unified framework for analyzing policies like unemployment insurance, hiring subsidies, and firing costs through their effects on search incentives and matching efficiency.
