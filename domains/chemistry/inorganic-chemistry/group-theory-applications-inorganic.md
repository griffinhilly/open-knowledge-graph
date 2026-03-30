---
id: group-theory-applications-inorganic
title: Group Theory Applications in Inorganic Chemistry
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: group-theory-molecular-symmetry
  type: hard
- id: mo-theory-transition-metal-complexes
  type: hard
builds-toward:
- term-symbols-d-electron
tags:
- group theory
- symmetry operations
- character tables
- SALCs
- selection rules
stage: expert
status: validated
---

# Group Theory Applications in Inorganic Chemistry

## Core Idea
Group theory provides a systematic method for constructing molecular orbital diagrams, predicting spectroscopic selection rules, and analyzing vibrational modes of coordination compounds. By identifying the point group of a complex, generating reducible representations for ligand orbital sets, and decomposing them into irreducible representations using character tables, you can determine which metal and ligand orbitals can interact — all without solving any integrals.

## Questions

```yaml
- question: "For an octahedral ML₆ complex, the six sigma-donor ligand orbitals generate a reducible representation that decomposes into which irreducible representations of the Oh point group?"
  type: multiple-choice
  options:
    - "a₁g + eg + t₂g"
    - "a₁g + eg + t₁u"
    - "t₂g + t₁u + a₂u"
    - "a₁g + t₁u + t₂g + eg"
  answer: 1
  explanation: "The six sigma-donor orbitals (one on each ligand, pointing at the metal) form a basis set for a reducible representation in Oh symmetry. Applying the reduction formula gives: Γ_sigma = a₁g + eg + t₁u. The a₁g combination matches the metal s orbital, the eg pair matches the metal d_z² and d_x²−y² orbitals, and the t₁u set matches the metal p_x, p_y, p_z orbitals. Crucially, no ligand sigma combination has t₂g symmetry — this is why the metal t₂g orbitals (d_xy, d_xz, d_yz) are nonbonding in a sigma-only octahedral complex, and it is the group-theoretic origin of the crystal field splitting."

- question: "The projection operator in group theory generates symmetry-adapted linear combinations (SALCs) from a single ligand orbital by applying all symmetry operations of the group and weighting the results by the characters of the target irreducible representation."
  type: true-false
  answer: true
  explanation: "The projection operator is the practical tool for constructing SALCs. You pick one ligand orbital as a generating function, apply each symmetry operation to see where it maps, multiply the result by the character of the target irreducible representation for that operation, and sum. The result is a SALC that transforms as the specified irreducible representation. For the a₁g SALC of six sigma orbitals in Oh, all characters are +1, so you get the sum of all six (properly normalized). For eg SALCs, the characters give specific linear combinations that match the shapes of d_z² and d_x²−y². This systematic procedure replaces guesswork with algorithm."

- question: "Group theory can predict whether a d-d electronic transition is symmetry-allowed but cannot predict its intensity."
  type: true-false
  answer: false
  explanation: "Group theory predicts both whether a transition is symmetry-allowed (does the direct product of initial state × operator × final state irreducible representations contain the totally symmetric representation?) AND provides qualitative intensity information. Symmetry-forbidden transitions (those where the direct product excludes the totally symmetric representation) have zero intensity by symmetry — the transition dipole integral vanishes exactly. For allowed transitions, group theory identifies which polarization component (x, y, or z) carries the intensity, enabling polarized absorption measurements on oriented crystals. What group theory cannot predict is the absolute magnitude of an allowed transition — that requires calculating the actual integral."

- question: "Using group theory, explain why the d-d transitions of an octahedral complex are Laporte-forbidden and describe the mechanism by which they gain weak intensity."
  type: short-answer
  answer: "In Oh symmetry, the d-orbitals belong to gerade (even) representations: t₂g and eg. The electric dipole operator transforms as t₁u (ungerade, odd). The direct product of two gerade representations with an ungerade operator is always ungerade, which cannot contain the totally symmetric a₁g representation. Therefore the integral ⟨ψ_initial|μ|ψ_final⟩ = 0 by symmetry — the transition is Laporte-forbidden. Intensity is gained through vibronic coupling: molecular vibrations of ungerade symmetry (t₁u, t₂u) temporarily distort the complex away from perfect Oh symmetry, mixing ungerade character into the d-orbitals. The transition becomes weakly allowed through the combined electronic-vibrational (vibronic) mechanism, typically giving molar absorptivities of 1-100 M⁻¹cm⁻¹."
  explanation: "This analysis also explains why tetrahedral complexes have stronger d-d bands: Td has no inversion center, so the Laporte rule does not apply. The d-orbitals can mix with p-orbitals of the same irreducible representation (both t₂ representations contain d and p orbitals in Td), giving the transitions partially allowed character."
```

## Explainer

In physical chemistry, you learned group theory as a framework for predicting IR and Raman activity of molecular vibrations. In inorganic chemistry, group theory becomes an even more powerful tool because coordination compounds have high symmetry, and the electronic structure of d-orbital complexes is exquisitely sensitive to that symmetry. The central application is constructing MO diagrams using symmetry-adapted linear combinations (SALCs) rather than guessing which orbitals interact.

The procedure is systematic. First, assign the point group of the complex (Oh for octahedral, Td for tetrahedral, D₄h for square planar, etc.). Second, identify the basis set of ligand orbitals you want to analyze — for sigma bonding, these are the ligand lone pairs pointing at the metal. Third, determine how this basis set transforms under each symmetry operation of the group, generating a reducible representation. Fourth, decompose the reducible representation into irreducible representations using the reduction formula. The resulting irreducible representations tell you exactly which metal orbitals can form bonding and antibonding combinations with the ligand set. For Oh sigma bonding, the decomposition gives a₁g + eg + t₁u — meaning metal s, d(eg), and p orbitals can form sigma bonds, while the t₂g d-orbitals are left nonbonding.

The same procedure applies to pi bonding. The twelve pi-donor (or pi-acceptor) orbitals on six octahedral ligands generate their own reducible representation, which decomposes into t₁g + t₁u + t₂g + t₂u. Only the t₂g component has a metal orbital counterpart (the d_xy, d_xz, d_yz set), so only the t₂g ligand pi-orbitals participate in metal-ligand pi bonding. This is the group-theoretic proof that pi interactions affect only the t₂g level in octahedral complexes — the foundation of ligand field theory's explanation of the spectrochemical series.

Selection rules for electronic transitions follow from the same orthogonality principle. The transition dipole moment integral ⟨ψ_f|μ|ψ_i⟩ is nonzero only if the direct product of the irreducible representations of ψ_f, μ, and ψ_i contains the totally symmetric representation. For d-d transitions in Oh, both initial and final states are gerade, while the dipole operator is ungerade (t₁u) — the product is ungerade and cannot contain a₁g, so the transition is Laporte-forbidden. This group-theoretic derivation replaces hand-waving arguments about parity with a rigorous mathematical proof. The same framework predicts which vibrations are IR-active, which are Raman-active, and whether specific electronic transitions can be observed in polarized spectra of oriented single crystals.
