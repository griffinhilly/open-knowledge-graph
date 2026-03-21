---
id: spectral-photometry-colors
title: Stellar Photometry, Colors, and Spectral Classification
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: parallax-and-distance-ladders
  type: soft
builds-toward:
- star-clusters-age-dating
tags:
- photometry
- colors
- spectral-classification
stage: formal-systems
status: draft
---

# Stellar Photometry, Colors, and Spectral Classification

## Core Idea
Photometry measures stellar brightness in different wavelength bands; color indices compare magnitudes at different wavelengths, revealing temperature. Spectral classification (O, B, A, F, G, K, M types) orders stars by temperature and composition. Together, photometry and spectroscopy enable measurement of distance, luminosity, temperature, and mass for stars.

## Questions

```yaml
- question: "Two stars are measured. Star X has a B−V color index of −0.3. Star Y has a B−V color index of +1.6. Which star has a higher surface temperature?"
  type: multiple-choice
  options:
    - "Star Y — a larger color index means more total luminosity, which indicates greater energy output and temperature"
    - "Star X — a smaller or negative B−V means the star is relatively brighter in blue light, indicating higher temperature"
    - "Neither — B−V measures chemical composition, not temperature"
    - "Star Y — positive B−V values indicate ultraviolet emission characteristic of hot stars"
  answer: 1
  explanation: "B−V is the difference in magnitude between blue and visual filters. Because magnitudes are on a reversed scale (smaller magnitude = brighter), a small or negative B−V means the star is brighter in blue than in visual — indicating its emission peaks toward shorter wavelengths and therefore a higher surface temperature. Star X with B−V = −0.3 is blue-white and hot (like an O or B star). Star Y with B−V = +1.6 is relatively brighter in visual light, indicating a cool red star. Option D has the relationship backwards — O-type stars (hot, blue) have negative or very small B−V values."

- question: "O-type stars have surprisingly weak hydrogen absorption lines despite hydrogen being by far their most abundant element. What is the correct explanation?"
  type: multiple-choice
  options:
    - "O-type stars have fused most of their hydrogen into helium through nuclear burning"
    - "At extremely high temperatures (above ~30,000 K), hydrogen is mostly ionized and has no bound electrons available to absorb photons at visible wavelengths"
    - "O-type stars rotate so rapidly that spectral lines are broadened beyond detectability"
    - "Hydrogen absorption only occurs in cool stars where molecules can form"
  answer: 1
  explanation: "Spectral line strengths depend on both the abundance of an element and the physical state of its atoms at the star's surface temperature. In O-type stars, temperatures exceed 30,000 K, which is hot enough to strip electrons from most hydrogen atoms — the hydrogen is ionized. Ionized hydrogen (a bare proton) cannot absorb photons at hydrogen's characteristic wavelengths because those absorption transitions require a bound electron. The hydrogen is present in enormous quantities, but it's in the wrong physical state to produce absorption lines. A-type stars (~10,000 K) show the strongest hydrogen lines because the temperature is 'just right' to populate the energy levels involved in visible-light absorption transitions."

- question: "A star with a large positive B−V color index is hotter than a star with a small or negative B−V color index."
  type: true-false
  answer: false
  explanation: "This reverses the relationship. A large positive B−V means the star is relatively fainter in blue light compared to visual — its emission peaks at longer (redder) wavelengths, indicating a lower surface temperature. Cool M-type stars have large positive B−V values. Hot O- and B-type stars have small or negative B−V values because they emit proportionally more blue light. The intuition is that hotter objects (like a blue flame) appear bluer, which means relatively more blue light — a smaller B−V. Cooler objects (like a red ember) appear redder — a larger B−V."

- question: "A star's spectral type provides information about both its surface temperature and the chemical composition of its atmosphere."
  type: true-false
  answer: true
  explanation: "Spectral classification does reveal both. The spectral sequence O–B–A–F–G–K–M is primarily a temperature sequence, but the specific pattern of absorption lines encodes chemical information as well. The presence and strength of lines from calcium, sodium, titanium oxide, iron, and other species tells astronomers which elements are present and in what ionization states in the star's photosphere. The Sun's G2 classification signals not just its temperature (~5,800 K) but also that it displays prominent ionized calcium H and K lines and neutral metal lines — chemical fingerprints. Deviations from expected line strengths for a given temperature class can reveal unusual abundances."

- question: "Why do A-type stars show the strongest hydrogen absorption lines even though many other star types also contain large amounts of hydrogen?"
  type: short-answer
  answer: "Hydrogen absorption line strength depends not just on how much hydrogen is present but on how many hydrogen atoms are in the right energy state to absorb visible light. In very hot O- and B-type stars, hydrogen is mostly ionized — no bound electrons, no absorption. In very cool K- and M-type stars, hydrogen atoms are in their lowest energy state (ground state) and require ultraviolet, not visible, photons to be excited — so visible absorption lines are weak. A-type stars (~10,000 K) hit the temperature 'sweet spot' where a significant fraction of hydrogen atoms have electrons in the first excited state (n=2), which is exactly the configuration needed to absorb visible-wavelength photons (the Balmer series). Temperature determines the population of that energy level."
  explanation: "This is the key insight that explains why spectral classification reflects temperature: absorption lines are 'thermometers' for the stellar photosphere. The same principle applies to other elements — calcium lines peak in G/K stars, titanium oxide only appears in cool M stars because molecules are destroyed at higher temperatures. Astronomers reading a spectrum aren't just cataloging what elements are present; they're reading the temperature from which quantum transitions are populated. This is what makes spectroscopy so powerful: a single spectrum encodes temperature, composition, and surface gravity."
```

## Explainer

Stars emit light across a broad range of wavelengths, and the shape of that emission — how much energy comes out at each wavelength — is determined primarily by the star's surface temperature. A hot star (say, 30,000 K) peaks in the ultraviolet and appears blue-white; a cool star (3,000 K) peaks in the infrared and appears red. **Photometry** exploits this by measuring a star's brightness through standardized filters that each transmit only a specific wavelength band. The most common system uses U (ultraviolet), B (blue), and V (visual/green) filters. By comparing the brightness measured through different filters, you construct a **color index** — for instance, B−V, the difference in magnitude between blue and visual bands. A small or negative B−V means the star is brighter in blue light, indicating high temperature; a large positive B−V means the star is brighter in the visual band relative to blue, indicating low temperature.

**Spectral classification** goes further by spreading starlight into its full spectrum and examining the pattern of absorption lines — dark features at specific wavelengths where atoms in the star's atmosphere absorb photons. The sequence O, B, A, F, G, K, M (from hottest to coolest) was established by organizing stars according to the strength of these absorption features, which turned out to correlate tightly with surface temperature. O-type stars are so hot that hydrogen is mostly ionized, so hydrogen absorption lines are weak; A-type stars have the strongest hydrogen lines because the temperature is just right for hydrogen atoms to populate the energy level that absorbs visible light; M-type stars are cool enough for molecules like titanium oxide to survive, producing broad absorption bands. The Sun is a G2 star — middle of the sequence, with prominent lines of ionized calcium and neutral metals.

The power of combining photometry and spectroscopy is that together they let you determine a star's fundamental physical properties from its light alone. Color index gives surface temperature quickly and cheaply (you only need two filter measurements). The spectral type refines the temperature and adds information about chemical composition and surface gravity. Once you know the temperature and luminosity — the latter requiring a distance measurement, which is where your knowledge of parallax and the distance ladder comes in — you can place the star on the **Hertzsprung-Russell diagram**, the central organizing tool of stellar astronomy. A star's position on the HR diagram reveals its evolutionary stage, mass, and remaining lifetime, all derived from measuring how bright it is and what color its light is.
