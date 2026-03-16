---
id: space-trusses-3d-analysis
title: 'Space Trusses: Three-Dimensional Analysis'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: truss-method-of-joints
  type: hard
- id: equilibrium-particles-3d
  type: hard
tags:
- space-trusses
- 3d
- three-dimensional
stage: formal-systems
status: draft
---

# Space Trusses: Three-Dimensional Analysis

## Core Idea
Space trusses are three-dimensional frameworks where all members are two-force members and joints are spherical (pin joints). Analysis uses the same principles as 2D trusses but with three equilibrium equations per joint. The stability condition requires at least 3m = 3n - 6 (for 3D), where m is members and n is joints.

## Explainer

You already know how to analyze a 2D truss using the method of joints: at each pin joint, every member carries only axial load (tension or compression), and you write two equilibrium equations (ΣFx = 0, ΣFy = 0) to find the unknown member forces. A space truss extends this directly to three dimensions — every joint is now a **spherical pin** that transmits force in any direction but cannot resist moments, so all members remain two-force members. The equilibrium equations become three: ΣFx = 0, ΣFy = 0, ΣFz = 0 at each joint.

Before solving any member forces, you need to verify that the truss is **statically determinate and stable**. The counting condition is m = 3n − 6, where m is the number of members and n is the number of joints (the 6 comes from the six reaction components provided by the supports in 3D — three force components and three moment components needed for spatial equilibrium). If m < 3n − 6, the truss is a mechanism and will collapse. If m > 3n − 6, it is statically indeterminate and the method of joints alone won't close the system. A simple space truss starts from a tetrahedron (4 joints, 6 members: 6 = 3×4 − 6 ✓) and grows by adding three new members and one new joint at each step while preserving determinacy.

The procedure at each joint mirrors the 2D method: express every unknown member force as T·**û**, where **û** is the unit vector from the joint toward the far end of the member (computed from position vectors, exactly as in 3D particle equilibrium). Sum all force components in x, y, and z and set each sum to zero. The resulting three equations let you solve for three unknown member forces per joint — provided you start at a joint where no more than three unknowns appear. Systematic ordering (start at the simplest joint and work inward) keeps the algebra manageable.

The key practical skill is accurate geometry. Every unit vector computation requires a clear coordinate system, explicit node coordinates, and careful arithmetic. Setting up a table of node coordinates at the start and computing **r** and |**r**| before writing any equilibrium equations prevents the cascading sign and component errors that derail 3D truss problems. The physics is identical to 2D — tension is positive (member pulls the joint), compression is negative (member pushes the joint) — only the bookkeeping is more involved.
