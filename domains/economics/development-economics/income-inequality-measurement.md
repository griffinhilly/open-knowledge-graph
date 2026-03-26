---
id: income-inequality-measurement
title: Measuring and Understanding Income Inequality
domain: economics
course: development-economics
prerequisites:
- id: gdp-and-national-income
  type: soft
- id: gross-domestic-product-development-measurement
  type: soft
- id: human-development-index
  type: soft
- id: multidimensional-poverty-measurement
  type: soft
builds-toward:
- inequality-kuznets-curve
tags:
- inequality
- measurement
stage: expert
status: validated
---
# Measuring and Understanding Income Inequality

## Core Idea
Income inequality is measured by Gini coefficients, Lorenz curves, and percentile shares. High inequality imposes economic costs through reduced social cohesion, political instability, and potentially reduced growth. Developing countries show substantial variation—Latin America exhibits high inequality despite moderate income levels while East Asia shows lower inequality, demonstrating that development paths and policy choices shape distributional outcomes.

## Questions

```yaml
- question: "Countries A and B both have a GDP per capita of $12,000. Country A has a Gini coefficient of 0.28; Country B has a Gini coefficient of 0.58. A policymaker claims the two countries have equivalent living standards because their averages are identical. What critical information does this claim miss?"
  type: multiple-choice
  options:
    - "GDP per capita is adjusted for purchasing power in Country A but not in Country B, making the comparison invalid"
    - "The Gini coefficient shows that Country B's income is far more concentrated at the top, meaning most households likely have incomes well below $12,000 while a small elite earns far above it — the average conceals vastly different typical lived experiences"
    - "Country B's higher Gini means it is growing faster, which will reduce inequality in the long run through the Kuznets curve"
    - "The policymaker is correct — Gini only measures distribution, not welfare, so the same GDP per capita implies identical aggregate welfare"
  answer: 1
  explanation: "GDP per capita is an average, and averages can be deeply misleading when distribution is skewed. A Gini of 0.58 (typical of highly unequal countries) means the Lorenz curve bows far below the 45-degree equality line — the bottom half of the population holds a small fraction of total income. Most households live on far less than $12,000 while income concentrates at the top. Equal averages can coexist with radically different distributions: the Gini coefficient is precisely the tool for seeing inside the average to evaluate actual distributional equality."

- question: "Why has the Palma ratio (top 10% share divided by bottom 40% share) gained favor as a complement to the Gini coefficient?"
  type: multiple-choice
  options:
    - "Because it is easier to calculate than the Gini and requires no graphical representation of a Lorenz curve"
    - "Because the middle 50% of the income distribution is relatively stable across countries and time — most inequality variation occurs in the tails — so the Palma ratio focuses attention where distributional differences are actually largest"
    - "Because international agencies like the World Bank officially adopted it as their primary inequality metric in 2010"
    - "Because it corrects a known mathematical error in the Gini coefficient that makes it underestimate inequality in developing countries"
  answer: 1
  explanation: "The insight behind the Palma ratio is empirical: across many countries and time periods, the middle 50% of the income distribution consistently holds roughly half of national income. Most of the cross-country variation in inequality shows up at the extremes — the richest 10% and the poorest 40%. By directly comparing these extremes, the Palma ratio focuses attention on where real differences lie. It is also intuitively interpretable: a Palma of 3 means the richest 10% earn three times as much as the poorest 40% combined."

- question: "A Gini coefficient of 0.5 means the top 50% of earners hold exactly 50% of all income."
  type: true-false
  answer: false
  explanation: "The Gini coefficient is not a percentile share ratio — it measures the area between the Lorenz curve and the 45-degree line of perfect equality, divided by the total area under the 45-degree line. A Gini of 0.5 means this ratio equals 0.5, which is consistent with many different shapes of the Lorenz curve and many different percentile shares. The 50th percentile income share is a separate statistic. In highly unequal economies, the top 50% can easily hold 80% or more of income while the Gini is around 0.5."

- question: "Two countries with identical GDP per capita can have very different distributions of income, as captured by differences in their Gini coefficients."
  type: true-false
  answer: true
  explanation: "This is the foundational motivation for inequality measurement. GDP per capita divides total income by population, but this average is consistent with any distribution from perfect equality to extreme concentration. The Gini coefficient and Lorenz curve reveal the shape of the distribution independent of the mean. A country where everyone earns $10,000 and a country where one person earns $1 million and ninety-nine earn roughly $1,000 can have the same GDP per capita but vastly different Gini coefficients (approaching 0 and 1, respectively)."

- question: "Through what economic mechanisms does high income inequality potentially slow economic growth — beyond simply being unfair?"
  type: short-answer
  answer: "High inequality can suppress growth through several reinforcing channels. First, it undermines human capital accumulation: poor households cannot invest in education, nutrition, and health for their children, reducing the economy's future productivity. Second, it weakens domestic demand — when income concentrates at the top, where marginal propensity to consume is lower, consumer markets remain thin and firms serving mass markets face limited opportunities. Third, it erodes social cohesion and institutional quality, breeding corruption, rent-seeking, and political instability that divert resources from productive use. Fourth, extreme inequality can produce political capture, where elites shape policy to protect their position rather than promote broad-based investment."
  explanation: "These channels explain why highly unequal countries often experience slower or more fragile growth — the distributional issue is not just ethical but functional. The cross-regional comparison in the topic illustrates this: East Asian economies combined rapid growth with relatively low inequality partly through land reform, broad education investment, and manufacturing-led employment; Latin American economies with historically high inequality (rooted in colonial land concentration) have faced more persistent growth challenges. Inequality is not an inevitable consequence of development; it is shaped by policies and institutions."
```

## Explainer

From your understanding of GDP and national income, you know that aggregate measures like GDP per capita tell you how much income a country produces on average — but averages can be deeply misleading. A country where ten people each earn $10,000 and a country where one person earns $91,000 and nine earn $1,000 have the same GDP per capita, but they are fundamentally different economies with different social dynamics, political pressures, and development prospects. **Income inequality measurement** provides the tools to look inside the average and understand how income is actually distributed.

The most intuitive tool is the **Lorenz curve**. To build one, rank every person in the population from poorest to richest along the horizontal axis (as cumulative percentages), and plot the cumulative share of total income they hold on the vertical axis. If income were perfectly equal, the Lorenz curve would be a 45-degree line — the bottom 20% would hold 20% of income, the bottom 50% would hold 50%, and so on. In practice, the curve bows below this line: the bottom 20% might hold only 5% of income while the top 20% holds 50%. The further the curve bows from the 45-degree line, the more unequal the distribution.

The **Gini coefficient** converts the Lorenz curve into a single number between 0 (perfect equality) and 1 (one person holds all income). It equals the area between the Lorenz curve and the 45-degree line, divided by the total area under the 45-degree line. A Gini of 0.25 (typical of Scandinavian countries) means relatively compressed incomes; a Gini of 0.60 (typical of South Africa or parts of Latin America) indicates extreme concentration. **Percentile ratios** offer a complementary view: the 90/10 ratio compares income at the 90th percentile to income at the 10th, capturing the gap between rich and poor without being sensitive to extreme outliers. The **Palma ratio** (share of the top 10% divided by share of the bottom 40%) has gained popularity because the middle 50% of the distribution tends to be stable across countries — most of the action is in the tails.

Why does inequality matter for development, beyond fairness? High inequality can suppress growth through several channels. It reduces **social cohesion** and trust, making collective action and public investment harder. It creates **political instability** — extreme inequality breeds resentment, corruption, and rent-seeking that divert resources from productive use. It can reduce **human capital accumulation** if poor households cannot invest in education and health. And it weakens **domestic demand** — when most income flows to a small elite, consumer markets remain thin, limiting opportunities for firms that serve mass markets. The wide variation in inequality across developing countries — Latin America persistently high, East Asia relatively low — shows that inequality is not an inevitable consequence of being poor. It reflects historical legacies (colonial land distribution, racial exclusion), policy choices (progressive taxation, public education, land reform), and the structure of growth itself (whether growth creates broad-based employment or concentrates gains in resource extraction and finance).
