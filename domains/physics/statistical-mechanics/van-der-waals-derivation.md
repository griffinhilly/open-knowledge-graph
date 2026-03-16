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

## Explainer

The ideal gas law PV = NkT is derived for non-interacting point particles. Real molecules are neither points nor non-interacting: they have finite size and attract each other at intermediate distances. The **van der Waals equation** (P + aN²/V²)(V − Nb) = NkT corrects both defects through a **mean-field approximation**, and understanding its derivation reveals both the power and the limits of mean-field thinking.

The excluded-volume correction comes first. A molecule is not a point — it occupies space, and no other molecule's center can enter a sphere of diameter σ around it. The second virial coefficient you studied captures this: at short range the pair potential is strongly repulsive, contributing a positive correction to the virial expansion. Summed over all molecules, the available volume for any given molecule's center-of-mass is not V but V − Nb, where b is the excluded volume per molecule (roughly four times the molecular volume, since each pair shares an excluded sphere). Replacing V with V − Nb in the ideal gas law gives the first correction, which increases the pressure for a given volume as expected — molecules are bumping into each other more often.

The attractive interaction correction is where mean-field theory enters. Molecules attract each other at intermediate range (van der Waals dispersion forces). A molecule in the bulk interior is surrounded by neighbors on all sides, so the net attractive force is zero. But a molecule near the container wall has fewer neighbors on the wall side — it is pulled back inward by its bulk neighbors. This inward pull reduces the momentum it delivers to the wall, reducing the measured pressure below the ideal value. In the mean-field approximation the reduction is proportional to the density squared: each molecule near the wall is attracted by a number proportional to the bulk density, and the number of molecules near any wall patch is also proportional to density. This gives the pressure correction −aN²/V², the second term in the van der Waals equation.

The van der Waals equation predicts a **critical point** at T_c = 8a/(27kb), V_c = 3Nb, P_c = a/(27b²). Below T_c, the P(V) isotherm develops an "S-shaped" curve with an unphysical region where pressure increases as volume increases — that would mean negative compressibility, making the system mechanically unstable. Maxwell's equal-area rule resolves this by replacing the unphysical portion with a horizontal tie line representing liquid-gas coexistence. The model therefore captures the essential physics of condensation: attractive interactions drive a first-order phase transition, and there is a critical temperature above which liquid and gas are indistinguishable. The mean-field approximation underestimates fluctuations near the critical point and gives incorrect critical exponents, but the qualitative picture — a critical point terminating a first-order transition line — is correct and is the starting point for the more refined theory of critical phenomena.
