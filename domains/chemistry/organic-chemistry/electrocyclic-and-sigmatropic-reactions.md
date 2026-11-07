---
id: electrocyclic-and-sigmatropic-reactions
title: Electrocyclic and Sigmatropic Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: diels-alder-reaction
  type: hard
- id: conjugated-dienes
  type: hard
- id: huckel-molecular-orbital-theory
  type: soft
- id: bonding-antibonding-orbitals
  type: soft
- id: photochemistry-excited-state-reactions
  type: soft
builds-toward: []
tags:
- pericyclic reactions
- Woodward-Hoffmann rules
- conrotatory
- disrotatory
- Cope rearrangement
- Claisen rearrangement
stage: formal-systems
status: validated
---

# Electrocyclic and Sigmatropic Reactions

## Core Idea
Electrocyclic and sigmatropic reactions are pericyclic: bonds form and break in one concerted step through a cyclic transition state. In an electrocyclic reaction, a conjugated polyene closes into a ring by joining its two ends, or a ring opens in reverse. In a sigmatropic rearrangement, a σ bond migrates across a π system, as in the [3,3] Cope and Claisen rearrangements. The Woodward–Hoffmann rules, based on orbital symmetry, predict which stereochemical paths are allowed under heat and under light.

## How It's Best Learned
Draw the π molecular orbitals of butadiene and hexatriene and identify the HOMO in each. Rotate the terminal lobes with physical models or careful sketches to see which rotation brings same-phase lobes together. Then work through the stereochemistry of a substituted triene and a substituted cyclobutene. For sigmatropic reactions, number the atoms on each fragment to name the shift, and map the Cope and Claisen rearrangements onto a six-atom chair.

## Common Misconceptions
- Heat and light give the same stereochemistry in an electrocyclic reaction. (The rules reverse under light; a thermal 4n-electron closure is conrotatory, while the photochemical one is disrotatory.)
- Pericyclic reactions go through ionic or radical intermediates. (They are concerted; all bond changes happen in one step, which is why their stereochemistry is so tightly controlled.)
- In a [3,3] shift, three atoms move. (The numbers count the atoms on each fragment between the old and new σ bond; in a Cope rearrangement the σ bond moves from between C1 and C1′ to between C3 and C3′.)

## Questions

```yaml
- question: "Under thermal conditions, how does a conjugated triene (6 π electrons) close to a cyclohexadiene?"
  type: multiple-choice
  options: ["Conrotatory", "Disrotatory", "Either, with equal ease", "It cannot close thermally"]
  answer: 1
  explanation: "For 4n + 2 π electrons, thermal electrocyclic reactions are disrotatory. The HOMO of a hexatriene has its terminal lobes in phase on the same face, so turning both ends in opposite directions brings matching lobes together."
- question: "A photochemical electrocyclic ring closure follows the same rotational mode as the corresponding thermal reaction."
  type: true-false
  answer: false
  explanation: "Light promotes an electron into the next orbital, which becomes the new HOMO and has the opposite terminal symmetry. The allowed rotation therefore switches between conrotatory and disrotatory."
- question: "Heating an allyl vinyl ether gives a γ,δ-unsaturated carbonyl compound. What is this reaction?"
  type: multiple-choice
  options: ["A [1,5] hydrogen shift", "A Diels–Alder cycloaddition", "A [3,3] Claisen rearrangement", "An electrocyclic ring opening"]
  answer: 2
  explanation: "The Claisen rearrangement is a [3,3] sigmatropic shift. The C–O σ bond breaks, a new C–C σ bond forms three atoms along each fragment, and the vinyl ether becomes a carbonyl."
- question: "Explain why the thermal ring closure of butadiene to cyclobutene is conrotatory."
  type: short-answer
  answer: "In the ground state, the HOMO of butadiene is ψ₂, whose terminal p lobes have opposite phase on the same face. Only turning both ends in the same direction (conrotation) brings same-phase lobes together to form the new σ bond."
  explanation: "The stereochemistry follows from the symmetry of the HOMO's end lobes. This is the frontier-orbital view of the Woodward–Hoffmann rules."
```

## Explainer

In a pericyclic reaction, all the bond changes happen at once, through a ring-shaped transition state, with no intermediate. You have already seen one class, the Diels–Alder cycloaddition. Two more classes complete the main set: electrocyclic reactions and sigmatropic rearrangements.

An electrocyclic reaction joins the two ends of a conjugated polyene with a new σ bond, making a ring with one fewer π bond. Hexa-1,3,5-triene closes to cyclohexa-1,3-diene. The reverse, a ring opening, is also electrocyclic. For the new bond to form, the p orbitals at the two ends must each turn 90° so they point at each other. They can turn the same way, which is conrotatory, or opposite ways, which is disrotatory. The choice decides where substituents end up.

Robert Burns Woodward and Roald Hoffmann explained the choice in 1965 using orbital symmetry. A simple version looks at the highest occupied molecular orbital, the HOMO. The new bond forms only if the lobes that meet have the same phase. In butadiene, with four π electrons, the HOMO has opposite-phase lobes on the same face at its two ends, so the ends must rotate together, conrotatory. In hexatriene, with six π electrons, the end lobes on the same face match, so the ends rotate opposite ways, disrotatory. The general thermal rule is conrotatory for 4n π electrons and disrotatory for 4n + 2. Light promotes an electron into the next orbital, flips the end symmetry, and reverses both rules.

Stereochemistry makes these rules visible. Heating (2E,4Z,6E)-octa-2,4,6-triene gives only cis-5,6-dimethylcyclohexa-1,3-diene, because disrotatory closure turns both methyl groups toward the same face.

A sigmatropic rearrangement moves a σ bond to a new position across a π system. It is named [i,j], where i and j count the atoms on each fragment from the old bond to the new one. The most useful are [3,3] shifts. In the Cope rearrangement, a 1,5-diene reorganizes into an isomeric 1,5-diene. In the Claisen rearrangement, an allyl vinyl ether becomes a γ,δ-unsaturated carbonyl compound, and the strong C=O bond drives the reaction forward. Both usually pass through a chair-like six-membered transition state, which lets you predict the alkene geometry of the product.
