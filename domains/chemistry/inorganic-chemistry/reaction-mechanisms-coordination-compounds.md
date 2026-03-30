---
id: reaction-mechanisms-coordination-compounds
title: Reaction Mechanisms of Coordination Compounds (Substitution)
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: crystal-field-theory
  type: hard
- id: isomerism-coordination-compounds
  type: soft
- id: chelate-effect-stability-constants
  type: soft
builds-toward:
- electron-transfer-reactions
- homogeneous-catalysis-mechanisms
tags:
- substitution mechanisms
- dissociative
- associative
- interchange
- trans effect
- lability
stage: advanced
status: validated
---

# Reaction Mechanisms of Coordination Compounds (Substitution)

## Core Idea
Ligand substitution in coordination compounds proceeds through dissociative (D), associative (A), or interchange (I) mechanisms, analogous to SN1, SN2, and concerted pathways in organic chemistry. Octahedral complexes predominantly undergo dissociative substitution, while square planar complexes favor associative substitution. The trans effect governs the selectivity of substitution in square planar complexes, and crystal field activation energy (CFAE) determines whether a complex is labile or inert.

## Questions

```yaml
- question: "Most octahedral substitution reactions proceed by a dissociative interchange (Id) mechanism rather than a purely associative (A) mechanism. What is the primary reason?"
  type: multiple-choice
  options:
    - "Octahedral complexes are always more thermodynamically stable, preventing association"
    - "The metal center in an octahedral complex is sterically crowded by six ligands, making it difficult for a seventh ligand to approach — bond breaking (dissociation) must precede or accompany bond making"
    - "The CFSE of the seven-coordinate transition state is always zero"
    - "Octahedral complexes cannot change their coordination number under any circumstances"
  answer: 1
  explanation: "Steric crowding at the metal center is the dominant factor. Six ligands around a metal ion leave little room for a seventh to approach, making a purely associative mechanism (increasing coordination number to 7 in the transition state) energetically costly. Instead, the departing ligand must partially dissociate (lengthening its bond) before or as the incoming ligand begins to bond. This is the dissociative interchange (Id) pathway. Square planar complexes, by contrast, have open coordination sites above and below the plane, readily accommodating a fifth ligand — which is why they favor associative (A) mechanisms."

- question: "The trans effect in square planar Pt(II) chemistry refers to the ability of certain ligands to labilize the ligand trans to themselves, facilitating its substitution."
  type: true-false
  answer: true
  explanation: "The trans effect is a kinetic phenomenon: ligands with a strong trans effect (like CO, CN⁻, C₂H₄, PR₃) weaken the bond to the ligand directly opposite them in a square planar complex, making that position more susceptible to substitution. The trans influence is the related ground-state thermodynamic effect (weakening of the trans M-L bond length). The trans effect order roughly follows: H₂O < NH₃ < Cl⁻ < Br⁻ < I⁻ < NO₂⁻ < CO ≈ CN⁻ ≈ C₂H₄. This effect is critically important in synthesis — it allows chemists to direct which ligand is replaced, enabling stereoselective preparation of specific isomers like cisplatin."

- question: "d³ and low-spin d⁶ octahedral complexes are kinetically inert, while d⁰ and high-spin d⁵ complexes are kinetically labile."
  type: true-false
  answer: true
  explanation: "Kinetic inertness correlates with crystal field activation energy (CFAE) — the loss of CFSE when moving from the octahedral ground state to the transition state geometry. d³ (t₂g³) and low-spin d⁶ (t₂g⁶) configurations have large CFSE in the octahedral geometry and lose significant stabilization in any transition state with a different coordination number, creating a large activation barrier. d⁰ has no d-electrons and thus no CFSE to lose, while high-spin d⁵ (t₂g³ eg²) has zero CFSE (each orbital singly occupied), so neither configuration faces a CFSE-based barrier. This is why Cr³⁺ (d³) and Co³⁺ low-spin (d⁶) complexes can be isolated as specific isomers that persist for days, while [Mn(H₂O)₆]²⁺ (d⁵ high-spin) exchanges water molecules in microseconds."

- question: "Explain how the trans effect is used to synthesize cisplatin, [Pt(NH₃)₂Cl₂], selectively rather than transplatin."
  type: short-answer
  answer: "Starting from [PtCl₄]²⁻, the first substitution replaces one Cl⁻ with NH₃ to give [PtCl₃(NH₃)]⁻. For the second substitution, the trans effect determines which Cl⁻ is replaced. Cl⁻ has a stronger trans effect than NH₃, so it labilizes the ligand trans to itself more than NH₃ does. The Cl⁻ trans to the newly added NH₃ is less labile (NH₃ has weak trans effect), while the Cl⁻ trans to another Cl⁻ is more labile (Cl⁻ has moderate trans effect). The incoming second NH₃ therefore replaces a Cl⁻ that is trans to Cl⁻, placing the second NH₃ cis to the first. This gives cisplatin. To make transplatin, you start from [Pt(NH₃)₄]²⁺ and add Cl⁻, which replaces NH₃ trans to NH₃ — but since all positions are equivalent initially, selective trans synthesis from the tetrachloride is the standard route to the cis isomer."
  explanation: "This synthesis elegantly demonstrates how understanding mechanism enables stereocontrol. Cisplatin is one of the most important anticancer drugs, while transplatin is therapeutically inactive — so the ability to selectively make one isomer is medically critical."
```

## Explainer

Understanding how coordination compounds react is as important as understanding their structure. Ligand substitution — replacing one ligand with another — is the most common reaction type for coordination compounds, and its mechanism determines the rate, selectivity, and stereochemical outcome. The mechanistic framework parallels organic chemistry but with important differences arising from the metal center's electronic structure.

Octahedral substitution reactions predominantly follow dissociative or dissociative interchange pathways. The transition state involves partial dissociation of the leaving ligand, generating a five-coordinate intermediate (or transition state) before the incoming ligand bonds. Evidence for this comes from the rate law: substitution rates for octahedral complexes typically depend on the concentration of the complex but not on the concentration of the incoming ligand, indicating that bond breaking is the rate-determining step. The identity of the incoming ligand has little effect on the rate — consistent with dissociation occurring before association. Crystal field activation energy (CFAE) provides a theoretical framework for predicting lability: complexes that lose significant CFSE upon distorting to the transition-state geometry are kinetically inert, while those with little CFSE to lose are labile.

Square planar substitution follows the opposite pattern: associative mechanisms dominate. The open coordination sites above and below the molecular plane allow a fifth ligand to approach and form a five-coordinate trigonal bipyramidal transition state. The rate law shows dependence on both the complex and incoming ligand concentrations. Most importantly, the trans effect governs selectivity: ligands with strong trans influence weaken the bond to the ligand opposite them, directing which position is substituted. This kinetic directing effect enables stereochemical control — the synthesis of cisplatin being the most celebrated example.

The Taube classification of complexes as labile or inert provides practical guidance. Labile complexes (d⁰, d¹, high-spin d⁴-d⁷, d⁹, d¹⁰) exchange ligands rapidly — typically with half-lives of seconds or less. Inert complexes (d³, low-spin d⁴-d⁶) exchange slowly, with half-lives of hours to days. Note that inert does not mean thermodynamically stable: a complex can be thermodynamically unstable but kinetically inert (it wants to react but cannot reach the products quickly). This distinction between thermodynamic stability and kinetic lability is one of the most important concepts in coordination chemistry.
