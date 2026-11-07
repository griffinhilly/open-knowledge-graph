---
id: michelson-interferometer
title: The Michelson Interferometer
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-interference
  type: hard
- id: path-difference-phase-difference
  type: soft
- id: optical-path-length-definition
  type: soft
- id: reflection-law
  type: soft
builds-toward:
- special-relativity-postulates
- gravitational-waves
tags:
- interference
- interferometry
- precision-measurement
- optics
stage: formal-systems
status: validated
---

# The Michelson Interferometer

## Core Idea
A Michelson interferometer splits one light beam into two with a partially silvered mirror, sends them down perpendicular arms to mirrors, and recombines them. The bright and dark fringes that appear depend on the difference in round-trip path length between the arms. Moving one mirror by half a wavelength changes that difference by a full wavelength and shifts the pattern by one fringe. This makes the instrument a ruler that measures length changes in units of the wavelength of light.

## How It's Best Learned
Trace the two paths on a diagram and write the round-trip path difference as 2(d₁ − d₂). Then count fringes as a mirror moves, either on a lab interferometer or in a simulation. Use the count to measure a laser's wavelength, then insert a gas cell to measure a refractive index. Finish with the Michelson-Morley experiment and with LIGO as two famous uses of the same layout.

## Common Misconceptions
- Moving a mirror by one wavelength shifts the pattern by one fringe. (The light travels the arm twice, so a mirror shift of λ/2 changes the path difference by λ and produces one fringe.)
- The interferometer measures the absolute length of each arm. (It measures changes in the difference between the two optical paths, not either length on its own.)
- The Michelson-Morley experiment found that light slows down when moving against the "ether wind." (It found no difference in light's speed along different directions, which is the famous null result.)

## Questions

```yaml
- question: "In a Michelson interferometer lit by a 633 nm laser, one mirror is moved 0.100 mm. About how many fringes pass a fixed point?"
  type: multiple-choice
  options: ["About 158", "About 316", "About 632", "About 1580"]
  answer: 1
  explanation: "Each fringe corresponds to a mirror shift of λ/2. N = 2Δd/λ = 2 × 1.00 × 10⁻⁴ m / 6.33 × 10⁻⁷ m ≈ 316."
- question: "Moving one mirror of a Michelson interferometer by half a wavelength shifts the fringe pattern by exactly one fringe."
  type: true-false
  answer: true
  explanation: "The beam goes to the mirror and back, so a shift of λ/2 changes the round-trip path by λ, which restores the same interference condition one order over."
- question: "What did Michelson and Morley set out to detect in 1887?"
  type: multiple-choice
  options: ["The wavelength of sodium light", "Earth's motion through a supposed light-carrying ether", "The speed of light in water", "Gravitational waves"]
  answer: 1
  explanation: "They expected the time for light to travel along and across Earth's direction of motion through the ether to differ. They saw no such shift, a result later explained by special relativity."
- question: "An empty gas cell of length L sits in one arm. As gas is let in, N fringes pass. Write the refractive index n of the gas in terms of N, L, and the vacuum wavelength λ."
  type: short-answer
  answer: "n = 1 + Nλ/(2L)"
  explanation: "The cell is crossed twice, so the optical path changes by 2L(n − 1). Each fringe is one wavelength of change: 2L(n − 1) = Nλ."
```

## Explainer
Albert Michelson designed his interferometer in the 1880s. Light from a source meets a beam splitter, a glass plate with a thin partly reflecting coating. Half the light reflects into one arm and half passes into the other arm, at right angles. Each beam reflects from a mirror at the end of its arm and returns to the beam splitter. There the two beams recombine and travel together to a screen or detector.

The two beams came from the same source, so they can interfere. If the mirrors sit at distances d₁ and d₂ from the beam splitter, the round-trip path difference is 2(d₁ − d₂). When this difference is a whole number of wavelengths, the beams arrive in step and the centre of the pattern is bright. When it is an odd number of half-wavelengths, they cancel and the centre is dark. In practice the pattern is a set of rings or straight fringes, because rays at slightly different angles travel slightly different paths. A second glass plate, called a compensator, is often placed in one arm so that both beams pass through the same thickness of glass.

Move one mirror slowly and the fringes march across the field of view. Each fringe that passes means the mirror moved λ/2. Counting N fringes gives the mirror's displacement, Δd = Nλ/2. Turned around, a known displacement gives the wavelength. Michelson used this idea to compare the metre with wavelengths of light, work that formed part of his 1907 Nobel Prize. A gas cell in one arm changes the optical path as it fills, which gives the gas's refractive index from the fringe count.

The most famous use came in 1887. Michelson and Edward Morley mounted an interferometer on a stone slab floating in mercury so they could rotate it smoothly. If light travelled through a fixed ether, the round-trip times along and across Earth's motion should differ, and rotating the apparatus should shift the fringes. They saw far less shift than predicted, consistent with none at all. This null result became one of the observations that special relativity explains.

The same layout, greatly enlarged, now detects gravitational waves. Each LIGO detector has arms 4 km long, with the light bounced back and forth many times in each arm. A passing wave stretches one arm and squeezes the other by a fraction near 10⁻²¹, and the interference signal at the output reveals that tiny change.
