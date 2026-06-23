---
id: stellar-spectral-classification
title: Stellar Spectral Classification
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: emission-absorption-spectra
  type: hard
- id: stellar-properties-luminosity-temperature
  type: hard
- id: blackbody-radiation
  type: soft
- id: atomic-structure-basics
  type: soft
- id: telescopes-and-observing-methods
  type: soft
- id: photometric-magnitude-systems
  type: soft
builds-toward:
- hertzsprung-russell-diagram
- nebulae-and-star-formation
tags:
- spectral-types
- OBAFGKM
- absorption-lines
- stellar-spectra
- Harvard-classification
- luminosity-class
stage: advanced
status: validated
---
# Stellar Spectral Classification

## Core Idea
Stars are classified into spectral types O, B, A, F, G, K, M (hottest to coolest) based on the pattern of absorption lines in their spectra. Each spectral type reflects which ions and molecules are stable at that photospheric temperature: O stars show ionized helium; A stars show strong hydrogen lines; G stars (like the Sun) show calcium and sodium; M stars show molecular TiO bands. The sequence is fundamentally a temperature sequence — most stars have similar hydrogen-dominated compositions. Luminosity classes (I–V) further distinguish supergiants from main-sequence dwarfs at the same spectral type.

## How It's Best Learned
Examine spectra of stars across the spectral sequence and identify characteristic absorption features for each type. Understand why the OBAFGKM order is not alphabetical — it was originally sorted by hydrogen line strength, then reorganized by temperature.

## Common Misconceptions
- Spectral type is not a direct indicator of composition; most stars are about 75% hydrogen regardless of their spectral class.
- Two stars of the same spectral type can have very different luminosities — a G2 supergiant and a G2 dwarf look similar in color but differ in size and brightness by many orders of magnitude.

## Questions

```yaml
- question: "An A-type star shows very strong hydrogen Balmer absorption lines, while an M-type star of similar mass shows almost none — instead displaying broad TiO molecular bands. What is the most accurate explanation?"
  type: multiple-choice
  options:
    - "The A star is far richer in hydrogen than the M star, whose hydrogen has been converted to helium over its lifetime"
    - "Both stars are about 75% hydrogen, but at different temperatures different quantum states are populated: the A star's ~10,000 K photosphere excites hydrogen to n=2 (enabling Balmer absorption), while the M star's ~3,000 K photosphere leaves hydrogen in the ground state and allows TiO molecules to survive"
    - "The M star's stronger gravity suppresses hydrogen line formation and allows heavy molecules to dominate"
    - "A stars have active hydrogen fusion in their photospheres, producing emission that appears as strong absorption in cooler surrounding gas"
  answer: 1
  explanation: "Both stars are approximately 75% hydrogen — composition is not the variable. At ~10,000 K (A stars), conditions are ideal for hydrogen atoms to have electrons in the n=2 state, producing the strongest Balmer absorption of any spectral type. In M stars (~2,500–3,500 K), thermal excitation cannot populate n=2 significantly, so hydrogen lines are weak; at the same time, temperatures are cool enough that TiO molecules survive without thermally dissociating. Spectral differences reflect temperature-driven excitation and ionization physics, not composition."

- question: "Two G5-type stars have identical color and temperature, but one shows broad, smeared spectral lines while the other shows narrow, sharp lines. The narrow-line star is most likely which of the following?"
  type: multiple-choice
  options:
    - "A white dwarf — extreme gravity compresses the atmosphere and sharpens transitions"
    - "A main-sequence dwarf — its compact, high-pressure atmosphere produces pressure broadening of spectral lines"
    - "A supergiant — its extended, low-density atmosphere has infrequent particle collisions, producing narrow lines"
    - "A neutron star — quantum confinement effects sharpen the spectral features at high density"
  answer: 2
  explanation: "Luminosity class is physically rooted in surface gravity and atmospheric pressure. Supergiants have extended, low-density atmospheres where atoms collide rarely — producing narrow, sharp lines. Main-sequence dwarfs have compact, high-pressure atmospheres where frequent collisions broaden energy levels through pressure (collisional) broadening, smearing spectral lines. This is why luminosity class can be read directly from line widths: a same-temperature comparison reveals whether a star is a supergiant (Roman numeral I) or a dwarf (V) purely from spectral appearance."

- question: "The OBAFGKM spectral sequence is fundamentally a temperature sequence; two stars at opposite ends of the sequence can have nearly identical chemical compositions yet produce completely different spectra."
  type: true-false
  answer: true
  explanation: "Nearly all main-sequence stars are approximately 75% hydrogen and 24% helium by mass, with trace amounts of heavier elements. Yet O stars (>30,000 K) and M stars (<3,500 K) look completely different — one dominated by ionized helium lines, the other by molecular absorption bands. The vastly different temperatures drive different ionization and excitation states, changing which spectral lines are observable even though the underlying composition is nearly identical."

- question: "O-type stars show weaker hydrogen absorption lines than A-type stars because O stars have converted more of their hydrogen to helium through nuclear fusion."
  type: true-false
  answer: false
  explanation: "O stars are still approximately 75% hydrogen — the weak Balmer lines reflect temperature physics, not depletion. At temperatures above 30,000 K, nearly all hydrogen is ionized (H+, proton), and ionized hydrogen has no electrons to produce absorption lines. Balmer lines require hydrogen atoms with electrons in the n=2 state, which is maximized around 10,000 K (A stars). Hotter O stars have too much ionization; cooler stars below ~6,000 K have insufficient thermal excitation of n=2. The weak lines in O stars are about ionization state, not hydrogen abundance."

- question: "A classmate says 'M stars show TiO absorption bands because they have a higher abundance of titanium than other stars.' Explain why this interpretation is wrong and what actually controls TiO band appearance."
  type: short-answer
  answer: "The appearance of TiO bands reflects temperature, not an unusual titanium abundance. TiO is a molecule, and molecules dissociate at high temperatures — in hotter stellar photospheres, the thermal energy is sufficient to break TiO apart into atomic Ti and O. Only in the cool photospheres of M stars (~2,500–3,500 K) is the temperature low enough for TiO molecules to survive intact and produce their characteristic broad absorption bands. The same titanium atoms are present across all spectral types but appear in different forms (atomic Ti+ lines in hotter stars, molecular TiO bands in cool ones) depending purely on photospheric temperature. Spectral line pattern is a temperature diagnostic, not a composition diagnostic."
  explanation: "This is the central insight of the Harvard spectral classification system: nearly all stars have similar compositions, and the dramatic variation in their spectra is explained almost entirely by temperature differences that shift the populations of different atomic and molecular quantum states — exactly as described by the Boltzmann distribution and Saha ionization equation."
```

## Explainer

From your study of emission and absorption spectra, you know that atoms absorb light at specific wavelengths corresponding to electron transitions, creating dark lines in a continuous spectrum. Stellar spectral classification applies this principle at scale: by examining which absorption lines appear in a star's spectrum and how strong they are, astronomers sort stars into a sequence that turns out to be fundamentally a **temperature sequence**.

The classic spectral types — **O, B, A, F, G, K, M** — run from hottest (O stars, above 30,000 K) to coolest (M stars, below 3,500 K). The ordering is not alphabetical because the original classification, developed at Harvard in the late 19th century, sorted stars by the strength of their hydrogen absorption lines. When astronomers later realized that temperature was the controlling variable, many original letter classes were dropped or merged, leaving the familiar non-alphabetical sequence. The mnemonic "Oh Be A Fine Girl/Guy, Kiss Me" has helped generations of students remember the order.

The crucial insight is that **temperature controls which spectral lines appear**, not composition. Nearly all stars are about 75% hydrogen and 24% helium by mass, yet their spectra look wildly different. In the hottest O stars, hydrogen is mostly ionized — its electrons are stripped away — so hydrogen lines are weak, while ionized helium lines dominate. In A stars (~10,000 K), conditions are ideal for hydrogen atoms to have electrons in the n=2 energy level, producing the strongest Balmer absorption lines of any spectral type. In cooler G stars like the Sun (~5,800 K), hydrogen lines weaken because fewer atoms are excited to n=2, while lines from heavier elements like calcium and sodium strengthen because those atoms remain un-ionized. In the coolest M stars, temperatures are low enough for molecules like titanium oxide (TiO) to survive, producing broad molecular absorption bands rather than sharp atomic lines. Each spectral type is a window into the physics of excitation and ionization at a particular temperature, as described by the Boltzmann and Saha equations.

Within each letter class, a numerical subtype from 0 to 9 provides finer temperature discrimination — the Sun is classified as G2, meaning it falls near the hot end of the G class. But spectral type alone does not tell you a star's luminosity. A **luminosity class**, denoted by Roman numerals I through V, distinguishes supergiants (I) from giants (III) from main-sequence dwarfs (V). The physical basis is surface gravity and atmospheric pressure: in a supergiant's distended atmosphere, lower pressure produces narrower, sharper spectral lines, while a dwarf's compact atmosphere produces broader lines due to pressure broadening. The full classification — such as G2 V for the Sun or B8 Ia for a blue supergiant — encodes both temperature and luminosity, placing the star precisely on the Hertzsprung-Russell diagram you will encounter next.
