---
id: simultaneous-equations-models
title: Simultaneous Equations Models and Identification
domain: economics
course: econometrics
prerequisites:
- id: endogeneity
  type: hard
- id: instrumental-variables
  type: hard
- id: two-stage-least-squares
  type: hard
- id: reduced-form-equations
  type: soft
builds-toward: []
tags:
- simultaneous equations
- simultaneity bias
- identification
- order condition
- rank condition
- supply and demand
- structural model
stage: formal-systems
status: validated
---

# Simultaneous Equations Models and Identification

## Core Idea
A simultaneous equations model (SEM) has several structural equations whose dependent variables are determined jointly, as price and quantity are set by supply and demand together. Each endogenous variable is correlated with the errors of the equations it appears in, so OLS on one equation is biased and inconsistent. An equation can be estimated only if it is identified: some exogenous variable that is excluded from it shifts the other equation. The order condition requires at least as many excluded exogenous variables as included endogenous explanatory variables; the rank condition requires that those excluded variables actually appear, with nonzero coefficients, elsewhere in the system. Identified equations are estimated by two-stage least squares.

## How It's Best Learned
Draw a supply-and-demand diagram where both curves shift randomly, and show that the observed price-quantity points trace out neither curve. Then add a variable that shifts only supply, such as weather in a crop market, and show that its movements trace out the demand curve. Writing the two structural equations and counting excluded variables for each turns this picture into the order condition.

## Common Misconceptions
- Regressing quantity on price with market data estimates the demand curve. (Observed points mix supply and demand shifts, so the OLS slope estimates neither curve without an identifying variable.)
- An equation is identified if it has at least one exogenous variable. (What matters is an exogenous variable excluded from that equation and included in another; included exogenous variables do not help identify it.)
- Satisfying the order condition guarantees identification. (The order condition is only necessary; the rank condition, which requires the excluded variable to have a nonzero coefficient in the other equation, is necessary and sufficient.)

## Questions

```yaml
- question: "A model of the wheat market has supply q = a₁p + b₁·rain + u₁ and demand q = a₂p + b₂·income + u₂. Which variable identifies the demand equation?"
  type: multiple-choice
  options: ["Income, because it appears in the demand equation", "Rain, because it shifts supply and is excluded from demand", "Price, because it appears in both equations", "Neither; demand cannot be identified"]
  answer: 1
  explanation: "To trace out the demand curve you need something that moves supply while leaving demand fixed. Rain is excluded from demand and appears in supply, so it serves as the instrument for price in the demand equation. Income likewise identifies the supply equation."
- question: "An equation with two endogenous explanatory variables and one excluded exogenous variable satisfies the order condition."
  type: true-false
  answer: false
  explanation: "The order condition requires at least as many excluded exogenous variables as included endogenous explanatory variables. One excluded variable cannot instrument for two endogenous regressors, so the equation is underidentified."
- question: "Why is OLS biased when applied to the demand equation in a supply-and-demand system?"
  type: multiple-choice
  options: ["Because quantity is measured with error", "Because a demand shock u₂ shifts the equilibrium price, so price is correlated with u₂", "Because price is always nonstationary", "Because the errors are heteroskedastic"]
  answer: 1
  explanation: "When demand rises unexpectedly, both price and quantity rise. Price therefore moves with the demand error, which violates the OLS assumption that regressors are uncorrelated with the error. This is simultaneity bias."
- question: "State the difference between the order condition and the rank condition for identifying an equation in a two-equation system."
  type: short-answer
  answer: "The order condition counts variables: the equation must exclude at least as many exogenous variables as it includes endogenous explanatory variables. The rank condition requires more: at least one of the excluded exogenous variables must actually appear with a nonzero coefficient in the other equation. Order is necessary; rank is necessary and sufficient."
  explanation: "An excluded variable that does not really shift the other equation cannot serve as an instrument, even though it passes the counting test."
```

## Explainer
From your study of endogeneity you know that simultaneity is one way a regressor becomes correlated with the error. Simultaneous equations models make that idea systematic. The classic case is a market. Supply and demand are two structural equations, each describing the behavior of one side, and price and quantity are both determined by where they meet.

Write the model as supply, q = α₁p + β₁z₁ + u₁, and demand, q = α₂p + β₂z₂ + u₂. Here p and q are **endogenous**, determined inside the system. The variables z₁ and z₂ are **exogenous**, determined outside it, such as rainfall for a crop and consumer income. Solve the two equations together and you get the reduced form: p and q each written as functions of z₁, z₂, and both errors. Because p depends on u₂, OLS on the demand equation is inconsistent. The same holds for supply.

This problem was recognized early. Elmer Working's 1927 article "What Do Statistical 'Demand Curves' Show?" explained that price-quantity data trace out a cloud of intersections. Trygve Haavelmo's 1943 work on simultaneous equations made simultaneity bias a central topic in econometrics.

The solution is **identification**. To estimate the demand curve, you need movements in supply that leave demand unchanged. Rainfall does that: it shifts supply, is excluded from demand, and so traces out points along the demand curve. Rainfall serves as the instrument for price in the demand equation. Income, excluded from supply, plays the same role for the supply equation.

Two conditions formalize this. The **order condition** says an equation can be identified only if the number of exogenous variables excluded from it is at least the number of endogenous explanatory variables it includes. It is a counting rule and is necessary, but not enough. The **rank condition** adds that the excluded variables must really matter in the other equation. If rainfall's true coefficient in supply were zero, it would pass the count but fail to identify demand. An equation with exactly enough instruments is just identified; one with more is overidentified, and the extra restrictions can be tested.

Once identified, each equation is estimated by two-stage least squares, using all exogenous variables in the system as instruments. Applications go beyond markets: labor supply and wage offers, crime and police spending, and money demand and interest rates have all been modeled this way.
