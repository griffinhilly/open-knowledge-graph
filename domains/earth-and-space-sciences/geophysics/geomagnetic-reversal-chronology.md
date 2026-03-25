---
id: geomagnetic-reversal-chronology
title: Geomagnetic Reversal Chronology and Magnetostratigraphy
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: geomagnetic-dynamo-theory
  type: hard
- id: paleomagnetic-dating-and-stratigraphy
  type: hard
tags:
- geomagnetic
- reversal
- chronology
- stratigraphy
stage: advanced
status: validated
---

# Geomagnetic Reversal Chronology and Magnetostratigraphy

## Core Idea
The geomagnetic field reverses at irregular intervals (averaging ~200 ka). A geomagnetic polarity time scale (GPTS) documents reversal patterns; magnetostratigraphy correlates magnetic reversals in sediments and lavas to the GPTS for dating.

## Questions

```yaml
- question: "A geologist finds a sedimentary section in Spain containing no dateable volcanic ash and no index fossils. The section shows a clear pattern of normal and reversed magnetic polarity zones. Can the section be dated, and if so, how?"
  type: multiple-choice
  options:
    - "No — without fossils or radiometric material, no age can be assigned to the section"
    - "Yes — the polarity sequence can be compared to the GPTS and, if a unique match is found, numerical ages can be assigned to polarity boundaries"
    - "Yes, but only approximately, because reversals are too irregular to constrain age to better than ±10 million years"
    - "No — sedimentary rocks do not reliably record magnetic polarity and cannot be used for magnetostratigraphy"
  answer: 1
  explanation: "This is magnetostratigraphy in action. Because geomagnetic reversals are globally synchronous, the pattern of polarity zones in any section — regardless of its lithology or fossil content — must match the same GPTS as every other section of the same age. By comparing the local polarity column (normal/reversed sequence and their thicknesses, weighted by estimated sedimentation rates) to the GPTS, a geologist can identify the most likely correlation and assign ages to boundaries. The method works independently of fossils, which is its great power — it can date sections where biostratigraphy fails."

- question: "The Cretaceous Normal Superchron was a ~40 million year period with no geomagnetic reversals. What does this imply for magnetostratigraphy applied to sediments deposited during this interval?"
  type: multiple-choice
  options:
    - "Sediments from the Cretaceous Normal Superchron cannot be dated by any method because they record only one polarity"
    - "Magnetostratigraphy cannot subdivide this interval because there are no polarity boundaries to correlate with the GPTS — other dating methods must be used for internal chronology"
    - "The superchron appears in the GPTS as a long reversed-polarity interval and is straightforward to identify"
    - "Sediments from this period show reversed polarity and are easily correlated across basins"
  answer: 1
  explanation: "Magnetostratigraphy works by correlating polarity boundaries — transitions between normal and reversed zones — to the GPTS. When there are no reversals for 40 million years, there are no polarity boundaries to match. A section recording the CNS appears as an undifferentiated normal-polarity interval; you can identify it as CNS, but you cannot subdivide its internal chronology using magnetostratigraphy. This is a genuine limitation of the method: biostratigraphy, cyclostratigraphy, or radiometric dating must provide internal age control within superchrons. The CNS appears as normal polarity (not reversed) in the GPTS — option C is also wrong."

- question: "Geomagnetic reversals occur at different times in different regions of the Earth, which is why the magnetic anomaly patterns on the seafloor differ between ocean basins."
  type: true-false
  answer: false
  explanation: "False — geomagnetic reversals are globally synchronous. When the dynamo reverses, the field changes polarity everywhere on Earth at essentially the same time (on geological timescales). The magnetic anomaly patterns on different seafloors differ because spreading rates differ: a fast-spreading ridge (like the East Pacific Rise) creates wider anomaly stripes for the same reversal interval than a slow-spreading ridge (like the Mid-Atlantic Ridge). The timing of the reversals is the same; only the width of the stripes recording those reversals varies with spreading rate."

- question: "The geomagnetic polarity time scale was extended back through the Cretaceous primarily by using marine magnetic anomalies combined with estimates of seafloor spreading rates."
  type: true-false
  answer: true
  explanation: "True. Dateable volcanic rocks on land (calibrated by ⁴⁰Ar/³⁹Ar dating) established the GPTS for the past ~5 million years. To extend the scale further back in time, geophysicists exploited the symmetric patterns of magnetic anomalies flanking mid-ocean ridges. If the spreading rate is known or can be estimated, the width of each anomaly stripe converts directly to a duration. By measuring anomaly patterns across many ridge systems and using spreading rates constrained by other data, the GPTS was extended through the Cretaceous and into the Jurassic — far beyond the reach of continental lavas."

- question: "Explain why the global synchroneity of geomagnetic reversals makes magnetostratigraphy a powerful correlation tool, and identify its key limitation."
  type: short-answer
  answer: "Because reversals happen simultaneously everywhere on Earth, the same polarity boundary in rocks from Italy and the Pacific represents exactly the same moment in time. This allows correlation of sedimentary sections across any distance without relying on shared fossils or lithologies. The key limitation is resolution: magnetostratigraphy can only place age constraints at polarity boundaries. Within a long normal or reversed zone — especially during superchrons — the method provides no internal chronology, and other dating methods must be used."
  explanation: "The synchroneity is what distinguishes magnetostratigraphy from, say, biostratigraphy: a fossil zone may appear at different times in different regions due to facies controls or migration lags, but a polarity reversal is isochronous globally. This makes it a true global correlation tool. The limitation matters practically: the Cretaceous Normal Superchron (no reversals for ~40 Ma) is a blank interval for magnetostratigraphy, requiring cyclostratigraphy or radiometric dating to establish internal chronology."
```

## Explainer

From your study of the geodynamo, you know that Earth's magnetic field periodically reverses polarity — north becomes south and south becomes north. From paleomagnetic dating, you know that rocks can record these polarity states and that the pattern of reversals can be matched across distant locations. Geomagnetic reversal chronology brings these ideas together into a single, precisely calibrated framework: the **geomagnetic polarity time scale (GPTS)**, which is essentially a barcode of normal and reversed polarity intervals stretching back through geologic time.

The GPTS was originally constructed by measuring the magnetic polarity and radiometric ages of young volcanic rocks, particularly basalt flows in places like Iceland and the western United States. When many dated lava flows were arranged in time sequence, a pattern emerged: intervals of normal polarity (field oriented like today) alternating with intervals of reversed polarity at irregular spacings. The major polarity intervals, lasting roughly 0.5 to 5 million years, are called **chrons** and are named after pioneers of geomagnetism — Brunhes (current normal), Matuyama (reversed), Gauss (normal), and Gilbert (reversed) for the most recent four. Within chrons, shorter episodes of opposite polarity called **subchrons** add finer detail; the Olduvai and Jaramillo subchrons within the Matuyama, for example, are normal-polarity intervals lasting a few hundred thousand years each.

The power of the GPTS lies in the fact that reversals are **globally synchronous** — when the field reverses, it reverses everywhere on Earth simultaneously. This means the polarity sequence recorded in a sedimentary section in Italy must match the sequence in a deep-sea core from the Pacific, even if the sediments are completely different in composition and fossil content. **Magnetostratigraphy** exploits this principle: by measuring the polarity of closely spaced samples through a stratigraphic section, a geologist builds a local polarity column — a sequence of normal and reversed zones. That local column is then compared to the GPTS to find the best-fit correlation, assigning numerical ages to the section's boundaries.

The calibration of the GPTS itself relies on a combination of radiometric dating (especially ⁴⁰Ar/³⁹Ar dating of volcanic rocks that bracket reversal boundaries) and the pattern of **marine magnetic anomalies** — the symmetric stripes of alternating normal and reversed polarity recorded in oceanic crust as it forms at mid-ocean ridges and spreads away. By measuring the width of these anomaly stripes and knowing the spreading rate, geophysicists extended the GPTS back through the Cretaceous and into the Jurassic, well beyond the reach of dateable continental lava flows. The resulting timescale — refined over decades and now known in versions like CK95 or GTS2020 — provides one of geology's most powerful correlation tools, capable of resolving ages to within a few tens of thousands of years for Cenozoic strata and anchoring global stratigraphic frameworks independent of fossil biozonation.
