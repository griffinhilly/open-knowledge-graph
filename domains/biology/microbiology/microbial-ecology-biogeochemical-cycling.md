---
id: microbial-ecology-biogeochemical-cycling
title: Microbial Ecology and Biogeochemical Cycling
domain: biology
course: microbiology
prerequisites:
- id: microbial-ecology-overview
  type: hard
- id: biogeochemical-cycles
  type: hard
builds-toward:
- ecosystem-services
- community-ecology-intro
tags:
- microbial-ecology
- biogeochemical-cycling
- nutrient-cycling
- ecosystem
stage: advanced
status: draft
---

# Microbial Ecology and Biogeochemical Cycling

## Core Idea
Microbes drive planetary biogeochemical cycles: nitrifying bacteria oxidize ammonia to nitrate; denitrifiers return nitrogen to the atmosphere; sulfur-oxidizing and sulfate-reducing bacteria cycle sulfur; methanogenic archaea produce methane from organic matter. Photosynthetic microbes (cyanobacteria, algae) fix CO₂ and produce O₂; heterotrophic bacteria mineralize dead organic matter, releasing nutrients. Disruption of microbial communities by pollution or overuse of antimicrobials impairs ecosystem nutrient cycling.

## Questions

```yaml
- question: "A farmer applies nitrogen fertilizer to increase crop yields. Despite adequate rainfall and sunlight, the crops show nitrogen deficiency symptoms. Soil testing reveals the nitrogen is present in the soil as N₂ gas. Which microbial process failure best explains this?"
  type: multiple-choice
  options:
    - "Nitrifying bacteria have been suppressed, preventing ammonia from being converted to nitrate that plants can absorb"
    - "Nitrogen-fixing bacteria have been outcompeted, preventing N₂ from being converted to ammonia"
    - "Denitrifying bacteria have been excessively active in waterlogged soil, converting nitrate back to N₂ faster than plants can absorb it"
    - "Methanogenic archaea are consuming the nitrogen-containing organic matter before nitrification can occur"
  answer: 2
  explanation: "If nitrogen exists as N₂ in the soil but crops are deficient, the problem is that nitrogen is cycling in the wrong direction — being lost to the atmosphere rather than retained in plant-available form. Denitrifying bacteria use nitrate as a terminal electron acceptor under anaerobic (waterlogged) conditions, reducing NO₃⁻ stepwise back to N₂. This is a natural process that becomes problematic when soils are waterlogged (anaerobic conditions favor denitrifiers) and nitrogen is being lost faster than fixation and nitrification replenish it. Option A (nitrification failure) would leave nitrogen as ammonia, not N₂. Option B (fixation failure) would prevent N₂ conversion to ammonia but would not explain nitrogen already present as N₂."

- question: "What would most likely happen to agricultural soil fertility over decades if all bacteria capable of nitrogen fixation were eliminated from a region's soils?"
  type: multiple-choice
  options:
    - "Minimal effect — atmospheric N₂ can be absorbed directly by plant roots, and the remaining nitrification cycle would maintain fertility"
    - "Fertility would decline because nitrogen fixation is the only route by which atmospheric N₂ enters the biological nitrogen cycle, and losses from denitrification and leaching cannot be replenished without it"
    - "Fertility would increase because fewer bacteria would compete with plants for soil nitrogen"
    - "Fertility would decline only in legume crops, which are uniquely dependent on root-nodule nitrogen fixation; other crops would be unaffected"
  answer: 1
  explanation: "Atmospheric N₂ constitutes about 78% of Earth's atmosphere but is biologically inert — the triple bond can only be broken by nitrogenase, an enzyme found exclusively in certain prokaryotes (rhizobia, cyanobacteria, free-living soil bacteria). Without nitrogen fixation, the only inputs to the biological nitrogen cycle would be lightning-fixed nitrogen (a minor, weather-dependent source) and synthetic fertilizer production (which industrially mimics the Haber-Bosch process). Losses from denitrification, leaching, and crop removal would progressively deplete available nitrogen. Option D is incorrect — all crops require nitrogen, and the atmospheric reservoir is useless without microbial fixation."

- question: "Ancient cyanobacteria were responsible for the Great Oxidation Event approximately 2.4 billion years ago, fundamentally transforming Earth's atmosphere from anoxic to oxygen-rich."
  type: true-false
  answer: true
  explanation: "Cyanobacteria were the first organisms capable of oxygenic photosynthesis — splitting water to release oxygen as a byproduct. Before cyanobacteria, Earth's atmosphere was essentially anoxic (reducing), with little free O₂. Over hundreds of millions of years, photosynthetic cyanobacteria in ancient oceans produced enough oxygen to overwhelm the capacity of reduced minerals to absorb it, leading to the Great Oxidation Event. This transformed atmospheric chemistry, made aerobic metabolism possible, and ultimately enabled the evolution of complex multicellular life. Cyanobacteria remain responsible for roughly 25% of global photosynthetic carbon fixation today."

- question: "Plants can use atmospheric nitrogen (N₂) directly, absorbing it through their leaves and roots; microbes are therefore not essential for nitrogen nutrition in plants."
  type: true-false
  answer: false
  explanation: "Plants cannot fix N₂ — they lack nitrogenase entirely. Plants absorb nitrogen from the soil in the form of nitrate (NO₃⁻) or ammonium (NH₄⁺), both of which are products of microbial metabolism. The biological nitrogen cycle depends completely on prokaryotes: nitrogen fixers to convert N₂ to ammonia, nitrifiers to convert ammonia to nitrate, and decomposers to mineralize organic nitrogen back to inorganic forms plants can absorb. This obligate dependence on microbial metabolism is why disrupting soil microbial communities — through antibiotics, heavy metals, or soil acidification — can collapse agricultural productivity even in soils that appear otherwise adequate."

- question: "Explain why antibiotic contamination of agricultural soils from livestock operations is an ecological concern beyond producing antibiotic-resistant bacteria."
  type: short-answer
  answer: "The biogeochemical cycles that sustain soil fertility — nitrogen fixation, nitrification, denitrification, and organic matter decomposition — depend on specific microbial metabolic capabilities performed by bacteria that are susceptible to antibiotics. If antibiotic contamination suppresses populations of nitrifying bacteria (e.g., Nitrosomonas, Nitrobacter), ammonium accumulates and nitrate availability for plants declines. If nitrogen-fixing bacteria are reduced, less atmospheric N₂ enters the soil cycle. If decomposers are impaired, organic matter accumulates and nutrient mineralization slows. These are not hypothetical concerns — studies have shown that antibiotic-contaminated soils show altered nitrogen cycling and reduced microbial diversity. The stakes extend beyond human medicine to the elemental cycles on which all agricultural productivity depends."
  explanation: "The key insight is that microbes are functional components of ecosystems, not just pathogens and commensals. Each metabolic guild (nitrifiers, fixers, decomposers, denitrifiers) performs a biogeochemical service that multicellular life cannot replicate. Disrupting these communities has systemic consequences for nutrient availability, soil structure, and ecosystem productivity — consequences that can persist long after antibiotic exposure ends because recovering microbial community composition is slow."
```

## Explainer

From your study of microbial ecology and biogeochemical cycles, you understand that microorganisms form complex communities and that elements like carbon, nitrogen, and sulfur cycle through Earth's systems. What ties these concepts together is a remarkable fact: microbes are not merely participants in biogeochemical cycling — they are the indispensable engines. Without microbial metabolism, the nitrogen cycle would stall, carbon would accumulate as undegraded organic matter, and Earth's atmosphere would be unrecognizable.

Consider the **nitrogen cycle** as a case study. Atmospheric N₂ is abundant but biologically inert — the triple bond is extraordinarily stable. Only certain prokaryotes (including cyanobacteria and rhizobia) possess **nitrogenase**, the enzyme that breaks this bond and converts N₂ to ammonia (NH₃) through **nitrogen fixation**. This ammonia enters the soil where **nitrifying bacteria** like *Nitrosomonas* oxidize it first to nitrite (NO₂⁻), then *Nitrobacter* oxidizes nitrite to nitrate (NO₃⁻) — the form most plants absorb. When soils become waterlogged and anaerobic, **denitrifying bacteria** like *Pseudomonas* use nitrate as a terminal electron acceptor instead of oxygen, reducing it stepwise back to N₂ gas that escapes to the atmosphere. Each of these transformations is performed exclusively by microbes, and each represents a different metabolic strategy for extracting energy from nitrogen compounds.

The **carbon cycle** likewise depends on microbial metabolism at every turn. Photosynthetic cyanobacteria and algae fix CO₂ into organic carbon using solar energy — cyanobacteria alone account for roughly 25% of global photosynthetic carbon fixation, and it was ancient cyanobacteria that oxygenated Earth's atmosphere 2.4 billion years ago. On the decomposition side, heterotrophic bacteria and fungi are the planet's primary **decomposers**, breaking down dead organic matter (cellulose, lignin, chitin) and returning carbon to the atmosphere as CO₂ through respiration. In anaerobic environments like wetlands and ruminant guts, **methanogenic archaea** produce methane (CH₄) from acetate or CO₂ + H₂, while **methanotrophic bacteria** in overlying aerobic zones oxidize methane back to CO₂, preventing much of it from reaching the atmosphere. The **sulfur cycle** follows similar logic: **sulfate-reducing bacteria** (like *Desulfovibrio*) use sulfate as an electron acceptor in anaerobic respiration, producing hydrogen sulfide (H₂S), while **sulfur-oxidizing bacteria** (like *Thiobacillus*) harvest energy by oxidizing H₂S back to sulfate.

The practical implications are enormous. Agricultural productivity depends on microbial nitrogen cycling — both the natural fixation by soil bacteria and the nitrification that makes nitrogen available to crops. When excess fertilizer runs into waterways, microbial decomposition of the resulting algal blooms consumes dissolved oxygen, creating **dead zones**. Antibiotic contamination of soils from livestock operations can suppress the very microbial communities that maintain soil fertility. Understanding that these global processes depend on specific microbial metabolic capabilities — nitrogenase, methane monooxygenase, sulfite reductase — means that disrupting microbial communities has consequences far beyond infection: it can destabilize the elemental cycles on which all life depends.
