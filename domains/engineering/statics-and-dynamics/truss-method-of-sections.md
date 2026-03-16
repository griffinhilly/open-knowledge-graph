---
id: truss-method-of-sections
title: 'Truss Analysis: Method of Sections'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: truss-method-of-joints
  type: hard
builds-toward:
- frames-machines-analysis
tags:
- statics
- truss
- method of sections
- structural analysis
stage: formal-systems
status: validated
---

# Truss Analysis: Method of Sections

## Core Idea
The method of sections finds forces in specific truss members without analyzing every joint. An imaginary cut passes through no more than three unknown members, separating the truss into two parts. Either free body is in equilibrium under applied loads, reactions, and the cut member forces — providing three equations (ΣFx, ΣFy, ΣM). By choosing the moment point at the intersection of two unknowns, the third unknown is isolated directly, making the method far more efficient than the method of joints when only a few member forces are needed.

## How It's Best Learned
Plan the cut carefully to expose only the members of interest, cutting through no more than three unknowns. Use the moment equation to isolate one unknown at a time by choosing the moment point at the concurrent intersection of the other two unknown forces.

## Common Misconceptions
- Cutting through more than three unknown members, making the problem unsolvable with three equations.
- Forgetting to include all external loads and support reactions on the selected free body.
- Incorrectly assuming the sign of a member force before calculation.

## Explainer

In the method of joints, you process a truss joint by joint, working from known boundary conditions inward. It is systematic but slow: to find the force in a member near the center of a large truss, you may need to analyze a dozen joints first. The **method of sections** is a strategic shortcut that lets you jump directly to the member you care about by exploiting the same equilibrium principle — but applied to an entire half of the truss at once.

The conceptual move is this: pass an imaginary cutting plane through the truss, slicing through the members of interest. This divides the truss into two separate pieces. Each piece is a rigid free body held in equilibrium by external loads on that half, support reactions, and the cut-member forces. The cut-member forces are internal to the original truss but become external forces on the free body — and they are the unknowns you want. Choose the simpler half (fewer loads), draw a free-body diagram with all forces shown, and apply equilibrium.

The critical constraint is that a 2D equilibrium problem provides exactly three independent equations: ΣFx = 0, ΣFy = 0, and ΣM = 0. Your cut must expose no more than three unknown member forces or the system is underdetermined. This is not a limitation so much as a guide for choosing your cut: position the plane to pass through the target member and at most two others. If your section exposes four or more unknowns, re-examine the geometry and try a different cut orientation.

The **moment equation** is what makes the method powerful beyond simple force balance. If two of the three cut-member forces are not parallel and their lines of action intersect at a point P, taking ΣM = 0 about P cancels both of those forces simultaneously — their moment arms are zero. The resulting equation contains only the one remaining unknown, which you can solve directly without first finding the other two. This often reduces a multi-step problem to a single calculation. For a Pratt or Warren truss, you can frequently determine the critical chord force in one moment equation, bypassing all the intermediate joints entirely.

The systematic procedure: solve all support reactions first (always), sketch the truss and draw the cutting plane, identify the three cut members and their directions, choose the simpler free body, label the unknown forces with assumed directions (tension positive by convention), select the best moment point to isolate one unknown, and solve. If an answer comes out negative, the member is in compression — simply reverse your assumed direction. The method of sections does not replace the method of joints; for a full force table of all members, joints is more efficient. But when you need one or a few specific member forces — especially in preliminary design, where a single critical member governs — sections is the right tool.
