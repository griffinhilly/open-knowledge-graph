---
id: voltammetry
title: Voltammetry and Polarography
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: potentiometry
  type: hard
- id: electrochemical-kinetics
  type: soft
- id: diffusion-and-ficks-laws
  type: soft
- id: electric-potential
  type: soft
- id: electric-current-and-resistance
  type: soft
- id: rc-circuits
  type: soft
tags:
- voltammetry
- cyclic voltammetry
- differential pulse
- stripping analysis
- limiting current
stage: advanced
status: validated
---

# Voltammetry and Polarography

## Core Idea
Voltammetry applies a controlled, time-varying potential to an electrochemical cell and measures the resulting current; analytical information is contained in characteristic peak (or half-wave) potentials and limiting currents proportional to analyte concentration. Cyclic voltammetry (CV) probes redox mechanism and reversibility by scanning potential in both directions. Differential pulse and square wave voltammetry enhance sensitivity by subtracting background capacitive current. Anodic stripping voltammetry (ASV) preconcentrates trace metals onto an electrode by deposition, then strips them to give ppt-level detection limits.

## How It's Best Learned
Record CV of ferricyanide/ferrocyanide at different scan rates to extract diffusion coefficients and assess reversibility using the Randles–Ševčík equation. Then determine Pb²⁺ and Cd²⁺ simultaneously by ASV to experience multi-element capability at trace levels.

## Common Misconceptions
- The peak current in cyclic voltammetry increases with scan rate (proportional to √ν for diffusion-controlled processes) — this is often confused with the idea that faster is more sensitive.
- A symmetric CV peak does not prove electrochemical reversibility — it must also satisfy Ep,a − Ep,c = 59/n mV at all scan rates.

## Questions

```yaml
- question: "In a cyclic voltammetry experiment, you double the scan rate and observe that the peak current increases by a factor of approximately 1.41 (√2). What does this tell you about the process?"
  type: multiple-choice
  options:
    - "The reaction is irreversible because peak current depends on scan rate"
    - "The electrode is becoming saturated at faster scan rates"
    - "The process is diffusion-controlled, since peak current scales with the square root of scan rate (Randles–Ševčík behavior)"
    - "The analyte concentration decreased during the experiment"
  answer: 2
  explanation: "For a diffusion-controlled process, the Randles–Ševčík equation gives ip ∝ √ν. Doubling the scan rate increases √ν by √2 ≈ 1.41, which is exactly what was observed. This behavior arises because at faster scan rates the diffusion layer is thinner — reactant has less time to be depleted near the surface — so more current flows. Scan-rate dependence itself does not indicate irreversibility; irreversibility is diagnosed by peak separation exceeding 59/n mV."

- question: "What is the primary purpose of the deposition step in anodic stripping voltammetry (ASV)?"
  type: multiple-choice
  options:
    - "To clean and activate the electrode surface before analysis"
    - "To measure background capacitive current so it can be subtracted during the stripping scan"
    - "To electroplate trace metal ions from a large solution volume onto the electrode, concentrating the analyte by orders of magnitude"
    - "To determine which metals are present by observing their reduction potentials during deposition"
  answer: 2
  explanation: "The deposition step is the source of ASV's extraordinary sensitivity. By holding the electrode at a very negative potential for several minutes, metal ions from a large volume of solution are electroplated onto a tiny electrode surface — concentrating parts-per-trillion analyte into a detectable quantity. When the potential is swept positively, each metal strips off at its characteristic potential, releasing minutes of accumulation in seconds. The signal amplification from this preconcentration step is what enables ppt detection limits impossible with direct CV."

- question: "A cyclic voltammogram shows a perfectly symmetrical pair of peaks — the anodic and cathodic peaks are mirror images of each other. This symmetry proves that the redox reaction is electrochemically reversible."
  type: true-false
  answer: false
  explanation: "Symmetry of peak shape is a necessary but not sufficient condition for reversibility. True electrochemical reversibility also requires that the peak separation (Ep,a − Ep,c) equals exactly 59/n mV at all scan rates. If the separation is larger than 59/n mV or increases with scan rate, electron transfer kinetics are sluggish (quasi-reversible or irreversible) even if the peaks look symmetric. Both criteria must be satisfied: correct peak separation AND scan-rate independence of that separation."

- question: "Differential pulse voltammetry achieves lower detection limits than simple cyclic voltammetry primarily because it reduces the capacitive (charging) current relative to the faradaic (reaction) current."
  type: true-false
  answer: true
  explanation: "The fundamental noise floor in electroanalytical measurements is set by capacitive current — the current that flows when the electrode double layer charges and discharges as the potential is scanned. This current is not related to the analyte and cannot be reduced by increasing sample concentration. Differential pulse methods sample current at specific points in a pulse cycle (end of pulse, when capacitive current has decayed exponentially but faradaic current remains) and subtract pairs of measurements to cancel the capacitive background. The result is a dramatic improvement in signal-to-noise for the analyte peak."

- question: "In cyclic voltammetry, why does the current peak and then decline as the potential sweep continues past the reduction potential? What physical process drives this peak shape?"
  type: short-answer
  answer: "As the potential reaches the reduction potential, analyte molecules at the electrode surface are reduced rapidly, generating a large current. But those surface molecules are quickly consumed and must be replenished by diffusion from the bulk solution. Diffusion is slow compared to the electrochemical reaction, so a depletion zone (diffusion layer) builds up near the electrode surface. As the diffusion layer thickens, fresh analyte must travel ever-increasing distances to reach the electrode, and the rate of arrival (and thus the current) falls. The peak marks the point where the reduction rate transitions from being limited by electrode kinetics to being limited by diffusion transport."
  explanation: "The peak shape is entirely a consequence of mass transport. Students often assume more negative potential should drive more current indefinitely, but the current is bounded by how fast analyte can arrive at the electrode surface. This is why peak current depends on √ν (diffusion rate scales with scan rate) and why peak current is proportional to concentration (more analyte diffuses to the surface per unit time)."
```

## Explainer

In potentiometry — your prerequisite — you measured the potential of an electrochemical cell at equilibrium while drawing essentially no current. Voltammetry flips this strategy: you deliberately **force the electrode potential** to change over time and then measure the current that flows as electroactive species are oxidized or reduced at the electrode surface. The current-versus-potential curve (called a **voltammogram**) encodes both qualitative information (what species are present, via their characteristic peak potentials) and quantitative information (how much is present, via peak or limiting current magnitudes).

The simplest experiment to understand is **cyclic voltammetry (CV)**. You start at a potential where nothing happens, sweep linearly to a more negative (or positive) potential, then reverse direction and sweep back. On the forward sweep, when the potential reaches the reduction potential of your analyte, current rises as molecules at the electrode surface are reduced. But the supply of reactant near the surface is finite — molecules must diffuse in from the bulk solution. This creates a peak: current rises as reduction begins, then falls as the **diffusion layer** thickens and fresh reactant can no longer reach the surface fast enough. On the reverse sweep, the reduced product sitting near the electrode is re-oxidized, producing a mirror-image peak. For a fully **reversible** reaction, the separation between the forward and reverse peaks is exactly 59/n millivolts (where n is the number of electrons transferred), and this separation stays constant regardless of how fast you scan. Deviations from this ideal reveal sluggish electron transfer kinetics, chemical reactions coupled to the electron transfer, or adsorption effects.

For analytical quantitation, CV is often too noisy because a large **capacitive current** (charging of the electrical double layer at the electrode surface) rides underneath the signal of interest. **Differential pulse voltammetry** and **square-wave voltammetry** solve this by applying small potential pulses superimposed on the sweep and sampling current at the end of each pulse, when the capacitive current has decayed but the faradaic (reaction) current persists. Subtracting currents measured at different points in the pulse cycle cancels the background, yielding sharp, well-defined peaks with detection limits orders of magnitude better than simple CV.

For trace-level analysis — parts per billion or below — **anodic stripping voltammetry (ASV)** adds a preconcentration step. First, you hold the electrode at a very negative potential for several minutes, electroplating trace metal ions (Pb²⁺, Cd²⁺, Cu²⁺) from a large volume of solution onto a tiny mercury or bismuth film electrode. Then you sweep the potential positively, stripping each metal back into solution at its characteristic potential. Because minutes of accumulation are released in seconds, the signal is enormously amplified. The stripping peak area is proportional to concentration, and different metals strip at different potentials, allowing simultaneous multi-element detection at concentrations as low as parts per trillion.
