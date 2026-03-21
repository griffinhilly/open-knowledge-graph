---
id: total-internal-reflection
title: Total Internal Reflection
domain: physics
course: waves-and-optics
prerequisites:
- id: snells-law
  type: hard
builds-toward:
- dispersion-and-prisms
tags:
- total internal reflection
- critical angle
- fiber optics
- TIR
stage: formal-systems
status: validated
---

# Total Internal Reflection

## Core Idea
When light travels from a denser medium (higher n) to a less dense medium, the refracted ray bends away from the normal. At the critical angle θ_c = arcsin(n₂/n₁), the refracted ray lies along the boundary. For angles greater than θ_c, no refracted ray exists and all light is reflected back — total internal reflection. This phenomenon is exploited in optical fibers, which guide light over long distances with minimal loss, and in reflective prisms.

## How It's Best Learned
Shine a laser from inside a semicircular glass block at the flat face. Slowly rotate the block and observe the refracted ray bending away until it disappears at the critical angle. Calculate θ_c and compare to observation.

## Common Misconceptions
- TIR only occurs going from high-n to low-n, not the reverse.
- At exactly the critical angle there is still refraction (grazing angle), not total reflection; total reflection requires exceeding the critical angle.

## Questions

```yaml
- question: "A light ray travels from glass (n = 1.5) toward air (n = 1.0). The angle of incidence is gradually increased from 0°. What happens when the angle exactly equals the critical angle?"
  type: multiple-choice
  options:
    - "All light is reflected back into the glass and the refracted ray disappears"
    - "The refracted ray travels along the glass-air interface at 90° to the normal; TIR begins for any larger angle"
    - "The reflected and refracted rays have exactly equal intensities"
    - "The angle of refraction equals the angle of incidence"
  answer: 1
  explanation: "At the critical angle, sin θ_c = n₂/n₁ = 1.0/1.5, so θ₂ = 90° — the refracted ray just grazes the boundary. This is the threshold: at this angle there is still a (grazing) refracted ray. For any angle greater than θ_c, the math requires sin θ₂ > 1, which is impossible, so no refracted ray exists and all energy reflects back. Option A describes what happens beyond the critical angle, not at it exactly."

- question: "A student shines light from air into water and increases the angle of incidence all the way to 85°. Why does total internal reflection not occur?"
  type: multiple-choice
  options:
    - "The angle is not large enough — the critical angle for the air-water interface is greater than 85°"
    - "TIR requires light to travel from the denser medium into the less dense medium; light going from air into water cannot undergo TIR regardless of angle"
    - "TIR only occurs in manufactured materials like optical fiber glass, not in water"
    - "The light is partially absorbed by the water before it can reflect"
  answer: 1
  explanation: "TIR is fundamentally asymmetric: it only occurs when light travels from a denser medium (higher n) to a less dense medium (lower n). Going from air (n ≈ 1.0) into water (n ≈ 1.33) is the wrong direction — the refracted ray bends toward the normal, and the refraction angle is always less than the incidence angle. There is no critical angle for this direction because sin θ₂ = (n₁/n₂) sin θ₁ < sin θ₁, never reaching 90°."

- question: "At angles greater than the critical angle, the interface between two media acts as a perfect mirror — all incident light is reflected with no energy loss."
  type: true-false
  answer: true
  explanation: "TIR is lossless in principle because there is no refracted ray into which energy can be transmitted. The evanescent field technically penetrates a fraction of a wavelength into the second medium, but no net energy is carried away. This is fundamentally different from ordinary reflection off a metal mirror (which absorbs a few percent) or off a glass surface near normal incidence (which reflects only ~4%). The lossless nature of TIR is what makes it so valuable for optical fibers."

- question: "Total internal reflection can occur when light travels from air into glass if the angle of incidence is large enough."
  type: true-false
  answer: false
  explanation: "TIR requires traveling from a higher-index medium into a lower-index medium. Air has n ≈ 1.0; glass has n ≈ 1.5. Light going from air into glass is moving into a denser medium, where refraction bends the ray toward the normal — the refraction angle is always less than the incidence angle and can never reach 90°. The sin factor (n_air/n_glass < 1) ensures no critical angle exists for this direction."

- question: "Explain why optical fibers can transmit light over kilometers with minimal loss, using the concept of total internal reflection."
  type: short-answer
  answer: "An optical fiber has a glass core with higher refractive index surrounded by cladding with a slightly lower index. Light entering the fiber at a shallow enough angle hits the core-cladding interface at an angle exceeding the critical angle, triggering TIR. The light reflects perfectly back into the core — no energy escapes into the cladding. This process repeats at every bounce along the entire length of the fiber. Since TIR is lossless, the only significant attenuation comes from absorption within the glass itself, not from the reflections."
  explanation: "The key insight is that TIR is not just 'good reflection' — it is theoretically perfect reflection. Conventional mirrors and partial reflections lose a small percentage at each bounce, which compounds over thousands of reflections across kilometers. TIR loses essentially nothing per bounce. The fiber geometry is designed so that any light ray within the acceptance cone strikes the boundary beyond the critical angle, guaranteeing TIR for the entire guided signal."
```

## Explainer

From Snell's law, you know that when light crosses from a medium with index n₁ into one with lower index n₂ < n₁, the refracted ray bends *away* from the normal — the angle of refraction is larger than the angle of incidence. Snell's law says n₁ sin θ₁ = n₂ sin θ₂, so sin θ₂ = (n₁/n₂) sin θ₁. Because n₁/n₂ > 1, sin θ₂ > sin θ₁. As you increase the incident angle θ₁, the refracted angle θ₂ grows faster. At some point, θ₂ reaches 90° — the refracted ray would travel along the boundary surface. The **critical angle** θ_c is precisely where this happens: sin θ_c = n₂/n₁, which is why the formula uses the ratio of the two indices.

What happens beyond the critical angle? There is no angle whose sine exceeds 1, so the math tells you no real refracted ray can exist. Physically, the energy that would have gone into refraction has nowhere to go except back into the original medium. The interface acts like a perfect mirror: **all** the incident light is reflected, with zero loss. This is fundamentally different from ordinary reflection from a silver mirror (which absorbs a few percent) or reflection off glass (which reflects at most ~4% per surface near normal incidence). Total internal reflection is lossless in principle, which is what makes it so useful.

The most important application is the **optical fiber**. A glass fiber with core index n_core is surrounded by cladding with a slightly lower index n_cladding. Light entering the fiber at a shallow angle hits the core-cladding interface at an angle greater than the critical angle — and is totally reflected back into the core. This happens over and over along the entire length of the fiber, bouncing the light forward with almost no loss even over kilometers. Modern telecommunications, internet infrastructure, and medical endoscopes all depend on this principle. The purity of the glass determines how far light can travel before absorption, not reflection losses.

An intuition check: TIR only occurs going from high-n to low-n. If you try to shine light from air into glass and increase the angle, you never get TIR — the refracted ray bends *toward* the normal in the denser medium, and the refracted angle is always less than the incident angle, never reaching 90°. The physics that produces TIR is fundamentally asymmetric: it requires the light to be traveling in the denser medium, trying to exit into the less-dense one. This is why you can see TIR effects in a swimming pool (light from inside the water trying to exit into air), but not from outside looking in.
