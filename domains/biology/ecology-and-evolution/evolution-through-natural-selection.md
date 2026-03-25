---
id: evolution-through-natural-selection
title: Evolution Through Natural Selection
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-genetics-intro
  type: hard
- id: probability-axioms-and-rules
  type: soft
- id: probability-rules-for-events
  type: soft
- id: natural-selection-types-and-examples
  type: soft
- id: life-history-evolution-r-and-k-selection
  type: soft
builds-toward:
- microevolution-and-macroevolution
- evidence-for-evolution
tags:
- evolution
- mechanisms
- natural-selection
stage: formal-systems
status: validated
---
# Evolution Through Natural Selection

## Core Idea
Natural selection acts on heritable variation within populations: individuals with traits better suited to their environment tend to survive and reproduce more successfully, passing advantageous traits to offspring. Over generations, this differential reproductive success leads to changes in allele frequencies and adaptation. Natural selection is the primary mechanism driving evolution and the diversity of life.

## Questions

```yaml
- question: "A population of bacteria is treated with an antibiotic. Within weeks, most survivors are resistant. What best explains this rapid shift?"
  type: multiple-choice
  options:
    - "The antibiotic caused the bacteria to mutate and develop resistance as an adaptive response to the threat"
    - "The most fit bacteria transferred their resistance directly to neighboring cells, spreading the trait horizontally"
    - "Bacteria with pre-existing resistance mutations survived and reproduced more, increasing the frequency of resistance alleles in each successive generation"
    - "The antibiotic selected for bacteria with better immune systems, which then passed on their stronger immunity"
  answer: 2
  explanation: "Natural selection works on pre-existing heritable variation — it does not create new mutations in response to selective pressure. Bacteria resistant to the antibiotic already existed in small numbers before treatment. When the antibiotic was introduced, susceptible bacteria died while resistant ones survived and reproduced, passing resistance to offspring. Over generations, resistant alleles became common. Option A describes Lamarckian inheritance (organisms adapting in response to need), which is incorrect. Horizontal gene transfer (option B) is a real phenomenon but not 'natural selection.'"

- question: "Stabilizing selection is acting on birth weight in a human population — both very small and very large babies survive less well than babies of intermediate weight. What genetic pattern do you expect over many generations?"
  type: multiple-choice
  options:
    - "The population shifts toward smaller babies as selection consistently removes the largest individuals"
    - "Allele frequencies remain unchanged because stabilizing selection conserves the status quo without affecting genetics"
    - "Variation in birth weight increases as selection favors a wider range of values"
    - "Alleles producing intermediate birth weights increase in frequency; alleles contributing to extreme values decrease"
  answer: 3
  explanation: "Stabilizing selection favors intermediate phenotype values and acts against both extremes, so alleles that push birth weight toward the extremes are selected against in each generation. Over time, those alleles decrease in frequency and phenotypic variation narrows. Option B is a common misconception: stabilizing selection absolutely changes allele frequencies — it just doesn't shift the mean. Option A describes directional selection, not stabilizing."

- question: "Natural selection acts directly on alleles — it evaluates an organism's genetic sequence and selects which alleles persist in the next generation."
  type: true-false
  answer: false
  explanation: "Natural selection acts on phenotypes — the observable traits expressed by organisms — not directly on DNA sequences. An allele that improves survival or reproduction increases in frequency because the organisms carrying it leave more offspring; selection 'sees' the trait (camouflage color, beak shape, disease resistance), not the underlying allele. The allele frequencies then change as a downstream consequence. This distinction matters: recessive alleles in heterozygotes often escape selection because they're not expressed in the phenotype."

- question: "For natural selection to produce evolutionary change across generations, variation in a population must be heritable."
  type: true-false
  answer: true
  explanation: "Heritability is one of Darwin's three required conditions for natural selection to work. If variation is not heritable — if offspring don't tend to resemble parents in the relevant trait — then even dramatic differences in reproductive success cannot change allele frequencies across generations. Non-heritable phenotypic variation (caused by diet, injury, or developmental environment rather than genetics) disappears in each generation and leaves no evolutionary legacy. This is why Darwin's argument requires both variation AND inheritance."

- question: "Explain why individual organisms do not evolve, but populations do. How does this distinction clarify what natural selection actually does?"
  type: short-answer
  answer: "Evolution is defined as a change in allele frequencies across generations in a population. Individual organisms have fixed genomes that do not change during their lifetimes (with minor exceptions like somatic mutation). What changes is which alleles are represented — and how frequently — in the breeding population across successive generations. Natural selection determines which individuals survive and reproduce, thereby influencing which alleles get passed to the next generation. The individual is the unit of selection; the population is the unit of evolution."
  explanation: "This distinction corrects the common misconception that organisms 'adapt' during their lifetimes in response to the environment (Lamarckian thinking). A giraffe doesn't grow a longer neck because it reaches for leaves; giraffes with genetically longer necks happened to survive better and left more offspring, so long-neck alleles became more frequent. The individual giraffe is the same from birth to death. The population, measured across generations, is what changes."
```

## Explainer

From population genetics, you know that populations carry genetic variation — different alleles at many loci — and that allele frequencies can change over generations. Natural selection is the specific mechanism by which allele frequencies change *because some variants improve survival and reproduction in a given environment*. It is not random. Unlike genetic drift, which shuffles allele frequencies by chance, natural selection consistently favors alleles that increase **fitness** — the relative ability of an individual to survive and produce viable offspring.

The logic of natural selection rests on three conditions that Darwin identified, each of which you can verify empirically. First, individuals in a population vary in their traits — some birds have longer beaks, some shorter; some bacteria divide faster, some slower. Second, at least some of that variation is **heritable**, meaning it is passed from parents to offspring through genetic information. Third, variation in traits leads to variation in reproductive success — individuals with certain trait values leave more offspring than others. When all three conditions hold, the traits associated with higher reproduction become more common in the next generation. This is not a theory about intent or design; it is a mechanical consequence of differential reproduction acting on heritable variation.

A concrete example makes the mechanism clear. Consider a population of beetles varying in color from light green to dark brown, living on brown bark. Birds that hunt by sight eat more green beetles because they are easier to spot. Brown beetles survive longer and produce more offspring, and their offspring tend to inherit the darker coloration. Over many generations, the population shifts toward darker colors — not because individual beetles change color, but because darker beetles contribute more genes to each successive generation. The population has **adapted** to its environment through natural selection. If the environment changes — say the bark becomes lighter due to pollution — the direction of selection reverses, and lighter beetles now have the advantage.

Natural selection can take several forms depending on which part of the trait distribution is favored. **Directional selection** shifts the population mean in one direction (as in the beetle example). **Stabilizing selection** favors intermediate values and reduces variation — human birth weight is a classic case, where very small and very large babies have lower survival. **Disruptive selection** favors both extremes over the middle, which can maintain or increase variation in the population and, under the right conditions, lead to speciation. In each case, the principle is the same: heritable traits that increase reproductive success become more common. Over vast stretches of time, this process — repeated across millions of populations encountering diverse environments — produces the adaptation and diversification that account for the extraordinary variety of life on Earth.
