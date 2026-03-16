---
id: friction-wedges-screws-belts
title: 'Friction Applications: Wedges, Screws, and Belts'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: dry-friction-coulombs-law
  type: hard
tags:
- statics
- friction
- wedges
- screws
- belt friction
stage: formal-systems
status: validated
---

# Friction Applications: Wedges, Screws, and Belts

## Core Idea
Wedge, screw, and belt problems apply Coulomb friction in specific geometric configurations. Wedge analysis draws separate FBDs for each contacting surface with friction at impending motion. Square-threaded screw mechanics reduces to a wrapped wedge problem, yielding the torque-load relationship and the self-locking condition: a screw is self-locking when the lead angle λ < φ_s (angle of friction). For flat belts or ropes over curved surfaces, the belt friction equation T_tight/T_slack = e^(μβ) relates the tight and slack-side tensions, where β is the contact angle in radians.

## How It's Best Learned
For wedge problems, draw FBDs of each contacting surface separately. For belt problems, identify the tight and slack sides from the direction of motion or impending motion before applying the exponential formula.

## Common Misconceptions
- Forgetting that friction forces act mutually on both contacting bodies.
- In belt problems, incorrectly identifying which side carries higher tension.
- Assuming a screw is always self-locking without verifying the lead angle condition.

## Explainer

From Coulomb's friction law, you know that a friction force at impending motion equals μₛN, where N is the normal force and the friction force opposes relative sliding. That single rule generates surprisingly rich behavior when applied to specific geometric configurations — wedges, screws, and belts — where friction becomes a deliberate engineering mechanism rather than an unavoidable loss.

A **wedge** converts a horizontal push into a vertical lift by changing the direction of the normal force. Two surfaces are in contact, and friction opposes motion at both interfaces simultaneously. The key technique is drawing separate free body diagrams for each contacting surface: the wedge itself and the block being lifted both have their own normal and friction forces, related by Newton's third law at the shared interface. Writing equilibrium equations for both FBDs gives enough equations to find the input force needed. The wedge angle determines mechanical advantage; the friction angle φₛ = arctan(μₛ) determines whether the system self-locks when the driving force is removed.

A **screw thread** is geometrically a wedge wrapped around a cylinder. As the screw advances by one **lead** (the axial distance per full revolution), the thread traces a helix at the **lead angle** λ = arctan(lead / 2πr). The torque required to advance the screw against a load maps exactly onto the wedge-pushing-a-block problem. The **self-locking condition** is λ < φₛ: if the lead angle is shallower than the friction angle, friction is strong enough to prevent back-driving under load. Standard fastening screws are designed to satisfy this condition, which is why they don't unscrew under vibration.

The **belt friction** problem has a different geometry — a rope or strap wrapped around a curved surface — but the same Coulomb friction at work. Consider a small arc element of the belt: the normal force between belt and surface generates a friction force tangent to the surface. Integrating this differential relationship around the entire contact angle β gives the exponential result T_tight/T_slack = e^(μβ), where β is in radians. The exponential is dramatic: doubling the wrap angle squares the achievable tension ratio. A few turns of rope around a capstan can hold enormous loads with modest force on the free end — this is the principle behind ship bollards, fishing reels, and rock-climbing belays. Identifying which side is tight and which is slack (from the direction of impending motion) must come before applying the formula.
