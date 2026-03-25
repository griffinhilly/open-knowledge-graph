---
id: supernova-type-ii-core-collapse
title: 'Type II Supernovae: Core-Collapse Explosions of Massive Stars'
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: neutron-star-formation-collapse
  type: hard
- id: stellar-nucleosynthesis
  type: soft
- id: nuclear-chemistry
  type: soft
- id: energy-conservation-applications
  type: soft
builds-toward:
- gamma-ray-burst-jet-physics
tags:
- supernova
- type-ii
- core-collapse
- massive-stars
stage: advanced
status: validated
---

# Type II Supernovae: Core-Collapse Explosions of Massive Stars

## Core Idea
Type II supernovae occur when the iron core of a massive star (>8 solar masses) collapses, rebounds off nuclear density, and generates a shockwave that blasts the star apart. The energy released comes from gravitational binding energy of the core, not thermonuclear burning, and these explosions distribute heavy elements throughout the galaxy, enriching future generations of stars.

## Questions

```yaml
- question: "A student claims: 'Type II supernovae are powered by the explosive thermonuclear burning of the iron core — iron fuses into heavier elements, releasing enormous energy.' What is fundamentally wrong with this explanation?"
  type: multiple-choice
  options:
    - "Iron does undergo thermonuclear burning, but the energy goes into neutrinos rather than the shockwave"
    - "Iron cannot release energy through either fusion or fission — it sits at the peak of the binding energy curve. The explosion energy comes from gravitational collapse, not nuclear burning"
    - "Iron does fission into lighter elements, but the energy is too small to power the explosion"
    - "The thermonuclear burning happens in the outer shell, not the core — the core is too cool"
  answer: 1
  explanation: "This is the central misconception about Type II supernovae. Iron-56 has the highest binding energy per nucleon of any nucleus — fusing or fissioning it requires energy input rather than releasing energy. The star builds up an iron core that is a nuclear dead end. The explosion energy (about 3×10⁴⁶ joules) comes entirely from the gravitational binding energy released as the core collapses from Earth-size to neutron-star size (~10 km radius). Nuclear reactions actually *steal* energy during collapse (photodisintegration absorbs energy shattering iron), making the collapse faster rather than powering the explosion."

- question: "The initial shockwave generated when the collapsing core bounces off nuclear density is sufficient on its own to unbind the stellar envelope and produce the supernova."
  type: multiple-choice
  options:
    - "True — the bounce shockwave carries more than enough energy to eject the envelope"
    - "False — the shock stalls within milliseconds because it loses energy photodisintegrating infalling iron; neutrino energy deposition is needed to revive it"
    - "False — the shock is absorbed by the neutron star's magnetic field before reaching the envelope"
    - "True — but only for stars below 15 solar masses; more massive stars require additional energy"
  answer: 1
  explanation: "The 'stalled shock' problem is one of the central unsolved puzzles of supernova theory. The bounce shockwave loses roughly 10⁴⁴ joules per solar mass of iron it must photodisintegrate as it fights its way outward through infalling material. The shock stalls within tens to hundreds of milliseconds. The leading mechanism for shock revival is neutrino heating: about 5% of the neutrino flux (itself carrying ~99% of the total energy) deposits enough energy behind the shock to revive it. Without this neutrino-driven mechanism, purely hydrodynamic models of core collapse do not produce successful explosions."

- question: "Approximately 99% of the energy released in a core-collapse supernova escapes as neutrinos, not as the visible explosion or light."
  type: true-false
  answer: true
  explanation: "The gravitational binding energy released (≈3×10⁴⁶ J) is partitioned very unevenly: roughly 99% is carried away by neutrinos that pass through the collapsing matter almost unimpeded, about 1% goes into the kinetic energy of the explosion (the actual blast that unbinds the star), and a tiny fraction (~0.01%) goes into electromagnetic radiation (the visible supernova light). Neutrino detection from SN 1987A — 19 neutrinos detected in two underground detectors from a supernova in the Large Magellanic Cloud — provided direct observational confirmation of this energy partition."

- question: "The iron core collapses because iron releases less energy per fusion reaction than lighter elements, causing the star's energy output to drop gradually until gravity wins."
  type: true-false
  answer: false
  explanation: "The collapse is not gradual — it is catastrophic and nearly instantaneous. The problem is not that iron fusion releases *less* energy, but that it releases *no* energy at all (it requires energy input). Once the iron core exceeds the Chandrasekhar mass, electron degeneracy pressure cannot support it. Two processes then *accelerate* the collapse: photodisintegration (photons shatter iron back into nucleons, absorbing energy) and electron capture (protons capture electrons to become neutrons, removing the particles providing degeneracy pressure). The result is a freefall implosion at ~25% of the speed of light that completes in under a second."

- question: "Why is iron the 'end of the line' for stellar nuclear burning, and how does this directly cause the core-collapse supernova?"
  type: short-answer
  answer: "Iron-56 has the highest binding energy per nucleon of any nucleus, meaning it is the most tightly bound configuration. Fusing iron requires energy rather than releasing it, so the star cannot extract energy from an iron core to support itself against gravity. Once the iron core grows beyond the Chandrasekhar mass (~1.4 solar masses), electron degeneracy pressure fails, and the core collapses in under a second. The collapse releases gravitational binding energy, which — primarily through neutrino heating of the stalled shockwave — ultimately powers the explosion that destroys the star."
  explanation: "The binding energy curve is the key link: every element lighter than iron releases energy when fused (moving up the curve toward iron), but iron itself cannot. The star's entire life is a sequence of energy-releasing fusion steps, each faster than the last, each producing a new ash that must then be fused. When silicon burning produces iron, the chain terminates abruptly. The star has no mechanism to prevent gravitational collapse and the rapid conversion of gravitational potential energy to the neutrinos and blast that define a Type II supernova."
```

## Explainer

A massive star spends most of its life fusing progressively heavier elements in its core — hydrogen to helium, helium to carbon, carbon to neon, neon to oxygen, oxygen to silicon — each stage burning faster than the last. From your study of stellar nucleosynthesis, you know that each successive fuel yields less energy per reaction. The final stage, silicon burning, produces **iron-group elements** in the core and lasts only about a day. Iron is the end of the line: its nuclear binding energy per nucleon is the highest of any element, so neither fission nor fusion of iron releases energy. The star has built an iron core that is essentially an inert dead end, supported only by electron degeneracy pressure.

The catastrophe begins when the iron core exceeds the **Chandrasekhar mass** (roughly 1.4 solar masses). At this point, electron degeneracy pressure can no longer support the core against gravity. Two processes accelerate the collapse: photodisintegration, where extreme temperatures (~10 billion K) cause photons to shatter iron nuclei back into protons and neutrons, absorbing energy rather than releasing it; and electron capture, where protons absorb electrons to become neutrons, removing the very particles providing degeneracy pressure. The core collapses at roughly a quarter of the speed of light, falling inward in less than a second — a freefall implosion of material that moments before was a structure the size of Earth.

The collapse halts abruptly when the core reaches **nuclear density** — about 2 × 10¹⁴ grams per cubic centimeter — and the strong nuclear force between neutrons stiffens the material into an incompressible neutron-rich object. The infalling material slams into this suddenly rigid core and **bounces**, generating an outward-moving shock wave. However, the shock alone is not enough to unbind the star: it loses energy by photodisintegrating the iron still raining down from above. This is the central puzzle of core-collapse supernova theory. The leading explanation is that neutrinos — produced in enormous quantities during neutronization of the core — deposit a small fraction of their energy (roughly 5%) into the material behind the stalled shock, reviving it over tens to hundreds of milliseconds. The energy budget is staggering: the collapsing core releases about 3 × 10⁴⁶ joules of gravitational binding energy, 99% of which escapes as neutrinos. Only about 1% goes into the kinetic energy of the explosion, and a tiny fraction into the visible light that makes the supernova shine.

The explosion blasts the star's outer layers into space at thousands of kilometers per second, creating an expanding **supernova remnant** that sweeps up interstellar gas and can be visible for tens of thousands of years. These ejecta carry with them all the elements forged during the star's life and during the explosion itself — including elements heavier than iron produced by rapid neutron capture (the r-process) in the extreme conditions of the explosion. Type II supernovae are distinguished observationally by the presence of hydrogen lines in their spectra, confirming that the progenitor retained its hydrogen envelope at the time of explosion. Every atom of oxygen you breathe, every grain of iron in Earth's core, was manufactured in a massive star and distributed by a core-collapse supernova billions of years ago. These explosions are not merely spectacular endpoints — they are the foundational events of cosmic chemical enrichment.
