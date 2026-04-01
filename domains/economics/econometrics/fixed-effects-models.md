---
id: fixed-effects-models
title: Fixed Effects Models
domain: economics
course: econometrics
prerequisites:
- id: panel-data-basics
  type: hard
- id: dummy-variables-regression
  type: hard
- id: linear-transformations
  type: hard
builds-toward:
- random-effects-models
- difference-in-differences
tags:
- fixed-effects
- within-estimator
- demeaning
- panel
stage: formal-systems
status: validated
---

# Fixed Effects Models

## Core Idea
The fixed effects (FE) estimator eliminates time-invariant unobserved heterogeneity by transforming the data so that unit means are removed — the 'within' transformation: ÿ_it = y_it − ȳᵢ. Regressing demeaned outcomes on demeaned regressors uses only within-unit variation over time, making α_i irrelevant. Equivalently, FE adds a dummy variable for each unit. Because FE uses only within-unit variation, it cannot estimate the effects of time-invariant regressors (e.g., gender, race). Two-way fixed effects adds time fixed effects, controlling for aggregate shocks common to all units.

## How It's Best Learned
Manually demean a small panel dataset and run OLS on the demeaned data — verify the results match software FE output. Then try including a time-invariant variable and see that it perfectly collinears with unit dummies.

## Common Misconceptions
- Fixed effects do not eliminate all bias — if the regressor changes within units for endogenous reasons (e.g., wage increases causing workers to move), FE still produces biased estimates.
- FE 'controls for' unobservables in the sense of absorbing them; it does not estimate them.

## Questions

```yaml
- question: "A researcher uses panel data to estimate the wage return to education with unit (person) fixed effects. She then tries to include a variable for each person's race. What happens?"
  type: multiple-choice
  options:
    - "The race variable gets a small but significant coefficient because FE controls for confounding"
    - "The race variable is perfectly collinear with the person fixed effects and drops out of the regression entirely"
    - "The FE estimator becomes inconsistent because race is endogenous"
    - "The coefficient on education becomes biased toward zero because race absorbs some of its variation"
  answer: 1
  explanation: "Race is a time-invariant characteristic — it doesn't change within a person over time. Fixed effects work by demeaning each person's data, which removes everything that is constant within that person. A time-invariant variable like race is constant within each person, so after demeaning it becomes a column of zeros — perfectly collinear with the unit dummies. This is a fundamental limitation of FE: you cannot estimate the level effect of any variable that has no within-unit variation."

- question: "A researcher studies how investment affects firm productivity using a firm fixed effects model. She argues: 'Since firms that are already highly productive tend to invest more, this within-firm correlation makes FE estimates biased.' Is she correct?"
  type: multiple-choice
  options:
    - "No — FE removes all endogeneity by controlling for firm-level unobservables"
    - "No — within-firm variation is by definition exogenous because firm identity is held constant"
    - "Yes — FE only removes time-invariant bias; if productivity shocks cause within-firm investment changes, FE estimates are still biased"
    - "Yes — FE should not be used when the outcome (productivity) causes the regressor (investment)"
  answer: 2
  explanation: "The researcher is correct. Fixed effects removes bias from time-invariant unobserved confounders (like a firm's permanent management quality), but it does not remove bias from time-varying confounders. If a firm experiences a positive productivity shock and responds by increasing investment within the same period, the within-firm variation in investment is correlated with the within-firm error. FE cannot solve this — it is a specific solution to a specific problem, not a general cure for endogeneity."

- question: "The within transformation (subtracting each unit's time-mean from every observation) eliminates time-invariant unobserved heterogeneity because any characteristic that doesn't change over time becomes zero after demeaning."
  type: true-false
  answer: true
  explanation: "This is the core insight behind fixed effects. If a unit's unobserved characteristic α_i is constant over time, then subtracting the unit's mean (ȳ_i = α_i + other terms) from each observation removes α_i exactly. What remains is only within-unit variation over time. This is mathematically equivalent to including a dummy variable for every unit — the dummies soak up the permanent unit-level differences."

- question: "Fixed effects models eliminate most forms of omitted variable bias in panel data, which is why they are the preferred estimator whenever panel data is available."
  type: true-false
  answer: false
  explanation: "Fixed effects eliminates only time-invariant omitted variable bias. If unobserved confounders change over time within units — for example, if workers who receive wage increases are simultaneously experiencing changes in unobserved motivation — FE estimates remain biased. Two-way FE additionally controls for common time shocks, but time-varying unit-level confounders still require additional strategies (instrumental variables, DiD, etc.). Choosing FE over random effects also involves tradeoffs in efficiency and the Hausman test."

- question: "Explain why a fixed effects regression cannot estimate the coefficient on a time-invariant variable such as gender or country of origin."
  type: short-answer
  answer: "Fixed effects works by demeaning each unit's observations — subtracting the unit's time-average from every period's value. A time-invariant variable like gender has the same value in every period for a given unit, so after demeaning it becomes identically zero for all observations. A column of zeros carries no information and is perfectly collinear with the unit fixed effects (which are also constant within each unit). The estimator literally cannot distinguish the effect of gender from the unit's permanent fixed effect — they are mathematically inseparable."
  explanation: "The intuition is that FE only uses variation within units over time. Since gender never varies within a person, there is no within-unit variation to exploit. This is the price of the FE strategy: you gain protection against time-invariant confounders, but you lose the ability to estimate time-invariant effects. If estimating the effect of time-invariant variables is the goal, you need a different strategy (random effects or between estimator), with the corresponding tradeoffs in bias and efficiency."
```

## Explainer

The fundamental problem in observational social science is that units — people, firms, countries — differ in ways we cannot measure. A student's innate ability, a firm's management culture, a country's institutional quality: these unobserved characteristics correlate with both the treatment variable (education spending, investment policy, governance reform) and the outcome (test scores, productivity, growth). Standard OLS, which you know from the normal linear regression model, will attribute to the observed regressor variation that actually comes from these hidden differences. The **fixed effects estimator** sidesteps this problem by discarding all variation *between* units and exploiting only variation *within* units over time.

The mechanics follow directly from your work on panel data and dummy variables. You can think of fixed effects as adding a dummy variable for every unit in the panel. Each dummy absorbs that unit's permanent characteristics — its average level of the outcome that can't be explained by observed regressors. Equivalently (and computationally more efficient), you **demean** the data: subtract each unit's time-average from every observation. This "within transformation" leaves only the within-unit deviations. The coefficient on regressor X is then estimated purely from periods when X changed for a given unit — not from comparing units with high X to units with low X. Because unobserved unit heterogeneity (α_i) is constant within a unit, demeaning removes it exactly.

The price of this power is the loss of cross-sectional variation. If a variable never changes within a unit — gender, country of birth, founding year of a firm — it is perfectly collinear with the unit fixed effects and drops out entirely. You cannot estimate the level effect of something that doesn't vary over time for any unit. Two-way fixed effects extend the model by also demeaning across time periods, absorbing common shocks that affect all units simultaneously (like a recession or a global commodity price spike). This leaves only variation that is both within-unit and within-time-period — the residual after removing unit means and time means.

The Common Misconceptions section flags the most important caveat: fixed effects remove *time-invariant* bias, but not all bias. If the regressor changes within a unit for reasons that are themselves correlated with the error — for instance, firms that are doing well choose to invest more, so investment correlates with productivity shocks — within-unit variation is also contaminated. Fixed effects are not a magic cure; they are a specific solution to a specific form of omitted variable bias. They work when the unobserved confounders are stable attributes of the unit. When confounders change over time, you need additional strategies like instrumental variables or difference-in-differences designs that build on the fixed effects logic.
