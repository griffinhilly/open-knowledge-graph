---
id: alkenone-paleothermometry
title: Alkenone Paleothermometry
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: paleoclimate-proxies
  type: hard
- id: ocean-sediment-proxies
  type: soft
builds-toward:
- marine-isotope-stages
- multi-proxy-climate-reconstruction
tags:
- biomarker-paleothermometry
- sea-surface-temperature
- alkenone-index
- paleoceanography
stage: advanced
status: draft
---

# Alkenone Paleothermometry

## Core Idea
Alkenones are long-chain ketones produced by certain coccolithophore algae whose unsaturation degree (UK'37 index) correlates with growth temperature. The ratio of C37:2 to C37:3 alkenones provides a paleothermometer with ~1-2°C accuracy, independent of carbonate and oxygen isotope systematics. This proxy is especially valuable for tropical and warm-water paleoceanography.

## How It's Best Learned
Extract lipids from sediment samples, separate alkenones via chromatography, and measure the C37:2 and C37:3 ratios using gas chromatography. Apply published calibrations to convert UK'37 to SST and compare results with δ18O-derived temperatures from the same sample.

## Common Misconceptions
- Alkenones record growth temperature but may be reworked or transported; assuming in-situ formation without independent age constraints can bias interpretations. - Assuming the UK'37-temperature relationship is global; regional calibrations often improve accuracy.

## Questions

```yaml
- question: "A researcher reconstructs sea surface temperatures using both foram δ¹⁸O and alkenone UK'₃₇ from the same sediment core and finds the two proxies disagree by 3°C in one interval. What is the most scientifically appropriate interpretation?"
  type: multiple-choice
  options:
    - "One proxy must be wrong; discard whichever disagrees with modern analogues for that region"
    - "The disagreement is within combined uncertainties of ±2°C and should be ignored"
    - "The proxies measure temperature through different chemical systems and can be differentially affected by diagenesis, ice-volume effects (δ¹⁸O), or sediment reworking (alkenones) — the disagreement is informative and warrants multi-proxy investigation"
    - "Alkenones are always more reliable than δ¹⁸O in tropical settings, so the foram data should be disregarded"
  answer: 2
  explanation: "Proxy disagreements are scientifically valuable, not merely problematic. Foram δ¹⁸O records both temperature and seawater isotopic composition (which changes with ice volume), so ice-volume corrections introduce uncertainty. Alkenones bypass carbonate chemistry entirely but can be physically reworked from older sediments. A 3°C discrepancy may reflect a real phenomenon (e.g., a freshwater event that shifted seawater δ¹⁸O without changing temperature), diagenetic alteration of one proxy, or reworking. Multi-proxy disagreement demands investigation, not arbitrary dismissal of one record."

- question: "Why does a higher UK'₃₇ value correspond to warmer sea surface temperatures?"
  type: multiple-choice
  options:
    - "Warmer water contains more dissolved carbon, which increases the total alkenone production rate"
    - "The C₃₇:₂ alkenone is more thermally stable and preferentially survives preservation in warmer sediments"
    - "Coccolithophores increase membrane unsaturation at cold temperatures and decrease it at warm temperatures; higher UK'₃₇ means more di-unsaturated (fewer double-bond) alkenones, reflecting warmer growth conditions"
    - "Warmer water dissolves the C₃₇:₃ form preferentially, leaving a higher ratio of C₃₇:₂ in the sediment"
  answer: 2
  explanation: "The biological mechanism is membrane fluidity regulation. At cold temperatures, coccolithophores synthesize more unsaturated alkenones (more double bonds) to maintain membrane flexibility — a form of homeoviscous adaptation. At warm temperatures, more saturated forms (fewer double bonds) maintain appropriate membrane rigidity. UK'₃₇ = [C₃₇:₂] / ([C₃₇:₂] + [C₃₇:₃]): more di-unsaturated (two double bonds, C₃₇:₂) relative to tri-unsaturated (three double bonds, C₃₇:₃) means higher UK'₃₇, reflecting warmer growth temperature."

- question: "Alkenone paleothermometry is particularly valuable because it records temperature through organic molecular structure, making it chemically independent of the carbonate system and a powerful cross-check for oxygen isotope proxies."
  type: true-false
  answer: true
  explanation: "This independence is alkenone paleothermometry's greatest strength. Foram δ¹⁸O records are affected by both temperature and the isotopic composition of seawater (δ¹⁸Osw), which itself varies with ice volume. Disentangling these two signals requires additional corrections. Alkenones record temperature purely through the degree of organic molecular unsaturation — no mineral dissolution, no isotopic fractionation corrections, no ice-volume dependence. In intervals where foram records are complicated by diagenesis or ice-volume uncertainty, alkenones can provide an independent temperature constraint."

- question: "Because alkenones are produced by surface-dwelling coccolithophores, they reliably record sea-floor bottom water temperatures at the sediment site."
  type: true-false
  answer: false
  explanation: "Alkenones are produced in the surface ocean by photic-zone coccolithophores — they record sea surface temperatures (SST), not bottom water temperatures. After the organisms die, the alkenone-containing particles sink and are preserved in the underlying sediment. The preserved UK'₃₇ signal reflects the temperature of the surface waters where the coccolithophores lived and grew, not the deep-water conditions at the sea floor where the sediment accumulates."

- question: "Why is physical reworking of alkenones a concern when reconstructing paleotemperatures, and what independent evidence is needed to rule it out?"
  type: short-answer
  answer: "Alkenones can be transported by bottom currents or bioturbation from older sediment layers into younger ones (or vice versa). If reworked alkenones from a different time period contaminate a sample, the measured UK'₃₇ would reflect a mixture of temperatures from multiple time intervals, biasing the paleotemperature estimate. Independent chronological controls — radiocarbon dating, biostratigraphy, or correlation with well-dated reference cores — are needed to verify that the alkenones in a given sediment horizon actually formed at the time the sediment was deposited."
  explanation: "This is why alkenone paleothermometry is most reliable in sediment cores with good age control and minimal evidence of bioturbation or current winnowing. High-sedimentation-rate sites are generally preferred because reworking mixes a smaller relative fraction of the signal. The concern about reworking is not unique to alkenones — all sedimentary proxies face it — but the fact that alkenone molecules can survive for millions of years makes them particularly susceptible to long-distance reworking from ancient outcrop material in some settings."
```

## Explainer

From your study of paleoclimate proxies, you know that past climates must be reconstructed from indirect indicators preserved in geological archives. Most ocean temperature proxies rely on the chemistry of calcium carbonate shells — oxygen isotope ratios in foraminifera, for example. **Alkenone paleothermometry** offers something different: a temperature record encoded not in mineral shells but in organic molecules produced by photosynthetic algae. This independence from carbonate chemistry makes alkenones a powerful cross-check and, in some settings, a superior alternative.

**Alkenones** are long-chain (C₃₇–C₃₉) unsaturated ketones synthesized by certain species of coccolithophore algae, primarily *Emiliania huxleyi* and *Gephyrocapsa oceanica*. These molecules serve as membrane lipids, and here is the key insight: the organisms adjust the degree of unsaturation in their alkenones in response to growth temperature. At warmer temperatures, they produce more fully saturated (fewer double bonds) alkenones; at cooler temperatures, they produce more unsaturated (more double bonds) forms. The **Uᴷ'₃₇ index** quantifies this by calculating the ratio of di-unsaturated (C₃₇:₂) to the sum of di- and tri-unsaturated (C₃₇:₂ + C₃₇:₃) alkenones. Higher Uᴷ'₃₇ values correspond to warmer sea surface temperatures.

The practical workflow involves extracting lipids from marine sediment cores using organic solvents, separating the alkenone fraction via gas chromatography, and measuring the relative abundance of the C₃₇:₂ and C₃₇:₃ peaks. Published calibrations — derived from global core-top datasets where modern SST is known — convert the measured Uᴷ'₃₇ to temperature, typically with an accuracy of ±1–2°C. The relationship is approximately linear over the 5–28°C range, making it straightforward to apply. However, at very cold temperatures (below ~5°C), the calibration loses sensitivity because the C₃₇:₃ alkenone dominates almost entirely, and at very warm temperatures (above ~28°C), the C₃₇:₂ form dominates, similarly compressing the signal.

One of the greatest strengths of alkenone paleothermometry is that it is chemically independent of the carbonate system. Oxygen isotope proxies from foraminifera are affected by both temperature and the isotopic composition of seawater (which changes with ice volume), requiring corrections that introduce uncertainty. Alkenones bypass this entirely — they record temperature through organic molecular structure, not mineral chemistry. This makes them especially valuable in tropical and subtropical ocean settings where the carbonate proxies may be complicated by dissolution or diagenesis. The tradeoff is that alkenones can be physically reworked — transported by currents or bioturbation from one sediment layer to another — so independent chronological control (radiocarbon dating, biostratigraphy) is essential to ensure the alkenones in a given sediment horizon actually represent the time period of interest.
