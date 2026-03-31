---
id: biogeochemistry
title: Biogeochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: redox-geochemistry
  type: hard
- id: carbon-isotopes-geochemistry
  type: soft
- id: organic-geochemistry
  type: soft
builds-toward:
- environmental-geochemistry
tags:
- biogeochemistry
- nutrient-cycling
- carbon-cycle
- nitrogen-cycle
- microbial-geochemistry
stage: expert
status: validated
---

# Biogeochemistry

## Core Idea
Biogeochemistry studies the cycling of elements (C, N, P, S, Fe, Mn) through the coupled biological, geological, and chemical processes that link the lithosphere, hydrosphere, atmosphere, and biosphere. Microorganisms are the primary engines: they catalyze thermodynamically favorable redox reactions that would be kinetically inhibited without enzymatic mediation, driving nutrient transformations that control ecosystem productivity, atmospheric composition, and water quality. The major biogeochemical cycles -- carbon, nitrogen, phosphorus, sulfur, and iron -- are interconnected through stoichiometric coupling (Redfield ratios in marine systems: C:N:P = 106:16:1), redox linkages, and microbial metabolic networks. Understanding these cycles is essential for predicting climate feedbacks, managing water quality, and interpreting the geological record of life-environment co-evolution.

## Questions

```yaml
- question: "In the modern ocean, nitrogen fixation (converting N2 to bioavailable NH4+) and denitrification (converting NO3- to N2) are roughly balanced. What would happen to marine primary productivity if denitrification rates doubled without a corresponding increase in nitrogen fixation?"
  type: multiple-choice
  options:
    - "Productivity would increase because more nitrogen would be available"
    - "Productivity would decrease in nitrogen-limited regions because the ocean's inventory of bioavailable nitrogen would decline as more NO3- is converted to unavailable N2, eventually limiting phytoplankton growth"
    - "No effect, because phosphorus limits marine productivity"
    - "Denitrification rate changes cannot affect productivity"
  answer: 1
  explanation: "Much of the ocean is nitrogen-limited: phytoplankton growth depends on the supply of bioavailable nitrogen (NH4+, NO3-). If denitrification removes nitrogen faster than fixation replaces it, the bioavailable nitrogen pool shrinks, reducing productivity. Over geological time, this imbalance would trigger a negative feedback: reduced productivity means less organic matter export, less oxygen consumption in subsurface waters, and less denitrification (which requires suboxic conditions) -- eventually restoring balance. This feedback coupling illustrates the self-regulating nature of biogeochemical cycles."

- question: "The Redfield ratio (C:N:P = 106:16:1) is a fixed biological constant that applies to all marine organisms."
  type: true-false
  answer: false
  explanation: "The Redfield ratio represents the average stoichiometry of marine phytoplankton and dissolved nutrients, but individual species deviate significantly. Diatoms, coccolithophores, and cyanobacteria have different C:N:P ratios depending on nutrient availability, growth rate, and taxonomy. Under phosphorus limitation, organisms accumulate more C and N per P; under nitrogen limitation, C:N increases. The Redfield ratio is a remarkably useful average that emerges from community-level averaging in the deep ocean, but it is not a biological law."

- question: "Explain why the iron and sulfur cycles are tightly coupled in marine sediments."
  type: short-answer
  answer: "In anoxic marine sediments, microbial sulfate reduction produces H2S, which reacts with reactive iron minerals (iron oxyhydroxides) to form iron sulfide minerals (FeS, eventually pyrite FeS2). This coupling means that iron availability limits how much sulfide is trapped in sediments (vs escaping to the water column), while sulfide production controls the redox state of iron. In the geological record, the ratio of reactive iron to total iron and the degree of pyritization are proxies for water column redox conditions. When reactive iron is exhausted and excess H2S accumulates in the water column (euxinia), the coupled Fe-S system records this as high degrees of pyritization and distinctive iron speciation patterns."
  explanation: "Iron and sulfur are coupled through their redox chemistry: iron oxyhydroxides are the primary sink for microbially produced sulfide, and the balance between iron supply and sulfide production determines the redox character of the depositional environment."
```

## Explainer

Biogeochemistry operates at the interface of biology and geology, where microbial metabolism drives the chemical transformations that shape Earth's surface environment. The fundamental insight is that microorganisms catalyze reactions that are thermodynamically favorable but kinetically inhibited at ambient conditions -- they make Earth's surface chemistry work.

The carbon cycle illustrates the biogeochemical approach. Photosynthesis fixes CO2 into organic matter. Most is respired back to CO2 by heterotrophs (the fast cycle, ~120 Gt C/yr). A tiny fraction (~0.1 Gt C/yr) is buried in sediments, removing carbon from the surface system and producing a stoichiometric equivalent of O2. Over geological time, this slow burial cycle has built up atmospheric O2 and stored vast quantities of organic carbon in the lithosphere. The balance between burial and weathering/volcanic return of fossil carbon controls atmospheric CO2 on million-year timescales, while the fast cycle redistributes carbon among atmosphere, ocean, and biosphere on annual to millennial scales.

The nitrogen cycle is the most biologically complex, with unique microbial processes at each oxidation state. Nitrogen fixation (N2 to NH4+, by cyanobacteria and specialized bacteria) converts inert atmospheric N2 to bioavailable form. Nitrification (NH4+ to NO2- to NO3-, by chemoautotrophs) converts ammonium to nitrate. Denitrification (NO3- to N2, by heterotrophs in suboxic conditions) returns nitrogen to the atmosphere. Anaerobic ammonium oxidation (anammox, NH4+ + NO2- to N2) provides an additional pathway. Each step has distinct isotopic fractionation, enabling delta-15N to trace nitrogen cycling in modern and ancient systems.

The phosphorus cycle is uniquely important as the ultimate limiting nutrient on geological timescales. Unlike C, N, and S, phosphorus has no significant gaseous phase and is not redox-sensitive in its common valence state (PO4 3-). Its supply to the ocean is controlled by continental weathering, and its removal is primarily through burial in marine sediments (organic P, authigenic apatite, iron-bound P). Because phosphorus limits total ocean productivity on long timescales, and because organic carbon burial couples to O2 accumulation, the phosphorus supply rate ultimately regulates atmospheric oxygen -- making phosphorus weathering a master variable in Earth system evolution.
