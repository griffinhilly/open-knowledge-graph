---
id: gravitational-lensing
title: Gravitational Lensing
domain: physics
course: general-relativity
prerequisites:
- id: schwarzschild-solution
  type: hard
- id: geodesic-equation
  type: hard
tags:
- lensing
- light-deflection
- einstein-ring
- weak-lensing
- strong-lensing
stage: expert
status: validated
---

# Gravitational Lensing

## Core Idea
Gravitational lensing is the deflection of light by massive objects, a direct consequence of photons following null geodesics in curved spacetime. For a photon passing a mass M with impact parameter b, GR predicts a deflection angle α = 4GM/(bc²), which is twice the naive Newtonian prediction. Strong lensing near galaxies and galaxy clusters produces multiple images, arcs, and Einstein rings; weak lensing produces subtle statistical distortions of background galaxy shapes used to map dark matter. Microlensing (temporary brightening) is used to detect compact objects and exoplanets. The 1919 solar eclipse observation of starlight deflection by the Sun, confirming the factor-of-two GR prediction over the Newtonian value, was the first experimental validation of general relativity.

## Questions

```yaml
- question: "General relativity predicts a deflection angle of 4GM/(bc²) for light passing a point mass, while a Newtonian calculation treating photons as massive particles gives 2GM/(bc²). Why is the GR result exactly twice the Newtonian value?"
  type: multiple-choice
  options:
    - "The factor of 2 comes from the photon's relativistic mass being twice its Newtonian effective mass"
    - "In GR, both the temporal curvature (g_{tt}) and the spatial curvature (g_{rr}) contribute equally to the deflection, whereas the Newtonian calculation only accounts for the temporal part"
    - "The Newtonian calculation is incorrect because it uses the wrong value of G"
    - "The factor of 2 arises from frame-dragging effects near the mass"
  answer: 1
  explanation: "In the weak-field limit, the Schwarzschild metric has perturbations in both g_{tt} and g_{rr}. The Newtonian calculation (equivalently, a purely temporal metric perturbation) captures only half the effect. The spatial curvature (the deviation of g_{rr} from unity) contributes an equal amount to the light deflection. For slowly moving massive particles, the spatial curvature contribution is suppressed by v²/c², but for photons traveling at c, both contributions are equal. This factor of 2 was the key prediction distinguishing GR from competing theories and was confirmed by Eddington's 1919 eclipse expedition."

- question: "An Einstein ring is observed when the source, lens, and observer are perfectly aligned."
  type: true-false
  answer: true
  explanation: "When a background source, a gravitational lens, and the observer are collinear, the lensing geometry has perfect axial symmetry. Light from the source is deflected around all sides of the lens equally, forming a complete ring — the Einstein ring. The angular radius of the ring is θ_E = √(4GM D_{LS}/(c² D_L D_S)), where D_L, D_S, and D_{LS} are the angular diameter distances to the lens, to the source, and from the lens to the source. Perfect alignment is rare, so partial arcs are much more commonly observed than complete rings."

- question: "Explain how weak gravitational lensing is used to map the distribution of dark matter in galaxy clusters."
  type: short-answer
  answer: "Weak lensing measures the small, coherent distortions (shear) in the shapes of thousands of background galaxies caused by the gravitational field of a foreground mass distribution. Individual galaxies have intrinsic random shapes, but the lensing-induced shear is correlated — galaxies behind a massive cluster are preferentially stretched tangentially to the cluster center. By statistically averaging over many background galaxies, the shear field is reconstructed, and from it the projected mass distribution of the lens is inferred through inversion. This technique is sensitive to all mass, not just luminous matter, making it a direct probe of dark matter distribution."
  explanation: "Weak lensing has become one of the most powerful tools in observational cosmology. It has confirmed that galaxy clusters contain far more mass than their visible components, mapped the filamentary structure of dark matter on cosmological scales, and provides constraints on dark energy through its effect on the growth of structure."

- question: "Calculate the deflection angle for starlight grazing the Sun's limb, given M_☉ ≈ 2 × 10³⁰ kg and R_☉ ≈ 7 × 10⁸ m."
  type: short-answer
  answer: "α = 4GM/(Rc²) = 4(6.67 × 10⁻¹¹)(2 × 10³⁰)/((7 × 10⁸)(3 × 10⁸)²) = 8.49 × 10⁻⁶ radians ≈ 1.75 arcseconds. This is the value predicted by GR and confirmed by Eddington's 1919 eclipse observations (within the measurement uncertainty of about 20%). The Newtonian prediction would be half this: 0.87 arcseconds. Modern VLBI measurements of radio source deflection by the Sun confirm the GR prediction to better than 0.01% accuracy."
  explanation: "1.75 arcseconds is tiny — roughly the angular size of a quarter seen from 3 km away — which is why a total solar eclipse (blocking the Sun's overwhelming brightness) was necessary for the optical measurement. Radio interferometry now achieves far greater precision without needing an eclipse."
```

## Explainer

The bending of light by gravity is a direct prediction of general relativity. Photons follow null geodesics — paths with ds² = 0 — in the curved spacetime around a massive object. Even in Newtonian gravity, one could naively calculate a deflection by treating a photon as a particle with mass m moving at speed c in a gravitational potential (Soldner's calculation from 1801 gives α = 2GM/bc²). Einstein initially published this Newtonian value in 1911. But when he completed the full theory in 1915, the correct GR result turned out to be twice as large: α = 4GM/(bc²), where b is the closest approach distance (impact parameter). The extra factor of 2 comes from the spatial curvature (the g_{rr} perturbation), which affects photons equally to the temporal curvature but is negligible for slowly moving particles.

The confirmation came in 1919 when Arthur Eddington led expeditions to observe a total solar eclipse from the island of Principe and from Sobral, Brazil. Stars whose light passed near the Sun's limb appeared displaced outward by about 1.7 arcseconds, consistent with the GR prediction of 1.75 arcseconds and inconsistent with the Newtonian prediction of 0.87 arcseconds. The result made Einstein an international celebrity. Modern measurements using very long baseline interferometry (VLBI) of radio quasars achieve far better precision, confirming the GR deflection to 0.01% accuracy through the Shapiro effect and astrometric measurements.

Gravitational lensing scales from solar-system tests to cosmological structures. Strong lensing occurs when a massive galaxy or galaxy cluster bends light from a more distant source dramatically enough to produce multiple images, arcs, or complete Einstein rings. The angular radius of an Einstein ring is θ_E = √(4GM D_{LS}/(c² D_L D_S)), typically about 1 arcsecond for galaxy-mass lenses. Strong lensing provides mass estimates for the lens and can magnify distant sources, acting as a natural telescope. The first observed gravitational lens was the "Twin Quasar" Q0957+561, discovered in 1979.

Weak lensing operates at larger angular scales where the deflections are too small to produce multiple images but large enough to distort the shapes of background galaxies by a few percent. By measuring the statistical correlation of these shape distortions across thousands of galaxies, astronomers reconstruct the projected mass distribution of the foreground structures. This technique directly maps dark matter, since the lensing signal depends on total mass regardless of whether it emits light. Weak lensing surveys have mapped the cosmic web of dark matter filaments, constrained the total matter density of the universe, and placed competitive bounds on the equation of state of dark energy. Microlensing — the temporary magnification of a background star by a compact foreground object — is sensitive to objects as small as planets and is used to detect exoplanets and constrain the population of compact dark objects in our galaxy.
