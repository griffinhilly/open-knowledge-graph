---
id: rotational-quantum-numbers-energy
title: Rotational Quantum Numbers and Energy Levels
domain: chemistry
course: physical-chemistry
prerequisites:
- id: rigid-rotor-model
  type: hard
- id: rotational-spectroscopy
  type: hard
builds-toward:
- vibrational-energy-levels-selection-rules
tags:
- rotational-spectroscopy
- quantum-numbers
- energy-levels
stage: advanced
status: draft
---

# Rotational Quantum Numbers and Energy Levels

## Core Idea
Rotational energy levels scale as E_J = BJ(J+1) where J is the angular momentum quantum number and B is the rotational constant proportional to 1/I (moment of inertia). Rotational transitions follow ΔJ = ±1 selection rule. Microwave spectroscopy directly measures closely-spaced rotational levels and yields precise bond lengths via moment of inertia.

## Explainer

From the rigid rotor model, you know that a diatomic molecule rotating about its center of mass behaves like a quantum mechanical rigid rotor — a system whose angular momentum is quantized rather than continuous. The **rotational quantum number J** takes integer values 0, 1, 2, 3, ... and determines both the angular momentum and the energy of each rotational state. The energy formula E_J = BJ(J+1) tells you something immediately important: rotational energy levels are not evenly spaced. The gap between J=0 and J=1 is 2B, between J=1 and J=2 is 4B, between J=2 and J=3 is 6B, and so on. Each successive gap grows by exactly 2B. This unequal spacing is a direct consequence of quantization and is the fingerprint that microwave spectroscopy exploits.

The **rotational constant B** equals ℏ²/(2I), where I is the moment of inertia of the molecule. For a diatomic molecule, I = μr², with μ being the reduced mass and r the bond length. This means B is inversely proportional to both the atomic masses and the square of the bond length. Light molecules with short bonds (like HF) have large B values and widely spaced rotational levels, while heavy molecules with long bonds (like ICl) have tiny B values and closely packed levels. Measuring B from a spectrum therefore gives you the moment of inertia directly, and from that you can extract the bond length with extraordinary precision — often to within 0.001 Å.

The **selection rule ΔJ = ±1** means that a molecule can only jump one rotational level at a time when it absorbs or emits a photon. This restriction comes from the conservation of angular momentum: a photon carries one unit of angular momentum, so the molecule must gain or lose exactly one quantum of rotational angular momentum. In absorption spectroscopy (ΔJ = +1), the absorbed frequencies form a pattern: ν = 2B, 4B, 6B, 8B, ... — a series of equally spaced lines separated by 2B. This beautifully regular pattern in the microwave spectrum is how rotational constants are measured in practice. Each line in the spectrum corresponds to a specific J → J+1 transition, and the uniform spacing 2B is the hallmark of a rigid rotor.

There is one additional subtlety from rotational spectroscopy that connects here: not every molecule has a pure rotational spectrum. A molecule must possess a permanent dipole moment to interact with the oscillating electric field of microwave radiation. Homonuclear diatomics like N₂ and O₂ are rotationally invisible in microwave spectroscopy because they lack a dipole moment, while heteronuclear diatomics like CO and HCl produce textbook rotational spectra. The degeneracy of each level also matters — each J level has (2J+1) degenerate states corresponding to different spatial orientations of the angular momentum vector, which affects the relative intensities of spectral lines through the Boltzmann distribution.
