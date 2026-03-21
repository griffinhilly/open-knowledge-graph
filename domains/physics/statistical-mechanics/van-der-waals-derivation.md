---
id: van-der-waals-derivation
title: Van der Waals Equation from Statistical Mechanics
domain: physics
course: statistical-mechanics
prerequisites:
- id: second-virial-coefficient
  type: hard
- id: mean-field-theory-statmech
  type: soft
builds-toward:
- critical-phenomena-statmech
tags:
- equation-of-state
- interactions
- mean-field
stage: advanced
status: draft
---

# Van der Waals Equation from Statistical Mechanics

## Core Idea
The van der Waals equation (P + aN²/V²)(V - Nb) = NkT accounts for excluded-volume repulsion (b) and attractive interactions (a) in a mean-field approximation. Its statistical derivation reveals when mean-field theory applies and predicts a critical point where the distinction between liquid and gas vanishes.

## Questions

```yaml
- question: "A real gas at high density is compressed into a small volume. According to the van der Waals equation, the attractive interaction term (aN²/V²) causes the measured pressure to be which of the following compared to an ideal gas at the same conditions?"
  type: multiple-choice
  options:
    - "Higher than ideal, because attractions pull molecules toward the walls"
    - "Lower than ideal, because attractions pull molecules near the walls back toward the interior, reducing momentum delivered to the wall"
    - "Equal to ideal, because intermolecular attractions cancel symmetrically"
    - "Higher than ideal at low temperature, lower at high temperature"
  answer: 1
  explanation: "Molecules near the container wall are attracted back toward the bulk interior by their neighbors. This inward pull reduces the momentum they transfer to the wall, so the measured pressure is lower than it would be for non-interacting particles. The correction is −aN²/V²: negative, reducing pressure. Option A reverses the direction of the effect — attractions pull molecules *away* from the walls, not toward them."

- question: "Below the critical temperature, the van der Waals P–V isotherm develops an 'S-shaped' curve with a region where pressure increases as volume increases. What does Maxwell's equal-area construction accomplish?"
  type: multiple-choice
  options:
    - "It provides the exact critical exponents that experiments confirm"
    - "It replaces the mechanically unstable S-shaped region with a horizontal tie line representing liquid-gas coexistence"
    - "It corrects the excluded-volume term b to account for molecular shape"
    - "It extends the mean-field equation to temperatures above the critical point"
  answer: 1
  explanation: "A region with positive slope in P(V) implies negative compressibility — the gas would expand when compressed — which is mechanically unstable and unphysical. Maxwell's construction replaces this unstable portion with a flat coexistence line at the equilibrium vapor pressure, representing the two phases (liquid and gas) coexisting at the same pressure. The equal-area rule determines which pressure: the area under the S-curve on each side of the line must be equal, enforcing thermodynamic equilibrium."

- question: "The van der Waals equation gives exact predictions for critical exponents (such as how magnetization vanishes at a critical temperature)."
  type: true-false
  answer: false
  explanation: "The van der Waals equation is a mean-field approximation that ignores fluctuations. Near the critical point, fluctuations become extremely large (the correlation length diverges), so mean-field theory breaks down. Experimentally, critical exponents differ from mean-field predictions — for example, the coexistence curve (density difference between liquid and gas) near T_c scales as (T_c−T)^β with β≈0.326, not the mean-field value of 0.5. The van der Waals equation gets the qualitative picture right but fails quantitatively near criticality."

- question: "In the van der Waals equation (P + aN²/V²)(V − Nb) = NkT, replacing V with V − Nb captures the fact that each molecule has less effective space to move in because other molecules physically occupy volume."
  type: true-false
  answer: true
  explanation: "The excluded-volume correction b accounts for the finite size of molecules. The center of one molecule cannot approach the center of another within a distance equal to the molecular diameter, so the free volume available to any molecule is V minus the volume excluded by all other molecules. This term is derived directly from the second virial coefficient for hard-sphere repulsion: it increases the effective pressure because molecules collide more frequently when less free volume is available."

- question: "Explain why the van der Waals equation predicts a critical point, and why the mean-field approximation that underlies it fails precisely near that critical point."
  type: short-answer
  answer: "The van der Waals equation predicts a critical point because the attractive term (reducing pressure) and the excluded-volume term (increasing it) compete in a way that — below a critical temperature T_c — creates a region of mechanical instability (the S-curve) representing liquid-gas coexistence. At T_c, this instability just disappears: the liquid and gas densities become equal. The mean-field approximation fails near T_c because it replaces actual molecular interactions with an average field proportional to density, ignoring correlated fluctuations. Near the critical point, fluctuations become large and long-ranged — density fluctuates wildly across large spatial scales — and these correlated fluctuations are exactly what the mean-field approach discards."
  explanation: "Mean-field theory works well when each molecule 'sees' many neighbors that average out, so replacing pairwise interactions with an average is reasonable. This holds at high density or far from the critical point. Near T_c, the system is poised between two phases, so tiny fluctuations can nucleate macroscopic regions of either phase — the correlation length diverges. Mean-field theory predicts wrong critical exponents because it effectively sets the correlation length to zero. More sophisticated renormalization-group theory correctly handles these fluctuations and recovers the observed exponents."
```

## Explainer

The ideal gas law PV = NkT is derived for non-interacting point particles. Real molecules are neither points nor non-interacting: they have finite size and attract each other at intermediate distances. The **van der Waals equation** (P + aN²/V²)(V − Nb) = NkT corrects both defects through a **mean-field approximation**, and understanding its derivation reveals both the power and the limits of mean-field thinking.

The excluded-volume correction comes first. A molecule is not a point — it occupies space, and no other molecule's center can enter a sphere of diameter σ around it. The second virial coefficient you studied captures this: at short range the pair potential is strongly repulsive, contributing a positive correction to the virial expansion. Summed over all molecules, the available volume for any given molecule's center-of-mass is not V but V − Nb, where b is the excluded volume per molecule (roughly four times the molecular volume, since each pair shares an excluded sphere). Replacing V with V − Nb in the ideal gas law gives the first correction, which increases the pressure for a given volume as expected — molecules are bumping into each other more often.

The attractive interaction correction is where mean-field theory enters. Molecules attract each other at intermediate range (van der Waals dispersion forces). A molecule in the bulk interior is surrounded by neighbors on all sides, so the net attractive force is zero. But a molecule near the container wall has fewer neighbors on the wall side — it is pulled back inward by its bulk neighbors. This inward pull reduces the momentum it delivers to the wall, reducing the measured pressure below the ideal value. In the mean-field approximation the reduction is proportional to the density squared: each molecule near the wall is attracted by a number proportional to the bulk density, and the number of molecules near any wall patch is also proportional to density. This gives the pressure correction −aN²/V², the second term in the van der Waals equation.

The van der Waals equation predicts a **critical point** at T_c = 8a/(27kb), V_c = 3Nb, P_c = a/(27b²). Below T_c, the P(V) isotherm develops an "S-shaped" curve with an unphysical region where pressure increases as volume increases — that would mean negative compressibility, making the system mechanically unstable. Maxwell's equal-area rule resolves this by replacing the unphysical portion with a horizontal tie line representing liquid-gas coexistence. The model therefore captures the essential physics of condensation: attractive interactions drive a first-order phase transition, and there is a critical temperature above which liquid and gas are indistinguishable. The mean-field approximation underestimates fluctuations near the critical point and gives incorrect critical exponents, but the qualitative picture — a critical point terminating a first-order transition line — is correct and is the starting point for the more refined theory of critical phenomena.
