---
id: molecular-dating-phylogenetic-clocks
title: Molecular Clocks and Phylogenetic Dating
domain: biology
course: ecology-and-evolution
prerequisites:
- id: molecular-clock
  type: hard
- id: phylogenetic-inference-methods
  type: hard
- id: exponential-growth-and-decay
  type: soft
- id: statistics-rigorous
  type: soft
- id: exponential-distribution-theory
  type: soft
- id: molecular-dating-fossil-calibration
  type: soft
builds-toward:
- molecular-evolution-rates
tags:
- molecular-clock
- dating
- evolution
- phylogenetics
stage: formal-systems
status: validated
---
# Molecular Clocks and Phylogenetic Dating

## Core Idea
The molecular clock hypothesis assumes substitutions accumulate at relatively constant rates in DNA or proteins, allowing divergence time estimation. Rates vary among genes, lineages, and sites; relaxed clock models accommodate this variation. By calibrating molecular clocks with fossil dates, we estimate divergence times for groups lacking good fossils and test whether molecular predictions match paleontological dates.

## Questions

```yaml
- question: "Two insect lineages are compared by molecular phylogenetics, and their sequences differ by a known number of substitutions. Without any fossil calibration points, what can researchers confidently conclude?"
  type: multiple-choice
  options:
    - "The exact divergence time in years, by applying a universal substitution rate derived from well-studied vertebrate lineages"
    - "That lineage A diverged twice as long ago as lineage B if its sequence divergence from the outgroup is twice as large"
    - "The relative divergence of the two lineages compared to each other, but not their absolute ages in years"
    - "Nothing interpretable, because molecular clocks are only valid when fossil evidence is already available"
  answer: 2
  explanation: "Sequence differences alone provide relative divergence — you can say lineage A and B are more or less divergent than lineage C and D, but not how many million years have passed. Converting sequence differences into absolute time requires knowing the substitution rate, and calibrating that rate requires an independent time anchor (typically a fossil). Without calibration, you have a relative timeline with no scale bar. Applying substitution rates from unrelated groups (e.g., vertebrates applied to insects) is unreliable because rates vary substantially across lineages."

- question: "A phylogenetic study uses a strict molecular clock and finds that its divergence date estimates for rodents are systematically younger than paleontological evidence suggests, while whale estimates are too old. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The fossil calibrations were mistakenly set as maximum ages rather than minimum age constraints"
    - "Violation of the strict clock assumption: rodents evolve faster than whales, and forcing a single rate across both lineages produces biased estimates for both"
    - "Rodent genomes have fewer neutral sites available for substitution, reducing their apparent evolutionary rate"
    - "The strict clock model applies only to mitochondrial DNA; nuclear genes require a relaxed clock"
  answer: 1
  explanation: "A strict clock assumes a single substitution rate across all lineages. Rodents are known to have faster molecular evolution than whales (shorter generation time, higher metabolic rate). If a single rate is forced onto the data, it will be a compromise — overestimating the time needed for slowly-evolving lineages (making whale dates too old) and underestimating the time for fast-evolving lineages (making rodent dates too young). Relaxed clock models solve this by allowing rates to vary across branches, producing more accurate estimates when rate heterogeneity is present."

- question: "Fossil calibration points used in molecular dating are typically treated as minimum age constraints for the node they calibrate, because the true divergence event must have predated the first appearance of fossils from that lineage."
  type: true-false
  answer: true
  explanation: "Correct. Fossilization is a rare, improbable event, and the oldest known fossil of a group is almost certainly younger than the actual divergence. A lineage must exist before it can leave fossils, and fossil preservation depends on many taphonomic factors. Therefore, a fossil dated to 65 million years ago tells us the divergence occurred at least 65 million years ago — but possibly earlier. In Bayesian molecular dating, this is encoded as a minimum age prior on the relevant node, with a probability distribution that allows for older dates."

- question: "When molecular dating estimates disagree with paleontological divergence dates, the molecular clock estimate should generally be trusted over the fossil record, because molecules provide more direct evidence of evolutionary time."
  type: true-false
  answer: false
  explanation: "Neither source of evidence automatically trumps the other. Molecular clock estimates can be wrong due to rate variation across lineages, poor calibration, model misspecification, or violation of the strict clock assumption. Fossil estimates can be wrong due to preservation gaps, misidentification, or incorrect stratigraphic dating. Disagreement is a signal that something needs investigation — it could be an undetected rate acceleration in one lineage, a significant gap in the fossil record, or a calibration error in either direction. The most productive response is to examine both sources critically and seek additional evidence."

- question: "Why can molecular dating estimate divergence times for groups with no fossil record at all, and what is required for this to work?"
  type: short-answer
  answer: "Molecular dating can work for groups without fossils by borrowing calibration information from other parts of the same phylogenetic tree. If a well-calibrated node (with fossil evidence) exists elsewhere in the tree, the substitution rate estimated at that node can be applied — through the relaxed clock model — to poorly-calibrated branches. The result is a complete time-calibrated tree, with dates estimated even for lineages that left no fossil trace."
  explanation: "This is one of the most powerful applications of molecular clocks: recovering the temporal history of groups like fungi, most marine invertebrates, and viruses that have minimal or no fossil records. The key requirements are: (1) at least some calibration nodes elsewhere in the tree from groups with fossils, (2) a good molecular phylogeny showing how the fossil-free group relates to calibrated groups, and (3) appropriate rate models (typically relaxed clocks) that allow rates to vary among lineages rather than forcing an inaccurate single rate onto the whole tree."
```

## Explainer

You already know from the molecular clock hypothesis that DNA and protein sequences accumulate substitutions over time, and from phylogenetic inference that we can reconstruct the branching relationships among species. **Molecular dating** combines these two ideas: if we know the rate at which substitutions accumulate and the number of substitutions separating two lineages, we can estimate when those lineages diverged. The logic is analogous to estimating how long ago two travelers parted by measuring how far apart they are now and knowing their walking speed.

The simplest version assumes a **strict clock** — a single, constant substitution rate across all lineages. Under this model, the number of differences between two sequences is directly proportional to the time since their common ancestor. But real molecular evolution is messier. Substitution rates vary across genes (mitochondrial DNA evolves faster than many nuclear genes), across lineages (rodents evolve faster than whales), and across sites within a gene (functionally constrained sites evolve slowly). A strict clock applied blindly to such data will produce misleading dates, which is why modern phylogenetics uses **relaxed clock models** that allow rates to vary among branches while still estimating divergence times.

The critical step that anchors molecular dates to real time is **calibration**. Sequence differences alone tell you relative divergence — lineage A and B are twice as divergent as lineage C and D — but not absolute time. To convert relative divergence into years, you need at least one point where you independently know the age. Fossil first appearances are the most common calibration points: if the oldest fossil of a group dates to 65 million years ago, that provides a minimum age for the node where that group originated. Calibration fossils are set as constraints (usually minimum ages, since the true divergence must predate the first fossil), and the statistical framework distributes rate estimates across the tree to make all calibrated nodes consistent.

The power of molecular dating is that it lets us estimate divergence times for groups with poor or nonexistent fossil records — fungi, many invertebrate lineages, viruses — by borrowing calibration information from better-preserved relatives. It also serves as an independent check on paleontological dates. When molecular and fossil estimates agree, our confidence in both increases; when they disagree, it signals either rate variation we have not accounted for, fossil gaps, or calibration problems. This interplay between molecular and paleontological evidence is one of the most productive feedback loops in modern evolutionary biology.
