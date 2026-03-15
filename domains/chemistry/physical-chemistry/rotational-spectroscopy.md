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
- id: rotational-spectroscopy
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
