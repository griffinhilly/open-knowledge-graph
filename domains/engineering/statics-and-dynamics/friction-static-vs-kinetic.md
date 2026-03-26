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
status: validated
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

## Questions

```yaml
- question: "A 10 kg block sits on a surface (μₛ = 0.4, μₖ = 0.3, g = 10 m/s²). Normal force is 100 N, so maximum static friction is 40 N. You apply a 25 N horizontal force. What is the actual friction force on the block?"
  type: multiple-choice
  options:
    - "25 N — static friction adjusts to balance the applied force exactly, since 25 N < 40 N"
    - "40 N — static friction always acts at its maximum value μₛN"
    - "30 N — kinetic friction applies because the block is in contact with the surface"
    - "0 N — friction only activates when the block is moving"
  answer: 0
  explanation: "Static friction is a reaction force: it matches the applied force to maintain equilibrium, up to its maximum μₛN. With 25 N applied and a 40 N maximum, the block stays stationary with friction = 25 N. Option B is the classic mistake — μₛN is the ceiling, not the default value. Kinetic friction (option C) only applies once sliding begins, and it remains constant at μₖN regardless of the applied force."

- question: "A wooden crate is being pushed across a concrete floor at constant velocity. To find the friction force opposing its motion, which coefficient should you use?"
  type: multiple-choice
  options:
    - "Kinetic friction coefficient μₖ — the crate is sliding, so kinetic friction applies"
    - "Static friction coefficient μₛ — constant velocity means equilibrium, so static friction is balancing the push"
    - "Either — they are approximately equal for most surfaces"
    - "The average of μₛ and μₖ — transitional motion uses a blended value"
  answer: 0
  explanation: "Once surfaces are in relative sliding motion, kinetic friction applies — always. The fact that velocity is constant means the net force is zero, but that is a consequence of the applied push equaling μₖN, not an indication that static friction is at work. Static friction only applies when surfaces are not sliding. μₛ > μₖ for essentially all real material pairs, so using μₛ would give an overestimate."

- question: "Static friction typically equals μₛN whenever the surfaces in contact are stationary."
  type: true-false
  answer: false
  explanation: "Static friction is a variable reaction force in the range 0 ≤ f_s ≤ μₛN. It equals exactly what equilibrium demands — no more, no less. When no horizontal force acts on a stationary block, static friction is zero. As applied force increases, static friction increases to match it. Only at the moment of impending motion does it reach μₛN. Treating μₛN as the default value leads to incorrect free-body diagrams."

- question: "It requires more force to start sliding two surfaces against each other than to sustain that sliding, because μₛ > μₖ."
  type: true-false
  answer: true
  explanation: "This asymmetry is fundamental to friction analysis. The maximum static friction force (μₛN) exceeds the kinetic friction force (μₖN) because μₛ > μₖ for all common surface pairs. In practice, this produces the familiar 'snap': you push harder and harder until the object breaks loose, then it suddenly accelerates — because the force you were applying (just above μₛN) now exceeds the smaller kinetic resistance (μₖN). ABS brakes exploit this by keeping tires in the static regime."

- question: "Explain why the friction force on a stationary block increases as you push harder, up to a point, and then suddenly drops when the block starts moving."
  type: short-answer
  answer: "Before the block moves, static friction is a reaction force that adjusts to maintain equilibrium — it exactly cancels the applied force, so the net force stays zero. When the applied force reaches μₛN (the maximum static friction), equilibrium can no longer be maintained and sliding begins. Once sliding, friction switches to kinetic friction f_k = μₖN, which is fixed and smaller than μₛN. Since the applied force now exceeds f_k, the net force is nonzero and the block accelerates."
  explanation: "The key is the distinction between static friction as a variable reaction force (0 to μₛN) and kinetic friction as a fixed value (μₖN). The 'snap' moment — when the block breaks loose and suddenly moves faster — occurs precisely because μₛ > μₖ. There is no smooth transition; once the static limit is exceeded, the friction force drops discontinuously from μₛN to μₖN."
```

## Explainer

**Static friction** is a variable force, and that variability is the first thing to internalize. When a block rests on a surface with no applied horizontal force, the friction force is zero — there is nothing to resist, so friction contributes nothing. Apply a small horizontal push, and static friction matches it exactly to maintain equilibrium. Push harder, and friction increases again to match. This continues up to a ceiling: f_s ≤ μₛN. The coefficient of static friction μₛ characterizes the threshold where the surfaces can no longer hold, not the friction magnitude in general. Before that threshold, static friction is a reaction force that adjusts to whatever equilibrium requires.

The moment surfaces begin to slide, the model changes discontinuously. **Kinetic friction** f_k = μₖN is fixed in magnitude for a given normal force, directed opposite to the velocity of relative motion. The magnitude no longer adjusts to balance applied forces — it is simply μₖN, regardless of how hard you push. Because μₖ < μₛ, less force is needed to sustain sliding than to initiate it. This asymmetry produces the familiar "snap": you push harder and harder until the object breaks loose, then it suddenly accelerates because the force you were applying now exceeds the smaller kinetic friction. Brake lockup works the same way — static friction between a rolling tire and the road is larger than kinetic friction once the tire skids, which is why anti-lock braking systems pulse the brakes to stay in the static regime.

For free-body diagram problems, the question to ask first is always: is the object moving? If stationary (or in impending motion), label friction f (unknown, magnitude between 0 and μₛN) with direction opposing the tendency to slip. If sliding, label it μₖN and mark the direction opposite to velocity. Applying the wrong model — using μₛN when the surface is already sliding, or treating kinetic friction as variable — is the most common error in friction problems.

The direction rule deserves special attention: friction always opposes *relative motion* or *impending relative motion* between the two surfaces in contact. This is not always horizontal. On an incline, friction acts along the surface opposing the component of weight driving the slip. In the belt and wedge problems you studied earlier, friction directions were determined by the tendency to slip at each contact, and getting the direction wrong changes the sign of your answer entirely. Draw the tendency to slip first, then mark friction opposing it.
