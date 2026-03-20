---
id: polarography
title: Polarography
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: voltammetry
  type: hard
tags:
- polarography
- dropping mercury electrode
- DME
- Ilkovic equation
- half-wave potential
- diffusion current
- mercury
stage: advanced
status: draft
---

# Polarography

## Core Idea
Polarography is a specialized form of voltammetry that uses a dropping mercury electrode (DME) as the working electrode, exploiting mercury's unique properties: a constantly renewed, atomically smooth surface that eliminates memory effects, a wide cathodic potential window (mercury is difficult to reduce), and highly reproducible drop characteristics. As potential is scanned linearly, a sigmoidal current-voltage curve (polarographic wave) develops, with the half-wave potential (E₁/₂) identifying the analyte and the diffusion-limited current (id) being proportional to concentration. The Ilkovic equation relates the diffusion current to concentration, diffusion coefficient, mercury flow rate, and drop time, providing a theoretical basis for quantitative analysis without empirical calibration.

## How It's Best Learned
Record a DC polarogram of Cd²⁺ or Zn²⁺ in a supporting electrolyte, measure E₁/₂ and the limiting current, then vary concentration to verify linearity predicted by the Ilkovic equation. Comparing DC, sampled-DC, and differential-pulse modes on the same solution demonstrates how modern pulse techniques improve sensitivity by suppressing capacitive current.

## Common Misconceptions
- The dropping mercury electrode is not obsolete simply because mercury is toxic; it remains the reference technique for certain applications because no other electrode material provides the same cathodic range and surface reproducibility.
- The half-wave potential is characteristic of the analyte-supporting electrolyte system, not of the analyte alone — changing the supporting electrolyte or pH shifts E₁/₂.

## Explainer

From your study of voltammetry, you understand the general principle: sweep the potential of a working electrode and measure the current that flows as electroactive species are reduced or oxidized at the surface. Polarography is a specific implementation of this principle that uses a **dropping mercury electrode (DME)** — a fine glass capillary from which mercury flows in a continuous stream of small drops, each falling away after a few seconds and being replaced by a fresh one. This seemingly quirky arrangement solves several fundamental problems that plague solid electrodes.

The first advantage is **surface renewal**. Every few seconds, the old mercury drop falls away and a pristine new surface forms. This means the electrode has no memory of previous measurements — no adsorbed products, no oxide films, no surface contamination. A solid platinum or carbon electrode gradually accumulates reaction products that change its behavior over time, requiring polishing and reconditioning. The DME renews itself automatically, giving extraordinary reproducibility from drop to drop and from day to day. The second advantage is mercury's **wide cathodic potential window**. Mercury is very difficult to reduce (its overpotential for hydrogen evolution is exceptionally high), so you can scan to very negative potentials — around −2.0 V versus SCE in many supporting electrolytes — without the electrode itself interfering. This cathodic range makes polarography ideal for reducing metal ions like Zn²⁺, Cd²⁺, Pb²⁺, and Tl⁺ that are difficult to measure at other electrodes.

As you scan the potential from mild to increasingly negative values, the current follows a characteristic **sigmoidal (S-shaped) curve** called a polarographic wave. At potentials far from the reduction potential of the analyte, no current flows. As the potential approaches E₁/₂, the analyte begins to reduce at the mercury surface and current rises. Eventually, every analyte ion arriving at the electrode surface is immediately reduced, and the current plateaus at the **diffusion-limited current** (id) — the maximum rate at which the analyte can diffuse from the bulk solution to the electrode. The **Ilkovic equation** relates this diffusion current to the analyte concentration, diffusion coefficient, mercury flow rate, and drop time, providing a direct theoretical link between the measured current and the amount of analyte present.

The **half-wave potential** (E₁/₂) — the potential at the midpoint of the sigmoidal wave — serves as a qualitative identifier, analogous to a chromatographic retention time. Each metal ion in a given supporting electrolyte has a characteristic E₁/₂ value. If your polarogram shows waves at −0.40 V and −0.60 V in 1 M KCl, you can identify them as cadmium and nickel by consulting tables of half-wave potentials. Modern pulse techniques like **differential pulse polarography** improve sensitivity by sampling current only at the end of each drop's life (when the capacitive charging current has decayed) and applying a small potential pulse superimposed on the linear ramp. This suppresses background noise and lowers detection limits from micromolar to nanomolar concentrations, keeping polarography relevant for trace metal analysis despite the environmental concerns surrounding mercury use.
