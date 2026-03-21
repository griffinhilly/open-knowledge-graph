---
id: parapatric-speciation
title: Parapatric Speciation
domain: biology
course: evolutionary-biology
prerequisites:
- id: speciation
  type: hard
- id: gene-flow
  type: soft
tags:
- speciation
- gene-flow
- microallopatry
stage: advanced
status: draft
---

# Parapatric Speciation

## Core Idea
Parapatric speciation occurs despite ongoing gene flow between diverging populations, typically driven by strong disruptive selection or polyploidy. Selection for local adaptation can build reproductive isolation faster than gene flow erodes it, particularly in plants with polyploidy. Examples include grass species evolving heavy-metal tolerance on mine tailings.

## Questions

```yaml
- question: "Grass populations on heavy-metal contaminated mine tailings diverge genetically from adjacent populations on normal soil, despite continuous seed and pollen exchange across the boundary. This divergence is possible because:"
  type: multiple-choice
  options:
    - "A physical barrier prevents most gene flow across the mine boundary"
    - "Heavy-metal tolerance alleles arise at such high mutation rates that drift overcomes gene flow"
    - "Selection against metal-intolerant plants on contaminated soil is strong enough to overcome the homogenizing effect of gene flow"
    - "The mine environment causes epigenetic changes that become heritable, bypassing genetic mechanisms"
  answer: 2
  explanation: "This is the textbook example of parapatric speciation in *Anthoxanthum odoratum*. Strong disruptive selection — metal-intolerant plants die quickly on contaminated soil, metal-tolerant plants are less fit on normal soil — creates a steep fitness gradient. Even though pollen and seeds cross the boundary, immigrants have very low fitness in the opposing environment, limiting effective gene flow. Selection strength substantially exceeding migration rate (s >> m) is the fundamental requirement for parapatric divergence. No physical barrier is needed; ecological selection does the work."

- question: "Allopolyploidy can produce immediate reproductive isolation between a new polyploid lineage and its parent species because:"
  type: multiple-choice
  options:
    - "Polyploids grow larger and outcompete diploids, driving the parent to extinction before hybridization can occur"
    - "Genome doubling after hybridization produces a chromosome set that cannot pair properly with either parent species during meiosis, causing hybrid sterility"
    - "Polyploids evolve in geographically isolated refugia and have no opportunity to mate with parental diploids"
    - "The regulatory incompatibilities between duplicated genomes prevent any gene expression and polyploids are always inviable"
  answer: 1
  explanation: "Allopolyploidy (hybridization + genome doubling) produces an organism with a complete chromosome set from each parent species. When this polyploid mates back with either parent, the resulting offspring has an unbalanced chromosome set — one set from the polyploid plus one set from the diploid parent — that cannot complete meiosis properly, causing sterility. The new polyploid is therefore immediately reproductively isolated from both parents, representing instant speciation. This is why polyploidy is a powerful and rapid route to speciation in plants, bypassing the gradual accumulation of genetic incompatibilities."

- question: "In parapatric speciation, reproductive isolation is present before geographic separation occurs — the populations diverge while remaining in contact."
  type: true-false
  answer: true
  explanation: "This is the defining feature of parapatric (and sympatric) speciation, distinguishing it from allopatric speciation. In allopatric speciation, geographic isolation precedes and enables genetic divergence. In parapatric speciation, populations occupy adjacent ranges with a contact zone, and reproductive isolation evolves *in situ* despite ongoing contact. Selection against immigrants and against hybrids — not a physical barrier — is what drives divergence. The key empirical challenge is demonstrating that isolation arose in situ rather than in prior allopatry followed by secondary contact."

- question: "A steep genetic boundary at a contact zone between two populations is strong evidence that they diverged through parapatric speciation rather than through allopatric speciation followed by secondary contact."
  type: true-false
  answer: false
  explanation: "This is a common misinterpretation. Both parapatric speciation and secondary contact after allopatry can produce sharp clines at contact zones. In fact, secondary contact of well-differentiated allopatric populations often produces *sharper* boundaries than in-situ parapatric divergence. Parapatric divergence is more typically associated with a *gradient* of allele frequency change (a broad cline) because ongoing gene flow prevents a sharp break. Distinguishing the two scenarios requires demographic modeling, phylogeographic analysis, and historical biogeographic evidence — a sharp boundary alone is not diagnostic."

- question: "Why is parapatric speciation theoretically more difficult to achieve than allopatric speciation, and what conditions make it possible?"
  type: short-answer
  answer: "In allopatric speciation, a physical barrier eliminates gene flow, allowing populations to diverge freely under any selection pressure. In parapatric speciation, gene flow continuously counteracts divergence, importing maladapted alleles that erode local differentiation. For parapatric speciation to proceed, selection must be strong enough to overcome this homogenizing effect (s >> m), and there must be mechanisms that reduce hybridization at the contact zone — ecological, behavioral, or phenological differences that lower encounter rates between diverging forms. Strong disruptive selection and reinforcement of reproductive barriers are therefore required, making parapatric speciation less likely but not impossible, especially with polyploidy or extreme environmental gradients."
  explanation: "The theoretical requirement for s >> m means parapatric speciation demands extreme ecological contrasts or genomic events (like polyploidy) that produce instant isolation. The challenge is also one of measurement: even if selection is strong, demonstrating that divergence occurred *with* rather than *without* gene flow requires showing that the populations were never geographically isolated during their history of divergence — a difficult inference from current distributions and genomic data."
```

## Explainer

From studying speciation, you know that new species arise when populations accumulate enough genetic and reproductive differences that they can no longer interbreed successfully. The classic model — allopatric speciation — makes this easy to understand because a physical barrier completely stops gene flow, allowing populations to diverge independently. **Parapatric speciation** asks a harder question: can populations diverge into separate species even when they remain in contact and individuals still cross the boundary between them?

The answer is yes, but it requires strong **disruptive selection** — selection that favors different phenotypes in adjacent environments so powerfully that it overcomes the homogenizing effect of gene flow. Imagine a continuous grassland where one patch sits on soil contaminated with heavy metals from an old mine. Grasses growing on contaminated soil experience intense selection for metal tolerance, while those a few meters away on normal soil do not. Seeds and pollen still drift between patches, blending the gene pools. But if metal-intolerant plants die quickly on the mine soil, selection against immigrants is so strong that the two populations begin to diverge genetically despite physical adjacency. Over time, if selection also favors assortative mating — where tolerant plants tend to pollinate other tolerant plants — reproductive isolation can build up. The grass *Anthoxanthum odoratum* on Welsh mine tailings is a textbook example of exactly this process.

**Polyploidy** provides another powerful route to parapatric speciation, particularly in plants. When an individual's entire genome duplicates (autopolyploidy) or when hybridization between two species is followed by genome doubling (allopolyploidy), the result is an organism that is immediately reproductively isolated from its parent population — the chromosome number mismatch causes meiotic failure in hybrids. This new polyploid lineage can coexist alongside its parent species in overlapping or adjacent ranges, qualifying as parapatric. Many crop species, including wheat and cotton, arose through allopolyploidy.

What makes parapatric speciation theoretically challenging is the tension between selection and gene flow. Models show that for divergence to proceed, selection coefficients must be large relative to migration rates, and there must be some mechanism — whether ecological, temporal, or behavioral — that reduces hybridization between the diverging forms. The resulting pattern is often a **cline**, a gradient of genetic or phenotypic change across the contact zone, rather than a sharp boundary. Detecting parapatric speciation in nature requires demonstrating that reproductive isolation evolved *in situ* with ongoing contact, rather than in prior allopatry followed by secondary contact — a distinction that is often difficult to make but is central to understanding how the geographic context of speciation shapes biodiversity.
