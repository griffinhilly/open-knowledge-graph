---
id: polarization-of-light
title: Polarization of Light
domain: physics
course: waves-and-optics
prerequisites:
- id: electromagnetic-waves
  type: hard
- id: transverse-and-longitudinal-waves
  type: hard
- id: electromagnetic-spectrum
  type: soft
- id: polarization-production-and-analysis
  type: soft
- id: fiber-optics-and-waveguides
  type: soft
builds-toward:
- malus-law
tags:
- polarization
- polarizer
- transverse wave
- electric field
- Brewster's angle
stage: advanced
status: validated
---
# Polarization of Light

## Core Idea
Light is a transverse electromagnetic wave in which the electric field oscillates perpendicular to propagation. Unpolarized light has electric field vectors in all transverse directions equally. A polarizer transmits only the component of E along its transmission axis, producing linearly polarized light. Polarization is exclusive to transverse waves — longitudinal waves like sound cannot be polarized. Methods of polarizing light include selective absorption (Polaroid filters), reflection (at Brewster's angle), and scattering.

## How It's Best Learned
Cross two polarizing filters completely to block all light, then insert a third at 45°. The surprising reappearance of light demonstrates that polarization states add vectorially, not as simple on/off filters.

## Common Misconceptions
- Sound cannot be polarized; polarization is a uniquely transverse-wave property.
- Two crossed polarizers block light completely, but inserting a third between them at an angle actually allows some light through — this surprises students.

## Questions

```yaml
- question: "Two polarizing filters are crossed (transmission axes at 90°) so that no light passes through. A third polarizer is inserted between them with its transmission axis at 45°. What happens?"
  type: multiple-choice
  options:
    - "No change — crossed polarizers block all light regardless of anything placed between them"
    - "Even less light passes, since the third filter adds another layer of blocking"
    - "Some light passes through, because the middle filter reorients the polarization state before it reaches the final filter"
    - "All light passes through, because the 45° filter cancels the effect of the crossed filters"
  answer: 2
  explanation: "The middle polarizer does not merely block — it transmits and reorients the polarization state. The first polarizer produces vertically polarized light. The 45° middle filter passes the cos²(45°) = 50% component along its axis; the exiting light is now polarized at 45°. The final filter (at 90° to the first but 45° to the middle) passes cos²(45°) = 50% of that light — roughly 25% passes the system when none did before. Option A is the classic misconception: polarizers are not simple blockers, they create new polarization states."

- question: "A researcher claims to have produced 'polarized sound waves' by vibrating a speaker in one controlled direction. This claim is:"
  type: multiple-choice
  options:
    - "Correct — any wave can have its oscillation direction restricted"
    - "Correct only if the sound travels through a specially aligned medium"
    - "Incorrect — sound is a longitudinal wave, and polarization requires transverse oscillations"
    - "Incorrect — polarization requires an electromagnetic field, ruling out mechanical waves"
  answer: 2
  explanation: "Polarization means restricting oscillations to a specific direction within the plane perpendicular to propagation. This only makes sense for transverse waves, where oscillations are perpendicular to travel and can be oriented different ways. Sound is longitudinal — air molecules oscillate parallel to the direction of wave travel (compressions and rarefactions). There is no transverse direction to restrict, so polarization is physically meaningless for sound. Option D is also false: water waves are transverse mechanical waves and can be described with polarization."

- question: "Polarization can only occur in transverse waves, not in longitudinal waves."
  type: true-false
  answer: true
  explanation: "Polarization means restricting oscillations to a specific direction within the plane perpendicular to propagation. Only transverse waves have oscillations perpendicular to travel — and therefore a choice of orientation to restrict. Longitudinal waves (like sound) oscillate parallel to propagation, with no transverse direction available, so polarization is undefined for them."

- question: "Inserting a third polarizing filter between two crossed polarizers can only reduce the transmitted intensity, never increase it."
  type: true-false
  answer: false
  explanation: "This is wrong, and the three-polarizer experiment demonstrates it dramatically. Two crossed polarizers transmit zero light. Inserting a third at 45° between them transmits approximately 25% of the light entering the system. The middle polarizer reorients the polarization state — light exiting it is polarized at 45°, which is no longer perpendicular to the final filter's axis. The third filter increases transmitted intensity from zero to a positive value. Polarizers are not merely absorbers; they actively create new polarization states."

- question: "Why does inserting a polarizer at 45° between two crossed polarizers allow light to pass through the system, even though the crossed polarizers alone transmit nothing?"
  type: short-answer
  answer: "The first polarizer produces vertically polarized light. Two crossed polarizers block all light because the second filter's horizontal axis is perpendicular to vertical polarization — zero component survives. The middle filter at 45° projects the vertical polarization onto its 45° axis (transmitting cos²45° = 50% intensity), producing light now polarized at 45°. This 45°-polarized light then hits the final horizontal filter: 45° is not perpendicular to horizontal, so a nonzero component (cos²45° = 50%) passes. The key is that the middle polarizer does not just attenuate — it creates a new polarization state that can couple to the final filter."
  explanation: "The math: first filter → I₀ vertically polarized. Middle filter → I₀/2 at 45°. Final filter → I₀/4 (horizontal). Each step involves a genuine reorientation of the polarization state, not just absorption. This is why the sequence 'vertical → 45° → horizontal' transmits light while 'vertical → horizontal' transmits none."
```

## Explainer

You already know that light is a transverse electromagnetic wave — the electric and magnetic fields oscillate perpendicular to the direction the wave travels. "Perpendicular to the direction of travel" describes a whole plane, and in unpolarized light, the electric field oscillates in every direction within that plane simultaneously and randomly. Think of it as a bundle of arrows all pointing outward from the wave's travel axis, randomly changing orientation many billions of times per second. **Polarization** means restricting those oscillations to a single direction, or a predictable pattern of directions.

The simplest way to polarize light is a **polarizer** — a material (like Polaroid film) that has an aligned molecular structure that absorbs electric field components perpendicular to its **transmission axis** while letting the parallel component pass. When unpolarized light hits a polarizer, only the component of each randomly oriented electric field vector that lies along the transmission axis survives. The output is light with the electric field oscillating exclusively along one direction: linearly polarized light. Because the random incoming vectors project onto the transmission axis, on average half the intensity passes through — this is why sunglasses dim the world while eliminating glare.

Polarization by **reflection** works differently and connects to Snell's law and electromagnetic boundary conditions. When light strikes a surface at a specific angle called **Brewster's angle**, the component of the electric field oscillating in the plane of incidence (the "p-polarization") is not reflected at all — it is entirely transmitted. Only the s-polarization (electric field perpendicular to the plane of incidence) reflects. The reflected glare from water, roads, and windows is therefore partially or fully s-polarized, which is why polarizing sunglasses — with their transmission axis vertical — cut glare selectively: they absorb the horizontally oscillating, reflected s-polarization.

The most counterintuitive result in introductory polarization is the three-polarizer experiment. Two crossed polarizers (transmission axes at 90°) block all light: the second polarizer's axis is perpendicular to the first, so zero component of the polarized light from the first survives. But insert a third polarizer *between* them at 45°, and light gets through. The first polarizer produces vertically polarized light. The middle polarizer at 45° passes the component of that vertical field along its 45° axis — reducing intensity by cos²(45°) = 50%, but now the light leaving the middle polarizer is polarized at 45°. The final polarizer, originally perpendicular to the first polarizer but at 45° to the middle one, passes the cos²(45°) = 50% component of the 45°-polarized light. The three-polarizer result isn't magic; it's a reminder that polarizers don't just block light — they *reorient* the polarization state, and it is the new state that encounters the next polarizer.
