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
