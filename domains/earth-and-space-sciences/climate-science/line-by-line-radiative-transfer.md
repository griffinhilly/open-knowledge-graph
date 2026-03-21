---
id: line-by-line-radiative-transfer
title: Line-by-Line Radiative Transfer Calculations
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: radiative-transfer-atmospheric
  type: hard
- id: ir-spectroscopy-basics
  type: soft
- id: atmosphere-composition-and-structure
  type: soft
- id: calculus
  type: soft
- id: absorption-and-emission-spectroscopy
  type: soft
builds-toward:
- climate-model-parameterization
- radiative-forcing-greenhouse-gases
tags:
- radiative-transfer
- spectroscopy
- gas-absorption
- climate-modeling
stage: advanced
status: draft
---

# Line-by-Line Radiative Transfer Calculations

## Core Idea
Line-by-line radiative transfer computes the absorption and emission of radiation by resolving the spectral absorption lines of atmospheric gases at high spectral resolution. This approach is computationally intensive but provides the most accurate calculation of radiative fluxes and forcings, serving as a benchmark for validating faster parameterized schemes used in climate models.

## Questions

```yaml
- question: "Why are line-by-line (LBL) radiative transfer models not used as the radiation scheme in general circulation models (GCMs) that simulate global climate?"
  type: multiple-choice
  options:
    - "LBL models are less accurate than the band models currently used in GCMs"
    - "LBL models require spectroscopic databases that are not publicly available"
    - "An LBL calculation must evaluate absorption at millions of spectral points per atmospheric column, making it far too slow for the thousands of columns and time steps in a GCM"
    - "LBL models cannot handle the temperature and pressure variations in the atmosphere"
  answer: 2
  explanation: "A single LBL calculation evaluates absorption at over a million spectral points across 50–100 atmospheric layers — a computationally enormous task. A GCM runs thousands of atmospheric columns at thousands of time steps over months of simulation time. Multiplying these numbers makes direct LBL integration impossible even on modern supercomputers. GCMs therefore use faster approximations (correlated-k, band models) that group absorption lines. LBL models are actually more accurate than band models — that is precisely why they serve as the benchmark for validating the faster schemes."

- question: "What is the primary role of line-by-line calculations in modern climate science, given that they are too slow for GCMs?"
  type: multiple-choice
  options:
    - "They are used to discover new greenhouse gases whose spectral lines have not yet been measured"
    - "They serve as benchmarks to validate the faster radiation parameterization schemes used in GCMs"
    - "They are used to run short-duration climate simulations when the highest possible accuracy is needed"
    - "They replace satellite observations when direct measurements are unavailable"
  answer: 1
  explanation: "LBL calculations serve as the gold standard for accuracy. When a GCM's radiation scheme (using band models or correlated-k methods) computes the radiative forcing from doubled CO₂, that number is trustworthy because it has been validated against LBL results for standardized atmospheric profiles. The benchmark role is essential: without it, climate modelers would not know whether their faster approximations introduce significant errors. LBL models are also used directly in remote sensing retrievals, where spectral precision determines retrieval accuracy."

- question: "Line-by-line radiative transfer models are the most computationally demanding option, but their accuracy is ultimately limited by approximations in the radiative transfer equations they solve."
  type: true-false
  answer: false
  explanation: "The accuracy of LBL models is limited primarily by the completeness and precision of spectroscopic databases (like HITRAN) and by how well the atmospheric temperature and composition profiles are known — not by approximations in the radiative transfer method. The LBL approach itself makes essentially no approximation in the physics: it resolves individual spectral lines and applies Beer-Lambert law and Planck emission layer by layer. The uncertainty lies in the input data (line positions, intensities, broadening parameters) rather than in the mathematical method."

- question: "A line-by-line model evaluates the absorption coefficient at hundreds of thousands to millions of individual spectral points because each atmospheric gas absorbs radiation at many discrete, narrow wavelengths rather than smoothly across broad bands."
  type: true-false
  answer: true
  explanation: "This is exactly right. Each gas molecule (CO₂, H₂O, O₃, CH₄, etc.) transitions between quantized rotational and vibrational energy states at specific, discrete frequencies. These absorption lines are narrow — widths of ~0.1 cm⁻¹ due to pressure broadening — and there are millions of them across the thermal infrared spectrum. A band model that divides the spectrum into broad bins misses the fine structure within each bin. LBL calculations resolve every line individually, requiring spectral points spaced at ~0.001 cm⁻¹ or finer, which is why the number of evaluation points is so enormous."

- question: "Why must an LBL radiative transfer model resolve individual spectral lines at very high spectral resolution rather than grouping absorption into broad wavelength bands?"
  type: short-answer
  answer: "Atmospheric gases absorb radiation at specific discrete frequencies determined by their quantum energy levels, not uniformly across broad bands. Within any broad band, there are regions of very strong absorption (at line centers) and very weak absorption (between lines). Radiation at frequencies near line centers is absorbed near the surface; radiation between lines escapes to space. A broad-band average smooths out this structure and systematically misrepresents the actual flux reaching each altitude. Resolving individual lines captures the real physical behavior — particularly important for optically thick lines of CO₂ and H₂O that dominate the greenhouse effect."
  explanation: "The practical consequence of band averaging is that it introduces systematic errors in computed fluxes that are acceptable for fast GCM runs but unacceptable for a benchmark. For example, the radiative forcing from doubling CO₂ depends on the detailed shape of CO₂ absorption lines in the 15 μm band — specifically, whether the line wings (where absorption is weaker) are correctly represented. Band models parameterize this using the correlated-k method, which works well but introduces approximation errors of a few percent. LBL models eliminate these errors by resolving every line, making them the definitive reference."
```

## Explainer

From your study of atmospheric radiative transfer, you know that the atmosphere absorbs and emits radiation at specific wavelengths determined by the molecular properties of its constituent gases. Each gas — CO₂, H₂O, O₃, CH₄, and others — has a unique set of **absorption lines**, discrete wavelengths at which its molecules transition between rotational and vibrational energy states. The key insight of **line-by-line (LBL) radiative transfer** is that to calculate radiative fluxes with the highest possible accuracy, you must resolve each of these individual spectral lines rather than grouping them into broad bands.

Consider what happens to infrared radiation emitted by Earth's surface as it travels upward through the atmosphere. At each altitude, the radiation encounters gas molecules that absorb at specific frequencies. Whether a photon is absorbed depends on the local concentration of each gas, the temperature (which affects the population of molecular energy states), and the pressure (which broadens absorption lines through collisions). An LBL model evaluates the **absorption coefficient** at each of hundreds of thousands to millions of individual spectral points — typically spaced at intervals of 0.001 cm⁻¹ or finer — across the entire thermal infrared spectrum. At each spectral point and each atmospheric layer, the model applies the **Beer-Lambert law** to calculate how much radiation is absorbed and how much is transmitted, then adds the thermal emission from that layer according to the **Planck function** at the local temperature. The calculation marches through the atmosphere layer by layer, tracking the upward and downward spectral radiance.

The spectroscopic data underlying LBL calculations come from laboratory measurements and quantum mechanical calculations compiled in databases like **HITRAN** (High-Resolution Transmission molecular absorption database). HITRAN catalogs millions of individual absorption lines for dozens of molecular species, specifying each line's center frequency, intensity, and broadening parameters. The accuracy of an LBL calculation is therefore limited primarily by the completeness and precision of these spectroscopic databases and by how well the atmospheric temperature and composition profiles are known — not by approximations in the radiative transfer method itself.

The cost of this accuracy is computational expense. A single LBL calculation of the radiative flux profile through a standard atmosphere may evaluate the absorption coefficient at over a million spectral points across 50–100 atmospheric layers — billions of individual evaluations. This makes LBL calculations far too slow to run at every grid point and every time step of a general circulation model, which is why GCMs use faster approximations called **correlated-k** or **band model** methods that group similar absorption lines together. The critical role of LBL models is as a **benchmark**: radiation parameterization schemes used in GCMs are validated by comparing their outputs against LBL results for standardized atmospheric profiles. When a GCM's radiation scheme computes the radiative forcing from doubled CO₂, the number is trustworthy precisely because it has been checked against LBL calculations that resolve every individual absorption line. LBL models are also used directly in remote sensing retrieval algorithms, where the precision of individual line shapes determines the accuracy of satellite-derived temperature and gas concentration profiles.
