---
id: intergenerational-mobility
title: Intergenerational Mobility
domain: economics
course: labor-economics
prerequisites:
- id: human-capital-theory
  type: hard
- id: returns-to-education
  type: soft
tags:
- mobility
- Chetty
- opportunity
- inequality
- Great-Gatsby-curve
stage: advanced
status: validated
---

# Intergenerational Mobility

## Core Idea
Intergenerational mobility measures the extent to which children's economic outcomes are independent of their parents' — the degree to which a person's position in the income distribution is determined by their own effort and ability versus their family background. The intergenerational elasticity (IGE) of income measures the correlation between parents' and children's earnings, with higher values indicating less mobility. The US has relatively low mobility (IGE ≈ 0.4-0.5) compared to Nordic countries (IGE ≈ 0.2). Chetty et al.'s work using IRS tax records revealed enormous geographic variation in mobility within the US, with local factors like school quality, social capital, and neighborhood characteristics explaining much of the variation. The "Great Gatsby curve" (Corak) documents a cross-country correlation between inequality and immobility, suggesting that higher inequality reduces intergenerational mobility.

## Questions

```yaml
- question: "An intergenerational elasticity (IGE) of 0.5 means that..."
  type: multiple-choice
  options:
    - "Children earn exactly half of what their parents earned"
    - "If a parent earns 10% above the mean, their child is expected to earn 5% above the mean — half the parental advantage persists"
    - "50% of children earn more than their parents"
    - "Income is completely determined by parental income"
  answer: 1
  explanation: "The IGE is the elasticity of child income with respect to parent income. An IGE of 0.5 means that 50% of the parents' position above (or below) the mean is transmitted to the next generation. A parent at the 90th percentile produces a child expected at the 70th percentile (halfway between 90th and 50th). Complete mobility would be IGE = 0 (parents' income has no effect); complete immobility would be IGE = 1 (children replicate parents' position exactly). The US IGE of 0.4-0.5 indicates substantial persistence — roughly half of economic advantage or disadvantage carries across generations."

- question: "The 'Great Gatsby curve' suggests that countries with higher income inequality tend to have higher intergenerational mobility."
  type: true-false
  answer: false
  explanation: "The Great Gatsby curve documents the opposite relationship: countries with higher inequality tend to have LOWER intergenerational mobility. The US and UK (high inequality, low mobility) contrast with Denmark and Finland (low inequality, high mobility). The proposed mechanism is that inequality increases the distance between rungs on the economic ladder, making it harder for children from low-income families to climb. Inequality also correlates with disparities in school quality, neighborhood conditions, and social capital that transmit advantage and disadvantage across generations."

- question: "What did Chetty et al.'s research reveal about geographic variation in mobility within the United States?"
  type: short-answer
  answer: "Using IRS tax records for millions of Americans, Chetty et al. found enormous variation in intergenerational mobility across US commuting zones. Children born to low-income families in some areas (e.g., Salt Lake City, San Jose) had much higher chances of reaching the top income quintile than those in other areas (e.g., Atlanta, Charlotte). The factors most correlated with high mobility were: less residential segregation, less income inequality, better schools, stronger social networks, and more two-parent families. This variation suggests that local institutions and community characteristics profoundly shape children's life chances."
  explanation: "The geographic variation is striking — a child's chances of upward mobility can differ by a factor of two or more depending on where they grow up, even controlling for parental income. Chetty's subsequent work using movers (families who relocate) showed that moving to a high-mobility area during childhood improves children's outcomes, with larger effects for younger children. This provides causal evidence that place matters — it is not just that high-mobility areas attract better-off families, but that the characteristics of the area itself improve outcomes."
```

## Explainer

The promise of meritocracy — that your economic position should reflect your talent and effort, not your parents' bank account — is central to the social contract in market economies. Intergenerational mobility research tests whether this promise is being kept. The answer, across developed countries, is: imperfectly, with enormous variation across places, time periods, and institutional contexts.

The intergenerational elasticity of income is the standard summary measure. Estimated from the regression of children's log earnings on parents' log earnings (typically measured at comparable ages, mid-career), it captures how much of a parent's relative income position is transmitted to the next generation. The US IGE of 0.4-0.5 is strikingly high compared to Nordic countries (0.15-0.25), meaning that family background matters roughly twice as much in the US as in Scandinavia. Canada, Germany, and France fall between these extremes. These differences persist after controlling for measurement issues (lifecycle bias, attenuation from transitory income shocks), suggesting they reflect genuine institutional differences.

The mechanisms of intergenerational transmission are multiple and interacting. Genetic inheritance of traits correlated with earnings (cognitive ability, personality) accounts for some persistence, though behavioral genetics estimates suggest this explains perhaps 30-40% of the IGE. The remainder reflects environmental transmission: wealthier parents provide better nutrition, healthcare, neighborhoods, schools, social networks, information about navigating institutions, and direct financial transfers. They also transmit aspirations, attitudes toward education, and cognitive stimulation through home environments. Disentangling these mechanisms is crucial for policy: genetic transmission is not amenable to policy intervention, while environmental transmission can be addressed through early childhood programs, school quality improvement, and neighborhood investment.

Chetty's research program, leveraging the universe of US tax records, transformed the field by moving from national averages to granular geographic data. The Opportunity Atlas shows upward mobility (the expected income rank of children born to 25th-percentile parents) for every census tract in America. The variation is enormous: in the highest-mobility tracts, low-income children reach the middle class at rates comparable to Denmark; in the lowest-mobility tracts, they remain stuck in poverty at rates worse than any national average. The five factors most correlated with high mobility — less residential segregation, less inequality, better schools, more social capital, and more stable families — point toward specific, place-based policy targets.

The Great Gatsby curve — the cross-country correlation between income inequality and intergenerational persistence — suggests that inequality and immobility are structurally linked, not independent phenomena. High inequality means more distance between income levels, making it harder for disadvantaged children to bridge the gap. It also means more segregation of residential neighborhoods, schools, and social networks by income, reducing the cross-class interactions that facilitate upward mobility. If this relationship is causal (and Chetty's within-US evidence supports this), then rising inequality is not just a distributional concern but a mobility concern — it is pulling up the ladder for the next generation.
