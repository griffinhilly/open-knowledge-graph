---
id: stellar-spectra-and-classification-scheme
title: Stellar Spectra and Spectral Classification
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: inverse-square-law-stellar-radiation
  type: soft
builds-toward:
- stellar-effective-temperature-color
- extinction-and-interstellar-reddening
tags:
- spectroscopy
- classification
- stellar-properties
stage: formal-systems
status: draft
---

# Stellar Spectra and Spectral Classification

## Core Idea
Stellar spectra display absorption lines that reflect composition and physical conditions in stellar atmospheres. The Harvard spectral classification sequence (OBAFGKM, from hottest to coolest) organizes stars by effective temperature, with spectral type determined from line strength patterns: hydrogen Balmer lines, ionized calcium lines, and metal lines. Spectroscopy provides detailed physical diagnostics of stellar atmospheres complementing other classification methods.

## How It's Best Learned
Study actual stellar spectra at different wavelengths. Identify key diagnostic lines and understand how line strength correlates with temperature and gravity. Use modern spectral databases to explore the diversity of real stellar spectra.

## Common Misconceptions
Spectral type does not uniquely determine luminosity; luminosity is determined by temperature and surface area separately. Spectral lines arise from absorption in the photosphere, not from the bulk composition of the star. Metal lines used in spectral classification refer to all elements heavier than helium, not just iron.

## Questions

```yaml
- question: "Two stars have nearly identical hydrogen abundances. One is an A-type star; the other is an M-type star. An astronomer finds that the A-type star shows far stronger hydrogen Balmer absorption lines. The best explanation is:"
  type: multiple-choice
  options:
    - "A-type stars contain more hydrogen than M-type stars"
    - "A-type stars are hotter, and their temperature happens to ionize hydrogen completely, producing more lines"
    - "A-type temperatures (~10,000 K) maximize the fraction of hydrogen atoms in the first excited state needed for Balmer transitions; M-type temperatures leave hydrogen mostly in the ground state"
    - "M-type stars are too dim to show strong absorption lines regardless of composition"
  answer: 2
  explanation: "Balmer lines arise from transitions starting at the second energy level (first excited state). At M-type temperatures (~3,000 K), nearly all hydrogen is in the ground state and cannot produce Balmer absorption. At A-type temperatures (~10,000 K), the thermal equilibrium population of the first excited state is maximized. At O-type temperatures (~50,000 K), hydrogen is mostly ionized and has no electrons to transition. Line strength reflects the atmospheric temperature conditions that govern excitation and ionization, not the abundance of the element."

- question: "A student claims the Harvard spectral sequence (OBAFGKM) orders stars by hydrogen content, from hydrogen-rich O-type to hydrogen-poor M-type, since O-stars show helium lines and M-stars show molecule bands. The correct interpretation is:"
  type: multiple-choice
  options:
    - "The student is correct — the sequence does track hydrogen abundance"
    - "The sequence orders stars primarily by temperature, and the changing line patterns reflect different ionization and excitation states at different temperatures — not different elemental abundances"
    - "The sequence orders stars by luminosity, not temperature"
    - "The student is partially correct — hydrogen abundance decreases along the sequence but temperature is also a factor"
  answer: 1
  explanation: "The Harvard sequence is a temperature sequence. Nearly all stars have similar compositions — mostly hydrogen and helium. The dramatic changes in spectral appearance (helium lines in O/B, hydrogen lines peaking in A, metal lines in G/K, molecular bands in M) reflect the changing ionization and excitation states as temperature varies, not different abundances. At 50,000 K, helium can be ionized — its lines appear. At 3,000 K, molecules can survive. Same abundances, different temperatures, completely different spectra."

- question: "A star's spectral type (e.g., G2) tells you everything you need to know to determine its luminosity."
  type: true-false
  answer: false
  explanation: "Spectral type (temperature class) and luminosity are separate properties. Two G2 stars can differ enormously in luminosity if one is a main-sequence dwarf and the other is a giant or supergiant — the same temperature but very different surface areas. Luminosity classification (I–V in the MKK system) provides the second dimension, encoded in the width and shape of spectral lines, which reflect surface gravity and atmospheric density. The full two-dimensional designation (e.g., G2V for the Sun) is needed to constrain luminosity."

- question: "Stellar spectral lines are absorption features, meaning they appear as dark gaps in the continuous spectrum where atmospheric atoms have absorbed photons at specific wavelengths."
  type: true-false
  answer: true
  explanation: "Absorption lines form when atoms in the stellar atmosphere (photosphere) absorb photons at the precise energies needed to excite their electrons to higher energy levels. These absorbed wavelengths are missing from the transmitted light, appearing as dark lines against the continuous rainbow. Each element has a unique pattern of line positions (its spectral fingerprint), which is how composition is identified. The strength of those lines depends on how many atoms are in the right ionization and excitation state to do the absorbing — which depends on temperature."

- question: "Explain why hydrogen Balmer absorption lines are strongest in A-type stars (~10,000 K) rather than in the hottest O-type stars, where hydrogen is equally abundant."
  type: short-answer
  answer: "Balmer lines require hydrogen atoms in the first excited state (second energy level). In O-type stars (~50,000 K), the temperature is high enough to ionize most hydrogen completely — stripped of electrons, ionized hydrogen cannot produce absorption lines. In M-type stars (~3,000 K), hydrogen atoms are almost entirely in the ground state and cannot produce Balmer transitions. At A-type temperatures (~10,000 K), the thermal equilibrium population of hydrogen in the first excited state is maximized. This illustrates that spectral line strength is determined by temperature-dependent physics, not by how much of an element is present."
  explanation: "This is the central lesson of spectral classification: the same element produces different absorption patterns at different temperatures because ionization and excitation states change. Spectral type is a temperature diagnostic, not a composition diagnostic. Every step along the OBAFGKM sequence represents a different thermal regime with different ionization equilibria — and that's what makes the sequence informative about stellar physics."
```

## Explainer

From the inverse-square law, you know that a star's apparent brightness decreases with the square of its distance, and that we can recover its intrinsic luminosity if we know how far away it is. But brightness alone tells us very little about what a star actually *is*. To learn a star's temperature, composition, and physical conditions, we need to spread its light into a **spectrum** — a rainbow of wavelengths — and read the patterns encoded in it.

When you disperse starlight through a prism or diffraction grating, you see a continuous rainbow crossed by dark **absorption lines** at specific wavelengths. These lines form because atoms in the star's outer atmosphere (the **photosphere**) absorb photons at the precise energies needed to excite their electrons to higher energy levels. Each chemical element produces a unique fingerprint of lines, so the pattern of absorption immediately reveals which elements are present. But the real power of stellar spectroscopy is that the *strength* of these lines depends not just on which elements exist, but on the temperature and pressure of the gas. Hydrogen is the most abundant element in virtually every star, yet hydrogen absorption lines (the **Balmer series**) are strongest in medium-temperature stars (~10,000 K) and weaker in both hotter and cooler stars — because the lines require hydrogen atoms with electrons already in the first excited state, and the population of those atoms peaks at intermediate temperatures.

This temperature dependence is the foundation of the **Harvard spectral classification**: O, B, A, F, G, K, M — from hottest (~50,000 K) to coolest (~3,000 K). The famous mnemonic "Oh Be A Fine Girl/Guy, Kiss Me" helps remember the sequence. **O-type** stars are blue-white and show lines of highly ionized helium and multiply ionized metals — only extreme temperatures can strip electrons from these atoms. **A-type** stars show the strongest hydrogen Balmer lines. **G-type** stars like our Sun display prominent ionized calcium (Ca II) lines and numerous metal lines, because at ~5,800 K, metals retain enough electrons to produce abundant absorption features. **M-type** stars are cool enough for molecules like titanium oxide (TiO) to survive in their atmospheres, producing broad absorption bands that dominate the spectrum.

Each spectral type is further divided into subtypes 0–9 (e.g., G2 for the Sun, where lower numbers are hotter within the class). Beyond temperature, the width and shape of spectral lines also encode information about **surface gravity** and therefore luminosity class. Giant and supergiant stars have more extended, lower-density atmospheres, producing narrower spectral lines than compact dwarf stars of the same temperature. This led to the **MKK luminosity classification** (I through V), which, combined with spectral type, gives a two-dimensional classification — for example, the Sun is a G2V star (G2 spectral type, luminosity class V for main-sequence dwarf). Together, spectral type and luminosity class allow astronomers to estimate a star's temperature, luminosity, radius, and evolutionary state from its light alone — without ever needing to visit it.
