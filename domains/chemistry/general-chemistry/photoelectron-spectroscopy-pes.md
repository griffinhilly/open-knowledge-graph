---
id: photoelectron-spectroscopy-pes
title: Photoelectron Spectroscopy (PES)
domain: chemistry
course: general-chemistry
prerequisites:
- id: electron-configuration
  type: hard
- id: ionization-energy-and-electron-removal
  type: hard
- id: photoelectric-effect
  type: soft
- id: periodic-trends
  type: soft
builds-toward:
- characterization-methods-tem-sem-xps
tags:
- photoelectron spectroscopy
- binding energy
- subshells
- electron configuration evidence
- AP Chemistry
stage: formal-systems
status: validated
---

# Photoelectron Spectroscopy (PES)

## Core Idea
Photoelectron spectroscopy shines high-energy light on atoms, knocks out electrons, and measures their kinetic energy. The binding energy of each electron is the photon energy minus that kinetic energy. A PES spectrum shows one peak for each occupied subshell: the peak's position gives the binding energy, and its relative height gives the number of electrons in that subshell. PES therefore provides direct experimental evidence for shells, subshells and electron configurations.

## How It's Best Learned
Start from a known configuration, such as neon's 1s² 2s² 2p⁶, and predict its spectrum before looking at it: three peaks, heights 2:2:6, with 1s far to the high-energy side. Then reverse the task and identify unknown elements from spectra. Finally, compare the same subshell across neighboring elements to see how nuclear charge shifts binding energy.

## Common Misconceptions
- A taller peak means the electrons are held more tightly. (Height reflects how many electrons are in the subshell; binding energy is read from the peak's position.)
- The PES binding energy of every peak equals the element's first ionization energy. (Only the lowest-energy peak matches the first ionization energy; inner peaks show electrons removed from deeper subshells.)
- Electrons in the same shell all have the same energy. (The 2s and 2p peaks of neon appear at different energies, showing that subshells within a shell differ in energy.)

## Questions

```yaml
- question: "A PES spectrum shows three peaks with relative heights 2 : 2 : 6, from highest to lowest binding energy. Which element is it?"
  type: multiple-choice
  options: ["Carbon", "Oxygen", "Neon", "Sodium"]
  answer: 2
  explanation: "Heights 2, 2 and 6 match 1s², 2s² and 2p⁶, which is neon. Carbon and oxygen would show smaller 2p peaks, and sodium would add a fourth peak for 3s¹."
- question: "In a PES spectrum, the tallest peak always corresponds to the electrons with the highest binding energy."
  type: true-false
  answer: false
  explanation: "Peak height is proportional to the number of electrons in a subshell. In neon, the 2p peak is tallest because it holds six electrons, yet it has the lowest binding energy."
- question: "How does the 1s peak of sodium compare with the 1s peak of neon?"
  type: multiple-choice
  options: ["Same binding energy, same height", "Higher binding energy, same height", "Lower binding energy, same height", "Higher binding energy, three times the height"]
  answer: 1
  explanation: "Both 1s subshells hold two electrons, so the heights match. Sodium has one more proton, so its 1s electrons are held more tightly and the peak appears at higher binding energy."
- question: "Explain how PES data support the idea that the second shell is divided into subshells."
  type: short-answer
  answer: "Electrons in the second shell give two separate peaks, not one. The 2s peak lies at higher binding energy than the 2p peak, and their heights (2 and up to 6) match the capacities of the s and p subshells."
  explanation: "If all n = 2 electrons had the same energy, they would give one peak. The split into two peaks with these height ratios is direct evidence for s and p subshells."
```

## Explainer

You have learned to write electron configurations like 1s² 2s² 2p⁶. Photoelectron spectroscopy is one of the experiments that shows these configurations are real.

The method builds on the photoelectric effect. A beam of photons with a known, high energy, usually X-rays or far ultraviolet light, strikes a sample of gaseous atoms. Each photon can eject one electron. The instrument measures the kinetic energy of the ejected electrons. Energy is conserved, so:

binding energy = photon energy − kinetic energy

Electrons held loosely leave with a lot of kinetic energy and have a small binding energy. Electrons held tightly leave with little kinetic energy and have a large binding energy.

A PES spectrum plots the number of electrons detected against binding energy. Electrons from the same subshell all have about the same binding energy, so they appear together as one peak. Two features of each peak carry information. Its position tells you how tightly those electrons are held. Its relative height tells you how many electrons are in that subshell.

Consider neon. Its spectrum has three peaks, at about 84, 4.7 and 2.1 MJ/mol. The first is the 1s subshell, deep in the atom and close to the nucleus. The other two are 2s and 2p. Their heights are in the ratio 2 : 2 : 6, matching the configuration exactly. Notice that the lowest binding energy, about 2.1 MJ/mol, equals neon's first ionization energy.

The spectrum also shows things that a configuration alone does not. The 2s and 2p peaks are separate, so electrons in the same shell can have different energies. Moving from one element to the next, the same subshell shifts to higher binding energy because the nucleus has one more proton. Sodium's 1s peak lies at higher energy than neon's, and sodium adds a small fourth peak for its single 3s electron at a very low binding energy.

The same principle, applied with X-rays to solid surfaces, is X-ray photoelectron spectroscopy (XPS), a standard tool for finding which elements are present at a surface and in what oxidation states. Kai Siegbahn shared the 1981 Nobel Prize in Physics for developing high-resolution electron spectroscopy.
