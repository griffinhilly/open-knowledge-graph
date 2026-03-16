---
id: mendelian-randomization
title: Mendelian Randomization and Genetic Causal Inference
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: genetic-epidemiology-concepts
  type: hard
- id: instrumental-variables-epidemiology
  type: hard
tags:
- causal-inference
- genetic-instruments
- gwas
stage: advanced
status: draft
---

# Mendelian Randomization and Genetic Causal Inference

## Core Idea
Mendelian randomization uses genetic variants as instrumental variables to estimate causal effects of modifiable risk factors on outcomes. Because genetic variants are randomly assorted at birth and typically affect outcomes only through their association with the risk factor, Mendelian randomization circumvents confounding and reverse causality plaguing observational epidemiology.

## Explainer

The central problem in observational epidemiology is confounding: people who drink heavily also tend to smoke, have poorer diets, and face more socioeconomic stress. When you observe that heavy drinkers have more cardiovascular disease, you cannot easily tell whether it is the alcohol causing harm or the constellation of other factors that co-occur with heavy drinking. Your study of instrumental variables introduced the solution in the abstract: find a variable that (1) reliably predicts the exposure, (2) is independent of confounders, and (3) affects the outcome only through the exposure. **Mendelian randomization** identifies these instruments in the genome.

The analogy to randomized controlled trials is the key insight. In an RCT, random assignment ensures that treatment and control groups are balanced on all confounders, observed and unobserved. Mendel's second law — the independent assortment of alleles during gamete formation — plays a similar role: which variant you inherit at a given locus is determined randomly at fertilization, not by your socioeconomic status, diet, or lifestyle. A genetic variant that causes you to metabolize alcohol faster (like the *ADH1B* Arg47His variant) will, on average, lead you to drink less because drinking becomes more unpleasant. That variant-exposure relationship is established by biology, not by choice. If people carrying the high-metabolism variant have lower rates of cardiovascular disease, that is hard to explain by confounding — their genotype differs, but otherwise they were randomly allocated to the "less alcohol" group at birth.

The three **instrumental variable assumptions** must hold for the inference to be valid. In the MR context: (1) **Relevance** — the genetic variant must genuinely associate with the exposure (testable using GWAS data); (2) **Independence** — the variant must not associate with confounders of the exposure-outcome relationship (the Mendelian randomization analogy to randomization; largely met but not guaranteed, especially with population stratification); (3) **Exclusion restriction** — the variant must affect the outcome only through its effect on the exposure, not through any independent pathway. This third assumption is where most MR analyses are vulnerable: many genetic variants have **pleiotropic** effects, influencing multiple biological pathways simultaneously. If the alcohol-metabolism variant also affects liver enzyme function independently of alcohol, the exclusion restriction is violated.

Modern **two-sample MR** extends the method by using summary statistics from two different GWAS studies — one for the variant-exposure association, one for the variant-outcome association — enabling very large effective sample sizes without needing individual-level data. Methods like MR-Egger, weighted median, and weighted mode allow sensitivity analyses that test whether results are robust to some degree of pleiotropy. When multiple independent genetic instruments for the same exposure all point to the same causal estimate, confidence in the result increases substantially. MR has provided credible causal evidence for LDL cholesterol in coronary disease, BMI in various outcomes, and vitamin D in multiple conditions — cases where decades of observational research were confounded by lifestyle factors that no statistical adjustment fully removes.
