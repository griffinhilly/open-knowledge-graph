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
stage: advanced
status: validated
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

## Questions

```yaml
- question: "A chemist runs a reaction at constant temperature and pressure and observes that it is spontaneous even though it is endothermic (ΔH > 0). Which explanation is correct?"
  type: multiple-choice
  options:
    - "The reaction is spontaneous because it must be releasing heat — the chemist's ΔH measurement must be wrong"
    - "ΔU < 0 is the true spontaneity criterion and must be satisfied here"
    - "The entropy increase is large enough that TΔS > ΔH, making ΔG = ΔH − TΔS negative"
    - "Volume work (−PΔV) drives the reaction since pressure is held constant"
  answer: 2
  explanation: "At constant T and P, the spontaneity criterion is ΔG < 0, not ΔH < 0 or ΔU < 0. Since G = H − TS, ΔG = ΔH − TΔS. When ΔS is sufficiently positive — the reaction substantially increases disorder — TΔS can exceed ΔH, making ΔG negative even for an endothermic process. Dissolving ammonium nitrate in water is a real example: endothermic but spontaneous because of the large entropy increase. Option B is wrong because ΔU < 0 is only the equilibrium criterion at constant S and V, not at constant T and P."

- question: "Why do chemists characterize heats of reaction as ΔH rather than ΔU?"
  type: multiple-choice
  options:
    - "Enthalpy is easier to measure calorimetrically than internal energy"
    - "H's natural variables are S and P — at constant pressure, ΔH equals the heat absorbed, so it directly captures what a calorimeter measures"
    - "Internal energy is only defined for ideal gases, while enthalpy applies to all states of matter"
    - "Internal energy is not conserved in chemical reactions, making it unsuitable as a thermodynamic potential"
  answer: 1
  explanation: "The Legendre transformation replaces V with P to produce H = U + PV, with dH = TdS + VdP. At constant pressure (dP = 0), dH = TdS = dq — the heat exchanged reversibly. The natural variables S and P match the experimental constraint (constant P in an open calorimeter), making H the right potential and ΔH the direct measure of heat flow. Option A has some practical truth but is not the thermodynamic reason. Options C and D are false."

- question: "Legendre transformations lose thermodynamic information — converting from U(S,V) to G(T,P) means you can no longer recover entropy or volume from G."
  type: true-false
  answer: false
  explanation: "Legendre transformations preserve all thermodynamic information — nothing is lost, only re-expressed in different natural variables. From G(T,P), entropy is recovered as S = −(∂G/∂T)_P and volume as V = (∂G/∂P)_T. The transformation is a mathematically exact change of variables, not an approximation. This is why each potential is equally valid as a complete thermodynamic description — they are all equivalent representations of the same physics."

- question: "At constant temperature and pressure, a spontaneous process always decreases the system's enthalpy."
  type: true-false
  answer: false
  explanation: "Spontaneity at constant T and P is governed by ΔG = ΔH − TΔS < 0, not by ΔH < 0 alone. Entropy-driven reactions — endothermic processes where disorder increases substantially — can be spontaneous even with ΔH > 0, because TΔS outweighs ΔH. Enthalpy decrease favors spontaneity, but it competes with entropy: at high temperatures, the TΔS term dominates. ΔH < 0 is neither necessary nor sufficient for spontaneity at constant T and P."

- question: "Why do all four thermodynamic potentials (U, H, A, G) contain the same information, yet the choice of which to use matters enormously in practice?"
  type: short-answer
  answer: "They contain the same information because each is a Legendre transform of the others — mathematically equivalent re-expressions of the same physics in different natural variables. But each potential is minimized at equilibrium only under its own natural constraints. Using the wrong potential for your experimental conditions forces you to track extra work terms explicitly rather than having them automatically absorbed into the potential's structure."
  explanation: "At constant T and P (most laboratory reactions), G is minimized at equilibrium — ΔG < 0 is the spontaneity criterion, and ΔG = 0 defines phase equilibrium. If you insist on working with U, you must separately account for heat exchange and PV work at every step — the bookkeeping G's structure handles automatically. The Legendre transform is precisely the operation that moves the work term inside the potential, making it invisible when the constraint is satisfied. Matching the potential to the constraint converts a complex balance of terms into a single inequality."
```

## Explainer

From your study of exact and inexact differentials, you know that the internal energy U has a beautifully exact differential: dU = TdS − PdV. This tells you that U's **natural variables** are S (entropy) and V (volume) — these are the variables you'd hold constant to reach equilibrium if you were minimizing U. In practice, experiments are almost never run at constant entropy and constant volume. Chemists run reactions at constant pressure and temperature; engineers analyze engines at constant temperature; atmospheric scientists deal with systems at constant pressure. The Legendre transformation is the mathematical machinery for switching to the variables that actually match your experimental constraints.

The **Legendre transformation** replaces a variable with its conjugate partner. Starting from U(S, V): to replace V with P (its conjugate, since P = −∂U/∂V), define **enthalpy** H = U + PV. Then dH = dU + PdV + VdP = TdS − PdV + PdV + VdP = TdS + VdP. Now H's natural variables are S and P — perfect for constant-pressure processes (like most chemistry). The change ΔH at constant pressure equals the heat absorbed, which is why chemists measure heats of reaction as ΔH, not ΔU. To replace S with T (since T = ∂U/∂S), subtract TS: **Helmholtz free energy** A = U − TS, with dA = −SdT − PdV, natural variables T and V. At constant T and V, equilibrium minimizes A. Finally, replacing both S with T and V with P gives **Gibbs free energy** G = U − TS + PV = H − TS, with dG = −SdT + VdP, natural variables T and P.

The payoff is that each potential is minimized at equilibrium under its natural constraints. A system at constant T and P (the most common laboratory situation) minimizes G — not U. This is why G is the central quantity in chemistry: if ΔG < 0 for a reaction at constant T and P, the reaction proceeds spontaneously. The condition ΔG = 0 defines phase equilibrium (why the Clausius-Clapeyron equation uses G). The decomposition G = H − TS shows that spontaneity is a competition between **enthalpy** (energetic stability, favoring low H) and **entropy** (thermal disorder, favoring high S, which increases −TS when T is large) — a trade-off that underlies everything from protein folding to materials processing.

Each transformation preserves all the thermodynamic information — nothing is lost, only re-expressed. The **Maxwell relations** (which this builds toward) exploit this: mixed second derivatives of the potentials are equal, giving powerful identities like (∂S/∂P)_T = −(∂V/∂T)_P. These connect quantities that seem unrelated (how entropy changes with pressure equals how volume changes with temperature) and allow you to express unmeasurable quantities (like entropy changes) in terms of measurable ones (PVT data). The discipline of choosing the right potential for the right constraints — rather than always working with U — is what makes thermodynamic calculations tractable.
