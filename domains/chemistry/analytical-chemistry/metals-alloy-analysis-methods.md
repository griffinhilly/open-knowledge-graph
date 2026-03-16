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
status: draft
---

# Metals and Alloy Analysis Methods

## Core Idea
Metallurgical analysis determines major and trace element composition in metals and alloys for quality control and certification. Techniques include wet chemical titration, gravimetry, atomic spectroscopy, and X-ray fluorescence, selected based on analyte concentration and matrix composition.

## Explainer

Every metal product — a steel bridge beam, an aluminum aircraft skin, a gold jewelry piece — must meet precise compositional specifications. Too much carbon in steel makes it brittle; too little chromium in stainless steel and it corrodes. Your knowledge of gravimetric analysis and atomic absorption spectroscopy provides the analytical foundations, and metals analysis applies them to one of the most industrially demanding contexts: determining exactly what is in an alloy and whether it meets specification.

The first challenge is **sample dissolution**. Unlike a water sample you can inject directly into an instrument, a solid metal must be converted into a solution. Most alloys dissolve in mineral acids — hydrochloric acid for aluminum alloys, nitric acid for copper alloys, mixtures of HCl and HNO₃ (aqua regia) for gold and platinum group metals. Some refractory alloys (titanium, tungsten, certain high-chromium steels) resist acid dissolution and require **fusion** with an alkalite flux like sodium peroxide or lithium metaborate at high temperature, followed by dissolution of the fused bead in dilute acid. The choice of dissolution method matters because it determines which acids and salts enter your measurement solution, potentially causing interferences in downstream analysis.

For **major components** (elements present above ~1%), classical wet chemistry remains important. EDTA complexometric titrations determine calcium and magnesium in light alloys, permanganometric titrations measure manganese in steel, and gravimetric precipitation of barium sulfate quantifies sulfur. These methods are slow but serve as **primary reference methods** against which instrumental techniques are validated. The gravimetric methods you have studied — precipitating an analyte as an insoluble compound, filtering, drying, and weighing — apply directly here: nickel in steel can be determined by precipitating nickel dimethylglyoximate, and silicon by dehydrating silica with perchloric acid.

For **trace and minor elements**, instrumental methods dominate. **Flame AAS** handles single-element determinations at ppm levels efficiently — measuring lead in brass or copper in steel, for example. **ICP-OES** (inductively coupled plasma optical emission spectroscopy) is the modern workhorse for multi-element analysis: a single dissolved sample, aspirated into an argon plasma at ~8000 K, simultaneously emits light at wavelengths characteristic of every element present, allowing 20 or more elements to be quantified in minutes. **X-ray fluorescence (XRF)** offers a completely different approach — it analyzes the solid sample directly without dissolution, exciting characteristic X-ray emissions by bombarding the surface with high-energy X-rays. Portable XRF instruments are used on factory floors for rapid sorting and screening, though they sacrifice some accuracy compared to solution-based methods. The choice among these techniques depends on the number of elements needed, required accuracy, sample throughput, and whether the analysis must be destructive or nondestructive.
