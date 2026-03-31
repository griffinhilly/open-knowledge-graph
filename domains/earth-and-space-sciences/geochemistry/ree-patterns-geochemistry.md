---
id: ree-patterns-geochemistry
title: REE Patterns in Geochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: trace-element-geochemistry
  type: hard
- id: partition-coefficients
  type: hard
builds-toward:
- mantle-geochemistry
- sedimentary-geochemistry
tags:
- rare-earth-elements
- REE
- chondrite-normalized
- Eu-anomaly
stage: expert
status: validated
---

# REE Patterns in Geochemistry

## Core Idea
The rare earth elements (La through Lu, plus Y) form a coherent geochemical group with smoothly varying ionic radii, making their chondrite-normalized abundance patterns powerful diagnostic tools. Because all REE are trivalent (except Eu2+ and Ce4+ under specific conditions), their relative behavior during geological processes reflects systematic size-dependent partitioning rather than dramatic chemical differences. The slope of the REE pattern (LREE/HREE ratio) indicates the depth and degree of melting (garnet retains HREE). Anomalies at Eu (controlled by plagioclase fractionation in the crust) and Ce (controlled by redox in marine environments) provide additional process-specific information. REE patterns are among the most widely used geochemical fingerprints in igneous, sedimentary, and environmental geochemistry.

## Questions

```yaml
- question: "A granite shows a strongly negative Eu anomaly (Eu/Eu* = 0.3) on its chondrite-normalized REE pattern. What process is most likely responsible?"
  type: multiple-choice
  options:
    - "Crystallization of garnet from the granitic magma"
    - "Fractionation of plagioclase, which selectively incorporates Eu2+ (substituting for Ca2+ in the crystal structure) while excluding trivalent REE, depleting Eu in the residual melt relative to its neighboring elements Sm and Gd"
    - "Weathering of the granite at Earth's surface"
    - "Contamination by seawater"
  answer: 1
  explanation: "Europium is unique among the REE because it can exist as Eu2+ under reducing conditions typical of silicate melts. Eu2+ has a similar ionic radius to Ca2+ and substitutes readily into the plagioclase structure. When plagioclase crystallizes and is removed (or was fractionated from a parent magma), Eu is selectively depleted from the melt while the other REE follow normal trivalent partitioning. The resulting negative Eu anomaly is the hallmark of intracrustal differentiation involving plagioclase."

- question: "MORB (mid-ocean ridge basalt) characteristically shows a flat to slightly LREE-depleted chondrite-normalized REE pattern, while ocean island basalt (OIB) shows strong LREE enrichment."
  type: true-false
  answer: true
  explanation: "MORB forms by moderate-degree (~10-20%) melting of depleted upper mantle (spinel peridotite) at shallow depth. Without residual garnet, HREE are not preferentially retained, producing a flat pattern. The depleted source contributes to slight LREE depletion. OIB forms by smaller-degree melting of enriched mantle sources, often with residual garnet at depth (retaining HREE), producing steep LREE-enriched patterns. The contrast in REE slope between MORB and OIB is a first-order diagnostic of source composition and melting conditions."

- question: "Explain what a positive Ce anomaly in marine chemical sediments indicates about the redox conditions during deposition."
  type: short-answer
  answer: "Cerium can be oxidized from Ce3+ to Ce4+ in oxygenated seawater. Ce4+ is highly insoluble and is scavenged onto manganese oxide surfaces and ferromanganese nodules, depleting dissolved Ce in seawater (producing the characteristic negative Ce anomaly in seawater). When these Mn-Fe oxides are incorporated into sediments, they carry excess Ce, producing a positive Ce anomaly. Alternatively, positive Ce anomalies in sediments can indicate incorporation of terrestrial material (which has no Ce anomaly relative to seawater patterns). The Ce anomaly in marine sediments and waters is therefore a proxy for ocean oxygenation: stronger negative anomalies in seawater indicate more oxidizing conditions driving Ce4+ scavenging."
  explanation: "The Ce anomaly is the only REE anomaly controlled by redox chemistry in the marine environment, making it a unique tracer of ocean oxygenation through Earth history."
```

## Explainer

The rare earth elements are the geochemist's most versatile pattern-recognition tool. Their coherent geochemical behavior -- all trivalent, similar bonding properties, smoothly decreasing ionic radius from La to Lu -- means that any deviation from a smooth chondrite-normalized pattern records a specific geological process.

Chondrite normalization removes the odd-even abundance variation (the Oddo-Harkins effect, where even-Z elements are more abundant) inherited from stellar nucleosynthesis. After normalization, any remaining pattern is geological. A flat pattern at 10x chondrite indicates a source with chondritic REE ratios. A steep LREE-enriched pattern indicates either a LREE-enriched source or a process that preferentially concentrated LREE. The slope of the pattern, quantified by La_N/Yb_N (where N = chondrite-normalized), ranges from ~1 (flat, like MORB) to >30 (steep, like kimberlites).

The two diagnostic anomalies -- Eu and Ce -- arise from unique redox chemistry. Europium can exist as Eu2+ in reducing conditions (silicate melts, lower crust). Eu2+ has the same charge and similar radius to Ca2+ and enters plagioclase readily. Plagioclase fractionation produces negative Eu anomalies in evolved magmas and complementary positive Eu anomalies in cumulate anorthosites. The magnitude of the Eu anomaly quantifies the role of plagioclase in the magmatic history. Cerium can be oxidized to Ce4+ in surface environments, making it insoluble and causing it to be removed from seawater onto oxide surfaces. Seawater has a pronounced negative Ce anomaly; marine precipitates inherit this signature.

In sedimentary geochemistry, REE patterns trace provenance. Sediments derived from felsic continental sources have negative Eu anomalies, LREE enrichment, and high total REE. Sediments from mafic sources have flatter patterns without Eu anomalies. Marine authigenic minerals (phosphorites, carbonates, iron formations) inherit the REE pattern of the seawater from which they precipitated, preserving a record of marine chemistry -- including Ce anomalies as a proxy for ocean oxygenation -- through geological time.
