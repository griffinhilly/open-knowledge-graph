---
id: wage-setting-equilibrium
title: Wage-Setting Equilibrium and Wage Bargaining
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: search-matching-unemployment
  type: hard
builds-toward:
- inflation-unemployment-tradeoff
tags:
- wage-setting
- bargaining
- wage-determination
stage: advanced
status: draft
---

# Wage-Setting Equilibrium and Wage Bargaining

## Core Idea
In search-and-matching models, wages emerge from bilateral bargaining over the surplus from a job match. The wage is a weighted average of the worker's reservation value and the firm's productivity minus its hiring cost. Tighter labor markets (higher vacancy-unemployment ratio) increase workers' bargaining power and equilibrium wages.

## Questions

```yaml
- question: "An economy experiences a surge in job vacancies while the number of unemployed workers stays constant, raising labor market tightness (v/u). According to the wage-setting model, what happens to the equilibrium wage and why?"
  type: multiple-choice
  options:
    - "The wage rises, because workers find new jobs faster (higher outside option) and firms fill vacancies slower (lower outside option) — both effects push wages up."
    - "The wage falls, because more vacancies mean firms are desperate to hire and will accept lower-wage workers."
    - "The wage is unchanged, because the Nash bargaining power β is a fixed parameter that doesn't depend on market conditions."
    - "The wage rises only if workers have bargaining power β > 0.5; otherwise firms capture the extra surplus."
  answer: 0
  explanation: "Tighter labor markets work on both sides of the table simultaneously. Workers' outside option improves (they find jobs faster), and firms' outside option worsens (they wait longer to fill a vacancy). Both effects increase the negotiated wage. This is the key insight of the wage-setting curve: tightness translates directly into wage pressure, regardless of the fixed bargaining power parameter."

- question: "In Nash bargaining, the worker's bargaining power β approaches 1. What does the equilibrium wage approach?"
  type: multiple-choice
  options:
    - "The worker's reservation value (unemployment benefit plus value of job search)."
    - "The firm's productivity minus its vacancy-posting cost — essentially the maximum the firm can pay."
    - "The average of worker reservation value and firm productivity, unaffected by β."
    - "Zero, because a worker with all the power captures the entire surplus, leaving nothing for a wage."
  answer: 1
  explanation: "The Nash wage is: w = reservation value + β × (total surplus). As β → 1, the worker captures the entire surplus, so the wage approaches the firm's maximum willingness to pay: productivity minus hiring costs. When β → 0, the wage collapses to the reservation value. This is the surplus-splitting logic at the heart of the model."

- question: "An increase in unemployment benefits raises the equilibrium wage even if the worker's bargaining power β is unchanged."
  type: true-false
  answer: true
  explanation: "Higher unemployment benefits raise the worker's outside option (the value of staying unemployed and searching). In the Nash wage formula, the wage equals the reservation value plus β times the surplus. A higher reservation value directly raises the wage, even with the same β. This is why policies affecting the outside option of workers — benefits, minimum wages, housing mobility — have wage effects in search-and-matching models."

- question: "In the wage-setting model, higher labor market tightness lowers the equilibrium wage because firms can fill vacancies more easily."
  type: true-false
  answer: false
  explanation: "This reverses the direction. Higher tightness means MORE vacancies relative to unemployed workers, so firms find it HARDER to fill positions — their outside option worsens. At the same time, workers find jobs faster — their outside option improves. Both effects push wages UP, not down. The wage-setting curve has a positive slope in tightness."

- question: "Why does a rise in labor market tightness (v/u) push wages up from both sides of the bargaining table simultaneously? Explain using the concept of outside options."
  type: short-answer
  answer: "Higher tightness means more vacancies per unemployed worker. For workers, this shortens expected unemployment duration — their outside option (the value of continued search) improves. For firms, more vacancies per applicant means longer expected vacancy duration — their outside option (waiting for another candidate) worsens. Since both sides' threat points move in the same direction, the negotiated wage rises. Neither side alone drives the increase; it is a simultaneous tightening of constraints from both parties."
  explanation: "The key is that tightness is a market-wide variable affecting both sides' fallback positions at once. This is why search-and-matching models generate a wage-setting curve with a positive slope — not because bargaining power changes, but because the outside options that anchor the bargaining range shift together."
```

## Explainer

In search-and-matching models, a job match generates a **surplus** — the difference between the value of a filled position and what both parties would get if they walked away. The worker's outside option is continued unemployment (collecting benefits, searching for another job). The firm's outside option is an unfilled vacancy (paying posting costs, waiting for another applicant). The wage must fall somewhere between these two outside options, because both sides prefer a deal to no deal. The question is where exactly in that range the wage lands.

The standard approach uses **Nash bargaining**, which you can think of as splitting a pie. The worker and firm each have a bargaining power parameter — typically denoted β for the worker and (1 − β) for the firm — that determines their share of the match surplus. The resulting wage equation takes the form: wage equals the worker's reservation value plus β times the total surplus. Equivalently, the wage is a weighted average of what the worker could get elsewhere and what the firm can afford to pay. When β is high, workers capture most of the surplus and wages are closer to productivity; when β is low, firms capture most of it and wages hover near the reservation value.

What makes this more than a static bargaining problem is the feedback through **labor market tightness** — the ratio of vacancies to unemployed workers (v/u). When the market is tight (many vacancies relative to job seekers), unemployed workers find jobs quickly, which raises their outside option. A worker who can credibly walk away and find another match soon has more leverage. Simultaneously, firms find it harder to fill vacancies in a tight market, which lowers their outside option. Both effects push the negotiated wage upward. The **wage-setting curve** plots this positive relationship: as tightness rises, equilibrium wages rise.

The wage-setting equilibrium emerges where the wage-setting curve intersects the **job-creation condition** — the requirement that firms find it profitable to post vacancies. Higher wages reduce the profitability of vacancies, so fewer are posted, which reduces tightness. The intersection pins down both the equilibrium wage and the equilibrium level of labor market tightness, and from tightness you can derive the equilibrium unemployment rate. This is why policy changes — like higher unemployment benefits raising the worker's reservation value, or productivity shocks shifting what firms can pay — propagate through the entire system: they shift the wage curve, change tightness, and alter unemployment in equilibrium.
