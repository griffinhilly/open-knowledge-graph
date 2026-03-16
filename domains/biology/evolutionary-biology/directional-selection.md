---
id: directional-selection
title: Directional Selection
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: selection-coefficient
  type: soft
builds-toward:
- adaptive-radiation
tags:
- selection
- population-dynamics
stage: advanced
status: draft
---

# Directional Selection

## Core Idea
Directional selection consistently favors alleles at one end of a phenotypic distribution, causing mean phenotype to shift monotonically over generations. The allele frequency trajectory is smooth and predictable, eventually reaching fixation unless mutation or drift counterbalance selection.

## Explainer

From your understanding of natural selection, you know that differential survival and reproduction can change allele frequencies in a population. The **selection coefficient** you have studied quantifies how much one allele is favored over another. Directional selection is the simplest and most intuitive mode of natural selection: it consistently favors individuals at one extreme of a trait distribution, shifting the population mean in that direction generation after generation.

Picture a bell curve representing body size in a population of mice. If larger mice survive winters better because they retain heat more efficiently, then each generation the largest individuals leave the most offspring, and the average body size creeps upward. The distribution does not just shift its center — it also loses variation at the disfavored (small) tail as those alleles are gradually eliminated. Given enough time and consistent pressure, the favorable allele reaches **fixation** (frequency = 1.0), and the trait distribution stabilizes at a new, shifted mean.

The trajectory of allele frequency change under directional selection follows a characteristic S-shaped (logistic) curve. When a beneficial allele is rare, it increases slowly because most copies are hidden in heterozygotes (especially if the allele is recessive). As it reaches intermediate frequency, selection is most efficient and the allele increases rapidly. As it approaches fixation, the rate slows again because there are fewer copies of the disfavored allele left to replace. The **selection coefficient** (s) controls the steepness of this curve: a strongly favored allele (large s) sweeps to fixation quickly, while a weakly favored allele (small s) takes many more generations and is more vulnerable to interference from genetic drift.

Classic examples of directional selection include the evolution of antibiotic resistance in bacteria (consistent selection for resistance alleles in the presence of antibiotics), industrial melanism in peppered moths (darker moths favored against soot-darkened trees), and the increase in beak depth in Darwin's finches during drought years (larger beaks crack harder seeds). In each case, the environment imposed a consistent fitness advantage on one phenotypic extreme, and the population responded by shifting its mean trait value. Directional selection is the mode of selection most responsible for adaptive evolution — the progressive refinement of traits that match organisms to their environments.
