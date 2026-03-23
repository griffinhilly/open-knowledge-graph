---
id: extinction-rates-phylogenetic-patterns
title: Extinction Rates and Phylogenetic Patterns
domain: biology
course: ecology-and-evolution
prerequisites:
- id: extinction-and-recovery
  type: soft
- id: molecular-evolution-phylogenetics
  type: soft
builds-toward:
- conservation-genetics-effective-size
- invasive-species-ecological-impacts
tags:
- extinction
- rates
- phylogenetic-patterns
- turnover
- mass-extinction
stage: formal-systems
status: draft
---

# Extinction Rates and Phylogenetic Patterns

## Core Idea
Extinction rates vary over geological time and across lineages. Mass extinctions alter ecosystem composition and create radiative opportunities. Modern extinction rates exceed background rates by orders of magnitude, driven by habitat loss, climate change, and invasive species.

## Questions

```yaml
- question: "Conservation funds are limited. Two species are at equal extinction risk: Species A is the last member of a lineage that diverged from all other living organisms 300 million years ago; Species B is one of 80 closely related species in a recently diversified clade. From a phylogenetic conservation perspective, which deserves higher priority?"
  type: multiple-choice
  options:
    - "Species B, because protecting one of 80 is more likely to preserve the clade's genetic diversity"
    - "Species A, because it represents a unique, irreplaceable branch of evolutionary history that cannot be recovered"
    - "Neither — extinction risk should be the only criterion, not phylogenetic position"
    - "Species B, because recently diversified clades are more evolutionarily active and therefore more valuable"
  answer: 1
  explanation: "Phylogenetic conservation prioritization values evolutionary uniqueness, not just species count. Species A's loss would remove an entire branch of the tree of life representing 300 million years of unique evolutionary history — metabolic pathways, developmental innovations, ecological roles found nowhere else. Losing one of 80 closely related species in a diverse clade is a much smaller loss of evolutionary heritage, since relatives preserve most of the clade's evolutionary information. This 'evolutionary distinctiveness' principle now formally informs frameworks like EDGE (Evolutionarily Distinct and Globally Endangered) conservation scoring."

- question: "Modern extinction rates compared to the background extinction rate are estimated to be approximately:"
  type: multiple-choice
  options:
    - "2–5 times higher, reflecting normal variation in extinction pressure across geological periods"
    - "10–20 times higher, consistent with an accelerated but not catastrophic extinction event"
    - "100–1,000 times higher, suggesting we may be entering a sixth mass extinction"
    - "Equal to or slightly below background rates, because conservation efforts have effectively offset habitat loss"
  answer: 2
  explanation: "The best estimates place modern extinction rates at 100 to 1,000 times the background rate of approximately 0.1–1 species per million species-years. This is the empirical basis for proposals that we are entering a sixth mass extinction comparable to the five recognized events in Earth's history. Option A and B understate the magnitude; option D contradicts the evidence. The wide range (100–1,000×) reflects genuine uncertainty in background rate estimation and in how many modern extinctions go undetected in poorly studied groups."

- question: "Extinction risk tends to cluster on the tree of life because traits that increase vulnerability — such as small range size, large body size, and slow reproduction — are often shared among close relatives."
  type: true-false
  answer: true
  explanation: "Phylogenetic conservatism means closely related species tend to share traits — including traits that affect extinction risk. Large body size, for example, is characteristic of entire mammalian orders; slow reproduction characterizes entire primate lineages; specialized diets characterize entire clades of beetles. When a stressor (habitat fragmentation, hunting) targets species with one of these traits, it tends to remove whole branches of the phylogenetic tree rather than random species. This non-random pattern means that the diversity loss from modern extinctions is disproportionately large: we are losing evolutionarily distinctive lineages, not just random leaves."

- question: "After mass extinctions, biodiversity typically recovers within tens of thousands of years through rapid adaptive radiation of surviving lineages."
  type: true-false
  answer: false
  explanation: "Recovery from mass extinctions takes millions, not thousands, of years. Even the explosive mammalian radiation after the end-Cretaceous extinction — one of the fastest post-extinction diversifications in the fossil record — required roughly 10–20 million years to produce the ecological and taxonomic diversity that existed before. The end-Permian extinction's recovery took even longer. This temporal scale has stark implications: even if extinction pressures were eliminated today, the evolutionary heritage destroyed by a mass extinction event cannot be restored on any timescale relevant to human civilization."

- question: "Why does a phylogenetic approach provide a better measure of the severity of the modern extinction crisis than simply counting how many species are lost?"
  type: short-answer
  answer: "Species counts treat all extinctions as equal, but they are not evolutionarily equivalent. Losing one species from a clade of 200 closely related species removes relatively little unique evolutionary information — the remaining 199 preserve most of the clade's genetic diversity, biochemical pathways, and ecological adaptations. Losing the only surviving member of an ancient, species-poor lineage removes an entire branch of the tree of life — millions of years of unique evolutionary history with no close relatives to preserve it. Phylogenetic approaches quantify how much evolutionary heritage is at stake, enabling prioritization that preserves the maximum breadth of life's diversity."
  explanation: "Metrics like 'phylogenetic diversity' (the summed branch lengths of the evolutionary tree represented by a set of species) capture this distinction. Conservation frameworks like EDGE explicitly weight species by both extinction risk and evolutionary distinctiveness. This phylogenetic lens also reveals that current extinctions are disproportionately affecting evolutionarily isolated lineages — amphibians, reptiles, and certain mammalian orders — making the tree of life thinner in ways that species counts alone do not capture."
```

## Explainer

From your understanding of extinction and recovery dynamics and molecular phylogenetics, you know that species go extinct, that life has rebounded from catastrophic losses, and that evolutionary relationships can be reconstructed from molecular data. Extinction rates and phylogenetic patterns bring these ideas together by asking: how fast do lineages disappear, which lineages are most vulnerable, and what does the tree of life look like after major extinction events?

The **background extinction rate** is the steady, low-level pace at which species disappear during normal geological time — roughly 0.1 to 1 species per million species-years for most well-studied groups. This baseline allows individual species turnover without disrupting ecosystem structure. Against this background, Earth has experienced five recognized **mass extinctions** — events where extinction rates spiked to tens or hundreds of times the background rate, eliminating 50–95% of species in geologically brief intervals. The end-Permian extinction (~252 million years ago) wiped out an estimated 90% of marine species; the end-Cretaceous (~66 million years ago) famously eliminated non-avian dinosaurs. Each mass extinction reshaped the phylogenetic tree by pruning entire clades, not just individual species.

Extinction is not phylogenetically random. Some lineages are consistently more vulnerable than others, and phylogenetic analysis reveals why. Species with small geographic ranges, low population sizes, slow reproduction, specialized diets, or large body sizes tend to face higher extinction risk — and these traits are often phylogenetically conserved, meaning closely related species share them. The result is that extinction tends to cluster on the tree of life, removing entire branches rather than plucking random leaves. When a mass extinction eliminates a major clade, it opens ecological space that surviving lineages can radiate into — the explosive diversification of mammals after the dinosaur extinction is the most familiar example. These **adaptive radiations** fill vacated niches and reshape biodiversity for millions of years.

Modern extinction rates are estimated at 100 to 1,000 times the background rate, driven primarily by habitat destruction, climate change, overexploitation, and invasive species. This has led some biologists to propose that we are entering a **sixth mass extinction**. Phylogenetic approaches are critical for assessing this claim: by mapping threat status onto evolutionary trees, conservation biologists can identify not just how many species are at risk, but how much unique evolutionary history would be lost. Losing the last species in an ancient, species-poor lineage (like the tuatara or the coelacanth) eliminates far more evolutionary heritage than losing one species from a large, recently diversified clade. This phylogenetic perspective now informs conservation prioritization, helping allocate limited resources to preserve the greatest breadth of the tree of life.
