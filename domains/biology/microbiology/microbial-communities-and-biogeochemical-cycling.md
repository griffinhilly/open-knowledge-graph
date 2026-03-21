---
id: microbial-communities-and-biogeochemical-cycling
title: Microbial Communities and Biogeochemical Cycling
domain: biology
course: microbiology
prerequisites:
- id: microbial-ecology-overview
  type: hard
- id: biogeochemical-cycles
  type: hard
builds-toward:
- symbiosis-commensalism-parasitism-microbes
tags:
- ecology
- cycling
- communities
stage: advanced
status: draft
---

# Microbial Communities and Biogeochemical Cycling

## Core Idea
Microbial communities drive global biogeochemical cycles (C, N, S, P). Bacteria and archaea oxidize and reduce these elements, generating energy and biomass. Anaerobic respiration, methanogenesis, and fermentation are critical in sediments, oceans, and anaerobic digesters. Microbial activities recycle nutrients and regulate climate.

## Questions

```yaml
- question: "Scientists add a broad-spectrum antibiotic to ocean sediments, killing most bacteria and archaea. What do you predict happens to the nitrogen cycle in those sediments?"
  type: multiple-choice
  options:
    - "Nitrogen cycling continues normally since plants and algae can perform nitrogen fixation"
    - "Only denitrification is affected since all other steps can proceed abiotically"
    - "Nitrogen fixation, nitrification, and denitrification are all severely disrupted since each step requires specific microorganisms"
    - "Nitrogen cycling accelerates since competition between microbes normally slows the process"
  answer: 2
  explanation: "Every enzymatic step in the nitrogen cycle — nitrogen fixation (requires nitrogenase, found only in certain bacteria and archaea), nitrification (NH₃→NO₂⁻ by Nitrosomonas; NO₂⁻→NO₃⁻ by Nitrobacter), denitrification (NO₃⁻→N₂ by denitrifying bacteria), and anammox — requires specific microorganisms. Plants cannot fix atmospheric N₂; algae and plants assimilate nitrate and ammonia but cannot perform the redox transformations that cycle nitrogen between oxidation states. Removing the microbial community doesn't just slow the cycle — it breaks it. This is the key insight: microorganisms are the engines, not assistants."

- question: "In an anaerobic digester, hydrogen (H₂) concentration rises abnormally high due to a disturbance. What is the most likely consequence for the microbial community's function?"
  type: multiple-choice
  options:
    - "Methanogens produce more methane since hydrogen is their primary substrate"
    - "Fermenting bacteria accelerate polymer breakdown to consume the excess hydrogen"
    - "High hydrogen concentration thermodynamically inhibits acetogens, causing fatty acid accumulation and disrupting the entire metabolic chain"
    - "The community self-corrects rapidly since microbial communities have redundant metabolic pathways"
  answer: 2
  explanation: "This tests the syntrophic (metabolic handoff) concept. Acetogens convert fatty acids to acetate and H₂ — but this reaction is thermodynamically favorable only when H₂ concentration is low. When H₂ accumulates, the acetogenesis reaction becomes unfavorable and stalls. Fatty acids accumulate and acidify the system. Methanogens (which consume H₂) cannot compensate fast enough. The entire chain — fermenters → acetogens → methanogens — grinds to a halt. This illustrates why microbial community function depends on tight metabolic coupling: disrupting one link breaks the whole chain."

- question: "Microorganisms are important participants in biogeochemical cycling, but plants, animals, and abiotic processes perform the fundamental transformations — like nitrogen fixation and nitrification — that move elements between chemical forms."
  type: true-false
  answer: false
  explanation: "This is the central misconception the topic addresses. Nitrogen fixation requires nitrogenase, which is found only in certain bacteria and archaea — no plant, animal, or abiotic process can break the N₂ triple bond under ambient conditions (except lightning, which contributes negligibly). Nitrification (oxidation of ammonia to nitrate) is performed exclusively by nitrifying bacteria. Denitrification is exclusively microbial. Methanogenesis is exclusively archaeal. Microorganisms are not participants alongside other agents; they are the indispensable engines. Remove them, and the cycles stop."

- question: "Microbial community composition directly determines ecosystem function in biogeochemical cycling because the product of one species' metabolism typically becomes the substrate for another species."
  type: true-false
  answer: true
  explanation: "This metabolic handoff principle — syntrophy — means that biogeochemical cycles are not performed by individual species but by community-level metabolic chains. In nitrogen cycling, nitrogen fixers produce ammonia for nitrifiers, who produce nitrate for denitrifiers. In anaerobic sediments, fermenting bacteria produce fatty acids for acetogens, who produce acetate for methanogens. If any species is lost, its substrates accumulate and its products become scarce, disrupting downstream steps. This is why microbial community structure (which species are present and at what abundances) is not just ecologically interesting — it directly determines whether and how fast these cycles operate."

- question: "Why is no single microbial species sufficient to complete a full biogeochemical cycle? What does this tell us about the relationship between microbial community composition and ecosystem function?"
  type: short-answer
  answer: "No single organism has evolved the full suite of enzymes needed to perform every transformation in a biogeochemical cycle, and in many cases individual transformations require extreme metabolic specializations that are incompatible with each other. Nitrogen fixation requires nitrogenase, which is irreversibly inactivated by oxygen — so nitrogen fixers often live in anaerobic microenvironments or protect nitrogenase with specialized structures. Aerobic nitrifiers require oxygen that would destroy nitrogen fixers. Denitrifiers require anaerobic conditions that aerobic nitrifiers cannot tolerate. Each step in the cycle is performed by organisms with incompatible metabolic requirements. This means biogeochemical cycles are emergent properties of microbial communities — they exist only when the right combination of species with complementary metabolisms are present and their metabolic outputs are coupled. If species are lost (through pollution, habitat change, or climate warming), the metabolic chain breaks, intermediate compounds accumulate, and cycles slow or fail. Community composition is thus the proximate determinant of ecosystem function."
  explanation: "The practical implication is that threats to microbial diversity are not merely about preserving biodiversity for its own sake — they threaten the functional integrity of processes like carbon burial, nitrogen availability, and methane flux that regulate Earth's climate and the productivity of ecosystems that humans depend on."
```

## Explainer

You already understand the basic structure of biogeochemical cycles — how carbon, nitrogen, sulfur, and phosphorus move between biotic and abiotic reservoirs — and you have an overview of microbial ecology. What this topic makes explicit is that **microorganisms are not just participants in these cycles; they are the engines that drive them**. Plants and animals contribute to biogeochemical cycling, but the transformations that close the loops — converting dead organic matter back to inorganic forms, fixing atmospheric gases into biologically available compounds, and mediating the redox chemistry that moves elements between oxidation states — are overwhelmingly performed by bacteria and archaea.

Consider the **nitrogen cycle** as a concrete example. Atmospheric N₂ is chemically inert — the triple bond between the two nitrogen atoms requires enormous energy to break. Only certain bacteria and archaea possess **nitrogenase**, the enzyme that reduces N₂ to ammonia (NH₃) in a process called **nitrogen fixation**. Without these microbes (free-living species like *Azotobacter* and symbiotic species like *Rhizobium* in legume root nodules), the biologically available nitrogen pool would eventually be depleted. Once fixed as ammonia, nitrogen passes through a microbial relay: **nitrifying bacteria** like *Nitrosomonas* oxidize NH₃ to nitrite (NO₂⁻), and *Nitrobacter* oxidizes nitrite to nitrate (NO₃⁻) — both steps are chemolithoautotrophic, meaning these organisms use inorganic nitrogen as their energy source. Nitrate can then be assimilated by plants and microbes, or it can be returned to the atmosphere as N₂ by **denitrifying bacteria** under anaerobic conditions. Every step in this cycle — fixation, nitrification, denitrification, and the anaerobic ammonium oxidation (anammox) discovered more recently — is exclusively microbial.

The same principle applies to **carbon and sulfur cycling**. In the carbon cycle, microbial decomposers mineralize organic matter back to CO₂ through aerobic respiration, while **methanogens** (strictly anaerobic archaea) produce methane (CH₄) in wetlands, rice paddies, and ruminant guts — making them major contributors to greenhouse gas emissions. Methanotrophic bacteria then oxidize methane back to CO₂, partially offsetting this flux. In the sulfur cycle, **sulfate-reducing bacteria** like *Desulfovibrio* use SO₄²⁻ as a terminal electron acceptor in anaerobic environments, producing hydrogen sulfide (H₂S) — the rotten-egg smell of anoxic mud. **Sulfur-oxidizing bacteria** then reoxidize H₂S back to sulfate, completing the cycle. These microbial redox transformations are not incidental side reactions; they represent the primary metabolic strategies by which entire communities of organisms generate ATP. The biogeochemical cycle is, from the microbe's perspective, an energy-harvesting strategy.

What makes microbial communities — rather than single species — so important is the concept of **metabolic handoffs**. No single organism performs all the transformations in a biogeochemical cycle. Instead, the product of one species' metabolism becomes the substrate for another's, creating tightly coupled **syntrophic relationships**. In anaerobic digesters, for example, fermenting bacteria break down complex organic polymers into volatile fatty acids, acetogenic bacteria convert those acids to acetate and hydrogen, and methanogenic archaea consume the acetate and hydrogen to produce methane. If any step in this chain stalls, intermediates accumulate and the entire community's metabolism grinds to a halt. This interdependence means that microbial community composition directly determines ecosystem function — and why disrupting microbial communities (through pollution, land use change, or climate warming) can have cascading effects on global nutrient cycling and atmospheric chemistry.
