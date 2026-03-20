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
stage: advanced
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

## Explainer

From infectious disease epidemiology, you know how to quantify transmission dynamics—reproduction numbers, serial intervals, incubation periods. From emerging infectious diseases, you know that novel disease emergence is shaped by environmental change, animal-human interfaces, and pathogen evolution. Vector-borne diseases sit at the convergence of these frameworks: they add a third biological actor—the **arthropod vector**—whose ecology, life history, and distribution determine whether a pathogen can reach a human host at all.

The key distinction in vector-borne disease is between **vector competence** and **vector capacity**. Competence is a binary biological property: can this arthropod species become infected with a pathogen and transmit it to a new host? Not every mosquito species can transmit malaria or dengue—the pathogen must survive the midgut, replicate, and migrate to the salivary glands to become transmissible. *Anopheles* mosquitoes are competent for malaria; *Aedes aegypti* and *Aedes albopictus* are competent for dengue and Zika; most other mosquito species are not. Capacity is a quantitative ecological concept: even a competent vector species transmits more in some environments than others, depending on its density, biting frequency, survival rate (which determines whether the pathogen has time to complete its **extrinsic incubation period** inside the vector), and the density of susceptible human hosts. The vectorial capacity equation formalizes these relationships and explains why two regions with the same vector species can have very different transmission intensities.

The **extrinsic incubation period (EIP)** is one of the most important concepts in vector-borne disease. It is the time from when a vector takes an infectious blood meal to when it can transmit the pathogen in a subsequent bite. For malaria (*Plasmodium falciparum*), the EIP is 10–12 days at 25°C but extends dramatically in cooler temperatures—which is why malaria transmission collapses at higher altitudes and latitudes. For dengue virus, the EIP is similarly temperature-sensitive. This is the precise mechanism by which climate change expands vector-borne disease range: as mean temperatures rise in previously cool regions, the EIP shortens enough to enable sustained transmission, and vector species that previously couldn't establish viable populations now can.

The reservoir structure of different vector-borne diseases explains why control strategies differ so fundamentally. Malaria's reservoir is humans—infected people are the source of parasites for mosquitoes, which then transmit to other humans. This means that reducing human-mosquito contact (bed nets, indoor residual spraying) directly interrupts transmission and that treating infected people reduces the infectious reservoir. West Nile virus, by contrast, cycles primarily between birds and *Culex* mosquitoes; humans are **dead-end hosts** who become infected when infected mosquitoes bite them but don't amplify transmission because viral titers in human blood are too low to infect feeding mosquitoes. This means treating sick people doesn't reduce transmission, and control must focus on reducing mosquito populations or bird-mosquito contact in the enzootic cycle.

**Integrated vector management (IVM)** combines multiple strategies because reliance on any single approach creates vulnerability. Chemical control (insecticides) can reduce vector populations rapidly but drives insecticide resistance evolution when applied uniformly and continuously—the genetics of resistance selection work exactly as they do in antibiotic resistance. **Larval source reduction** (eliminating standing water where *Aedes* mosquitoes breed) targets vectors before they become adults and is resistance-proof. **Biological control** (introducing *Bacillus thuringiensis israelensis*, larvivorous fish, or the Wolbachia bacterium that reduces dengue transmission in *Aedes*) adds further tools. Combining these approaches, rotating insecticide classes, and monitoring resistance levels represents the evidence-based standard—mirroring the combination therapy principle you'll encounter in antibiotic stewardship and cancer treatment.
