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

## Questions

```yaml
- question: "Researchers perform a reciprocal transplant experiment with two plant populations: one from dry highlands, one from wet lowlands. Each population grows better in its home environment than in the foreign one, and the locally native population outperforms the transplanted foreign population at each site. What does this pattern demonstrate?"
  type: multiple-choice
  options:
    - "Phenotypic plasticity — both populations carry the same alleles but express different phenotypes in response to the local environment"
    - "Local adaptation driven by differential natural selection — the home-site advantage shows that fitness differences are genetic and environment-specific, not just environmental effects on a shared genotype"
    - "Founder effects — the populations differ genetically because they originated from different ancestral colonizations, not because of selection"
    - "Gene flow homogenizing the populations toward a generalist genotype suited for intermediate conditions"
  answer: 1
  explanation: "The reciprocal transplant is the classic experimental test for local adaptation. Phenotypic plasticity (option A) would show one population performing well in both environments — that is resilience, not local adaptation. The key evidence is that each population performs *better at home than the foreign population does at that same site* — the performance ranking reverses across environments. This reversal is the signature of G×E interaction and local adaptation, not merely environmental effects. Founder effects (option C) would produce genetic differences but not necessarily fitness differences that track environmental matching."

- question: "What does 'genotype-by-environment interaction' (G×E) mean in the context of local adaptation?"
  type: multiple-choice
  options:
    - "The environment determines which genotype an organism develops — organisms inherit different genes depending on where they live"
    - "The relative fitness ranking of genotypes can differ across environments — a genotype that outperforms others in one environment may be outcompeted by those same genotypes in a different environment"
    - "Genotypes are identical across environments but express different phenotypes, a phenomenon also known as phenotypic plasticity"
    - "Gene flow between environments increases when G×E interactions are strong"
  answer: 1
  explanation: "G×E is not about the environment changing the genotype, nor is it just that phenotypes vary across environments (that would be plasticity). G×E specifically means that the *ranking* of genotypes by fitness changes across environments. Allele A beats allele B in a dry climate, but allele B beats allele A in a wet climate. This crossover interaction is the raw material for local adaptation: it creates the condition where different alleles are actually optimal in different places, giving selection divergent targets in each environment."

- question: "Strong gene flow between two populations experiencing different selection pressures can prevent local adaptation by continuously reintroducing alleles that perform poorly in each local environment."
  type: true-false
  answer: true
  explanation: "This is the fundamental tension in local adaptation: selection pushes each population toward its local optimum by increasing the frequency of locally beneficial alleles. Gene flow counteracts this by importing alleles from other populations — alleles that may be well-adapted elsewhere but are maladaptive locally. When gene flow is strong relative to selection, allele frequencies are homogenized across populations and local adaptation remains weak or absent. Only when selection is sufficiently strong relative to gene flow can populations diverge toward their local optima. This balance is why highly dispersive species often show weaker local adaptation than sedentary ones."

- question: "If a declining population is locally adapted to its environment, introducing individuals from a distant, genetically distinct population will reliably improve its fitness by increasing genetic diversity."
  type: true-false
  answer: false
  explanation: "This describes outbreeding depression, which is the opposite of genetic rescue. Locally adapted populations carry specific allele combinations that work well in their environment (G×E). Introducing alleles from a population adapted to a different environment can disrupt these locally beneficial combinations, producing offspring with reduced fitness in the local conditions. The introduced alleles may perform well in their home environment but be maladaptive here. Conservation practice must weigh the potential benefits of genetic rescue (increased diversity, reduced inbreeding) against the risk of outbreeding depression from introducing maladapted alleles."

- question: "Why is the reciprocal transplant experiment considered strong evidence for local adaptation, and what pattern would you expect to observe if local adaptation were present?"
  type: short-answer
  answer: "In a reciprocal transplant, individuals from each population are moved into both their home environment and the foreign environment, with fitness measured in all four combinations. Local adaptation predicts a specific crossing pattern: (1) each population performs better at home than in the foreign site (home-site advantage), and (2) the locally native population outperforms the transplanted foreign population in each site. This crossing pattern — where performance rankings reverse across environments — cannot be explained by phenotypic plasticity (which would allow one population to do well everywhere) or by simple environmental effects (which would affect all individuals similarly). The reversal of performance rankings between environments is the signature of G×E interaction underlying local genetic adaptation."
  explanation: "The reciprocal design is essential. A simple 'common garden' experiment (all populations grown in one environment) only shows which genotype does best there; it cannot reveal local adaptation because it doesn't test how each population performs in its own environment. The reversal of ranking across environments — not just difference in absolute performance — is what makes the case for local adaptation."
```

## Explainer

From your study of natural selection and adaptation, you know that populations evolve traits that increase fitness in their environment. **Local adaptation** is what happens when different populations of the same species face different environments and evolve in different directions. A classic test for local adaptation is the **reciprocal transplant experiment**: you move individuals from population A into environment B and vice versa. If each population performs better in its home environment than the foreign one, local adaptation is confirmed. The pattern is intuitive — plants adapted to high-altitude conditions grow poorly at low altitude, and vice versa — but the underlying genetics are more subtle than they first appear.

The subtlety comes from **genotype-by-environment interaction** (G×E). You already know that a genotype produces a phenotype, and that the environment influences that phenotype. G×E means the *ranking* of genotypes can change across environments — genotype A might outperform genotype B in a dry climate but underperform it in a wet one. This is not just environmental noise; it is a fundamental feature of how genes work. The same allele can code for a protein that functions well at one temperature and poorly at another. G×E interactions are the raw material for local adaptation: they create the possibility that different alleles are favored in different places.

The tension at the heart of local adaptation is between **selection** and **gene flow**. Selection pushes each population toward its local optimum, favoring locally beneficial alleles. Gene flow — which you studied as the movement of alleles between populations — does the opposite, importing alleles that are well-suited elsewhere but potentially maladaptive locally. When gene flow is strong relative to selection, populations remain genetically similar and local adaptation is weak. When selection is strong relative to gene flow, populations diverge. This balance determines whether populations can specialize for their local conditions or are forced into a genetic compromise.

Local adaptation has practical consequences far beyond textbook examples. In conservation biology, transplanting individuals between populations can either rescue declining populations (genetic rescue) or introduce maladapted alleles that reduce fitness (outbreeding depression). In agriculture, crop varieties bred for one region may fail in another due to G×E interactions, which is why multi-environment trials are essential. And at the largest scale, strong local adaptation with restricted gene flow can set the stage for speciation — populations adapted to different environments may eventually become reproductively isolated, splitting into distinct species.
