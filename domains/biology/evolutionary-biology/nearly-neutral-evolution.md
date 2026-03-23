---
id: nearly-neutral-evolution
title: Nearly Neutral Evolution and Drift-Selection Balance
domain: biology
course: evolutionary-biology
prerequisites:
- id: neutral-theory-evolution
  type: hard
- id: genetic-drift
  type: hard
- id: effective-population-size
  type: hard
builds-toward:
- molecular-evolution-rates
- slightly-deleterious-mutations
tags:
- neutral-theory
- drift
- selection
- molecular-evolution
stage: advanced
status: validated
---

# Nearly Neutral Evolution and Drift-Selection Balance

## Core Idea
Mutations with selection coefficients of order 1/(2Ne) evolve under combined influence of drift and weak selection. These 'nearly neutral' mutations have fixation rates between neutral and selected expectations, prevalent in genomic evolution.

## Questions

```yaml
- question: "A mutation has a selection coefficient of s = -0.0002 (slightly deleterious). Population A has Ne = 500; Population B has Ne = 50,000. What nearly neutral theory predicts is:"
  type: multiple-choice
  options:
    - "The mutation is equally likely to reach fixation in both populations because the selection coefficient is the same"
    - "The mutation behaves nearly neutrally in Population A (where 1/2Ne ≈ 0.001) but is efficiently purged in Population B (where 1/2Ne ≈ 0.00001)"
    - "The mutation is efficiently selected against in both populations because any negative s value enables selection to act"
    - "The mutation will fix faster in Population B because large populations have more total selection events per generation"
  answer: 1
  explanation: "Nearly neutral theory defines the boundary between drift-dominated and selection-dominated evolution as |s| ≈ 1/(2Ne). In Population A (Ne = 500), 1/(2Ne) ≈ 0.001, which is larger than |s| = 0.0002 — so the mutation is effectively neutral and drifts. In Population B (Ne = 50,000), 1/(2Ne) ≈ 0.00001, which is much smaller than |s| = 0.0002 — so selection efficiently purges this deleterious mutation. The same mutation has a different effective fate depending on population size."

- question: "Nearly neutral theory predicts that species with chronically small effective population sizes should, compared to species with large populations:"
  type: multiple-choice
  options:
    - "Have faster rates of adaptive evolution because drift accelerates beneficial mutation fixation"
    - "Accumulate more slightly deleterious substitutions, larger genomes, and more repetitive DNA"
    - "Show the same substitution rates as large-population species for all mutation types"
    - "Evolve higher mutation rates to compensate for reduced efficacy of selection"
  answer: 1
  explanation: "With small Ne, the drift threshold 1/(2Ne) is large, meaning a wider range of weakly deleterious mutations escape purifying selection and can drift to fixation. This predicts accumulation of slightly deleterious substitutions, growth of non-functional sequences (pseudogenes, repetitive elements), and genomic complexity. This pattern is empirically supported: mammals (small Ne) show more genomic bloat than bacteria or Drosophila (large Ne). Option A is wrong — drift can fix beneficial mutations faster but also fixes deleterious ones, net lowering fitness."

- question: "A mutation's fate under nearly neutral theory is determined primarily by its selection coefficient alone — population size affects the speed of fixation but not whether drift or selection dominates."
  type: true-false
  answer: false
  explanation: "This is the most common misconception nearly neutral theory corrects. Whether drift or selection dominates depends on both the selection coefficient AND effective population size together. Specifically, when |s| < 1/(2Ne), drift dominates regardless of the direction or magnitude of s within that range. Population size is not merely a speed parameter — it determines which evolutionary force governs the mutation's fate. A mutation with s = -0.001 is nearly neutral in a population of Ne = 100 (where 1/(2Ne) = 0.005) but strongly selected against in Ne = 10,000 (where 1/(2Ne) = 0.00005)."

- question: "Nearly neutral theory extends Kimura's neutral theory rather than replacing it — strictly neutral mutations still evolve according to Kimura's rules, and the nearly neutral category captures an additional class of mutations."
  type: true-false
  answer: true
  explanation: "Nearly neutral theory was developed by Tomoko Ohta as an extension of, not a replacement for, Kimura's neutral theory. Strictly neutral mutations (s = 0) still fix at a rate equal to the mutation rate, drift according to 1/(2Ne) sampling, and obey Kimura's predictions exactly. The nearly neutral category adds a gray zone: mutations with |s| small but nonzero, whose fates depend on both drift and selection in proportion to how |s| compares to 1/(2Ne). Together, the two frameworks explain a broader range of molecular evolution than either alone."

- question: "Why does effective population size determine whether a mutation with a small selection coefficient is 'effectively neutral,' and what does this imply for genomic differences between species with very different population sizes?"
  type: short-answer
  answer: "Natural selection can only 'see' a mutation if its fitness effect is large relative to the random sampling noise of genetic drift. That noise has magnitude approximately 1/(2Ne) — smaller populations have more drift, larger populations less. When |s| is smaller than 1/(2Ne), drift overwhelms selection and the mutation's fate is determined primarily by chance, not fitness. Species with small Ne (like mammals) have a large drift threshold, so a wide range of weakly deleterious mutations escape purifying selection and accumulate. Species with large Ne (like bacteria or Drosophila) have a tiny drift threshold, so even weak selection can efficiently purge deleterious variants and fix beneficial ones. The consequence is that large-Ne species have tighter functional constraint, leaner genomes, and faster adaptive evolution, while small-Ne species accumulate genomic bloat — not because of different mutation rates, but because of different selection efficacy."
  explanation: "This Ne-dependent model explains a major puzzle in comparative genomics: why mammalian genomes are so much larger and more repetitive than bacterial genomes. The answer is not more mutation but less ability to remove weakly deleterious insertions, duplications, and pseudogenes. Population size is the hidden variable that links molecular evolution rates to organismal life history."
```

## Explainer

Kimura's neutral theory, which you've already studied, drew a sharp line: mutations are either neutral (invisible to selection, governed entirely by drift) or selected (their fate determined by fitness effects). But real genomes are full of mutations that fall in a gray zone — slightly deleterious or slightly beneficial, with selection coefficients so small that drift can override selection. **Nearly neutral theory**, developed by Tomoko Ohta, fills this critical gap by asking what happens when the strength of selection and the strength of drift are comparable.

The boundary between "neutral" and "selected" is set by **effective population size (Ne)**, your other key prerequisite. A mutation with selection coefficient *s* behaves effectively as neutral when |*s*| is roughly equal to or less than **1/(2Ne)**. In a population of Ne = 10,000, any mutation with |*s*| < 0.00005 drifts almost as if it were strictly neutral. But the same mutation in a population of Ne = 100 would need |*s*| < 0.005 to be effectively neutral — a hundred-fold wider window. This means that **population size determines how much of the genome evolves by drift versus selection**. Small populations are "blind" to weakly selected mutations that large populations can efficiently purge or fix.

This has a striking prediction: species with smaller effective population sizes should accumulate more slightly deleterious substitutions, because drift overwhelms weak purifying selection. Empirically, this is exactly what we observe. Organisms with large populations (bacteria, Drosophila) show tighter functional constraint and less genomic bloat, while organisms with small populations (mammals, island species) accumulate more mildly harmful mutations, more pseudogenes, and more repetitive DNA. The nearly neutral framework also predicts that substitution rates for weakly selected sites should vary with population size, unlike strictly neutral sites where the substitution rate equals the mutation rate regardless of Ne.

Nearly neutral theory does not replace the neutral theory — it extends it. Strictly neutral mutations still exist and still follow Kimura's rules. But the nearly neutral category captures a large fraction of genomic changes, especially in non-coding regions and at synonymous sites where selection coefficients are real but tiny. By connecting population size to the efficiency of selection, Ohta's framework explains patterns that pure neutrality cannot: why genomes differ so dramatically in size and complexity across species, and why the molecular clock ticks at different rates in different lineages.
