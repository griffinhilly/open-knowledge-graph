---
id: dry-friction-coulombs-law
title: 'Dry Friction and Coulomb''s Law'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: equilibrium-rigid-bodies
  type: hard
- id: friction-forces
  type: soft
- id: frames-machines-analysis
  type: soft
builds-toward:
- friction-wedges-screws-belts
tags:
- statics
- friction
- Coulomb friction
- static friction
- kinetic friction
stage: formal-systems
status: validated
---
# Dry Friction and Coulomb's Law

## Core Idea
Coulomb's law states that the maximum static friction force is F_s,max = μ_s·N, where μ_s is the static friction coefficient and N is the normal contact force. Kinetic friction is F_k = μ_k·N with μ_k < μ_s. Friction is reactive: it takes whatever value is needed for equilibrium up to its maximum. Three states are possible — static equilibrium (F < μ_s·N), impending motion (F = μ_s·N), or sliding (F = μ_k·N). The angle of friction φ_s = arctan(μ_s) gives the angle of the resultant contact force from the normal at impending slip.

## How It's Best Learned
Identify which friction state applies (equilibrium, impending, or sliding) before setting up equations. Assume a friction direction in the FBD, solve, and verify the result is consistent with the assumed state.

## Common Misconceptions
- Using kinetic friction when the problem involves impending (not actual) motion.
- Assuming friction always acts in a fixed direction — it opposes the tendency of motion.
- Thinking friction force equals μN always, rather than at most μ_s·N.

## Explainer

From your study of rigid-body equilibrium, you know how to sum forces and moments to find unknown reactions. Friction introduces something new: a contact force whose magnitude is not independently determined by geometry or applied loads, but instead adjusts to maintain equilibrium — up to a limit. This **reactive** character is what makes friction problems require a judgment call before you can write equations.

**Coulomb's model** describes the frictional contact between two dry surfaces with just two parameters: the **static friction coefficient** μ_s and the **kinetic friction coefficient** μ_k. The normal force N at the contact surface (perpendicular to the interface) is determined from equilibrium, exactly as in your earlier work. The friction force F acts tangentially and opposes the tendency of relative motion between the surfaces. The key rule: friction takes whatever value is needed for equilibrium, from zero up to its maximum F_s,max = μ_s·N. Only when the applied force would require F to exceed that maximum does sliding occur.

This gives three mutually exclusive states. In **static equilibrium**, the object is not on the verge of moving, and F < μ_s·N — you solve for F from the equilibrium equations. At **impending motion**, the object is on the verge of sliding, and F = μ_s·N — this is the tipping point condition used in most engineering problems about "will this object slide?" Once the object is actually sliding, the friction force drops to the **kinetic** value F_k = μ_k·N, with μ_k < μ_s (kinetic friction is always smaller than the maximum static value). The reduction in friction after motion begins is why it's easier to keep an object sliding than to start it sliding.

The **angle of friction** φ_s = arctan(μ_s) offers a geometric way to see the same physics. The total contact force on a surface has a normal component N and a tangential component F. The resultant of these two components makes an angle arctan(F/N) with the normal. At impending slip, this resultant sits exactly at angle φ_s from the normal — the **friction cone**. Any resultant direction inside the cone is achievable by static friction; outside the cone, the surface cannot provide the needed reaction and the object slides. This geometric view is especially powerful when analyzing wedges and screws, where the same friction angle appears in the inclined-plane geometry.
