---
id: neutrino-mixing-pmns-matrix
title: Neutrino Mixing (PMNS Matrix)
domain: physics
course: particle-physics
prerequisites:
- id: neutrino-masses-and-oscillations
  type: hard
- id: ckm-matrix-quark-mixing
  type: soft
tags:
- pmns-matrix
- neutrino-mixing
- mixing-angles
- cp-phase-neutrino
stage: expert
status: validated
---

# Neutrino Mixing (PMNS Matrix)

## Core Idea
The Pontecorvo-Maki-Nakagawa-Sakata (PMNS) matrix relates the neutrino flavor eigenstates (nu_e, nu_mu, nu_tau) to the mass eigenstates (nu_1, nu_2, nu_3). It is parameterized by three mixing angles (theta_12, theta_13, theta_23), one Dirac CP phase (delta_CP), and potentially two additional Majorana phases. Unlike the CKM matrix, which is nearly diagonal, the PMNS matrix has two large mixing angles -- a qualitative difference that may hint at different underlying physics governing quark and lepton masses.

## Questions

```yaml
- question: "The CKM matrix is nearly diagonal (small mixing angles), while the PMNS matrix has two large mixing angles (theta_12 ~ 34 degrees, theta_23 ~ 49 degrees). Only theta_13 ~ 8.5 degrees is small. Why is this difference significant?"
  type: multiple-choice
  options:
    - "Because it means the PMNS matrix is more accurately measured"
    - "Because the dramatically different mixing patterns in the quark and lepton sectors suggest that the mechanism generating neutrino masses may be fundamentally different from the Higgs-Yukawa mechanism that generates quark masses — models like the seesaw mechanism or discrete flavor symmetries attempt to explain the large leptonic mixing angles"
    - "Because large mixing angles make neutrino experiments easier"
    - "Because the PMNS matrix has more free parameters than the CKM matrix"
  answer: 1
  explanation: "In the quark sector, the mass hierarchy is steep (m_t/m_u ~ 10^5) and the mixing angles are small (Cabibbo angle ~13 degrees, others smaller). In the lepton sector, the mass-squared ratios are moderate (Delta m^2_{32}/Delta m^2_{21} ~ 30) and two mixing angles are large. This pattern is not explained by the Standard Model. Various models predict specific patterns: tri-bimaximal mixing (theta_12 = arctan(1/sqrt(2)), theta_23 = 45 degrees, theta_13 = 0) was a popular Ansatz that predicted large angles from discrete symmetries, but the observation of nonzero theta_13 ruled out the exact pattern while keeping the general idea alive."

- question: "The PMNS matrix has one Dirac CP phase delta_CP, analogous to the CKM phase, plus two additional Majorana phases alpha_1 and alpha_2 that exist only if neutrinos are Majorana particles. Why don't the Majorana phases affect neutrino oscillation experiments?"
  type: short-answer
  answer: "The oscillation probability involves the product U_{alpha i}* U_{beta i} U_{alpha j} U_{beta j}*, where U is the PMNS matrix. The Majorana phases appear in the matrix as diagonal phase factors: U -> U * diag(1, e^{i*alpha_1/2}, e^{i*alpha_2/2}). In the product U_{alpha i}* U_{beta i}, the Majorana phase from column i cancels between the U* and U factors. Therefore, oscillation probabilities are independent of the Majorana phases. These phases are physical and affect lepton-number-violating processes like neutrinoless double beta decay, where the amplitude is proportional to m_{ee} = |sum_i U_{ei}^2 m_i|, and the U_{ei}^2 (not |U_{ei}|^2) retains the Majorana phases."
  explanation: "This is why determining whether neutrinos are Dirac or Majorana requires experiments beyond oscillation, such as neutrinoless double beta decay (0nu-beta-beta). The observation of 0nu-beta-beta would simultaneously prove neutrinos are Majorana particles and provide information about the absolute mass scale and Majorana phases."

- question: "The atmospheric mixing angle theta_23 is measured to be close to 45 degrees (maximal mixing). Current experiments cannot definitively determine whether theta_23 is slightly above or below 45 degrees (the 'octant' ambiguity). Why does the octant matter?"
  type: multiple-choice
  options:
    - "Because the sign determines whether the neutrino is a particle or antiparticle"
    - "Because the octant of theta_23 (whether nu_3 contains more nu_mu or more nu_tau) affects the interpretation of other measurements, particularly the sensitivity to the CP phase delta_CP in long-baseline experiments, and different theoretical models make distinct predictions about whether theta_23 is above or below maximal"
    - "Because maximal mixing would violate unitarity"
    - "Because the octant determines the neutrino mass ordering"
  answer: 1
  explanation: "If theta_23 = 45 degrees exactly, the nu_3 mass eigenstate is an equal mixture of nu_mu and nu_tau -- this would suggest an underlying mu-tau symmetry. If theta_23 differs from 45 degrees, the direction of the deviation (upper vs. lower octant) breaks this symmetry and constrains theoretical models. The octant also affects the oscillation probability through sub-leading terms involving theta_13 and delta_CP, so resolving it improves the measurement of CP violation. DUNE and Hyper-K aim to determine the octant definitively."
```

## Explainer

The **PMNS matrix** is the leptonic analog of the CKM matrix, describing how the three neutrino flavor eigenstates relate to the three mass eigenstates. It is conventionally parameterized as a product of three rotation matrices (by angles theta_12, theta_13, theta_23) with one Dirac CP phase delta_CP, multiplied by a diagonal matrix containing two Majorana phases. The standard parameterization is U = R_23(theta_23) * diag(1,1,e^{-i*delta}) * R_13(theta_13) * diag(1,e^{i*delta},1) * R_12(theta_12) * diag(1, e^{i*alpha_1/2}, e^{i*alpha_2/2}).

The three mixing angles have been measured by different types of experiments. **theta_12** (~34 degrees) was determined from solar neutrino oscillations (SNO, Super-K) and confirmed by the KamLAND reactor experiment. **theta_23** (~49 degrees) was measured from atmospheric neutrino oscillations (Super-K) and confirmed by long-baseline accelerator experiments (K2K, MINOS, T2K, NOvA). **theta_13** (~8.5 degrees) was measured by reactor experiments (Daya Bay, RENO, Double Chooz) in 2012, a breakthrough that opened the door to measuring the CP phase delta_CP, since CP violation in oscillations requires all three angles to be nonzero.

The **CP phase** delta_CP is the most important unmeasured parameter in the PMNS matrix. Current hints from T2K and NOvA suggest delta_CP may be near -pi/2 (maximal CP violation), but the statistical significance is insufficient for a definitive claim. DUNE (using a 1300 km baseline from Fermilab to South Dakota) and Hyper-Kamiokande (using a 295 km baseline from J-PARC to Kamioka) are designed to measure delta_CP with sufficient precision to establish CP violation at 5 sigma significance for a large fraction of possible values. Leptonic CP violation is of profound interest because it could be connected to the matter-antimatter asymmetry of the universe through leptogenesis.

The overall structure of the PMNS matrix -- two large angles and one small angle -- is strikingly different from the CKM matrix and suggests different organizing principles for the quark and lepton sectors. Numerous models based on discrete flavor symmetries (A_4, S_4, etc.) have been proposed to explain the pattern. The **tribimaximal mixing** pattern (sin^2(theta_12) = 1/3, sin^2(theta_23) = 1/2, theta_13 = 0) was a leading Ansatz until the discovery of nonzero theta_13. Modified patterns that accommodate theta_13 while preserving the approximate structure remain active areas of theoretical research.
