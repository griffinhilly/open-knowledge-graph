---
id: trace-element-geochemistry
title: Trace Element Geochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: geochemical-thermodynamics
  type: hard
builds-toward:
- partition-coefficients
- ree-patterns-geochemistry
- mantle-geochemistry
tags:
- trace-elements
- incompatible-elements
- compatible-elements
- spider-diagrams
stage: expert
status: validated
---

# Trace Element Geochemistry

## Core Idea
Trace elements (concentrations <0.1 wt%) obey Henry's Law in dilute solutions within minerals and melts, meaning their behavior is governed by partition coefficients rather than stoichiometric constraints. Elements are classified as compatible (preferentially entering the solid phase during melting, e.g., Ni, Cr, Co) or incompatible (preferentially entering the melt, e.g., Rb, Ba, Th, U, Nb, La). During partial melting, incompatible elements are strongly concentrated in small melt fractions, while compatible elements remain in the residue. This partitioning creates systematic abundance patterns in igneous rocks that encode information about the degree of melting, source composition, crystal fractionation history, and tectonic setting. Normalized multi-element diagrams (spider diagrams) and REE plots are the standard visualization tools.

## Questions

```yaml
- question: "A basalt has 300 ppm Ni and 500 ppm Cr, while a co-genetic rhyolite has 5 ppm Ni and 10 ppm Cr. What process explains this dramatic difference?"
  type: multiple-choice
  options:
    - "The rhyolite source contained less Ni and Cr"
    - "Fractional crystallization of olivine (which strongly incorporates Ni) and clinopyroxene/spinel (which incorporate Cr) from the basaltic parent magma removed these compatible elements from the melt, producing a highly depleted residual liquid that eventually became the rhyolite"
    - "Weathering of the rhyolite removed Ni and Cr"
    - "Ni and Cr are radioactive and decayed during the rhyolite's longer cooling time"
  answer: 1
  explanation: "Ni has a very high partition coefficient in olivine (D ~10-30) and Cr is highly compatible in spinel and clinopyroxene. During fractional crystallization, each increment of olivine removal drastically depletes Ni in the remaining melt. After extensive fractionation, evolved melts (andesites, dacites, rhyolites) have extremely low compatible-element concentrations. This depletion pattern is diagnostic of fractionation from a mafic parent."

- question: "An incompatible element with a partition coefficient of 0.01 will be enriched by a factor of 100 in a 1% partial melt relative to the source."
  type: true-false
  answer: true
  explanation: "For batch melting at low melt fractions, the concentration in the melt approaches C_source/D (when F << D). With D = 0.01 and F = 0.01, the enrichment factor is C_melt/C_source = 1/(D + F(1-D)) = 1/(0.01 + 0.01*0.99) = ~50. For very small F approaching zero, the enrichment approaches 1/D = 100. This extreme enrichment of highly incompatible elements in small melt fractions is why alkalic basalts (small degree melts) are enriched in incompatible elements relative to tholeiites (larger degree melts)."

- question: "Explain what a primitive-mantle-normalized spider diagram reveals about a subduction zone basalt that a simple major-element analysis cannot."
  type: short-answer
  answer: "A spider diagram plots a suite of trace elements (ordered by incompatibility) normalized to primitive mantle values. Subduction zone basalts show a characteristic pattern: enrichment in large-ion lithophile elements (LILE: Rb, Ba, K, Sr) and light REE, but depletion in high-field-strength elements (HFSE: Nb, Ta, Ti, Zr). The LILE enrichment reflects addition of fluid-mobile elements from the dehydrating subducted slab. The HFSE depletion reflects the retention of these elements in residual rutile and other refractory minerals in the slab. This Nb-Ta 'trough' on the spider diagram is the definitive geochemical fingerprint of subduction-related magmatism, invisible in major-element data."
  explanation: "The spider diagram reveals the selective element transfer from slab to mantle wedge: fluid-mobile elements are transferred (LILE enrichment) while fluid-immobile elements are retained (HFSE depletion)."
```

## Explainer

Trace elements are the fingerprints of geological processes. While major elements (Si, Al, Fe, Mg, Ca, Na, K) define the rock type (basalt vs. granite), trace elements resolve the processes that produced it: how much the mantle melted, what minerals crystallized from the magma, whether subducted sediment or fluids were involved, and what was left behind in the source.

The partition coefficient D (concentration in mineral / concentration in melt) is the fundamental parameter. For olivine, D_Ni ~10-30 (nickel is strongly compatible), while D_La ~0.001 (lanthanum is strongly incompatible). During partial melting, an element with D << 1 concentrates almost entirely in the melt, especially at small melt fractions. An element with D >> 1 remains locked in the residual solid. The batch melting equation, C_melt = C_source / (D + F(1-D)), quantifies this for any element and any melt fraction F.

Multi-element diagrams normalize trace element concentrations to a reference (primitive mantle, chondrite, or N-MORB) and plot them in order of decreasing incompatibility. The resulting pattern contains enormous information. A smooth, downward-sloping pattern indicates derivation from a depleted mantle source by moderate to large degrees of melting (like N-MORB). A steep, enriched pattern indicates small-degree melting of an enriched source (like ocean island basalts). Negative anomalies at specific elements (Nb, Ti depletion in arc basalts; Eu anomalies in plagioclase-fractionated rocks) diagnose specific mineral controls.

The power of trace element geochemistry lies in the fact that different elements respond differently to the same process: a single melting event simultaneously enriches Ba 100-fold while barely affecting Yb. This differential behavior creates patterns that constrain not just whether melting occurred, but the degree, depth, and residual mineralogy of the melting event -- information that major elements alone cannot provide.
