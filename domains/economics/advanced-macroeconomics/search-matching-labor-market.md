---
id: search-matching-labor-market
title: Search and Matching in the Labor Market
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: types-of-unemployment
  type: hard
- id: information-asymmetry
  type: soft
tags:
- unemployment
- job-search
- labor-market-frictions
- wage-setting
stage: expert
status: draft
---

# Search and Matching in the Labor Market

## Core Idea
Search and matching models treat unemployment as a frictional outcome of time required to find suitable job matches in decentralized labor markets. Firms and workers search separately; matching rates depend on labor market tightness (vacancy-to-unemployment ratio). Job creation and destruction rates jointly determine equilibrium unemployment, and wages result from bilateral bargaining. This framework explains persistent unemployment and frictional wage differentials and is now incorporated into most modern DSGE models.

## Questions

```yaml
- question: "In a search-matching model, labor market tightness rises sharply (many more vacancies relative to unemployed workers). What is the most likely effect on wages?"
  type: multiple-choice
  options:
    - "Wages rise because workers' outside option — continued searching — becomes more valuable"
    - "Wages fall because firms have more leverage when there are many open positions to fill"
    - "Wages are unaffected because wages are set by aggregate supply and demand, not individual bargaining"
    - "Wages fall because the higher matching rate reduces the time workers spend unemployed, lowering their bargaining claims"
  answer: 0
  explanation: "In Nash bargaining, both sides' outside options matter. When tightness is high, an unemployed worker quickly finds another offer — their outside option improves. This raises the worker's share of the match surplus and pushes wages up. The misconception is that more vacancies favor firms; in fact, tighter markets favor workers at the bargaining table."

- question: "An economy has many unfilled job vacancies and many unemployed workers simultaneously. In a search-matching framework, what best explains this coexistence?"
  type: multiple-choice
  options:
    - "The matching function produces new matches at a finite rate; finding a suitable partner takes time regardless of aggregate counts"
    - "Workers are being irrational by not accepting available jobs, causing artificial excess unemployment"
    - "Wages are set too high by regulation, preventing market clearing"
    - "The aggregate number of vacancies must be lower than the number of unemployed, so the premise is impossible in equilibrium"
  answer: 0
  explanation: "The central insight of search-matching theory is that decentralized labor markets require time to form matches even when both sides exist in abundance. The matching function M(u, v) produces matches as a flow, not instantaneously. Persistent simultaneous vacancies and unemployment are the normal frictional equilibrium outcome, not a sign of irrationality or policy failure."

- question: "In a search-matching model, wages are determined by the intersection of aggregate labor supply and demand curves."
  type: true-false
  answer: false
  explanation: "Wages in search-matching models are not determined by Walrasian market clearing. Instead, wages emerge from bilateral Nash bargaining within each individual match. The wage splits the match surplus — the value of production minus both parties' outside options — according to relative bargaining power. This is a fundamental departure from competitive equilibrium wage theory."

- question: "In search-matching equilibrium, a higher vacancy-to-unemployment ratio (labor market tightness) tends to increase wages by improving workers' outside options during bargaining."
  type: true-false
  answer: true
  explanation: "When tightness θ = v/u is high, an unemployed worker can expect to find another match quickly, raising the value of their outside option (continued search). This shifts the Nash bargaining solution in workers' favor, raising the equilibrium wage. Tightness therefore transmits aggregate labor market conditions into individual wage outcomes."

- question: "In the Diamond-Mortensen-Pissarides model, why can two identical workers doing identical jobs at different firms legitimately earn different wages?"
  type: short-answer
  answer: "Because wages are set by bilateral Nash bargaining within each match, not by a single market wage. If the matches were formed at different times or under different labor market conditions (different tightness), or if the matches involved different idiosyncratic match qualities, the surplus splits differently, yielding different wages even for identical workers."
  explanation: "The decentralized bilateral bargaining framework means there is no single 'market wage.' Each match produces its own negotiated wage based on the surplus available at that moment and the relative outside options. This is the mechanism behind frictional wage dispersion — a feature the model explains but competitive models cannot."
```

## Explainer

From your study of types of unemployment, you know that frictional unemployment exists because workers and jobs don't connect instantly. Search and matching theory takes this observation and builds a formal framework around it. The core insight is that finding a job is like finding a good apartment: even when plenty of vacancies exist, it takes time, effort, and luck to find the right match. This **search friction** is not a market failure to be eliminated — it is a structural feature of any decentralized labor market where workers and firms must find each other.

The workhorse of this literature is the **matching function**, typically written as M(u, v), where u is the number of unemployed workers searching and v is the number of vacant positions. Think of it like a production function, but instead of producing goods, it produces new employer-employee matches. The ratio v/u is called **labor market tightness** — when tightness is high (many vacancies relative to unemployed workers), firms struggle to fill positions quickly but workers find jobs easily. When tightness is low, the reverse holds. This single variable captures the state of the labor market from both sides.

Once a worker and firm meet, they face a bilateral bargaining problem because their match creates a **surplus** — the value of production minus each party's outside option. The standard approach uses **Nash bargaining**: the wage splits the surplus according to the relative bargaining power of workers and firms. This means wages are not simply set by supply and demand in a Walrasian sense; they emerge from negotiation within each match. A worker's outside option is the value of continued searching, and a firm's outside option is the value of continued recruiting, so both depend on overall labor market tightness. Tight labor markets raise workers' outside options and push wages up.

The model closes with a **job creation condition**: firms post vacancies as long as the expected cost of recruiting (which depends on how tight the market is) is less than the expected profit from a filled position. In equilibrium, labor market tightness adjusts until firms are indifferent about posting one more vacancy. This pins down the equilibrium unemployment rate, vacancy rate, and wage simultaneously. The framework explains why unemployment persists even in a healthy economy, why identical workers can earn different wages at different firms, and why labor market policies like unemployment insurance or hiring subsidies affect not just the level of unemployment but the entire wage-setting process. The Diamond-Mortensen-Pissarides model, which formalized these ideas, earned the 2010 Nobel Prize precisely because it provided a tractable equilibrium theory of unemployment that the classical Walrasian framework could not.
