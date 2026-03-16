---
id: vector-autoregression-models
title: Vector Autoregression (VAR) Models and Impulse Responses
domain: economics
course: econometrics
prerequisites:
- id: autoregressive-ar-models
  type: hard
- id: dynamic-panel-gmm
  type: soft
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- regression-discontinuity
tags:
- time-series
- var
- multivariate
stage: formal-systems
status: draft
---

# Vector Autoregression (VAR) Models and Impulse Responses

## Core Idea
A VAR(p) model extends AR to multiple series where each variable depends on its own and all other variables' lags. VARs capture dynamic cross-variable relationships without imposing strong identifying assumptions. Impulse responses show shock propagation; forecast error variance decomposition quantifies each variable's contribution to forecast error in others.

## Explainer

You already know that an AR(p) model lets a variable predict its own future values using its own past — GDP this quarter depends on GDP last quarter and the quarter before. The **VAR(p)** model is the natural multivariate generalization: let each variable in a system depend on its own lags *and* the lags of all other variables in the system. For a two-variable system with GDP growth (y₁) and inflation (y₂), a VAR(1) writes: y₁,t = α₁₀ + α₁₁y₁,t₋₁ + α₁₂y₂,t₋₁ + ε₁,t and y₂,t = α₂₀ + α₂₁y₁,t₋₁ + α₂₂y₂,t₋₁ + ε₂,t. The off-diagonal coefficients (α₁₂ and α₂₁) capture cross-variable dynamics: does last quarter's inflation predict this quarter's GDP growth? Each equation is a standard OLS regression, so estimation is straightforward once you choose the lag length p (typically selected by AIC or BIC).

The real power of VARs emerges through **impulse response functions (IRFs)**. An IRF traces the effect of a one-standard-deviation shock to one variable on all variables in the system over subsequent periods. A monetary policy shock — a surprise interest rate increase — reverberates through output, prices, and exchange rates in ways that play out over quarters. The IRF lets you plot these propagation paths. Your eigenvalue knowledge is critical here: the stability of the VAR requires that all eigenvalues of the companion matrix lie inside the unit circle. If any eigenvalue has modulus ≥ 1, the system explodes rather than settling back to equilibrium — the same stationarity requirement you encountered in the univariate AR model, now generalized to a matrix condition.

The deeper challenge with VARs is **identification**. The residuals ε₁,t and ε₂,t are typically correlated — a simultaneous GDP shock and inflation shock may be triggered by the same underlying event. To interpret impulse responses causally, you need to assign the correlation to one side or the other — to say which shock causes which contemporaneous movement. The most common approach is **Cholesky ordering**: variables listed first are assumed to respond only to their own shock contemporaneously, while variables listed later can respond immediately to shocks above them in the ordering. This ordering imposes a triangular structure on the impact matrix and is not neutral — swapping the order of GDP and inflation changes the impulse responses. More sophisticated identification uses economic theory (long-run restrictions, sign restrictions, or external instruments) to achieve identification without imposing an arbitrary ordering.

**Forecast error variance decomposition (FEVD)** complements IRFs by answering: at a given forecast horizon, what fraction of the uncertainty in variable i is attributable to shocks in variable j? At short horizons, most of a variable's forecast error variance is typically explained by its own shocks. As the horizon extends, cross-variable contributions grow. In a monetary VAR, the FEVD might show that monetary policy shocks explain only 5% of output variance at one quarter but 20% at eight quarters — the dynamics take time to work through. Together, IRFs and FEVDs give a rich picture of how shocks propagate and linger in a dynamic multivariate system, making VARs the workhorse tool for empirical macroeconomics.
