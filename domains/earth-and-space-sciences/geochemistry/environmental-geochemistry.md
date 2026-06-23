---
id: environmental-geochemistry
title: Environmental Geochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: aqueous-geochemistry
  type: hard
- id: redox-geochemistry
  type: hard
- id: biogeochemistry
  type: soft
- id: sedimentary-geochemistry
  type: soft
- id: weathering-soil-chemistry
  type: soft
builds-toward: []
tags:
- environmental-geochemistry
- contamination
- remediation
- heavy-metals
- water-quality
stage: expert
status: validated
---

# Environmental Geochemistry

## Core Idea
Environmental geochemistry applies geochemical principles to understand the sources, transport, fate, and remediation of contaminants in natural systems. Contaminant behavior is controlled by the same thermodynamic and kinetic processes that govern natural geochemistry: speciation (which determines toxicity and mobility), adsorption (which retards transport), precipitation/dissolution (which creates sinks and sources), and redox transformations (which change mobility and toxicity). Key contaminant classes include heavy metals (As, Pb, Cd, Cr, Hg), radionuclides (U, Cs, Sr), organic pollutants, and excess nutrients. Understanding the geochemical controls on contaminant behavior enables prediction of plume migration, risk assessment, and design of remediation strategies that work with natural processes rather than against them.

## Questions

```yaml
- question: "Hexavalent chromium (Cr6+, as chromate CrO4 2-) is a mobile, toxic groundwater contaminant. A remediation strategy involves injecting a reducing agent to convert Cr6+ to Cr3+. Why does this transformation reduce both mobility and toxicity?"
  type: multiple-choice
  options:
    - "Cr3+ is radioactive and decays to a non-toxic element"
    - "Cr3+ is highly insoluble at near-neutral pH (forming Cr(OH)3 precipitates), immobilizing it in the aquifer matrix, and it is far less toxic than Cr6+ because it does not cross cell membranes as readily as the chromate oxyanion"
    - "The reducing agent destroys the chromium atoms"
    - "Cr3+ is volatile and escapes to the atmosphere"
  answer: 1
  explanation: "Cr6+ exists as the chromate oxyanion, which is soluble and mobile in groundwater across a wide pH range, and is a potent carcinogen because it enters cells through sulfate transport channels. Cr3+ is a cation that forms insoluble hydroxide precipitates at pH > 5, effectively immobilizing it. Cr3+ is also far less toxic, being an essential trace nutrient at low concentrations. This redox-based remediation exploits the dramatic difference in geochemical behavior between the two oxidation states."

- question: "Dilution of contaminated groundwater by clean recharge water is sufficient to remediate most groundwater contamination plumes."
  type: true-false
  answer: false
  explanation: "Dilution reduces concentrations but does not remove the contaminant mass. Sorbed contaminants desorb slowly, dissolved-phase NAPL (non-aqueous phase liquid) dissolves over decades, and mineral-hosted contaminants (e.g., arsenic on iron oxides) can be released by changing redox or pH conditions. Effective remediation must address the source, not just the dissolved plume. Natural attenuation (biodegradation, sorption, precipitation) can work for some contaminants but requires demonstration that it is occurring at sufficient rates. Most contamination requires active intervention at the source zone."

- question: "Explain why acid mine drainage (AMD) can have pH values below 2 and extremely high dissolved metal concentrations."
  type: short-answer
  answer: "When sulfide minerals (primarily pyrite, FeS2) are exposed to oxygen and water during mining, they oxidize: FeS2 + 3.5O2 + H2O -> Fe2+ + 2SO4 2- + 2H+. The sulfuric acid produced drops pH dramatically. At low pH, Fe2+ is oxidized to Fe3+ (catalyzed by iron-oxidizing bacteria like Acidithiobacillus), and Fe3+ acts as an additional oxidant for pyrite (Fe3+ + FeS2 -> Fe2+ + S/SO4 + H+), creating a self-sustaining acid-generation cycle. The extremely low pH dissolves other metal-bearing minerals (Cu, Zn, Cd, Pb, As sulfides and secondary minerals), producing metal concentrations orders of magnitude above natural levels. AMD can persist for decades to centuries after mining ceases if sulfide source material remains exposed."
  explanation: "The autocatalytic nature of AMD -- where the product (Fe3+) accelerates the reaction -- explains why it is so persistent and severe. Bacterial catalysis increases the Fe2+ to Fe3+ oxidation rate by factors of 10^5-10^6."
```

## Explainer

Environmental geochemistry is applied aqueous and redox geochemistry in the service of environmental protection. The same principles that govern natural water-rock interaction also control contaminant behavior -- speciation, sorption, precipitation, redox transformation -- but with the added complexity of anthropogenic source terms and regulatory thresholds.

Metal contaminant mobility is controlled by speciation and sorption. Arsenic illustrates the complexity: As(V) (arsenate) adsorbs strongly onto iron oxyhydroxides at near-neutral pH, providing a natural attenuation mechanism. But if redox conditions become reducing, the iron oxyhydroxides dissolve (reductive dissolution), releasing both iron and adsorbed arsenic. Simultaneously, As(V) is reduced to As(III), which adsorbs less strongly. The result is arsenic mobilization under reducing conditions -- the mechanism responsible for the arsenic crisis in South and Southeast Asian aquifers. Understanding these coupled redox-sorption processes is essential for predicting contaminant behavior.

Organic contaminant fate is governed by biodegradation, sorption to organic matter, and volatilization. Chlorinated solvents (TCE, PCE) are denser than water (DNAPLs) and sink to the bottom of aquifers, creating persistent source zones that dissolve slowly over decades. Biodegradation under anaerobic conditions can transform TCE to less-chlorinated products (reductive dechlorination), but incomplete dechlorination can produce vinyl chloride -- more toxic than the parent compound. This is why understanding the geochemical and microbiological conditions along a plume is critical: the wrong conditions produce worse contaminants.

Remediation design leverages geochemical processes. Permeable reactive barriers use zero-valent iron to reductively dechlorinate solvents or precipitate metals as the groundwater flows through. In-situ bioremediation stimulates microbial degradation by adding electron donors or acceptors. Monitored natural attenuation relies on demonstrating that natural processes (biodegradation, dispersion, sorption) are reducing contaminant concentrations at rates sufficient to protect receptors. In each case, the remediation strategy must be grounded in site-specific geochemical characterization to succeed.
