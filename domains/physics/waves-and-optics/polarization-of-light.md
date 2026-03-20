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

## Explainer

You already know that light is a transverse electromagnetic wave — the electric and magnetic fields oscillate perpendicular to the direction the wave travels. "Perpendicular to the direction of travel" describes a whole plane, and in unpolarized light, the electric field oscillates in every direction within that plane simultaneously and randomly. Think of it as a bundle of arrows all pointing outward from the wave's travel axis, randomly changing orientation many billions of times per second. **Polarization** means restricting those oscillations to a single direction, or a predictable pattern of directions.

The simplest way to polarize light is a **polarizer** — a material (like Polaroid film) that has an aligned molecular structure that absorbs electric field components perpendicular to its **transmission axis** while letting the parallel component pass. When unpolarized light hits a polarizer, only the component of each randomly oriented electric field vector that lies along the transmission axis survives. The output is light with the electric field oscillating exclusively along one direction: linearly polarized light. Because the random incoming vectors project onto the transmission axis, on average half the intensity passes through — this is why sunglasses dim the world while eliminating glare.

Polarization by **reflection** works differently and connects to Snell's law and electromagnetic boundary conditions. When light strikes a surface at a specific angle called **Brewster's angle**, the component of the electric field oscillating in the plane of incidence (the "p-polarization") is not reflected at all — it is entirely transmitted. Only the s-polarization (electric field perpendicular to the plane of incidence) reflects. The reflected glare from water, roads, and windows is therefore partially or fully s-polarized, which is why polarizing sunglasses — with their transmission axis vertical — cut glare selectively: they absorb the horizontally oscillating, reflected s-polarization.

The most counterintuitive result in introductory polarization is the three-polarizer experiment. Two crossed polarizers (transmission axes at 90°) block all light: the second polarizer's axis is perpendicular to the first, so zero component of the polarized light from the first survives. But insert a third polarizer *between* them at 45°, and light gets through. The first polarizer produces vertically polarized light. The middle polarizer at 45° passes the component of that vertical field along its 45° axis — reducing intensity by cos²(45°) = 50%, but now the light leaving the middle polarizer is polarized at 45°. The final polarizer, originally perpendicular to the first polarizer but at 45° to the middle one, passes the cos²(45°) = 50% component of the 45°-polarized light. The three-polarizer result isn't magic; it's a reminder that polarizers don't just block light — they *reorient* the polarization state, and it is the new state that encounters the next polarizer.
