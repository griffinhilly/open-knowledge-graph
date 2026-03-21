---
id: fermi-gas-finite-temperature
title: Fermi Gas at Finite Temperature
domain: physics
course: statistical-mechanics
prerequisites:
- id: fermi-energy-fermi-surface
  type: hard
- id: canonical-ensemble
  type: soft
tags:
- fermi-gas
- thermal-effects
- thermodynamic-quantities
stage: advanced
status: draft
---

# Fermi Gas at Finite Temperature

## Core Idea
For kT ≪ E_F, the Fermi-Dirac distribution n(E) ≈ 1 for E < μ(T), ≈ 0 for E > μ(T), smoothing over a width ~kT. Chemical potential μ(T) ≈ E_F [1 − π^2(kT/E_F)^2/12 + ...]. Heat capacity C_V ≈ (π^2 k_B^2 T / 3) g(E_F) is linear in T, a signature of Fermi liquid behavior.

## Questions

```yaml
- question: "Classical statistical mechanics predicts that each free electron in a metal should contribute (3/2)k_B to the heat capacity, but measured electronic heat capacities are far smaller — roughly 100 times smaller at room temperature. What is the quantum mechanical explanation?"
  type: multiple-choice
  options:
    - "Electrons in metals are relativistic, so classical thermodynamics does not apply to them"
    - "The Pauli exclusion principle blocks most electrons from absorbing thermal energy because all nearby states are occupied; only electrons within ~kT of the Fermi energy have access to empty states and can be thermally excited"
    - "Electron-phonon collisions immediately transfer any absorbed thermal energy to the lattice, so the electrons never actually warm up"
    - "Electron-electron repulsion creates an energy gap just above the Fermi energy, preventing thermal excitation"
  answer: 1
  explanation: "This is the resolution of the classical heat capacity problem that baffled 19th-century physics. Classical equipartition assigns (3/2)k_B per particle regardless of quantum statistics. The quantum answer: an electron deep in the Fermi sea — say, 2 eV below E_F — cannot absorb a thermal fluctuation of ~0.025 eV (room temperature kT) because every state it might jump into within that energy range is already filled by other electrons (Pauli exclusion). Only electrons within roughly kT of the Fermi surface have accessible empty states nearby. The fraction of thermally active electrons is ~kT/E_F ≈ 0.5% at room temperature for a typical metal, making the electronic heat capacity ~100 times smaller than the classical prediction."

- question: "In a metal at room temperature with E_F ≈ 5 eV and kT ≈ 0.025 eV, approximately what fraction of the conduction electrons are thermally active — capable of absorbing thermal energy?"
  type: multiple-choice
  options:
    - "Nearly all of them — thermal energy at room temperature is sufficient to excite electrons throughout the band"
    - "About 50% — electrons above the Fermi level midpoint are thermally accessible"
    - "About kT/E_F ≈ 0.5% — only electrons within ~kT of the Fermi surface have access to empty states"
    - "None — room temperature is far below the quantum threshold for electron excitation in metals"
  answer: 2
  explanation: "The fraction of thermally active electrons is of order kT/E_F. For typical metals, E_F is a few electron volts while kT at room temperature is ~0.025 eV, giving a ratio of ~0.5%. This tiny fraction is why the electronic heat capacity is so much smaller than the classical prediction: instead of all N electrons contributing (3/2)k_B each, only ~N(kT/E_F) electrons contribute energy of order kT each, giving C_V^{el} ∝ Nk_B(kT/E_F) ∝ T. This linear-T dependence and its small coefficient are direct consequences of the Pauli principle restricting thermal excitations to a thin shell near E_F."

- question: "At finite temperature, the Fermi-Dirac distribution becomes a perfect step function with occupation exactly 1 below μ and exactly 0 above μ."
  type: true-false
  answer: false
  explanation: "The perfect step function is only the T = 0 limit. At any finite temperature T > 0, the Fermi-Dirac distribution f(E) = 1/(exp((E−μ)/kT) + 1) smoothly transitions from ~1 to ~0 over an energy width of approximately 4kT around the chemical potential μ. States just below μ have occupation slightly less than 1; states just above μ have occupation slightly more than 0. The step function is an approximation that becomes exact only as T → 0. For metals at room temperature, where kT ≈ 0.025 eV ≪ E_F ≈ 5 eV, the step remains very sharp and the T = 0 approximation is excellent — but it is still not exact."

- question: "The linear temperature dependence of electronic heat capacity (C_V ∝ T) is a direct consequence of the Pauli exclusion principle restricting thermal excitations to a thin shell of states near the Fermi energy."
  type: true-false
  answer: true
  explanation: "The argument runs directly: thermal excitations are restricted to electrons within ~kT of E_F (Pauli blocks all deeper electrons). The number of thermally active electrons scales as N(kT/E_F). Each picks up energy of order kT. So the total thermal energy scales as U_el ∝ N(kT/E_F)(kT) = Nk²T²/E_F, and the heat capacity C_V = dU/dT ∝ Nk²T/E_F ∝ T. The linear T dependence follows from the two-step logic: Pauli exclusion limits which electrons participate, and how many participate grows linearly with T as the thermal window expands."

- question: "Why does the chemical potential μ(T) shift downward from E_F as temperature increases, rather than remaining fixed at E_F?"
  type: short-answer
  answer: "The downward shift of μ arises from the asymmetric density of states around E_F. In three dimensions, the density of states g(E) ∝ √E, meaning there are more available states just above E_F than just below it. When temperature smears the Fermi-Dirac step, electrons are promoted from just below E_F to just above it. Because g(E) is larger just above E_F, more electrons are added to the region above E_F than are removed from the region below. To maintain the total electron count fixed (charge neutrality), the chemical potential must shift downward — lowering μ slightly reduces the occupation of high-energy states and increases occupation of low-energy states until the total count is restored. The leading correction is μ(T) ≈ E_F[1 − (π²/12)(kT/E_F)²]."
  explanation: "If the density of states were perfectly symmetric around E_F (equal numbers of states just above and just below), the symmetric smearing of the Fermi function would not change the total electron count and μ would remain at E_F. The downward shift is a consequence of the asymmetry: g(E) increases with E, so the asymmetric promotion of electrons requires a compensating downward shift in μ. This effect is tiny in metals at room temperature (the correction is of order (kT/E_F)² ~ 0.003) but becomes important near absolute zero and in systems with sharp features in g(E)."
```

## Explainer

From your study of the Fermi energy and Fermi surface, you have the T = 0 picture: a sharp step function in the occupation number, with all states filled below E_F and all states empty above it. The Fermi surface in k-space is the boundary between occupied and empty states — for a free electron gas it's a perfect sphere, and for real metals it's a complex shape that controls nearly every electronic property. The question at finite temperature is: what happens to this sharp boundary when thermal energy becomes available?

The key insight is that only electrons within roughly kT of the Fermi energy can be affected by temperature. An electron deep in the Fermi sea, say 1 eV below E_F, cannot absorb a thermal fluctuation of 0.025 eV (room temperature) because every neighboring state it might jump into is already occupied. Only electrons close to E_F have access to empty states just above. The result is that the sharp step at E_F smears out over a width of about 4kT, with electrons just below E_F having slightly less than full occupation and electrons just above E_F having slightly more than zero occupation. Everywhere far from E_F, the distribution is essentially unchanged from the T = 0 result.

This thermal smearing also shifts the **chemical potential** μ(T) slightly below E_F. The reason is asymmetric: the density of states g(E) typically increases with energy (in 3D, g(E) ∝ √E), so there are more states just above E_F than just below it. When temperature smears the distribution, slightly more electrons are promoted above E_F than are removed from below, which means the system has "too many" electrons at high energies relative to the symmetric case. To keep the total electron count fixed, μ must shift downward to re-balance. The leading correction is μ(T) ≈ E_F[1 − (π²/12)(kT/E_F)²], a quadratic suppression that is tiny for metals at room temperature.

The linear heat capacity is the most experimentally important prediction. Classical statistical mechanics predicts each electron should contribute (3/2)k_B to the heat capacity — a result that dramatically overestimates the measured heat capacity of metals. The resolution is that only the fraction ~kT/E_F of electrons near the Fermi surface can absorb thermal energy. Each of these electrons picks up energy of order kT, giving an electronic contribution to heat capacity of C_V^{el} ∝ Nk_B(kT/E_F) ∝ T. This linear T dependence is a characteristic signature of **Fermi liquid behavior** and has been confirmed in countless metals. At very low temperatures where lattice vibrations (which contribute C_V ∝ T³) are frozen out, the linear electronic term dominates, allowing direct measurement of g(E_F).

The Sommerfeld expansion — expanding thermodynamic quantities in powers of (kT/E_F) — is the systematic framework for computing all finite-temperature corrections. The same framework predicts the **Wiedemann-Franz law**: the ratio of thermal to electrical conductivity is proportional to T, with a universal coefficient. Both heat and charge are carried by electrons near the Fermi surface, and the ratio of these two transport coefficients depends only on fundamental constants and T. This law, confirmed across a wide range of metals, is another consequence of the Fermi-Dirac distribution applied to a nearly-free electron gas. Deviations from it signal that electron-electron or electron-phonon scattering is breaking the simple Fermi liquid picture.


