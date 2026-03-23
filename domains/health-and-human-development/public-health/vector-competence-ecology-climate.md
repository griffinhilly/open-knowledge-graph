---
id: vector-competence-ecology-climate
title: Vector Competence, Ecology, and Climate Effects
domain: health-and-human-development
course: public-health
prerequisites:
- id: infectious-disease-epidemiology
  type: hard
- id: environmental-health-determinants
  type: soft
builds-toward:
- outbreak-transmission-models
- environmental-epidemiology-assessment
tags:
- vector-borne-disease
- ecology
- climate
stage: expert
status: draft
---

# Vector Competence, Ecology, and Climate Effects

## Core Idea
Vector-borne disease transmission depends critically on vector competence—the mosquito, tick, or other arthropod's biological and behavioral ability to carry and transmit a pathogen. Vector competence is determined by vector species, parasite's extrinsic incubation period, temperature, humidity, and urban ecology. Climate change and urbanization directly affect vector distribution and transmission dynamics, explaining the emergence and geographic expansion of diseases like dengue, Zika, and Lyme disease into new regions.

## How It's Best Learned
Map the geographic range of a vector-borne disease and relate changes over time to temperature and precipitation patterns.

## Common Misconceptions
Assuming all mosquito species transmit the same pathogens—competence varies widely by species and population genetics.

## Questions

```yaml
- question: "Lyme disease transmission by Ixodes ticks has recently appeared in parts of Canada where ticks were present but transmission was historically absent. Which factor best explains the emergence?"
  type: multiple-choice
  options:
    - "The tick has evolved greater biological competence to transmit Borrelia in northern populations"
    - "Human populations in newly affected areas have lower immunity due to lack of prior exposure"
    - "Warming temperatures allow ticks to survive long enough to complete the pathogen's extrinsic incubation period"
    - "Deforestation is bringing humans into closer contact with previously isolated tick habitats"
  answer: 2
  explanation: "Vector competence requires not just vector survival but sufficient lifespan to allow the pathogen to complete its extrinsic incubation period (EIP) — the time needed for the pathogen to develop from ingestion to salivary transmission. If the EIP exceeds the vector's lifespan, transmission cannot occur regardless of tick density. Warming temperatures shorten the EIP and extend tick activity seasons, pushing regions across the threshold where transmission becomes biologically possible. This is the core mechanism connecting climate change to geographic expansion of vector-borne diseases: not merely range extension of the vector, but range extension of viable transmission conditions."

- question: "A tropical city with intermittent tap water supply experiences a dengue outbreak. A nearby city with continuous piped water has no outbreak despite similar temperatures. What best explains the difference?"
  type: multiple-choice
  options:
    - "Higher temperatures in cities with interrupted water make Aedes aegypti more active, increasing biting frequency"
    - "Interrupted water supply forces households to store water in containers, creating ideal Aedes aegypti breeding habitat near human populations"
    - "Piped water systems contain chlorine that kills dengue virus before transmission occurs"
    - "Aedes aegypti only colonizes cities with piped water infrastructure, and is absent from informal settlements"
  answer: 1
  explanation: "Aedes aegypti is an intensely urban mosquito that breeds in small, clean water containers. Intermittent water supply causes households to store water in buckets, drums, and tanks — ideal breeding habitat. This creates high vector density directly adjacent to human populations, driving up the human-biting rate and vectorial capacity. Continuous piped water eliminates the need for container storage, removing the breeding habitat. Option A has the biology backwards: shorter mosquito lifespan (from heat stress) reduces transmission probability, because vectors must survive long enough to complete the EIP. Option C is incorrect — dengue is not waterborne."

- question: "If a mosquito species is found in a region, that is sufficient evidence to conclude it could transmit a vector-borne pathogen if that pathogen were introduced there."
  type: true-false
  answer: false
  explanation: "Vector presence and vector competence are distinct. Competence requires species-specific biological compatibility between vector and pathogen — the pathogen must replicate successfully in that species' midgut cells, disseminate to the salivary glands, and reach transmissible concentrations. Many mosquito species present in dengue-endemic regions never transmit it because they lack this biological compatibility. Additionally, even a competent vector cannot transmit if environmental conditions (primarily temperature) don't allow the pathogen to complete the EIP within the vector's lifespan. Presence is a necessary but far from sufficient condition."

- question: "A 1–2°C rise in average temperature can enable vector-borne disease transmission in entirely new geographic zones where it was previously biologically impossible, not merely shift existing transmission geography."
  type: true-false
  answer: true
  explanation: "This is the central mechanism connecting climate warming to disease emergence. Near the thermal threshold for transmission, the relationship between temperature and EIP completion probability is non-linear — small temperature increases can flip a region from 'impossible' to 'possible.' The key is not that vectors move northward (they already survive there) but that the EIP can now be completed within the vector's lifespan in regions where it previously could not. This explains why dengue has transmitted locally in Florida and southern Europe, and why Lyme disease vectors have colonized Canada — these are not gradual shifts but threshold crossings."

- question: "Why is 'the vector species is present in the region' insufficient to predict that a vector-borne disease will spread there, and what additional conditions must be met?"
  type: short-answer
  answer: "Vector presence establishes only that the arthropod exists in the area. For transmission to occur, three additional conditions must be met: (1) vector competence — the species must be biologically capable of taking up, replicating, and transmitting the specific pathogen (which varies widely by species and even population genetics); (2) EIP completion — the pathogen must complete its extrinsic incubation period within the vector's lifespan, which depends on temperature; and (3) sufficient vectorial capacity — vector density, human-biting rate, and daily survival must be high enough to sustain transmission. Climate and urban ecology affect conditions 2 and 3 simultaneously, which is why their interaction determines whether introduced pathogens establish local transmission."
  explanation: "The distinction matters for surveillance and public health response. Finding a competent vector species in a new region is a warning signal but not a prediction; the full ecological context must be assessed. Conversely, absence of disease despite vector presence may reflect temperature constraints on the EIP rather than absence of vector competence."
```

## Explainer

From infectious disease epidemiology, you know that disease transmission requires a susceptible host, a pathogen, and a route of transmission. For vector-borne diseases, that route runs through a living arthropod — a mosquito, tick, sandfly, or other invertebrate that doesn't just mechanically carry the pathogen but allows it to replicate and mature before transmitting it to a new host. **Vector competence** is the biological capacity of a specific vector species (or population) to take up, maintain, and transmit a pathogen. It is not a binary on/off property — it is a spectrum shaped by the vector's genetic makeup, the pathogen's compatibility with that species' cells, and the environmental conditions governing the interaction.

The concept of the **extrinsic incubation period (EIP)** is central to understanding why temperature matters so much. After a mosquito takes a blood meal from an infected host, the pathogen must replicate within the mosquito's gut, disseminate to the salivary glands, and reach high enough concentrations to be transmitted in a subsequent bite. This takes time — 8–12 days for dengue in *Aedes aegypti* at 28°C, but considerably longer at lower temperatures. At temperatures below a critical threshold, the pathogen simply cannot complete its development cycle before the mosquito dies of old age (mosquito lifespans are also temperature-dependent). This is why vector-borne diseases are geographically constrained by climate: not because the mosquitoes can't survive in colder regions, but because the EIP would exceed the mosquito's lifespan there, making transmission biologically impossible. As average temperatures rise even 1–2°C, the EIP shortens and the geographic zone where transmission is possible expands toward higher latitudes and elevations.

**Vector competence** interacts with **vectorial capacity** — a broader mathematical concept capturing the full transmission potential of a vector population. Vectorial capacity incorporates vector density, human-biting rate, daily survival probability, and the EIP. Small changes in any component can have non-linear effects on transmission: if daily mosquito survival increases from 0.85 to 0.90 (a modest improvement in vector lifespan under warmer, wetter conditions), the probability of surviving long enough to complete the EIP roughly doubles. This is why climate change projections for vector-borne diseases are not incremental — they predict expansion into entirely new geographic zones where transmission was previously impossible. Dengue, endemic in the tropics for decades, has now transmitted locally in Florida, Texas, and southern Europe. Lyme disease vectors (*Ixodes scapularis*) have colonized Canada. These are not accidents but predictable consequences of warming temperatures extending the thermal envelope for transmission.

Urban ecology adds a second driver. **Aedes aegypti** — the primary dengue, Zika, and chikungunya vector — is an intensely urban mosquito that breeds in small, clean water containers: flower pots, discarded tires, bottle caps. Urban expansion creates ideal habitat. Planned cities with good sanitation infrastructure and piped water reduce container breeding; dense informal settlements with intermittent water supply (causing household water storage) create the ideal epidemiological environment. This means that climate change and urbanization are not independent drivers — they interact, and the areas experiencing the most rapid informal urbanization in tropical regions face the compound risk of expanding vector range meeting expanding vector habitat. Effective vector control requires integrating both ecological drivers into surveillance and intervention design.
