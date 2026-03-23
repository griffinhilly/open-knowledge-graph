---
id: dislocation-motion-and-slip
title: Dislocation Motion and Slip Systems
domain: engineering
course: materials-science
prerequisites:
- id: point-defects-and-vacancies
  type: hard
- id: crystallographic-planes-directions
  type: soft
builds-toward:
- plastic-deformation-yielding-materials
- strengthening-mechanisms-materials
tags:
- dislocations
- slip
- edge-dislocation
- screw-dislocation
- burgers-vector
stage: formal-systems
status: draft
---

# Dislocation Motion and Slip Systems

## Core Idea
Dislocations are line defects (edge, screw, or mixed character) characterized by the Burgers vector magnitude and direction. Plastic deformation occurs when dislocations move (glide) on specific crystallographic planes and directions called slip systems. Each slip system combines a slip plane (typically close-packed) and slip direction (typically close-packed direction), with number of systems determined by crystal structure (FCC has 12, BCC has 12, HCP has 3).

## Questions

```yaml
- question: "Theoretical calculations predict that a perfect metal crystal should require ~10 GPa of shear stress to deform plastically. Real metals yield at 10–100 MPa — a factor of 100–1000 lower. What explains this enormous discrepancy?"
  type: multiple-choice
  options:
    - "Real metals contain many grain boundaries that act as weak planes, reducing the required stress"
    - "Dislocations allow plastic deformation to occur by propagating local bond-breaking sequentially rather than sliding entire planes simultaneously"
    - "The theoretical calculation assumes room temperature; real metals are softer because thermal vibrations assist deformation"
    - "Real metals have impurities that lubricate the slip planes, dramatically lowering friction between atomic layers"
  answer: 1
  explanation: "The theoretical shear strength assumes all atoms in a plane slide simultaneously — a synchronized collective motion requiring enormous force. Dislocations short-circuit this: a dislocation line represents the boundary between slipped and unslipped regions, and it glides forward by breaking only a few atomic bonds at a time (like the ripple in a rug). The energy required is orders of magnitude smaller because only local, sequential bond-breaking is needed. Grain boundaries (option A) actually impede dislocation motion and increase yield stress, not decrease it."

- question: "FCC metals like copper are much more ductile and formable than HCP metals like magnesium at room temperature. The primary structural reason is..."
  type: multiple-choice
  options:
    - "FCC metals have lower melting points, making them softer under applied stress"
    - "FCC metals have 12 independent slip systems compared to only 3 primary slip systems in HCP, making it easier to find active slip systems for any loading direction"
    - "HCP metals have stronger covalent bonds that resist dislocation motion more effectively"
    - "FCC metals have larger Burgers vectors, which means more plastic displacement per dislocation passage"
  answer: 1
  explanation: "Ductility requires that slip systems be activated in multiple directions as a material deforms. FCC has 4 {111} close-packed planes × 3 ⟨110⟩ directions = 12 slip systems, so whatever direction stress is applied, several systems are favorably oriented (high Schmid factor). HCP has only 3 primary basal slip systems — loading at most orientations will find no system with a high Schmid factor, so the material fractures instead of yielding plastically. Option D is backwards: smaller Burgers vectors (not larger) are energetically favored since dislocation energy scales as |b|²."

- question: "The elastic strain energy stored in a dislocation is proportional to |b|², which is why dislocations in crystals preferentially form with the shortest possible Burgers vectors."
  type: true-false
  answer: true
  explanation: "Dislocation energy per unit length scales approximately as μb²/2, where μ is the shear modulus. The shortest lattice translation vectors — which lie along close-packed directions — minimize |b| and therefore minimize the energy cost of creating and maintaining the dislocation. This energy criterion explains why slip preferentially occurs on close-packed planes in close-packed directions: not just because the planes are widely spaced, but because these directions provide the smallest Burgers vectors."

- question: "Dislocations prefer to glide on close-packed planes because those planes have the highest atomic density, making them the strongest and most resistant planes in the crystal."
  type: true-false
  answer: false
  explanation: "The reasoning is opposite. Close-packed planes are favored because they are the most widely *spaced* planes in the crystal — there is more distance between them, so it costs less energy to create the planar separation needed for slip. High atomic density on the plane itself means the atoms are tightly packed laterally, which relates to the Burgers vector length, but the key reason for preferring close-packed planes for slip is their large interplanar spacing (low energy to shear apart), not their in-plane strength."

- question: "Why does dislocation glide require so much less applied stress than sliding one complete atomic plane over another in a perfect crystal, even though both ultimately move atoms the same net distance?"
  type: short-answer
  answer: "Sliding an entire plane simultaneously requires every atom to pass over the energy barrier of its neighbor at once — all bonds must be stretched and broken in concert, requiring enormous collective stress (~10 GPa). Dislocation glide breaks only the few bonds at the dislocation core at any moment; the rest of the crystal remains undisturbed. As the dislocation advances one atomic spacing, only a small number of local bonds break and reform. The stress needed is only sufficient to drive this local, sequential process, not the global simultaneous process — hence 100–1000× lower yield stress."
  explanation: "An analogy: dragging a large rug across the floor requires enormous friction force on the entire area simultaneously. Propagating a ripple across the rug requires only the force to lift and slide a small buckle at a time. The net displacement is the same; the local force required is dramatically different. This analogy directly maps to the dislocation mechanism."
```

## Explainer

From your study of crystal structures and point defects, you know that metals are crystalline — atoms occupy regular lattice positions with periodic spacing. A naive estimate of the theoretical shear strength of a perfect crystal, calculated by asking how much stress is needed to slide one entire atomic plane over another simultaneously, gives values around 10 GPa. Real metals yield at stresses 100 to 1000 times lower, typically 10–100 MPa. The explanation for this enormous discrepancy is dislocations. A **dislocation** is a line defect — a boundary between a region of the crystal that has already slipped and a region that has not — and it moves under shear stress like the ripple in a rug: you can shift a heavy carpet by propagating a small buckle across it with far less force than dragging the whole carpet at once.

An **edge dislocation** is easiest to visualize: imagine inserting an extra half-plane of atoms partway into the crystal. The edge of that half-plane is the dislocation line, running perpendicular to the cross-section you drew. The **Burgers vector** b characterizes the dislocation quantitatively: if you trace a closed circuit in the distorted crystal around the dislocation line (a Burgers circuit) and compare it to the same circuit in the perfect crystal, the closure failure — the extra vector needed to close the loop — is b. For an edge dislocation, b is perpendicular to the dislocation line and points in the direction the half-plane was inserted. Under an applied shear stress, the edge dislocation glides in the direction of b along its slip plane — atom by atom, breaking and reforming only local bonds at each step — eventually reaching the crystal surface where it produces one unit of permanent slip. A **screw dislocation**, in contrast, has b parallel to the dislocation line, and its motion is perpendicular to b, tracing a helical path through the lattice. Real dislocations in crystals are mixed — neither pure edge nor pure screw — but can always be decomposed into edge and screw components.

Dislocations glide preferentially on **close-packed planes** in **close-packed directions** — these combinations are called **slip systems**. The physics is geometric: close-packed planes are the most widely spaced in the crystal (lowest energy to open a gap between them) and close-packed directions are the shortest lattice translation vectors (smallest |b|, therefore smallest elastic strain energy stored in the dislocation, which scales as |b|²). FCC metals (copper, aluminum, nickel) have 4 close-packed {111} planes, each with 3 close-packed ⟨110⟩ directions — 12 slip systems total. Whatever direction you apply stress, several of these 12 systems will be favorably oriented to activate, so FCC metals deform plastically in virtually any loading geometry and are typically ductile. HCP metals (magnesium, zinc at room temperature) have only 3 primary basal plane slip systems; fewer available orientations means it is easy to find loading directions where no slip system is favorably oriented — the material fractures instead of yielding, making HCP metals more brittle.

The stress required to activate a given slip system depends on the orientation of the applied stress relative to that system. **Schmid's law** gives the resolved shear stress as τ = σ·cos φ·cos λ, where φ is the angle between the loading axis and the slip plane normal, and λ is the angle between the loading axis and the slip direction. The factor cos φ·cos λ is the Schmid factor; it is maximized at 45° orientation and drops to zero when the slip direction or slip plane normal is perpendicular to the applied stress. Yielding begins when the resolved shear stress on the most favorably oriented slip system first reaches the **critical resolved shear stress** (CRSS) — the material's intrinsic resistance to dislocation glide. The CRSS is not fixed; it increases as dislocations multiply and entangle, which is the microscopic origin of strain hardening and the basis for all of the strengthening mechanisms you will study next.
