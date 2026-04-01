---
id: mass-spectrometry-structural
title: Mass Spectrometry Structural
domain: biology
course: structural-biology
prerequisites:
- id: protein-folding-and-chaperones
  type: hard
- id: amino-acid-structure-and-properties
  type: soft
builds-toward:
- hydrogen-deuterium-exchange
tags:
- mass-spectrometry
- native-MS
- cross-linking-MS
- XL-MS
- structural-proteomics
stage: expert
status: validated
---
# Mass Spectrometry Structural

## Core Idea
Structural mass spectrometry encompasses a suite of MS-based techniques that provide information about protein structure, interactions, and dynamics. Native MS preserves non-covalent complexes in the gas phase, measuring the intact mass and stoichiometry of protein assemblies. Cross-linking MS (XL-MS) identifies residue pairs in spatial proximity by chemically cross-linking them and identifying the cross-linked peptides by LC-MS/MS, providing distance constraints analogous to NMR NOEs but applicable to much larger systems. These approaches complement high-resolution structural methods by characterizing heterogeneous, dynamic, and transient interactions that resist crystallization, providing restraints for integrative structural modeling.

## Questions

```yaml
- question: "Cross-linking mass spectrometry (XL-MS) uses chemical cross-linkers to connect residue pairs that are within a defined distance. How does this provide structural information?"
  type: multiple-choice
  options:
    - "Cross-linkers modify all residues equally, so no structural information is obtained"
    - "Each identified cross-link establishes a maximum distance constraint between the two connected residues (typically ~25-30 Angstroms for common amine-reactive cross-linkers like DSS/BS3), providing spatial proximity information analogous to long-range NMR NOEs but applicable to much larger complexes"
    - "Cross-linking mass spectrometry measures the molecular weight of each cross-linker"
    - "Cross-links only form between residues on the protein surface, providing surface mapping information"
  answer: 1
  explanation: "When a cross-linker (like DSS, with a ~11.4 Angstrom spacer arm) bridges two lysine residues, it establishes that those lysines are within cross-linkable distance (~25-30 Angstroms, accounting for the spacer arm plus side chain flexibility). LC-MS/MS identification of the cross-linked peptides reveals which residue pairs are proximal. With hundreds of cross-links across a large complex, the data provides a network of distance constraints that can be used for structural modeling — docking subunits, validating computational models, or building integrative models. Unlike NMR (limited to ~40 kDa), XL-MS works on megadalton-scale complexes and in heterogeneous, in-cell environments."

- question: "Native mass spectrometry requires denaturing the protein complex to measure its mass."
  type: true-false
  answer: false
  explanation: "Native MS is defined by its preservation of non-covalent interactions. Gentle electrospray ionization from a non-denaturing buffer (ammonium acetate, not organic solvents or acid) transfers intact protein complexes to the gas phase with their non-covalent associations preserved. The measured mass reveals the complex stoichiometry (how many copies of each subunit), and collision-induced dissociation can probe the stability and connectivity of subunits. Native MS can analyze complexes up to several megadaltons (ribosomes, proteasomes) and can resolve multiple coexisting stoichiometries in a heterogeneous sample — providing population-level information about complex assembly."

- question: "What advantage does XL-MS have over crystallography for studying large, flexible, multi-component complexes?"
  type: short-answer
  answer: "Large, flexible, multi-component complexes often resist crystallization (heterogeneity and flexibility prevent lattice formation) and may exceed the size limits of NMR. XL-MS works in solution under near-native conditions and tolerates heterogeneity — different conformational states and subcomplexes are cross-linked simultaneously, and the cross-links from each state contribute to the data. The resulting distance constraints can be integrated with other structural data (cryo-EM density maps, SAXS envelopes, computational models) in integrative modeling frameworks. XL-MS is also applicable in living cells (in-cell XL-MS), capturing interactions in their native environment including transient and weak associations that do not survive purification."
  explanation: "The nuclear pore complex (~120 MDa, 30+ subunit types) was structurally characterized in large part through integrative modeling combining XL-MS distance constraints with cryo-ET density, crystallographic substructures, and SAXS data — a landmark achievement in integrative structural biology."
```

## Explainer

The traditional structural biology methods — crystallography, cryo-EM, NMR — each have blind spots. Crystallography requires crystals, cryo-EM struggles with small or heterogeneous specimens, and NMR is limited to small proteins. **Structural mass spectrometry** fills these gaps by providing structural information from heterogeneous, dynamic, and even in-cell samples, with no size limit and minimal sample requirements.

**Native mass spectrometry** uses gentle electrospray ionization to transfer intact protein complexes from solution to the gas phase without disrupting non-covalent interactions. The measured mass-to-charge ratio reveals the total mass of the complex, from which stoichiometry can be deduced. For a heteromeric complex, native MS answers a fundamental question that can be surprisingly difficult to answer otherwise: how many copies of each subunit are present? Collision-induced dissociation (CID) — gradually increasing the collision energy to disassemble the complex in the gas phase — reveals which subunits are peripheral (ejected first) and which are core (released last), providing topology information. Native MS has characterized complexes from small heterodimers to intact ribosomes and virus capsids.

**Cross-linking mass spectrometry (XL-MS)** chemically bridges residue pairs that are in spatial proximity. A bifunctional cross-linker (like DSS or BS3, which reacts with primary amines on lysine side chains) is added to the protein or complex in solution. Cross-links form between lysine pairs within ~25-30 Angstroms. The cross-linked protein is then digested with protease, and the resulting peptide mixture is analyzed by LC-MS/MS. Specialized software (like pLink, XlinkX, or xiSearch) identifies cross-linked peptide pairs from their characteristic fragmentation patterns. Each identified cross-link is a **distance constraint** — the two residues must be within cross-linkable distance in the native structure.

The power of structural MS is most apparent in **integrative structural biology** — combining data from multiple techniques to model structures that no single method can determine alone. The nuclear pore complex, the mediator complex, and chromatin remodeling machines have all been structurally characterized using integrative approaches where XL-MS distance constraints guide the assembly of subunit crystal structures into the overall complex architecture, constrained by cryo-EM density maps and SAXS shape information. Structural MS provides the "glue" that connects high-resolution substructures into the complete biological assembly.
