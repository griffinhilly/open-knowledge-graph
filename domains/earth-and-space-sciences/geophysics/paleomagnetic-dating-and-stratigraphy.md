---
id: paleomagnetic-dating-and-stratigraphy
title: Paleomagnetic Dating and Magnetostratigraphy
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: paleomagnetism-and-reversals
  type: hard
tags:
- paleomagnetism
- magnetostratigraphy
- dating
- chronology
stage: expert
status: validated
---

# Paleomagnetic Dating and Magnetostratigraphy

## Core Idea
Magnetostratigraphy uses the pattern of paleomagnetic reversals (magnetic polarity zones) preserved in sedimentary and volcanic sequences to establish age correlations across regions, independent of fossils. The geomagnetic polarity time scale (GPTS) calibrates reversal boundaries using radiometric dates; reversal patterns are globally synchronous, enabling correlation and dating of undated sequences. Combined with biostratigraphy and radiometric dating, magnetostratigraphy yields high-resolution chronologies for Phanerozoic and Cenozoic strata.

## Questions

```yaml
- question: "A geologist measures a local polarity column showing four alternating zones (normal-reversed-normal-reversed) and compares it to the GPTS, finding three possible matching segments. What type of information would best resolve this ambiguity?"
  type: multiple-choice
  options:
    - "Measuring the paleomagnetic inclination in each layer more precisely"
    - "Biostratigraphic data (fossil assemblages) or radiometric dates from interbedded volcanic ash to constrain the possible age range"
    - "Resampling the section at closer intervals to subdivide each zone more finely"
    - "Comparing the pattern to a section from another continent, since different locations record different reversal sequences"
  answer: 1
  explanation: "A short polarity sequence of normal-reversed zones is not unique — the same pattern of alternations can appear multiple times in the GPTS at different ages. Pattern matching alone is ambiguous. Independent age constraints from biostratigraphy (fossil assemblages that restrict the possible age range) or radiometric dates (from interbedded volcanic ash or lava flows) narrow the candidates to the correct GPTS segment. Option D is wrong because geomagnetic reversals are globally synchronous — all sections worldwide record the same reversal at the same time, so another continent would show the same ambiguous pattern."

- question: "Why can magnetostratigraphy correlate sedimentary sections from different continents that contain entirely different fossil assemblages?"
  type: multiple-choice
  options:
    - "Sediment deposition rates are globally constant, so depth directly translates to age on any continent"
    - "The same rock types always form simultaneously at all locations worldwide"
    - "Geomagnetic reversals are globally synchronous — the same reversal is recorded at the same time everywhere on Earth, providing a shared chronological signal regardless of lithology or fossils"
    - "Magnetic minerals only form at specific temperatures, linking rocks that formed under identical climate conditions"
  answer: 2
  explanation: "The global synchrony of geomagnetic reversals is the fundamental principle behind magnetostratigraphy's power for correlation. When the geomagnetic field reverses, it reverses everywhere simultaneously — in marine sediments, continental fluvial deposits, volcanic rocks, and glacial tills alike. This creates a common chronological pattern that is independent of what fossils are present or what kind of rock formed. Marine and continental sections with completely different biota share the same reversal sequence, making correlation possible where biostratigraphy cannot reach."

- question: "Magnetostratigraphy can precisely date a sedimentary sequence independently, without any supporting information from fossils or radiometric dating."
  type: true-false
  answer: false
  explanation: "Magnetostratigraphy produces a local polarity column — a barcode of normal and reversed zones — that must be matched against the GPTS. But a short sequence of polarity zones is not unique: normal-reversed-normal could match dozens of segments in the multi-million-year GPTS. Independent age constraints from biostratigraphy or radiometric dates are typically required to uniquely assign the local column to the correct position in the timescale. Magnetostratigraphy is most powerful as part of an integrated dating approach, combining magnetics with other methods — not as a standalone dating technique."

- question: "Magnetostratigraphy is particularly useful for correlating marine sedimentary sections with continental sections because geomagnetic reversals are recorded regardless of rock type or biological content."
  type: true-false
  answer: true
  explanation: "Marine and continental environments have entirely different biotic assemblages, making direct biostratigraphic correlation impossible — an ammonite biozone in a marine section has no equivalent in a continental fluvial deposit. Because geomagnetic reversals are global events recorded in any rock with magnetic minerals — marine limestone, continental mudstone, volcanic ash, glacial till — magnetostratigraphy provides a common chronological signal that bridges these otherwise uncorrelatable depositional environments. This is one of magnetostratigraphy's principal advantages over other stratigraphic tools."

- question: "Explain why the characteristic remanent magnetization (ChRM) must be isolated through progressive demagnetization before a rock can be used in magnetostratigraphy."
  type: short-answer
  answer: "Rocks can acquire multiple magnetic components over their history. The primary magnetization records the ambient field at the time of rock formation, but later events — low-temperature chemical alteration, weathering, exposure to later magnetic fields — can imprint secondary magnetizations that point in different directions. If these secondary components are not removed, the measured bulk magnetization is a mixture that may not reflect the original field direction. Progressive demagnetization (thermal or alternating field) systematically removes the weakly held secondary components first, leaving the characteristic remanent magnetization (ChRM) — the most stable component, which is the primary signal used for correlation."
  explanation: "This step is not optional: undemagnetized samples from the same stratigraphic unit may show scattered directions due to secondary overprinting, while properly demagnetized samples from the same unit cluster tightly around the primary field direction. The demagnetization process is essentially a laboratory experiment that separates the chronologically meaningful signal from later noise, allowing reliable determination of normal vs. reversed polarity at each sampled level."
```

## Explainer

From your study of paleomagnetism and reversals, you know that rocks can preserve a record of Earth's magnetic field at the time they formed — volcanic rocks lock in the field direction when magnetic minerals cool through their Curie temperature, and sedimentary rocks record the field as magnetic grains align during deposition. You also know that Earth's field periodically reverses polarity. **Magnetostratigraphy** exploits these facts to build a dating and correlation tool that works independently of fossils, lithology, or geographic location.

The basic procedure begins with collecting oriented samples at closely spaced intervals through a stratigraphic section — a cliff face, a road cut, a drill core. Each sample is brought to the laboratory and subjected to progressive **demagnetization** (either by heating in steps or by exposing it to alternating magnetic fields of increasing strength) to strip away secondary magnetization components acquired after the rock formed. What remains is the **characteristic remanent magnetization (ChRM)**, which reflects the ambient field at the time of formation. By measuring the declination and inclination of the ChRM for each sample, the geologist determines whether the field was normal (like today) or reversed at the time that layer was deposited. Plotting polarity against stratigraphic position produces a **local magnetic polarity column**: a vertical barcode of normal and reversed zones.

This local polarity column is then compared to the **geomagnetic polarity time scale (GPTS)** — the master reference sequence of dated reversals compiled from radiometrically dated volcanic rocks and marine magnetic anomalies. Because reversals are globally synchronous (the field reverses everywhere at once), the pattern of normal and reversed intervals in any section on Earth should match some segment of the GPTS. The task is pattern matching: finding the unique stretch of the GPTS that best fits the observed local column. This is rarely unambiguous from magnetics alone — a sequence of three or four polarity zones could match multiple parts of the timescale. Independent age constraints from **biostratigraphy** (fossil assemblages that restrict the possible age range) or **radiometric dates** (from interbedded ash layers or lava flows) narrow the possibilities and lock the local column into the correct position on the GPTS.

Once the correlation is established, every polarity boundary in the section receives a numerical age from the GPTS, providing a chronological framework with resolution on the order of tens to hundreds of thousands of years — significantly finer than most biostratigraphic zonations. This makes magnetostratigraphy particularly valuable for correlating marine and continental sections (where fossil assemblages differ), for dating sediments that lack suitable fossils, and for calibrating the timing of evolutionary, climatic, and tectonic events across the Cenozoic and Mesozoic. The method's independence from lithology and biological content gives it a uniquely global reach among stratigraphic tools.
