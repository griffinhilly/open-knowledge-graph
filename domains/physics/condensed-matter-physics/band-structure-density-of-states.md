---
id: band-structure-density-of-states
title: Band Structure and Density of States
domain: physics
course: condensed-matter-physics
prerequisites:
- id: nearly-free-electron-model
  type: hard
- id: tight-binding-model
  type: hard
tags:
- band-structure
- density-of-states
- van-hove-singularity
- fermi-surface
stage: expert
status: validated
---

# Band Structure and Density of States

## Core Idea
The band structure E_n(k) is the energy-versus-wavevector relationship for electrons in a crystal, with n the band index and k the crystal momentum in the Brillouin zone. The density of states g(E) counts the number of electronic states per unit energy: g(E) = sum_n integral [delta(E - E_n(k))] d^3k / (2pi)^3. Peaks in the density of states (van Hove singularities) occur where the gradient nabla_k E_n(k) vanishes — at band edges, saddle points, and flat regions. The density of states at the Fermi level, g(E_F), governs essentially all low-energy properties: electronic specific heat, Pauli paramagnetism, superconducting transition temperature, and transport.

## Questions

```yaml
- question: "Van Hove singularities in the density of states occur at energies where ∇_k E(k) = 0. Why do these lead to peaks or kinks in g(E)?"
  type: multiple-choice
  options:
    - "At these points electrons cannot move, so they accumulate and increase the density of states"
    - "The density of states integral weights each k-point by 1/|∇_k E|; where the gradient vanishes, the integrand diverges, creating a non-analytic feature in g(E)"
    - "The Pauli exclusion principle forces more electrons into these energy states"
    - "These are points where the crystal potential is strongest"
  answer: 1
  explanation: "The density of states can be written as a surface integral g(E) = integral dS / |∇_k E(k)| over the constant-energy surface E(k) = E. Where ∇_k E → 0, the integrand diverges. In 3D, this produces integrable singularities (kinks or logarithmic divergences) rather than true infinities, but in 1D and 2D the singularities can be stronger. Van Hove showed that these critical points occur at a minimum of four energies in any 3D band (the minimum, maximum, and two types of saddle points)."

- question: "The Fermi surface is the surface in k-space where E_n(k) = E_F. Why is its geometry so important for understanding metallic properties?"
  type: multiple-choice
  options:
    - "The Fermi surface determines the crystal structure of the metal"
    - "Only electrons near the Fermi surface participate in low-energy processes (conduction, heat capacity, scattering), so the shape of the Fermi surface controls transport, magnetic oscillations, and response to perturbations"
    - "The Fermi surface determines the binding energy of core electrons"
    - "The Fermi surface is important only for semiconductors, not metals"
  answer: 1
  explanation: "At typical temperatures, kT << E_F, so the Fermi-Dirac distribution is sharp: states well below E_F are fully occupied and inert; states well above are empty. Only states within ~kT of E_F can be thermally excited or respond to external fields. The Fermi surface is where these active electrons live. Its shape — spherical for free electrons, complex and multi-sheeted for real metals — determines which scattering processes are available, how electrons respond to magnetic fields (de Haas-van Alphen oscillations), and the anisotropy of conductivity."

- question: "In three dimensions, the free-electron density of states goes as g(E) ∝ √E. How does this change qualitatively in a real crystal?"
  type: true-false
  answer: false
  explanation: "This question as stated is not true-false — but to clarify: the free-electron √E density of states is modified significantly in a real crystal. Band gaps create energy ranges where g(E) = 0. Van Hove singularities create peaks and kinks. Flat bands (common in tight-binding models with localized orbitals) produce sharp peaks. The overall shape of g(E) reflects the full band structure and can look nothing like √E. Measuring g(E) experimentally (via photoemission or tunneling spectroscopy) is one of the primary ways to probe electronic structure."

- question: "Explain why the density of states at the Fermi level, g(E_F), appears in the formulas for so many different physical properties of metals."
  type: short-answer
  answer: "Low-energy properties of metals are dominated by electrons near the Fermi level, because only these electrons can change their state in response to small perturbations (thermal, magnetic, electric). The number of such electrons available to respond is proportional to g(E_F). Electronic specific heat is C_el = (π²/3)k_B²T g(E_F), reflecting how many states are thermally accessible. Pauli paramagnetic susceptibility is χ = μ_B² g(E_F), since only Fermi-level electrons can flip spin. The BCS superconducting transition temperature depends on g(E_F) through the coupling strength. In each case, g(E_F) measures the 'reservoir' of responsive electrons."
  explanation: "This is why transition metals with their high d-band density of states near E_F have large specific heat coefficients, strong Pauli paramagnetism, and (in some cases) superconductivity — they simply have more electrons available to participate in low-energy physics."
```

## Explainer

The **band structure** E_n(k) is the complete map of allowed electron energies as a function of crystal momentum k within the Brillouin zone. Each band n is a continuous function of k, and the set of all bands determines virtually every electronic property of the material. Band structures are typically plotted along high-symmetry paths in the Brillouin zone (for example, Gamma-X-M-Gamma in a square lattice), which captures the essential features: band widths, gap sizes, band crossings, and flat regions.

While the band structure contains full information, many properties depend only on how many states exist at each energy — the **density of states** g(E). This is computed by integrating over the Brillouin zone: g(E) = sum_n integral delta(E - E_n(k)) d^3k / (2pi)^3. For free electrons in 3D, g(E) is proportional to sqrt(E), reflecting the growing surface area of the constant-energy sphere. In a real crystal, g(E) is dramatically modified: it vanishes in band gaps, shows peaks and kinks at **van Hove singularities** (where the gradient of E_n(k) vanishes), and can have sharp spikes from flat bands.

Van Hove singularities are topologically guaranteed. In any 3D band, the gradient must vanish at the band minimum, the band maximum, and at least two saddle points. At these energies, the density of states has non-analytic behavior — a step discontinuity at band edges in 3D, logarithmic divergences at saddle points, and true divergences in lower dimensions. These features have direct physical consequences: if a van Hove singularity lies near the Fermi level, the high density of states enhances the electronic specific heat, magnetic susceptibility, and the tendency toward instabilities (magnetic ordering, charge density waves, superconductivity).

The **Fermi surface** — the constant-energy surface E_n(k) = E_F in k-space — is the single most important geometric object in the physics of metals. At low temperatures, only electrons within ~k_BT of the Fermi surface can participate in transport, thermal, or magnetic processes. The shape of the Fermi surface determines anisotropic conductivity, the de Haas-van Alphen effect (oscillations of magnetization with magnetic field that directly map out the Fermi surface cross-sections), nesting conditions that drive charge and spin density waves, and the phase space for electron-phonon scattering. Experimental techniques like ARPES (angle-resolved photoemission spectroscopy) can now measure both the band structure and the Fermi surface with remarkable precision.
