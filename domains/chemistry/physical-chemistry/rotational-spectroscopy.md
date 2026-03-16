---
id: rotational-spectroscopy
title: Rotational (Microwave) Spectroscopy
domain: chemistry
course: physical-chemistry
prerequisites:
- id: rigid-rotor-model
  type: hard
- id: selection-rules-spectroscopy
  type: hard
- id: rotational-kinematics
  type: soft
- id: electromagnetic-spectrum
  type: soft
- id: angular-momentum
  type: soft
builds-toward:
- vibrational-spectroscopy-theory
tags:
- microwave
- rotational-constant
- bond-length
- dipole-moment
- centrifugal-distortion
stage: advanced
status: validated
---

# Rotational (Microwave) Spectroscopy

## Core Idea
Rotational spectroscopy probes transitions between molecular rotational energy levels using microwave radiation (roughly 1–1000 GHz). For a rigid diatomic rotor, allowed transitions occur at frequencies ν = 2B(J+1) where J is the lower-state quantum number, producing a series of equally spaced lines separated by 2B. The rotational constant B = h/(8π²Ic) directly yields the moment of inertia and hence the bond length with high precision. Real spectra show centrifugal distortion (decreasing line spacing at high J) and require a permanent dipole moment for observation.

## How It's Best Learned
Simulate or analyze a diatomic microwave spectrum, extract B from line spacings, and calculate the bond length. Compare your result to known values to assess the accuracy of the rigid rotor approximation.

## Common Misconceptions
- Assuming all molecules show microwave spectra — homonuclear diatomics like N₂ have no dipole and are microwave-inactive.
- Forgetting that line spacings give 2B, not B.

## Explainer

You already know from the rigid rotor model that a diatomic molecule rotating in space has quantized energy levels E_J = BJ(J+1), where B = h/(8π²Ic) is the **rotational constant** and J is the rotational quantum number. Rotational spectroscopy is the experimental technique that measures transitions between these levels, using microwave radiation to drive the molecule from one rotational state to the next. The selection rules you studied tell you that allowed transitions require ΔJ = ±1 and — critically — the molecule must have a **permanent dipole moment**. This is why homonuclear diatomics like H₂ and N₂ are invisible to microwave spectroscopy: with no dipole, the oscillating electric field of the microwave radiation has nothing to grab onto.

For an absorption transition from J to J+1, the transition frequency is ν = 2B(J+1). This produces a beautifully simple pattern: the first line (J=0→1) appears at 2B, the second (J=1→2) at 4B, the third at 6B, and so on. The spectrum is a series of **equally spaced lines separated by 2B**. This uniform spacing is the hallmark of a rigid rotor spectrum, and it makes extracting B almost trivially easy — just measure the gap between adjacent lines and divide by two. From B you get the moment of inertia I = h/(8π²Bc), and from I you extract the bond length r since I = μr² for a diatomic, where μ is the reduced mass. This gives bond lengths with extraordinary precision, often to five or six significant figures.

Real molecules are not perfectly rigid, however. As J increases and the molecule spins faster, centrifugal force stretches the bond slightly, increasing the moment of inertia and decreasing the effective rotational constant. This effect is called **centrifugal distortion**, and it causes the line spacing to decrease gradually at high J values. The corrected energy expression adds a term −D_J[J(J+1)]², where D_J is the centrifugal distortion constant. In practice, D_J is much smaller than B (typically by a factor of 10⁴ or more), so the effect is subtle but measurable — and it actually provides additional information about the bond's stiffness.

The power of rotational spectroscopy lies in its directness: the spacing of microwave absorption lines maps almost one-to-one onto molecular geometry. Unlike electronic or vibrational spectroscopy, where extracting structural parameters requires modeling multiple interacting degrees of freedom, a microwave spectrum of a simple molecule gives you the bond length with minimal interpretation. For polyatomic molecules the analysis grows more complex — you need three rotational constants (A, B, C) for an asymmetric top — but the principle remains the same: rotational transitions reveal the mass distribution of the molecule with remarkable precision.
