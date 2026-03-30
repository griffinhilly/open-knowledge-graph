---
id: tight-binding-model
title: Tight-Binding Model
domain: physics
course: condensed-matter-physics
prerequisites:
- id: bloch-theorem
  type: hard
- id: band-theory-intro
  type: soft
tags:
- tight-binding
- lcao
- hopping-integral
- band-structure
stage: expert
status: validated
---

# Tight-Binding Model

## Core Idea
The tight-binding model constructs crystal electronic states by starting from isolated atomic orbitals and introducing hopping between neighboring atoms. An electron in atomic orbital phi(r - R_i) at site R_i can tunnel to a neighboring site R_j with amplitude t (the hopping or transfer integral). The resulting Bloch states have energies E(k) = epsilon_0 - t sum_delta e^{ik·delta}, where the sum runs over nearest-neighbor vectors delta. For a simple cubic lattice with one orbital per site, this gives E(k) = epsilon_0 - 2t(cos k_x a + cos k_y a + cos k_z a) — a cosine band whose width is 12t. The tight-binding approach naturally produces narrow bands from localized orbitals and is the complement of the nearly free electron model.

## Questions

```yaml
- question: "In the tight-binding model, the bandwidth (energy range of a band) is directly proportional to the hopping integral t. What physical quantity determines the magnitude of t?"
  type: multiple-choice
  options:
    - "The atomic number of the element"
    - "The temperature of the crystal"
    - "The overlap between atomic orbitals on neighboring sites — larger overlap means larger |t| and wider bands"
    - "The number of electrons per atom"
  answer: 2
  explanation: "The hopping integral t = <phi(r - R_i)|H|phi(r - R_j)> measures how much an electron's energy changes when it tunnels from one atomic site to a neighbor. This depends directly on the spatial overlap between orbitals on adjacent sites. Tightly bound core electrons have small overlap and narrow bands; diffuse s and p orbitals have large overlap and wide bands. This is why d-bands in transition metals are narrower than sp-bands, and why bandwidth generally increases with pressure (atoms closer together means more overlap)."

- question: "The tight-binding model and the nearly free electron model are opposite limits of the same physics — they both produce band structures with gaps, just starting from different assumptions."
  type: true-false
  answer: true
  explanation: "The nearly free electron model starts from delocalized plane waves and treats the crystal potential as a weak perturbation — appropriate for wide bands and small gaps. The tight-binding model starts from localized atomic orbitals and treats inter-site tunneling as the perturbation — appropriate for narrow bands formed from localized states. Real materials fall somewhere between these limits. For simple metals (Na, Al), the NFE picture is more natural. For transition metal d-bands and rare earth f-bands, tight-binding is more natural. Both produce the same qualitative result: discrete energy bands separated by gaps."

- question: "In a one-dimensional tight-binding chain with lattice constant a and nearest-neighbor hopping t, the dispersion is E(k) = ε₀ - 2t cos(ka). At what k-values does the group velocity v = (1/ħ)(dE/dk) vanish, and what does this imply physically?"
  type: short-answer
  answer: "The group velocity vanishes at k = 0 and k = ±π/a (the zone center and zone boundaries). At these k-values, dE/dk = 2ta sin(ka)/ħ = 0. Physically, k = 0 corresponds to all atomic orbitals in phase (a bonding-like state), and k = π/a corresponds to alternating phases (an antibonding-like state). Both are standing waves with zero net velocity. Near these points the electron behaves as if it has a large effective mass. The density of states diverges at the band edges (van Hove singularities in 1D), reflecting the accumulation of states where the dispersion is flat."
  explanation: "The vanishing group velocity at zone boundaries connects to the nearly-free-electron picture: these are precisely the standing waves created by Bragg reflection. In tight-binding language, it's where constructive or destructive interference between hopping paths produces a stationary state."

- question: "Why do d-electron bands in transition metals tend to be much narrower than s- or p-electron bands?"
  type: short-answer
  answer: "d orbitals are more spatially localized than s or p orbitals at the same principal quantum number, because their angular momentum keeps them closer to the nucleus. This means the overlap integral between d orbitals on neighboring atoms is smaller, giving a smaller hopping integral t. Since bandwidth is proportional to t (and to the coordination number), d-bands are narrow — typically 3-5 eV wide compared to 10-15 eV for sp-bands. This narrowness has profound consequences: narrow bands mean high density of states, strong correlation effects, and magnetism (as in iron, cobalt, nickel)."
  explanation: "The same logic applies even more strongly to f-electrons in rare earths and actinides. Their 4f/5f orbitals are so localized that hopping is tiny, producing extremely narrow bands (~0.1 eV) where electron correlations dominate completely."
```

## Explainer

The tight-binding model approaches band theory from the atomic limit: start with isolated atoms, each with well-defined atomic orbitals, then bring them together to form a crystal and see how the discrete atomic energy levels broaden into bands. This is essentially the **LCAO** (linear combination of atomic orbitals) method applied to an infinite periodic system. The key parameter is the **hopping integral** t, which measures the quantum mechanical amplitude for an electron to tunnel from an orbital on one atom to an orbital on a neighboring atom.

For a one-dimensional chain with one orbital per atom, the Bloch states are psi_k(r) = (1/sqrt(N)) sum_n e^{ikna} phi(r - na), and the energy eigenvalue is E(k) = epsilon_0 - 2t cos(ka), where epsilon_0 is the on-site atomic energy. The cosine dispersion has a bandwidth of 4t: the bonding state at k = 0 (all orbitals in phase) has the lowest energy, and the antibonding state at k = pi/a (alternating phases) has the highest. In three dimensions on a simple cubic lattice, the sum over three directions gives E(k) = epsilon_0 - 2t(cos k_x a + cos k_y a + cos k_z a) with bandwidth 12t.

The physical content of the model is that **bandwidth measures delocalization**. Larger orbital overlap means larger t and wider bands — the electron is more "free" to move through the crystal. Smaller overlap means narrower bands and more localized behavior. This is why s and p electrons, which extend far from the nucleus, form wide bands and behave nearly free-electron-like, while d and f electrons form narrow bands where strong correlation effects (magnetism, Mott insulating behavior, heavy fermion physics) become important. The tight-binding model quantifies this intuition precisely.

In practice, realistic tight-binding models include multiple orbitals per site, different hopping amplitudes for sigma and pi bonding, next-nearest-neighbor hopping, and spin-orbit coupling. The method is computationally efficient because the Hamiltonian is sparse (only neighboring sites are coupled), and it provides excellent physical intuition about how band structure arises from chemistry. It is also the natural language for many modern topics: the Hubbard model adds on-site electron-electron repulsion to tight-binding, graphene's band structure is a two-orbital tight-binding model on the honeycomb lattice, and topological insulator models are often formulated in tight-binding language.
