---
id: dislocation-types-and-motion
title: Dislocation Types and Motion
domain: engineering
course: materials-science
prerequisites:
- id: crystal-defects
  type: hard
- id: plastic-deformation-mechanisms
  type: hard
- id: crystal-structure-classification
  type: soft
builds-toward:
- work-hardening-and-recovery
- solid-solution-strengthening
tags:
- edge-dislocation
- screw-dislocation
- burgers-vector
- dislocation-glide
- dislocation-climb
stage: advanced
status: draft
---

# Dislocation Types and Motion

## Core Idea
Dislocations are the primary carriers of plastic deformation in crystalline materials, and they come in two idealized forms. An edge dislocation consists of an extra half-plane of atoms inserted into the lattice, with its Burgers vector perpendicular to the dislocation line. A screw dislocation creates a helical ramp of atoms, with its Burgers vector parallel to the dislocation line. Real dislocations are typically mixed, containing both edge and screw character along their length. Dislocations move by glide (conservative motion on the slip plane, requiring only bond rearrangement) or climb (non-conservative motion perpendicular to the slip plane, requiring vacancy diffusion and therefore elevated temperature). The interactions between dislocations — pinning, annihilation, junction formation — govern strain hardening behavior and are central to understanding why metals strengthen as they deform.

## How It's Best Learned
Draw a Burgers circuit around both edge and screw dislocations to derive the Burgers vector direction and magnitude. Use physical models or 3D visualizations to see how glide moves a dislocation through the lattice versus how climb requires atoms to leave or join the extra half-plane. Connect dislocation multiplication (Frank-Read sources) to the observed increase in dislocation density during deformation.

## Common Misconceptions
- The Burgers vector is a property of the dislocation, not the observer's circuit direction — reversing the circuit direction reverses the sign but not the magnitude.
- Screw dislocations are not less important than edge dislocations; they can cross-slip onto different planes, giving metals additional ductility that pure edge motion cannot provide.
- Dislocation climb is not just "slow glide" — it is a fundamentally different mechanism that requires mass transport and is thermally activated.

## Questions

```yaml
- question: "A metal component operates reliably at room temperature but creeps under sustained load at 0.5 Tm. The mechanism responsible for this high-temperature plasticity is:"
  type: multiple-choice
  options:
    - "Increased dislocation glide velocity because thermal energy lowers the Peierls barrier"
    - "Dislocation climb, which allows dislocations to bypass obstacles by absorbing or emitting vacancies through thermally-activated diffusion"
    - "Grain boundary melting that allows slip between adjacent grains at elevated temperature"
    - "Multiplication of dislocations by Frank-Read sources, which becomes active only above a threshold temperature"
  answer: 1
  explanation: "Glide is conservative — it requires only bond rearrangement at the dislocation core and can occur at any temperature. At room temperature, dislocations glide until they pile up against obstacles (grain boundaries, precipitates, other dislocations) and are stuck. Climb requires vacancy diffusion to move the dislocation perpendicular to its slip plane, allowing it to step over the obstacle. Vacancy diffusion is thermally activated and becomes significant only above roughly 0.4 Tm. This is why creep is predominantly a high-temperature phenomenon: glide alone cannot bypass obstacles, but climb can."

- question: "Both an edge dislocation and a screw dislocation in an FCC metal are subjected to an applied shear stress on their primary slip plane. Which dislocation can move to an entirely different crystallographic plane to avoid an obstacle?"
  type: multiple-choice
  options:
    - "The edge dislocation, because its extra half-plane can tilt to intersect other slip planes"
    - "Both equally, because any dislocation under sufficient stress can switch slip planes"
    - "The screw dislocation, because its Burgers vector is parallel to its line, so it has no unique slip plane and can cross-slip"
    - "Neither; both are confined to their original slip plane unless they climb"
  answer: 2
  explanation: "A screw dislocation's defining geometric feature — its Burgers vector being parallel to the dislocation line — means it has no unique slip plane. Any plane containing the Burgers vector direction is a valid slip plane for a screw dislocation. This enables cross-slip: the dislocation moves from one slip plane to another when stress geometry favors it, allowing it to circumvent obstacles that pure glide could not bypass. An edge dislocation's Burgers vector is perpendicular to its line, fixing it to a unique slip plane (glide plane). It cannot cross-slip; it can only leave its plane by climb."

- question: "For an edge dislocation, the Burgers vector is perpendicular to the dislocation line; for a screw dislocation, the Burgers vector is parallel to the dislocation line."
  type: true-false
  answer: true
  explanation: "This geometric relationship is the defining characteristic of each dislocation type and has direct physical consequences. For edge dislocations, the perpendicular Burgers vector means there is an extra half-plane of atoms pointing toward the dislocation line — the dislocation is the terminus of this half-plane. For screw dislocations, the parallel Burgers vector creates the helical ramp geometry. Most real dislocations are mixed (the Burgers vector makes an intermediate angle with the line), but decomposing them into edge and screw components remains useful for analyzing glide, climb, and cross-slip behavior."

- question: "Dislocation climb is essentially a faster or thermally-assisted version of dislocation glide, driven by the same bond-rearrangement mechanism."
  type: true-false
  answer: false
  explanation: "Glide and climb are fundamentally different mechanisms, not different speeds of the same process. Glide is conservative: the dislocation moves within its slip plane by sequential bond rearrangement at the core, requiring no net mass transport and no diffusion. It can occur at cryogenic temperatures. Climb is non-conservative: the dislocation moves perpendicular to its slip plane by absorbing or emitting vacancies — atoms must diffuse away from or to the dislocation core, which requires thermal activation. This is why climb is negligible at room temperature and becomes important only above roughly 0.4 Tm."

- question: "Why can dislocations enable plastic deformation at stresses orders of magnitude below the theoretical strength of a perfect crystal, and what is the mechanistic difference between dislocation glide and dislocation climb?"
  type: short-answer
  answer: "In a perfect crystal, plastic deformation would require simultaneously breaking all bonds across an entire slip plane — an enormous stress (~G/10, where G is the shear modulus). Dislocations allow deformation one atomic step at a time: only the bonds at the dislocation core need to break and reform at any instant, requiring far less stress. Glide moves the dislocation within its slip plane through sequential bond rearrangement with no diffusion required. Climb moves the dislocation perpendicular to its slip plane by exchanging atoms with the surrounding lattice (absorbing or emitting vacancies), which requires thermally-activated vacancy diffusion and is therefore significant only at elevated temperatures."
  explanation: "The analogy is moving a rug by pushing a wrinkle across it versus sliding the whole rug at once. The dislocation is the wrinkle — a localized defect that requires only local atomic rearrangement to advance. This is why metals yield at stresses 10–1000× lower than theoretical predictions for defect-free crystals. Glide vs. climb distinguishes two regimes of deformation: glide dominates at low temperatures and produces work hardening as dislocations pile up; climb allows dislocations to recover and anneal at high temperatures, enabling creep."
```

## Explainer

From crystal defects, you know that a perfect crystal has a regular arrangement of atoms, and that point defects like vacancies disrupt this order locally. From plastic deformation, you know that metals yield not by breaking entire planes of bonds simultaneously — which would require stresses far higher than observed — but by moving defects through the lattice one atomic step at a time. The dislocation is that defect, and understanding its geometry explains why metals deform at stresses orders of magnitude below theoretical values.

An **edge dislocation** is most easily pictured by imagining an extra half-plane of atoms inserted partway into a crystal from above. The "tip" of this extra half-plane — where it ends inside the crystal — is the dislocation line. The lattice is compressed above the dislocation and stretched below. To quantify the disturbance, draw a closed rectangular path (**Burgers circuit**) around a region of perfect crystal: it closes perfectly. Draw the same circuit around the dislocation: it fails to close by one atomic spacing — the closure vector is the **Burgers vector** b, which for an edge dislocation points perpendicular to the dislocation line. When a shear stress is applied, the extra half-plane migrates through the crystal one atomic spacing at a time: bonds at the tip break and reform on the other side. This is **glide**, and it requires only bond rearrangement at the dislocation core — a process that needs no diffusion and can proceed at any temperature.

A **screw dislocation** is harder to visualize but equally important. Cut a crystal halfway through and displace the halves by one lattice parameter parallel to the cut plane: the crystal remains connected, but the atomic planes form a helical ramp. The dislocation line runs along the axis of the helix, and the Burgers vector is parallel to this line. The key property that distinguishes screw dislocations is **cross-slip**: because the Burgers vector is parallel to the line, the screw dislocation has no unique slip plane — it can jump from one plane to another if the stress geometry allows. This gives metals a ductility that pure edge-dislocation glide alone would not provide; dislocations can sidestep obstacles.

The distinction between **glide** and **climb** matters at high temperatures. Glide keeps the dislocation on its slip plane. Climb moves it perpendicular to the slip plane by absorbing or emitting vacancies — atoms leave the dislocation core (or arrive at it) from the surrounding lattice, driven by thermal fluctuations. Climb requires mass transport by vacancy diffusion, so it is strongly thermally activated. At room temperature climb is negligible; at elevated temperatures (roughly above 0.4 T_melting), climb becomes important enough to allow dislocations to bypass obstacles they cannot glide around. This is why materials creep under sustained load at high temperature — dislocations that glide to a barrier can slowly climb over it rather than piling up indefinitely.
