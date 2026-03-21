---
id: newtons-third-law
title: 'Newton''s Third Law: Action-Reaction Pairs'
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
builds-toward:
- conservation-of-momentum
- friction-forces
tags:
- newtons-laws
- action-reaction
- force-pairs
stage: formal-systems
status: validated
---

# Newton's Third Law: Action-Reaction Pairs

## Core Idea
For every force exerted by object A on object B, there is an equal and opposite force exerted by B on A. These action-reaction pairs always act on different objects, which is why they do not cancel. Newton's third law is the reason rockets accelerate in space: the engine pushes exhaust backward, and the exhaust pushes the rocket forward.

## How It's Best Learned
Identify force pairs by asking: 'Object A pushes on object B — what does B push back on?' Practice with systems like two blocks in contact, a person pushing a wall, or a car tire pushing on the road.

## Common Misconceptions
- Thinking action-reaction forces cancel out: they act on different objects, so they affect each object's motion separately.
- Confusing action-reaction pairs with balanced forces: balanced forces act on the same object; Newton's-third-law pairs act on different objects.

## Questions

```yaml
- question: "A horse pulls a cart forward with force F. By Newton's third law, the cart pulls the horse backward with force F. A student argues this means the cart can never accelerate forward. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The cart's pull on the horse is slightly smaller due to friction losses"
    - "Newton's third law only applies to objects at rest, not accelerating ones"
    - "The two equal-and-opposite forces act on different objects (horse and cart), so each object's motion is governed only by the net force on that object alone"
    - "The horse's force on the cart is slightly larger, creating a net force forward"
  answer: 2
  explanation: "Action-reaction pairs always act on different objects. The horse pulls the cart forward with force F — this force acts on the cart. The cart pulls the horse backward with force F — this force acts on the horse. Apply Newton's second law to each separately: the cart accelerates forward if F exceeds friction on the cart. The paired forces never cancel because they are on different objects."

- question: "A book sits still on a table. The force of gravity pulls it downward, and the normal force from the table pushes it upward. Are these two forces a Newton's third law action-reaction pair?"
  type: multiple-choice
  options:
    - "Yes — they are equal, opposite, and in contact with each other"
    - "No — they act on the same object (the book); Newton's third law pairs always act on two different objects"
    - "Yes — any two equal and opposite forces constitute a Newton's third law pair"
    - "No — action-reaction pairs must involve the same type of force, and gravity and normal force are different types"
  answer: 1
  explanation: "Balanced forces and Newton's third law pairs are distinct. Gravity and the normal force both act on the book — they are balanced forces on a single object producing zero net force. The actual Newton's third law partner of 'Earth's gravity pulls the book downward' is 'the book's gravity pulls Earth upward.' The third-law pair must involve the same type of force and act on two different objects."

- question: "Newton's third law force pairs always act on two different objects."
  type: true-false
  answer: true
  explanation: "This is the defining property that distinguishes Newton's third law pairs from balanced forces. When A exerts a force on B, B exerts an equal and opposite force on A — always on A and B separately, never both on the same object. This is why the two forces do not cancel: cancellation would require them to act on the same object."

- question: "If you push a wall and the wall pushes back on you with an equal and opposite force, the two forces cancel and you experience zero net force."
  type: true-false
  answer: false
  explanation: "The two forces act on different objects — your force acts on the wall, and the wall's force acts on you. 'Canceling' requires forces to act on the same object. You do experience the wall's force (which is why you don't accelerate into the wall), but that force acts only on you. The wall simultaneously experiences only your force. Net force on each object is computed from forces on that object alone."

- question: "Why don't action-reaction force pairs cancel each other out, even though they are always equal in magnitude and opposite in direction?"
  type: short-answer
  answer: "Because the two forces in an action-reaction pair act on different objects. Cancellation requires two forces to act on the same object and sum to zero. Newton's second law applies to a single object — you sum only the forces on that object. The paired force acts on the other object entirely and plays no role in the first object's equation of motion."
  explanation: "A book rests on a table because gravity and the normal force (both on the book) cancel — these are not a third-law pair. The third-law partner of the table's normal force on the book is the book's normal force on the table — a different force on a different object. Only forces on the same object can cancel."
```

## Explainer

From Newton's second law, you know that the net force on an object determines its acceleration: **F**_net = m**a**. But Newton's second law doesn't say where forces come from. Newton's third law fills that gap: forces always come in pairs. Every force is one member of an **action-reaction pair** — for every force object A exerts on object B, object B exerts an equal and opposite force on object A. Forces don't exist in isolation; they are interactions between two objects, and both objects always feel the effect.

The central confusion to dissolve: if action and reaction forces are equal and opposite, why does anything ever accelerate? The answer is that **they act on different objects**. When you push a box forward with force F, the box pushes back on you with force F in the opposite direction. Apply Newton's second law to each object separately: the box experiences force F forward and accelerates forward; you experience force F backward and decelerate (or accelerate backward). The two forces don't cancel because they act on different objects — each affects only its own object's motion.

Compare this carefully with **balanced forces**, which do act on the same object and do produce zero net force. A book resting on a table has two forces acting on it: gravity pulling it downward and the table's normal force pushing it upward. These are equal and opposite, they act on the same object (the book), their net effect is zero, and the book stays still. These are not a Newton's third law pair. The actual third-law partner of "Earth pulls book downward" is "book pulls Earth upward" — a tiny gravitational force the book exerts on the Earth, which is so massive it accelerates imperceptibly. Identifying genuine action-reaction pairs requires checking that the forces are of the same type (both gravitational, or both contact), equal in magnitude, opposite in direction, and acting on two different objects.

The rocket example shows the third law's power in the absence of any obvious "thing to push against." In empty space, a rocket engine expels exhaust gas backward. The engine pushes the gas backward; by Newton's third law, the gas pushes the rocket forward with equal force. The rocket doesn't need ground, air, or anything else to push against — the interaction with the ejected exhaust is sufficient. Every form of locomotion exploits the same principle: your foot pushes backward on the ground, the ground pushes forward on you; a propeller pushes air backward, the air pushes the aircraft forward; a swimmer's hand pushes water backward, the water pushes the swimmer forward. In each case, moving requires accelerating something else in the opposite direction — the third law ensures these always come together.
