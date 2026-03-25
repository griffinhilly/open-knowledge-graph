---
id: malus-law
title: Malus's Law
domain: physics
course: waves-and-optics
prerequisites:
- id: polarization-of-light
  type: hard
- id: sine-cosine-tangent-ratios
  type: hard
- id: lensmakers-equation
  type: soft
tags:
- Malus's law
- intensity
- polarizer angle
- cosine squared
stage: advanced
status: validated
---
# Malus's Law

## Core Idea
When polarized light of intensity I₀ passes through a polarizer whose transmission axis makes an angle θ with the polarization direction of the incoming light, the transmitted intensity is I = I₀cos²θ. At θ = 0°, full transmission; at θ = 90°, no transmission. For initially unpolarized light passing through a single polarizer, the transmitted intensity is always I₀/2 regardless of orientation, since all directions are equally represented.

## How It's Best Learned
Use a photometer behind two polarizers; rotate the second polarizer while recording intensity. Plot I vs. θ and verify the cos²θ dependence. Extrapolate to θ = 90° to confirm complete extinction.

## Common Misconceptions
- Malus's law applies to already-polarized incident light; for unpolarized light, the first polarizer always transmits exactly half, independent of its orientation.
- Students apply cosθ instead of cos²θ because they project the electric field amplitude (cosθ) but forget that intensity ∝ E².

## Explainer

From your study of polarization, you know that polarized light has its electric field oscillating along a single axis. When such light encounters a polarizer — a filter that only transmits oscillations along one specific direction called the **transmission axis** — the question is: how much light gets through? The answer depends entirely on the angle θ between the incoming light's polarization direction and the polarizer's transmission axis.

The derivation starts with vector projection. The incoming electric field has amplitude E₀. Only the component of that field along the transmission axis can pass through: E_transmitted = E₀ cos θ. This is a direct application of the trigonometry you studied — projecting a vector onto another direction recovers a factor of cosine of the angle between them. But transmitted intensity is not proportional to amplitude — it is proportional to amplitude squared (intensity scales as the square of the field amplitude). So I_transmitted = I₀ cos²θ. This is **Malus's Law**, and the squaring step is where students most often err. A cosθ answer confuses amplitude with intensity.

The behavior of cos²θ is worth memorizing through its key values. At θ = 0° (polarizer perfectly aligned with incoming polarization), cos²0° = 1 — full transmission. At θ = 90° (polarizer perpendicular to incoming polarization), cos²90° = 0 — complete extinction, no light passes. At θ = 45°, cos²45° = 0.5 — exactly half the intensity is transmitted. Two polarizers crossed at 90° produce total darkness. Inserting a third polarizer between them at 45° and applying Malus's Law twice in sequence shows that light now passes through the combination — a counterintuitive result that follows directly from the mathematics and can be verified experimentally with three inexpensive polarizing filters.

For initially **unpolarized light**, no single polarization direction dominates; all orientations of the electric field are equally represented. Averaging cos²θ over all orientations from 0° to 360° gives exactly ½. So a single polarizer always transmits exactly I₀/2 of the incident unpolarized intensity, regardless of how you orient it — the orientation only matters for a second polarizer placed downstream, where Malus's Law then applies with the angle between the two transmission axes.

## Questions

```yaml
- question: "Polarized light of intensity 80 W/m² hits a polarizer whose transmission axis is 60° from the light's polarization direction. What is the transmitted intensity?"
  type: multiple-choice
  options:
    - "40 W/m²"
    - "20 W/m²"
    - "69 W/m²"
    - "0 W/m²"
  answer: 1
  explanation: "I = I₀ cos²θ = 80 · cos²60° = 80 · (0.5)² = 80 · 0.25 = 20 W/m². The common mistake is using cosθ: 80 · cos60° = 40 W/m². Intensity is proportional to E², not E, so the cosine must be squared."

- question: "Unpolarized light passes through two polarizers. The first is oriented vertically. The second is oriented 30° from vertical. What fraction of the original intensity exits the second polarizer?"
  type: short-answer
  answer: "The first polarizer transmits I₀/2 (unpolarized → first polarizer always halves intensity, regardless of orientation). The second polarizer transmits I₀/2 · cos²30° = I₀/2 · 0.75 = 3I₀/8. So the final intensity is 3/8 = 37.5% of the original."
  explanation: "Apply the two-step process: (1) unpolarized to first polarizer always gives I₀/2; (2) first-polarized light to second polarizer gives Malus's Law with the angle between the two transmission axes. Never apply Malus's Law to the first polarizer acting on unpolarized light."

- question: "Why does inserting a polarizer at 45° between two crossed (90°-apart) polarizers allow some light through, when the two crossed polarizers alone transmit no light?"
  type: short-answer
  answer: "The two crossed polarizers alone: light polarized by the first hits the second at 90°, giving cos²90° = 0. With a middle polarizer at 45°: light polarized by the first passes through the middle at angle 45° with intensity I₀/2 · cos²45° = I₀/4, now polarized at 45°. This light hits the final polarizer at 45° from its axis: I₀/4 · cos²45° = I₀/8. Non-zero light emerges because each step rotates the polarization axis — the middle polarizer changes the polarization state, not just the intensity."
  explanation: "This result demonstrates that polarizers are not simply passive blockers — they actively change the polarization direction of transmitted light. The middle polarizer 'rotates' the polarization axis in stages, allowing the final crossed polarizer to receive some component."
```
