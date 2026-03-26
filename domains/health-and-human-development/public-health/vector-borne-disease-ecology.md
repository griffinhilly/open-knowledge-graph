---
id: vector-borne-disease-ecology
title: Vector-Borne Disease Ecology and Control
domain: health-and-human-development
course: public-health
prerequisites:
- id: infectious-disease-surveillance
  type: soft
- id: emerging-infectious-diseases
  type: hard
- id: community-ecology-intro
  type: soft
- id: infectious-disease-epidemiology
  type: soft
- id: outbreak-investigation
  type: soft
builds-toward:
- one-health-framework
- global-burden-of-disease
tags:
- vector-borne
- malaria
- dengue
- Aedes
- reservoir-host
- vector-control
stage: expert
status: validated
---
# Vector-Borne Disease Ecology and Control

## Core Idea
Vector-borne diseases are transmitted through the bites of living organisms—primarily arthropods such as mosquitoes, ticks, and sandflies—that carry pathogens between hosts. Transmission dynamics depend on vector competence, vector capacity (density, biting rate, survival), the extrinsic incubation period, and the susceptibility of human hosts. Climate change is expanding the geographic range of vectors like Aedes mosquitoes, increasing dengue and Zika transmission at higher latitudes and elevations. Control strategies operate at the vector (insecticides, larval source reduction, biological control), host (personal protection, vaccination), and environmental levels, ideally combined in integrated vector management.

## How It's Best Learned
Compare the transmission cycles of two vector-borne diseases with different reservoir structures—malaria (human reservoir) versus West Nile virus (avian reservoir with humans as dead-end hosts)—and derive why control strategies differ between them.

## Common Misconceptions
- Eliminating the vector entirely is rarely ecologically feasible or desirable; control aims to reduce vector density below transmission thresholds.
- Resistance to insecticides evolves rapidly when a single compound is used uniformly; rotation and combination strategies are required.
- Climate change effects on vector-borne disease are not simply 'more disease everywhere'; they shift geographic distributions and seasonality, sometimes reducing transmission in areas that become too hot or dry.

## Questions

```yaml
- question: "West Nile virus cycles between birds and Culex mosquitoes. Humans become infected when bitten by infected mosquitoes, but infected humans have viral titers too low to infect feeding mosquitoes. What follows for control strategy?"
  type: multiple-choice
  options:
    - "Treating infected humans with antivirals is the primary control approach, since it reduces the infectious reservoir"
    - "Control must focus on reducing mosquito populations or the bird-mosquito transmission cycle, since treating human cases does not interrupt transmission"
    - "Vaccination of humans is the most efficient control strategy since humans are the primary amplifying host"
    - "Eliminating the Culex mosquito species entirely is both feasible and necessary for control"
  answer: 1
  explanation: "Because humans are dead-end hosts — infected humans cannot transmit to feeding mosquitoes — treating sick people does nothing to interrupt the transmission cycle. The virus amplifies between birds (reservoir hosts) and Culex mosquitoes; humans are accidental infections outside this cycle. This contrasts sharply with malaria, where humans ARE the reservoir and treating infections reduces the infectious pool available to mosquitoes. For West Nile, control must target the enzootic cycle: reduce Culex populations through larval source reduction, insecticides, or biological control. Option D is wrong because eliminating a vector species is rarely ecologically feasible or desirable."

- question: "Why does climate warming cause malaria and dengue transmission to expand to higher elevations and latitudes, even in regions where the mosquito vectors are already present?"
  type: multiple-choice
  options:
    - "Warmer temperatures increase human outdoor activity, raising exposure to mosquito bites"
    - "Warmer temperatures shorten the extrinsic incubation period, allowing the pathogen to complete development inside the vector before the mosquito dies"
    - "Warmer temperatures increase mosquito biting rates, increasing the probability of transmission per mosquito-human contact"
    - "Warmer temperatures reduce the effectiveness of insecticides, allowing mosquito populations to grow unchecked"
  answer: 1
  explanation: "The extrinsic incubation period (EIP) is the critical bottleneck. The EIP is the time from when a vector takes an infectious blood meal until it can transmit in a subsequent bite. For malaria at 25°C, EIP is 10–12 days; in cooler temperatures it extends dramatically. Since mosquitoes live only 2–4 weeks, a long EIP means most vectors die before becoming infectious — transmission cannot be sustained. As temperatures rise in previously cool regions, the EIP shortens enough that vectors survive long enough to transmit. This is the precise mechanism linking climate change to range expansion: not just 'more mosquitoes' but 'mosquitoes that live long enough for the pathogen to complete its development.'"

- question: "Integrated vector management aims to eliminate vector species largely, using combined chemical, biological, and environmental strategies to achieve eradication."
  type: true-false
  answer: false
  explanation: "IVM's goal is to reduce vector density below transmission thresholds, not to eliminate the species. Complete elimination of a vector species is rarely ecologically feasible (vectors often have broad geographic ranges and rapid reproductive rates), and elimination of a widespread arthropod species would have unpredictable ecological consequences. The practical target is reducing population density to levels where the basic reproduction number R₀ falls below 1 — at which point transmission cannot be sustained. IVM achieves this through combining larval source reduction, insecticides, biological control, and personal protection, chosen to minimize resistance development and ecological disruption."

- question: "Applying the same insecticide uniformly and continuously across a region will eventually drive the mosquito population to zero as the most susceptible individuals are killed."
  type: true-false
  answer: false
  explanation: "Uniform, continuous insecticide application creates strong directional selection for resistance, following the same evolutionary logic as antibiotic resistance. Mosquitoes with any heritable resistance survive and reproduce; over generations, resistance alleles spread through the population. Rather than driving the population to zero, prolonged uniform exposure drives the population toward resistance, ultimately making the insecticide ineffective. IVM addresses this by rotating insecticide classes (to prevent selection for resistance to any one mechanism), combining with non-chemical methods, and monitoring resistance levels — analogous to the combination therapy and stewardship strategies used for antibiotics."

- question: "Explain why treating infected humans effectively controls malaria but not West Nile virus. What property of the transmission cycle determines whether human treatment reduces overall disease spread?"
  type: short-answer
  answer: "The determining factor is whether humans are amplifying hosts (reservoir) or dead-end hosts. In malaria, humans are the primary reservoir: parasites replicate to high densities in human blood, and infected humans are the source of parasites for feeding mosquitoes. Treating infected humans reduces the infectious reservoir, directly interrupting transmission. In West Nile virus, the parasite amplifies between birds and Culex mosquitoes; human infections are incidental, and viral titers in human blood are too low to infect feeding mosquitoes. Treating human cases removes them from a dead-end branch of the transmission network that doesn't feed back into the cycle."
  explanation: "This distinction — reservoir host vs. dead-end host — is fundamental to designing effective control strategies. It explains why malaria control combines bed nets (reducing human-mosquito contact) with case treatment (reducing the infectious reservoir), while West Nile control focuses entirely on the bird-mosquito cycle. Misidentifying the reservoir leads to misdirected interventions: spending resources treating dead-end human cases for West Nile would have minimal impact on transmission, while neglecting the enzootic cycle would allow virus to continue amplifying. Understanding reservoir ecology before designing interventions is essential to public health practice."
```

## Explainer

From infectious disease epidemiology, you know how to quantify transmission dynamics—reproduction numbers, serial intervals, incubation periods. From emerging infectious diseases, you know that novel disease emergence is shaped by environmental change, animal-human interfaces, and pathogen evolution. Vector-borne diseases sit at the convergence of these frameworks: they add a third biological actor—the **arthropod vector**—whose ecology, life history, and distribution determine whether a pathogen can reach a human host at all.

The key distinction in vector-borne disease is between **vector competence** and **vector capacity**. Competence is a binary biological property: can this arthropod species become infected with a pathogen and transmit it to a new host? Not every mosquito species can transmit malaria or dengue—the pathogen must survive the midgut, replicate, and migrate to the salivary glands to become transmissible. *Anopheles* mosquitoes are competent for malaria; *Aedes aegypti* and *Aedes albopictus* are competent for dengue and Zika; most other mosquito species are not. Capacity is a quantitative ecological concept: even a competent vector species transmits more in some environments than others, depending on its density, biting frequency, survival rate (which determines whether the pathogen has time to complete its **extrinsic incubation period** inside the vector), and the density of susceptible human hosts. The vectorial capacity equation formalizes these relationships and explains why two regions with the same vector species can have very different transmission intensities.

The **extrinsic incubation period (EIP)** is one of the most important concepts in vector-borne disease. It is the time from when a vector takes an infectious blood meal to when it can transmit the pathogen in a subsequent bite. For malaria (*Plasmodium falciparum*), the EIP is 10–12 days at 25°C but extends dramatically in cooler temperatures—which is why malaria transmission collapses at higher altitudes and latitudes. For dengue virus, the EIP is similarly temperature-sensitive. This is the precise mechanism by which climate change expands vector-borne disease range: as mean temperatures rise in previously cool regions, the EIP shortens enough to enable sustained transmission, and vector species that previously couldn't establish viable populations now can.

The reservoir structure of different vector-borne diseases explains why control strategies differ so fundamentally. Malaria's reservoir is humans—infected people are the source of parasites for mosquitoes, which then transmit to other humans. This means that reducing human-mosquito contact (bed nets, indoor residual spraying) directly interrupts transmission and that treating infected people reduces the infectious reservoir. West Nile virus, by contrast, cycles primarily between birds and *Culex* mosquitoes; humans are **dead-end hosts** who become infected when infected mosquitoes bite them but don't amplify transmission because viral titers in human blood are too low to infect feeding mosquitoes. This means treating sick people doesn't reduce transmission, and control must focus on reducing mosquito populations or bird-mosquito contact in the enzootic cycle.

**Integrated vector management (IVM)** combines multiple strategies because reliance on any single approach creates vulnerability. Chemical control (insecticides) can reduce vector populations rapidly but drives insecticide resistance evolution when applied uniformly and continuously—the genetics of resistance selection work exactly as they do in antibiotic resistance. **Larval source reduction** (eliminating standing water where *Aedes* mosquitoes breed) targets vectors before they become adults and is resistance-proof. **Biological control** (introducing *Bacillus thuringiensis israelensis*, larvivorous fish, or the Wolbachia bacterium that reduces dengue transmission in *Aedes*) adds further tools. Combining these approaches, rotating insecticide classes, and monitoring resistance levels represents the evidence-based standard—mirroring the combination therapy principle you'll encounter in antibiotic stewardship and cancer treatment.
