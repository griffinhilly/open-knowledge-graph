---
id: ocean-sediments-and-stratigraphy
title: Ocean Sediments and Paleoceanographic Records
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: seafloor-spreading-mid-ocean-ridges
  type: hard
- id: sedimentary-rocks
  type: hard
- id: stratigraphy
  type: soft
- id: paleoclimatology
  type: soft
tags:
- marine sediments
- foraminifera
- pelagic sediments
- deep-sea cores
- paleoceanography
stage: advanced
status: validated
---

# Ocean Sediments and Paleoceanographic Records

## Core Idea
Ocean sediments accumulate slowly over millions of years and preserve a detailed archive of past ocean conditions. Pelagic sediments include biogenic oozes (made of calcareous or siliceous microfossils such as foraminifera and radiolarians), terrigenous clays blown or washed from land, and hydrogenous deposits (e.g., manganese nodules). Deep-sea sediment cores provide records of past ocean temperatures (via oxygen isotope ratios in foraminiferal shells), ice volume, ocean circulation, and productivity. The carbonate compensation depth (CCD) — the depth below which CaCO₃ dissolves — controls the global distribution of calcareous sediments.

## How It's Best Learned
Interpret a simplified oxygen isotope record from a foraminifera core, identifying glacial-interglacial cycles. Map the distribution of sediment types across an ocean basin and explain the pattern using water depth relative to CCD and proximity to land.

## Common Misconceptions
- Sediment accumulation on the ocean floor is extremely slow — often 1–10 mm per thousand years — so layers represent vast time spans.
- Foraminifera shells do not record temperature directly; temperature is inferred from isotopic fractionation in calcite, requiring calibration.

## Questions

```yaml
- question: "A sediment core is drilled from the abyssal plain at 5,200 meters depth. The core contains almost no calcareous shells — only red-brown clay. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "No foraminifera or calcareous plankton lived in the surface waters above this site"
    - "The site is below the carbonate compensation depth (CCD), where seawater is corrosive to CaCO₃ and dissolves shells as fast as they accumulate"
    - "The sediment is too old — calcareous shells decompose after a few thousand years in any seafloor environment"
    - "The site is too far from land to receive terrigenous input, leaving only empty water above the clay layer"
  answer: 1
  explanation: "The carbonate compensation depth (CCD) — typically 4,000–5,000 m — is the depth below which increased pressure and lower temperature make seawater corrosive to calcium carbonate. Below the CCD, calcareous shells dissolve before they can accumulate. The abyssal plain at 5,200 m is below the CCD, so even if abundant foraminifera and coccolithophores lived in surface waters above this site, their shells would dissolve on the way down or on the seafloor. Only non-carbonate material like clay survives at these depths."

- question: "When paleoceanographers measure a sustained increase in δ¹⁸O values going down a sediment core (representing older time periods), this most likely indicates:"
  type: multiple-choice
  options:
    - "Warmer ocean temperatures only — heavier oxygen isotopes concentrate in warmer water"
    - "Colder ocean temperatures, growth of continental ice sheets, or both — because both lower temperatures and larger ice sheets increase δ¹⁸O in seawater"
    - "Faster foraminiferal growth rates producing thicker shells with more oxygen"
    - "Shallower water depths at the time of deposition"
  answer: 1
  explanation: "δ¹⁸O in foraminiferal shells reflects two signals simultaneously: (1) cooler water temperatures cause foraminifera to incorporate more ¹⁸O (temperature effect), and (2) growing ice sheets preferentially lock up light ¹⁶O on land, enriching seawater in ¹⁸O (ice volume effect). Both effects move δ¹⁸O in the same direction during glaciations. Disentangling the two signals requires additional proxies (like Mg/Ca ratios for temperature). The common misconception is treating δ¹⁸O as a direct, unambiguous thermometer."

- question: "Deep-sea sediment cores provide a more continuous record of past climate than most terrestrial sedimentary sequences because deep-ocean sedimentation is rarely interrupted by erosion."
  type: true-false
  answer: true
  explanation: "Terrestrial sedimentary records are frequently interrupted by erosion, uplift, river channel migration, glacial scouring, and other processes that destroy or gap the record. Deep-sea sediments, by contrast, accumulate continuously (if slowly — 1–10 mm per thousand years) in stable, protected environments far from energetic erosive processes. This continuity makes ocean sediment cores the primary archive for reconstructing multi-million-year climate histories, including the orbital-scale ice age cycles identified by correlating δ¹⁸O records across ocean basins worldwide."

- question: "The δ¹⁸O ratio measured in foraminiferal shells is a direct, unambiguous thermometer for past ocean surface temperatures."
  type: true-false
  answer: false
  explanation: "This is a critical misconception. δ¹⁸O in foraminiferal calcite reflects two effects: the temperature of the water the organism lived in, and the isotopic composition of the seawater itself — which changes as ice sheets grow and shrink (ice sheets lock up light ¹⁶O, enriching seawater in ¹⁸O). A high δ¹⁸O value could mean cold water, large ice sheets, or both. Separating these signals requires additional proxies and calibration studies. The Common Misconceptions section in this topic explicitly notes this: temperature is inferred from isotopic fractionation, not read directly."

- question: "Why do scientists drill for paleoclimate records in deep ocean sediments rather than relying on more accessible land-based sedimentary records?"
  type: short-answer
  answer: "Deep-sea sediments accumulate slowly and continuously over millions of years without the interruptions that frequently gap terrestrial records (erosion, glacial scouring, river migration, uplift). They also preserve detailed chemical signals in microfossil shells — particularly δ¹⁸O in foraminifera — that encode past temperatures and ice volumes. The global network of deep-sea cores allows records from different ocean basins to be correlated, revealing synchronized global patterns like orbital-scale ice ages. No terrestrial archive approaches this combination of continuity, chemical preservation, and global coverage."
  explanation: "The rarity of complete, continuous, multi-million-year terrestrial records makes deep-sea cores uniquely valuable. Ice cores (another continuous archive) extend only ~800,000 years; deep-sea sediment records stretch back tens of millions of years. The slow accumulation rate — typically 1–10 mm per 1,000 years — means each centimeter of core can represent thousands of years of climate history."
```

## Explainer

From your study of sedimentary rocks, you know that sediments accumulate in layers and that each layer records conditions at the time of deposition. From seafloor spreading, you know that oceanic crust forms at mid-ocean ridges and moves outward, aging as it goes. Ocean sediments sit on top of this crust, and the fundamental insight is that they provide the most continuous and detailed record of Earth's climate history available anywhere — far more complete than most terrestrial records, which are frequently interrupted by erosion.

Ocean sediments come in three main varieties. **Biogenic sediments** (or oozes) are made from the skeletal remains of microscopic organisms that lived in the surface waters and sank to the bottom when they died. Calcareous ooze comes from organisms like **foraminifera** and coccolithophores that build shells of calcium carbonate; siliceous ooze comes from diatoms and radiolarians that build shells of silica. **Terrigenous sediments** are particles weathered from continents and delivered to the ocean by rivers, wind, or ice — they dominate near coastlines and downwind of major deserts. **Hydrogenous sediments** precipitate directly from seawater through chemical reactions, forming features like manganese nodules that grow at rates of millimeters per million years.

The distribution of these sediment types across the ocean floor is not random — it follows predictable rules. The most important is the **carbonate compensation depth** (CCD), typically at 4,000–5,000 meters. Above this depth, calcareous shells accumulate on the seafloor; below it, the water is so cold and under such high pressure that it becomes corrosive to calcium carbonate, dissolving shells faster than they accumulate. This means the deep abyssal plains are covered in terrigenous clay (the only material that survives at any depth), while shallower mid-ocean ridges and plateaus are blanketed in calcareous ooze. The CCD itself has shifted up and down through geological time in response to changes in ocean chemistry, and tracking these shifts in sediment cores reveals past changes in ocean circulation and carbon cycling.

The real power of ocean sediments lies in what the microfossils record chemically. When a foraminifer builds its calcite shell, it incorporates oxygen atoms from seawater. Oxygen comes in two stable isotopes — lighter ¹⁶O and heavier ¹⁸O — and the ratio between them in the shell (written as **δ¹⁸O**) depends on two things: the temperature of the water the organism lived in, and the isotopic composition of the seawater itself (which changes as ice sheets grow and shrink, preferentially locking up light ¹⁶O on land). By measuring δ¹⁸O down a sediment core, paleoceanographers reconstruct a timeline of glacial and interglacial periods stretching back tens of millions of years. Each centimeter of core may represent thousands of years of history, and the global network of deep-sea cores has allowed scientists to correlate these records across ocean basins, revealing the synchronized rhythm of ice ages driven by orbital variations in Earth's path around the Sun.
