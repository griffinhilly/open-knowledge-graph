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
stage: advanced
status: draft
---

# Dislocation Motion and Slip Systems

## Core Idea
Dislocations are line defects (edge, screw, or mixed character) characterized by the Burgers vector magnitude and direction. Plastic deformation occurs when dislocations move (glide) on specific crystallographic planes and directions called slip systems. Each slip system combines a slip plane (typically close-packed) and slip direction (typically close-packed direction), with number of systems determined by crystal structure (FCC has 12, BCC has 12, HCP has 3).

## Explainer

From your study of crystal structures and point defects, you know that metals are crystalline — atoms occupy regular lattice positions with periodic spacing. A naive estimate of the theoretical shear strength of a perfect crystal, calculated by asking how much stress is needed to slide one entire atomic plane over another simultaneously, gives values around 10 GPa. Real metals yield at stresses 100 to 1000 times lower, typically 10–100 MPa. The explanation for this enormous discrepancy is dislocations. A **dislocation** is a line defect — a boundary between a region of the crystal that has already slipped and a region that has not — and it moves under shear stress like the ripple in a rug: you can shift a heavy carpet by propagating a small buckle across it with far less force than dragging the whole carpet at once.

An **edge dislocation** is easiest to visualize: imagine inserting an extra half-plane of atoms partway into the crystal. The edge of that half-plane is the dislocation line, running perpendicular to the cross-section you drew. The **Burgers vector** b characterizes the dislocation quantitatively: if you trace a closed circuit in the distorted crystal around the dislocation line (a Burgers circuit) and compare it to the same circuit in the perfect crystal, the closure failure — the extra vector needed to close the loop — is b. For an edge dislocation, b is perpendicular to the dislocation line and points in the direction the half-plane was inserted. Under an applied shear stress, the edge dislocation glides in the direction of b along its slip plane — atom by atom, breaking and reforming only local bonds at each step — eventually reaching the crystal surface where it produces one unit of permanent slip. A **screw dislocation**, in contrast, has b parallel to the dislocation line, and its motion is perpendicular to b, tracing a helical path through the lattice. Real dislocations in crystals are mixed — neither pure edge nor pure screw — but can always be decomposed into edge and screw components.

Dislocations glide preferentially on **close-packed planes** in **close-packed directions** — these combinations are called **slip systems**. The physics is geometric: close-packed planes are the most widely spaced in the crystal (lowest energy to open a gap between them) and close-packed directions are the shortest lattice translation vectors (smallest |b|, therefore smallest elastic strain energy stored in the dislocation, which scales as |b|²). FCC metals (copper, aluminum, nickel) have 4 close-packed {111} planes, each with 3 close-packed ⟨110⟩ directions — 12 slip systems total. Whatever direction you apply stress, several of these 12 systems will be favorably oriented to activate, so FCC metals deform plastically in virtually any loading geometry and are typically ductile. HCP metals (magnesium, zinc at room temperature) have only 3 primary basal plane slip systems; fewer available orientations means it is easy to find loading directions where no slip system is favorably oriented — the material fractures instead of yielding, making HCP metals more brittle.

The stress required to activate a given slip system depends on the orientation of the applied stress relative to that system. **Schmid's law** gives the resolved shear stress as τ = σ·cos φ·cos λ, where φ is the angle between the loading axis and the slip plane normal, and λ is the angle between the loading axis and the slip direction. The factor cos φ·cos λ is the Schmid factor; it is maximized at 45° orientation and drops to zero when the slip direction or slip plane normal is perpendicular to the applied stress. Yielding begins when the resolved shear stress on the most favorably oriented slip system first reaches the **critical resolved shear stress** (CRSS) — the material's intrinsic resistance to dislocation glide. The CRSS is not fixed; it increases as dislocations multiply and entangle, which is the microscopic origin of strain hardening and the basis for all of the strengthening mechanisms you will study next.
