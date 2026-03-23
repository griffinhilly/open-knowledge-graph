---
id: non-newtonian-fluids
title: Non-Newtonian Fluids
domain: engineering
course: fluid-mechanics
prerequisites:
- id: viscosity-and-newtonian-fluids
  type: hard
tags:
- non-Newtonian
- shear thinning
- shear thickening
- Bingham plastic
- viscoelastic
- rheology
- power-law fluid
stage: formal-systems
status: validated
---
# Non-Newtonian Fluids

## Core Idea
Non-Newtonian fluids are those whose shear stress is not linearly proportional to the strain rate — their apparent viscosity varies with shear rate, time, or flow history. The most common models are: shear-thinning (pseudoplastic) fluids like blood, paint, and polymer solutions, where viscosity decreases with increasing shear rate (modeled by the power-law τ = Kγ̇ⁿ with n < 1); shear-thickening (dilatant) fluids like cornstarch suspensions, where viscosity increases with shear rate (n > 1); and Bingham plastics like toothpaste and drilling mud, which behave as solids below a yield stress τ_y and flow as viscous fluids above it (τ = τ_y + μ_p·γ̇). Viscoelastic fluids (like polymer melts) exhibit both viscous and elastic behavior — they can store energy and exhibit phenomena like die swell, rod climbing (Weissenberg effect), and elastic recoil. Rheometry — controlled shear and extensional testing — is used to characterize these complex behaviors.

## How It's Best Learned
Derive the velocity profile for a power-law fluid in a pipe (it changes from parabolic to blunted for n < 1 and pointed for n > 1) and compare it to the Newtonian parabolic profile. Sketch the shear stress vs. strain rate curves for Newtonian, shear-thinning, shear-thickening, and Bingham plastic fluids on the same axes. Study real examples: why does ketchup flow easily when shaken (thixotropy), why does paint stay on a wall after brushing (shear-thinning with recovery), and why does a polymer solution climb a rotating rod (normal stress differences).

## Common Misconceptions
- Shear-thinning and thixotropy are not the same. Shear-thinning is an instantaneous decrease of viscosity with shear rate; thixotropy is a time-dependent decrease at constant shear rate (the fluid's structure gradually breaks down). Many real fluids exhibit both.
- The power-law model τ = Kγ̇ⁿ fails at very low and very high shear rates, where real shear-thinning fluids approach constant Newtonian plateaus (zero-shear viscosity η₀ and infinite-shear viscosity η∞). The Carreau or Cross models capture these limits.
- Yield stress is a practical concept, not always a sharp physical threshold. Whether a material has a "true" yield stress or simply a very high viscosity at low shear rates is debated (the "yield stress myth" controversy), but the Bingham model remains a useful engineering approximation.

## Questions

```yaml
- question: "Paint flows easily under the high shear of a brush stroke but then stays on the wall without dripping once applied. Which type of non-Newtonian behavior does this describe?"
  type: multiple-choice
  options:
    - "Shear-thickening (dilatant) — the paint hardens when the brush applies force"
    - "Bingham plastic — the paint has a yield stress that keeps it in place once extruded from the brush"
    - "Shear-thinning (pseudoplastic) — viscosity is low under the high shear of brushing and recovers at rest"
    - "Viscoelastic — the paint stores elastic energy during brushing and releases it afterward"
  answer: 2
  explanation: "Shear-thinning fluids have an apparent viscosity that decreases as shear rate increases. During brushing, the high shear rate reduces viscosity dramatically, making the paint flow easily. Once on the wall, shear rate drops to near zero, and viscosity recovers — the paint becomes thick enough not to drip. This is the deliberate design goal of architectural paints. Note that the recovery happens instantaneously with the reduction in shear rate; if the recovery were time-dependent (the paint slowly thickened after the shear stopped), that would be thixotropy — a related but distinct phenomenon."

- question: "A dense cornstarch suspension flows easily when stirred gently but solidifies momentarily when struck or stepped on. Which model best describes this behavior?"
  type: multiple-choice
  options:
    - "Bingham plastic — it has a yield stress that must be overcome before flow begins"
    - "Shear-thinning — the gentle stirring exceeds the yield stress while the strike does not"
    - "Shear-thickening (dilatant) — apparent viscosity increases with increasing shear rate"
    - "Viscoelastic — stored elastic energy causes the solid-like response to impact"
  answer: 2
  explanation: "A cornstarch suspension is the classic shear-thickening (dilatant) fluid: apparent viscosity increases as shear rate increases (power-law exponent n > 1). Gentle stirring applies low shear, giving low viscosity and easy flow. A sudden strike applies very high shear rate, dramatically increasing apparent viscosity and producing solid-like resistance. This is opposite to shear-thinning behavior. Note the contrast with Bingham plastics: cornstarch flows at low shear rates but resists at high shear rates, while a Bingham plastic is solid below a yield stress and flows above it."

- question: "Shear-thinning and thixotropy are two names for the same phenomenon: both describe fluids whose viscosity decreases as they are sheared."
  type: true-false
  answer: false
  explanation: "These are distinct phenomena. Shear-thinning (pseudoplastic behavior) is an instantaneous response: the apparent viscosity depends only on the current shear rate, with no memory of past shear history. Apply a shear rate, the viscosity is determined immediately. Thixotropy is time-dependent: the viscosity decreases gradually at a constant shear rate as the fluid's internal structure breaks down, and then gradually recovers when shear is removed. Many real fluids (like ketchup) are both shear-thinning and thixotropic, but the two effects operate on different timescales and arise from different mechanisms."

- question: "A Bingham plastic flows at all shear rates — below the yield stress it has very high viscosity, and above it the viscosity drops."
  type: true-false
  answer: false
  explanation: "This description incorrectly treats the yield stress as a viscosity threshold rather than a flow threshold. A true Bingham plastic does not flow at all when shear stress is below the yield stress τ_y — the material deforms elastically (like a solid) but the strain rate is zero. Only when τ > τ_y does the material flow, with a linear stress-strain rate relationship τ = τ_y + μ_p·γ̇. Toothpaste sitting on a brush is a good example: it does not slowly drip or creep — it sits immobile because the gravitational stress is below τ_y. The Bingham model is a solid-then-fluid transition, not a high-viscosity-to-low-viscosity transition."

- question: "Explain why assuming Newtonian behavior for blood would lead to incorrect predictions in cardiovascular engineering applications."
  type: short-answer
  answer: "Blood is a shear-thinning fluid: its apparent viscosity decreases as shear rate increases. In large arteries with high flow rates and high shear, blood behaves nearly Newtonian. But in small capillaries with low shear rates, blood viscosity is significantly higher than the Newtonian value — red blood cells aggregate into rouleaux (stacks) at low shear, increasing resistance. Assuming constant Newtonian viscosity would underestimate resistance in small vessels and overestimate it in large ones, giving incorrect pressure drop predictions, wrong flow distributions, and misleading predictions about conditions like atherosclerosis where local shear rates are altered. Medical device design (artificial hearts, stents) requires rheologically accurate blood models."
  explanation: "Blood's shear-thinning behavior arises from the deformability and aggregation of red blood cells. At high shear, cells deform and align, reducing viscosity. At low shear, they aggregate into rouleaux, increasing viscosity. This variation is physiologically significant: the cardiovascular system operates across a wide range of shear rates from the aorta to capillaries. The power-law or Carreau model captures this behavior far better than the Newtonian model. Beyond blood, many biological fluids (synovial fluid in joints, mucus in airways) are non-Newtonian, making rheology essential to biomedical engineering."
```

## Explainer

Your prerequisite on viscosity established the Newtonian model: shear stress τ is proportional to strain rate γ̇, with the constant of proportionality being the dynamic viscosity μ. Water, air, and most simple solvents obey this linear relationship — double the strain rate, double the stress. But this is a special case, not a universal rule. **Non-Newtonian fluids** are materials where the relationship between stress and strain rate is nonlinear, time-dependent, or both. Once you look, they are everywhere: blood, concrete, toothpaste, ketchup, polymer melts, paint, and drilling mud all behave in ways the Newtonian model cannot capture.

The simplest departure is the **power-law (Ostwald-de Waele) model**: τ = Kγ̇ⁿ, where K is a consistency index and n is the flow behavior index. When n = 1, you recover the Newtonian case. When n < 1, the **apparent viscosity** η_app = Kγ̇^(n-1) decreases as the fluid is sheared harder — this is **shear-thinning** (or pseudoplastic) behavior. Paint is a classic example: it flows easily under the high shear of a brush stroke, then quickly becomes more viscous and stays on the wall without dripping. Blood vessels exploit shear-thinning to allow red blood cells to flow efficiently through narrow capillaries at high shear while behaving more viscously in large vessels at low shear. When n > 1, viscosity increases with shear rate — this is **shear-thickening** (or dilatant) behavior. A dense cornstarch suspension is the prototype: at low agitation it flows freely, but a sudden impact solidifies it momentarily. This is why running on a cornstarch pool works until you slow down.

A physically distinct class is the **Bingham plastic**: fluids that do not flow at all below a threshold **yield stress** τ_y, then flow as viscous fluids above it. The constitutive relation is τ = τ_y + μ_p·γ̇ for τ > τ_y, and γ̇ = 0 otherwise. Toothpaste sits on your brush rather than flowing off — it has yielded in the tube (where pressure exceeds τ_y) but sits immobile once extruded. Concrete, mayonnaise, and drilling muds are all practical Bingham plastics. Engineering pipe flow calculations for these materials require finding the **plug flow region** at the center of the pipe (where stresses are below τ_y) surrounded by yielded flowing material near the walls.

**Viscoelastic fluids** add another layer of complexity: they have both viscous dissipation and elastic energy storage. Polymer melts and solutions fall into this category. When you shear them, they both flow and deform elastically — and when the stress is removed, they partially recover. This produces striking phenomena like the **Weissenberg effect** (a polymer solution climbs a rotating rod rather than being flung outward) and **die swell** (extruded polymer expands upon leaving a nozzle because stored elastic energy relaxes). The **Deborah number** De = relaxation time / flow time scale characterizes whether elastic or viscous behavior dominates. At De ≪ 1, the fluid appears viscous; at De ≫ 1, it behaves elastically. Understanding these behaviors is essential for polymer processing, food engineering, and biological fluid mechanics — domains where assuming Newtonian behavior would give wildly incorrect predictions.
