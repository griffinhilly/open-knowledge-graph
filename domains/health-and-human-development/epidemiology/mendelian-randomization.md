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
stage: expert
status: draft
---

# Mendelian Randomization and Genetic Causal Inference

## Core Idea
Mendelian randomization uses genetic variants as instrumental variables to estimate causal effects of modifiable risk factors on outcomes. Because genetic variants are randomly assorted at birth and typically affect outcomes only through their association with the risk factor, Mendelian randomization circumvents confounding and reverse causality plaguing observational epidemiology.

## Questions

```yaml
- question: "A researcher proposes using a genetic variant in the serotonin transporter gene as an instrument to study whether depression causes cardiovascular disease. Later evidence shows the same variant also directly affects inflammatory pathways in the heart, independent of depression. Which instrumental variable assumption does this violate?"
  type: multiple-choice
  options:
    - "Relevance — the variant does not strongly predict depression"
    - "Independence — the variant associates with cardiovascular confounders"
    - "Exclusion restriction — the variant affects the outcome through a pathway other than the exposure"
    - "None — pleiotropic effects are permitted in Mendelian randomization"
  answer: 2
  explanation: "The exclusion restriction requires that the genetic instrument affects the outcome only through the exposure (depression), not through any independent pathway. A variant that directly influences cardiac inflammation violates this: it creates a back-door path from instrument to outcome that bypasses the exposure. This is the most common threat to MR validity — many genetic variants have pleiotropic effects, which is why sensitivity analyses like MR-Egger are used to test robustness."

- question: "Why does Mendel's law of independent assortment make genetic variants useful as instrumental variables in epidemiology?"
  type: multiple-choice
  options:
    - "Because genetic variants perfectly predict the exposure, eliminating measurement error"
    - "Because alleles are assigned randomly at conception, creating natural balance across confounders like socioeconomic status and lifestyle"
    - "Because genetic variants are fixed at birth and cannot be changed by behavior"
    - "Because GWAS studies can identify variants with very large effect sizes on exposures"
  answer: 1
  explanation: "The power of MR as a causal method comes from randomization: just as an RCT randomly assigns treatment, Mendel's second law randomly assigns alleles during gamete formation. This random assignment is independent of confounders like diet, income, or smoking — factors that plague observational epidemiology. That a variant predicts exposure is necessary (relevance), but it's the *random* nature of allele inheritance that satisfies the independence assumption and gives MR its causal inference logic."

- question: "The independence assumption in Mendelian randomization is analogous to randomization in a clinical trial, because alleles are randomly assigned at conception rather than based on an individual's lifestyle or social circumstances."
  type: true-false
  answer: true
  explanation: "This is exactly right and is the core analogy that makes MR compelling. In an RCT, randomization ensures that treatment and control groups are balanced on observed and unobserved confounders. Mendel's law plays a comparable role: which allele you inherit at a locus is determined at fertilization by processes independent of your later environment, diet, or behavior. This is why MR is called 'nature's randomized controlled trial.' The analogy is imperfect — population stratification can violate independence — but the logic is sound."

- question: "A genetic variant that strongly predicts heavy alcohol consumption is a valid Mendelian randomization instrument for studying alcohol's effect on liver disease, regardless of whether it also directly influences liver enzyme activity."
  type: true-false
  answer: false
  explanation: "This describes a violation of the exclusion restriction. If the variant directly affects liver enzyme activity independent of alcohol consumption, it creates a pathway from the genetic instrument to the outcome that does not pass through the exposure. The exclusion restriction requires the instrument to affect the outcome *only through* the exposure. Strong prediction of the exposure (relevance) is necessary but not sufficient — all three IV assumptions must hold for a valid MR analysis."

- question: "Explain why Mendelian randomization can estimate causal effects that observational epidemiology cannot, and identify the key assumption most likely to be violated."
  type: short-answer
  answer: "MR uses genetic variants as instruments to mimic randomization: because alleles are assigned randomly at conception and cannot be changed by behavior, the variant-exposure association is not confounded by lifestyle factors. By using only the variation in exposure predicted by the genotype, MR bypasses the confounding that makes observational associations unreliable. The assumption most likely to be violated is the exclusion restriction: genetic variants often have pleiotropic effects, influencing multiple biological pathways simultaneously. If the instrument affects the outcome through any pathway other than the target exposure, the causal estimate is biased."
  explanation: "Observational studies suffer because people who differ in exposure (e.g., alcohol consumption) also differ in many other ways (diet, stress, socioeconomic status) — these co-occurring factors confound the exposure-outcome association. MR exploits the biological lottery of inheritance: your genotype was assigned before you had a lifestyle. The exclusion restriction is the hardest assumption to verify because pleiotropy is biologically common, which is why modern two-sample MR includes sensitivity analyses (MR-Egger, weighted median) that can detect and partially correct for pleiotropic bias."
```

## Explainer

The central problem in observational epidemiology is confounding: people who drink heavily also tend to smoke, have poorer diets, and face more socioeconomic stress. When you observe that heavy drinkers have more cardiovascular disease, you cannot easily tell whether it is the alcohol causing harm or the constellation of other factors that co-occur with heavy drinking. Your study of instrumental variables introduced the solution in the abstract: find a variable that (1) reliably predicts the exposure, (2) is independent of confounders, and (3) affects the outcome only through the exposure. **Mendelian randomization** identifies these instruments in the genome.

The analogy to randomized controlled trials is the key insight. In an RCT, random assignment ensures that treatment and control groups are balanced on all confounders, observed and unobserved. Mendel's second law — the independent assortment of alleles during gamete formation — plays a similar role: which variant you inherit at a given locus is determined randomly at fertilization, not by your socioeconomic status, diet, or lifestyle. A genetic variant that causes you to metabolize alcohol faster (like the *ADH1B* Arg47His variant) will, on average, lead you to drink less because drinking becomes more unpleasant. That variant-exposure relationship is established by biology, not by choice. If people carrying the high-metabolism variant have lower rates of cardiovascular disease, that is hard to explain by confounding — their genotype differs, but otherwise they were randomly allocated to the "less alcohol" group at birth.

The three **instrumental variable assumptions** must hold for the inference to be valid. In the MR context: (1) **Relevance** — the genetic variant must genuinely associate with the exposure (testable using GWAS data); (2) **Independence** — the variant must not associate with confounders of the exposure-outcome relationship (the Mendelian randomization analogy to randomization; largely met but not guaranteed, especially with population stratification); (3) **Exclusion restriction** — the variant must affect the outcome only through its effect on the exposure, not through any independent pathway. This third assumption is where most MR analyses are vulnerable: many genetic variants have **pleiotropic** effects, influencing multiple biological pathways simultaneously. If the alcohol-metabolism variant also affects liver enzyme function independently of alcohol, the exclusion restriction is violated.

Modern **two-sample MR** extends the method by using summary statistics from two different GWAS studies — one for the variant-exposure association, one for the variant-outcome association — enabling very large effective sample sizes without needing individual-level data. Methods like MR-Egger, weighted median, and weighted mode allow sensitivity analyses that test whether results are robust to some degree of pleiotropy. When multiple independent genetic instruments for the same exposure all point to the same causal estimate, confidence in the result increases substantially. MR has provided credible causal evidence for LDL cholesterol in coronary disease, BMI in various outcomes, and vitamin D in multiple conditions — cases where decades of observational research were confounded by lifestyle factors that no statistical adjustment fully removes.
