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

## Explainer

In potentiometry — your prerequisite — you measured the potential of an electrochemical cell at equilibrium while drawing essentially no current. Voltammetry flips this strategy: you deliberately **force the electrode potential** to change over time and then measure the current that flows as electroactive species are oxidized or reduced at the electrode surface. The current-versus-potential curve (called a **voltammogram**) encodes both qualitative information (what species are present, via their characteristic peak potentials) and quantitative information (how much is present, via peak or limiting current magnitudes).

The simplest experiment to understand is **cyclic voltammetry (CV)**. You start at a potential where nothing happens, sweep linearly to a more negative (or positive) potential, then reverse direction and sweep back. On the forward sweep, when the potential reaches the reduction potential of your analyte, current rises as molecules at the electrode surface are reduced. But the supply of reactant near the surface is finite — molecules must diffuse in from the bulk solution. This creates a peak: current rises as reduction begins, then falls as the **diffusion layer** thickens and fresh reactant can no longer reach the surface fast enough. On the reverse sweep, the reduced product sitting near the electrode is re-oxidized, producing a mirror-image peak. For a fully **reversible** reaction, the separation between the forward and reverse peaks is exactly 59/n millivolts (where n is the number of electrons transferred), and this separation stays constant regardless of how fast you scan. Deviations from this ideal reveal sluggish electron transfer kinetics, chemical reactions coupled to the electron transfer, or adsorption effects.

For analytical quantitation, CV is often too noisy because a large **capacitive current** (charging of the electrical double layer at the electrode surface) rides underneath the signal of interest. **Differential pulse voltammetry** and **square-wave voltammetry** solve this by applying small potential pulses superimposed on the sweep and sampling current at the end of each pulse, when the capacitive current has decayed but the faradaic (reaction) current persists. Subtracting currents measured at different points in the pulse cycle cancels the background, yielding sharp, well-defined peaks with detection limits orders of magnitude better than simple CV.

For trace-level analysis — parts per billion or below — **anodic stripping voltammetry (ASV)** adds a preconcentration step. First, you hold the electrode at a very negative potential for several minutes, electroplating trace metal ions (Pb²⁺, Cd²⁺, Cu²⁺) from a large volume of solution onto a tiny mercury or bismuth film electrode. Then you sweep the potential positively, stripping each metal back into solution at its characteristic potential. Because minutes of accumulation are released in seconds, the signal is enormously amplified. The stripping peak area is proportional to concentration, and different metals strip at different potentials, allowing simultaneous multi-element detection at concentrations as low as parts per trillion.
