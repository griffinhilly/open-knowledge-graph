---
id: truss-method-of-joints
title: 'Truss Analysis: Method of Joints'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: equilibrium-rigid-bodies
  type: hard
- id: equilibrium-particles-2d
  type: hard
builds-toward:
- truss-method-of-sections
- frames-machines-analysis
tags:
- statics
- truss
- method of joints
- structural analysis
- two-force members
stage: formal-systems
status: validated
---

# Truss Analysis: Method of Joints

## Core Idea
A simple truss is a structure of two-force members connected at frictionless joints, where all external loads and reactions are applied only at joints. Because each joint is a concurrent force system, two equilibrium equations (ΣFx = 0, ΣFy = 0) are available per joint. Analysis proceeds joint by joint, starting with a joint having at most two unknown member forces. Zero-force members — members that carry no load — can be identified by inspection using two specific geometric rules, simplifying the analysis considerably.

## How It's Best Learned
Find global support reactions first, then identify the starting joint with only two unknowns. Use a consistent sign convention (assume tension positive). Work joint to joint and verify equilibrium at the last unchecked joint.

## Common Misconceptions
- Assuming truss members resist bending or shear — they carry only axial (tension/compression) loads.
- Assuming all members are in tension; many will be in compression.
- Missing zero-force members that simplify the analysis.

## Explainer

A truss is an idealized structure built from **two-force members**: slender bars that are pinned at both ends and loaded only at the pins. Because the pin cannot transmit a moment, and because the member is in equilibrium, the forces at each end must be equal, opposite, and directed along the member's axis. Every member is either pulling its joints toward each other (**tension**, the member is being stretched) or pushing them apart (**compression**, the member is being squeezed). There is no bending, no shear — just pure axial force. This idealization transforms a complex structure into a collection of simpler equilibrium problems.

The method of joints exploits the fact that each joint is a **concurrent force system** — all forces meeting at a single point — so you only have two equilibrium equations available: ΣFx = 0 and ΣFy = 0. (Moment equations about a point are automatically satisfied for concurrent systems and give no new information.) With only two equations, you can solve for at most two unknown member forces per joint. The algorithm is: find global support reactions first using the whole-truss free-body diagram (where you learned rigid body equilibrium), then identify a starting joint with exactly two unknown members, and work joint to joint through the truss, carrying known forces forward.

Before diving into joint-by-joint analysis, scan the truss for **zero-force members** — members carrying no load that can be identified by inspection. Two rules cover most cases: (1) if only two non-collinear members meet at an unloaded joint, both carry zero force; (2) if two members at a joint are collinear and a third meets at the same joint with no external load, the third member carries zero force. Identifying zero-force members early eliminates unknowns, often turning a three-unknown joint into a solvable two-unknown joint.

Sign conventions matter for physical interpretation. The standard approach is to assume each unknown member force is in **tension** (pulling away from the joint). If the algebra gives a positive result, the assumption was correct and the member is in tension. A negative result means the member is in compression. Compression members in long, slender bars are vulnerable to buckling — a different failure mode than yielding — so correctly identifying them is not just an academic exercise. At the end, verify your results by applying equilibrium at the last joint you haven't explicitly solved; if it closes, your entire analysis is consistent.
