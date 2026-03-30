---
id: nearly-free-electron-model
title: Nearly Free Electron Model
domain: physics
course: condensed-matter-physics
prerequisites:
- id: bloch-theorem
  type: hard
- id: time-independent-perturbation-theory
  type: hard
tags:
- nearly-free-electron
- band-gap
- perturbation-theory
- bragg-scattering
stage: expert
status: validated
---

# Nearly Free Electron Model

## Core Idea
The nearly free electron model treats the crystal potential as a weak perturbation on free electrons. Free electron energy parabolas E = ħ^2k^2/2m, when folded into the first Brillouin zone, cross at zone boundaries. The periodic potential lifts these degeneracies through Bragg scattering, opening energy gaps of magnitude 2|V_G| at each zone boundary, where V_G is the Fourier component of the potential at reciprocal lattice vector G. This model explains the origin of band gaps from first principles and shows that even a weak potential qualitatively changes the electronic structure from continuous to banded.

## Questions

```yaml
- question: "In the nearly free electron model, band gaps open at Brillouin zone boundaries. What is the physical mechanism?"
  type: multiple-choice
  options:
    - "Electrons cannot exist at zone boundaries due to the uncertainty principle"
    - "At zone boundaries, the electron wavelength satisfies the Bragg condition, creating two standing waves — one concentrating charge on atoms (lower energy) and one between atoms (higher energy) — and the energy difference is the gap"
    - "The effective mass of electrons becomes infinite at zone boundaries"
    - "Zone boundaries are where the electron-electron repulsion is strongest"
  answer: 1
  explanation: "At a zone boundary, the electron wavevector satisfies the Bragg condition k = G/2, and two degenerate plane waves e^{ikr} and e^{i(k-G)r} are mixed by the potential. The resulting standing waves are cos(Gx/2) and sin(Gx/2). The cosine wave concentrates electron density on the ion cores (lower energy from attractive potential), while the sine wave concentrates density between ions (higher energy). The energy splitting between these two standing waves is the band gap, equal to 2|V_G|."

- question: "If all Fourier components V_G of the crystal potential are zero, the nearly free electron model reduces to free electrons with no band gaps."
  type: true-false
  answer: true
  explanation: "The band gap at each zone boundary is 2|V_G|, so if V_G = 0 for all G, all gaps vanish and the energy bands are simply the free-electron parabola folded into the Brillouin zone. The model makes this limit explicit: band structure is a perturbative consequence of the periodic potential, and the strength of each gap is directly proportional to the corresponding Fourier component. This is why nearly-free-electron theory works well for simple metals like sodium and aluminum, where the effective potential is indeed weak."

- question: "The nearly free electron model predicts that band gaps are proportional to the Fourier components of the crystal potential. Why does this make FCC metals like aluminum nearly-free-electron-like while transition metals are not?"
  type: short-answer
  answer: "In aluminum and other simple metals, the valence electrons are s and p electrons that are relatively delocalized, making the effective crystal potential weak. The Fourier components V_G are small, so the band structure closely resembles free-electron parabolas with small gaps — the nearly free electron model is quantitatively accurate. In transition metals, the d electrons are more localized around atomic cores, creating a stronger effective periodic potential with large V_G. The resulting band structure has large gaps and flat bands that deviate strongly from free-electron behavior, making the tight-binding model more appropriate."
  explanation: "This is a useful heuristic: the more delocalized the valence electrons, the weaker the effective potential they see, and the better the nearly-free-electron approximation works. The crossover from NFE to tight-binding behavior roughly tracks the localization of the relevant orbitals."

- question: "In the nearly free electron model, what determines whether a material is a metal or an insulator?"
  type: short-answer
  answer: "The key is whether the Fermi energy falls within a band or within a gap. If the number of electrons per unit cell is such that bands are partially filled (Fermi energy crosses a band), the material is metallic. If there are exactly enough electrons to completely fill one or more bands, and the next band is separated by a gap, the Fermi energy falls in the gap and the material is an insulator. In the NFE model, this depends on the interplay between the electron count, the size of the gaps (set by |V_G|), and the geometry of the Brillouin zone — particularly whether the Fermi surface intersects zone boundaries."
  explanation: "Monovalent metals (one electron per atom) always have a half-filled first band and are metallic. Divalent metals can be metallic if the bands overlap despite the gap (which happens when the Fermi sphere extends beyond zone boundaries in some directions). The NFE model makes this geometry transparent."
```

## Explainer

The nearly free electron model asks: what happens to free electrons when you turn on a weak periodic potential? For truly free electrons, the energy is a simple parabola E = hbar^2 k^2 / 2m, and there are no gaps — every energy is allowed. But when this parabola is "folded" into the first Brillouin zone (by shifting k by reciprocal lattice vectors G), the parabolas from different zones overlap and cross. At the crossing points, which occur at zone boundaries where k = G/2, two plane wave states are degenerate.

The periodic potential V(r) = sum_G V_G e^{iG·r} lifts these degeneracies through **Bragg scattering**. Near a zone boundary, the states e^{ikr} and e^{i(k-G)r} are nearly degenerate and are strongly mixed by V_G. Degenerate perturbation theory gives two new eigenstates — standing waves that are symmetric and antisymmetric combinations — with energies split by 2|V_G|. The symmetric standing wave (cos type) piles charge density on the ion cores where the potential is most attractive, lowering its energy. The antisymmetric one (sin type) piles charge between ions, raising its energy. The energy difference is the **band gap**.

The size of each gap is controlled by the Fourier component V_G of the potential at the corresponding reciprocal lattice vector. This is physically sensible: if the potential has a strong component at wavevector G, the electrons at the corresponding zone boundary scatter strongly and the gap is large. If V_G is small, the gap is small and the band structure looks nearly free-electron-like. This is why the model works well for **simple metals** like sodium, potassium, and aluminum, where the valence electrons are delocalized s/p electrons that see a weak effective potential (screened by other electrons).

The nearly free electron model provides the clearest picture of how band gaps arise and why some materials are metals while others are insulators. A metal has a Fermi energy that falls within a band (partially filled states available for conduction). An insulator has a Fermi energy in a gap (no states available at the Fermi level). Whether the bands are partially or completely filled depends on the electron count per unit cell, the gap sizes, and the Brillouin zone geometry. This model is complementary to the tight-binding approach: NFE starts from delocalized electrons and adds a weak lattice, while tight-binding starts from localized atomic orbitals and adds inter-atomic hopping. Real band structures interpolate between these limits.
