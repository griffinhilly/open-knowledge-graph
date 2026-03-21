---
id: friction-forces
title: 'Friction: Static and Kinetic'
domain: physics
course: classical-mechanics
prerequisites:
- id: free-body-diagrams
  type: hard
- id: newtons-second-law
  type: hard
- id: newtons-third-law
  type: soft
builds-toward:
- work-and-energy
- conservation-of-energy
tags:
- friction
- static-friction
- kinetic-friction
- normal-force
stage: formal-systems
status: validated
---
# Friction: Static and Kinetic

## Core Idea
Friction is a contact force that opposes relative sliding motion between surfaces. Static friction (f_s ≤ μ_s N) prevents surfaces from sliding; it adjusts up to its maximum. Kinetic friction (f_k = μ_k N) acts once surfaces are sliding and has a fixed magnitude. Both are proportional to the normal force N through coefficients μ that depend on the materials in contact.

## How It's Best Learned
Solve inclined-plane problems systematically: decompose weight into components parallel and perpendicular to the slope, find N, then compute friction. Check whether the object is on the verge of sliding (use static friction inequality) or already sliding (use kinetic friction equation).

## Common Misconceptions
- Thinking friction always equals μN — static friction only equals μ_s N at its maximum.
- Believing friction always opposes motion: static friction opposes the tendency of motion, which may not align with the direction of motion.
- Assuming μ depends on surface area — it depends on material properties, not contact area.

## Questions

```yaml
- question: "A 10 kg box rests on a horizontal surface with μ_s = 0.4 and μ_k = 0.3. You push it with a 20 N horizontal force. The maximum static friction force is 39.2 N. Is the box moving, and what is the friction force?"
  type: multiple-choice
  options:
    - "Yes, moving; friction = 29.4 N (kinetic friction)"
    - "No, stationary; friction = 39.2 N (maximum static friction)"
    - "No, stationary; friction = 20 N (static friction adjusts to exactly balance the applied force)"
    - "Yes, moving; friction = 39.2 N (static friction at maximum)"
  answer: 2
  explanation: "Static friction is a constraint force — it takes whatever value is needed to prevent sliding, up to its maximum. Since the applied 20 N is less than the maximum static friction of 39.2 N, the box doesn't slide. Static friction adjusts to exactly 20 N to maintain equilibrium. It only equals μ_s N at the moment of impending motion. This is the most common misconception: students assume friction always equals μN, but that is only true at the threshold of sliding."

- question: "Why does it typically require more force to start an object sliding than to keep it sliding once motion begins?"
  type: multiple-choice
  options:
    - "The contact area between surfaces increases as the object begins to move, creating more resistance"
    - "The normal force decreases slightly once the object is in motion, reducing the friction"
    - "The coefficient of kinetic friction is smaller than the coefficient of static friction for most material pairs, so the friction force drops once sliding begins"
    - "Momentum must be overcome before motion starts, adding to the required force"
  answer: 2
  explanation: "For most material pairs, μ_k < μ_s. Before sliding, static friction can provide up to μ_s N of resistance. Once sliding begins, friction drops to the fixed value μ_k N. This is why furniture is hardest to move when you first push it — you must overcome maximum static friction to initiate motion, but once it's sliding, the required force drops. Contact area and momentum are irrelevant; the coefficient values are the explanation."

- question: "The friction force acting on a stationary object always equals μ_s × N, where μ_s is the coefficient of static friction and N is the normal force."
  type: true-false
  answer: false
  explanation: "This is the central misconception about static friction. Static friction is variable — it takes whatever value maintains equilibrium, which can be anywhere from zero up to μ_s N. It equals μ_s N only when the object is on the verge of sliding (impending motion). A box sitting undisturbed on a floor with no applied force has zero static friction, not μ_s N."

- question: "Both the coefficient of static friction and the coefficient of kinetic friction between two surfaces are independent of the contact area between those surfaces."
  type: true-false
  answer: true
  explanation: "This surprises many students who intuit that more surface area in contact means more friction. In the standard friction model, both μ_s and μ_k depend only on the material properties of the contacting surfaces (e.g., rubber on concrete vs. wood on wood), not on how large the contact patch is. A wide tire and a narrow tire of the same rubber compound on the same road surface have the same friction coefficients."

- question: "A student says 'friction always opposes motion.' Why is this description incomplete, and what is the more precise statement?"
  type: short-answer
  answer: "For kinetic friction, opposing the direction of sliding is accurate. But static friction opposes the tendency of relative motion — the direction the surface would slide if friction weren't present — which may differ from the direction of any actual motion. A book on an accelerating car experiences static friction acting forward (in the direction of motion) because that's what prevents the book from sliding backward relative to the car."
  explanation: "The distinction matters for free-body diagram analysis. Static friction acts to maintain the no-slip condition, so its direction is whatever is needed to prevent relative sliding — not necessarily opposite to the direction of travel. Always ask: 'Which direction would this surface tend to slide without friction?' Static friction opposes that tendency."
```

## Explainer

From your work with free-body diagrams and Newton's second law, you know how to identify forces and apply ΣF = ma. Friction is a contact force that appears at the interface between surfaces — it always acts tangent to the surface (parallel to it), in the direction that opposes relative sliding or the tendency of sliding. Understanding friction requires recognizing that it comes in two fundamentally different regimes depending on whether the surfaces are moving relative to each other.

**Static friction** acts when two surfaces are in contact but not sliding. Its crucial property is that it is *variable*, not fixed. When you push gently on a heavy box and it doesn't move, static friction adjusts to exactly cancel your push — it takes whatever value is needed to maintain equilibrium. Push harder and static friction increases to match. This continues until you reach the maximum static friction force: f_{s,max} = μ_s N, where μ_s is the **coefficient of static friction** and N is the normal force. At that point, if you push any harder, the box starts to slide. Static friction is a **constraint force** — it enforces the constraint that the surfaces don't slide, up to a limit.

Once surfaces are sliding, **kinetic friction** takes over. Unlike static friction, kinetic friction has a single fixed value: f_k = μ_k N, where μ_k is the **coefficient of kinetic friction**. It always acts opposite to the velocity of sliding. Importantly, μ_k < μ_s for most material pairs, which is why it takes more force to start an object sliding than to keep it sliding — you have likely noticed this when pushing furniture. Both coefficients depend only on the materials in contact (wood on wood, rubber on concrete, etc.), not on the contact area or the speed of sliding.

The inclined-plane problem makes these ideas concrete. A block of weight W sits on a slope at angle θ. Decompose W: the component perpendicular to the slope is W cos θ (balanced by the normal force N = W cos θ), and the component parallel to the slope, pulling the block downhill, is W sin θ. The maximum static friction force is μ_s N = μ_s W cos θ. The block slides when the downhill pull exceeds this maximum — when W sin θ > μ_s W cos θ, which simplifies to tan θ > μ_s. This gives the **critical angle**: the steepest slope a block can sit on without sliding, equal to arctan(μ_s). Once sliding, the net force downhill is W sin θ − μ_k W cos θ = W(sin θ − μ_k cos θ), which by Newton's second law gives the acceleration. All of classical friction analysis is built from this one technique: find N, determine which regime applies, compute the friction force, and include it in ΣF = ma.
