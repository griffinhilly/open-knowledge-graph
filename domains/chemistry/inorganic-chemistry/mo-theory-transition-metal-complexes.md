---
id: mo-theory-transition-metal-complexes
title: Molecular Orbital Theory for Transition Metal Complexes
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: molecular-orbital-theory-advanced
  type: hard
- id: ligand-field-theory
  type: hard
- id: group-theory-molecular-symmetry
  type: soft
builds-toward:
- electronic-spectra-tanabe-sugano
- metal-metal-bonding
tags:
- molecular orbital theory
- MO diagrams
- sigma bonding
- pi bonding
- transition metal complexes
stage: advanced
status: validated
---

# Molecular Orbital Theory for Transition Metal Complexes

## Core Idea
Molecular orbital theory applied to transition metal complexes constructs MO diagrams by combining metal d (and s, p) orbitals with symmetry-adapted linear combinations of ligand orbitals. In an octahedral complex, sigma-bonding ligand combinations interact with the metal eg and a₁g orbitals, producing bonding and antibonding MO sets. The t₂g metal orbitals may be nonbonding (sigma-only ligands), destabilized (pi-donors), or stabilized (pi-acceptors). This full MO treatment reproduces and extends CFT/LFT predictions while providing a rigorous orbital basis for understanding bonding.

## Questions

```yaml
- question: "In the MO diagram of an octahedral complex with sigma-only ligands, which metal-based orbitals become the HOMO for a d⁶ low-spin configuration?"
  type: multiple-choice
  options:
    - "The bonding eg MOs"
    - "The nonbonding t₂g MOs"
    - "The antibonding eg* MOs"
    - "The metal 4s-based a₁g MO"
  answer: 1
  explanation: "With sigma-only ligands, the metal t₂g orbitals (d_xy, d_xz, d_yz) point between the ligands and have no sigma-bonding ligand counterpart — they remain nonbonding. In a d⁶ low-spin complex, all six electrons fill the t₂g set completely. These are the highest occupied molecular orbitals, making them the HOMO. The bonding eg MOs are lower in energy (filled by ligand electrons), while the antibonding eg* MOs are the LUMO — the 'Δ_oct' gap in MO theory is the energy difference between t₂g and eg*."

- question: "The crystal field splitting parameter Δ_oct in MO theory corresponds to the energy gap between the nonbonding t₂g orbitals and the antibonding eg* orbitals, not between bonding sets."
  type: true-false
  answer: true
  explanation: "This is a critical conceptual point. In CFT, Δ_oct appears to be between two sets of d-orbitals. In MO theory, the full picture reveals that the 'eg' orbitals involved in the splitting are actually antibonding MOs formed from metal eg-symmetry orbitals mixing with ligand sigma-donor SALCs. The t₂g orbitals are nonbonding (with sigma-only ligands) or modified by pi interactions. The gap between these two sets — t₂g (nonbonding or pi-modified) and eg* (antibonding) — is what CFT calls Δ_oct. This explains why stronger sigma-donors produce larger Δ: they push the eg* antibonding orbitals higher."

- question: "In the MO diagram of [Co(CO)₆]³⁺, the t₂g orbitals are significantly stabilized compared to a sigma-only complex. This stabilization results from pi-back-bonding into CO's empty π* orbitals."
  type: true-false
  answer: true
  explanation: "CO has empty π* orbitals with the correct symmetry (t₂g in Oh) to overlap with the filled metal t₂g orbitals. This interaction creates bonding and antibonding combinations: the bonding combination lowers the energy of the metal-based t₂g electrons (stabilizing them), while the antibonding combination raises CO-based orbitals. The net effect is that the occupied t₂g level drops in energy, increasing the gap to eg* and producing a very large Δ_oct. This is the MO basis for CO being the strongest common field ligand."

- question: "Construct the qualitative MO energy level diagram for an octahedral ML₆ complex with pi-donor ligands and explain how it differs from the sigma-only case."
  type: short-answer
  answer: "Start with the sigma-only case: six ligand sigma SALCs interact with metal orbitals of matching symmetry (a₁g with s, t₁u with p, eg with d_z²/d_x²−y²) to form bonding and antibonding pairs. The t₂g metal orbitals are nonbonding. Now add pi-donor interactions: the ligand pi-donor orbitals (filled) have t₂g symmetry and interact with the metal t₂g orbitals. Since the ligand pi-orbitals are filled, this produces a bonding MO (mostly ligand character, lower energy) and an antibonding MO (mostly metal character, higher energy). The metal-based t₂g level is pushed UP in energy, decreasing the gap to eg* — hence Δ_oct shrinks. This is the MO explanation for why pi-donors are weak-field ligands."
  explanation: "For pi-acceptors, the effect reverses: the ligand pi* orbitals are empty and higher in energy than the metal t₂g. The interaction produces a bonding MO (mostly metal character, lowered) and antibonding MO (mostly ligand character, raised). The metal-based t₂g drops in energy, increasing Δ_oct. The full MO diagram thus provides a unified picture of the entire spectrochemical series."
```

## Explainer

Ligand field theory explained the spectrochemical series qualitatively: pi-donors weaken the field, sigma-donors are intermediate, pi-acceptors strengthen the field. Molecular orbital theory provides the quantitative orbital framework underlying these observations. By constructing MO diagrams for octahedral complexes, you can see exactly which orbitals interact, how they shift in energy, and where electrons reside — resolving ambiguities that LFT leaves qualitative.

The construction of an octahedral ML₆ MO diagram begins with symmetry. The six ligand sigma-donor orbitals combine into symmetry-adapted linear combinations (SALCs) that transform as a₁g, eg, and t₁u representations of the Oh point group. The metal provides orbitals of matching symmetry: the 4s orbital (a₁g), the three 4p orbitals (t₁u), and two of the five 3d orbitals (d_z² and d_x²−y², which transform as eg). These six matched pairs produce six bonding MOs and six antibonding MOs. The remaining three metal d-orbitals (d_xy, d_xz, d_yz, transforming as t₂g) have no sigma-bonding ligand counterpart and remain nonbonding — these are the t₂g orbitals of crystal field theory. The twelve ligand electrons fill the six bonding MOs; the metal d-electrons then fill the t₂g and, if needed, the antibonding eg* orbitals. The energy gap between t₂g and eg* is Δ_oct.

Adding pi interactions modifies this picture at the t₂g level. Pi-donor ligands (with filled p or pi orbitals of t₂g symmetry) interact with the metal t₂g orbitals to form bonding and antibonding combinations. Since the ligand orbitals are already filled, the bonding combination drops below the original t₂g level (gaining ligand character) and the antibonding combination rises above it (gaining metal character). The metal d-electrons now occupy this raised antibonding combination, effectively pushing t₂g up and shrinking Δ. For pi-acceptor ligands (with empty π* orbitals of t₂g symmetry), the interaction pulls the metal t₂g electrons down into a bonding combination, increasing Δ. The MO diagram thus provides a rigorous, visual explanation for the entire spectrochemical series.

This MO approach also reveals features invisible to simpler models. The covalent nature of bonding is explicit: bonding MOs have mixed metal-ligand character, and the degree of mixing determines the covalency of the bond. The charge-transfer transitions observed spectroscopically correspond to electron promotions between MOs of primarily ligand character and MOs of primarily metal character. And the frontier orbital analysis (HOMO-LUMO considerations) connects directly to reactivity predictions — a bridge to the organometallic chemistry and catalysis topics ahead.
