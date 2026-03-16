---
id: legendre-transformations-potentials
title: Legendre Transformations and Thermodynamic Potentials
domain: physics
course: thermodynamics
prerequisites:
- id: exact-and-inexact-differentials
  type: hard
- id: free-energy-thermodynamic-relations
  type: soft
builds-toward:
- maxwell-relations-thermodynamics
- thermodynamic-availability-exergy
tags:
- potentials
- transformations
- natural-variables
stage: formal-systems
status: draft
---

# Legendre Transformations and Thermodynamic Potentials

## Core Idea
Legendre transformations are mathematical operations that exchange variables in a function—for example, replacing volume V with pressure P in the internal energy U(S,V) to obtain the enthalpy H(S,P). Different thermodynamic potentials (internal energy, enthalpy, Helmholtz free energy, Gibbs free energy) are Legendre transforms of each other and are useful under different experimental conditions. Choosing the right potential simplifies problem-solving by making the natural variables match the constraints of the system.

## How It's Best Learned
Construct each potential from the others via Legendre transformation. Identify which potential is natural for different experimental conditions (constant T vs constant S, constant P vs constant V).

## Common Misconceptions
- Thinking all potentials contain the same information (they do, but natural variables differ).
- Confusing the potential (e.g., H) with its differential form.
- Applying Gibbs free energy without recognizing when H and TS terms are separately meaningful.

## Explainer

From your study of exact and inexact differentials, you know that the internal energy U has a beautifully exact differential: dU = TdS − PdV. This tells you that U's **natural variables** are S (entropy) and V (volume) — these are the variables you'd hold constant to reach equilibrium if you were minimizing U. In practice, experiments are almost never run at constant entropy and constant volume. Chemists run reactions at constant pressure and temperature; engineers analyze engines at constant temperature; atmospheric scientists deal with systems at constant pressure. The Legendre transformation is the mathematical machinery for switching to the variables that actually match your experimental constraints.

The **Legendre transformation** replaces a variable with its conjugate partner. Starting from U(S, V): to replace V with P (its conjugate, since P = −∂U/∂V), define **enthalpy** H = U + PV. Then dH = dU + PdV + VdP = TdS − PdV + PdV + VdP = TdS + VdP. Now H's natural variables are S and P — perfect for constant-pressure processes (like most chemistry). The change ΔH at constant pressure equals the heat absorbed, which is why chemists measure heats of reaction as ΔH, not ΔU. To replace S with T (since T = ∂U/∂S), subtract TS: **Helmholtz free energy** A = U − TS, with dA = −SdT − PdV, natural variables T and V. At constant T and V, equilibrium minimizes A. Finally, replacing both S with T and V with P gives **Gibbs free energy** G = U − TS + PV = H − TS, with dG = −SdT + VdP, natural variables T and P.

The payoff is that each potential is minimized at equilibrium under its natural constraints. A system at constant T and P (the most common laboratory situation) minimizes G — not U. This is why G is the central quantity in chemistry: if ΔG < 0 for a reaction at constant T and P, the reaction proceeds spontaneously. The condition ΔG = 0 defines phase equilibrium (why the Clausius-Clapeyron equation uses G). The decomposition G = H − TS shows that spontaneity is a competition between **enthalpy** (energetic stability, favoring low H) and **entropy** (thermal disorder, favoring high S, which increases −TS when T is large) — a trade-off that underlies everything from protein folding to materials processing.

Each transformation preserves all the thermodynamic information — nothing is lost, only re-expressed. The **Maxwell relations** (which this builds toward) exploit this: mixed second derivatives of the potentials are equal, giving powerful identities like (∂S/∂P)_T = −(∂V/∂T)_P. These connect quantities that seem unrelated (how entropy changes with pressure equals how volume changes with temperature) and allow you to express unmeasurable quantities (like entropy changes) in terms of measurable ones (PVT data). The discipline of choosing the right potential for the right constraints — rather than always working with U — is what makes thermodynamic calculations tractable.
