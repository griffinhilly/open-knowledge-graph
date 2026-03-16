---
id: truss-joint-and-section-methods
title: 'Truss Analysis: Joint and Section Methods'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rigid-body-equilibrium-planar
  type: hard
- id: truss-method-of-joints
  type: soft
- id: truss-method-of-sections
  type: soft
builds-toward:
- truss-applications-and-design
tags:
- trusses
- joint method
- section method
- two-force members
- internal forces
stage: formal-systems
status: draft
---

# Truss Analysis: Joint and Section Methods

## Core Idea
Trusses are frameworks of straight two-force members connected at pin joints. The method of joints examines equilibrium at each pin, solving for member forces sequentially; the method of sections cuts through members to expose internal forces, allowing efficient analysis of selected members. Both rely on the principle that two-force members carry pure tension or compression.

## Explainer

The analytical power of truss analysis comes from a single geometric constraint: every member is straight and connected only at its endpoints by frictionless pins, with loads applied only at joints. Under these conditions, a member cannot exert a bending moment on its end pins — the only force it can apply is along its own axis. This is the definition of a **two-force member**: pure tension (pulling the joints together) or pure compression (pushing them apart). Every truss member is therefore a scalar unknown, not a vector — you need only find its magnitude, and the sign tells you tension or compression.

The **method of joints** exploits this by isolating each pin and writing equilibrium: ΣFx = 0, ΣFy = 0. With two equations per joint and one unknown per member, you proceed sequentially — start at a joint with only two unknown members (often a free end or a support joint after computing reactions from rigid-body equilibrium) and propagate inward. The method works every time, but it requires working through all joints to reach any single interior member, which is inefficient for large trusses. Watch for **zero-force members**: if a joint connects only two non-collinear members with no external load, both are zero-force. These simplify the analysis dramatically.

The **method of sections** is a shortcut for finding the force in a specific interior member without solving the whole truss. The idea is to cut the truss completely through three (or fewer) unknown members with an imaginary plane, producing two separate free bodies. Each free body is in equilibrium under the external loads on its side plus the three exposed member forces. With three equilibrium equations (ΣFx, ΣFy, ΣM) and three unknowns, you solve directly. Choosing the moment center cleverly — a point where two of the three cut member forces intersect — often reduces the problem to one equation with one unknown.

The strategic skill is choosing which method to apply and where to start. For finding all member forces, use joints working from the outside in. For finding one or two specific interior forces efficiently, use sections and pick a smart cut. In practice you often combine both: compute reactions first (rigid-body equilibrium of the whole truss), identify zero-force members by inspection, then apply whichever method reaches the target members fastest. The physical interpretation is always the check: compression members are being squeezed and are at risk of buckling; tension members are being pulled and are at risk of yielding. The sign convention must be tracked carefully throughout.
