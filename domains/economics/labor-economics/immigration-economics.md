---
id: immigration-economics
title: Immigration Economics
domain: economics
course: labor-economics
prerequisites:
- id: labor-market-equilibrium
  type: hard
- id: wage-determination
  type: soft
tags:
- immigration
- labor-mobility
- Mariel-boatlift
- wage-effects
- complementarity
stage: advanced
status: validated
---

# Immigration Economics

## Core Idea
Immigration economics examines how the inflow of foreign workers affects native wages, employment, and the overall economy. The simple competitive model predicts that immigration increases labor supply, depressing wages for native workers who are substitutes for immigrants and raising wages for those who are complements. Empirical evidence — particularly Card's (1990) Mariel boatlift study and subsequent area-based analyses — generally finds small negative effects on native wages, especially for the average native worker, though effects on close substitutes (particularly low-skilled natives and previous immigrants) may be larger. The immigration surplus — the net gain to the receiving economy from employing immigrant labor at below-native wages — is positive but small relative to GDP. The debate centers on distributional effects (who gains and who loses), long-run assimilation, and fiscal impacts.

## Questions

```yaml
- question: "Card's (1990) study of the Mariel boatlift — when 125,000 Cuban refugees suddenly arrived in Miami — found that..."
  type: multiple-choice
  options:
    - "Native wages in Miami fell sharply due to the sudden increase in labor supply"
    - "Miami's labor market absorbed the immigrants with little detectable effect on native wages or employment"
    - "All Cuban immigrants immediately found high-paying jobs"
    - "The Miami labor market collapsed and never recovered"
  answer: 1
  explanation: "Card found that despite a 7% increase in Miami's labor force over a few months, there was no significant decline in wages or employment for native workers, including less-skilled natives and previous immigrants. This was surprising because the standard competitive model predicts wage depression from a large supply shock. The finding suggested that local labor markets are more absorptive than the simple model implies — through demand-side responses, geographic mobility of other workers, and industrial adjustment."

- question: "The wage impact of immigration is identical for all native workers regardless of their skill level."
  type: true-false
  answer: false
  explanation: "The impact depends on the degree of substitutability between immigrants and natives. Native workers whose skills are close substitutes for immigrants' skills face the most wage pressure. Native workers whose skills are complements to immigrants' skills may actually benefit. Low-skilled native workers face more competition from low-skilled immigrants, while high-skilled natives may benefit from complementary low-skilled immigrant labor (e.g., affordable childcare enabling higher workforce participation). The distributional effects are central — the aggregate effect may be small while specific groups experience significant impacts."

- question: "What is the 'immigration surplus' and why is it typically small relative to GDP?"
  type: short-answer
  answer: "The immigration surplus is the net gain to the native population from immigration — the increase in total output minus the portion that goes to immigrants themselves as wages. It is small (estimated at 0.1-0.3% of GDP) because while immigrants contribute significantly to output, most of that output accrues to the immigrants themselves as compensation. The surplus arises from the difference between immigrants' marginal product and their wage, which benefits employers and complementary workers. It is a real gain but modest relative to the total economy."
  explanation: "Borjas's calculation shows that the surplus depends on the square of the labor supply increase times the elasticity of labor demand. Even a large immigration flow produces a small surplus because the triangle gain is small relative to the rectangular transfer from native workers (whose wages fall) to employers (who pay lower wages). Immigration's largest economic effect is redistribution — from native workers who compete with immigrants to employers who hire them — rather than aggregate efficiency gain."
```

## Explainer

Immigration is simultaneously one of the most politically charged and empirically contested topics in labor economics. The theoretical predictions are relatively clear — they follow from supply and demand — but the empirical magnitudes have been fiercely debated for decades, with methodological choices often driving conclusions as much as the underlying data.

The basic supply-demand framework is the starting point. An inflow of immigrant workers shifts the labor supply curve outward. If immigrants are perfect substitutes for native workers, this increased supply reduces the equilibrium wage and increases employment (firms hire more at the lower wage). If immigrants are complements to native workers (e.g., immigrant construction laborers complementing native construction supervisors), both groups' wages can rise. The magnitude of the wage effect depends on the elasticity of labor demand and the degree of substitutability — parameters that are empirically estimated, not theoretically determined.

Card's Mariel boatlift study (1990) provided a natural experiment that seemed too good to be true: 125,000 Cuban refugees arrived in Miami over a few months in 1980, increasing the labor force by about 7%. If immigration depresses wages, this sudden, large, exogenous shock should produce detectable effects. Using a difference-in-differences design comparing Miami to control cities, Card found no significant impact on native wages or unemployment. This finding was influential but controversial — Borjas (2017) later reanalyzed the data using a narrower definition of low-skilled workers and found significant wage effects, leading to a methodological debate that remains unresolved.

The broader empirical literature using area-based approaches (comparing immigration-heavy and immigration-light cities) generally finds small wage effects, but these estimates may be biased by native out-migration (if natives leave high-immigration areas, diluting the measured impact) and capital adjustment (if firms invest more in high-immigration areas, absorbing the labor supply shock). National-level analyses by Borjas, which avoid the geographic mobility problem by comparing skill groups (defined by education and experience) over time, tend to find larger negative effects — a 10% increase in labor supply in a skill group reduces wages by 3-4%. The disagreement between area-based and national studies reflects fundamentally different identification strategies and remains a central methodological debate.

The distributional dimension is crucial for policy. Even if the aggregate wage effect is small, specific groups may be significantly affected. Low-skilled native workers and previous immigrants are the closest substitutes for new low-skilled immigrants and bear the largest wage losses. High-skilled natives who are complementary to immigrant labor — or who benefit from immigrant-provided services (affordable childcare, food service, construction) that expand their own labor supply options — may gain. The immigration surplus accrues mainly to employers and complementary workers, while the costs fall on substitutable workers. This distributional pattern explains why the same overall finding ("small average effects") can support very different policy conclusions depending on which distributional consequences are emphasized.
