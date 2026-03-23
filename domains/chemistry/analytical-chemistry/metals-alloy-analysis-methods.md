---
id: metals-alloy-analysis-methods
title: Metals and Alloy Analysis Methods
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: gravimetric-analysis
  type: hard
- id: atomic-absorption-spectroscopy
  type: hard
tags:
- metallurgical analysis
- metals
- alloys
stage: advanced
status: validated
---

# Metals and Alloy Analysis Methods

## Core Idea
Metallurgical analysis determines major and trace element composition in metals and alloys for quality control and certification. Techniques include wet chemical titration, gravimetry, atomic spectroscopy, and X-ray fluorescence, selected based on analyte concentration and matrix composition.

## Questions

```yaml
- question: "A quality control lab must simultaneously determine 25 trace elements in dissolved steel samples with ppm-level accuracy. Which technique is most appropriate?"
  type: multiple-choice
  options:
    - "Flame AAS — accurate and well-established for metal analysis"
    - "Gravimetric precipitation — primary reference method for most metals"
    - "ICP-OES — simultaneously quantifies many elements in a single aspirated solution"
    - "XRF on solid samples — nondestructive and fast"
  answer: 2
  explanation: "ICP-OES is the modern workhorse for multi-element analysis precisely because a single dissolved sample yields data on 20+ elements in minutes. Flame AAS measures only one element per run, making 25-element panels inefficient. Gravimetric methods are far too slow for routine multi-element work. XRF is fast and nondestructive but sacrifices accuracy compared to solution-based methods and is better suited for screening than certification."

- question: "A titanium alloy sample resists complete dissolution in HCl, HNO₃, and aqua regia. What is the standard next step for preparing it for analysis?"
  type: multiple-choice
  options:
    - "Increase acid concentration and heating time until the alloy dissolves"
    - "Fusion with an alkaline flux (e.g., sodium peroxide or lithium metaborate) followed by dissolution of the fused bead in dilute acid"
    - "Analyze the solid directly by flame AAS without dissolution"
    - "Dilute the sample with a soluble matrix modifier and proceed to ICP-OES"
  answer: 1
  explanation: "Refractory alloys including titanium and tungsten-based materials resist acid dissolution. The standard approach is high-temperature fusion with an alkaline flux, which chemically breaks down the refractory oxide matrix. The resulting fused bead is then dissolved in dilute acid to produce a solution compatible with spectroscopic techniques. Increasing acid aggressiveness will not dissolve refractory materials — fusion is a qualitatively different, non-acid approach."

- question: "XRF analysis of solid metal samples generally provides higher quantitative accuracy for trace element determination than ICP-OES after acid dissolution."
  type: true-false
  answer: false
  explanation: "XRF is valuable for its speed, nondestructive nature, and suitability for factory-floor screening. However, it sacrifices accuracy compared to solution-based methods. ICP-OES after careful dissolution provides better sensitivity and accuracy for trace elements, which is why it dominates certification analysis. XRF is used when speed and sample preservation matter more than maximum accuracy."

- question: "Classical wet chemical methods such as gravimetric precipitation and titrimetry remain important in metals analysis as primary reference methods against which instrumental techniques are validated."
  type: true-false
  answer: true
  explanation: "Despite being slow and labor-intensive, classical methods like permanganometric titration for manganese and gravimetric nickel dimethylglyoximate precipitation are metrologically traceable primary methods. Instrumental techniques like ICP-OES are faster but require calibration and validation against these classical standards. The reference role of classical methods in a quality system is distinct from their day-to-day use for routine analysis."

- question: "Why does the choice of acid dissolution method matter beyond simply getting the metal into solution?"
  type: short-answer
  answer: "The dissolution medium introduces specific acids, salts, and oxidation states into the measurement solution. These can cause spectral or chemical interferences in downstream analysis — for example, perchloric acid used for silicon dehydration may interfere with certain ICP-OES emission lines, and residual chloride from HCl dissolving copper alloys can affect atomization in flame AAS. Selecting the right dissolution method means controlling the matrix to minimize downstream interferences and ensure the analyte is in the correct chemical form for the chosen technique."
  explanation: "This is the key systems-thinking insight: sample preparation and measurement are coupled. A dissolution method optimized for one technique (e.g., HCl for aluminum alloys read by flame AAS) may perform poorly for another (e.g., ICP-OES with certain wavelengths sensitive to chloride). Analysts must think through the entire analytical chain from dissolution to detection when selecting a method."
```

## Explainer

Every metal product — a steel bridge beam, an aluminum aircraft skin, a gold jewelry piece — must meet precise compositional specifications. Too much carbon in steel makes it brittle; too little chromium in stainless steel and it corrodes. Your knowledge of gravimetric analysis and atomic absorption spectroscopy provides the analytical foundations, and metals analysis applies them to one of the most industrially demanding contexts: determining exactly what is in an alloy and whether it meets specification.

The first challenge is **sample dissolution**. Unlike a water sample you can inject directly into an instrument, a solid metal must be converted into a solution. Most alloys dissolve in mineral acids — hydrochloric acid for aluminum alloys, nitric acid for copper alloys, mixtures of HCl and HNO₃ (aqua regia) for gold and platinum group metals. Some refractory alloys (titanium, tungsten, certain high-chromium steels) resist acid dissolution and require **fusion** with an alkalite flux like sodium peroxide or lithium metaborate at high temperature, followed by dissolution of the fused bead in dilute acid. The choice of dissolution method matters because it determines which acids and salts enter your measurement solution, potentially causing interferences in downstream analysis.

For **major components** (elements present above ~1%), classical wet chemistry remains important. EDTA complexometric titrations determine calcium and magnesium in light alloys, permanganometric titrations measure manganese in steel, and gravimetric precipitation of barium sulfate quantifies sulfur. These methods are slow but serve as **primary reference methods** against which instrumental techniques are validated. The gravimetric methods you have studied — precipitating an analyte as an insoluble compound, filtering, drying, and weighing — apply directly here: nickel in steel can be determined by precipitating nickel dimethylglyoximate, and silicon by dehydrating silica with perchloric acid.

For **trace and minor elements**, instrumental methods dominate. **Flame AAS** handles single-element determinations at ppm levels efficiently — measuring lead in brass or copper in steel, for example. **ICP-OES** (inductively coupled plasma optical emission spectroscopy) is the modern workhorse for multi-element analysis: a single dissolved sample, aspirated into an argon plasma at ~8000 K, simultaneously emits light at wavelengths characteristic of every element present, allowing 20 or more elements to be quantified in minutes. **X-ray fluorescence (XRF)** offers a completely different approach — it analyzes the solid sample directly without dissolution, exciting characteristic X-ray emissions by bombarding the surface with high-energy X-rays. Portable XRF instruments are used on factory floors for rapid sorting and screening, though they sacrifice some accuracy compared to solution-based methods. The choice among these techniques depends on the number of elements needed, required accuracy, sample throughput, and whether the analysis must be destructive or nondestructive.
