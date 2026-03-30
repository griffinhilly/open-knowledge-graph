---
id: type-i-type-ii-superconductors
title: Type I and Type II Superconductors
domain: physics
course: condensed-matter-physics
prerequisites:
- id: ginzburg-landau-theory
  type: hard
tags:
- type-i-superconductor
- type-ii-superconductor
- vortex
- mixed-state
- abrikosov
stage: expert
status: validated
---

# Type I and Type II Superconductors

## Core Idea
Type I superconductors (most elemental metals: Pb, Sn, Al) have kappa < 1/sqrt(2) and exhibit a single critical field H_c: below H_c, flux is completely expelled (Meissner state); above H_c, superconductivity is destroyed abruptly (first-order transition). Type II superconductors (most alloys and all high-T_c materials) have kappa > 1/sqrt(2) and exhibit two critical fields: below H_{c1}, full Meissner effect; between H_{c1} and H_{c2}, flux penetrates as quantized Abrikosov vortices in a mixed state; above H_{c2}, normal state. Type II behavior enables superconductivity to survive in much higher fields, making these materials essential for magnets, power cables, and other applications.

## Questions

```yaml
- question: "Why are Type II superconductors far more useful for high-field applications than Type I?"
  type: multiple-choice
  options:
    - "Type II materials have lower resistivity in the normal state"
    - "Type I superconductors are destroyed at a single (typically low) critical field H_c, while Type II superconductors remain superconducting up to H_{c2}, which can be orders of magnitude larger — e.g., Nb₃Sn has H_{c2} ~ 25 T versus lead's H_c ~ 0.08 T"
    - "Type I superconductors cannot carry current"
    - "Type II superconductors have higher critical temperatures"
  answer: 1
  explanation: "The upper critical field H_{c2} = Φ₀/(2πξ²) can be enormous when the coherence length ξ is short — as in dirty alloys and high-T_c cuprates where ξ ~ 1-2 nm. MRI magnets (Nb-Ti, H_{c2} ~ 10-15 T), particle accelerator magnets (Nb₃Sn, H_{c2} ~ 25 T), and fusion magnets all exploit Type II superconductors in the mixed state. Type I materials have H_c of order 0.01-0.1 T, far too low for most applications. The practical current-carrying capacity in the mixed state depends on vortex pinning."

- question: "In the mixed state of a Type II superconductor, each vortex carries exactly one flux quantum Φ₀ = hc/2e. What enforces this quantization?"
  type: multiple-choice
  options:
    - "The crystal lattice spacing determines the flux per vortex"
    - "The single-valuedness of the macroscopic wavefunction ψ = |ψ|e^{iφ}: the phase φ must change by exactly 2πn around any closed loop enclosing vortices, and since the flux is related to the phase winding by Φ = (ħc/e*) × (phase change/2π) with e* = 2e, each 2π winding contributes one Φ₀ = hc/2e"
    - "The magnetic field cannot be divided into smaller units"
    - "Flux quantization is an approximation that breaks down at high fields"
  answer: 1
  explanation: "Flux quantization is a topological requirement. The order parameter ψ = |ψ|e^{iφ} is single-valued, so the phase accumulated around any closed path must be an integer multiple of 2π. Using the second GL equation to relate the phase gradient to the current and vector potential, and applying Stokes' theorem, gives Φ = nΦ₀. A vortex is a topological defect where the phase winds by 2π, trapping one flux quantum. The factor of 2e (rather than e) in Φ₀ = hc/2e directly reflects the Cooper pair charge."

- question: "Abrikosov predicted that vortices in the mixed state form a regular triangular lattice. This has been directly observed by multiple experimental techniques."
  type: true-false
  answer: true
  explanation: "The Abrikosov vortex lattice (1957, Nobel Prize 2003) was first directly imaged by Essmann and Träuble (1967) using the Bitter decoration technique (magnetic particles settling on vortex positions). It has since been observed by scanning tunneling microscopy (STM, which images the suppressed density of states at vortex cores), small-angle neutron scattering (SANS, which sees the magnetic field modulation), and magnetic force microscopy. The triangular (hexagonal) lattice minimizes the free energy among all periodic arrangements. In some materials with anisotropic Fermi surfaces, square vortex lattices can be stabilized."

- question: "Explain the role of vortex pinning in determining the practical current-carrying capacity of a Type II superconductor."
  type: short-answer
  answer: "When a transport current flows through a Type II superconductor in the mixed state, it exerts a Lorentz force F = J × Φ₀ (per unit length) on each vortex. If vortices are free to move, their motion generates an electric field (Faraday's law) and dissipates energy — the material shows resistance despite being nominally 'superconducting.' Vortex pinning — trapping vortices at defects, grain boundaries, precipitates, or artificially introduced nanostructures — prevents this motion. The critical current J_c is the current at which the Lorentz force overcomes the pinning force. Maximizing J_c requires engineering the microstructure to provide strong, dense pinning centers. This is why practical superconducting wires are carefully designed alloys or composites, not pure single crystals."
  explanation: "Without pinning, a Type II superconductor in the mixed state would have zero critical current — any current would move vortices and create resistance. The entire field of applied superconductivity is essentially the engineering of vortex pinning."
```

## Explainer

The distinction between Type I and Type II superconductors, predicted by Abrikosov from Ginzburg-Landau theory, is one of the most practically important results in condensed matter physics. **Type I** superconductors (most pure elemental metals) have a Ginzburg-Landau parameter kappa = lambda/xi less than 1/sqrt(2). The normal-superconducting interface has positive surface energy, so the system avoids creating interfaces. Below the thermodynamic critical field H_c, flux is completely expelled (Meissner state). At H_c, a first-order transition destroys superconductivity entirely. Because H_c is typically small (0.01-0.1 T), Type I materials have limited practical utility.

**Type II** superconductors (alloys, compounds, high-T_c cuprates, and most technologically useful materials) have kappa > 1/sqrt(2). The negative surface energy means the system gains energy by creating normal-superconducting boundaries. This leads to the **mixed state** (or vortex state) between two critical fields. Below H_{c1} = (Phi_0/4pi lambda^2) ln(kappa), full Meissner flux expulsion occurs. Above H_{c1}, it becomes energetically favorable for flux to enter as **quantized vortices** — tubes of normal material (diameter ~2xi) each carrying exactly one flux quantum Phi_0 = hc/2e, surrounded by circulating supercurrents that decay over a distance lambda. The vortices repel each other and arrange into a triangular **Abrikosov lattice**.

As the applied field increases, vortices pack closer together. At the **upper critical field** H_{c2} = Phi_0/(2pi xi^2), vortex cores overlap and the entire material becomes normal. Because xi can be very short in dirty materials and high-T_c compounds (1-2 nm), H_{c2} can be enormous: 25 T for Nb_3Sn, over 100 T for YBCO. This is what makes Type II superconductors useful for high-field magnets. Between H_{c1} and H_{c2}, the material is partially superconducting and partially normal (the vortex cores are normal), with the superconducting fraction decreasing as H approaches H_{c2}.

The practical utility of Type II superconductors depends critically on **vortex pinning**. In a current-carrying superconductor, the Lorentz force pushes vortices transverse to the current. Moving vortices generate an electric field and dissipate energy — producing resistance even in the "superconducting" state. To carry large currents without resistance, vortices must be pinned at defects, grain boundaries, or engineered nanostructures. The **critical current density** J_c is set by the depinning force, not by pair breaking. Entire industries (MRI magnets, particle accelerators, fusion reactors, power transmission) depend on optimizing vortex pinning in Type II superconducting wires and tapes.
