---
id: hyperconjugation
title: Hyperconjugation
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carbocation-stability-rearrangement
  type: hard
- id: covalent-bonding
  type: soft
builds-toward: []
tags:
- hyperconjugation
- sigma donation
- carbocation stabilization
- alkene stability
- orbital overlap
stage: formal-systems
status: draft
---
# Hyperconjugation

## Core Idea
Hyperconjugation is the stabilizing interaction in which electrons in a C-H or C-C sigma bond adjacent to a carbocation (or other electron-deficient center) partially delocalize into the empty p-orbital on the cation. This sigma-to-p donation is the primary reason tertiary carbocations are more stable than secondary or primary ones: more adjacent C-H bonds means more hyperconjugative donors. The same effect explains why more-substituted alkenes are thermodynamically more stable (Zaitsev's rule) — the filled sigma orbitals of alkyl groups donate into the pi-star orbital of the double bond.

## How It's Best Learned
Draw the orbital picture explicitly: show the filled sigma bond aligned parallel to the empty p-orbital, and sketch the electron density flowing from sigma into p. Compare ethyl cation (three hyperconjugative donors) vs tert-butyl cation (nine donors) to see why substitution matters. Use computational orbital diagrams if available to visualize the interaction.

## Common Misconceptions
- Hyperconjugation is not the same as inductive effect — induction is through-bond polarization of sigma electrons, while hyperconjugation involves actual orbital overlap and partial delocalization.
- Hyperconjugation does not break the C-H bond; the sigma electrons are only partially shared with the adjacent empty orbital.
- The effect operates in neutral molecules too (explaining alkene stability), not only in carbocations.

## Explainer

You already understand that tertiary carbocations are more stable than secondary, which are more stable than primary. The explanation you may have first encountered — "alkyl groups are electron-donating" — is correct but incomplete. **Hyperconjugation** is the specific orbital interaction that explains *how* alkyl groups donate electron density to stabilize adjacent electron-deficient centers, and it operates through a mechanism fundamentally different from inductive effects.

Picture a carbocation: a carbon atom with an empty p-orbital sticking straight up, perpendicular to the plane of its three bonds. Now look at the C–H bonds on the carbon directly next to it. Each of those C–H sigma bonds has a filled bonding orbital with two electrons. When a C–H bond is aligned parallel to the empty p-orbital — an anti-periplanar or roughly parallel geometry — the filled sigma orbital can partially overlap with the empty p-orbital. Electron density flows from the C–H bond into the empty orbital, partially filling it and spreading the positive charge over a larger volume. This is **sigma-to-p donation**, and it stabilizes the cation without breaking any bonds. The C–H bond weakens slightly and lengthens a tiny amount, but it remains intact.

The stability trend now makes quantitative sense. A methyl cation (CH₃⁺) has no adjacent C–H bonds to donate — it receives zero hyperconjugative stabilization. An ethyl cation (primary, CH₃CH₂⁺) has three C–H bonds on the neighboring carbon that can donate. An isopropyl cation (secondary) has six such donors across two adjacent carbons. A tert-butyl cation (tertiary) has nine donors across three adjacent carbons. More donors means more electron density flowing into the empty p-orbital, more charge delocalization, and greater stability. This is why each additional alkyl substituent on a cation provides a measurable stability increase of roughly 15–20 kJ/mol.

Hyperconjugation is not limited to carbocations. The same logic explains why more-substituted alkenes are thermodynamically more stable, a trend you know as **Zaitsev's rule**. In an alkene, the π-bond has both a bonding orbital (filled) and an antibonding orbital (π*, empty). Adjacent C–H sigma bonds can donate into the π* orbital, stabilizing the molecule. A trisubstituted alkene has more adjacent C–H donors than a monosubstituted one, and heats of hydrogenation confirm the stability difference. Hyperconjugation also appears in conformational analysis (it contributes to the preference for staggered over eclipsed conformations) and in radical stability. Whenever you see stabilization correlated with the number of adjacent alkyl groups, hyperconjugation is almost certainly at work.
