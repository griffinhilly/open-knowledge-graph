---
id: partition-coefficients
title: Partition Coefficients
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: trace-element-geochemistry
  type: hard
- id: geochemical-thermodynamics
  type: hard
builds-toward:
- ree-patterns-geochemistry
- mantle-geochemistry
tags:
- partition-coefficients
- Kd
- crystal-melt-partitioning
- mineral-chemistry
stage: expert
status: validated
---

# Partition Coefficients

## Core Idea
The partition coefficient (D or Kd) quantifies how a trace element distributes between a mineral and a coexisting melt or fluid: D = C_mineral / C_melt. D depends on the element's ionic radius and charge (compatibility with the crystal site), the mineral's crystal structure, melt composition, temperature, and pressure. Elements whose ionic radius and charge match an available crystal site have high D (compatible); mismatches produce low D (incompatible). The bulk partition coefficient for a rock (D-bulk) is the weighted average of mineral D values, weighted by the modal abundance of each mineral. D-bulk controls whether an element is enriched or depleted during partial melting and fractional crystallization, making it the key parameter linking mantle mineralogy to magma composition.

## Questions

```yaml
- question: "Garnet has a very high partition coefficient for heavy rare earth elements (HREE) like Yb (D ~ 4-7) but low D for light REE like La (D ~ 0.01). How does this affect the REE pattern of a melt produced by partial melting of garnet-bearing mantle?"
  type: multiple-choice
  options:
    - "The melt will have a flat REE pattern"
    - "The melt will be depleted in HREE (retained by garnet in the residue) and enriched in LREE (incompatible in garnet), producing a steep, LREE-enriched pattern diagnostic of deep melting in the garnet stability field"
    - "The melt will be enriched in HREE from the garnet"
    - "Garnet does not affect REE patterns during melting"
  answer: 1
  explanation: "During partial melting, HREE are retained by residual garnet (high D means they stay in the solid), while LREE enter the melt (low D). The resulting melt is strongly LREE-enriched and HREE-depleted. This steep REE pattern is diagnostic of melting at depths >60-80 km where garnet is stable. Shallower melting (spinel peridotite, where no mineral strongly fractionates HREE from LREE) produces flatter REE patterns. REE patterns thus constrain the depth of melting."

- question: "Partition coefficients are fixed physical constants for each element-mineral pair."
  type: true-false
  answer: false
  explanation: "D values depend on temperature, pressure, melt composition, mineral composition, and crystal chemistry. D for REE in clinopyroxene increases with pressure and decreases with temperature. D values in silica-rich melts differ from those in mafic melts. The lattice strain model (Blundy and Wood) provides a physical framework for predicting how D varies: it depends on the elastic strain energy required to substitute a foreign ion into a crystal site, which varies with the size mismatch between the ion and the site. Published D values must be used with attention to the conditions under which they were determined."

- question: "Explain the concept of bulk partition coefficient and why it matters more than individual mineral D values for modeling partial melting."
  type: short-answer
  answer: "The bulk D is the sum of each mineral's D weighted by its mass fraction in the source rock: D-bulk = sum(x_i * D_i), where x_i is the weight fraction and D_i is the mineral-melt partition coefficient. It matters more than individual D values because the partial melting equation uses D-bulk as the aggregate control on element behavior. A highly compatible element in one mineral (e.g., Ni in olivine, D=15) may have a moderate D-bulk (~3-4) if olivine is only 25% of the source. The mineralogy of the source (proportion of olivine, pyroxene, garnet, spinel) directly controls D-bulk and therefore the predicted melt composition."
  explanation: "Individual mineral D values determine the partitioning physics; bulk D integrates the mineralogical reality of the source into a single parameter used in melting models."
```

## Explainer

Partition coefficients are the quantitative link between crystal chemistry and magma geochemistry. They encode, in a single number per element-mineral pair, whether and how strongly an element is incorporated into a crystal structure during magmatic processes.

The physical basis is crystal-chemical. Each mineral has specific crystallographic sites with defined sizes and charges. An element with the right ionic radius and charge for a site enters readily (high D). The lattice strain model formalizes this: D for an element depends on the strain energy penalty for fitting a foreign ion into the site. Elements whose radius matches the site's ideal radius have the highest D; elements too large or too small have exponentially decreasing D. This produces the characteristic parabolic D pattern when plotted against ionic radius -- the basis for predicting D values for elements without experimental data.

In practice, D values are determined experimentally (equilibrating mineral and melt at controlled T-P-X and analyzing both) or empirically (from natural mineral-glass pairs in volcanic rocks). The most important datasets for igneous petrology cover olivine, clinopyroxene, orthopyroxene, garnet, plagioclase, spinel, and amphibole in basaltic to rhyolitic melts. These values populate the melting and crystallization models (batch melting, fractional melting, Rayleigh fractionation) that predict how trace element concentrations evolve during magma genesis and differentiation.

The sensitivity of melt composition to source mineralogy, through D-bulk, is what makes trace elements such powerful probes of mantle processes. The presence or absence of garnet in the mantle source (controlled by pressure/depth) completely changes the HREE behavior and produces diagnostic REE slope differences between shallow and deep-derived magmas. Similarly, the presence of residual amphibole, phlogopite, or accessory phases (rutile, apatite, zircon) selectively retains specific elements, creating the characteristic depletion patterns that fingerprint source mineralogy and tectonic setting.
