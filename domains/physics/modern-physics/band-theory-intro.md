---
id: band-theory-intro
title: Band Theory of Solids
domain: physics
course: modern-physics
prerequisites:
- id: pauli-exclusion-principle
  type: hard
- id: atomic-orbitals
  type: hard
- id: particle-in-a-box
  type: soft
tags:
- solid-state
- band-gap
- conductor
- insulator
- semiconductor
- valence-band
stage: advanced
status: validated
---

# Band Theory of Solids

## Core Idea
When atoms are brought together in a crystal, their discrete atomic energy levels broaden into continuous allowed bands separated by forbidden band gaps. The Pauli exclusion principle determines how electrons fill these bands. A material is a conductor if its highest occupied band is partially filled (electrons can easily gain kinetic energy), an insulator if all bands are either completely full or empty with a large gap, and a semiconductor if the gap is small enough for electrons to bridge it thermally or with light. Band theory underpins all modern electronics and photovoltaics.

## How It's Best Learned
Start from molecular orbital formation in diatomic molecules (bonding + antibonding), then extend to a chain of N atoms to get N closely-spaced levels forming a band. Count electrons and fill bands using Pauli exclusion to classify metals, insulators, and semiconductors.

## Common Misconceptions
- Conductors have 'free electrons' that are not bound at all — conduction electrons are quantum states delocalized over the crystal; they are still bound to the overall material.
- Semiconductors are poor conductors at all temperatures — at room temperature a small gap semiconductor has thermally excited electrons in the conduction band; conductivity increases strongly with temperature.

## Explainer

You know from atomic orbitals that electrons in isolated atoms occupy discrete energy levels — 1s, 2s, 2p, and so on. You also know from the Pauli exclusion principle that no two electrons can share the same quantum state. Band theory shows what happens when you bring N atoms together into a crystal: the discrete atomic levels do not stay discrete. Each atomic level broadens into a **band** of N closely-spaced energy levels, because the wavefunctions of neighboring atoms overlap and interact. With N ~ 10²³ atoms in a macroscopic crystal, the energy levels in each band are so densely packed they are effectively continuous.

The origin of the broadening has a clean analogy in chemistry. When two hydrogen atoms form a molecule, the 1s atomic orbital splits into a bonding orbital (lower energy) and an antibonding orbital (higher energy). Three atoms in a chain give three levels; N atoms give N levels spread over roughly the same energy range. The spacing between levels shrinks as N grows, but the total bandwidth stays roughly constant. The gaps between atomic levels become **band gaps** in the crystal — energy ranges where no allowed quantum state exists. An electron in the crystal can have energies within the allowed bands, but not within the gaps.

Now apply the Pauli exclusion principle to fill these bands with electrons. Each band holds 2N states (factor of 2 for spin), and you fill from the bottom up with the available electrons. The electrical behavior of the material is determined by how the bands are filled: if the highest occupied band is **partially filled**, electrons near the top can easily absorb a small amount of energy from an electric field and accelerate — the material is a **metal** (conductor). If all bands are either completely full or completely empty, electrons cannot respond to a weak field because there are no nearby empty states to move into — the material is an **insulator**. The gap size determines the boundary: silicon has a 1.1 eV gap (semiconductor, thermally bridgeable at room temperature), diamond has a 5.5 eV gap (insulator), and copper has a partly-filled band (metal).

Semiconductors occupy the critical middle ground. Their band gap is small enough that thermal energy at room temperature promotes some electrons from the filled **valence band** into the empty **conduction band**, leaving behind positively-charged vacancies called **holes**. Both the excited electrons and the holes contribute to electrical conduction. Doping — introducing impurity atoms — can shift the Fermi level to create n-type (electron-rich) or p-type (hole-rich) semiconductors. The p-n junction formed at their interface is the foundation of diodes, transistors, solar cells, and LEDs. The particle-in-a-box intuition you already have is directly relevant here: the standing-wave solutions in the periodic crystal potential are what produce the allowed bands, and the wave-nature of electrons is exactly why band structure exists at all.
