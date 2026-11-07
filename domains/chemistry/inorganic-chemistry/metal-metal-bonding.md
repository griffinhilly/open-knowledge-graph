---
id: metal-metal-bonding
title: Metal-Metal Bonding
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: mo-theory-transition-metal-complexes
  type: hard
- id: organometallic-chemistry-fundamentals
  type: soft
builds-toward:
- cluster-compounds
tags:
- metal-metal bonds
- quadruple bond
- delta bond
- bond order
- multiply bonded metals
stage: expert
status: validated
---

# Metal-Metal Bonding

## Core Idea
Transition metals can form direct metal-metal bonds with bond orders from one (single) through four (quadruple), the latter involving sigma, two pi, and one delta component. The delta bond — unique to metal-metal bonding — arises from face-to-face overlap of d_xy orbitals and explains the eclipsed geometry of quadruply bonded species like [Re₂Cl₈]²⁻. Metal-metal bond strength and order are analyzed using the MO framework, with the effective bond order determined by the number of bonding minus antibonding electrons divided by two.

## How It's Best Learned
Draw the d_z², d_xz, d_yz and d_xy orbitals on two metals facing each other along z, and sketch how each pair overlaps: head-on, side-on, and face-to-face. Then build the σ < π < δ < δ* < π* < σ* ladder and fill it for d⁴-d⁴, d⁵-d⁵ and d⁶-d⁶ pairs, computing the bond order each time. Rotate one half of a model by 45° to see the δ overlap vanish.

## Common Misconceptions
- A quadruple bond is four times as strong as a single bond. (The π and δ components are weaker than the σ component, and the δ component is the weakest, so a quadruple bond is far less than four times as strong.)
- All five d-orbitals on each metal take part in the quadruple bond. (Four do; in [Re₂Cl₈]²⁻ the d_x²−y² orbitals point at the chloride ligands and are used for metal-ligand bonding.)
- The eclipsed Cl arrangement in [Re₂Cl₈]²⁻ is chosen to reduce steric clash. (Steric repulsion alone would favor the staggered form; the eclipsed geometry is needed for δ overlap.)
- Adding more d-electrons to a dimer always strengthens the metal-metal bond. (Beyond d⁴-d⁴ the extra electrons enter δ*, π* and σ* orbitals, so the bond order falls.)

## Questions

```yaml
- question: "The quadruple bond in [Re₂Cl₈]²⁻ consists of which types of orbital interactions?"
  type: multiple-choice
  options:
    - "Four equivalent sigma bonds"
    - "One sigma (d_z²-d_z²), two pi (d_xz-d_xz and d_yz-d_yz), and one delta (d_xy-d_xy) bond"
    - "Two sigma and two pi bonds, like a C≡C triple bond with an extra sigma"
    - "One sigma, one pi, and two delta bonds"
  answer: 1
  explanation: "The quadruple bond uses four of the five d-orbitals on each metal. The d_z² orbitals overlap head-on (sigma). The d_xz and d_yz pairs overlap laterally (two pi bonds). The d_xy orbitals overlap face-to-face (delta bond). The d_x²−y² orbitals on each metal point at the chloride ligands and are used for metal-ligand bonding, not metal-metal bonding. The delta component is uniquely characteristic of metal-metal bonding — it has no analogue in organic chemistry — and it requires the chloride ligands to be eclipsed rather than staggered, because staggering would destroy the d_xy-d_xy overlap."

- question: "The eclipsed geometry of the chloride ligands in [Re₂Cl₈]²⁻ is a direct consequence of the delta bond between the two rhenium atoms."
  type: true-false
  answer: true
  explanation: "Delta bonds form from face-to-face overlap of d_xy orbitals on adjacent metals. This overlap is maximized when the ligands on the two metals are eclipsed (aligned) and goes to zero when they are staggered (rotated 45°). The delta bond energy is sufficiently large to overcome the steric preference for staggered ligands, locking the complex in the eclipsed conformation. This is a striking example of electronic structure dictating molecular geometry: without the delta bond, the eight chlorides would prefer a staggered arrangement to minimize Cl-Cl repulsion."

- question: "A dinuclear metal complex has the metal-metal MO configuration σ²π⁴δ²δ*²π*². What is the effective bond order?"
  type: short-answer
  answer: "The bond order is 2. Bonding electrons: σ²π⁴δ² = 8. Antibonding electrons: δ*²π*² = 4. Bond order = (8 − 4)/2 = 2, a net double bond."
  explanation: "Bond order = (bonding electrons − antibonding electrons)/2. The filled delta and delta* cancel (no net delta bonding), and two of the four pi electrons are canceled by the two pi* electrons, leaving the sigma bond and one net pi bond. A common error is to forget the π* electrons and get a bond order of 3, so careful counting of antibonding electrons is essential."

- question: "Explain why the metal-metal bond in [Mo₂(CH₃COO)₄] (Mo-Mo distance ~2.09 Å) is much shorter than a typical Mo-Mo single bond (~2.8 Å), and describe the bonding."
  type: short-answer
  answer: "The short Mo-Mo distance indicates a bond order much higher than one. [Mo₂(CH₃COO)₄] contains a Mo-Mo quadruple bond: σ²π⁴δ². Each Mo is in the +2 oxidation state (d⁴), contributing 4 electrons; the total of 8 metal electrons fills the σ, two π, and δ bonding MOs exactly. No antibonding orbitals are occupied, giving the maximum bond order of 4. The acetate ligands bridge the two metals, holding them in proximity, and the eclipsed arrangement of the bridging carboxylates is enforced by the delta bond. The short bond distance (comparable to a Mo≡Mo triple bond in some compounds) reflects the quadruple bond's high electron density between the nuclei."
  explanation: "The discovery of the quadruple bond in [Re₂Cl₈]²⁻ by F.A. Cotton in 1964 opened an entirely new chapter in inorganic chemistry. It demonstrated that metals could form bonds with no organic analogue and led to the broader study of multiply bonded transition metal compounds."
```

## Explainer

The concept of metal-metal bonding extends the molecular orbital framework to direct interactions between two metal centers. While single metal-metal bonds are common (as in Mn₂(CO)₁₀, where each Mn contributes one electron to the bond to achieve 18 electrons), the truly distinctive feature of metal-metal bonding is the possibility of bond orders up to four — including the delta bond, which has no counterpart in organic chemistry.

The delta bond arises from face-to-face overlap of d_xy orbitals on two adjacent metal atoms. Unlike sigma bonds (head-on overlap, cylindrically symmetric) and pi bonds (lateral overlap, one nodal plane containing the bond axis), the delta bond has two nodal planes containing the bond axis. The overlap is weaker than sigma or pi, making the delta bond the weakest component of a quadruple bond, but it has profound structural consequences: it locks the complex into an eclipsed ligand arrangement because rotation about the metal-metal axis reduces the d_xy overlap, which falls to zero at the staggered (45°) arrangement.

The MO diagram for a metal-metal bond in an M₂L₈ species arranges the molecular orbitals in order of increasing energy: σ < π < δ < δ* < π* < σ*. For a quadruple bond (8 bonding electrons from two d⁴ metals), the configuration is σ²π⁴δ², and all bonding orbitals are filled with no antibonding occupation. As electrons are added (moving to heavier d⁵, d⁶, d⁷ metals), they enter antibonding orbitals, reducing the bond order progressively: σ²π⁴δ²δ*² gives a triple bond (bond order 3), σ²π⁴δ²δ*²π*⁴ gives a single bond (bond order 1). This systematic variation in bond order produces measurable trends in bond lengths and vibrational frequencies across a series of isostructural dinuclear compounds.

Metal-metal bonding is not limited to dinuclear species. When multiple metal atoms form M-M bonds in a single compound, the result is a metal cluster — a topic with its own rich chemistry. The concepts of sigma, pi, and delta metal-metal interactions developed here extend directly to triangular, square, octahedral, and larger metal clusters, where the delocalization of metal-metal bonding electrons across multiple centers creates electronic structures that parallel the band theory of bulk metals.
