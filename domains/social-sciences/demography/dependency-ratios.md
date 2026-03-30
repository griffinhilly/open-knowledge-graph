---
id: dependency-ratios
title: Dependency Ratios
domain: social-sciences
course: demography
prerequisites:
- id: population-pyramids-and-age-structure
  type: hard
- id: population-aging-demography
  type: soft
builds-toward:
- demographic-dividend
tags:
- dependency-ratio
- support-ratio
- old-age
- youth
stage: advanced
status: validated
---

# Dependency Ratios

## Core Idea
Dependency ratios measure the relationship between the "dependent" population (those not typically in the labor force) and the "productive" population (those of working age). The total dependency ratio divides the population aged 0-14 and 65+ by the population aged 15-64. The youth dependency ratio uses only the 0-14 numerator; the old-age dependency ratio uses only the 65+. These ratios provide a rough index of the economic burden on the working-age population. A declining total dependency ratio — typically occurring when fertility falls but before aging raises the old-age share — creates a "demographic window" of favorable conditions for economic growth. However, dependency ratios are crude proxies: they assume fixed age boundaries for labor force participation and treat all dependents as economically equivalent, ignoring the very different costs of children versus elderly.

## How It's Best Learned
Calculate all three dependency ratios for a country at multiple points in time (e.g., 1960, 1990, 2020, 2050 projected). Plotting the youth and old-age components separately reveals the transition from youth-heavy to elderly-heavy dependency — the "passing of the baton" between the two types of burden.

## Common Misconceptions
- A low dependency ratio does not automatically produce economic growth — it creates favorable conditions (a demographic window) that can only be exploited through appropriate investments in education, employment, and institutions.
- The conventional age boundaries (0-14 and 65+) are arbitrary and increasingly misleading as life expectancy increases and labor force participation patterns change. A 65-year-old in Japan may be economically active; a 20-year-old in university is technically "working age" but not earning.

## Questions

```yaml
- question: "A country's total dependency ratio falls from 90 to 50 over three decades as fertility declines. What does this change represent, and why might it not translate into economic growth?"
  type: multiple-choice
  options:
    - "Each working-age person now supports fewer dependents, but without investment in education, job creation, and institutions, the larger working-age population may be unemployed or underemployed"
    - "The country has become wealthier because fewer children means more savings"
    - "The change is meaningless because dependency ratios do not affect economic outcomes"
    - "Immigration of working-age adults is the only explanation for such a rapid decline"
  answer: 0
  explanation: "A declining dependency ratio means more workers per dependent — a favorable structural condition. But structure does not determine outcomes. If the expanding working-age population cannot find productive employment (due to weak institutions, poor education, insufficient capital formation), the demographic window will close without producing a dividend. East Asian countries exploited their windows through massive investment in education and export-oriented employment; some other countries with similar demographic profiles did not, and the window passed without comparable growth."

- question: "The old-age dependency ratio and the youth dependency ratio have similar economic implications because both measure non-working populations."
  type: true-false
  answer: false
  explanation: "Youth and elderly dependents have very different economic profiles. Youth dependency requires investment in education, nutrition, and healthcare that produces future workers — it is consumption that builds human capital. Old-age dependency requires pensions, healthcare (often expensive late-life care), and long-term support — it is consumption that does not generate future productive capacity. The fiscal and institutional demands differ substantially, which is why countries transitioning from high youth to high elderly dependency face qualitatively different challenges, not just a shift in the same kind of burden."

- question: "Explain the concept of the 'demographic window' and identify the conditions under which it opens and closes."
  type: short-answer
  answer: "The demographic window is the period during which the total dependency ratio is relatively low — typically when fertility has declined enough to reduce youth dependency but before population aging raises old-age dependency. It opens as the large cohorts born during the high-fertility era enter the workforce while the number of child dependents falls. It closes when those same large cohorts begin retiring, raising the old-age dependency ratio. The window typically lasts 30-50 years and represents a one-time structural opportunity: the ratio of workers to dependents is temporarily favorable, creating conditions for accelerated savings, investment, and economic growth — if complementary policies are in place."
  explanation: "The window is 'one-time' because it depends on the transitional age structure between high-fertility and aging phases. Once it closes, the old-age dependency ratio rises permanently (or until a new baby boom occurs, which is rare). Countries that miss the window — through unemployment, poor governance, or failure to invest in human capital — cannot reopen it by demographic means."
```

## Explainer

From population pyramids, you can see that different populations have different proportions of young, working-age, and elderly people. Dependency ratios quantify these proportions into a single number that approximates the economic support burden on the working-age population.

The **total dependency ratio** is (population 0-14 + population 65+) / population 15-64, typically multiplied by 100. A ratio of 80 means there are 80 dependents per 100 working-age people. This can be decomposed into the **youth dependency ratio** (0-14 / 15-64) and the **old-age dependency ratio** (65+ / 15-64). The two components move in opposite directions during the demographic transition: youth dependency falls as fertility declines, and old-age dependency rises as the population ages. The total dependency ratio traces a U-shaped curve, dipping to a minimum during the transition period.

This minimum creates the **demographic window** — a period of 30-50 years when the ratio of workers to dependents is unusually favorable. The window opens when fertility decline reduces the number of children while the large pre-decline birth cohorts are in their working years. It closes when those cohorts begin retiring, raising the old-age dependency ratio. During the window, the economic potential is real: fewer dependents per worker means higher potential savings rates, more resources available for investment per child (improving human capital), and a larger workforce relative to the total population.

But the window is an opportunity, not a guarantee. The **demographic dividend** — the actual economic growth that can result from a favorable dependency ratio — requires complementary conditions: educated workers, available employment, functioning institutions, and openness to trade. East Asia's rapid economic growth from the 1960s to 1990s coincided with a dramatic opening of the demographic window, but the growth was realized because of massive investments in education and export-oriented industrialization. Countries with similar demographic windows but weaker institutions — parts of Latin America and the Middle East in the same period — captured less of the potential dividend.

A critical limitation of dependency ratios is that the age boundaries are **arbitrary and static**. The 15-64 "working age" range was established when most people entered the labor force in their teens and retired in their early 60s. Today, with extended education delaying workforce entry and increasing healthy life expectancy enabling work past 65, the conventional ratio overstates dependency. Some demographers use alternative measures like the prospective old-age dependency ratio (defining "old" as having 15 or fewer remaining years of life expectancy, rather than a fixed age) or the economic dependency ratio (using actual labor force participation data). These refinements produce substantially different pictures of dependency in aging societies.
