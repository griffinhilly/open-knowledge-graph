---
id: luminosity-and-event-rates
title: Luminosity and Event Rates
domain: physics
course: particle-physics
prerequisites:
- id: cross-section-measurements
  type: hard
tags:
- luminosity
- event-rates
- collider-parameters
- van-der-meer-scan
stage: expert
status: validated
---

# Luminosity and Event Rates

## Core Idea
Luminosity is the proportionality constant between a process's cross section and its event rate: dN/dt = L * sigma. The instantaneous luminosity depends on the beam parameters (number of particles per bunch, bunch frequency, beam size), while the integrated luminosity (integral of L over time) determines the total number of events collected. Precise luminosity measurement (currently ~1-2% at the LHC) is essential because it directly scales every cross section measurement.

## Questions

```yaml
- question: "The LHC design luminosity is 10^{34} cm^{-2} s^{-1}. The total inelastic proton-proton cross section at 13 TeV is approximately 80 mb = 80 x 10^{-27} cm^2. How many inelastic collisions occur per second, and what does this imply for the detector?"
  type: multiple-choice
  options:
    - "About 80 collisions per second, which is easily manageable"
    - "About 8 x 10^8 (800 million) collisions per second — with 2808 bunches crossing at 40 MHz, this corresponds to approximately 20-50 simultaneous collisions per bunch crossing (pileup), which the detectors must be designed to handle"
    - "About 10^{34} collisions per second"
    - "About 10^{10} collisions per second, but most are filtered by the trigger"
  answer: 1
  explanation: "dN/dt = L * sigma = 10^{34} * 80 x 10^{-27} = 8 x 10^8 per second. Divided among ~3000 filled bunches crossing at 40 MHz, this gives ~25 interactions per bunch crossing at design luminosity (pileup <mu> ~ 25). At Run 2/3, <mu> reached 30-60. Each pileup interaction produces ~30 charged particles, so the detector must reconstruct the physics objects from ~1000 tracks per bunch crossing while rejecting the pileup contribution. The HL-LHC will operate at <mu> ~ 200, requiring major detector upgrades."

- question: "Luminosity at the LHC is calibrated using van der Meer (vdM) scans. How does this calibration work?"
  type: short-answer
  answer: "In a van der Meer scan, the two beams are deliberately displaced transversely (in x and y) while monitoring the collision rate. The rate as a function of beam separation traces out the beam overlap profile. The peak rate and the effective beam widths (Sigma_x, Sigma_y) determine the luminosity through L = f_rev * n_b * N_1 * N_2 / (2*pi * Sigma_x * Sigma_y), where f_rev is the revolution frequency, n_b is the number of colliding bunch pairs, and N_1, N_2 are the bunch populations. This method directly measures the beam overlap without assumptions about the beam shape. The calibration is transferred to online luminosity monitors (luminosity detectors counting collision products) that then track the luminosity during physics running. The dominant uncertainties are from beam-beam effects, bunch population measurements, and non-Gaussian beam tails, achieving ~1-2% total uncertainty."
  explanation: "The vdM technique was invented by Simon van der Meer (who also invented stochastic cooling, enabling the SppS and the W/Z discovery). It remains the primary absolute luminosity calibration method at all hadron colliders."

- question: "The HL-LHC (High-Luminosity LHC) aims to deliver 3000 fb^{-1} of integrated luminosity, compared to ~300 fb^{-1} from the LHC Runs 1-3 combined. Why does a factor of 10 more data significantly extend the physics reach?"
  type: multiple-choice
  options:
    - "Because all measurements improve by a factor of 10"
    - "Because statistical sensitivity scales as sqrt(L) for discovery (so 10x more data gives ~3x better significance for rare signals) and as 1/sqrt(L) for statistical uncertainties on measured quantities — additionally, more data enables measurements of extremely rare processes (Higgs self-coupling, rare Higgs decays) that require thousands of signal events to be observable above background"
    - "Because the beam energy also increases by a factor of 10"
    - "Because systematic uncertainties decrease proportionally to the luminosity"
  answer: 1
  explanation: "For a signal of S events on a background of B events, the significance goes as S/sqrt(B) proportional to sqrt(L). So 10x more luminosity gives ~3x better significance. This is crucial for rare processes: di-Higgs production (sigma ~ 31 fb at 14 TeV) yields ~100 events in 3000 fb^{-1}, barely enough for observation. Precision measurements of Higgs couplings improve as 1/sqrt(L) (for statistically limited channels) or plateau (for systematically limited ones). The HL-LHC is designed to exploit the full statistical potential of the LHC energy frontier."
```

## Explainer

**Luminosity** is the fundamental metric that converts theoretical cross sections into observable event counts. For a collider, the instantaneous luminosity depends on the machine parameters: L = f * n_b * N_1 * N_2 / (4*pi * sigma_x * sigma_y), where f is the revolution frequency, n_b is the number of colliding bunches, N_1 and N_2 are the particles per bunch, and sigma_x, sigma_y are the transverse beam sizes at the interaction point. The LHC achieves its high luminosity through ~10^{11} protons per bunch, ~2800 bunches, and beam sizes squeezed to ~15 micrometers at the interaction points.

**Integrated luminosity** L_int = integral(L dt) is typically quoted in inverse femtobarns (fb^{-1}) at the LHC. One fb^{-1} means that a process with a cross section of 1 fb would produce on average one event. The LHC Run 2 (2015-2018) delivered about 140 fb^{-1} per experiment at 13 TeV. For context: the W boson production cross section is ~200 nb, so Run 2 produced ~30 billion W bosons. Higgs production (via gluon fusion) has a cross section of ~50 pb, yielding ~7 million Higgs bosons. But with branching ratios (H -> gamma gamma is 0.2%) and detection efficiencies (typically 30-50%), the observed signal events number in the thousands for Higgs and even fewer for rarer processes.

**Pileup** is the unavoidable consequence of high luminosity: at the LHC, 20-60 proton-proton collisions occur in each bunch crossing, and only one (or occasionally two) produce the hard-scattering event of interest. The remaining "minimum-bias" events deposit energy in the calorimeters, produce tracks in the tracker, and generally degrade the measurement resolution. Pileup mitigation techniques -- vertex identification, charged-hadron subtraction, jet trimming, PUPPI -- are critical for maintaining physics performance. At the HL-LHC (<mu> ~ 200), new timing detectors will measure particle arrival times with ~30 ps precision, enabling separation of vertices along the z-axis and in time.

The **luminosity uncertainty** is a correlated systematic that affects every cross section measurement at a collider. At the LHC, it has been reduced from ~5% in early Run 1 to ~1.2% in Run 2 through improved van der Meer scan techniques, better beam instrumentation, and cross-calibration between multiple luminosity detectors. For precision measurements (such as the W mass or inclusive Z cross section), the luminosity uncertainty is often the dominant systematic. At future e+e- colliders, luminosity can be measured to ~0.1% or better using low-angle Bhabha scattering, enabling percent-level precision on absolute cross sections.
