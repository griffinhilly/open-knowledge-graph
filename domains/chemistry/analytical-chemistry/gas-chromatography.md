---
id: gas-chromatography
title: Gas Chromatography (GC)
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: chromatography-fundamentals
  type: hard
- id: intermolecular-forces
  type: soft
- id: kinetic-theory-of-gases
  type: soft
- id: diffusion-and-ficks-laws
  type: soft
tags:
- GC
- gas chromatography
- FID
- temperature programming
- capillary column
- headspace
stage: advanced
status: validated
---

# Gas Chromatography (GC)

## Core Idea
Gas chromatography separates volatile compounds by partitioning between an inert carrier gas (mobile phase) and a liquid or solid stationary phase in a heated column. Retention depends on boiling point and stationary phase polarity; temperature programming improves separation of wide-boiling-range mixtures. Detectors include the flame ionization detector (FID, universal for hydrocarbons), thermal conductivity detector (TCD, universal), and electron capture detector (ECD, highly sensitive for halogenated compounds). GC–MS coupling provides both separation power and mass spectral identification.

## How It's Best Learned
Separate and quantify a mixture of volatile organic compounds using an internal standard method. Comparing isothermal and temperature-programmed runs demonstrates the resolution–analysis time trade-off, while changing the stationary phase polarity shows how elution order can be reversed.

## Common Misconceptions
- GC requires volatile analytes; non-volatile compounds must be derivatized (e.g., silylation of fatty acids) before injection.
- Carrier gas flow rate affects both efficiency and retention time — changing the flow rate is not simply a speed adjustment but alters column performance.

## Explainer

Gas chromatography works by exploiting a simple physical principle: different volatile compounds spend different amounts of time dissolved in a liquid coating versus riding in a gas stream. From your chromatography fundamentals prerequisite, you know that separation requires a mobile phase that carries analytes through a stationary phase, and that compounds which interact more strongly with the stationary phase elute later. In GC, the mobile phase is an inert **carrier gas** — typically helium or hydrogen — and the stationary phase is a thin liquid film coated on the inner wall of a long, narrow capillary column housed inside a temperature-controlled oven.

Two properties primarily determine how long a compound stays on the column: its **boiling point** and its **polarity relative to the stationary phase**. Low-boiling compounds spend more time in the gas phase and elute first; high-boiling compounds dissolve more readily in the stationary phase liquid and elute later. Polarity adds a second dimension — a polar stationary phase (like polyethylene glycol) retains polar analytes more strongly, while a nonpolar phase (like polydimethylsiloxane) retains nonpolar analytes. By choosing the right stationary phase, you can tune selectivity to separate compounds that have similar boiling points but different polarities, or even reverse elution order entirely.

**Temperature programming** is the most powerful tool for handling real-world samples. If you run the oven at a single temperature (isothermal), low-boiling compounds elute quickly as sharp peaks while high-boiling compounds elute slowly as broad, barely detectable humps — or never elute at all. By ramping the oven temperature during the run, you give every compound an optimized elution window: early-eluting compounds separate well at the initial low temperature, and late-eluting compounds are pushed off the column as the temperature rises. This is conceptually analogous to gradient elution in HPLC, except you are changing temperature instead of mobile phase composition.

Detection is where GC becomes quantitative. The **flame ionization detector (FID)** burns the column effluent in a hydrogen flame and measures the resulting ion current — it responds to virtually all organic compounds proportionally to their carbon content, making it the default workhorse for quantitative organic analysis. The **thermal conductivity detector (TCD)** measures the carrier gas thermal conductivity change when an analyte is present, and responds to all compounds including inorganics and permanent gases, though with lower sensitivity. For specialized applications, the **electron capture detector (ECD)** provides extraordinary sensitivity for halogenated compounds like pesticides and PCBs. Coupling GC to a mass spectrometer (**GC-MS**) provides both separation and definitive identification from mass spectral fragmentation patterns — it is the gold standard for environmental analysis, forensic toxicology, and flavor chemistry.
