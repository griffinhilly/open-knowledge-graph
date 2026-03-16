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
status: draft
---

# Nearly Neutral Evolution and Drift-Selection Balance

## Core Idea
Mutations with selection coefficients of order 1/(2Ne) evolve under combined influence of drift and weak selection. These 'nearly neutral' mutations have fixation rates between neutral and selected expectations, prevalent in genomic evolution.

## Explainer

Kimura's neutral theory, which you've already studied, drew a sharp line: mutations are either neutral (invisible to selection, governed entirely by drift) or selected (their fate determined by fitness effects). But real genomes are full of mutations that fall in a gray zone — slightly deleterious or slightly beneficial, with selection coefficients so small that drift can override selection. **Nearly neutral theory**, developed by Tomoko Ohta, fills this critical gap by asking what happens when the strength of selection and the strength of drift are comparable.

The boundary between "neutral" and "selected" is set by **effective population size (Ne)**, your other key prerequisite. A mutation with selection coefficient *s* behaves effectively as neutral when |*s*| is roughly equal to or less than **1/(2Ne)**. In a population of Ne = 10,000, any mutation with |*s*| < 0.00005 drifts almost as if it were strictly neutral. But the same mutation in a population of Ne = 100 would need |*s*| < 0.005 to be effectively neutral — a hundred-fold wider window. This means that **population size determines how much of the genome evolves by drift versus selection**. Small populations are "blind" to weakly selected mutations that large populations can efficiently purge or fix.

This has a striking prediction: species with smaller effective population sizes should accumulate more slightly deleterious substitutions, because drift overwhelms weak purifying selection. Empirically, this is exactly what we observe. Organisms with large populations (bacteria, Drosophila) show tighter functional constraint and less genomic bloat, while organisms with small populations (mammals, island species) accumulate more mildly harmful mutations, more pseudogenes, and more repetitive DNA. The nearly neutral framework also predicts that substitution rates for weakly selected sites should vary with population size, unlike strictly neutral sites where the substitution rate equals the mutation rate regardless of Ne.

Nearly neutral theory does not replace the neutral theory — it extends it. Strictly neutral mutations still exist and still follow Kimura's rules. But the nearly neutral category captures a large fraction of genomic changes, especially in non-coding regions and at synonymous sites where selection coefficients are real but tiny. By connecting population size to the efficiency of selection, Ohta's framework explains patterns that pure neutrality cannot: why genomes differ so dramatically in size and complexity across species, and why the molecular clock ticks at different rates in different lineages.
