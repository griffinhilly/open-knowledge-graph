---
id: empirical-methods-labor-economics
title: Empirical Methods in Labor Economics
domain: economics
course: labor-economics
prerequisites:
- id: labor-market-equilibrium
  type: hard
- id: minimum-wage-economics
  type: soft
- id: returns-to-education
  type: soft
- id: causal-inference-econometrics
  type: soft
tags:
- credibility-revolution
- difference-in-differences
- regression-discontinuity
- instrumental-variables
- natural-experiments
- Card-Krueger
stage: advanced
status: validated
---

# Empirical Methods in Labor Economics

## Core Idea
Labor economics has been at the frontier of the "credibility revolution" in empirical economics — the shift from structural estimation and OLS regressions toward quasi-experimental methods that provide more credible causal identification. The key challenge is that most labor market questions involve endogeneity: does education cause higher wages, or do more able people both earn more and get more education? Do minimum wages reduce employment, or do states that raise minimum wages differ systematically from those that do not? Four identification strategies dominate modern labor economics: difference-in-differences (comparing changes in outcomes between a treated and control group, as in Card and Krueger's 1994 minimum wage study), regression discontinuity (exploiting sharp eligibility thresholds, as in studies using age cutoffs for policy eligibility), instrumental variables (using exogenous variation to isolate causal effects, as in Angrist and Krueger's 1991 use of quarter of birth to instrument for schooling), and natural experiments (exploiting policy changes, institutional features, or historical accidents as sources of quasi-random variation). These methods transformed the field from one where empirical claims were weakly identified to one with a high standard of causal evidence.

## Questions

```yaml
- question: "Card and Krueger's (1994) study of New Jersey's minimum wage increase used which identification strategy?"
  type: multiple-choice
  options:
    - "Instrumental variables, using political ideology as an instrument for the minimum wage"
    - "Regression discontinuity, using the minimum wage threshold as a cutoff"
    - "Difference-in-differences, comparing employment changes in New Jersey fast-food restaurants (treatment) to Pennsylvania fast-food restaurants (control) before and after the increase"
    - "Randomized controlled trial, with randomly selected restaurants receiving higher minimum wages"
  answer: 2
  explanation: "Card and Krueger used a difference-in-differences (DiD) design: they surveyed fast-food restaurants in New Jersey and eastern Pennsylvania before and after New Jersey raised its minimum wage from $4.25 to $5.05 in 1992. Pennsylvania, which did not raise its minimum wage, served as the control group. The key assumption (parallel trends) is that employment in New Jersey and Pennsylvania restaurants would have changed similarly absent the minimum wage increase. They found no evidence that the increase reduced employment — a finding that challenged the standard competitive model and was consistent with monopsony."

- question: "The 'credibility revolution' in labor economics refers to the development of new economic theories about how labor markets function."
  type: true-false
  answer: false
  explanation: "The credibility revolution is about empirical methodology, not theory. It refers to the shift — beginning in the late 1980s and accelerating in the 1990s — from relying on structural models and cross-sectional regressions (which require strong, often untestable assumptions) toward quasi-experimental methods (DiD, RD, IV, natural experiments) that provide more credible identification of causal effects. The term was coined by Angrist and Pischke. The revolution changed what counts as convincing empirical evidence in labor economics: instead of a well-specified structural model, researchers now need a credible source of exogenous variation — either experimental or quasi-experimental — to support causal claims."

- question: "Why did Angrist and Krueger (1991) use quarter of birth as an instrument for years of schooling in their study of returns to education, and what makes this a valid instrument?"
  type: short-answer
  answer: "Compulsory schooling laws require students to stay in school until a certain age (typically 16). Because school entry is determined by calendar-year cutoffs, students born earlier in the year reach the compulsory schooling age earlier in their academic career and can legally drop out with less total schooling than those born later. Quarter of birth thus affects years of schooling (relevance) through the interaction of compulsory schooling laws and school entry dates. For validity (the exclusion restriction), quarter of birth must affect earnings only through its effect on schooling — not through any direct channel. Angrist and Krueger argued that birth timing is essentially random with respect to ability and other determinants of earnings, making it a plausible instrument."
  explanation: "This study is a canonical example of the instrumental variables approach in labor economics. OLS estimates of returns to education are biased because ability affects both schooling and earnings (omitted variable bias). The IV strategy uses quarter of birth to isolate variation in schooling that is plausibly exogenous — driven by the accident of birth timing interacting with institutional rules, not by individual choices. The estimated return to education was roughly 7-8% per year, similar to OLS, suggesting that ability bias in the returns-to-education literature may be smaller than feared. However, the instrument has been criticized for being weak (quarter of birth explains very little variation in schooling) and for potential violations of the exclusion restriction (birth season may correlate with family background)."
```

## Explainer

The central challenge of empirical labor economics is the same challenge that pervades all empirical social science: establishing causation rather than mere correlation. Does an additional year of schooling cause wages to rise by 8%, or do people who would have earned high wages anyway also happen to get more education? Does the minimum wage reduce employment, or do unobserved economic conditions confound the relationship? These questions cannot be answered by running a regression of wages on schooling, because the regression coefficient conflates the causal effect of schooling with the selection effect of who gets more schooling. The credibility revolution was the field's collective response to this identification problem.

**Difference-in-differences** (DiD) is perhaps the most widely used quasi-experimental method in labor economics. The core idea is simple: compare the change in an outcome for a group affected by a policy change (treatment group) to the change for a group not affected (control group). The difference in these differences removes time-invariant unobserved factors (which are differenced out within each group) and common time trends (which cancel in the between-group comparison). Card and Krueger's 1994 minimum wage study is the canonical example: they compared employment changes in New Jersey fast-food restaurants before and after a minimum wage increase to changes in neighboring Pennsylvania restaurants over the same period. The critical assumption is parallel trends — that absent the treatment, the two groups would have experienced similar changes. DiD has been extended to staggered adoption settings (where different states adopt policies at different times), to synthetic control methods (which construct a weighted comparison group), and to event-study designs that allow visual assessment of pre-treatment trends.

**Regression discontinuity** (RD) exploits sharp eligibility thresholds to identify causal effects. When a policy assigns treatment based on whether a running variable crosses a cutoff — financial aid eligibility at a GPA threshold, retirement benefits at age 62, unemployment insurance extension at a duration cutoff — units just above and just below the cutoff are nearly identical except for treatment status, creating a local quasi-experiment. RD designs are compelling because the identification is visual: if the outcome shows a discrete jump at the cutoff, the effect is apparent in a simple graph. In labor economics, RD has been used to study the effects of unemployment insurance duration on job search (using duration cutoffs), the impact of disability insurance on labor force participation (using age-based eligibility rules), and the returns to attending elite universities (using admission score thresholds).

**Instrumental variables** (IV) address endogeneity by finding a source of variation in the endogenous variable that is uncorrelated with the error term. The instrument must be relevant (correlated with the endogenous variable) and valid (affecting the outcome only through the endogenous variable — the exclusion restriction). Angrist and Krueger's (1991) quarter-of-birth instrument for schooling illustrates the logic: compulsory schooling laws interact with school-entry cutoff dates to create exogenous variation in how much schooling people get. Those born in Q1 can drop out with slightly less schooling than those born in Q4, and this birth-timing variation is plausibly unrelated to ability or other earnings determinants. IV estimates identify a local average treatment effect (LATE) — the causal effect for "compliers" whose behavior is changed by the instrument — which may differ from the average treatment effect in the population.

**Natural experiments** is the broader category encompassing any situation where institutional features, policy changes, or historical accidents create quasi-random variation that can be exploited for causal inference. The Vietnam draft lottery (random draft numbers used to study the effect of military service on earnings), German reunification (an exogenous shock to labor markets used to study convergence), and immigration shocks from political events (the Mariel boatlift used by Card to study the effect of immigration on native wages) are all natural experiments that provided credible identification for questions that seemed intractable with observational data alone. The common thread is opportunistic identification: rather than designing an experiment, the researcher recognizes that history or institutions have created one.
