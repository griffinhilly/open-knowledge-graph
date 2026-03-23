---
id: malus-law-derivation
title: 'Malus''s Law: Derivation and Applications'
domain: physics
course: waves-and-optics
prerequisites:
- id: malus-law
  type: soft
- id: polarization-linear-production
  type: hard
builds-toward:
- wave-plates-quarter-half-wave
tags:
- malus-law
- polarization
- intensity-transmission
stage: advanced
status: validated
---

# Malus's Law: Derivation and Applications

## Core Idea
Malus's law states that linearly polarized light of intensity I₀ transmitted through a polarizer oriented at angle θ to the polarization direction has transmitted intensity I = I₀cos²θ. This relationship arises from the component of the electric field parallel to the polarizer's transmission axis.

## Questions

```yaml
- question: "Two polarizers are crossed (their transmission axes are 90° apart) and block all incident light. A third polarizer is inserted between them at 45° to the first. What fraction of the original intensity emerges after all three?"
  type: multiple-choice
  options:
    - "Zero — crossed polarizers block all light regardless of what is inserted between them"
    - "1/√2 — since cos(45°) = 1/√2 and only one projection step occurs"
    - "1/2 — only the final polarizer reduces the intensity"
    - "1/4 — applying Malus's law twice: I₀ → I₀cos²(45°) = I₀/2, then I₀/2 → (I₀/2)cos²(45°) = I₀/4"
  answer: 3
  explanation: "Apply Malus's law at each polarizer. After the first polarizer, the light is polarized along 0°. The intermediate polarizer at 45° transmits I₁ = I₀cos²(45°) = I₀/2, and the polarization direction is now 45°. The final polarizer is at 90°, so the angle between incoming polarization (45°) and the final axis (90°) is 45°. It transmits I₂ = I₁cos²(45°) = (I₀/2)(1/2) = I₀/4. The key insight is that the intermediate polarizer rotates the polarization direction, creating a nonzero component along the final axis — something impossible if you think of polarizers as pure absorption filters."

- question: "Malus's law gives I = I₀cos²θ. If intensity were directly proportional to electric field amplitude rather than amplitude squared, what would the transmitted intensity relationship look like?"
  type: multiple-choice
  options:
    - "I = I₀cos²θ — no change, since the cosine projection already accounts for this"
    - "I = I₀cosθ — intensity would follow the projected amplitude directly"
    - "I = I₀sin²θ — the perpendicular component would be transmitted instead"
    - "I = I₀/cos²θ — intensity would increase at larger angles to compensate"
  answer: 1
  explanation: "The derivation has two steps: (1) project the electric field amplitude onto the transmission axis, giving E_t = E₀cosθ; (2) square to get intensity, giving I ∝ E_t² = E₀²cos²θ. If intensity were proportional to amplitude instead of amplitude squared, only step 1 would contribute and the transmitted intensity would be I₀cosθ — a linear function of cosθ, not a quadratic one. The cos²θ (rather than cosθ) dependence is entirely due to the I ∝ E² relationship, which is fundamental to wave energy."

- question: "According to Malus's law, at θ = 90° (crossed polarizers), the transmitted intensity is zero because the electric field is completely absorbed by the polarizer material."
  type: true-false
  answer: false
  explanation: "The zero transmission at θ = 90° follows from cos²(90°) = 0, which means the component of the electric field parallel to the transmission axis is exactly zero — there is no projection along the allowed direction, so nothing passes through. It is not that the field is absorbed per se; it is that the field has no component in the direction that the polarizer transmits. The mechanism is vector projection (only the component along the transmission axis passes), not selective absorption of a particular amount."

- question: "When polarized light at 45° strikes a polarizer, exactly half the original intensity is transmitted."
  type: true-false
  answer: true
  explanation: "By Malus's law: I = I₀cos²(45°) = I₀ × (1/√2)² = I₀ × 1/2 = I₀/2. This result is also memorable as a check: at 0°, full transmission; at 90°, zero; at 45° (halfway between), exactly half. This is only exact because intensity goes as cos² rather than as cos (which would give I₀/√2 ≈ 0.707I₀ at 45°). The cos² dependence ensures the 45° case is a clean half."

- question: "In the three-polarizer demonstration, why does inserting a polarizer at 45° between two crossed polarizers allow light through, when the crossed polarizers alone transmit nothing? What must you track to explain this correctly?"
  type: short-answer
  answer: "You must track the electric field vector, not just the intensity. Two crossed polarizers transmit nothing because the first polarizer establishes a polarization direction (say 0°) and the second (at 90°) has zero component along 0°. When the intermediate polarizer at 45° is inserted, it projects the 0°-polarized light onto the 45° axis, transmitting half the intensity — but critically, the transmitted light is now polarized at 45°. The final polarizer (at 90°) now sees light polarized at 45°, which has a nonzero projection (cos²45° = 1/2) along 90°. The intermediate polarizer effectively rotates the polarization direction in a step, creating a path from 0° to 90° via 45°."
  explanation: "If you think of polarizers as filters that simply 'block a fraction of photons' without changing the polarization direction, the three-polarizer result is mysterious. The explanation requires understanding that each polarizer resets the polarization direction to its own transmission axis — the output is always polarized along the polarizer's axis, regardless of the input polarization direction. Malus's law gives the intensity cost of each step; the rotation of polarization direction is the key mechanism that allows a second step to occur at all."
```

## Explainer

The derivation of Malus's law connects two things you already know: the geometry of linearly polarized light and the fact that intensity is proportional to the square of the electric field amplitude. From your study of linear polarization, you know that the electric field oscillates in a single plane, and you can describe its direction as a vector. A polarizer transmits only the component of the electric field aligned with its **transmission axis** — everything perpendicular to that axis is blocked.

When linearly polarized light with electric field amplitude E₀ strikes a polarizer whose transmission axis makes an angle θ with the polarization direction, only the parallel component passes. That component has amplitude E₀ cos θ — this is straightforward vector projection, the same operation you use to find the component of any vector along a chosen axis. The perpendicular component E₀ sin θ is absorbed or reflected by the polarizer material. The transmitted electric field amplitude is therefore E_t = E₀ cos θ.

Now apply the intensity relationship: intensity is proportional to the square of the field amplitude, I ∝ E². The incident intensity is I₀ ∝ E₀², and the transmitted intensity is I ∝ (E₀ cos θ)² = E₀² cos²θ. Therefore I = I₀ cos²θ. The derivation has exactly two steps: project the field amplitude (cosine), then square for intensity (cosine squared). The cos²θ factor is the complete explanation of why intensity drops to zero at 90° rather than at some other angle — it follows entirely from the vector nature of the electric field.

Several results follow immediately. At θ = 0°, I = I₀ (all transmitted). At θ = 90°, I = 0 (crossed polarizers block all light). At θ = 45°, I = I₀/2 (half transmitted). A striking application is the three-polarizer demonstration: two crossed polarizers block all light, but inserting a third polarizer between them at 45° allows some light through. Applying Malus's law twice — first to the 0°→45° transition (I₁ = I₀/2), then to the 45°→90° transition (I₂ = I₁/2 = I₀/4) — gives the correct result. The intermediate polarizer rotates the polarization state, creating a non-zero component along the final axis. This result is impossible if you think of polarization as simply filtering out some light; it only makes sense when you track the electric field vector through each interaction.
