---
id: lifecycle-labor-supply
title: Lifecycle Labor Supply
domain: economics
course: labor-economics
prerequisites:
- id: labor-supply-theory
  type: hard
- id: human-capital-theory
  type: soft
- id: gender-wage-gap
  type: soft
tags:
- lifecycle-model
- Heckman
- selection-correction
- Chiappori
- collective-model
- extensive-margin
- intensive-margin
- female-labor-force-participation
stage: advanced
status: validated
---

# Lifecycle Labor Supply

## Core Idea
Lifecycle labor supply models analyze how individuals and households allocate time between work, leisure, and home production over the course of their lives, rather than treating labor supply as a static decision at a point in time. The framework distinguishes between the extensive margin (whether to participate in the labor force at all) and the intensive margin (how many hours to work conditional on participation), a distinction critical for understanding female labor supply. Key contributions include Heckman's (1974, 1979) selection correction for the extensive margin (accounting for the fact that observed wages represent only those who chose to participate), the MaCurdy (1981) lifecycle model (where intertemporal substitution of leisure means workers supply more labor when wages are temporarily high), and Chiappori's (1988, 1992) collective household model (which models the household as two agents with different preferences bargaining over labor supply, replacing the unitary household assumption). These models explain the dramatic rise in female labor force participation, the U-shaped lifecycle earnings profile, the decline in male labor force participation, and the impact of tax and transfer policies on work incentives.

## Questions

```yaml
- question: "Heckman's selection correction addresses what fundamental problem in estimating the labor supply function for women?"
  type: multiple-choice
  options:
    - "Women are less productive than men, requiring a different production function"
    - "Observed wages exist only for women who choose to work, creating a non-random sample — women with high potential wages are overrepresented, biasing wage and labor supply estimates"
    - "Women's wages are determined by different factors than men's wages"
    - "Women face discrimination that must be removed before estimating true labor supply"
  answer: 1
  explanation: "The selection problem is statistical, not behavioral. When we observe wages, we only observe them for people who have chosen to work — those whose market wage exceeds their reservation wage. Women who stay out of the labor force are disproportionately those with low potential wages and/or high reservation wages (due to high home productivity, young children, or a high-earning spouse). Estimating labor supply from the observed sample treats these self-selected participants as representative of all women, biasing estimates of the wage effect on labor supply. Heckman's two-step procedure corrects for this by first modeling the participation decision (probit) and then including the inverse Mills ratio as a regressor in the wage/hours equation to account for the non-random sample."

- question: "The lifecycle labor supply model predicts that workers should work more hours during periods when their wages are temporarily high."
  type: true-false
  answer: true
  explanation: "This is the intertemporal substitution of leisure — the central prediction of the lifecycle model. Workers who can choose when to work will concentrate their labor supply in periods when the return to work is highest (wages are temporarily high relative to their lifecycle average) and take more leisure when wages are temporarily low. This prediction follows from the standard intertemporal optimization: the marginal rate of substitution between leisure today and leisure tomorrow equals the ratio of wages today and tomorrow (adjusted for the interest rate). Empirically, the intensive-margin elasticity of intertemporal substitution is modest (around 0.1-0.5 for men), but the extensive-margin response (entering or exiting the labor force) can be much larger, particularly for married women and older workers."

- question: "How does Chiappori's collective model of household labor supply differ from the traditional unitary household model, and why does the distinction matter?"
  type: short-answer
  answer: "The unitary model treats the household as a single decision-maker with a single utility function, as if household members pool all income and maximize joint utility. Chiappori's collective model recognizes that households contain multiple members with potentially different preferences, and models household decisions as the outcome of a bargaining process. Each member has their own utility function, and the household allocation is Pareto efficient — no member can be made better off without making another worse off. The sharing rule determines how household resources are divided, and it depends on each member's bargaining power (influenced by outside options such as divorce value, own earnings, welfare benefits, and marriage market conditions). This matters because it predicts that changes in women's outside options (e.g., divorce law reform, female wage growth) shift the sharing rule and affect labor supply even if total household income is unchanged — a prediction the unitary model cannot make."
  explanation: "The collective model explains empirical findings that the unitary model cannot: income in the wife's name affects spending differently from income in the husband's name (violating income pooling), changes in divorce laws affect married women's labor supply (through bargaining power, not direct applicability), and conditional cash transfers targeted to women change household behavior differently from transfers to men. The model also provides a framework for understanding the relationship between female labor force participation and women's economic empowerment — when women's labor market opportunities improve, their bargaining position within the household strengthens, which further encourages participation."
```

## Explainer

Static labor supply theory asks: given a wage rate, how many hours does a person choose to work? This question, while foundational, misses most of what makes labor supply interesting and policy-relevant. People do not make a single labor supply decision — they make a sequence of decisions over decades, influenced by changing wages, evolving household composition, the arrival and aging of children, health shocks, and retirement incentives. Lifecycle labor supply models embed the static tradeoff in this dynamic context, and the richer framework changes both the theoretical predictions and the empirical methods.

The **extensive margin** — whether to participate at all — is arguably more important than the intensive margin for understanding labor supply variation across groups and over time. The dramatic rise in female labor force participation (from about 34% in 1950 to 57% in 2000 in the United States) was overwhelmingly an extensive-margin phenomenon: women entered the workforce, not that working women worked more hours. Heckman recognized that this creates a fundamental statistical problem: when we observe wages, we see only those who chose to work. If a researcher estimates the effect of wages on hours worked using data only from working women, the estimate is biased because the sample is self-selected — women with high potential wages are more likely to participate. The Heckman selection correction (1979) models the participation decision explicitly and adjusts the hours/wage equation for the non-random sample. This correction was so influential that it became one of the most widely used econometric techniques in labor economics, and it contributed to Heckman's 2000 Nobel Prize.

The **intertemporal dimension** of lifecycle models changes how we think about labor supply elasticities. MaCurdy (1981) distinguished between the Marshallian elasticity (response to a permanent wage change, confounded by income effects), the Hicksian elasticity (response holding utility constant), and the Frisch elasticity (response to a temporary wage change, holding the marginal utility of wealth constant). The Frisch elasticity captures pure intertemporal substitution: when wages are temporarily high, workers substitute toward more work and less leisure, and when wages are temporarily low, they substitute toward leisure. This is why taxi drivers work more hours on rainy days (when wages per hour are temporarily high due to demand) and why seasonal workers concentrate labor in high-wage periods. The Frisch elasticity is typically larger than the Marshallian elasticity because temporary wage changes do not trigger the income effect that partially offsets the substitution effect of permanent changes. Estimates of the male Frisch elasticity range from 0.1 to 0.5 — small but positive, and larger on the extensive margin.

**Chiappori's collective model** (1988, 1992) revolutionized how economists think about household labor supply. The traditional approach treated the household as a unitary decision-maker — "the household maximizes utility" as if the family were a single person. This assumption implies income pooling (it does not matter which spouse earns the income) and a single set of preferences. Both predictions are rejected by the data: money controlled by women is spent differently than money controlled by men, and changes in women's outside options (divorce law reform, welfare availability, female wage growth) affect household decisions even holding total resources constant. Chiappori's model explains these findings by modeling the household as two agents who bargain to a Pareto-efficient allocation. The "sharing rule" — how total household resources are divided between the spouses — depends on bargaining power, which in turn depends on outside options. When a woman's potential earnings rise or divorce becomes more accessible, her bargaining power increases, she claims a larger share of household resources, and her labor supply and consumption decisions shift accordingly. This framework connects labor economics to family economics, gender economics, and development economics, providing a unified theory of how changes in women's economic opportunities translate into changes in household behavior, fertility decisions, and child investment.
