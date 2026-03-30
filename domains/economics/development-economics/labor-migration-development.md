---
id: labor-migration-development
title: Labor Migration and Development
domain: economics
course: development-economics
prerequisites:
- id: lewis-model-structural-transformation
  type: soft
- id: wage-dynamics-labor-frictions
  type: soft
tags:
- migration
- labor
stage: advanced
status: validated
---

# Labor Migration and Development

## Core Idea
Internal rural-urban migration and international migration from poor to rich countries are central to development. Migration allows workers to access higher-wage opportunities and reallocates labor from low to high-productivity sectors. Migration also creates social disruption, urban congestion, and brain drain when highly educated workers leave. Optimal migration policy balances these effects.

## Questions

```yaml
- question: "According to the Harris-Todaro model, why does rural-to-urban migration continue even when measured urban unemployment is high?"
  type: multiple-choice
  options:
    - "Migrants are irrational and overestimate their chances of finding urban work"
    - "Migrants respond to expected wages — the probability of finding a high-wage job times the wage — not the actual current unemployment rate"
    - "Urban wages are always higher than rural wages regardless of unemployment, so migration is always rational"
    - "Rural areas push migrants out by reducing agricultural wages as cities attract workers"
  answer: 1
  explanation: "The Harris-Todaro key insight is that the relevant comparison is not current rural wages vs. current urban wages among the employed — it is rural wages vs. the expected urban wage, which accounts for the probability of finding employment. If urban wages are high enough, a worker may rationally migrate even when unemployment is substantial, because the expected payoff (probability of employment × wage) still exceeds the certain rural income. This is why urban slums persist alongside urban growth: migration equilibrium occurs when expected urban wages equal rural wages, not when urban unemployment is zero."

- question: "A poor country trains doctors using heavy public subsidies. Those doctors emigrate to rich countries after qualifying. Beyond the loss of their current labor, what is the primary long-run economic cost to the sending country?"
  type: multiple-choice
  options:
    - "The sending country loses the taxes those doctors would have paid"
    - "The sending country loses the human capital investment it financed — resources spent training workers who now generate returns for a richer country"
    - "The sending country must import medical services, which is always more expensive than domestic provision"
    - "The sending country's remaining doctors face higher competition from foreign-trained workers who return"
  answer: 1
  explanation: "Brain drain transfers not just the workers but the educational investment that produced them. The sending country bore the cost (public funding, foregone alternative uses of those individuals' training years) but captures none of the future return. This is the core of the brain drain concern: it represents a transfer of publicly financed human capital from poor to rich countries. The phenomenon is most acute in professions with long training periods heavily subsidized by the state — medicine, engineering, academia."

- question: "Remittances from international migrants often exceed the value of official foreign aid received by developing countries."
  type: true-false
  answer: true
  explanation: "This is empirically true for many developing countries. Remittances have grown to be one of the largest financial inflows to low- and middle-income countries, surpassing official development assistance in aggregate. Unlike foreign aid, remittances flow directly to households, often bypassing government intermediaries, and can be more reliably counter-cyclical — migrants may send more when their home country faces a crisis."

- question: "The Harris-Todaro model predicts that migration will slow and stop once urban unemployment rises high enough to equalize the expected urban wage with the rural wage."
  type: true-false
  answer: false
  explanation: "This statement misreads the Harris-Todaro equilibrium condition. The model predicts that migration continues until EXPECTED urban wages equal rural wages — meaning equilibrium includes some positive unemployment rate. The prediction is NOT that migration stops when unemployment is high; rather, migration reaches a steady state where the unemployment rate is precisely the level that equalizes expected returns. If the urban wage rises or rural wages fall, migration increases until a new equilibrium unemployment rate is established. Migration does not stop because unemployment is high — it finds an equilibrium WITH unemployment."

- question: "In what sense is the decision to migrate analogous to an investment in education, and what does this imply about who is most likely to migrate?"
  type: short-answer
  answer: "Migration, like education, involves upfront costs (travel, job search, social dislocation) borne now in exchange for a stream of higher future earnings. This implies that migration is more attractive for younger workers (more future years over which to recoup the investment), for workers with higher earning potential in the destination, and for those with lower costs of moving. It also implies a selection effect: migrants are not random draws from the population — they tend to be younger, more educated, and more entrepreneurially minded than those who stay."
  explanation: "The investment framing explains several patterns: why migration rates are highest among young adults, why educated workers are more likely to migrate internationally (higher wage gains justify the cost), and why migration can reduce in volatility as workers age (the remaining payoff period shrinks). It also helps explain remittances — migrants who view migration as temporary may remit heavily to maintain ties for an eventual return, while those who migrate permanently eventually reduce remittances."
```

## Explainer

From the Lewis model of structural transformation, you know that development involves moving workers from low-productivity agriculture to higher-productivity industry and services. **Labor migration** is the mechanism through which this reallocation actually happens — people physically move from rural villages to cities, or from poor countries to rich ones, in search of better wages. At its core, migration is an investment decision: the migrant bears upfront costs (travel, job search, social dislocation) in exchange for expected future earnings gains, just as a student invests time in education for higher future wages.

**Internal migration** — typically rural-to-urban — is the most common form in developing countries and the engine of urbanization. When a young person leaves a farming village for a factory job in a growing city, two things happen simultaneously. First, the migrant earns more, because urban industrial wages exceed rural agricultural wages (this is the Lewis model's core prediction). Second, the economy becomes more productive in aggregate, because the same worker now produces more value. This is why urbanization and economic growth are so tightly correlated across countries: migration reallocates labor toward its most productive use.

**International migration** operates on the same logic at a larger scale. Wage gaps between rich and poor countries are enormous — a construction worker might earn ten times more in the Gulf states than in Bangladesh. **Remittances**, the money migrants send home, have become one of the largest financial flows to developing countries, exceeding foreign aid in many cases. For sending households, remittances provide insurance against crop failure and income to invest in children's education. For sending countries, remittances provide foreign exchange and can reduce poverty more directly than many aid programs.

But migration also generates costs that explain why it remains politically contentious. Urban areas in developing countries often grow faster than infrastructure and housing can accommodate, producing slums, congestion, and strained public services — the phenomenon captured by the **Harris-Todaro model**, where migration continues even when urban unemployment is high because migrants respond to expected rather than actual wages. **Brain drain** occurs when the most educated and skilled workers leave poor countries for rich ones, depriving the sending country of the human capital it invested in. A doctor trained at public expense in Ghana who practices in London represents a transfer of human capital from poor to rich. Whether the net effect of migration is positive depends on the balance between these gains and costs — and that balance varies enormously depending on who migrates, where they go, and whether they maintain economic ties to their origin.
