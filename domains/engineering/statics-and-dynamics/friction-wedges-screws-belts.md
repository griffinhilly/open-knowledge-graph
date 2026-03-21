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

## Questions

```yaml
- question: "A rope is wrapped around a post with contact angle β = π radians (half a turn), with μ = 0.3. The slack-side tension is T_slack = 50 N. A student doubles the wrap to β = 2π (one full turn). How does the tight-side tension T_tight change?"
  type: multiple-choice
  options:
    - "It doubles — the tension ratio is proportional to the wrap angle"
    - "It quadruples — doubling the wrap angle squares the achievable tension ratio"
    - "It increases by e^(0.3π) — adding one more half-turn multiplies the ratio by the same factor"
    - "It stays the same — T_tight depends on the applied force, not the wrap angle"
  answer: 2
  explanation: "The belt friction equation is T_tight/T_slack = e^(μβ). At β = π: ratio = e^(0.3π) ≈ 2.57, so T_tight ≈ 128 N. At β = 2π: ratio = e^(0.6π) ≈ 6.59, so T_tight ≈ 330 N. Doubling β from π to 2π squares the ratio (e^(0.6π) = (e^(0.3π))²), not doubles it. This exponential relationship is why a few turns of rope around a capstan can hold enormous loads — adding half a turn doesn't add a fixed amount, it multiplies the existing ratio by e^(μπ)."

- question: "A square-threaded screw has lead angle λ = 8° and the friction angle φ_s = arctan(μ_s) = 12°. What happens when the driving torque is removed while the screw is loaded?"
  type: multiple-choice
  options:
    - "The screw back-drives — the load pushes it backward because the lead angle is less than 45°"
    - "The screw self-locks — friction is strong enough to prevent back-driving because λ < φ_s"
    - "The screw back-drives — the load always overcomes static friction unless the thread is locked mechanically"
    - "The screw self-locks only if the load is applied axially; radial loads always cause back-driving"
  answer: 1
  explanation: "The self-locking condition for a screw is λ < φ_s. Here λ = 8° < φ_s = 12°, so the screw self-locks. The lead angle measures how steeply the thread helix rises; the friction angle measures the angle at which friction force can balance the load's tendency to push the nut backward down the thread. When the lead angle is shallower than the friction angle, friction wins and the screw stays put. Standard fasteners are designed this way — if λ > φ_s, the screw would unscrew under vibration."

- question: "In a belt friction problem, the tight side always carries higher tension than the slack side, and identifying which side is tight requires knowing the direction of impending motion."
  type: true-false
  answer: true
  explanation: "The belt friction equation T_tight/T_slack = e^(μβ) always gives a ratio ≥ 1 (since e^(μβ) > 1 for μ, β > 0), so the tight side always has higher tension. Which side is tight depends on the physical setup: the tight side is the side the load or motion tends to pull the belt toward. Identifying tight vs. slack from the direction of impending motion must happen before applying the formula — applying it backward gives an inverted ratio that is less than 1, predicting a physically impossible configuration."

- question: "Doubling the contact angle β in a belt friction problem doubles the achievable tension ratio T_tight/T_slack."
  type: true-false
  answer: false
  explanation: "The relationship is exponential, not linear: T_tight/T_slack = e^(μβ). Doubling β replaces e^(μβ) with e^(2μβ) = (e^(μβ))², which squares the original ratio. For example, if the original ratio is 3, doubling the wrap angle gives ratio 9, not 6. This exponential behavior is the engineering power of capstans and bollards — a small number of additional turns produces a dramatically larger holding force, not a proportional increase."

- question: "Explain why the self-locking condition for a screw (λ < φ_s) means the screw will not back-drive under axial load. What physical mechanism keeps the screw from unscrewing when the driving torque is removed?"
  type: short-answer
  answer: "A screw thread is geometrically a wedge wrapped around a cylinder. When an axial load tries to push the screw backward (unscrew it), the load's component along the thread helix must overcome the friction force at the thread surface. The lead angle λ controls how much of the axial load resolves into a back-driving force along the thread; the friction angle φ_s controls the maximum friction available to resist it. When λ < φ_s, the friction force is larger than the component of the load trying to slide the thread backward, so the thread stays in place — friction self-locks the system."
  explanation: "This is exactly the wedge self-locking analysis applied to a helical geometry. Standard bolts and machine screws use fine threads (small lead angle) specifically to ensure self-locking. Power screws used for lifting or pressing (like a car jack) may deliberately have larger lead angles to allow back-driving, trading self-locking for mechanical advantage. The condition λ = φ_s is the tipping point: below it the screw holds, above it the screw unwinds under load."
```

## Explainer

From Coulomb's friction law, you know that a friction force at impending motion equals μₛN, where N is the normal force and the friction force opposes relative sliding. That single rule generates surprisingly rich behavior when applied to specific geometric configurations — wedges, screws, and belts — where friction becomes a deliberate engineering mechanism rather than an unavoidable loss.

A **wedge** converts a horizontal push into a vertical lift by changing the direction of the normal force. Two surfaces are in contact, and friction opposes motion at both interfaces simultaneously. The key technique is drawing separate free body diagrams for each contacting surface: the wedge itself and the block being lifted both have their own normal and friction forces, related by Newton's third law at the shared interface. Writing equilibrium equations for both FBDs gives enough equations to find the input force needed. The wedge angle determines mechanical advantage; the friction angle φₛ = arctan(μₛ) determines whether the system self-locks when the driving force is removed.

A **screw thread** is geometrically a wedge wrapped around a cylinder. As the screw advances by one **lead** (the axial distance per full revolution), the thread traces a helix at the **lead angle** λ = arctan(lead / 2πr). The torque required to advance the screw against a load maps exactly onto the wedge-pushing-a-block problem. The **self-locking condition** is λ < φₛ: if the lead angle is shallower than the friction angle, friction is strong enough to prevent back-driving under load. Standard fastening screws are designed to satisfy this condition, which is why they don't unscrew under vibration.

The **belt friction** problem has a different geometry — a rope or strap wrapped around a curved surface — but the same Coulomb friction at work. Consider a small arc element of the belt: the normal force between belt and surface generates a friction force tangent to the surface. Integrating this differential relationship around the entire contact angle β gives the exponential result T_tight/T_slack = e^(μβ), where β is in radians. The exponential is dramatic: doubling the wrap angle squares the achievable tension ratio. A few turns of rope around a capstan can hold enormous loads with modest force on the free end — this is the principle behind ship bollards, fishing reels, and rock-climbing belays. Identifying which side is tight and which is slack (from the direction of impending motion) must come before applying the formula.
