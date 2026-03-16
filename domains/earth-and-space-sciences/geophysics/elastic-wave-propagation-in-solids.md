---
id: elastic-wave-propagation-in-solids
title: Elastic Wave Propagation in Solids
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-waves
  type: soft
- id: differential-equations-intro
  type: hard
- id: conservation-of-energy
  type: hard
- id: wave-equation-pde
  type: soft
- id: wave-equation-one-dimensional
  type: soft
builds-toward:
- seismic-body-waves-p-and-s
- seismic-surface-waves-rayleigh-love
- seismic-tomography-velocity-imaging
tags:
- seismology
- waves
- continuum-mechanics
- elasticity
stage: advanced
status: draft
---

# Elastic Wave Propagation in Solids

## Core Idea
Elastic waves propagate through solids by deforming the material elastically and transferring energy via strain-stress coupling. The wave equation derives from Newton's second law applied to continuous media, yielding plane wave solutions with velocity depending on elastic moduli and density. Seismic P and S waves are the two fundamental modes of elastic wave propagation in 3D solids.

## Questions

```yaml
- question: "What material property is required for a solid to support S-waves (shear waves) but not required for P-waves?"
  type: multiple-choice
  options:
    - "High density, which resists shear deformation"
    - "A non-zero shear modulus G, reflecting the material's resistance to shear strain"
    - "Low bulk modulus K, allowing the material to compress easily"
    - "Crystalline atomic structure rather than amorphous arrangement"
  answer: 1
  explanation: "P-wave (compressional) velocity depends on bulk modulus K and shear modulus G as v_P = sqrt((K + 4G/3)/ρ). S-wave velocity is v_S = sqrt(G/ρ). If G = 0 (as in a liquid, which cannot resist shear), S-wave velocity is zero — shear waves cannot propagate. P-waves can still propagate in liquids because bulk modulus K remains non-zero. This is why seismic S-waves vanish in Earth's liquid outer core."

- question: "If the bulk modulus K of a solid increases while its density ρ stays constant, the P-wave velocity in that solid increases."
  type: true-false
  answer: true
  explanation: "P-wave velocity is v_P = sqrt((K + 4G/3)/ρ). Increasing K with ρ fixed directly increases the numerator inside the square root, so v_P increases. Physically, a stiffer material (higher K) resists compression more strongly and returns to equilibrium faster, propagating the disturbance at higher speed. This is why seismic P-wave velocities are higher in denser, stiffer mantle rocks than in softer crustal materials."

- question: "Why is the elastic wave equation derived by applying Newton's second law to a continuous volume element rather than to individual atoms?"
  type: short-answer
  answer: "Seismic wavelengths (meters to kilometers) are vastly larger than atomic spacings (angstroms), so discrete atomic structure is irrelevant at the scales of interest. Treating the solid as a continuous elastic medium — where stress and strain are defined for infinitesimal volume elements — is an excellent approximation. Newton's second law applied to such a volume element, combined with the linear stress-strain constitutive relation (Hooke's law), yields the wave equation governing macroscopic elastic deformation."
  explanation: "This continuum mechanics approach is a recurring strategy in physics: when the phenomenon of interest operates on length scales much larger than the microscopic structure, you replace discrete atoms with continuous fields. The validity of this approximation breaks down only when wavelengths approach atomic dimensions (e.g., in phonon physics), which is irrelevant for seismology."
```

## Explainer

From your study of the 1D wave equation and seismic waves, you know that disturbances can propagate through materials, and that seismic P- and S-waves have different velocities and particle motions. Elastic wave propagation in solids gives you the mathematical framework to understand *why* those differences exist — deriving wave speeds and wave modes from the fundamental mechanical properties of materials.

The key idea is treating the solid as a continuous elastic medium. Real solids are made of atoms separated by angstroms, but seismic wavelengths span meters to kilometers — ten orders of magnitude larger. At these scales, the discrete atomic structure is invisible, and the solid can be modeled as a continuous field of stress and strain. Newton's second law applied to an infinitesimal volume element gives: ρ ∂²u/∂t² = ∇·σ, where u is the displacement field, ρ is density, and σ is the stress tensor. The constitutive relation (generalized Hooke's law) then connects stress to strain: σ = C : ε, where C is the elastic stiffness tensor and ε is the strain tensor. Combining these two equations yields the elastic wave equation — a PDE governing how displacement disturbances evolve in space and time.

For an isotropic solid (one whose properties are the same in all directions), the stiffness tensor simplifies to just two independent parameters: the bulk modulus K (resistance to volumetric compression) and the shear modulus G (resistance to shear deformation). The wave equation then splits into two independent modes. Compressional (P-wave) motion involves volume changes — particles move back and forth along the direction of propagation — and travels at v_P = sqrt((K + 4G/3)/ρ). Shear (S-wave) motion involves no volume change — particles move perpendicular to the propagation direction — and travels at v_S = sqrt(G/ρ). Because K and G are both positive for any solid and G appears with a positive coefficient in v_P, P-waves are always faster than S-waves in isotropic media.

The dependence on G explains the S-wave behavior you encountered in seismology. For a liquid, G = 0 — liquids cannot resist sustained shear deformation because they flow. Substituting G = 0 gives v_S = 0: shear waves cannot exist in liquids. P-waves still propagate because liquids do resist compression (K > 0). This is the rigorous foundation for the seismological observation that S-waves disappear at the boundary with Earth's liquid outer core.

Plane wave solutions — displacement fields of the form u = A exp(i(k·x − ωt)) — are the natural solutions to the elastic wave equation. The dispersion relation (the relationship between wavenumber k and frequency ω) is non-dispersive for these bulk modes in a homogeneous solid: all frequencies travel at the same speed, which is why seismic body waves arrive as sharp pulses rather than smeared-out signals. Surface waves (Rayleigh and Love) behave differently — they are dispersive, with different frequencies traveling at different speeds — but that requires boundary conditions at a free surface and is the subject of the next topics in this sequence.
