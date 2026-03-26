---
id: vector-autoregression-var
title: Vector Autoregression (VAR) Models
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: time-series-cross-section
  type: hard
- id: causal-inference-observational-data
  type: soft
- id: eigenvalues-and-eigenvectors
  type: hard
- id: matrix-operations
  type: hard
- id: systems-of-first-order-linear-odes
  type: soft
- id: eigenvalues-and-eigenvectors
  type: soft
- id: panel-data-fixed-effects
  type: soft
- id: count-data-regression-models
  type: soft
- id: conversation-analysis-social-order
  type: soft
- id: cost-effectiveness-analysis
  type: soft
- id: critical-discourse-analysis
  type: soft
- id: difference-in-differences-estimation-research-methods-social-science
  type: soft
- id: field-experiments-real-world
  type: soft
- id: focus-group-research
  type: soft
- id: instrumental-variables-methods
  type: soft
- id: intersectional-analysis-methods
  type: soft
- id: longitudinal-qualitative-research
  type: soft
- id: mediation-analysis-social
  type: soft
- id: meta-analysis-systematic-review
  type: soft
- id: missing-data-mechanisms-imputation
  type: soft
- id: moderation-analysis-interaction
  type: soft
- id: narrative-analysis-methods
  type: soft
- id: operationalization-construct-validity
  type: soft
- id: positivism-interpretivism-paradigm-debate
  type: soft
- id: qualitative-comparative-analysis
  type: soft
- id: rapid-ethnography-methods
  type: soft
- id: sensitivity-analysis-unmeasured-confounding
  type: soft
- id: triangulation-method-convergence
  type: soft
builds-toward:
- structural-var-models
- impulse-response-analysis
tags:
- time-series
- multivariate
- dynamics
- causal
stage: expert
status: validated
---
# Vector Autoregression (VAR) Models

## Core Idea
Vector autoregression models capture dynamic interdependencies among multiple time series. Each variable is regressed on its own past values and the past values of all other variables. VARs reveal which variables Granger-cause others, and impulse-response functions show how a shock to one variable propagates through the system. VARs are used to study feedback loops in economic systems, policy dynamics, and social processes.

## Questions

```yaml
- question: "A VAR study finds that past values of central bank interest rates significantly improve predictions of future GDP growth, even after controlling for past GDP growth. This finding is best described as:"
  type: multiple-choice
  options:
    - "Proof that interest rates cause GDP growth via monetary transmission mechanisms"
    - "Evidence that interest rates Granger-cause GDP growth — a statistical finding about predictive precedence, not structural causation"
    - "Evidence that GDP growth Granger-causes interest rates, since the central bank responds to economic conditions"
    - "A spurious correlation that requires an instrumental variable to interpret causally"
  answer: 1
  explanation: "Granger causality is a statistical test: does X's past predict Y beyond what Y's own past already predicts? Finding that it does establishes predictive precedence — not structural causation. It can still be confounded by omitted variables (e.g., a third factor that drives both interest rates and growth in sequence). Structural causation requires additional identification assumptions beyond what Granger testing provides."

- question: "When computing impulse response functions from a VAR model, researchers must orthogonalize the shocks (e.g., via Cholesky decomposition). The ordering of variables matters because:"
  type: multiple-choice
  options:
    - "Different orderings change the number of lag periods estimated in the model"
    - "Different variable orderings produce different orthogonalized shocks and therefore different impulse responses, because the ordering encodes assumptions about which variables respond contemporaneously to which shocks"
    - "Cholesky decomposition is only numerically stable for specific variable orderings"
    - "The ordering determines which variables are treated as exogenous versus endogenous in the system"
  answer: 1
  explanation: "In a VAR, all variables are endogenous and shocks are correlated. To trace how a shock to one variable propagates, the shocks must be separated — but there is no unique way to do this without imposing structure. Cholesky decomposition achieves orthogonalization by recursively assigning shocks in order: the first variable's shock affects all others contemporaneously, but the second variable's shock does not affect the first contemporaneously, and so on. Different orderings produce different impulse responses, each encoding different causal assumptions. This is why ordering decisions require theoretical justification and why structural VAR extends the framework."

- question: "A key advantage of VAR models over single-equation AR models is that VAR explicitly captures bidirectional and feedback relationships — where variable A influences variable B and variable B influences variable A over time."
  type: true-false
  answer: true
  explanation: "This is the central motivation for VAR. A single-equation AR model for GDP growth uses only past GDP growth to predict future GDP growth, missing the role of unemployment, inflation, and interest rates in the dynamic system. VAR estimates a system of equations simultaneously, allowing GDP to affect unemployment and unemployment to affect GDP in subsequent periods — the feedback loops that characterize real economic dynamics. The 'vector' in VAR refers to the vector of variables evolving jointly."

- question: "Granger causality, as tested in a VAR model, establishes that one variable produces structural changes in another — making it equivalent to evidence from a randomized experiment for observational time series."
  type: true-false
  answer: false
  explanation: "Granger causality is a statistical criterion about predictive precedence: does X's past improve predictions of Y beyond Y's own past? This can be confounded by omitted variables — a third factor Z that drives X first and Y later would make X appear to Granger-cause Y even with no direct causal link. Randomized experiments establish structural causation by controlling assignment; Granger tests cannot replicate this because time series are observational. Structural VAR models attempt to recover causal identification by imposing theoretically motivated restrictions."

- question: "Why does orthogonalizing VAR shocks via Cholesky decomposition require researchers to make causal assumptions about the ordering of variables, and what problem does this create for interpreting results?"
  type: short-answer
  answer: "In a VAR, the error terms across equations are typically correlated — a surprise increase in GDP and a surprise drop in unemployment may occur together because both respond to some common contemporaneous factor. To isolate the effect of a shock to one variable, you must attribute the correlated variation to one equation first. Cholesky decomposition does this by assuming a recursive causal order: the first-ordered variable can affect all others contemporaneously, while the last-ordered variable only affects others with a lag. This ordering is a causal assumption, not a statistical one. The problem: different orderings produce different impulse responses, and there is often no consensus on the 'correct' ordering, making results sensitive to a researcher's untestable theoretical assumptions."
  explanation: "This is why the move from reduced-form VAR to structural VAR is necessary for causal interpretation. Structural VAR imposes restrictions grounded in economic theory (e.g., monetary policy cannot affect output within the same quarter) to identify orthogonal structural shocks. The Cholesky problem reveals a general truth: recovering causal dynamics from observational time series always requires imposing identifying assumptions — the question is whether those assumptions are explicit and theoretically justified."
```

## Explainer

From your time series prerequisites, you know how to model a single variable — say, GDP growth — using its own past values via an autoregressive (AR) model. But social and economic systems rarely evolve in isolation. GDP growth, unemployment, and inflation interact dynamically: a rise in unemployment may suppress inflation, which may prompt a policy rate cut, which may stimulate growth, which reduces unemployment. A **Vector Autoregression (VAR)** model handles this by running a system of AR equations simultaneously — one for each variable — where every variable in the system can depend on its own lags and the lags of every other variable.

The matrix representation connects directly to your linear algebra prerequisites. If you have k variables and p lags, the VAR(p) model is written as **y_t = A_1 y_{t-1} + A_2 y_{t-2} + ... + A_p y_{t-p} + ε_t**, where **y_t** is a k×1 vector of observations and each **A_i** is a k×k coefficient matrix. The eigenvalues of the companion matrix determine stability — for the system to be stationary (not explosive), all eigenvalues must lie inside the unit circle. This is exactly the stability analysis from your dynamical systems background applied to empirical data.

**Granger causality** is one of the key tools VAR provides. Variable X Granger-causes Y if past values of X help predict Y beyond what Y's own past already predicts — tested by whether the coefficients on lagged X in the Y equation are jointly significant. This is a statistical definition of predictive precedence, not philosophical causality, but it is a principled way to detect directional temporal relationships in observational data. From your causal inference prerequisites, you know this is not the same as establishing structural causation — Granger causality can be confounded by omitted variables.

**Impulse response functions (IRFs)** translate VAR coefficients into something interpretable: they trace how a one-unit shock to one variable ripples through the system over time. If you hit GDP with an unexpected positive shock, the IRF shows the predicted trajectory of GDP, unemployment, and inflation over the next several periods. The shape of these paths — does unemployment respond quickly or slowly? does the effect persist or decay? — is typically what researchers report. Because all variables affect all others, the shocks must be **orthogonalized** (usually via Cholesky decomposition) to separate their effects, which requires ordering decisions that encode causal assumptions. This is where the transition to structural VAR models begins.
