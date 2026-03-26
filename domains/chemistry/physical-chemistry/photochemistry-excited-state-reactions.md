---
id: photochemistry-excited-state-reactions
title: 'Photochemistry: Excited State Reactions'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: electronic-spectroscopy-theory
  type: hard
- id: reaction-mechanisms-elementary-steps
  type: hard
- id: excited-state-decay-pathways
  type: soft
- id: photochemical-processes-excited-states
  type: soft
- id: fluorescence-quantum-yield-lifetime
  type: soft
builds-toward: []
tags:
- photochemistry
- excited-states
- reaction-mechanisms
stage: advanced
status: validated
---
# Photochemistry: Excited State Reactions

## Core Idea
Excited electronic states have different geometries, orbital occupancy, and reactivity than ground states. Photochemical reactions proceed via different mechanisms and activation barriers; forbidden ground-state reactions become allowed from excited states. Photochemistry enables reactions that violate thermal symmetry rules and has applications in photosynthesis, vision, and synthesis.

## Questions

```yaml
- question: "A [2+2] cycloaddition between two alkenes is thermally forbidden but proceeds readily under UV irradiation. What does the photon actually do to enable this reaction?"
  type: multiple-choice
  options:
    - "It provides the activation energy needed to push the reaction over the thermal energy barrier"
    - "It changes the orbital occupancy of the excited state, altering the orbital symmetry so the reaction becomes symmetry-allowed"
    - "It breaks one of the double bonds, making the alkene more reactive toward addition"
    - "It raises the temperature of the molecules locally so they can overcome the thermal barrier"
  answer: 1
  explanation: "The [2+2] cycloaddition is thermally forbidden because the orbital symmetry of the ground-state reactants does not correlate smoothly to products — a symmetry-imposed energy barrier exists. UV light promotes an electron to a higher orbital, changing the electron configuration and therefore the orbital symmetry of the excited state. In the excited state, the symmetry now permits smooth orbital correlation to the cyclobutane product — the reaction is photochemically allowed. Options A and D reflect the common misconception that photons merely supply energy; they miss the key point that orbital symmetry, not just energy, governs reaction accessibility."

- question: "In the retinal chromophore of rhodopsin (vision), light triggers a cis-to-trans isomerization that has a large thermal barrier. Which description best explains why the excited state undergoes this reaction so readily?"
  type: multiple-choice
  options:
    - "The photon heats the retinal molecule so it can surmount the thermal isomerization barrier"
    - "On the excited-state potential energy surface, the barrier for cis-to-trans isomerization is nearly absent — the molecule rolls downhill toward the trans configuration"
    - "The excited state has a higher bond order for the C=C bond, making rotation easier"
    - "The photon directly breaks the π-bond, allowing free rotation before it reforms"
  answer: 1
  explanation: "Excited-state potential energy surfaces have completely different topography from the ground-state surface. For retinal, the excited-state surface has a minimum near the perpendicular (90°) geometry and slopes downhill toward the trans product — the reaction is nearly barrierless. This is why it occurs in femtoseconds despite being hindered thermally. The photon does not heat the molecule or mechanically break the bond; it promotes the electron to a state where the reaction coordinate is downhill rather than uphill."

- question: "Providing more photons of higher energy is generally sufficient to make any thermally forbidden reaction proceed photochemically."
  type: true-false
  answer: false
  explanation: "Whether a reaction is photochemically allowed depends on orbital symmetry in the excited state, not just energy input. Some reactions that are thermally forbidden are photochemically allowed (like thermal conrotatory vs. photochemical disrotatory ring closures), but photochemical excitation still must produce an excited state with the right symmetry for the desired product. Additionally, the excited molecule can deactivate via fluorescence, phosphorescence, or non-reactive pathways before reaching the photoproduct. Simply increasing photon energy or intensity does not override these symmetry constraints."

- question: "The Woodward–Hoffmann rules predict that a thermally forbidden reaction can become photochemically allowed because excitation changes the electron configuration and therefore the orbital symmetry of the reactive species."
  type: true-false
  answer: true
  explanation: "This is the central prediction of Woodward–Hoffmann orbital symmetry conservation. A thermal reaction requires the orbital symmetry of starting material and product to correlate smoothly (be 'symmetry-allowed') on the ground-state surface. When a reaction is symmetry-forbidden thermally, the correlation involves an orbital crossing that creates a high barrier. After photon absorption, a different orbital is occupied, and the symmetry correlation in the excited state may be allowed. This is precisely why electrocyclic reactions (like conjugated diene ring closure) have opposite stereochemical outcomes under thermal vs. photochemical conditions."

- question: "Why is it more accurate to say that a photon 'changes the rules' of a reaction rather than simply 'provides the energy' needed to overcome a thermal barrier?"
  type: short-answer
  answer: "A photon promotes an electron to a higher-energy orbital, creating an electronically excited state with a different electron configuration. This different configuration changes the orbital symmetry of the molecule — meaning the symmetry relationships that determine which reactions are allowed or forbidden are fundamentally altered. A thermally forbidden reaction has a symmetry-imposed barrier regardless of how much thermal energy is available; adding more heat cannot fix a symmetry mismatch. The excited state accesses a different potential energy surface with different topology, where the same bond changes that were symmetry-forbidden become symmetry-allowed. The photon is not surmounting the same barrier — it is accessing a different reaction pathway entirely."
  explanation: "This distinction matters practically: reactions like [2+2] cycloadditions cannot be made to proceed thermally even at very high temperatures because the orbital symmetry barrier is not a simple kinetic barrier. Only photochemical excitation, which changes the orbital occupancy and hence the symmetry, opens the pathway. Conversely, some photochemical reactions cannot be forced thermally for the same reason."
```

## Explainer

From your work on electronic spectroscopy, you know that absorbing a photon promotes an electron from a bonding or nonbonding orbital into a higher-energy orbital. What photochemistry adds is the recognition that this electronically excited molecule is, in effect, a *different chemical species* — one with its own geometry, its own reactivity, and its own set of accessible reaction pathways. The excited state has a different electron configuration than the ground state, which means different bond orders, different charge distributions, and often a dramatically different molecular shape. A molecule that is perfectly stable on the ground-state surface may be highly reactive on the excited-state surface.

The key insight connecting this to reaction mechanisms is the **Woodward–Hoffmann rules** and orbital symmetry conservation. Many thermal reactions are "symmetry-forbidden" — meaning the orbital symmetry of reactants and products does not correlate smoothly along the reaction coordinate, creating a large energy barrier. But photochemical excitation changes the orbital occupancy. A reaction that is thermally forbidden (like a conrotatory ring closure of a conjugated diene under thermal conditions) becomes photochemically allowed because the excited-state orbital symmetry now permits smooth correlation. This is why photochemistry opens doors that heating alone cannot: it accesses entirely different regions of the potential energy surface.

Once a molecule is in an excited state, several competing processes determine what happens next. The molecule can **fluoresce** (emit a photon and return to the ground state), undergo **intersystem crossing** to a triplet state (where it may phosphoresce or react differently), or proceed along a **photochemical reaction pathway** — such as bond cleavage, isomerization, or cycloaddition. The branching between these fates depends on the relative rates, which are governed by the energy gaps between states and the geometry of the potential energy surfaces. Conical intersections — points where two electronic surfaces cross — are often the funnels through which excited-state population returns to the ground state or channels into photoproducts.

Concrete examples make this tangible. In vision, retinal absorbs a photon and undergoes *cis*-to-*trans* isomerization in femtoseconds — a reaction with a large thermal barrier but nearly barrierless on the excited-state surface. In photosynthesis, chlorophyll's excited state transfers energy through a chain of pigments before driving charge separation. In organic synthesis, photocycloadditions like the [2+2] reaction are thermally forbidden but photochemically allowed, giving chemists access to strained ring systems that would be impossible to make with heat alone. In each case, the photon is not merely providing energy — it is changing the *rules* of the reaction by populating an electronic state with fundamentally different symmetry and bonding character.
