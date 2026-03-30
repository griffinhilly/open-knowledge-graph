---
id: w-and-z-boson-physics
title: W and Z Boson Physics
domain: physics
course: particle-physics
prerequisites:
- id: electroweak-unification
  type: hard
- id: electroweak-precision-measurements
  type: soft
tags:
- w-boson
- z-boson
- weak-interaction
- gauge-bosons
stage: expert
status: validated
---

# W and Z Boson Physics

## Core Idea
The W+/- and Z bosons are the massive gauge bosons of the weak interaction, discovered at CERN's SppS collider in 1983. Their masses (~80.4 and 91.2 GeV), widths, and couplings to fermions are precisely predicted by the electroweak theory. The W boson mediates charged-current interactions (changing quark and lepton flavor) while the Z mediates neutral-current interactions, and their detailed study tests the SU(2)_L x U(1)_Y gauge structure at the quantum level.

## Questions

```yaml
- question: "The W boson couples only to left-handed fermions and right-handed antifermions. This means W bosons produced in quark-antiquark annihilation at a hadron collider are longitudinally polarized at threshold but become increasingly longitudinally polarized at high energy. Why is the longitudinal polarization component particularly interesting?"
  type: multiple-choice
  options:
    - "Because longitudinal W bosons are easier to detect"
    - "Because the longitudinal polarization state comes from the Goldstone boson eaten by the W during electroweak symmetry breaking — it is directly connected to the Higgs mechanism, and its scattering amplitudes grow with energy, making it sensitive to the details of symmetry breaking"
    - "Because longitudinal W bosons have a larger cross section"
    - "Because transverse polarizations are forbidden at high energy"
  answer: 1
  explanation: "By the Goldstone boson equivalence theorem, at high energy the amplitude for longitudinal W scattering equals the amplitude for the corresponding Goldstone boson scattering. Without the Higgs boson, the WW scattering amplitude would grow as E^2 and violate unitarity at approximately 1.2 TeV. The Higgs boson cancels this growth, restoring unitarity. Measuring longitudinal WW scattering at the LHC (vector boson scattering) directly tests this cancellation mechanism."

- question: "The Z boson decays to all kinematically accessible fermion-antifermion pairs. Its branching ratios are: hadrons ~70%, neutrinos ~20%, charged leptons ~10%. Why is the hadronic branching ratio so much larger than the leptonic one?"
  type: short-answer
  answer: "The Z couples to all fermion pairs with strength proportional to their weak isospin and hypercharge quantum numbers. For each fermion, the partial width is proportional to (v_f^2 + a_f^2) * N_c, where v_f and a_f are the vector and axial-vector couplings and N_c is the color factor (3 for quarks, 1 for leptons). The Z can decay to 5 quark flavors (u, d, s, c, b -- not top, which is too heavy), each with N_c = 3, giving 15 'effective' quark channels versus 3 charged lepton channels and 3 neutrino channels. The large hadronic fraction is primarily a counting effect: more quark channels times the color factor of 3."
  explanation: "The precise branching ratios also depend on the electroweak couplings of each fermion. Up-type quarks have different v_f and a_f from down-type quarks, so the partial widths are not all equal. Measuring these ratios tests the electroweak coupling assignments of the Standard Model."

- question: "At hadron colliders, W bosons are primarily produced by quark-antiquark annihilation: u dbar -> W+ and dbar u -> W+. The W+ and W- production cross sections are different at the LHC but equal at the Tevatron. Why?"
  type: multiple-choice
  options:
    - "Because the LHC uses different beam energies for each direction"
    - "Because the LHC is a pp collider (both beams are protons) while the Tevatron was ppbar — in pp collisions, the proton has more u quarks than d quarks (two u vs one d), so u dbar -> W+ is enhanced relative to d ubar -> W-, creating a charge asymmetry; at ppbar, the asymmetry from the proton is exactly compensated by the antiproton"
    - "Because the W+ is lighter than the W- at the LHC"
    - "Because QCD corrections are different for W+ and W-"
  answer: 1
  explanation: "The proton contains two valence u quarks and one valence d quark. At the LHC (pp), W+ production (mainly ud-bar) samples the u valence distribution while W- production (mainly du-bar) samples the d valence distribution. Since u(x) > d(x) at large x, sigma(W+) > sigma(W-) by about 30% at 13 TeV. This charge asymmetry, measured as a function of rapidity, directly constrains the ratio of u and d quark PDFs. At the Tevatron (ppbar), the antiproton provides the conjugate sea, and the charge asymmetry cancels in the total cross section."
```

## Explainer

The **W and Z bosons** were discovered at CERN in 1983 by the UA1 and UA2 experiments at the SppS proton-antiproton collider, confirming the electroweak theory of Glashow, Weinberg, and Salam (Nobel Prize 1979). The W boson (mass 80.4 GeV, width 2.1 GeV) mediates all charged-current weak processes: nuclear beta decay, muon decay, quark flavor changes. The Z boson (mass 91.2 GeV, width 2.5 GeV) mediates neutral-current processes. Their masses arise from the Higgs mechanism and are predicted by the gauge couplings and the Higgs vacuum expectation value.

**W boson physics** at the LHC involves production rates of tens of nanobars (billions of events per year at high luminosity), making the W a precision tool. The charge asymmetry constrains PDFs; the transverse mass distribution measures M_W with ~10 MeV precision; the W polarization tests the V-A structure of the charged current; and W+jets production is a major background to top quark and new physics searches. The helicity structure of W decays is maximally parity-violating: W+ preferentially emits the positively charged lepton in its spin direction, and the negatively charged lepton opposite. This polarization is directly observable in the lepton angular distribution.

The **Z boson** has been the most precisely studied particle in history, thanks to the LEP and SLD programs. At LEP, approximately 17 million Z decays were recorded across four experiments (ALEPH, DELPHI, L3, OPAL), enabling measurements of M_Z, Gamma_Z, and the Z couplings to individual fermion species with permille precision. The forward-backward asymmetries A_FB measure the product of initial- and final-state Z couplings, directly testing the electroweak mixing angle. The left-right asymmetry A_LR at SLD (using polarized electron beams) provides the single most precise determination of sin^2(theta_eff). Together, these measurements form the foundation of the electroweak precision program.

**Vector boson scattering** (VBS) -- processes like WW -> WW, WZ -> WZ, and ZZ -> ZZ -- probes the mechanism of electroweak symmetry breaking at the highest energies. Without the Higgs boson, the scattering amplitude for longitudinal W pairs grows as E^2 and violates unitarity at approximately 1.2 TeV. The Higgs boson restores unitarity through cancellation between s-channel Higgs exchange and the gauge boson self-coupling diagrams. The LHC has observed VBS processes and confirmed the expected energy behavior, but precision tests of the WWWW quartic coupling and searches for anomalous couplings continue to probe whether the Higgs sector is exactly as the Standard Model predicts.
