---
id: friction-static-vs-kinetic
title: Static and Kinetic Friction
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: friction-wedges-screws-belts
  type: soft
- id: equilibrium-particles-2d
  type: soft
builds-toward:
- friction-incline-and-horizontal
- friction-with-belt-drives
tags:
- friction
- static
- kinetic
- coefficient
stage: formal-systems
status: draft
---

# Static and Kinetic Friction

## Core Idea
Static friction is the force that prevents motion between surfaces in contact; it can vary from zero up to μₛN where μₛ is the coefficient of static friction. Kinetic friction occurs when surfaces are sliding and equals μₖN, where μₖ < μₛ. The transition between static and kinetic defines the threshold of motion for engineering design.

## How It's Best Learned
Perform experiments on inclined planes, measuring angles at which objects start to slip versus angles at which they maintain sliding motion. Use free-body diagrams to show the friction force as either static (when impending motion or equilibrium) or kinetic (when moving).

## Common Misconceptions
- Assuming static friction always equals μₛN (it can be less).
- Confusing when to use μₛ versus μₖ in problems.
- Treating friction direction incorrectly (it opposes relative motion or impending motion).

## Explainer

**Static friction** is a variable force, and that variability is the first thing to internalize. When a block rests on a surface with no applied horizontal force, the friction force is zero — there is nothing to resist, so friction contributes nothing. Apply a small horizontal push, and static friction matches it exactly to maintain equilibrium. Push harder, and friction increases again to match. This continues up to a ceiling: f_s ≤ μₛN. The coefficient of static friction μₛ characterizes the threshold where the surfaces can no longer hold, not the friction magnitude in general. Before that threshold, static friction is a reaction force that adjusts to whatever equilibrium requires.

The moment surfaces begin to slide, the model changes discontinuously. **Kinetic friction** f_k = μₖN is fixed in magnitude for a given normal force, directed opposite to the velocity of relative motion. The magnitude no longer adjusts to balance applied forces — it is simply μₖN, regardless of how hard you push. Because μₖ < μₛ, less force is needed to sustain sliding than to initiate it. This asymmetry produces the familiar "snap": you push harder and harder until the object breaks loose, then it suddenly accelerates because the force you were applying now exceeds the smaller kinetic friction. Brake lockup works the same way — static friction between a rolling tire and the road is larger than kinetic friction once the tire skids, which is why anti-lock braking systems pulse the brakes to stay in the static regime.

For free-body diagram problems, the question to ask first is always: is the object moving? If stationary (or in impending motion), label friction f (unknown, magnitude between 0 and μₛN) with direction opposing the tendency to slip. If sliding, label it μₖN and mark the direction opposite to velocity. Applying the wrong model — using μₛN when the surface is already sliding, or treating kinetic friction as variable — is the most common error in friction problems.

The direction rule deserves special attention: friction always opposes *relative motion* or *impending relative motion* between the two surfaces in contact. This is not always horizontal. On an incline, friction acts along the surface opposing the component of weight driving the slip. In the belt and wedge problems you studied earlier, friction directions were determined by the tendency to slip at each contact, and getting the direction wrong changes the sign of your answer entirely. Draw the tendency to slip first, then mark friction opposing it.
