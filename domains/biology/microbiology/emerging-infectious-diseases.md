---
id: emerging-infectious-diseases
title: Emerging Infectious Diseases
domain: biology
course: microbiology
prerequisites:
- id: infectious-disease-epidemiology
  type: hard
- id: viral-replication-cycle
  type: soft
- id: antibiotic-resistance-mechanisms
  type: soft
- id: human-microbiome
  type: soft
tags:
- zoonosis
- spillover
- pandemic
- viral evolution
- One Health
- SARS-CoV-2
- pandemic preparedness
stage: advanced
status: validated
---
# Emerging Infectious Diseases

## Core Idea
Emerging infectious diseases are newly identified diseases or diseases that have recently expanded in range, host breadth, or incidence. More than 60% are zoonoses — diseases transmitted from animals to humans via spillover events driven by land use change, wildlife trade, and deforestation that bring humans into novel contact with animal reservoirs. RNA virus mutation rates and genomic reassortment (in segmented viruses like influenza) generate new strains capable of human adaptation. The One Health framework recognizes that human, animal, and environmental health are inseparably linked, and pandemic preparedness requires integrated surveillance at the human-animal-environment interface. HIV (from chimpanzee SIVcpz), SARS-CoV, SARS-CoV-2, Ebola, and Nipah illustrate recurring spillover patterns.

## How It's Best Learned
Trace the spillover and emergence history of HIV — phylogenetic reconstruction linking it to SIVcpz, the colonial-era conditions enabling spread, and the decades of cryptic transmission before recognition. Then apply the same spillover framework to SARS-CoV-2, comparing what was and was not predictable, and what surveillance gaps allowed the pandemic to unfold.

## Common Misconceptions
- Emerging diseases do not arise spontaneously — they represent existing animal pathogens crossing species barriers when ecological or behavioral conditions change.
- Viruses do not reliably evolve toward reduced virulence over time; virulence evolution depends on transmission trade-offs specific to each pathogen-host system.
- Pandemic preparedness is not primarily about stockpiling vaccines; robust surveillance infrastructure, rapid diagnostic capacity, and public health response systems are equally essential.

## Questions

```yaml
- question: "Deforestation in a tropical region brings agricultural workers into sustained contact with bat colonies that were previously isolated. Shortly afterward, a novel viral disease begins spreading in nearby communities. Which explanation best accounts for this emergence?"
  type: multiple-choice
  options:
    - "Deforestation weakened the immune systems of local populations, allowing existing human pathogens to become more virulent"
    - "Deforestation changed ecological conditions that enabled an existing bat virus to spill over into humans, who had no prior immunity to it"
    - "The virus spontaneously mutated in a common human pathogen after humans began clearing the forest"
    - "Bats evolved a more transmissible virus in response to human encroachment on their habitat"
  answer: 1
  explanation: "Emerging infectious diseases do not arise spontaneously — they represent existing animal pathogens crossing species barriers when ecological conditions change. Deforestation is a primary driver because it eliminates the physical separation between wildlife reservoirs and human communities, increasing the frequency of contact and therefore the probability of spillover. The virus already existed in bats; what changed was the opportunity for human exposure. This is the same mechanism behind HIV (from chimpanzees), Ebola (from bats), and Nipah (from fruit bats)."

- question: "A novel influenza strain emerges with surface proteins from both an avian and a human influenza virus. What mechanism most likely produced this combination?"
  type: multiple-choice
  options:
    - "Rapid accumulation of point mutations in the viral RNA polymerase, which gradually shifted antigenicity"
    - "Horizontal gene transfer between influenza and a bacterial co-infection in the same host"
    - "Genomic reassortment — co-infection of a single host cell by two different influenza strains caused viral genome segments to shuffle and combine"
    - "CRISPR-mediated editing of the viral genome during replication in an intermediate host"
  answer: 2
  explanation: "Influenza is a segmented RNA virus with 8 genome segments. When two different influenza strains co-infect the same cell, the segments can mix during replication, producing progeny viruses with novel combinations — a process called genomic reassortment. This mechanism generated the 1918, 1957, 1968, and 2009 pandemic strains. It is distinct from point mutation, which generates gradual antigenic drift. Reassortment can produce entirely new surface protein combinations overnight, which is why novel reassortant strains can evade existing immunity in the entire population."

- question: "Viruses reliably evolve toward reduced virulence over time, because killing the host before transmission is disadvantageous and evolution selects against it."
  type: true-false
  answer: false
  explanation: "This is a common but incorrect generalization. Virulence evolution depends on transmission trade-offs specific to each pathogen-host system. If a pathogen transmits primarily through contact with sick individuals, high virulence is disadvantageous. But if transmission occurs before symptoms appear, or through vectors, or via environmental shedding from corpses, there is no consistent selection pressure toward reduced virulence. Ebola, for example, has not evolved significantly reduced virulence despite decades of outbreaks. The 'inevitable attenuation' idea is a myth — virulence evolution is contingent, not directional."

- question: "More than half of emerging infectious diseases in humans originate as zoonoses — infections that crossed from animal reservoirs into humans."
  type: true-false
  answer: true
  explanation: "Studies of emerging infectious diseases consistently find that over 60% are zoonotic in origin. HIV, SARS-CoV, SARS-CoV-2, Ebola, Nipah, Hendra, Marburg, and many other significant pathogens all originated in animal reservoirs. This pattern reflects the enormous diversity of viruses circulating in wildlife — particularly bats, rodents, and non-human primates — and the increasing frequency of human-wildlife contact. Understanding this pattern is the basis of the One Health framework and motivates wildlife surveillance as a pandemic preparedness strategy."

- question: "Why does presymptomatic infectiousness — the ability to transmit a pathogen before showing symptoms — make a respiratory virus dramatically harder to contain than a virus that only transmits after symptoms appear?"
  type: short-answer
  answer: "When a virus only transmits after symptoms appear, containment is possible: identify sick people, isolate them, trace their contacts, and quarantine exposed individuals. The symptomatic individual is a visible signal for intervention. Presymptomatic transmission breaks this logic: an infected person who feels well continues normal social activity — commuting, attending events, traveling — while actively spreading the virus. By the time symptoms appear and alert the person or their contacts, the virus has already propagated through one or more transmission chains. Contact tracing becomes retrospective rather than prospective, exponential growth is already underway, and containment requires restricting the movement of apparently healthy people at enormous social and economic cost."
  explanation: "This is exactly why SARS-CoV-2 was so much harder to contain than SARS-CoV-1. SARS-CoV-1 was most infectious after symptom onset, enabling containment by isolating the symptomatic. SARS-CoV-2's substantial presymptomatic transmission window made the standard response toolkit far less effective."
```

## Explainer

From your study of infectious disease epidemiology, you understand how pathogens spread through populations and how we measure and model transmission. **Emerging infectious diseases** (EIDs) are the subset of infectious diseases that are either entirely new to humans, have recently expanded their geographic range or host species, or have dramatically increased in incidence. They represent the leading edge of the ongoing evolutionary contest between microbes and their hosts — and understanding why they emerge requires integrating virology, ecology, and public health in ways that no single discipline can accomplish alone.

The most important pattern in emergence is **zoonotic spillover**: the majority of new human infections originate in animal reservoirs. HIV crossed from chimpanzees, SARS-CoV and SARS-CoV-2 likely originated in bats (with possible intermediate hosts), Ebola circulates in bat populations in central Africa, and Nipah virus spills over from fruit bats in South and Southeast Asia. These are not random events. Spillover is driven by ecological disruption — deforestation, agricultural expansion, wildlife trade, and urbanization push humans into closer contact with animals harboring viruses to which we have no immunity. The frequency of spillover events is increasing precisely because these ecological pressures are intensifying globally.

Once a pathogen enters a human host, whether it causes a limited outbreak or a global pandemic depends on its capacity for **sustained human-to-human transmission**. RNA viruses are disproportionately represented among emerging pathogens because their error-prone polymerases (which you studied in viral replication) generate high mutation rates, producing the genetic variation on which natural selection can act. Influenza adds another mechanism — **genomic reassortment** — where co-infection of a single cell with two different influenza strains can shuffle genome segments to produce entirely novel combinations, as occurred in the 1918, 1957, 1968, and 2009 pandemics. A virus that adapts to transmit efficiently via respiratory droplets, has a presymptomatic infectious period (allowing carriers to spread it before they feel sick), and encounters an immunologically naive population has all the ingredients for pandemic spread.

The **One Health framework** responds to these realities by insisting that human health, animal health, and environmental health are inseparable. Surveillance systems that monitor wildlife populations for novel viruses, that track antibiotic resistance in agricultural settings, and that detect unusual disease clusters in human communities are all necessary components of preparedness. The lesson of recent pandemics is not that emergence is unpredictable — in fact, scientists had warned about coronavirus pandemic potential for years before SARS-CoV-2 — but that the gap between scientific warning and institutional response remains dangerously wide. Effective preparedness requires standing diagnostic infrastructure (platforms that can rapidly develop tests for novel pathogens), genomic surveillance networks (to detect and track variants in real time), and public health systems capable of implementing containment measures before exponential growth makes them futile.
