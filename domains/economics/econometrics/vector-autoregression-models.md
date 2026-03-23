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
status: validated
---

# Vector Autoregression (VAR) Models and Impulse Responses

## Core Idea
A VAR(p) model extends AR to multiple series where each variable depends on its own and all other variables' lags. VARs capture dynamic cross-variable relationships without imposing strong identifying assumptions. Impulse responses show shock propagation; forecast error variance decomposition quantifies each variable's contribution to forecast error in others.

## Questions

```yaml
- question: "An economist builds a VAR with GDP growth and inflation and reports: 'A shock to GDP has no contemporaneous effect on inflation, but a shock to inflation immediately affects GDP.' What best explains this asymmetric result?"
  type: multiple-choice
  options:
    - "This follows necessarily from the OLS estimation of the VAR equations"
    - "This reflects a specific Cholesky ordering where GDP was listed first, imposing the assumption that GDP shocks are contemporaneously exogenous to inflation"
    - "This is the standard empirical finding confirmed by all identification strategies"
    - "This means GDP growth Granger-causes inflation but not vice versa"
  answer: 1
  explanation: "In a Cholesky-identified VAR, the variable listed first is assumed to respond only to its own shock contemporaneously — shocks to variables listed later cannot affect it in the same period. By placing GDP first, the researcher implicitly assumes GDP does not respond to inflation shocks within a period, while inflation can respond to GDP shocks. Swapping the order would reverse this asymmetry and change all impulse responses. The result is not a neutral mathematical output — it is a consequence of an identification assumption."

- question: "In a VAR(1) model, the stability condition requires:"
  type: multiple-choice
  options:
    - "All individual autoregressive coefficients to be less than 1 in absolute value"
    - "All eigenvalues of the companion matrix to have modulus less than 1"
    - "The residuals of all equations to be uncorrelated with each other"
    - "The number of lags p to equal the number of variables in the system"
  answer: 1
  explanation: "Stability in a multivariate system is not captured by individual coefficient bounds — it requires that all eigenvalues of the companion (block) matrix lie strictly inside the unit circle. This generalizes the univariate AR stability condition |ρ| < 1 to the matrix setting. If any eigenvalue has modulus ≥ 1, the system is explosive — shocks grow without bound rather than damping out. Option A is a sufficient condition only in special cases, not generally."

- question: "Swapping the order of variables in a Cholesky-identified VAR changes the impulse response functions because the ordering imposes assumptions about which variables can react to which shocks contemporaneously."
  type: true-false
  answer: true
  explanation: "The Cholesky decomposition assigns all contemporaneous correlation to the variable listed first — it cannot respond to variables below it in the same period, while variables below it can respond to it immediately. Reordering changes which variable 'causes' contemporaneous movements in others and thus changes the IRFs. This non-neutrality is why sophisticated identification strategies use economic theory (long-run restrictions, sign restrictions) rather than relying on an arbitrary ordering."

- question: "Forecast error variance decomposition (FEVD) shows that at all forecast horizons, a variable's forecast uncertainty is dominated by its own past shocks — cross-variable contributions remain small and stable over time."
  type: true-false
  answer: false
  explanation: "Cross-variable contributions to FEVD typically grow with the forecast horizon. At short horizons (e.g., one quarter ahead), most of a variable's forecast uncertainty comes from its own shocks because there has been little time for other variables' shocks to propagate through the system. As the horizon extends, the dynamic transmission channels activate and other variables' shocks account for increasing shares of forecast error variance. The claim that cross-variable contributions remain small and stable conflates short-run with long-run dynamics."

- question: "Explain why impulse response functions from a reduced-form VAR cannot be interpreted causally without an identification strategy, and what the Cholesky ordering assumes."
  type: short-answer
  answer: "Reduced-form VAR residuals are typically correlated across equations — a simultaneous shock to GDP and inflation makes it impossible to say which caused which contemporaneous movement. To compute IRFs, you need to decompose this joint shock into orthogonal components and assign causal direction. The Cholesky ordering assumes a triangular structure: the variable listed first is hit by a 'pure' own shock that cannot be caused by variables below it in the same period, while variables lower in the ordering can respond contemporaneously to those above. This is an identifying assumption about causal priority, not a statistical result."
  explanation: "Without identification, an 'inflation shock' in a VAR is actually a mixture of true inflation shocks and all other contemporaneously correlated shocks. The Cholesky ordering is one way to resolve this ambiguity by imposing a recursive causal structure. Its validity depends entirely on whether the causal ordering chosen matches reality — which is an economic judgment, not a statistical one. This is why economists say 'the VAR is identified up to an orthogonalization choice.'"
```

## Explainer

You already know that an AR(p) model lets a variable predict its own future values using its own past — GDP this quarter depends on GDP last quarter and the quarter before. The **VAR(p)** model is the natural multivariate generalization: let each variable in a system depend on its own lags *and* the lags of all other variables in the system. For a two-variable system with GDP growth (y₁) and inflation (y₂), a VAR(1) writes: y₁,t = α₁₀ + α₁₁y₁,t₋₁ + α₁₂y₂,t₋₁ + ε₁,t and y₂,t = α₂₀ + α₂₁y₁,t₋₁ + α₂₂y₂,t₋₁ + ε₂,t. The off-diagonal coefficients (α₁₂ and α₂₁) capture cross-variable dynamics: does last quarter's inflation predict this quarter's GDP growth? Each equation is a standard OLS regression, so estimation is straightforward once you choose the lag length p (typically selected by AIC or BIC).

The real power of VARs emerges through **impulse response functions (IRFs)**. An IRF traces the effect of a one-standard-deviation shock to one variable on all variables in the system over subsequent periods. A monetary policy shock — a surprise interest rate increase — reverberates through output, prices, and exchange rates in ways that play out over quarters. The IRF lets you plot these propagation paths. Your eigenvalue knowledge is critical here: the stability of the VAR requires that all eigenvalues of the companion matrix lie inside the unit circle. If any eigenvalue has modulus ≥ 1, the system explodes rather than settling back to equilibrium — the same stationarity requirement you encountered in the univariate AR model, now generalized to a matrix condition.

The deeper challenge with VARs is **identification**. The residuals ε₁,t and ε₂,t are typically correlated — a simultaneous GDP shock and inflation shock may be triggered by the same underlying event. To interpret impulse responses causally, you need to assign the correlation to one side or the other — to say which shock causes which contemporaneous movement. The most common approach is **Cholesky ordering**: variables listed first are assumed to respond only to their own shock contemporaneously, while variables listed later can respond immediately to shocks above them in the ordering. This ordering imposes a triangular structure on the impact matrix and is not neutral — swapping the order of GDP and inflation changes the impulse responses. More sophisticated identification uses economic theory (long-run restrictions, sign restrictions, or external instruments) to achieve identification without imposing an arbitrary ordering.

**Forecast error variance decomposition (FEVD)** complements IRFs by answering: at a given forecast horizon, what fraction of the uncertainty in variable i is attributable to shocks in variable j? At short horizons, most of a variable's forecast error variance is typically explained by its own shocks. As the horizon extends, cross-variable contributions grow. In a monetary VAR, the FEVD might show that monetary policy shocks explain only 5% of output variance at one quarter but 20% at eight quarters — the dynamics take time to work through. Together, IRFs and FEVDs give a rich picture of how shocks propagate and linger in a dynamic multivariate system, making VARs the workhorse tool for empirical macroeconomics.
