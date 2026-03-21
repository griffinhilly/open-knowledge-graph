---
id: critical-angle-derivation
title: Critical Angle and Total Internal Reflection Derivation
domain: physics
course: waves-and-optics
prerequisites:
- id: total-internal-reflection
  type: soft
- id: snells-law
  type: hard
builds-toward:
- fiber-optics-and-waveguides
tags:
- total-internal-reflection
- critical-angle
stage: formal-systems
status: draft
---

# Critical Angle and Total Internal Reflection Derivation

## Core Idea
When light travels from a denser to less dense medium, total internal reflection occurs when the incident angle exceeds the critical angle θc = arcsin(n₂/n₁). At this angle, the refracted ray would be 90°; beyond it, all light reflects. This phenomenon is essential for fiber optics and optical waveguides.

## Questions

```yaml
- question: "A glass fiber (n = 1.5) is submerged in water (n = 1.33) instead of air (n = 1.0). Compared to air-clad fiber, the critical angle for total internal reflection is:"
  type: multiple-choice
  options:
    - "Smaller — the index contrast is less, so TIR requires a smaller incident angle"
    - "Larger — the index contrast is less, so the critical angle increases"
    - "The same — the critical angle depends only on the core index, not the cladding"
    - "Undefined — TIR cannot occur between glass and water"
  answer: 1
  explanation: "The critical angle is θc = arcsin(n₂/n₁). With air cladding: arcsin(1.0/1.5) ≈ 41.8°. With water cladding: arcsin(1.33/1.5) ≈ 62.5°. A larger critical angle means light must hit the interface at a steeper angle to achieve TIR, making it harder to confine. The index *contrast* (n₁ − n₂) determines how tightly light is trapped — lower contrast means a larger critical angle and a narrower acceptance cone for the fiber."

- question: "A diver shines a flashlight upward from underwater toward the surface. As the diver tilts the beam from straight-up toward horizontal, what happens at the critical angle?"
  type: multiple-choice
  options:
    - "The light refracts into the air at 90° to the normal, skimming along the water surface"
    - "The light reflects back down and also refracts straight up through the surface at 0°"
    - "The light stops traveling and is absorbed at the interface"
    - "Nothing special happens; the light continues refracting normally"
  answer: 0
  explanation: "At exactly the critical angle, the refracted ray would be at θ₂ = 90° — traveling along the interface rather than into the air. This is the boundary condition from which the formula is derived: setting θ₂ = 90° in Snell's law gives n₁ sin θc = n₂ sin 90° = n₂. Beyond this angle, sin θ₂ would need to exceed 1, which is impossible — so no refracted ray exists and all light reflects back into the water."

- question: "Total internal reflection can occur when light travels from air into glass."
  type: true-false
  answer: false
  explanation: "TIR requires traveling from a denser medium (higher n) to a less dense one (lower n). Going from air (n ≈ 1.0) into glass (n ≈ 1.5), the refracted ray bends *toward* the normal — θ₂ < θ₁. No matter how steep the incident angle, refraction still occurs. The critical angle formula θc = arcsin(n₂/n₁) only yields a valid angle when n₂ < n₁; otherwise arcsin gives a value greater than 1, which has no solution — meaning TIR is impossible in that direction."

- question: "The critical angle is the minimum angle of incidence at which total internal reflection occurs."
  type: true-false
  answer: false
  explanation: "The critical angle is the *minimum* angle at which TIR occurs only in the sense that TIR happens at angles *equal to or greater than* θc. Below the critical angle, light partially refracts and partially reflects. At the critical angle and above, all light reflects internally. So the critical angle is a lower threshold — TIR occurs for all angles ≥ θc, not just at the critical angle itself."

- question: "Why does Snell's law 'have no solution' for the refracted angle when the incident angle exceeds the critical angle? What does this mean physically?"
  type: short-answer
  answer: "Snell's law requires sin θ₂ = (n₁/n₂) sin θ₁. When n₁ > n₂ and θ₁ > θc, the product (n₁/n₂) sin θ₁ exceeds 1. Since sin of any real angle cannot exceed 1, there is no real angle θ₂ that satisfies the equation. Physically, this means there is no direction the refracted ray could travel — geometry prohibits any transmitted ray from existing, so all light reflects back into the denser medium."
  explanation: "This is the key insight: TIR is not a mysterious special phenomenon but simply the consequence of refraction becoming geometrically impossible. The mathematics breaks down because you would need the refracted ray to travel at an angle whose sine exceeds 1. Nature's response is total reflection. Understanding this as 'refraction forbidden → reflection required' is more powerful than memorizing the formula, because it explains why the transition at θc is sharp and complete."
```

## Explainer

The critical angle derivation is a direct consequence of Snell's law pushed to its logical limit. Recall Snell's law from your prerequisite work: n₁ sin θ₁ = n₂ sin θ₂. When light moves from a denser medium (higher n₁, like glass) into a less dense one (lower n₂, like air), the refracted ray bends away from the normal — θ₂ > θ₁. As you increase the incident angle θ₁, the refracted angle θ₂ grows faster. The question is: what happens when θ₂ tries to reach 90°?

At θ₂ = 90°, the refracted ray would travel exactly along the interface — it skims the surface and never actually enters the second medium. Plugging this into Snell's law: n₁ sin θc = n₂ sin 90° = n₂. Solving for the **critical angle**: θc = arcsin(n₂/n₁). This is the threshold. At angles below θc, light partially refracts and partially reflects (as you know from normal refraction). At angles above θc, Snell's law has no solution — there is no refracted ray — and all the light reflects back into the first medium. This is **total internal reflection**.

The key intuition is that total internal reflection is not a special phenomenon — it is simply what happens when refraction becomes geometrically impossible. The math doesn't give you a valid θ₂ above θc because sin θ₂ would need to exceed 1, which has no physical solution. Nature's response is to reflect all the light instead. Think of it as the boundary refusing to let light through.

The practical consequence is striking: light trapped inside a glass fiber by total internal reflection can travel enormous distances with almost no loss, because it never escapes the sides of the fiber. Every bend in a fiber-optic cable maintains the critical angle condition, keeping the light bouncing internally from wall to wall. The same principle explains why a swimming pool bottom looks silvery when you look at it from a shallow angle underwater, and why diamonds are cut at angles that maximize total internal reflection — trapping light inside until it exits through the top face.
