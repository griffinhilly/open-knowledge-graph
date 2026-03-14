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
builds-toward:
- work-hardening-and-recovery
- solid-solution-strengthening
tags:
- edge-dislocation
- screw-dislocation
- burgers-vector
- dislocation-glide
- dislocation-climb
stage: formal-systems
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
