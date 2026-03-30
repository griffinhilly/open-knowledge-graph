---
id: parton-distribution-functions
title: Parton Distribution Functions
domain: physics
course: particle-physics
prerequisites:
- id: deep-inelastic-scattering
  type: hard
- id: qcd-basics
  type: hard
tags:
- parton-distribution-functions
- pdfs
- dglap
- proton-structure
stage: expert
status: validated
---

# Parton Distribution Functions

## Core Idea
Parton distribution functions (PDFs) f_i(x, Q^2) give the probability density of finding parton i (quark flavor or gluon) carrying momentum fraction x inside the proton at resolution scale Q^2. PDFs cannot be calculated perturbatively and must be extracted from experimental data, but their evolution with Q^2 is predicted by the DGLAP equations and serves as a rigorous test of QCD.

## Questions

```yaml
- question: "PDFs depend on both x (parton momentum fraction) and Q^2 (resolution scale). The x dependence must be measured, but the Q^2 dependence is predicted by the DGLAP evolution equations. What physical process drives the Q^2 evolution?"
  type: multiple-choice
  options:
    - "Quarks accelerate as the proton moves faster"
    - "At higher Q^2, the virtual photon resolves shorter distances and sees the quarks splitting into quark-gluon pairs and gluons splitting into quark-antiquark pairs — this QCD radiation redistributes momentum from high-x to low-x partons as Q^2 increases"
    - "Higher Q^2 means more energy is available to create new quarks"
    - "The strong coupling constant changes with Q^2, making the proton expand"
  answer: 1
  explanation: "DGLAP evolution is driven by the splitting functions P_{ab}(z), which give the probability of parton a emitting parton b carrying fraction z of its momentum. A quark can radiate a gluon (P_{qg}), a gluon can split into a quark-antiquark pair (P_{gq}), and a gluon can radiate a gluon (P_{gg}). At higher Q^2, more of these splittings are resolved, populating the low-x region and depleting high-x partons. The splitting functions are calculable in perturbative QCD, so the Q^2 evolution is a firm prediction."

- question: "The gluon PDF g(x, Q^2) is the dominant parton distribution at small x. At the LHC (Q^2 ~ 10^4 GeV^2), more than 50% of the proton's momentum is carried by gluons. Yet gluons cannot be directly probed by virtual photons in DIS. How is the gluon PDF determined?"
  type: short-answer
  answer: "The gluon PDF is determined indirectly from several sources: (1) the momentum sum rule — the gluon carries whatever momentum fraction is not accounted for by quarks; (2) scaling violations in F_2 — the Q^2 dependence of the quark distributions is driven by gluon splitting, so measuring dF_2/d(ln Q^2) constrains g(x); (3) the longitudinal structure function F_L, which is directly proportional to g(x) at leading order; (4) jet production cross sections in pp and ppbar collisions, which are dominated by gluon-gluon and quark-gluon scattering; and (5) direct photon production and heavy quark production. Modern PDF fits combine all these data in global QCD analyses."
  explanation: "The indirect nature of gluon PDF extraction means it carries larger uncertainties than the quark PDFs, especially at very small and very large x. This is a major source of systematic uncertainty for LHC cross section predictions."

- question: "Two major collaborations (CT, MSHT, NNPDF) provide independent PDF sets. These are critical inputs for predicting cross sections at the LHC. Why do different PDF sets give different predictions, and how are the differences handled?"
  type: multiple-choice
  options:
    - "They use different experimental data and so are measuring different things"
    - "They use similar data but different methodological choices — functional forms for the x dependence, treatment of experimental uncertainties, perturbative order, heavy quark schemes — so their central values and uncertainty bands differ. Cross section predictions quote a 'PDF uncertainty' by comparing results across sets or using the error sets provided by each group"
    - "The differences are negligible and purely cosmetic"
    - "Only one collaboration is correct; the others are deprecated"
  answer: 1
  explanation: "PDF extraction is a complex inference problem: parameterize the x dependence at a starting scale Q_0^2, evolve to all other scales using DGLAP, and fit to thousands of data points. Different groups make different choices about parameterization flexibility (NNPDF uses neural networks with minimal assumptions; CT/MSHT use fixed functional forms), data selection, and uncertainty propagation. The resulting differences are real and propagated to LHC predictions as 'PDF uncertainties,' which are often the dominant theoretical uncertainty for precision cross sections like Higgs production via gluon fusion."
```

## Explainer

**Parton distribution functions** are the bridge between the fundamental QCD Lagrangian and observable hadron-level cross sections. The factorization theorem of QCD states that a hadronic cross section can be written as a convolution of perturbatively calculable partonic cross sections with non-perturbative PDFs: sigma(pp -> X) = sum_{i,j} integral f_i(x_1, Q^2) * f_j(x_2, Q^2) * sigma-hat(ij -> X) dx_1 dx_2. This separation into short-distance (calculable) and long-distance (universal but non-perturbative) components is the foundation of collider phenomenology.

The **DGLAP evolution equations** describe how PDFs change with the resolution scale Q^2. As Q^2 increases, the probe resolves finer structure and sees more parton splittings. The equations are integro-differential equations involving the splitting functions P_{ab}(z), which are calculated perturbatively and now known to three-loop accuracy (NNLO). The evolution predicts that at high Q^2, the gluon and sea quark distributions grow rapidly at small x while the valence quark distributions shift toward smaller x. This has been verified over four decades in Q^2 by combining DIS data from HERA with hadron collider data from the Tevatron and LHC.

Modern **global PDF fits** (CT18, MSHT20, NNPDF4.0) extract PDFs by fitting to thousands of data points from DIS, Drell-Yan, jet production, W/Z production, top quark production, and other processes. The input data span a wide range of x (from ~10^{-5} at HERA to ~0.7 from fixed-target DIS) and Q^2 (from a few GeV^2 to ~10^5 GeV^2 at the LHC). The fits determine not only central values but also uncertainty bands, propagated using either the Hessian method (CT, MSHT) or Monte Carlo replicas (NNPDF). PDF uncertainties are typically the dominant theoretical uncertainty for LHC precision measurements.

At very small x (below ~10^{-3}), the rapid growth of the gluon PDF raises the question of **saturation**: at some point, the gluon density becomes so high that nonlinear recombination effects (gluon merging) must balance the splitting, taming the growth. This regime is described by the BFKL and BK/JIMWLK evolution equations and is a major target for future electron-ion collider (EIC) experiments. Understanding the transition from the dilute (DGLAP) to the saturated regime is one of the frontiers of QCD.
