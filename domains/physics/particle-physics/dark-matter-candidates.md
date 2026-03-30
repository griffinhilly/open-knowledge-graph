---
id: dark-matter-candidates
title: Dark Matter Candidates
domain: physics
course: particle-physics
prerequisites:
- id: bsm-overview
  type: hard
- id: standard-model-overview
  type: hard
tags:
- dark-matter
- wimps
- axions
- direct-detection
stage: expert
status: validated
---

# Dark Matter Candidates

## Core Idea
Astrophysical and cosmological observations establish that approximately 27% of the universe's energy density consists of non-baryonic dark matter that interacts gravitationally but has not been detected electromagnetically. Particle physics provides several well-motivated candidates: weakly interacting massive particles (WIMPs), axions, sterile neutrinos, and others. Each candidate has distinct production mechanisms, mass ranges, and experimental signatures, driving a diverse program of direct detection, indirect detection, and collider searches.

## Questions

```yaml
- question: "The 'WIMP miracle' refers to the observation that a stable particle with weak-scale mass (~100 GeV - 1 TeV) and weak-scale coupling naturally produces the observed dark matter relic density through thermal freeze-out. How does this work?"
  type: multiple-choice
  options:
    - "WIMPs are produced in nuclear reactors and accumulate over time"
    - "In the early universe, WIMPs are in thermal equilibrium with the SM plasma through annihilation and creation processes; as the universe expands and cools, the annihilation rate drops below the expansion rate and the WIMP abundance 'freezes out' at Omega_DM ~ 0.3 / (sigma*v / 3 x 10^{-26} cm^3/s) — for a particle with weak-scale cross section sigma*v ~ alpha_W^2/m_W^2 ~ 10^{-26} cm^3/s, this gives approximately the observed dark matter density"
    - "WIMPs condense from the Higgs field during the electroweak phase transition"
    - "WIMPs are created by gravitational effects during inflation"
  answer: 1
  explanation: "The thermal relic calculation gives Omega h^2 approximately 0.1 * (3 x 10^{-26} cm^3/s) / (sigma*v). For sigma*v ~ alpha^2/(100 GeV)^2 ~ 10^{-25} - 10^{-26} cm^3/s, the predicted density matches the observed Omega h^2 ~ 0.12. This coincidence -- that the weak scale independently solves both the hierarchy problem and the dark matter problem -- motivated decades of WIMP searches. However, the WIMP miracle is a suggestive coincidence, not a proof, and dark matter could well be something other than a thermal WIMP."

- question: "Direct detection experiments search for dark matter particles scattering off atomic nuclei in underground detectors. The current best limits (from XENON-nT and LZ) exclude spin-independent WIMP-nucleon cross sections above approximately 10^{-47} cm^2 for WIMP masses around 30 GeV. What is the ultimate background that limits these experiments?"
  type: short-answer
  answer: "The ultimate irreducible background is coherent elastic neutrino-nucleus scattering (CEvNS) from solar, atmospheric, and diffuse supernova background neutrinos -- the so-called 'neutrino floor' (more precisely, the 'neutrino fog'). Solar neutrinos (pp and B-8) produce nuclear recoils that mimic low-mass WIMPs (below ~10 GeV), while atmospheric neutrinos mimic higher-mass WIMPs. Below the neutrino floor, WIMP signals cannot be distinguished from neutrino backgrounds without directional detection (which could exploit the anisotropy of the WIMP wind relative to the isotropic neutrino background). Current experiments are within about an order of magnitude of the neutrino floor for WIMP masses around 10-100 GeV."
  explanation: "The neutrino floor is not an absolute barrier but rather a region where the sensitivity improvement per unit exposure slows dramatically (from sqrt(exposure) to a much weaker scaling). The next generation of experiments (DARWIN, XLZD) aims to reach the neutrino floor by ~2030."

- question: "The QCD axion, originally proposed to solve the strong CP problem, is also a viable dark matter candidate. How does axion dark matter differ fundamentally from WIMP dark matter in its production mechanism?"
  type: multiple-choice
  options:
    - "Axions are produced thermally, just like WIMPs, but at lower temperatures"
    - "Axion dark matter is produced non-thermally through the vacuum misalignment mechanism: the axion field starts at a random initial value and oscillates about the minimum of its potential when the Hubble rate drops below the axion mass — these coherent oscillations behave as cold dark matter, with the relic density depending on the initial misalignment angle and the axion mass, typically requiring m_a ~ 10^{-5} - 10^{-3} eV"
    - "Axions are produced in supernovae"
    - "Axions are created from the decay of heavier dark matter particles"
  answer: 1
  explanation: "The axion is ultralight (micro-eV to milli-eV) compared to WIMPs (GeV to TeV), and its dark matter density comes from a coherent classical field rather than a thermal particle population. The misalignment mechanism produces cold dark matter because the axion field oscillations have zero momentum. Additional contributions come from the decay of topological defects (cosmic strings, domain walls) formed during the Peccei-Quinn phase transition. Axion dark matter searches (ADMX, MADMAX, ABRACADABRA) exploit the axion's coupling to photons in the presence of a strong magnetic field (axion-photon conversion in a microwave cavity)."
```

## Explainer

The evidence for **dark matter** comes from multiple independent observations spanning scales from individual galaxies to the observable universe. Galaxy rotation curves, gravitational lensing, the dynamics of galaxy clusters, the cosmic microwave background power spectrum, and the large-scale structure of the universe all require a non-baryonic matter component that constitutes about 27% of the total energy density. The properties of dark matter are constrained: it must be non-relativistic at the time of structure formation (cold), long-lived (stable on cosmological timescales), and interact weakly (if at all) with photons and baryons.

**WIMPs** have been the leading dark matter candidate for decades, motivated by the hierarchy problem (new particles at the weak scale) and the WIMP miracle (thermal freeze-out naturally producing the right relic density). SUSY neutralinos, Kaluza-Klein photons, and other BSM particles at the 100 GeV - 1 TeV scale are specific WIMP candidates. The experimental program has three prongs: (1) direct detection (measuring WIMP-nucleus scattering in underground detectors), (2) indirect detection (searching for WIMP annihilation products in the galaxy -- gamma rays, antiprotons, positrons, neutrinos), and (3) collider production (producing dark matter at the LHC, detected as missing transverse energy). Despite decades of effort, no confirmed detection has occurred, and the remaining WIMP parameter space is shrinking.

The **QCD axion** is motivated independently by the strong CP problem: why the QCD vacuum angle theta is observed to be less than ~10^{-10}, despite having no reason within the Standard Model to be small. The Peccei-Quinn mechanism dynamically relaxes theta to zero by introducing a new global U(1) symmetry, and the axion is the pseudo-Goldstone boson of this symmetry. The axion mass and couplings are inversely related to the symmetry-breaking scale f_a: m_a ~ 6 x 10^{-6} eV * (10^{12} GeV / f_a). The allowed window for the axion dark matter mass is roughly 10^{-6} to 10^{-3} eV (with model-dependent boundaries), and experiments are beginning to probe this range.

Beyond WIMPs and axions, a rich landscape of dark matter candidates exists: **sterile neutrinos** (keV-scale, produced through mixing with active neutrinos, warm dark matter), **dark photons** (new U(1) gauge bosons kinetically mixed with the photon), **asymmetric dark matter** (where the dark matter abundance is set by a matter-antimatter asymmetry analogous to baryons), **primordial black holes**, and **fuzzy dark matter** (ultra-light axion-like particles with m ~ 10^{-22} eV whose de Broglie wavelength is on galactic scales). The breadth of candidates reflects our ignorance of the dark sector and motivates a diverse experimental program spanning underground laboratories, space-based observatories, microwave cavities, atom interferometers, and colliders.
