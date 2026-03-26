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

## Questions

```yaml
- question: "A 10 kg block sits on a horizontal surface with μ_s = 0.4. The normal force is approximately 98 N, giving F_s,max = 39.2 N. A 30 N horizontal force is applied. What is the friction force?"
  type: multiple-choice
  options:
    - "39.2 N — always use F = μ_s·N for friction problems"
    - "29.4 N — use kinetic friction μ_k·N since a force is applied"
    - "30 N — friction matches the applied force exactly, since it does not exceed the maximum"
    - "0 N — the block is not moving so there is no friction"
  answer: 2
  explanation: "Friction is reactive: it takes whatever value equilibrium requires, up to its maximum. Here, equilibrium requires only 30 N of friction to balance the applied force, which is less than F_s,max = 39.2 N — so the block does not slide and friction equals exactly 30 N. Using μ_s·N always (option A) is the most common error — that value is the maximum, not the actual friction force. Using kinetic friction (option B) is wrong because the block is not sliding. The friction force is 0 only when no tangential force tends to cause sliding."

- question: "An engineer needs to determine whether a crate will slide when pushed with force F. In which order should they proceed?"
  type: multiple-choice
  options:
    - "Apply F = μ_k·N immediately, since that governs motion"
    - "Assume the crate is sliding, calculate kinetic friction, and verify afterward"
    - "First solve equilibrium equations to find what friction force is required; compare to F_s,max = μ_s·N to determine whether sliding occurs"
    - "Use F = μ_s·N for the friction force regardless, since static friction governs impending motion"
  answer: 2
  explanation: "The correct procedure is: assume static equilibrium, solve for the required friction force from equilibrium equations, then compare to F_s,max = μ_s·N. If the required friction is less than or equal to the maximum, the crate stays put and friction equals the required value. If equilibrium would require more friction than the surface can provide, sliding occurs and you switch to F = μ_k·N. The friction state must be determined before you can write the correct friction equation — there is no shortcut."

- question: "The friction force between two surfaces usually equals μ_s × N, regardless of the magnitude of the applied load."
  type: true-false
  answer: false
  explanation: "F = μ_s·N gives the maximum static friction force — the upper limit, not the actual value. For any applied load that does not cause impending motion, the actual friction force is less than this maximum and is determined by equilibrium. Only at the instant of impending slip does the friction force reach μ_s·N. This reactive character distinguishes friction from most other forces in statics: you cannot write the friction force directly from geometry; you must first determine the friction state."

- question: "Kinetic friction is smaller than maximum static friction, which is why it takes more force to start an object sliding than to keep it sliding once motion has begun."
  type: true-false
  answer: true
  explanation: "μ_k < μ_s by definition of Coulomb's model. When a block is on the verge of sliding, the maximum static friction F_s,max = μ_s·N must be overcome. Once sliding begins, the friction drops to F_k = μ_k·N, which is smaller. This reduction is why you can feel a 'give' when you first budge a stuck object — the resisting force drops once motion starts. Practically, this means the force needed to maintain motion is less than the force needed to initiate it."

- question: "What does it mean to say that friction is a 'reactive' force, and why does this require you to determine the friction state before writing the friction equation?"
  type: short-answer
  answer: "A reactive force adjusts its magnitude in response to the loads applied to a system, rather than having a fixed value determined by geometry or material alone. Friction opposes the tendency of motion and takes whatever value equilibrium requires — from zero up to its maximum μ_s·N. Because friction can take any value in that range, you cannot write a single friction equation without first knowing which of the three states applies: static equilibrium (F < μ_s·N, determined by equilibrium), impending motion (F = μ_s·N, the tipping-point condition), or sliding (F = μ_k·N, once motion has started). Each state uses a different equation, and choosing the wrong one produces an incorrect answer."
  explanation: "This is the central challenge of friction problems in statics: unlike a pin joint or roller support, friction does not have a unique force determined by the geometry. You must make a judgment about the state first, then set up equations, then verify that your assumed state is consistent with the solution. If the check fails, you assumed the wrong state and must redo the analysis."
```

## Explainer

From your study of rigid-body equilibrium, you know how to sum forces and moments to find unknown reactions. Friction introduces something new: a contact force whose magnitude is not independently determined by geometry or applied loads, but instead adjusts to maintain equilibrium — up to a limit. This **reactive** character is what makes friction problems require a judgment call before you can write equations.

**Coulomb's model** describes the frictional contact between two dry surfaces with just two parameters: the **static friction coefficient** μ_s and the **kinetic friction coefficient** μ_k. The normal force N at the contact surface (perpendicular to the interface) is determined from equilibrium, exactly as in your earlier work. The friction force F acts tangentially and opposes the tendency of relative motion between the surfaces. The key rule: friction takes whatever value is needed for equilibrium, from zero up to its maximum F_s,max = μ_s·N. Only when the applied force would require F to exceed that maximum does sliding occur.

This gives three mutually exclusive states. In **static equilibrium**, the object is not on the verge of moving, and F < μ_s·N — you solve for F from the equilibrium equations. At **impending motion**, the object is on the verge of sliding, and F = μ_s·N — this is the tipping point condition used in most engineering problems about "will this object slide?" Once the object is actually sliding, the friction force drops to the **kinetic** value F_k = μ_k·N, with μ_k < μ_s (kinetic friction is always smaller than the maximum static value). The reduction in friction after motion begins is why it's easier to keep an object sliding than to start it sliding.

The **angle of friction** φ_s = arctan(μ_s) offers a geometric way to see the same physics. The total contact force on a surface has a normal component N and a tangential component F. The resultant of these two components makes an angle arctan(F/N) with the normal. At impending slip, this resultant sits exactly at angle φ_s from the normal — the **friction cone**. Any resultant direction inside the cone is achievable by static friction; outside the cone, the surface cannot provide the needed reaction and the object slides. This geometric view is especially powerful when analyzing wedges and screws, where the same friction angle appears in the inclined-plane geometry.
