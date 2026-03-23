---
id: sedimentary-provenance-source-analysis
title: Sedimentary Provenance and Source-to-Sink Analysis
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: sedimentary-rock-detrital-chemical
  type: hard
builds-toward:
- stratigraphy-law-superposition-correlation
- plate-tectonics-continental-drift-evidence
tags:
- sedimentary
- provenance
- tectonics
stage: formal-systems
status: validated
---

# Sedimentary Provenance and Source-to-Sink Analysis

## Core Idea
Mineral composition, heavy minerals, grain shape, and isotopic signatures in sedimentary rocks reveal the geographic location, lithology, and age of source rocks. Provenance analysis reconstructs ancient continental positions, identifies past mountain belts, and tracks sediment pathways from uplift to deposition.

## Questions

```yaml
- question: "A sandstone contains abundant fresh feldspar, lithic fragments, and very little quartz. What does this composition indicate about its provenance?"
  type: multiple-choice
  options:
    - "The sediment was derived from a distant, mature cratonic source and transported by a major river system"
    - "The sediment came from a nearby source with limited weathering and transport, such as a recently uplifted granitic or volcanic terrane"
    - "The sediment was recycled from an older sedimentary sequence that had already been quartz-enriched"
    - "The high feldspar content indicates deep-water deposition far from any terrestrial source"
  answer: 1
  explanation: "Feldspar is chemically and mechanically fragile — it breaks down during prolonged weathering and transport. Its abundance in an immature sandstone (arkose) indicates the sediment did not travel far or weather long before deposition. Fresh feldspar requires a nearby granitic, gneissic, or volcanic source and rapid burial. Long transport produces mature sediment depleted in feldspar and enriched in resistant quartz. The QFL diagram places feldspar-rich sandstones in the continental block or magmatic arc fields — both implying tectonically active, nearby sources."

- question: "A detrital zircon U-Pb age spectrum from a Cretaceous sandstone shows populations at 1.1 Ga, 1.8 Ga, and 2.7 Ga. What does this reveal that QFL modal analysis cannot?"
  type: multiple-choice
  options:
    - "The sandstone was deposited during three separate events at 1.1, 1.8, and 2.7 billion years ago"
    - "The source terrain included igneous and metamorphic rocks with crystallization ages of 1.1, 1.8, and 2.7 Ga, identifying specific ancient geological provinces"
    - "The sandstone has been metamorphosed three times, resetting the zircon clock at each event"
    - "The heavy mineral assemblage contains three distinct mineral populations with different weathering stabilities"
  answer: 1
  explanation: "Detrital zircon geochronology dates when each zircon crystallized in its source rock — not when the sediment was deposited. Age populations can be matched to known geological events: 1.1 Ga to the Grenville orogen, 1.8 Ga to the Trans-Hudson orogen, 2.7 Ga to Archean cratons, for example. This fingerprints the specific source terrains that contributed sediment, even if those terranes have since been displaced by plate motion. QFL analysis indicates tectonic setting; detrital zircon identifies specific provinces and ages."

- question: "A quartz-rich, feldspar-poor sandstone (quartz arenite) is strong evidence for deposition close to the source terrain."
  type: true-false
  answer: false
  explanation: "A quartz arenite indicates textural and chemical maturity, which requires prolonged weathering, long transport, or recycling through multiple sedimentary cycles — the opposite of proximity to source. Feldspar is destroyed by weathering and mechanical abrasion during transport; only after extensive processing does a feldspar-poor quartz arenite result. Sediment deposited close to its source typically preserves abundant fresh feldspar and rock fragments (lithics) precisely because they haven't been destroyed yet. Immature, proximal deposits are arkoses and lithic sandstones, not quartz arenites."

- question: "An upward change in detrital zircon age populations within a sedimentary sequence — progressively older age peaks appearing in younger strata — can record the progressive erosional unroofing of a mountain belt."
  type: true-false
  answer: true
  explanation: "As a mountain belt erodes, it exposes progressively deeper (and often older) crustal levels over time. If upper-crustal rocks have one zircon age signature and the deeper metamorphic basement has a different signature, their progressive exposure shifts the provenance signal in the adjacent basin stratigraphy. Reading provenance upsection records the erosional history of the orogen in reverse: shallow, young sources early; deep, old sources later. This reconstructs mountain belt evolution even when the mountains themselves have been entirely eroded away."

- question: "Why is detrital zircon geochronology considered the most powerful single provenance tool, and what property of zircon makes it uniquely suited for this application?"
  type: short-answer
  answer: "Zircon (ZrSiO₄) is exceptionally resistant to mechanical and chemical destruction during weathering, erosion, and transport — surviving multiple sedimentary cycles without losing its isotopic record. Crucially, zircon incorporates uranium but excludes lead when it crystallizes, so the accumulation of radiogenic lead records the crystallization age with high precision via U-Pb geochronology. Each zircon grain is effectively a clock recording when its source rock formed. This age can be matched to known geological provinces to fingerprint source terrains that may no longer exist at the surface."
  explanation: "The combination of physical durability and isotopic clock makes detrital zircon uniquely informative. Heavy minerals like garnet are more lithology-specific but are destroyed by weathering. Bulk QFL composition indicates tectonic setting but not specific age constraints. Detrital zircon provides age constraints directly matchable to known geological provinces, enabling provenance tracing across thousands of kilometers and billions of years of geological time."
```

## Explainer

From your work on sedimentary rocks, you know that detrital sediments are composed of fragments eroded from pre-existing rocks, transported by water, wind, or ice, and deposited in a new location. **Provenance analysis** reverses this journey — it reads the composition of a sedimentary rock to determine where its components came from, what kind of rocks were being eroded, and how far the sediment traveled. This detective work connects sedimentary basins to their source terrains, reconstructing ancient geography and tectonic history.

The simplest provenance tool is **mineral composition**. Quartz is mechanically and chemically resistant, surviving long transport distances and intense weathering. Feldspar is abundant in igneous and metamorphic rocks but breaks down relatively quickly during transport and chemical weathering. A sandstone rich in feldspar (an arkose) therefore indicates a nearby granitic or gneissic source with limited weathering — often a recently uplifted continental block. A mature quartz arenite, composed almost entirely of quartz, indicates prolonged weathering, long transport, or recycling through multiple sedimentary cycles. The ratio of quartz to feldspar to lithic (rock) fragments places a sandstone on the **QFL diagram**, which correlates compositional modes with tectonic settings: continental block sources, magmatic arc sources, and recycled orogen sources each produce distinctive QFL signatures.

**Heavy mineral analysis** adds resolution. Minerals like zircon, tourmaline, garnet, rutile, and chrome spinel survive weathering and transport, and each is diagnostic of specific source lithologies. Chrome spinel points to an ultramafic (mantle-derived) source. Blue sodic amphibole indicates high-pressure metamorphic rocks from a subduction complex. The assemblage of heavy minerals in a sandstone acts like a fingerprint of the eroding source terrain. **Detrital zircon geochronology** takes this further by dating individual zircon grains using U-Pb isotopic ratios. Since zircon is nearly indestructible and records the crystallization age of its parent igneous or metamorphic rock, a population of detrital zircon ages from a sandstone reveals the ages of all the source rocks that contributed sediment. Matching these age populations to known geological provinces identifies the source terrain, even when that terrain has since been displaced by plate motion or buried under younger rocks.

Provenance analysis becomes most powerful when integrated across a stratigraphic section. Changes in sandstone composition or detrital zircon age spectra upsection record the progressive unroofing of a mountain belt — as erosion strips away upper crustal rocks, deeper and older source lithologies become exposed, shifting the sediment signature. This **unroofing sequence** tracks the erosional history of an orogen in real time, preserved in the adjacent basin fill. By combining compositional, mineralogical, and isotopic provenance data with paleocurrent indicators (cross-bedding directions, channel orientations), geologists reconstruct entire source-to-sink systems — from the mountains being eroded, through the rivers carrying sediment, to the basins where it accumulated — mapping ancient landscapes that no longer exist.
