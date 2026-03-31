---
id: search-and-matching-models
title: Search and Matching Models
domain: economics
course: labor-economics
prerequisites:
- id: labor-market-equilibrium
  type: hard
tags:
- search-theory
- matching-function
- Mortensen-Pissarides
- Beveridge-curve
- Nash-bargaining
stage: advanced
status: validated
---

# Search and Matching Models

## Core Idea
Search and matching models (Diamond, Mortensen, Pissarides — 2010 Nobel Prize) explain labor market dynamics by modeling the costly, time-consuming process of matching workers with jobs. Rather than assuming frictionless instantaneous matching, these models treat the labor market as a decentralized process where unemployed workers search for vacancies, firms post vacancies and screen applicants, and matches form through a stochastic matching function M(U, V). Once matched, wages are determined by Nash bargaining that splits the match surplus between worker and firm. The framework explains why unemployment and vacancies coexist (the Beveridge curve), how unemployment insurance affects job search and labor market outcomes, and why job creation and destruction drive business cycle dynamics.

## Questions

```yaml
- question: "The matching function M(U, V) in the Mortensen-Pissarides model takes as inputs..."
  type: multiple-choice
  options:
    - "Wages and productivity"
    - "The number of unemployed workers (U) and the number of job vacancies (V), producing the flow of new matches per unit of time"
    - "GDP and the interest rate"
    - "Worker education levels and firm sizes"
  answer: 1
  explanation: "The matching function is the core technology of search models — it determines how many new worker-firm matches form per period given the stocks of searching workers and open vacancies. It is typically assumed to be increasing in both arguments (more searchers or more vacancies produce more matches) with constant returns to scale. The ratio V/U (labor market tightness) is a key variable: when tightness is high (many vacancies per unemployed worker), workers find jobs quickly but firms take longer to fill positions."

- question: "In search and matching models, unemployment exists even when the number of vacancies equals the number of unemployed workers."
  type: true-false
  answer: true
  explanation: "This is a fundamental insight of search theory. Even when U = V, matching takes time due to information frictions, geographic mismatch, skill mismatch, and the stochastic nature of the search process. Not every worker-vacancy pair is a suitable match, and even suitable pairs take time to find each other. The matching function captures this: even with many searchers on both sides, the flow of new matches per period is finite. This 'frictional' unemployment exists at all points on the Beveridge curve and is a permanent feature of any labor market with search frictions."

- question: "How is the wage determined in the Mortensen-Pissarides model, and why does this differ from the competitive model?"
  type: short-answer
  answer: "Wages are determined by Nash bargaining between the matched worker and firm, splitting the match surplus (the value of the match above each party's outside option). The worker's outside option is the value of unemployment (search income, UI benefits, leisure); the firm's outside option is the value of an unfilled vacancy. The surplus is divided according to bargaining power parameters. This differs from the competitive model where the wage equals MRPL — in search models, bilateral monopoly after matching creates surplus to be divided, and the wage depends on bargaining power, outside options, and labor market tightness."
  explanation: "The Nash bargaining solution splits surplus proportionally to each party's bargaining power. When the labor market is tight (many vacancies, few unemployed), workers' outside options improve (they can find another match quickly if this one fails), shifting bargaining power toward workers and raising wages. When the market is slack, firms' outside options improve, reducing wages. This endogenous wage determination links wages to aggregate labor market conditions and creates a channel through which macroeconomic shocks transmit to wages and employment."
```

## Explainer

The Walrasian model of the labor market assumes that workers and firms find each other instantly, costlessly, and with perfect information. In this frictionless world, the market clears, unemployment is voluntary, and the only interesting question is the equilibrium wage. Search and matching models start from the recognition that this assumption is wildly unrealistic: finding a job takes months, filling a position takes weeks, and the process is fundamentally uncertain for both sides. This realism comes at the cost of mathematical complexity but produces a much richer set of predictions about unemployment dynamics, wage determination, and labor market policy.

The matching function is the central building block. It is the labor market analog of a production function: just as a factory combines capital and labor to produce output, the matching function combines unemployed workers and vacancies to produce new employment relationships. The standard specification M(U, V) = m * U^alpha * V^(1-alpha) has constant returns to scale, meaning that doubling both unemployed workers and vacancies doubles the flow of new matches. The key ratio theta = V/U (labor market tightness) determines how easy it is for each side to find a match: when theta is high (many vacancies per unemployed worker), workers find jobs quickly but firms struggle to fill positions.

Once a worker and firm are matched, they create a joint surplus — the value of the ongoing employment relationship exceeds the sum of their outside options (the worker's value of continued search plus the firm's value of an unfilled vacancy). This surplus must be divided, and Nash bargaining is the standard solution concept. The worker's share increases with their bargaining power (which may reflect union status, scarcity of skills, or legal protections) and with the tightness of the labor market (a tight market improves the worker's fallback by making it easier to find another job). This wage-setting mechanism creates a direct link between aggregate labor market conditions and individual wages.

The Beveridge curve — the negative relationship between the unemployment rate and the vacancy rate — is a natural implication of the model. When aggregate demand is strong, firms post many vacancies and unemployment is low (northeast of the curve). When demand is weak, vacancies are scarce and unemployment is high (southwest of the curve). Shifts of the Beveridge curve (outward shifts indicate worsened matching efficiency) can reflect structural changes: skill mismatch, geographic mismatch, or changes in search intensity. The movement along versus shifts of the Beveridge curve is central to distinguishing cyclical from structural unemployment.

The model's policy implications are substantial. Unemployment insurance (UI) raises the worker's outside option (the value of unemployment), reducing search intensity and increasing the reservation wage. This lengthens unemployment durations and raises equilibrium unemployment — the standard moral hazard concern. But UI also enables better matching by allowing workers to search longer and more selectively rather than accepting the first available job. The net welfare effect depends on the balance between these search-quality and moral hazard effects. Employment protection legislation (firing costs) reduces both job destruction (fewer layoffs) and job creation (firms are more cautious about hiring), with ambiguous net employment effects but clearer effects on labor market dynamics: lower flows in and out of employment.
