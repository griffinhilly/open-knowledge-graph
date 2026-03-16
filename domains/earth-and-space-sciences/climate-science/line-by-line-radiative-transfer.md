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

## Explainer

From your study of atmospheric radiative transfer, you know that the atmosphere absorbs and emits radiation at specific wavelengths determined by the molecular properties of its constituent gases. Each gas — CO₂, H₂O, O₃, CH₄, and others — has a unique set of **absorption lines**, discrete wavelengths at which its molecules transition between rotational and vibrational energy states. The key insight of **line-by-line (LBL) radiative transfer** is that to calculate radiative fluxes with the highest possible accuracy, you must resolve each of these individual spectral lines rather than grouping them into broad bands.

Consider what happens to infrared radiation emitted by Earth's surface as it travels upward through the atmosphere. At each altitude, the radiation encounters gas molecules that absorb at specific frequencies. Whether a photon is absorbed depends on the local concentration of each gas, the temperature (which affects the population of molecular energy states), and the pressure (which broadens absorption lines through collisions). An LBL model evaluates the **absorption coefficient** at each of hundreds of thousands to millions of individual spectral points — typically spaced at intervals of 0.001 cm⁻¹ or finer — across the entire thermal infrared spectrum. At each spectral point and each atmospheric layer, the model applies the **Beer-Lambert law** to calculate how much radiation is absorbed and how much is transmitted, then adds the thermal emission from that layer according to the **Planck function** at the local temperature. The calculation marches through the atmosphere layer by layer, tracking the upward and downward spectral radiance.

The spectroscopic data underlying LBL calculations come from laboratory measurements and quantum mechanical calculations compiled in databases like **HITRAN** (High-Resolution Transmission molecular absorption database). HITRAN catalogs millions of individual absorption lines for dozens of molecular species, specifying each line's center frequency, intensity, and broadening parameters. The accuracy of an LBL calculation is therefore limited primarily by the completeness and precision of these spectroscopic databases and by how well the atmospheric temperature and composition profiles are known — not by approximations in the radiative transfer method itself.

The cost of this accuracy is computational expense. A single LBL calculation of the radiative flux profile through a standard atmosphere may evaluate the absorption coefficient at over a million spectral points across 50–100 atmospheric layers — billions of individual evaluations. This makes LBL calculations far too slow to run at every grid point and every time step of a general circulation model, which is why GCMs use faster approximations called **correlated-k** or **band model** methods that group similar absorption lines together. The critical role of LBL models is as a **benchmark**: radiation parameterization schemes used in GCMs are validated by comparing their outputs against LBL results for standardized atmospheric profiles. When a GCM's radiation scheme computes the radiative forcing from doubled CO₂, the number is trustworthy precisely because it has been checked against LBL calculations that resolve every individual absorption line. LBL models are also used directly in remote sensing retrieval algorithms, where the precision of individual line shapes determines the accuracy of satellite-derived temperature and gas concentration profiles.
