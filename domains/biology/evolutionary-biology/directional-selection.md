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

## Questions

```yaml
- question: "A beneficial allele conferring antibiotic resistance starts at 1% frequency in a bacterial population. Researchers observe that its frequency increases slowly at first, then accelerates, then slows again near fixation. What explains this S-shaped trajectory?"
  type: multiple-choice
  options:
    - "Mutation rate fluctuates across the experiment, causing variable rates of allele introduction"
    - "Selection pressure decreases as resistance becomes common, reducing the advantage"
    - "When rare, most copies are hidden in heterozygotes and selection is inefficient; near fixation, few disfavored copies remain to replace"
    - "Genetic drift dominates when the allele is rare or near fixation, overriding directional selection"
  answer: 2
  explanation: "The S-shaped (logistic) trajectory is an inherent feature of directional selection, not a sign of changing selection pressure. When the beneficial allele is rare, most individuals are homozygous for the ancestral allele and selection acts on relatively few favorable copies. As the allele reaches intermediate frequencies, selection is maximally efficient — many favorable vs. unfavorable comparisons are made each generation. Near fixation, there are few disfavored alleles left to replace, so the rate slows again. This is the expected mathematical trajectory, not an artifact of changing conditions."

- question: "In a population of mice exposed to consistent cold winters, larger mice survive better and reproduce more. Which statement best characterizes directional selection in this scenario?"
  type: multiple-choice
  options:
    - "The population's mean body size will fluctuate around a stable optimum as allele frequencies reach equilibrium"
    - "Both large and small mice will be favored simultaneously, splitting the distribution"
    - "The mean body size will shift upward monotonically over generations, with variation at the small tail decreasing"
    - "Body size will not evolve because it is a polygenic trait not subject to simple directional selection"
  answer: 2
  explanation: "Directional selection consistently favors one extreme (large body size here), causing the population mean to shift in that direction generation after generation. As large-body alleles increase in frequency, small-body alleles are progressively eliminated from the population — reducing variance at the disfavored tail. This contrasts with stabilizing selection (which maintains the mean while reducing variation at both extremes) and disruptive selection (which favors both extremes, increasing variance and potentially splitting the distribution)."

- question: "Under directional selection, variation in the population decreases at the disfavored end of the trait distribution as alleles favoring that extreme are gradually eliminated."
  type: true-false
  answer: true
  explanation: "As directional selection consistently favors one extreme, the alleles producing the disfavored extreme become progressively rarer. This asymmetrically reduces variation: the disfavored tail shrinks while the favored tail may persist or even expand as the mean shifts. If selection continues to fixation, all variation in that trait is eliminated — the population becomes monomorphic for the favored allele. This is distinct from stabilizing selection, which reduces variation at both extremes symmetrically."

- question: "Directional selection produces a constant, linear increase in allele frequency each generation until the favored allele reaches fixation."
  type: true-false
  answer: false
  explanation: "The trajectory is S-shaped (logistic), not linear. Rate of change is slowest when the allele is rare (few favorable copies to select among), fastest at intermediate frequencies (maximum contrast between favored and disfavored), and slowest again near fixation (few disfavored copies left to replace). A constant linear increase would require that the same number of alleles switch each generation regardless of current frequency — this ignores that selection efficiency depends on the frequency of both alleles in the population."

- question: "Why does the rate of allele frequency change under directional selection follow an S-shaped curve rather than increasing at a constant rate, and what does the steepness of the curve reflect?"
  type: short-answer
  answer: "The S-shape arises because selection efficiency depends on the current frequencies of both alleles. When the favored allele is rare, few favorable vs. unfavorable comparisons occur per generation, so change is slow. At intermediate frequencies, both alleles are common and selection acts with maximum efficiency, producing rapid change. Near fixation, few disfavored alleles remain to be replaced, so change slows again. The steepness of the S is controlled by the selection coefficient (s): a strongly favored allele (large s) sweeps rapidly; a weakly favored allele (small s) follows a shallower, longer S-curve and is more vulnerable to genetic drift before it can reach fixation."
  explanation: "This S-shaped dynamic has practical implications for predicting evolutionary change. A beneficial allele can lurk at low frequency for many generations before becoming visible — a period when it is vulnerable to loss by drift. Once it reaches intermediate frequency, the sweep can be rapid. This helps explain why antibiotic resistance can appear to emerge 'suddenly' in clinical settings: the resistance allele may have been present at undetectable low frequency for a long time before selection drove it to dominance."
```

## Explainer

From your understanding of natural selection, you know that differential survival and reproduction can change allele frequencies in a population. The **selection coefficient** you have studied quantifies how much one allele is favored over another. Directional selection is the simplest and most intuitive mode of natural selection: it consistently favors individuals at one extreme of a trait distribution, shifting the population mean in that direction generation after generation.

Picture a bell curve representing body size in a population of mice. If larger mice survive winters better because they retain heat more efficiently, then each generation the largest individuals leave the most offspring, and the average body size creeps upward. The distribution does not just shift its center — it also loses variation at the disfavored (small) tail as those alleles are gradually eliminated. Given enough time and consistent pressure, the favorable allele reaches **fixation** (frequency = 1.0), and the trait distribution stabilizes at a new, shifted mean.

The trajectory of allele frequency change under directional selection follows a characteristic S-shaped (logistic) curve. When a beneficial allele is rare, it increases slowly because most copies are hidden in heterozygotes (especially if the allele is recessive). As it reaches intermediate frequency, selection is most efficient and the allele increases rapidly. As it approaches fixation, the rate slows again because there are fewer copies of the disfavored allele left to replace. The **selection coefficient** (s) controls the steepness of this curve: a strongly favored allele (large s) sweeps to fixation quickly, while a weakly favored allele (small s) takes many more generations and is more vulnerable to interference from genetic drift.

Classic examples of directional selection include the evolution of antibiotic resistance in bacteria (consistent selection for resistance alleles in the presence of antibiotics), industrial melanism in peppered moths (darker moths favored against soot-darkened trees), and the increase in beak depth in Darwin's finches during drought years (larger beaks crack harder seeds). In each case, the environment imposed a consistent fitness advantage on one phenotypic extreme, and the population responded by shifting its mean trait value. Directional selection is the mode of selection most responsible for adaptive evolution — the progressive refinement of traits that match organisms to their environments.
