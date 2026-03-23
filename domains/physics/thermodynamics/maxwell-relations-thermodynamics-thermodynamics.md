---
id: maxwell-relations-thermodynamics-thermodynamics
title: Maxwell Relations
domain: physics
course: thermodynamics
prerequisites:
- id: legendre-transformations-potentials
  type: hard
- id: helmholtz-free-energy
  type: soft
builds-toward:
- thermodynamic-availability-exergy
tags:
- potentials
- relations
- measurable-properties
stage: advanced
status: validated
---

# Maxwell Relations

## Core Idea
Maxwell relations are a set of equations derived from the equality of mixed partial derivatives of thermodynamic potentials; for example, (∂T/∂V)_S = -(∂P/∂S)_V. They provide powerful constraints linking different measurable properties (like pressure, volume, temperature, entropy) and allow the calculation of hard-to-measure quantities from easily measured ones. Maxwell relations emerge naturally from the exactness of thermodynamic differentials and are a cornerstone of experimental thermodynamics.

## How It's Best Learned
Derive Maxwell relations from the four main potentials (U, H, F, G). Practice using them to express hard-to-measure derivatives in terms of easy ones.

## Common Misconceptions
- Forgetting the sign changes when reordering variables.
- Applying them to non-equilibrium states.
- Confusing the Maxwell relation from one potential with those from others.

## Explainer

From your study of Legendre transformations and thermodynamic potentials, you know that the internal energy U is not the only thermodynamic potential — by performing Legendre transforms, you can construct the enthalpy H, the Helmholtz free energy F, and the Gibbs free energy G, each with its own set of natural variables. Each potential is a state function, meaning its differential is exact and path-independent. **Maxwell relations** are the powerful set of equations that fall out of this exactness via a single mathematical theorem: Schwarz's theorem on the equality of mixed partial derivatives.

The derivation is straightforward once you see the pattern. Take the Helmholtz free energy: dF = -S dT - P dV. This tells you that (dF/dT)_V = -S and (dF/dV)_T = -P. Because F is a state function, its differential is exact, so the mixed second partial derivatives must be equal: d(-S)/dV at constant T equals d(-P)/dT at constant V. This gives **(dS/dV)_T = (dP/dT)_V** — one of the four standard Maxwell relations. The same procedure applied to the other three potentials yields three more relations: from U (natural variables S, V), (dT/dV)_S = -(dP/dS)_V; from H (natural variables S, P), (dT/dP)_S = (dV/dS)_P; and from G (natural variables T, P), (dS/dP)_T = -(dV/dT)_P. Each relation equates a different pair of partial derivatives, and each belongs to a specific potential with specific natural variables.

The practical utility is immediate and profound. Entropy cannot be read directly from any instrument — there is no "entropy meter." But (dS/dV)_T = (dP/dT)_V converts an unmeasurable entropy derivative into a pressure-temperature measurement at constant volume, which is routine experimental work. Similarly, (dS/dP)_T = -(dV/dT)_P expresses an entropy derivative in terms of the thermal expansion coefficient, another standard measurement. Maxwell relations systematically bridge the gap between the quantities that thermodynamic theory requires (entropy derivatives) and the quantities that laboratory equipment can deliver (pressure, volume, temperature, and their rates of change). This is why they are indispensable in experimental thermodynamics: they make the full apparatus of thermodynamic potentials experimentally accessible.

Two technical pitfalls deserve emphasis. First, **sign errors** are the most common mistake. The minus signs in the differentials of each potential (dF = -S dT - P dV, dG = -S dT + V dP) propagate into the Maxwell relations, and forgetting or misplacing a sign gives the wrong relation. The mnemonic "Good Physicists Have Studied Under Very Fine Teachers" encodes the arrangement of variables around a thermodynamic square that tracks these signs. Second, Maxwell relations only hold at **thermodynamic equilibrium** — they are derived from state functions, which are defined only for equilibrium states. Applying them to non-equilibrium processes, where thermodynamic potentials are not well-defined, produces meaningless results. Each relation also belongs to a specific potential, and confusing which relation comes from which potential — for instance, using the Helmholtz relation when the natural variables of the problem are T and P (which call for the Gibbs relation) — is another frequent source of error.

## Questions

```yaml
- question: "You want to determine (∂S/∂V)_T — how entropy changes with volume at constant temperature — but cannot measure entropy directly. Which Maxwell relation gives this in terms of measurable quantities?"
  type: multiple-choice
  options:
    - "(∂S/∂V)_T = -(∂P/∂T)_V, from the Helmholtz free energy F"
    - "(∂S/∂V)_T = (∂T/∂P)_V, from the internal energy U"
    - "(∂S/∂V)_T = (∂P/∂T)_V, from the Helmholtz free energy F"
    - "(∂S/∂V)_T = (∂V/∂T)_P, from the Gibbs free energy G"
  answer: 2
  explanation: "From the Helmholtz free energy, dF = -S dT - P dV, giving (∂F/∂T)_V = -S and (∂F/∂V)_T = -P. Schwarz's theorem equates the mixed partials: ∂(-S)/∂V|_T = ∂(-P)/∂T|_V, yielding (∂S/∂V)_T = (∂P/∂T)_V. Option A has a spurious minus sign — the most common error. The right-hand side is accessible from pressure-temperature measurements at fixed volume, converting an unmeasurable entropy derivative into a routine experimental quantity."

- question: "Why do Maxwell relations require thermodynamic potentials to have exact differentials?"
  type: multiple-choice
  options:
    - "Exact differentials guarantee that mixed partial derivatives are equal (Schwarz's theorem), enabling the cross-variable equalities Maxwell relations express"
    - "Only exact differentials can be integrated along thermodynamic paths, which is needed to derive the potentials"
    - "Non-exact differentials violate the second law of thermodynamics"
    - "Exactness ensures thermodynamic processes are reversible, which is required for entropy to be well-defined"
  answer: 0
  explanation: "Maxwell relations exploit Schwarz's theorem: for an exact differential dΦ = M dx + N dy, the mixed partial derivatives are equal: (∂M/∂y)_x = (∂N/∂x)_y. Thermodynamic potentials (U, H, F, G) are state functions, so their differentials are exact, and Schwarz's theorem applies. Heat δQ and work δW are NOT exact differentials — they are path-dependent — which is why Maxwell relations cannot be derived from them."

- question: "Maxwell relations allow the calculation of entropy derivatives — which are hard to measure — in terms of pressure, volume, and temperature derivatives, which are straightforward to measure experimentally."
  type: true-false
  answer: true
  explanation: "This is the core practical utility. Entropy cannot be read directly from an instrument, but (∂S/∂V)_T = (∂P/∂T)_V requires only pressure-temperature measurements at fixed volume. Similarly, (∂S/∂P)_T = -(∂V/∂T)_P involves thermal expansion coefficients. Maxwell relations bridge the unmeasurable (entropy derivatives) to the measurable (mechanical and thermal quantities), making them indispensable for experimental thermodynamics."

- question: "The Maxwell relation from the Helmholtz free energy and the Maxwell relation from the Gibbs free energy are different expressions of the same underlying equation and can be used interchangeably."
  type: true-false
  answer: false
  explanation: "Each thermodynamic potential has its own natural variables and its own distinct Maxwell relation, equating a different pair of partial derivatives. From F (natural variables T, V): (∂S/∂V)_T = (∂P/∂T)_V. From G (natural variables T, P): (∂S/∂P)_T = -(∂V/∂T)_P. These are different equations. Applying the wrong potential's Maxwell relation gives the wrong result — this is the misconception of confusing which relation belongs to which potential."

- question: "Explain the mathematical mechanism behind Maxwell relations and why it is useful for experimental thermodynamics."
  type: short-answer
  answer: "Maxwell relations arise from Schwarz's theorem: for any smooth state function Φ(x, y), the mixed partial derivatives are equal — ∂²Φ/∂x∂y = ∂²Φ/∂y∂x. Thermodynamic potentials are state functions with exact differentials, so Schwarz's theorem applies. For the Helmholtz free energy F, dF = -S dT - P dV gives (∂(-S)/∂V)_T = (∂(-P)/∂T)_V, yielding (∂S/∂V)_T = (∂P/∂T)_V. The practical utility: entropy changes cannot be measured directly, but (∂P/∂T)_V is obtained from standard pressure-temperature measurements at fixed volume. Maxwell relations systematically convert hard-to-measure thermodynamic derivatives into combinations of easily accessible ones."
  explanation: "The four main Maxwell relations come from the four standard potentials U, H, F, G. Each equates one entropy-involving derivative (the hard side) with a combination of P, V, T derivatives (the measurable side). Getting the signs right — which requires tracking the minus signs in dF = -S dT - P dV and similar — is the primary technical challenge in applying them."
```
