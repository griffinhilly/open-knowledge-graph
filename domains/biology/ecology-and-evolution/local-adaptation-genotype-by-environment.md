---
id: local-adaptation-genotype-by-environment
title: Local Adaptation and Genotype-by-Environment Interaction
domain: biology
course: ecology-and-evolution
prerequisites:
- id: adaptation-and-fitness
  type: hard
- id: gene-flow-migration
  type: hard
- id: natural-selection
  type: hard
builds-toward:
- speciation
- evolutionary-constraints
tags:
- local-adaptation
- genotype-environment-interaction
- fitness-landscape
stage: formal-systems
status: draft
---

# Local Adaptation and Genotype-by-Environment Interaction

## Core Idea
Local adaptation occurs when populations evolve different alleles in response to local environmental conditions, creating a mismatch between genotypes and foreign environments. Genotype-by-environment (G×E) interactions mean the same allele has different effects in different environments. Gene flow opposes local adaptation by homogenizing populations, while selection maintains divergence.

## Explainer

From your study of natural selection and adaptation, you know that populations evolve traits that increase fitness in their environment. **Local adaptation** is what happens when different populations of the same species face different environments and evolve in different directions. A classic test for local adaptation is the **reciprocal transplant experiment**: you move individuals from population A into environment B and vice versa. If each population performs better in its home environment than the foreign one, local adaptation is confirmed. The pattern is intuitive — plants adapted to high-altitude conditions grow poorly at low altitude, and vice versa — but the underlying genetics are more subtle than they first appear.

The subtlety comes from **genotype-by-environment interaction** (G×E). You already know that a genotype produces a phenotype, and that the environment influences that phenotype. G×E means the *ranking* of genotypes can change across environments — genotype A might outperform genotype B in a dry climate but underperform it in a wet one. This is not just environmental noise; it is a fundamental feature of how genes work. The same allele can code for a protein that functions well at one temperature and poorly at another. G×E interactions are the raw material for local adaptation: they create the possibility that different alleles are favored in different places.

The tension at the heart of local adaptation is between **selection** and **gene flow**. Selection pushes each population toward its local optimum, favoring locally beneficial alleles. Gene flow — which you studied as the movement of alleles between populations — does the opposite, importing alleles that are well-suited elsewhere but potentially maladaptive locally. When gene flow is strong relative to selection, populations remain genetically similar and local adaptation is weak. When selection is strong relative to gene flow, populations diverge. This balance determines whether populations can specialize for their local conditions or are forced into a genetic compromise.

Local adaptation has practical consequences far beyond textbook examples. In conservation biology, transplanting individuals between populations can either rescue declining populations (genetic rescue) or introduce maladapted alleles that reduce fitness (outbreeding depression). In agriculture, crop varieties bred for one region may fail in another due to G×E interactions, which is why multi-environment trials are essential. And at the largest scale, strong local adaptation with restricted gene flow can set the stage for speciation — populations adapted to different environments may eventually become reproductively isolated, splitting into distinct species.
