---
id: pharmacogenomics
title: Pharmacogenomics
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: variant-calling-and-gwas
  type: hard
- id: population-genomics
  type: soft
- id: gene-expression-overview
  type: soft
builds-toward: []
tags:
- pharmacogenomics
- drug-response
- CYP450
- precision-medicine
- adverse-drug-reactions
- genotype-phenotype
stage: expert
status: validated
---
# Pharmacogenomics

## Core Idea
Pharmacogenomics studies how genetic variation affects drug response — efficacy, dosing, and adverse reactions. Variants in drug-metabolizing enzymes (CYP2D6, CYP2C19), drug transporters (ABCB1), and drug targets (VKORC1 for warfarin, HLA alleles for hypersensitivity) explain much of the inter-individual variability in drug response. Clinical pharmacogenomics translates these findings into genotype-guided prescribing: patients are genotyped for relevant variants, and drug choice or dose is adjusted accordingly. Guidelines from CPIC (Clinical Pharmacogenetics Implementation Consortium) provide evidence-based recommendations for over 100 drug-gene pairs.

## How It's Best Learned
Trace the warfarin dosing example end-to-end: examine how CYP2C9 and VKORC1 genotypes affect warfarin metabolism and sensitivity, calculate a genotype-adjusted dose using the IWPC algorithm, and compare to the standard one-size-fits-all dosing approach. Then examine the pharmacogenomic landscape of a commonly prescribed drug (e.g., clopidogrel/CYP2C19) and review the CPIC guideline.

## Common Misconceptions
- Pharmacogenomics does not mean every drug needs genetic testing — only drug-gene pairs with strong evidence and actionable clinical recommendations warrant routine genotyping.
- A "poor metabolizer" genotype does not always mean the drug will not work — for prodrugs (like clopidogrel, which requires CYP2C19 activation), poor metabolizers have reduced efficacy; for drugs metabolized to inactive forms, poor metabolizers may have increased drug exposure and toxicity.

## Questions

```yaml
- question: "A patient is genotyped as a CYP2D6 ultrarapid metabolizer. They are prescribed codeine, a prodrug that CYP2D6 converts to morphine. What is the clinical concern?"
  type: multiple-choice
  options: ["The patient will metabolize codeine too slowly, leading to no pain relief", "The patient will convert codeine to morphine much faster and in greater quantity than normal, risking morphine toxicity", "CYP2D6 does not affect codeine metabolism", "The patient will need a higher dose of codeine for adequate effect"]
  answer: 1
  explanation: "Codeine is a prodrug that requires CYP2D6-mediated conversion to its active metabolite morphine. Ultrarapid metabolizers have multiple copies of functional CYP2D6 genes, producing excess enzyme activity. They convert codeine to morphine much faster and more completely than normal metabolizers, potentially achieving toxic morphine levels from standard doses. This has caused fatalities, particularly in children. CPIC guidelines recommend avoiding codeine in CYP2D6 ultrarapid metabolizers and using an alternative analgesic."

- question: "Pharmacogenomic testing is only relevant for rare genetic disorders, not for commonly prescribed medications."
  type: true-false
  answer: false
  explanation: "Pharmacogenomic variants are common in the general population. Roughly 7% of Caucasians are CYP2D6 poor metabolizers, 2-15% of various populations are CYP2C19 poor metabolizers, and nearly all individuals carry at least one actionable pharmacogenomic variant. CPIC provides guidelines for widely prescribed drugs including clopidogrel (antiplatelet), warfarin (anticoagulant), SSRIs (antidepressants), codeine (analgesic), and 5-fluorouracil (chemotherapy). Pharmacogenomics affects everyday prescribing, not just rare diseases."

- question: "Explain why the same pharmacogenomic variant can have opposite clinical effects depending on whether the drug is an active compound or a prodrug."
  type: short-answer
  answer: "A drug-metabolizing enzyme variant (e.g., CYP2D6 poor metabolizer) reduces the enzyme's activity. For an active drug that the enzyme inactivates, reduced metabolism means higher and longer drug exposure, increasing the risk of side effects and toxicity — the patient effectively gets a higher dose than intended. For a prodrug that requires the enzyme to convert it to the active form, reduced metabolism means less active metabolite is produced, leading to therapeutic failure — the patient effectively gets a lower dose. The same genotype (poor metabolizer) causes toxicity in one case and inefficacy in the other, which is why the drug's metabolic pathway must be understood to interpret the genotype correctly."
  explanation: "This bidirectional effect is one of the most important concepts in pharmacogenomics. CYP2D6 poor metabolizers, for example, are at risk of toxicity from nortriptyline (active drug metabolized by CYP2D6) but at risk of therapeutic failure from codeine (prodrug activated by CYP2D6). The genotype is the same; the clinical recommendation depends on the drug."
```

## Explainer

The observation that patients respond differently to the same drug has been a persistent problem in medicine. Some patients achieve therapeutic benefit at standard doses while others experience severe adverse reactions or no benefit at all. Pharmacogenomics provides a molecular explanation: genetic variants in drug-metabolizing enzymes, transporters, targets, and immune molecules account for a large fraction of this variability. Understanding these variants enables precision prescribing — choosing the right drug at the right dose for each patient based on their genotype.

The most clinically important pharmacogenes are the **cytochrome P450 enzymes** — a family of liver enzymes that metabolize approximately 75% of all drugs. CYP2D6 alone metabolizes about 25% of drugs in clinical use, including codeine, tamoxifen, many antidepressants, and several antipsychotics. CYP2D6 is highly polymorphic, with alleles ranging from nonfunctional (no enzyme activity) to gene duplications (ultrarapid metabolism). The population distribution of these alleles varies by ancestry: CYP2D6 ultrarapid metabolizers are more common in East African and Middle Eastern populations (~10-30%) than in Europeans (~1-2%). CYP2C19 affects clopidogrel (an antiplatelet drug critical after cardiac stenting), where poor metabolizers have reduced drug activation and increased risk of stent thrombosis.

Beyond metabolism, genetic variation in **drug targets** directly affects efficacy. VKORC1 variants alter warfarin sensitivity by modifying the drug's target enzyme, with common variants explaining ~25% of dose variability. HLA alleles (particularly HLA-B*57:01 and HLA-B*15:02) mediate severe immune-mediated adverse drug reactions — abacavir hypersensitivity and carbamazepine-induced Stevens-Johnson syndrome, respectively. Pre-prescription HLA genotyping for these drugs has become standard of care in many settings, preventing potentially fatal adverse reactions.

The clinical implementation of pharmacogenomics is coordinated by **CPIC**, which publishes evidence-based guidelines translating genotype results into prescribing actions. For each drug-gene pair, CPIC defines metabolizer phenotype categories (poor, intermediate, normal, rapid, ultrarapid), assigns specific dosing or drug-choice recommendations for each category, and grades the evidence strength. Major health systems (St. Jude, Vanderbilt, Mayo Clinic) now implement preemptive pharmacogenomic testing — genotyping patients for panels of pharmacogenes before any specific drug is prescribed, storing the results in the medical record, and triggering clinical decision support alerts when a relevant drug is prescribed. This proactive approach avoids the delay of reactive testing and positions pharmacogenomics as a routine component of clinical care.
