---
id: gas-chromatography-quantitative-analysis
title: 'Gas Chromatography: Quantitative Analysis and Calibration'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: gas-chromatography
  type: hard
- id: chromatography-fundamentals
  type: hard
- id: calibration-curve-methods
  type: soft
builds-toward:
- gas-chromatography-mass-spectrometry-gc-ms
- two-dimensional-chromatography-comprehensive
tags:
- GC
- quantitation
- calibration
- peak-area
- internal-standard
stage: formal-systems
status: draft
---

# Gas Chromatography: Quantitative Analysis and Calibration

## Core Idea
Quantitative GC converts detector signals (FID, ECD, etc.) into analyte concentration through area or height measurement and calibration. Advanced approaches include internal standard methods to correct for injection volume variation, response factor calculations accounting for detector sensitivity, and handling of co-eluting compounds through peak deconvolution.

## How It's Best Learned
Analyze multi-component GC standards, prepare calibration curves using different methods, and quantify unknowns with various approaches.

## Common Misconceptions
Assuming peak height and area give equivalent results (they diverge when peak shape varies). Neglecting the impact of sample matrix on detector response factors.

## Questions

```yaml
- question: "Two analysts measure the same analyte mixture using identical GC conditions. Analyst A uses external standard calibration; Analyst B uses the internal standard method. Their results diverge by 12%. What is the most likely cause?"
  type: multiple-choice
  options:
    - "Analyst A's injections varied in volume across samples, introducing proportional error that the internal standard method corrects"
    - "The internal standard co-eluted with the analyte in Analyst B's analysis, distorting peak areas"
    - "Analyst A used peak area while Analyst B used peak height, which always diverge"
    - "Different detector response factors applied to the two analysts' instruments"
  answer: 0
  explanation: "Injection volume variability is the primary limitation of external standard calibration. Even small differences in injected volume produce proportional differences in peak area, introducing scatter across samples and standards. The internal standard method corrects for this by adding a fixed amount of a non-analyte compound to every sample and standard — both the analyte and the IS experience the same injection volume variation, so their area ratio cancels the error. Options B and C describe real issues but wouldn't produce systematic 12% divergence between methods on the same samples. Option D would affect both analysts equally."

- question: "An analyst injects equal masses of hexane and toluene into a GC-FID system and observes that hexane gives a larger peak area despite equal mass. What does this demonstrate?"
  type: multiple-choice
  options:
    - "The column retained toluene longer, spreading its peak and reducing height but not area"
    - "Hexane eluted as a sharper peak, so its height is larger even though area is the same"
    - "FID response factors differ between compounds — equal masses produce different detector signals"
    - "Toluene partially decomposed on the column, reducing the amount reaching the detector"
  answer: 2
  explanation: "FID response is roughly proportional to the number of carbon-hydrogen bonds involved in combustion, not simply mass. Hexane (fully aliphatic) has a higher FID response per unit mass than toluene (aromatic ring carbons respond less efficiently to FID). This is the relative response factor: the ratio of detector signal to analyte mass differs between compounds. Ignoring this and treating all peak areas as directly comparable masses would introduce systematic errors in multicomponent analysis. Options A and B confuse peak shape effects with area. Option D is a different phenomenon."

- question: "Peak area is always preferred over peak height for GC quantitation because it is more reproducible under all chromatographic conditions."
  type: true-false
  answer: false
  explanation: "Peak area is generally preferred because it is proportional to the total mass of analyte reaching the detector regardless of peak shape. However, peak height can outperform area when peaks partially overlap: integrating the area of two merged peaks introduces larger errors than reading the heights of partially resolved maxima. The claim that area is *always* preferred is the misconception — the choice depends on peak resolution. When peaks are fully resolved, area is more robust; when peaks partially overlap, height measurement at the apex may be more accurate."

- question: "In the internal standard method, the ratio of analyte peak area to internal standard peak area is used instead of raw analyte area because the ratio corrects for injection volume variation."
  type: true-false
  answer: true
  explanation: "This is the core logic of the internal standard method. If injection volume varies by 5% between runs, both the analyte signal and the IS signal change by ~5% — so their ratio remains constant. The calibration curve plots this area ratio versus analyte concentration, meaning any injection volume variation affects numerator and denominator equally and cancels out. This is why the IS must be added at the same concentration to every sample and standard before injection — it must experience exactly the same injection variability as the analyte to function as a correction factor."

- question: "Why must an internal standard be chemically similar to the analyte, and why must it be fully resolved chromatographically from the analyte?"
  type: short-answer
  answer: "Chemical similarity is required so the IS behaves like the analyte during sample preparation and injection — if the IS has very different volatility or solubility, it may be lost or enriched at different rates than the analyte during sample handling, breaking the correction logic. The IS must also have a similar detector response factor so that its signal scales predictably with the analyte's. Full chromatographic resolution is required so that the two peaks can be integrated independently — if the IS co-elutes with the analyte, their peaks overlap and neither can be accurately measured."
  explanation: "The internal standard method's validity depends on the IS being a perfect surrogate for the analyte everywhere except the concentration axis. Chemical similarity ensures it behaves identically during injection; similar response factors ensure detector behavior is comparable; chromatographic resolution ensures the two peaks can be distinguished. Violating any of these requirements introduces systematic bias that defeats the purpose of using an IS in the first place."
```

## Explainer

From your study of gas chromatography, you understand how compounds are separated by differential partitioning between a mobile gas phase and a stationary phase inside a column. From chromatography fundamentals, you know that the detector at the column exit produces a signal proportional to the amount of analyte passing through it. Quantitative GC is the discipline of converting that detector signal into a reliable concentration or mass value — and the gap between "getting a peak" and "getting an accurate number" is larger than it first appears.

The detector output is a chromatogram: a series of peaks plotted as signal intensity versus time. For quantitation, you measure either **peak area** (the integrated area under the curve) or **peak height** (the maximum signal intensity). Peak area is generally preferred because it is proportional to the total mass of analyte that passed through the detector, regardless of peak shape. Peak height can be affected by band broadening, tailing, or slight retention time shifts that change the peak's width without changing the total mass. However, height can outperform area when peaks partially overlap, because area integration of merged peaks introduces larger errors than reading the height of a partially resolved maximum.

The relationship between peak area and analyte concentration is established through **calibration**. The simplest approach is external standard calibration: you inject standards of known concentration, plot area versus concentration, and read unknown concentrations from the resulting curve. This works when injection volumes are highly reproducible. In practice, manual or autosampler injections vary slightly in volume, introducing scatter. The **internal standard method** corrects for this by adding a fixed amount of a non-analyte compound (the internal standard) to every sample and standard. You then plot the ratio of analyte area to internal standard area versus concentration. Since both compounds experience the same injection volume variation, the ratio cancels the error. Choosing an internal standard requires that it be chemically similar to the analyte (so it behaves similarly in the injection and separation) but fully resolved chromatographically.

A subtlety often overlooked is that different detectors have different **response factors** for different compounds. An FID (flame ionization detector) responds roughly in proportion to the number of carbon atoms, so equal masses of hexane and toluene give different peak areas. A **relative response factor** quantifies this ratio and must be determined experimentally or looked up in reference tables. Ignoring response factors — treating all peak areas as directly comparable — is a common source of quantitative error, especially in multicomponent analyses where you need accurate concentrations for every compound in a mixture, not just relative abundances.
