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

## Explainer

From Snell's law, you know that when light crosses from a medium with index n₁ into one with lower index n₂ < n₁, the refracted ray bends *away* from the normal — the angle of refraction is larger than the angle of incidence. Snell's law says n₁ sin θ₁ = n₂ sin θ₂, so sin θ₂ = (n₁/n₂) sin θ₁. Because n₁/n₂ > 1, sin θ₂ > sin θ₁. As you increase the incident angle θ₁, the refracted angle θ₂ grows faster. At some point, θ₂ reaches 90° — the refracted ray would travel along the boundary surface. The **critical angle** θ_c is precisely where this happens: sin θ_c = n₂/n₁, which is why the formula uses the ratio of the two indices.

What happens beyond the critical angle? There is no angle whose sine exceeds 1, so the math tells you no real refracted ray can exist. Physically, the energy that would have gone into refraction has nowhere to go except back into the original medium. The interface acts like a perfect mirror: **all** the incident light is reflected, with zero loss. This is fundamentally different from ordinary reflection from a silver mirror (which absorbs a few percent) or reflection off glass (which reflects at most ~4% per surface near normal incidence). Total internal reflection is lossless in principle, which is what makes it so useful.

The most important application is the **optical fiber**. A glass fiber with core index n_core is surrounded by cladding with a slightly lower index n_cladding. Light entering the fiber at a shallow angle hits the core-cladding interface at an angle greater than the critical angle — and is totally reflected back into the core. This happens over and over along the entire length of the fiber, bouncing the light forward with almost no loss even over kilometers. Modern telecommunications, internet infrastructure, and medical endoscopes all depend on this principle. The purity of the glass determines how far light can travel before absorption, not reflection losses.

An intuition check: TIR only occurs going from high-n to low-n. If you try to shine light from air into glass and increase the angle, you never get TIR — the refracted ray bends *toward* the normal in the denser medium, and the refracted angle is always less than the incident angle, never reaching 90°. The physics that produces TIR is fundamentally asymmetric: it requires the light to be traveling in the denser medium, trying to exit into the less-dense one. This is why you can see TIR effects in a swimming pool (light from inside the water trying to exit into air), but not from outside looking in.
