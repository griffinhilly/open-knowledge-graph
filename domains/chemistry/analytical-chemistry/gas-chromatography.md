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

## Questions

```yaml
- question: "A chemist needs to separate a mixture of compounds that have very similar boiling points but different polarities. Which strategy would most effectively improve resolution?"
  type: multiple-choice
  options:
    - "Apply temperature programming to ramp the oven temperature during the run"
    - "Increase the carrier gas flow rate to sharpen peak shape"
    - "Switch to a stationary phase whose polarity strongly matches some analytes but not others, exploiting differential polar interactions to separate what boiling point alone cannot"
    - "Use a longer column with the same stationary phase to give more theoretical plates"
  answer: 2
  explanation: "When compounds have similar boiling points, temperature programming cannot selectively resolve them — they will still co-elute at nearly the same temperature. Stationary phase polarity is the key second dimension of selectivity. A polar stationary phase (like PEG/Carbowax) retains polar analytes through dipole-dipole and hydrogen bonding interactions far more than it retains nonpolar analytes of similar boiling point — effectively pulling apart compounds that boiling point cannot separate. Choosing a 'like dissolves like' stationary phase that differentially retains your target analytes is the first tool for improving selectivity. A longer column increases efficiency (plates) but won't separate compounds if the selectivity (α) is essentially 1.0."

- question: "A forensic chemist analyzing environmental water samples needs to detect trace levels of organochlorine pesticides (e.g., DDT, lindane). Which GC detector should they choose?"
  type: multiple-choice
  options:
    - "Flame ionization detector (FID) — provides universal response to all organic compounds and is the standard workhorse detector"
    - "Thermal conductivity detector (TCD) — responds to all compounds including inorganics and provides the best overall sensitivity"
    - "Electron capture detector (ECD) — provides extraordinary sensitivity specifically for halogenated compounds, making trace-level organochlorine detection practical"
    - "Any detector works equally well; detector choice only affects analysis speed"
  answer: 2
  explanation: "Detector selection is application-driven. The ECD responds to compounds with high electron affinity — especially halogenated compounds — with sensitivity orders of magnitude higher than the FID or TCD for these analytes. FID is universal for organic carbon but is relatively insensitive to halogenated compounds because the halogens reduce ionization efficiency. TCD has even lower sensitivity than FID for trace analysis. For organochlorine pesticides at parts-per-trillion levels in environmental matrices, ECD is the appropriate choice. Its high selectivity for halogens also simplifies chromatograms from complex matrices — many non-halogenated matrix components don't respond at all. For definitive identification (not just detection), GC-MS would be the gold standard."

- question: "In gas chromatography, compounds elute in order of increasing molecular weight — lighter molecules travel faster through the column and appear as earlier peaks."
  type: true-false
  answer: false
  explanation: "Elution order in GC is determined by boiling point and polarity interactions with the stationary phase, not by molecular weight per se. Two compounds with the same molecular weight but different boiling points will elute at very different times. Equally, on a polar stationary phase, a low-molecular-weight polar compound can elute after a higher-molecular-weight nonpolar compound because of stronger polar interactions with the stationary phase. Molecular weight correlates roughly with boiling point for homologous series (e.g., alkanes), which is why the correlation sometimes seems to hold — but it fails systematically for polar analytes, aromatic compounds, and structurally diverse mixtures."

- question: "Temperature programming in GC allows early-eluting compounds to be separated at a lower initial oven temperature, while the temperature is then ramped upward to push later-eluting, higher-boiling compounds off the column within a practical run time."
  type: true-false
  answer: true
  explanation: "This is the core operating principle of temperature programming. At a low starting temperature, volatile/low-boiling compounds partition efficiently between the stationary phase and gas phase and separate with good resolution. If the temperature were held constant, high-boiling compounds would remain dissolved in the stationary phase for so long that their peaks would broaden enormously or not appear within the run window. By ramping the temperature, the analyst effectively optimizes each analyte's elution: early compounds separate cleanly at the low temperature, and the rising temperature progressively reduces retention for everything else, compressing and sharpening later peaks. The result is a chromatogram where all peaks elute with reasonable width and within a practical time — impossible with a single isothermal temperature for wide-boiling-range samples."

- question: "Why does isothermal GC fail for samples containing analytes with a wide range of boiling points, and how does temperature programming solve this problem?"
  type: short-answer
  answer: "At a single temperature optimized for low-boiling analytes, high-boiling compounds remain in the stationary phase so long that their peaks become extremely broad and may never elute. If the temperature is raised to elute high-boilers, low-boiling compounds race through almost instantly as unresolved, overlapping peaks. Temperature programming starts low (resolving early eluters) and ramps upward (accelerating late eluters), giving every analyte an effective elution window."
  explanation: "The van Deemter equation and partition coefficient K explain why: K decreases exponentially with temperature. At low temperature, high-K (high-boiling) compounds are almost entirely dissolved in the stationary phase — their peaks are infinitely broad in the limit. At high temperature, low-K (low-boiling) compounds elute before they can separate — their peaks are unresolved. Temperature programming is conceptually analogous to gradient elution in HPLC (increasing solvent strength over time), except the driving parameter is temperature rather than mobile phase composition. Both strategies solve the same 'general elution problem': the impossibility of simultaneously optimizing resolution for both early and late eluters with a constant mobile phase condition."
```

## Explainer

Gas chromatography works by exploiting a simple physical principle: different volatile compounds spend different amounts of time dissolved in a liquid coating versus riding in a gas stream. From your chromatography fundamentals prerequisite, you know that separation requires a mobile phase that carries analytes through a stationary phase, and that compounds which interact more strongly with the stationary phase elute later. In GC, the mobile phase is an inert **carrier gas** — typically helium or hydrogen — and the stationary phase is a thin liquid film coated on the inner wall of a long, narrow capillary column housed inside a temperature-controlled oven.

Two properties primarily determine how long a compound stays on the column: its **boiling point** and its **polarity relative to the stationary phase**. Low-boiling compounds spend more time in the gas phase and elute first; high-boiling compounds dissolve more readily in the stationary phase liquid and elute later. Polarity adds a second dimension — a polar stationary phase (like polyethylene glycol) retains polar analytes more strongly, while a nonpolar phase (like polydimethylsiloxane) retains nonpolar analytes. By choosing the right stationary phase, you can tune selectivity to separate compounds that have similar boiling points but different polarities, or even reverse elution order entirely.

**Temperature programming** is the most powerful tool for handling real-world samples. If you run the oven at a single temperature (isothermal), low-boiling compounds elute quickly as sharp peaks while high-boiling compounds elute slowly as broad, barely detectable humps — or never elute at all. By ramping the oven temperature during the run, you give every compound an optimized elution window: early-eluting compounds separate well at the initial low temperature, and late-eluting compounds are pushed off the column as the temperature rises. This is conceptually analogous to gradient elution in HPLC, except you are changing temperature instead of mobile phase composition.

Detection is where GC becomes quantitative. The **flame ionization detector (FID)** burns the column effluent in a hydrogen flame and measures the resulting ion current — it responds to virtually all organic compounds proportionally to their carbon content, making it the default workhorse for quantitative organic analysis. The **thermal conductivity detector (TCD)** measures the carrier gas thermal conductivity change when an analyte is present, and responds to all compounds including inorganics and permanent gases, though with lower sensitivity. For specialized applications, the **electron capture detector (ECD)** provides extraordinary sensitivity for halogenated compounds like pesticides and PCBs. Coupling GC to a mass spectrometer (**GC-MS**) provides both separation and definitive identification from mass spectral fragmentation patterns — it is the gold standard for environmental analysis, forensic toxicology, and flavor chemistry.
