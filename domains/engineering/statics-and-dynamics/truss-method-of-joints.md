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

## Questions

```yaml
- question: "At a truss joint with no external load, exactly two members meet at a non-collinear angle. What can you immediately conclude by inspection?"
  type: multiple-choice
  options:
    - "Both members are in compression — joints without external loads always develop compressive forces"
    - "Both members carry zero force — the zero-force member rule for two non-collinear members at an unloaded joint"
    - "One member is in tension and one in compression, balancing each other"
    - "Nothing can be concluded without solving the full equilibrium equations"
  answer: 1
  explanation: "This is the first zero-force member rule: if exactly two non-collinear members meet at a joint with no external load applied, both members must carry zero force. The reasoning comes directly from equilibrium: ΣFx = 0 and ΣFy = 0 at the joint. If the two members are not collinear (their axes are not along the same line), the only solution satisfying both equations simultaneously is that both forces equal zero. Identifying this by inspection eliminates those unknowns immediately, simplifying the subsequent joint-by-joint analysis considerably."

- question: "You assume a truss member is in tension (positive) and solve the equilibrium equations at a joint. The algebra gives a result of −15 kN. What does this mean?"
  type: multiple-choice
  options:
    - "You made an arithmetic error — member forces cannot be negative if you assumed tension"
    - "The member carries 15 kN in compression — the negative sign indicates your tension assumption was wrong"
    - "The member is a zero-force member because the magnitude is indeterminate"
    - "You should re-solve the joint using a compression assumption and the answer will be +15 kN"
  answer: 1
  explanation: "A negative result is not an error — it is meaningful information. The standard method assumes all unknown member forces are in tension (pulling away from the joint). A positive result confirms tension; a negative result means the member is actually in compression, with magnitude equal to the absolute value of the result. The member carries 15 kN in compression. You do not need to re-solve; you simply report the member as −15 kN (or 15 kN compression). Identifying compression members is practically important: long, slender compression members can buckle at loads well below their yield strength, a failure mode tension members don't face."

- question: "Truss members resist only axial (tension or compression) forces, not bending moments or shear forces."
  type: true-false
  answer: true
  explanation: "This is the defining idealization that makes truss analysis tractable. A truss member is modeled as a two-force member: pinned at both ends, loaded only at the pins. Because the pin cannot transmit a moment, and because the member is in static equilibrium, the forces at each end must be equal, opposite, and directed along the member's axis. No transverse loads are applied between pins, so no bending or shear develops. This idealization reduces each member to a single scalar unknown (the axial force, positive = tension, negative = compression), which is what allows the method of joints to work with just ΣFx = 0 and ΣFy = 0."

- question: "If you get a negative member force when solving by method of joints, you should re-do the calculation assuming compression."
  type: true-false
  answer: false
  explanation: "A negative member force is not an error requiring re-calculation — it is the answer. The method of joints assumes all unknown forces are tension (positive). If the algebra produces a negative value, the result tells you directly that the member is in compression, with magnitude equal to the absolute value. Re-doing the calculation with a compression assumption would yield a positive number of the same magnitude, but you gain no new information. The sign convention is consistent throughout: report positive values as tension, negative values as compression."

- question: "Why should zero-force members be identified before beginning joint-by-joint analysis, and what is the practical consequence of missing them?"
  type: short-answer
  answer: "Zero-force members are identified by inspection using two geometric rules: (1) two non-collinear members at an unloaded joint both carry zero force; (2) three members at an unloaded joint where two are collinear means the third carries zero force. Identifying them first eliminates unknowns from the analysis — a joint that appears to have three unknowns may reduce to two once a zero-force member is identified, making it immediately solvable. Missing zero-force members forces you to start at a more complex joint or solve a larger system of equations simultaneously, which is more error-prone and time-consuming. In design, recognizing zero-force members also identifies where material could be eliminated without loss of structural function."
  explanation: "Zero-force members seem counterintuitive — why does a structural member carry no load? They appear in trusses either to provide rigidity for load cases other than the one being analyzed, or to brace compression members against buckling, or simply because the geometry required them. They are real members doing real structural work — just not carrying axial load in the specific loading case under analysis. This is why they are left in the design but can be skipped analytically."
```

## Explainer

A truss is an idealized structure built from **two-force members**: slender bars that are pinned at both ends and loaded only at the pins. Because the pin cannot transmit a moment, and because the member is in equilibrium, the forces at each end must be equal, opposite, and directed along the member's axis. Every member is either pulling its joints toward each other (**tension**, the member is being stretched) or pushing them apart (**compression**, the member is being squeezed). There is no bending, no shear — just pure axial force. This idealization transforms a complex structure into a collection of simpler equilibrium problems.

The method of joints exploits the fact that each joint is a **concurrent force system** — all forces meeting at a single point — so you only have two equilibrium equations available: ΣFx = 0 and ΣFy = 0. (Moment equations about a point are automatically satisfied for concurrent systems and give no new information.) With only two equations, you can solve for at most two unknown member forces per joint. The algorithm is: find global support reactions first using the whole-truss free-body diagram (where you learned rigid body equilibrium), then identify a starting joint with exactly two unknown members, and work joint to joint through the truss, carrying known forces forward.

Before diving into joint-by-joint analysis, scan the truss for **zero-force members** — members carrying no load that can be identified by inspection. Two rules cover most cases: (1) if only two non-collinear members meet at an unloaded joint, both carry zero force; (2) if two members at a joint are collinear and a third meets at the same joint with no external load, the third member carries zero force. Identifying zero-force members early eliminates unknowns, often turning a three-unknown joint into a solvable two-unknown joint.

Sign conventions matter for physical interpretation. The standard approach is to assume each unknown member force is in **tension** (pulling away from the joint). If the algebra gives a positive result, the assumption was correct and the member is in tension. A negative result means the member is in compression. Compression members in long, slender bars are vulnerable to buckling — a different failure mode than yielding — so correctly identifying them is not just an academic exercise. At the end, verify your results by applying equilibrium at the last joint you haven't explicitly solved; if it closes, your entire analysis is consistent.
