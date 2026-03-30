---
id: drude-sommerfeld-models
title: Drude and Sommerfeld Models
domain: physics
course: condensed-matter-physics
prerequisites:
- id: fermi-gas-ideal-quantum
  type: hard
- id: band-theory-intro
  type: soft
tags:
- drude-model
- sommerfeld-model
- free-electron
- electrical-conductivity
stage: expert
status: validated
---

# Drude and Sommerfeld Models

## Core Idea
The Drude model treats conduction electrons as a classical ideal gas that undergoes collisions with a characteristic relaxation time tau, yielding the DC conductivity sigma = ne^2 tau / m and the Hall coefficient R_H = -1/ne. It correctly predicts Ohm's law and the Wiedemann-Franz ratio but fails for the electronic specific heat (predicting 3/2 k_B per electron, far too large). The Sommerfeld model corrects this by applying Fermi-Dirac statistics: at temperature T, only the fraction ~k_BT/E_F of electrons near the Fermi surface are thermally active, giving a specific heat C_el = (pi^2/2)(k_BT/E_F)(Nk_B) that is linear in T and much smaller than the classical prediction.

## Questions

```yaml
- question: "The Drude model successfully predicts the Wiedemann-Franz law (κ/σT = L₀) relating thermal and electrical conductivity. Why does this work despite the model's incorrect treatment of electron statistics?"
  type: multiple-choice
  options:
    - "The Wiedemann-Franz law is independent of electron statistics"
    - "Both thermal and electrical conductivity depend on the same relaxation time τ and carrier density n. When you form the ratio κ/σT, the incorrectly estimated velocity and specific heat per electron cancel, leaving a ratio that depends only on fundamental constants — the errors compensate in the ratio"
    - "Drude used quantum mechanics for the thermal conductivity calculation"
    - "The Wiedemann-Franz law only works at high temperatures where classical statistics are valid"
  answer: 1
  explanation: "In the Drude model, σ = ne²τ/m and κ = (1/3)nv²τc_v, where the classical values of v² = 3k_BT/m and c_v = 3k_B/2 give κ/σT = 3(k_B/e)² / 2. The Sommerfeld model replaces v² → v_F² and c_v → (π²/2)(k_BT/E_F)k_B, but these changes cancel in the ratio, giving κ/σT = π²k_B²/(3e²) = L₀, the Lorenz number. The numerical prefactor changes (Sommerfeld gets π²/3 instead of 3/2) but is closer to experiment. The cancellation of errors is a beautiful accident."

- question: "Why does the Drude model overestimate the electronic specific heat of metals by a factor of ~100?"
  type: multiple-choice
  options:
    - "The Drude model ignores electron-electron interactions"
    - "Classically, all n electrons each contribute 3k_B/2 to the heat capacity. Quantum mechanically (Sommerfeld), only electrons within ~k_BT of the Fermi level can absorb thermal energy — a fraction ~k_BT/E_F of the total — reducing the specific heat by a factor of ~T/T_F ≈ 1/100 at room temperature"
    - "The Drude model uses the wrong value of the electron mass"
    - "Phonon contributions mask the electronic specific heat in the Drude model"
  answer: 1
  explanation: "For typical metals, E_F ~ 5-10 eV and room temperature k_BT ~ 0.025 eV, so k_BT/E_F ~ 1/200-1/400. The Pauli exclusion principle 'freezes out' most electrons: those deep in the Fermi sea have no empty states nearby to be excited into. Only the thin shell of electrons within ~k_BT of E_F can participate in thermal processes. This was one of the great triumphs of applying quantum statistics to metals — it resolved the long-standing puzzle of why the electronic contribution to specific heat was far smaller than the classically expected value."

- question: "The Drude model predicts a Hall coefficient R_H = -1/ne for a metal with n free electrons per unit volume. Some real metals (e.g., aluminum, beryllium) have positive Hall coefficients. Does this falsify the free-electron picture?"
  type: true-false
  answer: false
  explanation: "A positive Hall coefficient does not falsify free-electron physics per se — it reveals the limitations of the single-band free-electron model. In metals with multiple partially filled bands, the Hall coefficient depends on the contributions from both electron-like and hole-like carriers. If hole carriers dominate the Hall response (which can happen due to band structure effects and anisotropic scattering), R_H becomes positive. Beryllium and aluminum are classic examples: their band structures create hole pockets that dominate the Hall effect. A multi-band Drude model or full Boltzmann transport calculation correctly accounts for these cases."

- question: "Explain the key physical improvement Sommerfeld made over Drude, and why it matters for understanding metals."
  type: short-answer
  answer: "Sommerfeld replaced the classical Maxwell-Boltzmann distribution with the quantum Fermi-Dirac distribution for the conduction electrons, while keeping the free-electron (no lattice potential) and relaxation-time approximations. This single change resolves the specific heat anomaly (C_el ∝ T instead of constant), correctly predicts the Pauli paramagnetic susceptibility (temperature-independent, proportional to g(E_F)), and fixes the magnitude of the thermopower. The essential physics is that Fermi-Dirac statistics restrict thermal excitations to the narrow energy window ~k_BT around E_F, rather than allowing all electrons to participate equally."
  explanation: "Historically, the specific heat problem was devastating for the Drude model — equipartition demanded a huge electronic contribution that experiments simply did not show. Sommerfeld's fix (1928) showed that quantum statistics, not some failure of the free-electron picture, was the missing ingredient."
```

## Explainer

The **Drude model** (1900) is the simplest theory of electrical conduction: treat the n conduction electrons per unit volume as a classical ideal gas that undergoes random collisions every tau seconds on average, each collision randomizing the electron's velocity. Between collisions, an applied electric field E accelerates each electron, producing a drift velocity v_d = -eE tau/m and a current density j = nev_d = (ne^2 tau/m)E. This immediately gives **Ohm's law** with conductivity sigma = ne^2 tau/m. The model also predicts the Hall effect (R_H = -1/ne), AC conductivity (sigma(omega) = sigma_0/(1 - i omega tau)), and a Wiedemann-Franz-like ratio between thermal and electrical conductivity.

The Drude model has two major failures, both rooted in its classical treatment of electron statistics. First, the **specific heat**: equipartition gives each electron 3k_B/2, predicting a total electronic specific heat of (3/2)nk_B — far larger than what is observed. Experimentally, the electronic specific heat at room temperature is roughly 1% of the classical value. Second, the **magnetic susceptibility**: classical electrons should exhibit Curie-like paramagnetism proportional to 1/T, but metals show temperature-independent Pauli paramagnetism.

**Sommerfeld** (1928) resolved both problems by a single change: replacing the Maxwell-Boltzmann distribution with the **Fermi-Dirac distribution**. At temperature T, the occupation of states follows f(E) = 1/(e^{(E-E_F)/k_BT} + 1). Since E_F is typically 5-10 eV while k_BT at room temperature is only 0.025 eV, the Fermi function is nearly a step function. Only electrons within ~k_BT of E_F can be thermally excited — a fraction k_BT/E_F of the total. This immediately gives a specific heat C_el = gamma T with gamma proportional to g(E_F) (and thus to m*/m), roughly 100 times smaller than the classical prediction at room temperature. Similarly, only Fermi-surface electrons can flip their spin in a magnetic field, giving temperature-independent Pauli paramagnetism chi = mu_B^2 g(E_F).

The Sommerfeld model retains the free-electron assumption (no lattice potential, parabolic dispersion) and the phenomenological relaxation time tau. Despite this simplicity, it quantitatively explains the electronic specific heat and magnetic susceptibility of simple metals and provides the correct framework for understanding transport. Its limitations — inability to explain band gaps, the sign of the Hall coefficient in some metals, or the origin of tau itself — are addressed by adding the periodic lattice potential (Bloch's theorem) and the theory of electron-phonon and electron-impurity scattering.
