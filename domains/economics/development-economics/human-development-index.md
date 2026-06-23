---
id: human-development-index
title: The Human Development Index
domain: economics
course: development-economics
prerequisites:
- id: development-measurement-fundamentals
  type: hard
- id: development-definition-and-measurement
  type: soft
- id: economic-development-definition
  type: soft
- id: gdp-limitations-alternative-metrics
  type: soft
- id: gross-domestic-product-development-measurement
  type: soft
tags:
- HDI
- measurement
- welfare
stage: advanced
status: validated
---

# The Human Development Index

## Core Idea
The HDI combines life expectancy, education (mean and expected years), and GNI per capita into a single index scaled 0–1. It enables cross-country comparisons of development progress and reveals that countries at similar income levels achieve vastly different human outcomes based on health and education investment.

## Questions

```yaml
- question: "Two countries have nearly identical GNI per capita. Country A has high life expectancy and high educational attainment. Country B has low life expectancy and low educational attainment. What does HDI analysis predict?"
  type: multiple-choice
  options:
    - "Their HDI scores will be similar, since GNI per capita is the dominant HDI component"
    - "Country A will score significantly higher, demonstrating that policy choices in health and education determine human outcomes independently of income"
    - "Country B will score higher because lower baseline human development means it has more potential for measured improvement"
    - "Neither country's HDI can be predicted without knowing the exact income figures to three decimal places"
  answer: 1
  explanation: "This scenario describes exactly what the HDI was designed to reveal: the divergence between income and human outcomes. Sri Lanka and Equatorial Guinea are the canonical real-world version of this comparison. The HDI uses a geometric mean of all three dimensions, so strong health and education performance gives Country A a much higher score even at the same income. This is the HDI's central insight — income alone does not determine human welfare; it depends critically on how income is invested in public health and education."

- question: "Why does the HDI use a geometric mean of its three dimension indices rather than a simple arithmetic average?"
  type: multiple-choice
  options:
    - "The geometric mean is computationally simpler when combining indices expressed in different units"
    - "A geometric mean ensures that very low performance on any single dimension substantially pulls down the overall score, preventing high income from fully compensating for poor health or education"
    - "The geometric mean gives extra weight to the income dimension, which the UNDP considers most important for development"
    - "The geometric mean eliminates the need to normalize each dimension to a 0–1 scale before combining"
  answer: 1
  explanation: "The switch from arithmetic to geometric mean (made in 2010) was deliberate. With an arithmetic mean, a very low score in one dimension (say, health = 0.1) can be offset by high scores in others. With a geometric mean, a near-zero score drags the overall product toward zero regardless of the other dimensions. This reflects a normative choice: a long life, knowledge, and a decent standard of living are not perfect substitutes — extreme deprivation in any one cannot be 'averaged away' by abundance in another."

- question: "A country with very high oil revenues and GNI per capita will necessarily have a high HDI score."
  type: true-false
  answer: false
  explanation: "Equatorial Guinea is the textbook counterexample. It has some of the highest per capita GNI in sub-Saharan Africa from oil revenues, yet scores poorly on the HDI because that income is concentrated among elites while most citizens lack access to basic healthcare and education. The geometric mean means that low scores on the health and education dimensions substantially depress the overall HDI even when income is high. High income is neither sufficient nor necessary for high human development — policy choices about distribution and investment in public goods are equally decisive."

- question: "The HDI's education dimension combines two indicators: mean years of schooling for current adults and expected years of schooling for children entering school today."
  type: true-false
  answer: true
  explanation: "The two-indicator approach is intentional. Mean years of schooling for adults captures the *existing stock* of human capital in the current workforce — what has already been achieved. Expected years of schooling for children captures the system's current *trajectory* — what it is promising the next generation. Using both gives a richer picture than a single indicator: a country might have a highly educated adult population from past investment but a collapsing school system, or vice versa. Earlier HDI versions used adult literacy rate, which was replaced to better capture both quantity and quality of education."

- question: "Explain what the comparison between Sri Lanka and Equatorial Guinea reveals about the relationship between income and human development, and why this is the HDI's core insight."
  type: short-answer
  answer: "Sri Lanka has modest per capita income but achieves high HDI scores through strong public investment in free healthcare and universal education, translating limited resources into long lives and an educated population. Equatorial Guinea has much higher per capita income from oil but scores poorly because that wealth is concentrated among elites while most citizens lack basic health and education services. This comparison demonstrates the HDI's central insight: income is not destiny — the same level of national income can produce dramatically different human outcomes depending on whether it is distributed equitably and invested in public goods. This finding challenges income-centric development frameworks and supports the capabilities approach: what matters is not just what a country earns, but whether that translates into people living long, healthy, and educated lives. The HDI makes this gap visible and politically consequential."
```

## Explainer

From studying **development measurement fundamentals**, you know that GDP per capita alone fails to capture whether an economy's output translates into genuine improvements in human welfare. The **Human Development Index (HDI)**, introduced by the United Nations Development Programme in 1990 and championed by economist Mahbub ul Haq (drawing on Amartya Sen's capabilities approach), was designed to provide a simple but more complete alternative.

The HDI combines three dimensions into a single number between 0 and 1. The **health dimension** uses life expectancy at birth — a powerful summary statistic because long lives require adequate nutrition, clean water, healthcare access, and absence of violence. The **education dimension** combines two indicators: mean years of schooling for adults (what has been achieved) and expected years of schooling for children entering school (what the system promises). The **income dimension** uses gross national income (GNI) per capita, adjusted for purchasing power parity so that a dollar reflects roughly the same buying power across countries. Each dimension is normalized to a 0–1 scale using observed minimum and maximum values, and the three dimension indices are combined using a geometric mean rather than a simple average — meaning that very low performance on any single dimension pulls down the overall score substantially.

The HDI's most powerful insight is the divergence it reveals between income and human outcomes. Sri Lanka and Equatorial Guinea illustrate this starkly. Sri Lanka, with modest per capita income, achieves high HDI scores through strong public investment in healthcare and free education. Equatorial Guinea, with very high per capita income from oil, scores poorly because that income is concentrated among elites while most citizens lack basic health and education services. Cuba, Kerala (India), and Costa Rica are other classic cases of countries or regions that "punch above their weight" on human development relative to income — demonstrating that policy choices about how income is distributed and invested matter as much as the income level itself.

The HDI has important limitations you should understand. It ignores inequality within countries (the Inequality-adjusted HDI, or IHDI, was created to address this). It omits political freedoms, environmental sustainability, and security. Its three dimensions are weighted equally, which is a normative choice that can be debated. And because it is a national average, it can mask enormous variation within countries — the HDI of urban Shanghai versus rural Guizhou within China would tell very different stories. Despite these limitations, the HDI succeeded in shifting the global development conversation: when the UNDP publishes annual rankings, governments that score poorly relative to their income face public pressure to invest in health and education, making the index a tool of both measurement and accountability.
