---
id: line-spectra-discrete-frequencies
title: Line Spectra and Discrete Spectral Frequencies
domain: physics
course: modern-physics
prerequisites:
- id: photon-absorption-emission
  type: hard
- id: emission-absorption-spectra
  type: soft
builds-toward:
- atomic-spectroscopy-intro
tags:
- spectroscopy
- atomic-physics
stage: advanced
status: draft
---

# Line Spectra and Discrete Spectral Frequencies

## Core Idea
Atomic spectra consist of discrete lines at specific frequencies corresponding to transitions between quantized energy levels. Emission spectra show lines where atoms emit photons; absorption spectra show dark lines where photons are absorbed. Line positions reveal energy level spacings; relative intensities reflect transition probabilities and populations. Spectral series (Lyman, Balmer, Paschen, etc.) group transitions ending at the same lower level, appearing as regular patterns that beautifully confirm the quantized energy level picture.

## Explainer

From your study of photon absorption and emission, you know that atoms can only absorb or emit photons whose energy exactly matches the gap between two allowed energy levels: E_photon = hf = E_upper − E_lower. The frequencies of emitted and absorbed light are therefore not arbitrary — they form a discrete **line spectrum**, a fingerprint unique to each element. A gas of hydrogen atoms illuminated by white light will absorb only the specific frequencies that correspond to transitions from the ground state up to excited states, leaving dark lines in the transmitted spectrum. Heat the same gas, and electrons thermally excited to higher levels fall back down, emitting those same frequencies as bright lines. The emission and absorption line positions are identical because they map the same energy level differences.

For hydrogen, the energy levels follow the Bohr formula E_n = −13.6 eV / n², where n = 1, 2, 3, … is the **principal quantum number**. A transition from level n_upper down to level n_lower emits a photon of frequency f = (E_upper − E_lower)/h = (13.6 eV/h)(1/n_lower² − 1/n_upper²). Grouping transitions by their common lower level defines the **spectral series**: the **Lyman series** (n_lower = 1) falls in the ultraviolet, the **Balmer series** (n_lower = 2) falls partly in the visible, and the **Paschen series** (n_lower = 3) falls in the infrared. The Balmer series was empirically discovered in 1885, before quantum mechanics, and its regular spacing pattern (visible lines at 656 nm, 486 nm, 434 nm, …) was one of the key clues that led to the Bohr model.

The pattern within each series also has a beautiful structure. As n_upper increases from n_lower + 1 toward infinity, the energy gap increases toward the **series limit** (13.6 eV/n_lower²), and the lines crowd together at higher frequencies. The series limit corresponds to ionization: the electron is removed completely, leaving a continuum of frequencies above the limit rather than discrete lines. Observing where a series converges in the spectrum lets you measure the ionization energy of an atom directly.

**Relative intensities** of spectral lines carry information beyond line positions. A stronger line means either more atoms are making that transition (a population effect — more atoms in the relevant excited state, governed by the Boltzmann distribution at a given temperature) or the transition is intrinsically more probable (a quantum mechanical transition probability, related to the matrix element of the interaction). This is why some spectral lines are prominent and others are faint even when the energy gap would suggest otherwise. For qualitative purposes, the key insight is that each element's line spectrum is unique — no two elements have the same set of energy levels — making spectroscopy the primary tool for identifying chemical composition of distant stars, planetary atmospheres, and laboratory samples without physical contact.
