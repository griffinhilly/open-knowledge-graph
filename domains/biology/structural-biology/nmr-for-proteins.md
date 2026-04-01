---
id: nmr-for-proteins
title: NMR for Proteins
domain: biology
course: structural-biology
prerequisites:
- id: protein-folding-and-chaperones
  type: hard
- id: amino-acid-structure-and-properties
  type: soft
builds-toward:
- noesy-and-distance-constraints
tags:
- NMR
- nuclear-magnetic-resonance
- chemical-shift
- protein-dynamics
- solution-structure
stage: expert
status: validated
---
# NMR for Proteins

## Core Idea
Nuclear magnetic resonance (NMR) spectroscopy determines protein structures and dynamics in solution by exploiting the magnetic properties of atomic nuclei (primarily 1H, 13C, 15N). In a strong magnetic field, nuclear spins resonate at frequencies (chemical shifts) sensitive to their local electronic environment, and through-space (NOE) and through-bond (J-coupling) interactions between nuclei provide distance and connectivity information. Unlike X-ray crystallography and cryo-EM, NMR studies proteins in solution at near-physiological conditions and provides unique information about molecular dynamics on timescales from picoseconds to seconds. The primary limitation is molecular size — NMR is most effective for proteins below ~40 kDa (with special techniques extending to ~100 kDa), because larger proteins have slower tumbling and broader linewidths that degrade spectral resolution.

## Questions

```yaml
- question: "Why is protein NMR typically limited to molecules below ~40 kDa, while X-ray crystallography and cryo-EM have no practical upper size limit?"
  type: multiple-choice
  options:
    - "NMR magnets cannot produce strong enough fields for larger molecules"
    - "Larger proteins tumble more slowly in solution, which increases transverse relaxation rates (broader NMR lines) and causes severe spectral overlap — the signals from thousands of atoms become too broad and too overlapping to resolve"
    - "Larger proteins are always insoluble, so NMR cannot be performed"
    - "NMR requires crystallization, which fails for large proteins"
  answer: 1
  explanation: "NMR resolution depends on the linewidth of each resonance, which is inversely proportional to the transverse relaxation time (T2). T2 decreases as molecular tumbling slows (larger molecules tumble more slowly). Broader lines mean more spectral overlap, and with thousands of 1H, 13C, and 15N resonances in a protein, the spectrum becomes uninterpretable above ~40 kDa with standard methods. TROSY (Transverse Relaxation-Optimized Spectroscopy) selects for the slowest-relaxing component of each multiplet, extending the practical limit to ~100 kDa, but this requires deuteration and is still far more limited than crystallography or cryo-EM in terms of molecular size."

- question: "NMR provides a single, unique structure for a protein, just like X-ray crystallography."
  type: true-false
  answer: false
  explanation: "NMR structure determination produces an ensemble of structures, not a single one. The experimental data (NOE distance restraints, dihedral angle restraints, residual dipolar couplings) constrain the structure but do not uniquely determine it — there are typically more degrees of freedom than restraints. Simulated annealing or molecular dynamics calculations generate an ensemble of structures that all satisfy the experimental restraints equally well. This ensemble reflects both the uncertainty in the data and the genuine conformational dynamics of the protein in solution. Regions that are well-defined across the ensemble (low RMSD) are conformationally rigid; regions that vary (high RMSD) are genuinely flexible. This is actually an advantage — the ensemble captures biological dynamics that a single crystal structure cannot."

- question: "What information does NMR provide about protein dynamics that crystallography cannot?"
  type: short-answer
  answer: "NMR measures molecular motions over a wide range of timescales: backbone and side chain dynamics on the ps-ns timescale (from 15N and 13C relaxation measurements — order parameters quantifying the amplitude of motion), conformational exchange on the us-ms timescale (from relaxation dispersion experiments — detecting interconversion between distinct conformational states), and slow exchange on the ms-s timescale (from hydrogen-deuterium exchange — measuring solvent accessibility reflecting protein breathing motions). This multi-timescale dynamic information reveals which regions are rigid vs. flexible, which residues interconvert between multiple conformations relevant to function (enzyme catalysis, allosteric regulation, ligand binding), and which regions are transiently exposed. X-ray crystallography provides only B-factors (which conflate dynamics with crystal disorder) and cannot access these timescale-specific dynamic measurements."
  explanation: "NMR dynamics studies have revealed that enzyme catalysis often involves conformational fluctuations on the same timescale as the catalytic rate — suggesting that dynamics are rate-limiting. Allosteric communication has been shown to propagate through networks of dynamically coupled residues. These insights are invisible to static structural methods."
```

## Explainer

X-ray crystallography and cryo-EM provide exquisitely detailed snapshots of protein structure, but they are fundamentally static methods — they capture the molecule frozen in time (literally, in the case of cryo-EM). **NMR spectroscopy** complements these methods by studying proteins in solution, at physiological temperatures, and with unique sensitivity to molecular dynamics. For understanding how proteins actually work — the conformational changes they undergo, the flexible regions they use for recognition, the dynamic fluctuations that enable catalysis — NMR is often the method of choice.

The physical basis of NMR is nuclear spin. Certain atomic nuclei (1H, 13C, 15N — all with spin-1/2) behave as tiny magnets that align in an external magnetic field. When perturbed by radiofrequency pulses, they resonate at characteristic frequencies (**chemical shifts**) that depend on the local electronic environment. A proton in an alpha helix has a different chemical shift than one in a beta sheet, and one near an aromatic ring differs from one in a hydrophobic core. The **chemical shift fingerprint** — the 2D HSQC spectrum showing one peak for each amide NH in the backbone — is the starting point for protein NMR. Each peak corresponds to one residue, and its position reports on the residue's local environment.

**Structure determination** by NMR relies primarily on the **Nuclear Overhauser Effect** (NOE) — a through-space interaction between protons that are close in space (< 5 Angstroms) regardless of their position in the amino acid sequence. A network of thousands of NOE-derived distance restraints, combined with backbone dihedral angle restraints (from chemical shifts and J-couplings) and residual dipolar couplings (which constrain bond orientations relative to the magnetic field), defines the three-dimensional structure. Computational methods (simulated annealing, molecular dynamics) generate an ensemble of structures consistent with all restraints. Well-determined regions converge to a tight ensemble; flexible regions diverge — providing a direct readout of structural precision and molecular flexibility.

The unique strength of NMR is **dynamics measurement**. By analyzing how nuclear spins relax back to equilibrium after perturbation, NMR quantifies molecular motion on multiple timescales. **Fast motions** (ps-ns) — bond vibrations and loop fluctuations — are measured by 15N and 13C relaxation rates and expressed as order parameters (S^2, ranging from 0 for fully disordered to 1 for rigid). **Intermediate motions** (us-ms) — conformational exchange between distinct states — are detected by relaxation dispersion experiments that reveal the populations, interconversion rates, and chemical shift differences between the exchanging states. **Slow motions** (ms-s) — protein "breathing" that transiently exposes the hydrophobic core — are measured by hydrogen-deuterium exchange. This multi-timescale dynamic portrait is unique to NMR and has transformed our understanding of how proteins use motion for function.
