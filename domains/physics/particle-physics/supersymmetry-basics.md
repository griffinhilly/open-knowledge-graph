---
id: supersymmetry-basics
title: Supersymmetry Basics
domain: physics
course: particle-physics
prerequisites:
- id: bsm-overview
  type: hard
- id: standard-model-overview
  type: hard
tags:
- supersymmetry
- susy
- sparticles
- naturalness
stage: expert
status: validated
---

# Supersymmetry Basics

## Core Idea
Supersymmetry (SUSY) is a symmetry relating bosons and fermions: every Standard Model particle has a superpartner with spin differing by 1/2. SUSY solves the hierarchy problem by cancelling the quadratic divergences in the Higgs mass, provides a dark matter candidate (the lightest supersymmetric particle), and enables gauge coupling unification. The minimal supersymmetric Standard Model (MSSM) doubles the particle content and introduces over 100 new parameters, making it a rich but complex framework.

## Questions

```yaml
- question: "SUSY solves the hierarchy problem by cancelling the quadratic divergences in the Higgs mass. For example, the top quark loop contributes delta m_H^2 ~ -3 y_t^2 Lambda^2 / (8 pi^2) to the Higgs mass-squared. How does the top squark (stop) cancel this?"
  type: multiple-choice
  options:
    - "The stop has opposite electric charge and its loop contribution has opposite sign"
    - "The stop is a scalar with the same Yukawa coupling y_t, and its loop contributes delta m_H^2 ~ +3 y_t^2 Lambda^2 / (8 pi^2) — the opposite sign arises because fermion loops and boson loops contribute with opposite signs to the Higgs self-energy; if the stop and top have the same coupling and mass, the cancellation is exact"
    - "The stop absorbs the top quark's contribution through mixing"
    - "The stop loop is suppressed by a factor of 1/Lambda^2 that cancels the Lambda^2 from the top loop"
  answer: 1
  explanation: "In supersymmetry, for every fermion loop that contributes +Lambda^2, there is a boson (superpartner) loop that contributes -Lambda^2, and vice versa. The relative sign comes from the minus sign for closed fermion loops in Feynman diagrams. If SUSY is exact (superpartners have the same mass as their partners), the cancellation is perfect and there are no quadratic divergences at all. When SUSY is broken (superpartners are heavier), the cancellation is imperfect and gives delta m_H^2 ~ (m_stop^2 - m_top^2) * y_t^2 * ln(Lambda) / (8 pi^2). For the hierarchy problem to be solved 'naturally,' the stop mass should be within a factor of ~10 of the top mass, suggesting m_stop below ~1-2 TeV."

- question: "In the MSSM with R-parity conservation, the lightest supersymmetric particle (LSP) is stable. If the LSP is the lightest neutralino (a mixture of the superpartners of the photon, Z, and Higgs bosons), it is a natural dark matter candidate. Why?"
  type: short-answer
  answer: "The lightest neutralino has the right properties for a WIMP (weakly interacting massive particle) dark matter candidate: it is electrically neutral (it doesn't emit or absorb light), it is stable (R-parity prevents its decay into SM particles), it interacts via the weak force (giving detectable cross sections in direct detection experiments and the right annihilation rate in the early universe), and its mass can naturally be in the 100 GeV - 1 TeV range. The 'WIMP miracle' is that a particle with weak-scale mass and weak-scale couplings naturally produces a thermal relic abundance consistent with the observed dark matter density Omega_DM ~ 0.26 — the annihilation cross section sigma*v ~ 3 x 10^{-26} cm^3/s is in the right ballpark for a weakly interacting particle with mass ~100 GeV."
  explanation: "While the WIMP miracle is suggestive, it is not proof. Direct detection experiments (XENON, LZ, PandaX) have excluded much of the natural WIMP parameter space without a detection. The remaining allowed regions include well-tempered neutralinos, co-annihilation scenarios, and resonance regions. If the LSP is a gravitino or axino instead of a neutralino, the phenomenology changes entirely."

- question: "The MSSM has 105 new free parameters beyond the Standard Model's 19. Despite this, SUSY is considered a predictive framework. How is this possible?"
  type: multiple-choice
  options:
    - "Because most of the parameters are unmeasurable"
    - "Because specific SUSY-breaking mechanisms (gravity mediation, gauge mediation, anomaly mediation) relate the 105 parameters to a small number of inputs at a high scale — for example, the constrained MSSM (CMSSM) reduces the parameters to just 5 (m_0, m_{1/2}, A_0, tan beta, sign(mu)), which then predict the entire superpartner spectrum through renormalization group evolution"
    - "Because the 105 parameters are all very small"
    - "Because experiments can only measure a few parameters at a time"
  answer: 1
  explanation: "The large number of MSSM parameters reflects our ignorance of how SUSY is broken. Specific breaking mechanisms impose relations among the soft SUSY-breaking parameters at the mediation scale, reducing the parameter count dramatically. Gravity mediation gives 5 parameters (CMSSM/mSUGRA), gauge mediation gives 6, anomaly mediation gives 3-4. Each scenario predicts a distinctive pattern of superpartner masses and mixing angles. LHC searches have excluded the simplest versions of each scenario in significant regions of parameter space, but more complex (and less constrained) scenarios remain viable."
```

## Explainer

**Supersymmetry** is the unique extension of the Poincare spacetime symmetry that relates particles of different spin. In a SUSY theory, every boson has a fermionic partner and vice versa: the electron (spin 1/2) has a scalar selectron (spin 0), the photon (spin 1) has a fermionic photino (spin 1/2), and the Higgs boson (spin 0) has a fermionic higgsino (spin 1/2). This doubling of the particle spectrum is the price of the symmetry, but the payoff is substantial: the quadratic divergences in the Higgs mass cancel exactly if SUSY is unbroken.

The **MSSM** (Minimal Supersymmetric Standard Model) is the simplest phenomenologically viable SUSY model. It contains superpartners for all SM particles: squarks and sleptons (spin-0 partners of quarks and leptons), gluinos (spin-1/2 partner of the gluon), charginos and neutralinos (spin-1/2 mixtures of wino, bino, and higgsino states), and two Higgs doublets (required by the structure of SUSY and holomorphy of the superpotential), giving five physical Higgs bosons (h, H, A, H+, H-). The 105 new parameters are the soft SUSY-breaking masses, mixing angles, and phases.

A key feature of the MSSM is **R-parity**, a discrete symmetry under which SM particles have R = +1 and superpartners have R = -1. If R-parity is conserved, superpartners are always produced in pairs and the lightest superpartner (LSP) is stable. A neutral LSP (typically the lightest neutralino) is an excellent dark matter candidate. R-parity also implies that SUSY events at the LHC always contain two LSPs escaping the detector, producing the characteristic missing transverse energy signature. SUSY searches at the LHC typically look for jets and/or leptons plus large missing energy.

The **experimental status** of SUSY is that no superpartners have been found. LHC searches have excluded gluinos below ~2.3 TeV and first/second generation squarks below ~1.8 TeV in simplified models. Light stops (below ~1.2 TeV in most scenarios) are excluded except in compressed spectra where the stop-LSP mass difference is small. These limits have pushed the MSSM into regions of parameter space where the hierarchy problem solution requires some fine-tuning (~1% level or worse), leading to debate about whether naturalness remains a reliable guide. SUSY remains theoretically attractive for its other virtues -- gauge coupling unification, dark matter, and its role in string theory -- and the search continues at the LHC, the HL-LHC, and future colliders.
