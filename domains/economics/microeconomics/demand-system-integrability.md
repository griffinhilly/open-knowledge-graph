---
id: demand-system-integrability
title: Demand Systems and Integrability Conditions
domain: economics
course: microeconomics
prerequisites:
- id: duality-consumer-preferences
  type: hard
- id: integrability-revealed-preference
  type: hard
- id: preference-rationality-consistent-choices
  type: soft
builds-toward:
- weak-strong-axiom-revealed-preference
tags:
- demand
- integrability
- consistency
- rationality
stage: advanced
status: validated
---
# Demand Systems and Integrability Conditions

## Core Idea
Not all demand functions can come from maximizing a utility function; they must satisfy integrability conditions (Slutsky symmetry, negative semi-definiteness). These conditions ensure the demand system is consistent with optimization. Testing whether observed demand satisfies integrability reveals whether consumer behavior is rational without knowing preferences.

## Questions

```yaml
- question: "An economist estimates a demand system from household survey data and finds that the compensated cross-price effect of good A on good B differs from the compensated cross-price effect of good B on good A. What does this imply?"
  type: multiple-choice
  options:
    - "The consumers have unusual preferences and need a more flexible utility function"
    - "The demand system fails Slutsky symmetry and cannot be rationalized by any utility function"
    - "The estimation is merely imprecise and the difference is likely sampling error"
    - "The consumers violate budget balance but could still be utility-maximizing"
  answer: 1
  explanation: "Slutsky symmetry — that the (i,j) and (j,i) entries of the Slutsky matrix are equal — is a necessary condition for a demand system to be consistent with utility maximization. If this condition fails, no utility function exists that could generate the observed demands, regardless of how flexible that function is. The observed asymmetry is direct evidence against rationality as utility maximization, not a sign of unusual preferences or estimation noise."

- question: "Which pair of conditions must the Slutsky matrix satisfy for a demand system to be integrable?"
  type: multiple-choice
  options:
    - "Symmetry and positive definiteness"
    - "Symmetry and negative semi-definiteness"
    - "Homogeneity of degree zero and negative semi-definiteness"
    - "Symmetry alone — semi-definiteness follows automatically from symmetry"
  answer: 1
  explanation: "Integrability requires both Slutsky symmetry (the matrix equals its transpose) and negative semi-definiteness (no positive eigenvalues, implying compensated own-price effects are non-positive). Symmetry alone is not sufficient — a symmetric matrix can have positive eigenvalues. Both conditions are independently necessary and jointly sufficient, flowing from the properties of the expenditure function derived under utility minimization."

- question: "Slutsky symmetry is an observable implication of rationality that can be tested using demand data without ever directly observing a consumer's preferences."
  type: true-false
  answer: true
  explanation: "This is precisely the power of integrability conditions. Slutsky symmetry — that compensated cross-price effects are equal across goods — is a restriction on the structure of observable demand, not on the shape of an unobservable utility function. Economists can estimate the Slutsky matrix from expenditure survey data and test symmetry statistically without specifying or observing preferences. It translates the abstract axiom of rationality into a falsifiable empirical claim."

- question: "If a demand system satisfies Slutsky symmetry, it is guaranteed to be consistent with utility maximization."
  type: true-false
  answer: false
  explanation: "Symmetry is necessary but not sufficient. The Slutsky matrix must also be negative semi-definite — meaning compensated own-price effects are non-positive. A symmetric Slutsky matrix could still have a positive eigenvalue, which would violate the requirement that holding utility constant, a price increase cannot cause a consumer to buy more of that good. Both conditions together are required to guarantee integrability."

- question: "Why do integrability conditions matter for empirical demand analysis, and what failure do they detect?"
  type: short-answer
  answer: "Integrability conditions (Slutsky symmetry and negative semi-definiteness) determine whether an estimated demand system is consistent with utility-maximizing behavior. If an estimated Slutsky matrix is asymmetric or has a positive eigenvalue, the data reject the rationality hypothesis — no coherent optimization problem could generate those demands. This lets researchers test rationality from observable demand data without assuming a specific utility function."
  explanation: "The key insight is that integrability conditions bridge theory and data: they translate the abstract requirement of 'rational optimization' into testable restrictions on the structure of demand. Without these conditions, any demand function could claim to be rational. With them, rationality makes falsifiable predictions about the relationship between compensated cross-price effects — predictions that can be checked with household expenditure surveys."
```

## Explainer

From your work on duality, you know that a utility-maximizing consumer generates demand through two equivalent routes: direct utility maximization (Marshallian demands) and expenditure minimization (Hicksian demands), linked by the Slutsky equation. The **integrability question** inverts this: given an observed demand function x(p, w), does there exist a utility function that rationalizes it? The answer is: not always. Integrability conditions are the set of restrictions that a demand function must satisfy to be consistent with utility maximization.

The key object is the **Slutsky matrix** — the matrix of compensated price effects, with entry (i, j) equal to ∂x_i/∂p_j + x_j·(∂x_i/∂w). For demand generated by utility maximization, this matrix must satisfy two conditions. First, **Slutsky symmetry**: the (i, j) entry must equal the (j, i) entry, meaning the compensated cross-price effect of good j on good i equals the compensated cross-price effect of good i on good j. Second, **negative semi-definiteness**: the matrix can have no positive eigenvalues, meaning compensated own-price effects are non-positive. Both conditions follow directly from the properties of the expenditure function you derived in your duality study.

These conditions have concrete economic content. Symmetry says that how coffee consumption responds to a compensated increase in tea prices must equal how tea consumption responds to a compensated increase in coffee prices. This is an observable, testable implication of rationality — not an assumption about any particular preference shape, but a structural requirement of optimization itself. Negative semi-definiteness says that compensated demand slopes downward: hold utility constant, raise a price, and the consumer buys no more of that good.

The power of integrability conditions is that they let you test rationality from demand data without ever observing preferences directly. If you estimate a demand system from household expenditure surveys and find that the Slutsky matrix is asymmetric or has a positive eigenvalue, you have evidence against utility-maximizing behavior — without specifying what utility function the consumer "should" have. This is the bridge between the axiomatic revealed preference framework you studied and empirical demand analysis: integrability conditions are how you check whether a system of observed demand functions is consistent with a coherent underlying optimization problem.
