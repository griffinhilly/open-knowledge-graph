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
stage: abstract-reasoning
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

## Explainer

From your study of emission and absorption spectra, you know that atoms absorb light at specific wavelengths corresponding to electron transitions, creating dark lines in a continuous spectrum. Stellar spectral classification applies this principle at scale: by examining which absorption lines appear in a star's spectrum and how strong they are, astronomers sort stars into a sequence that turns out to be fundamentally a **temperature sequence**.

The classic spectral types — **O, B, A, F, G, K, M** — run from hottest (O stars, above 30,000 K) to coolest (M stars, below 3,500 K). The ordering is not alphabetical because the original classification, developed at Harvard in the late 19th century, sorted stars by the strength of their hydrogen absorption lines. When astronomers later realized that temperature was the controlling variable, many original letter classes were dropped or merged, leaving the familiar non-alphabetical sequence. The mnemonic "Oh Be A Fine Girl/Guy, Kiss Me" has helped generations of students remember the order.

The crucial insight is that **temperature controls which spectral lines appear**, not composition. Nearly all stars are about 75% hydrogen and 24% helium by mass, yet their spectra look wildly different. In the hottest O stars, hydrogen is mostly ionized — its electrons are stripped away — so hydrogen lines are weak, while ionized helium lines dominate. In A stars (~10,000 K), conditions are ideal for hydrogen atoms to have electrons in the n=2 energy level, producing the strongest Balmer absorption lines of any spectral type. In cooler G stars like the Sun (~5,800 K), hydrogen lines weaken because fewer atoms are excited to n=2, while lines from heavier elements like calcium and sodium strengthen because those atoms remain un-ionized. In the coolest M stars, temperatures are low enough for molecules like titanium oxide (TiO) to survive, producing broad molecular absorption bands rather than sharp atomic lines. Each spectral type is a window into the physics of excitation and ionization at a particular temperature, as described by the Boltzmann and Saha equations.

Within each letter class, a numerical subtype from 0 to 9 provides finer temperature discrimination — the Sun is classified as G2, meaning it falls near the hot end of the G class. But spectral type alone does not tell you a star's luminosity. A **luminosity class**, denoted by Roman numerals I through V, distinguishes supergiants (I) from giants (III) from main-sequence dwarfs (V). The physical basis is surface gravity and atmospheric pressure: in a supergiant's distended atmosphere, lower pressure produces narrower, sharper spectral lines, while a dwarf's compact atmosphere produces broader lines due to pressure broadening. The full classification — such as G2 V for the Sun or B8 Ia for a blue supergiant — encodes both temperature and luminosity, placing the star precisely on the Hertzsprung-Russell diagram you will encounter next.
