---
id: wage-dynamics-labor-frictions
title: Wage Dynamics and Labor Market Frictions
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: search-matching-unemployment
  type: hard
tags:
- wages
- labor-frictions
- unemployment
stage: advanced
status: draft
---

# Wage Dynamics and Labor Market Frictions

## Core Idea
In models with search and matching, wages result from bilateral bargaining between employers and employees. Because workers and firms earn rents from the match (the surplus from employment relative to remaining unemployed or unfilled), there is room for negotiation. Wage dynamics reflect movements in unemployment, worker and firm outside options, and the value of the match. This framework explains why wages are sticky downward and respond sluggishly to labor market conditions, contributing to unemployment persistence.

## Questions

```yaml
- question: "During a severe recession, unemployment rises from 5% to 12%, yet wages fall by only 1–2%. A classical economist argues workers are simply refusing to accept market-clearing wages. How does the search-and-matching framework better explain this pattern?"
  type: multiple-choice
  options:
    - "Workers have strong unions that contractually prevent nominal wage cuts regardless of market conditions"
    - "The match surplus remains positive even in downturns, so both workers and firms prefer sticky wages to destroying the match and incurring future search and hiring costs"
    - "Minimum wage laws create a binding floor that prevents wages from falling to market-clearing levels"
    - "Firms raise efficiency wages to preserve morale, fully offsetting any downward pressure from unemployment"
  answer: 1
  explanation: "In search-and-matching models, once a worker-firm pair is matched, their relationship generates a surplus above what either could get by returning to search. Even in a recession, this match surplus typically remains positive — both sides still prefer the existing arrangement to the costly alternative of separating and searching again. The wage is determined by Nash bargaining over this surplus, not by a spot labor market clearing. As a result, wages are sticky: they respond sluggishly to aggregate conditions because the relevant margin is the value of the ongoing match, not the current market wage for new hires."

- question: "In a Nash bargaining wage model, a worker's 'outside option' refers to:"
  type: multiple-choice
  options:
    - "The highest wage currently offered by a competing employer actively recruiting the worker"
    - "The worker's legal right to strike and withhold labor during negotiations"
    - "The value of being unemployed — unemployment benefits, the value of leisure, and the expected gains from continuing to search for a new match"
    - "The minimum wage floor set by government regulation"
  answer: 2
  explanation: "In the Nash bargaining framework, the outside option is what each party gets if negotiations break down and the match is dissolved. For the worker, this is the value of unemployment: benefits received while unemployed, the value of leisure, and the discounted expected value of eventually finding a new job through search. This outside option sets a floor on the wage — the worker would reject any offer below it. When unemployment is high, this outside option deteriorates (new jobs are scarcer), which theoretically pushes wages down, but other frictions prevent large adjustments."

- question: "In a frictionless competitive labor market, wages are determined by supply and demand; in a search-and-matching model, wages are instead determined by bilateral bargaining over the rents from a successful match."
  type: true-false
  answer: true
  explanation: "This contrast is the central insight of search-and-matching theory. In a frictionless market, the wage is the market-clearing price — no individual worker or firm has bargaining power. In a world with search frictions, finding a match takes time and resources, so a matched pair earns rents above their respective outside options. These rents create room for negotiation, and the Nash bargaining solution splits them according to relative bargaining power. The wage is therefore not a market price but the outcome of bilateral negotiation, which is why it behaves differently — especially in response to aggregate shocks."

- question: "On-the-job search, where employed workers continue looking for better matches while working, tends to compress the wage distribution over time as all workers converge to the same wage."
  type: true-false
  answer: false
  explanation: "On-the-job search actually generates a wage *ladder* — a distribution of wages rather than convergence. Workers accept low-paying jobs as stepping stones and use on-the-job search to receive outside offers that trigger renegotiation or job switching to higher-paying positions. Recessions damage this ladder by reducing the arrival rate of outside offers, slowing wage growth and trapping workers in lower-paying jobs longer. The resulting wage distribution is dispersed, not compressed, and the dynamics of climbing and falling along this ladder connect to macroeconomic phenomena like earnings inequality and post-recession wage scarring."

- question: "Why does the search-and-matching framework predict that employment adjustments (hiring and firing rates) respond faster to a recession than wage adjustments do?"
  type: short-answer
  answer: "Wages are determined by bargaining over the match surplus — the value of the ongoing relationship relative to both parties' outside options. Even as unemployment rises in a recession and workers' outside options deteriorate, the existing match still generates positive surplus for both sides. The wage is constrained by the worker's bargaining power parameter and by unemployment benefits that put a floor on the outside option. Destroying the match to rehire at a lower wage forces both parties to incur future search and recruiting costs, which may exceed the gains from a lower wage. Firms therefore prefer to maintain wages while adjusting through quantities — slowing hiring, cutting hours, or laying off marginal workers — producing the observed pattern where employment responds faster than wages to aggregate shocks."
  explanation: "This mechanism also explains why unemployment is persistent after recessions: wages don't fall enough to clear the market quickly, so unemployment works off gradually through the slow process of firms opening new vacancies and workers searching for matches. The Beveridge curve — the empirical inverse relationship between vacancies and unemployment — traces out the adjustment path as the economy moves between tight and slack labor market conditions."
```

## Explainer

In a frictionless labor market, wages adjust instantly to clear supply and demand — anyone willing to work at the going rate finds a job immediately. But real labor markets look nothing like this. It takes time and resources for workers to find jobs and for firms to fill vacancies. From your study of search and matching models, you know that this friction creates a **match surplus**: once a worker and firm find each other, the value of their relationship exceeds what either could get by returning to the search pool. The question of wage dynamics is essentially the question of how this surplus gets divided.

The standard approach is **Nash bargaining**, where the wage splits the match surplus according to the relative bargaining power of each side. The worker's outside option is the value of being unemployed — collecting unemployment benefits, enjoying leisure, and continuing to search. The firm's outside option is the value of an unfilled vacancy — paying recruiting costs while waiting for another applicant. The wage lands somewhere between these outside options, weighted by a bargaining power parameter. When the labor market tightens (low unemployment, many vacancies), workers' outside options improve because they can find alternative jobs more easily, and wages rise. When the market slackens, firms gain leverage and wages fall — but often slowly.

This framework explains a key empirical puzzle: **wage stickiness**. In a deep recession, unemployment spikes but wages barely fall. The search-and-matching model explains why. Even as unemployment rises and workers' outside options deteriorate, the wage is pinned partly by the worker's bargaining power parameter, by unemployment benefits that put a floor on the outside option, and by the fact that existing matches still generate positive surplus. Firms would rather keep workers at somewhat-above-market wages than destroy the match and incur future hiring costs. The result is that wages respond sluggishly to aggregate conditions, and unemployment adjustments happen primarily through quantities (hiring and firing rates) rather than prices.

The dynamics become richer when you allow for **on-the-job search**, where employed workers can look for better matches while working. This creates wage ladders: workers gradually move up to higher-paying jobs over time, and a recession destroys this job ladder by reducing the arrival rate of outside offers. Wage dynamics then reflect not just current bargaining but the entire distribution of match qualities and the rate at which workers climb or fall along the wage distribution. These models connect the microeconomic bargaining problem to macroeconomic phenomena like the Beveridge curve (the inverse relationship between vacancies and unemployment) and the persistence of unemployment after recessions.
