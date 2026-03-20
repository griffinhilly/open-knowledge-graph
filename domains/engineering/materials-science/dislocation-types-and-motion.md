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

## Explainer

From crystal defects, you know that a perfect crystal has a regular arrangement of atoms, and that point defects like vacancies disrupt this order locally. From plastic deformation, you know that metals yield not by breaking entire planes of bonds simultaneously — which would require stresses far higher than observed — but by moving defects through the lattice one atomic step at a time. The dislocation is that defect, and understanding its geometry explains why metals deform at stresses orders of magnitude below theoretical values.

An **edge dislocation** is most easily pictured by imagining an extra half-plane of atoms inserted partway into a crystal from above. The "tip" of this extra half-plane — where it ends inside the crystal — is the dislocation line. The lattice is compressed above the dislocation and stretched below. To quantify the disturbance, draw a closed rectangular path (**Burgers circuit**) around a region of perfect crystal: it closes perfectly. Draw the same circuit around the dislocation: it fails to close by one atomic spacing — the closure vector is the **Burgers vector** b, which for an edge dislocation points perpendicular to the dislocation line. When a shear stress is applied, the extra half-plane migrates through the crystal one atomic spacing at a time: bonds at the tip break and reform on the other side. This is **glide**, and it requires only bond rearrangement at the dislocation core — a process that needs no diffusion and can proceed at any temperature.

A **screw dislocation** is harder to visualize but equally important. Cut a crystal halfway through and displace the halves by one lattice parameter parallel to the cut plane: the crystal remains connected, but the atomic planes form a helical ramp. The dislocation line runs along the axis of the helix, and the Burgers vector is parallel to this line. The key property that distinguishes screw dislocations is **cross-slip**: because the Burgers vector is parallel to the line, the screw dislocation has no unique slip plane — it can jump from one plane to another if the stress geometry allows. This gives metals a ductility that pure edge-dislocation glide alone would not provide; dislocations can sidestep obstacles.

The distinction between **glide** and **climb** matters at high temperatures. Glide keeps the dislocation on its slip plane. Climb moves it perpendicular to the slip plane by absorbing or emitting vacancies — atoms leave the dislocation core (or arrive at it) from the surrounding lattice, driven by thermal fluctuations. Climb requires mass transport by vacancy diffusion, so it is strongly thermally activated. At room temperature climb is negligible; at elevated temperatures (roughly above 0.4 T_melting), climb becomes important enough to allow dislocations to bypass obstacles they cannot glide around. This is why materials creep under sustained load at high temperature — dislocations that glide to a barrier can slowly climb over it rather than piling up indefinitely.
