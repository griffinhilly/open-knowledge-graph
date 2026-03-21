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

## Questions

```yaml
- question: "A polarographic experiment measures Cd²⁺ in 1 M KCl, finding E₁/₂ = −0.40 V. The supporting electrolyte is then changed to 0.1 M HNO₃. What should the experimenter expect?"
  type: multiple-choice
  options:
    - "E₁/₂ remains at −0.40 V because it is a fixed property of cadmium"
    - "E₁/₂ shifts because the half-wave potential depends on the analyte–electrolyte system, not the analyte alone"
    - "E₁/₂ disappears entirely because cadmium cannot be reduced in nitric acid"
    - "The diffusion current changes but E₁/₂ stays constant"
  answer: 1
  explanation: "E₁/₂ is characteristic of the analyte in a specific supporting electrolyte, not of the analyte alone. Complexation equilibria, activity coefficients, and pH all affect the formal reduction potential in solution, shifting E₁/₂. This is why reference tables specify both the analyte and the supporting electrolyte. Option A is the classic misconception — treating E₁/₂ as an intrinsic property of the element rather than a system-dependent parameter."

- question: "In a DC polarogram, why does the current plateau at the limiting diffusion current (id) rather than continuing to rise as potential becomes more negative?"
  type: multiple-choice
  options:
    - "The electrode becomes fully coated with reduced metal, blocking further reaction"
    - "Every analyte molecule arriving at the electrode surface is immediately reduced, so the rate is set by diffusion, not electrode kinetics"
    - "The mercury drop falls off before higher currents can develop"
    - "Capacitive charging current cancels the faradaic current at very negative potentials"
  answer: 1
  explanation: "At potentials on the limiting-current plateau, the reduction is so thermodynamically favorable that every analyte ion reaching the electrode surface reacts instantly. The current is no longer limited by electrode kinetics but by the rate at which analyte can diffuse from the bulk solution to the surface — a mass-transport limit. Because diffusion rate is fixed by concentration gradient and the diffusion coefficient, the current stops rising even as potential becomes more negative. The Ilkovic equation quantifies this diffusion-limited rate, which is why id is proportional to concentration."

- question: "The primary analytical advantage of the dropping mercury electrode is that each new drop provides a fresh, uncontaminated surface, eliminating memory effects from previous measurements."
  type: true-false
  answer: true
  explanation: "Surface renewal is the DME's defining advantage. Solid electrodes accumulate adsorbed products, oxide films, and surface contamination that alter their behavior over time, requiring frequent reconditioning. The DME circumvents this by discarding the old drop every few seconds and growing a pristine mercury surface. This gives exceptional reproducibility from drop to drop and explains why polarography remains the reference method for certain trace metal analyses despite mercury's toxicity."

- question: "The half-wave potential measured for cadmium in 1 M KCl is an intrinsic property of cadmium ions and remains the same regardless of the supporting electrolyte used."
  type: true-false
  answer: false
  explanation: "E₁/₂ depends on the complete analyte–electrolyte system. The supporting electrolyte affects the formal reduction potential through complexation (Cd²⁺ forms chloro-complexes in KCl), ionic strength, activity coefficients, and pH. Changing from 1 M KCl to 1 M NH₄OH, for example, would shift E₁/₂ substantially because cadmium forms amine complexes in ammonia. This system dependence is why half-wave potential tables always specify the electrolyte conditions."

- question: "Why does mercury provide a wider cathodic potential window than solid platinum or carbon electrodes?"
  type: short-answer
  answer: "Mercury has an exceptionally high overpotential for hydrogen evolution — it requires a much more negative potential to reduce H⁺ to H₂ than platinum or carbon do. This means you can scan to approximately −2.0 V versus SCE in many supporting electrolytes without the background current from hydrogen evolution interfering. Platinum and carbon catalyze hydrogen evolution more readily, so they produce interfering background currents at much less negative potentials, limiting how far into the cathodic range you can probe."
  explanation: "The cathodic window is determined by the competing reduction of the solvent or supporting electrolyte. For aqueous solutions, this is usually hydrogen evolution (2H⁺ + 2e⁻ → H₂). Mercury's high hydrogen evolution overpotential is a kinetic barrier — the reaction is thermodynamically favorable but kinetically sluggish on mercury surfaces, suppressing the background current and allowing measurement of analyte reductions at very negative potentials. This unique property makes polarography ideal for reducing metal ions like Zn²⁺, Cd²⁺, and Pb²⁺ that require strongly negative potentials."
```

## Explainer

From your study of voltammetry, you understand the general principle: sweep the potential of a working electrode and measure the current that flows as electroactive species are reduced or oxidized at the surface. Polarography is a specific implementation of this principle that uses a **dropping mercury electrode (DME)** — a fine glass capillary from which mercury flows in a continuous stream of small drops, each falling away after a few seconds and being replaced by a fresh one. This seemingly quirky arrangement solves several fundamental problems that plague solid electrodes.

The first advantage is **surface renewal**. Every few seconds, the old mercury drop falls away and a pristine new surface forms. This means the electrode has no memory of previous measurements — no adsorbed products, no oxide films, no surface contamination. A solid platinum or carbon electrode gradually accumulates reaction products that change its behavior over time, requiring polishing and reconditioning. The DME renews itself automatically, giving extraordinary reproducibility from drop to drop and from day to day. The second advantage is mercury's **wide cathodic potential window**. Mercury is very difficult to reduce (its overpotential for hydrogen evolution is exceptionally high), so you can scan to very negative potentials — around −2.0 V versus SCE in many supporting electrolytes — without the electrode itself interfering. This cathodic range makes polarography ideal for reducing metal ions like Zn²⁺, Cd²⁺, Pb²⁺, and Tl⁺ that are difficult to measure at other electrodes.

As you scan the potential from mild to increasingly negative values, the current follows a characteristic **sigmoidal (S-shaped) curve** called a polarographic wave. At potentials far from the reduction potential of the analyte, no current flows. As the potential approaches E₁/₂, the analyte begins to reduce at the mercury surface and current rises. Eventually, every analyte ion arriving at the electrode surface is immediately reduced, and the current plateaus at the **diffusion-limited current** (id) — the maximum rate at which the analyte can diffuse from the bulk solution to the electrode. The **Ilkovic equation** relates this diffusion current to the analyte concentration, diffusion coefficient, mercury flow rate, and drop time, providing a direct theoretical link between the measured current and the amount of analyte present.

The **half-wave potential** (E₁/₂) — the potential at the midpoint of the sigmoidal wave — serves as a qualitative identifier, analogous to a chromatographic retention time. Each metal ion in a given supporting electrolyte has a characteristic E₁/₂ value. If your polarogram shows waves at −0.40 V and −0.60 V in 1 M KCl, you can identify them as cadmium and nickel by consulting tables of half-wave potentials. Modern pulse techniques like **differential pulse polarography** improve sensitivity by sampling current only at the end of each drop's life (when the capacitive charging current has decayed) and applying a small potential pulse superimposed on the linear ramp. This suppresses background noise and lowers detection limits from micromolar to nanomolar concentrations, keeping polarography relevant for trace metal analysis despite the environmental concerns surrounding mercury use.
