---
id: antimicrobial-resistance-population-dynamics
title: 'Antimicrobial Resistance: Selection Pressure and Population Dynamics'
domain: health-and-human-development
course: public-health
prerequisites:
- id: infectious-disease-epidemiology
  type: hard
- id: basic-reproduction-number
  type: soft
builds-toward:
- antimicrobial-stewardship-strategies
- emerging-infectious-disease-surveillance
tags:
- antimicrobial-resistance
- selection
- evolution
stage: abstract-reasoning
status: draft
---

# Antimicrobial Resistance: Selection Pressure and Population Dynamics

## Core Idea
Antibiotic use creates selective pressure favoring resistant bacterial strains through competition for resources and elimination of susceptible competitors. At population scale, resistance emerges and spreads through subtherapeutic dosing, unnecessary prescriptions, and agricultural overuse. Resistance genes spread between bacterial species through horizontal gene transfer, making antimicrobial resistance a community problem requiring population-level interventions, not individual treatment decisions alone.

## How It's Best Learned
Compare antibiotic resistance prevalence trends to antibiotic consumption by country and examine lag relationships.

## Common Misconceptions
Thinking resistant pathogens are less fit—many resistant strains replicate as effectively as susceptible ones, enabling rapid spread.

## Explainer

At its core, antimicrobial resistance is Darwinian natural selection running in real time at the population level. A bacterial population is not genetically uniform — through spontaneous mutation and horizontal gene transfer, it contains individuals with varying sensitivity to antibiotics. When you introduce an antibiotic, you are imposing a severe environmental filter: susceptible bacteria die, resistant bacteria survive and reproduce. The next generation is disproportionately resistant. This selection pressure doesn't create resistance — the resistant variants were already present in the population — it amplifies whatever resistance exists until it dominates. Every antibiotic exposure, in every patient or animal, contributes to this selection.

Your understanding of the **basic reproduction number (R₀)** applies directly to resistance dynamics. A resistant strain can only spread and persist if its effective reproduction number exceeds 1 — that is, if each resistant bacterium infects more than one new host. In a hospital ward full of immunocompromised patients and broad-spectrum antibiotics, resistant strains face almost no competition from susceptible organisms (which the antibiotics kill) and encounter hosts who cannot clear infection effectively. The effective R of a resistant pathogen in that environment can be very high. In the community, resistance spreads more slowly, but **subtherapeutic dosing** — incomplete antibiotic courses, low-dose prophylaxis in agriculture — keeps susceptible bacteria under selection pressure without reliably killing resistant ones, enriching the resistant fraction in the population over time.

What makes antimicrobial resistance uniquely dangerous compared to other selective advantages is **horizontal gene transfer (HGT)**. Resistance genes are often carried on **plasmids** — mobile genetic elements that can be transferred between bacteria through conjugation, transformation, or transduction, even across species boundaries. A resistance gene that evolved in a soil bacterium can migrate to a clinical pathogen within years. **Carbapenemases** — enzymes that degrade last-resort carbapenems — have spread from environmental organisms to Enterobacteriaceae precisely through plasmid transfer. Unlike ordinary evolution, HGT means resistance can leap across the phylogenetic tree instantly, bypassing the need for de novo mutation in each lineage.

The public health implication is that individual clinical decisions aggregate into population-level outcomes. A physician who prescribes an antibiotic for a viral illness does not harm that individual patient's bacterial flora in a way that's clinically apparent, but contributes to the community-level reservoir of resistant organisms. This is why antimicrobial resistance cannot be solved by better individual prescribing alone — it requires **antimicrobial stewardship** programs that regulate antibiotic use at the institutional level, international surveillance to track resistance emergence and spread, and policy interventions to reduce agricultural overuse. The same epidemiological tools used to model infectious disease transmission apply here: reducing the effective R of resistant strains below 1 requires either reducing antibiotic selection pressure, breaking transmission routes between carriers, or both.

