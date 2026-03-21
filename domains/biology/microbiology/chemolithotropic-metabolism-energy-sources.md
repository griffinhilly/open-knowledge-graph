---
id: chemolithotropic-metabolism-energy-sources
title: Chemolithotropic Metabolism and Inorganic Energy Sources
domain: biology
course: microbiology
prerequisites:
- id: bacterial-metabolism-overview
  type: hard
- id: nitrogen-fixation-microbiology
  type: soft
builds-toward:
- microbial-succession-and-nutrient-cycling
tags:
- chemolithotrophy
- energy
- metabolism
stage: advanced
status: draft
---

# Chemolithotropic Metabolism and Inorganic Energy Sources

## Core Idea
Chemolithotrophic bacteria oxidize inorganic compounds (H₂S, NH₃, Fe²⁺, H₂) to gain energy, while fixing CO₂ for carbon. These 'autotrophs' include nitrifiers, sulfur oxidizers, and iron oxidizers, and are essential for nutrient cycling. Some are facultative (can also use organic substrates), while others are obligate chemolithotrophs.

## How It's Best Learned
Study enrichment cultures of nitrifying bacteria and sulfur oxidizers. Examine sulfur globule inclusions in sulfur bacteria under microscopy.

## Common Misconceptions
Chemolithotrophs are not common pathogens—most are environmental bacteria. 'Autotrophy' refers to carbon fixation from CO₂, not energy generation; some organotrophs are also autotrophs.

## Questions

```yaml
- question: "Thiobacillus oxidizes H₂S to sulfate while fixing CO₂ for carbon. Which metabolic category best describes this organism?"
  type: multiple-choice
  options:
    - "Heterotroph — it uses inorganic compounds and therefore does not require organic carbon"
    - "Chemolithoautotroph — it obtains energy from inorganic chemical oxidation and carbon from CO₂ fixation"
    - "Photoautotroph — inorganic sulfur oxidation is equivalent to light-driven energy capture"
    - "Chemoheterotroph — it oxidizes sulfur compounds the way heterotrophs oxidize organic compounds"
  answer: 1
  explanation: "The terminology requires distinguishing energy source from carbon source. 'Chemolitho-' indicates energy from inorganic chemical oxidation. 'Autotroph' indicates carbon from CO₂ fixation. Thiobacillus does both, making it a chemolithoautotroph. Option A contains a critical error: 'heterotroph' refers to using organic compounds for carbon, not for energy. Thiobacillus uses CO₂ as its carbon source, so it is an autotroph regardless of its energy source. Autotrophy and heterotrophy describe the carbon axis; chemotrophy and phototrophy describe the energy axis — these are independent classification dimensions."

- question: "Nitrifying bacteria in soil are essential for plant nutrition primarily because:"
  type: multiple-choice
  options:
    - "They fix atmospheric N₂ into ammonia, making nitrogen available where it was absent"
    - "They convert ammonia to nitrate, the form of nitrogen most readily absorbed by plant roots"
    - "They decompose organic matter, releasing ammonia that plants can then absorb directly"
    - "They compete with plants for soil ammonia, stimulating plants to develop more efficient root systems"
  answer: 1
  explanation: "Nitrifying bacteria perform a two-step process: Nitrosomonas oxidizes NH₃ to NO₂⁻, and Nitrobacter oxidizes NO₂⁻ to NO₃⁻ (nitrate). Plants absorb nitrate far more readily than ammonia. Without nitrification, ammonia from decomposition would accumulate in soil but remain relatively inaccessible to most plant roots. Option A describes nitrogen fixation (converting N₂ to ammonia), performed by different bacteria like Rhizobium — nitrifiers start from ammonia, they do not fix N₂. Option C describes decomposers (ammonifiers), a prior step in the nitrogen cycle, not nitrifiers."

- question: "Autotrophy is defined by how an organism obtains energy — autotrophs make their own energy from sunlight or inorganic compounds, while heterotrophs must consume energy from organic compounds."
  type: true-false
  answer: false
  explanation: "Autotrophy refers to carbon source, not energy source. An autotroph fixes inorganic carbon (CO₂) to build organic biomolecules; a heterotroph obtains carbon from organic compounds. Energy source is a separate classification axis: chemotrophs use chemical energy; phototrophs use light energy. A photoautotroph (plant) uses light for energy and CO₂ for carbon. A chemolithoautotroph uses inorganic chemical oxidation for energy and CO₂ for carbon. These axes are independent — there are even photoheterotrophs that use light for energy but require organic carbon. Confusing autotrophy with energy generation is the most common error in this area."

- question: "Chemolithotrophs generally grow more slowly than heterotrophic bacteria because inorganic oxidations yield less free energy than glucose oxidation."
  type: true-false
  answer: true
  explanation: "The amount of ATP harvestable from an oxidation reaction depends on the redox potential difference between electron donor and acceptor. Glucose oxidation provides a large potential difference and yields ~686 kcal/mol. Inorganic electron donors like NH₃, Fe²⁺, and H₂S have smaller potential differences with oxygen, yielding far less ATP per mole of substrate — nitrifying bacteria extract only about 60-70 kcal/mol from ammonia oxidation. This lower energy return requires processing more substrate and results in slower growth. The tradeoff allows chemolithotrophs to thrive in environments where no organic carbon exists, which heterotrophs cannot exploit."

- question: "Why are chemolithotrophs described as 'living off rocks and air,' and why does this metabolic strategy make them ecologically indispensable in environments without organic carbon?"
  type: short-answer
  answer: "Chemolithotrophs use inorganic compounds (H₂S, NH₃, Fe²⁺, H₂ — derived from geological processes, hence 'rocks') as electron donors for energy generation, while fixing atmospheric CO₂ ('air') as their carbon source. This makes them primary producers in environments where no sunlight and no organic carbon are available — deep-sea hydrothermal vents, cave systems, deep subsurface rock formations. They are the base of these food webs, converting chemical energy stored in inorganic compounds into organic biomolecules that support all other organisms in the ecosystem. Without them, these environments would be essentially lifeless."
  explanation: "The ecological significance follows directly from the metabolic strategy: independence from both photosynthesis and pre-existing organic carbon means any environment with inorganic electron donors and CO₂ can support a chemolithotroph community. This explains microbial life in extreme environments and their critical roles in global biogeochemical cycling — nitrification, sulfur cycling, and iron oxidation are all chemolithotroph-mediated processes."
```

## Explainer

From your study of bacterial metabolism, you know that all organisms need two things: an energy source to drive cellular work and a carbon source to build biomolecules. Most organisms you have encountered so far — including the heterotrophs covered in earlier topics — get both from organic compounds like glucose. **Chemolithotrophs** break this pattern entirely: they harvest energy by oxidizing inorganic molecules and fix CO₂ from the atmosphere for carbon. They are, in effect, living off rocks and air.

The logic is the same redox chemistry you already understand. In aerobic respiration, glucose is the electron donor and oxygen is the terminal electron acceptor, with the energy from electron transfer captured as a proton gradient that drives ATP synthase. Chemolithotrophs use inorganic electron donors instead of glucose. **Nitrifying bacteria** like *Nitrosomonas* oxidize ammonia (NH₃) to nitrite, and *Nitrobacter* oxidizes nitrite to nitrate — each step releasing electrons that feed into an electron transport chain. **Sulfur-oxidizing bacteria** like *Thiobacillus* oxidize hydrogen sulfide (H₂S) or elemental sulfur to sulfate. **Iron-oxidizing bacteria** convert ferrous iron (Fe²⁺) to ferric iron (Fe³⁺). In each case, oxygen typically serves as the terminal electron acceptor, and the resulting proton motive force drives ATP synthesis by the same chemiosmotic mechanism used in mitochondria.

The energy yields from these inorganic oxidations are typically much lower than from glucose oxidation, because the redox potential difference between donor and acceptor is smaller. This means chemolithotrophs grow slowly compared to heterotrophs — but they can thrive in environments where no organic carbon exists. They are the primary producers in deep-sea hydrothermal vent ecosystems, acid mine drainage, and deep subsurface rock formations. Some are **obligate chemolithotrophs**, unable to use organic compounds at all, while others are **facultative**, switching to organic substrates when available.

The ecological importance of these organisms is difficult to overstate. Nitrifying bacteria drive the nitrogen cycle by converting ammonia (which plants cannot easily use) into nitrate (which plants absorb readily). Sulfur oxidizers prevent toxic H₂S accumulation in soils and aquatic sediments. Iron oxidizers influence mineral weathering and soil formation. Without chemolithotrophs cycling these inorganic compounds, the biogeochemical cycles that sustain all life on Earth would grind to a halt. They also have practical applications: bioleaching uses iron- and sulfur-oxidizing bacteria to extract metals from low-grade ores, and nitrifying bacteria are essential in wastewater treatment for removing ammonia.
