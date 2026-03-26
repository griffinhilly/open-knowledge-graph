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

## Questions

```yaml
- question: "You need to find the force in a single diagonal member near the center of a large Pratt truss. Which approach is more efficient?"
  type: multiple-choice
  options:
    - "Method of joints starting from a support — it's more systematic and less error-prone"
    - "Method of sections — pass a cut through the target member and at most two others, then apply equilibrium to one half"
    - "Both methods require the same number of steps for a single target member"
    - "Method of joints is faster because each joint uses only two equilibrium equations"
  answer: 1
  explanation: "The method of sections is specifically designed for this situation: finding a specific member force without analyzing every joint. A cut through the target member and two others produces a free body that can be solved with three equilibrium equations. The method of joints, by contrast, requires solving every joint between the support and the target member — potentially a dozen or more joints. The method of sections lets you jump directly to the answer."

- question: "A cutting plane exposes two horizontal chord members (upper and lower) and one diagonal member. You want to find the force in the diagonal. Which equilibrium equation isolates it most directly?"
  type: multiple-choice
  options:
    - "ΣFx = 0 — the diagonal's horizontal component is larger than those of the chord members"
    - "ΣFy = 0 — the horizontal chord members have no vertical components, so only the diagonal appears"
    - "ΣM = 0 about a point on the diagonal — this eliminates the diagonal force from the equation"
    - "Solve all three equations simultaneously; there is no shortcut for this configuration"
  answer: 1
  explanation: "The two horizontal chord members lie along the x-axis, so they contribute zero to a vertical force balance. ΣFy = 0 therefore contains only the diagonal member's vertical component (plus any external vertical loads), isolating the diagonal force in a single equation. Taking moments about the intersection of the two chords would also work if they intersect, but ΣFy = 0 is more direct here. Option C is backwards — you'd take moments about a point on the diagonal's line of action to eliminate the diagonal, not to find it."

- question: "Support reactions must be determined before applying the method of sections."
  type: true-false
  answer: true
  explanation: "True. The free body created by the cut includes all external forces on that half of the truss, including support reactions. If the reactions are unknown, you cannot write a complete equilibrium equation — the system will have more unknowns than equations. Solving the entire truss for support reactions using the global free body is always the first step, regardless of which internal analysis method follows."

- question: "The method of sections can be applied to a cutting plane that exposes four unknown member forces, provided you use most three equilibrium equations."
  type: true-false
  answer: false
  explanation: "False. A 2D equilibrium problem yields exactly three independent equations (ΣFx = 0, ΣFy = 0, ΣM = 0). With four unknowns and three equations, the system is underdetermined — there is no unique solution. The cut must expose at most three unknown member forces. If your cut exposes four unknowns, you must redesign the cut: try a different cutting plane orientation that passes through fewer members."

- question: "Why does taking moments about the intersection point of two unknown member forces isolate the third unknown in a single equation?"
  type: short-answer
  answer: "The moment of a force about a point equals the force magnitude times its perpendicular distance (moment arm) from that point. If two unknown forces pass through the chosen moment point, their moment arms are zero — they produce no moment about that point regardless of their magnitude. The ΣM = 0 equation about that point therefore contains only the third unknown force, which can be solved directly without first finding the other two. This is the core strategic advantage of the method of sections over a brute-force simultaneous system."
  explanation: "Concretely: for a truss with two chord members that converge at a panel point, taking moments about that panel point eliminates both chord forces from the moment equation, leaving only the diagonal member force. This reduces a 3×3 system to a 1×1 equation — the difference between a single calculation and a multi-step solve. Choosing the best moment point is the skill that separates efficient sections analysis from laborious algebra."
```

## Explainer

In the method of joints, you process a truss joint by joint, working from known boundary conditions inward. It is systematic but slow: to find the force in a member near the center of a large truss, you may need to analyze a dozen joints first. The **method of sections** is a strategic shortcut that lets you jump directly to the member you care about by exploiting the same equilibrium principle — but applied to an entire half of the truss at once.

The conceptual move is this: pass an imaginary cutting plane through the truss, slicing through the members of interest. This divides the truss into two separate pieces. Each piece is a rigid free body held in equilibrium by external loads on that half, support reactions, and the cut-member forces. The cut-member forces are internal to the original truss but become external forces on the free body — and they are the unknowns you want. Choose the simpler half (fewer loads), draw a free-body diagram with all forces shown, and apply equilibrium.

The critical constraint is that a 2D equilibrium problem provides exactly three independent equations: ΣFx = 0, ΣFy = 0, and ΣM = 0. Your cut must expose no more than three unknown member forces or the system is underdetermined. This is not a limitation so much as a guide for choosing your cut: position the plane to pass through the target member and at most two others. If your section exposes four or more unknowns, re-examine the geometry and try a different cut orientation.

The **moment equation** is what makes the method powerful beyond simple force balance. If two of the three cut-member forces are not parallel and their lines of action intersect at a point P, taking ΣM = 0 about P cancels both of those forces simultaneously — their moment arms are zero. The resulting equation contains only the one remaining unknown, which you can solve directly without first finding the other two. This often reduces a multi-step problem to a single calculation. For a Pratt or Warren truss, you can frequently determine the critical chord force in one moment equation, bypassing all the intermediate joints entirely.

The systematic procedure: solve all support reactions first (always), sketch the truss and draw the cutting plane, identify the three cut members and their directions, choose the simpler free body, label the unknown forces with assumed directions (tension positive by convention), select the best moment point to isolate one unknown, and solve. If an answer comes out negative, the member is in compression — simply reverse your assumed direction. The method of sections does not replace the method of joints; for a full force table of all members, joints is more efficient. But when you need one or a few specific member forces — especially in preliminary design, where a single critical member governs — sections is the right tool.
