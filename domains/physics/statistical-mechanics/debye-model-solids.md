---
id: debye-model-solids
title: Debye Model of Solids
domain: physics
course: statistical-mechanics
prerequisites:
- id: heat-capacity-of-gases
  type: hard
- id: partition-function-definition
  type: soft
builds-toward:
- einstein-model-solids
- debye-temperature
tags:
- solids
- phonons
- heat-capacity
stage: expert
status: draft
---

# Debye Model of Solids

## Core Idea
The Debye model treats solid vibrations as a gas of phonons with a linear dispersion relation ω = v_s k up to a cutoff frequency ω_D. The density of states g(ω) = 9N ω^2 / ω_D^3 for ω ≤ ω_D recovers the Einstein model limit at high T and gives C_V → 12π^4 R/5 (T/Θ_D)^3 at low T.

## Questions

```yaml
- question: "Diamond has a Debye temperature Θ_D ≈ 2200 K; lead has Θ_D ≈ 100 K. At room temperature (≈ 300 K), which material has a heat capacity closer to the classical Dulong-Petit value of 3R?"
  type: multiple-choice
  options:
    - "Diamond, because a higher Θ_D means more phonon modes are activated at a given temperature"
    - "Lead, because 300 K >> 100 K so nearly all of lead's phonon modes are thermally accessible at room temperature"
    - "Both have the same heat capacity because Dulong-Petit applies universally above absolute zero"
    - "Diamond, because stiff bonds store more energy per degree of freedom than weak bonds"
  answer: 1
  explanation: "The Debye temperature sets the scale above which Dulong-Petit applies: when T >> Θ_D, all modes are thermally accessible and C_V ≈ 3R. For lead, 300 K >> 100 K, so nearly all phonon modes are active and lead's heat capacity is close to 3R. For diamond, 300 K << 2200 K, so most high-frequency modes are frozen out; diamond's heat capacity at room temperature is well below 3R. Option A reverses the logic: high Θ_D means modes are hard to excite (stiff bonds, high frequencies), not easy."

- question: "Why does the Debye model predict C_V ∝ T³ at low temperatures, rather than the temperature-independent 3R of Dulong-Petit?"
  type: multiple-choice
  options:
    - "At low temperatures, atoms vibrate more slowly, reducing the number of atomic collisions that transfer heat"
    - "At low temperatures, only low-frequency phonon modes are thermally accessible, and their density of states g(ω) ∝ ω² produces a T³ integral for total energy"
    - "At low temperatures, quantum zero-point energy dominates and suppresses thermal fluctuations by a factor proportional to T³"
    - "Dulong-Petit fails at low T because atoms rearrange into a different crystal structure with fewer degrees of freedom"
  answer: 1
  explanation: "The T³ law has two ingredients: (1) only modes with ℏω ≲ k_BT are appreciably excited — at low T, this restricts access to low-frequency, long-wavelength phonons near the bottom of the spectrum; (2) the density of states is g(ω) ∝ ω², so the number of accessible modes grows as (k_BT/ℏ)². Combining the energy per mode (~k_BT) with the count of accessible modes (~T²) gives total energy U ∝ T³ and C_V = dU/dT ∝ T³. At high T, all modes are accessible and equipartition gives the constant 3R."

- question: "At temperatures much higher than the Debye temperature (T >> Θ_D), the Debye model recovers the classical Dulong-Petit result C_V = 3R."
  type: true-false
  answer: true
  explanation: "This is the high-temperature limit: when k_BT >> ℏω for all phonon modes, the quantum Planck distribution for each mode reduces to the classical result and each mode contributes k_B to the heat capacity. Summing over all 3N modes gives C_V = 3Nk_B = 3R per mole. This is a necessary consistency check for any correct quantum model of solids: it must reproduce classical thermodynamics in the high-temperature limit where quantum effects are negligible."

- question: "The Einstein model (all atoms vibrating at a single frequency) and the Debye model both correctly predict the T³ dependence of heat capacity at low temperatures."
  type: true-false
  answer: false
  explanation: "At low temperatures, the Einstein and Debye models diverge significantly. The Einstein model predicts C_V ∝ e^(−Θ_E/T) at low T — an exponential decay, far faster than any power law — because a single uniform frequency means all modes are equally and sharply frozen out below Θ_E. The Debye model predicts the T³ law because low-frequency modes (ω → 0) are always accessible, and there are ω² of them per frequency interval. Experimental measurements fit the T³ law; the Einstein model overestimates how rapidly heat capacity drops at low temperature."

- question: "Why are only low-frequency phonon modes excited at low temperatures, and how does this produce the T³ temperature dependence of heat capacity?"
  type: short-answer
  answer: "A phonon mode contributes to heat capacity only if thermal energy k_BT is sufficient to excite it — specifically when k_BT ≳ ℏω. At low T, k_BT is small, so only modes with very low frequency ω satisfy this condition; high-frequency modes are frozen out. The number of accessible modes is those with ω ≲ k_BT/ℏ, and since the density of states is g(ω) ∝ ω², integrating up to this cutoff gives an accessible mode count proportional to (k_BT)³/ℏ³ ∝ T³. Each accessible mode contributes ~k_B to heat capacity, so C_V ∝ T³."
  explanation: "The T³ law is a prediction of the density-of-states structure of 3D wave propagation, not an empirical fit. The ω² density of states reflects that in three dimensions there are quadratically more long-wavelength modes than short-wavelength ones (the same geometry that gives the Planck distribution for photons). At low T, we sample only the bottom of this ω² spectrum, and the T³ result follows inevitably from the counting."
```

## Explainer

From your study of heat capacity of gases, you know that the equipartition theorem predicts C_V = (f/2)R per mole for each quadratic degree of freedom. For a monatomic solid, each atom has three kinetic and three potential energy degrees of freedom, giving C_V = 3R — the **Dulong-Petit law**, which works well at high temperatures. But experiments show that heat capacity falls dramatically below 3R at low temperatures, eventually approaching zero as T → 0. The Debye model is the quantum statistical mechanics story that explains this falloff.

The key physical picture is that atoms in a solid don't vibrate independently — they are coupled, and their collective vibrations form waves that travel through the crystal. These quantized sound waves are called **phonons**, and they play the same role for lattice vibrations that photons play for electromagnetic radiation. At low temperatures, most high-frequency vibrational modes are "frozen out" because thermal energy k_BT is too small to excite a phonon of energy ℏω. Only low-frequency, long-wavelength phonons get excited, and there are few of them — hence the low heat capacity. The partition function approach you may have encountered makes this precise: each phonon mode contributes to heat capacity only when k_BT ≳ ℏω_mode.

The Debye model's improvement over the Einstein model (which treated all atoms as independent oscillators at a single frequency) is in the **density of states**. Real phonons have a range of frequencies from zero up to a maximum **Debye frequency** ω_D, with a density of states g(ω) ∝ ω². This quadratic density of states reflects the geometry of three-dimensional wave propagation — just as in electromagnetic radiation, lower frequencies crowd together more densely in frequency space. The cutoff ω_D is set by requiring that the total number of modes equal 3N (three vibrational modes per atom), fixing ω_D in terms of the speed of sound and the atomic density.

The two limiting regimes are clean and physically transparent. At high temperature (k_BT >> ℏω_D), all modes are thermally excited and equipartition holds: C_V → 3R, recovering Dulong-Petit. At low temperature (k_BT << ℏω_D), only the low-frequency ω ∝ k modes near the origin are populated, and the calculation gives the celebrated **Debye T³ law**: C_V ∝ (T/Θ_D)³, where the **Debye temperature** Θ_D = ℏω_D/k_B characterizes the material. Diamond, with its stiff bonds and light carbon atoms, has Θ_D ≈ 2200 K — its modes are hard to excite, and its room-temperature heat capacity is well below 3R. Lead, with heavy atoms and weak bonds, has Θ_D ≈ 100 K — nearly all its modes are active at room temperature.
