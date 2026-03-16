---
id: bonding-antibonding-orbitals
title: 'Bonding and Antibonding Orbitals: Sigma, Pi, and the HOMO-LUMO Gap'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-orbital-diagrams
  type: hard
builds-toward: []
tags:
- sigma-orbitals
- pi-orbitals
- antibonding
- HOMO-LUMO
- orbital-overlap
- star-notation
stage: advanced
status: draft
---

# Bonding and Antibonding Orbitals: Sigma, Pi, and the HOMO-LUMO Gap

## Core Idea
When atomic orbitals overlap to form molecular orbitals, constructive interference produces bonding orbitals (lower energy, electron density concentrated between nuclei) while destructive interference produces antibonding orbitals (higher energy, nodal plane between nuclei, denoted with an asterisk: sigma*, pi*). Sigma bonds arise from head-on overlap along the internuclear axis, while pi bonds arise from lateral overlap of p or d orbitals. The HOMO (highest occupied molecular orbital) and LUMO (lowest unoccupied molecular orbital) define the frontier orbitals that dominate chemical reactivity and spectroscopic transitions. The HOMO-LUMO gap determines the wavelength of the lowest-energy electronic absorption and is a key predictor of molecular stability, color, and conductivity.

## How It's Best Learned
Visualize bonding and antibonding combinations for s-s, s-p, and p-p overlaps by drawing the wavefunctions and identifying nodes. Then connect the HOMO-LUMO gap to UV-Vis absorption wavelengths for a series of conjugated molecules, seeing how extended conjugation narrows the gap and shifts absorption to longer wavelengths.

## Common Misconceptions
- Thinking antibonding orbitals are simply "non-bonding"; antibonding orbitals actively destabilize the molecule when occupied, raising the energy more than the corresponding bonding orbital lowers it.
- Assuming the HOMO-LUMO gap is fixed for a molecule; it depends on geometry, substituents, and solvent environment.

## Explainer

From molecular orbital diagrams, you already know that atomic orbitals combine to form molecular orbitals when atoms bond. The crucial insight here is that this combination always produces pairs: for every bonding molecular orbital formed by constructive interference, there is a corresponding **antibonding molecular orbital** formed by destructive interference. If you start with two atomic orbitals, you get exactly two molecular orbitals — one lower in energy than the original atomic orbitals (bonding) and one higher (antibonding). Electrons are never "lost" in this process; the total number of orbitals is conserved.

The difference between bonding and antibonding orbitals is fundamentally about where the electron density concentrates. In a **bonding orbital**, the wavefunctions of the two atoms add constructively in the region between the nuclei, creating a buildup of electron density that holds the atoms together — the electrons are shared in a way that screens the nuclear repulsion. In an **antibonding orbital** (marked with an asterisk: σ* or π*), the wavefunctions subtract destructively, producing a **node** — a plane of zero electron density — between the nuclei. Electrons in antibonding orbitals actually destabilize the molecule, and this destabilization is slightly greater than the stabilization provided by the corresponding bonding orbital. This asymmetry explains why He₂ does not exist: its four electrons would fill both the σ bonding and σ* antibonding orbitals, and the net effect would be no stabilization at all (actually slight destabilization).

The distinction between **sigma (σ)** and **pi (π)** orbitals relates to the geometry of overlap. Sigma bonds form from head-on overlap along the internuclear axis — s-s, s-p, or p-p end-on. They are cylindrically symmetric and are the strongest type of covalent bond. Pi bonds form from lateral, side-by-side overlap of p orbitals (or d orbitals) perpendicular to the internuclear axis. Pi overlap is weaker because the orbital lobes do not point directly at each other. Each type has its antibonding counterpart: σ* and π*, with the same symmetry but with nodes that prevent the electron density from concentrating between nuclei.

The **HOMO** and **LUMO** — the highest occupied and lowest unoccupied molecular orbitals — are called the **frontier orbitals** because they dominate a molecule's chemistry. When a molecule acts as a nucleophile, it donates electrons from its HOMO. When it acts as an electrophile, it accepts electrons into its LUMO. The energy gap between HOMO and LUMO determines the lowest-energy electronic transition the molecule can undergo — this is the absorption you see in UV-Vis spectroscopy. A large HOMO-LUMO gap means the molecule absorbs only high-energy UV light and appears colorless. A small gap means it absorbs visible light and appears colored. In conjugated systems like polyenes and aromatic compounds, extending the conjugation narrows the HOMO-LUMO gap systematically, which is why beta-carotene (11 conjugated double bonds) is orange while ethylene (one double bond) absorbs only in the far UV.
