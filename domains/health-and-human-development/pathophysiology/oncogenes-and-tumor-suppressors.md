---
id: oncogenes-and-tumor-suppressors
title: Oncogenes and Tumor Suppressor Genes
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: gene-regulation-eukaryotes
  type: soft
builds-toward:
- familial-cancer-syndromes
tags:
- oncogenes
- tumor-suppressors
- genetic-instability
stage: expert
status: draft
---

# Oncogenes and Tumor Suppressor Genes

## Core Idea
Oncogenes are mutated growth-promoting genes causing excessive proliferation; activation requires only one copy (dominant). Tumor suppressors restrain growth; loss requires inactivation of both copies (recessive). Classic suppressors (TP53, RB, APC) are lost early in carcinogenesis.

## How It's Best Learned
Compare gain-of-function (oncogenes) and loss-of-function (suppressors) mutations using examples. Understand Knudson's two-hit hypothesis for tumor suppressors. Study therapeutic implications: oncogenes are actionable targets (EGFR, BCR-ABL).

## Common Misconceptions
Not all mutations in oncogenes are cancer-causing—some are passenger mutations with no functional consequence. Heterozygous loss of a tumor suppressor does not cause disease; both alleles must be disrupted.

## Questions

```yaml
- question: "A patient inherits one mutant copy of RB1 in every cell of their body (familial retinoblastoma). Why do tumors develop earlier and more frequently than in patients who have two normal RB1 copies at birth?"
  type: multiple-choice
  options:
    - "The inherited mutant copy acts as a dominant oncogene, immediately driving proliferation in retinal cells"
    - "Having one mutant copy in every cell means only a single additional somatic mutation is needed to eliminate RB1 function, rather than two independent somatic events"
    - "The inherited mutant copy prevents DNA repair, accelerating all mutations throughout the genome"
    - "Heterozygous loss of RB1 already reduces the brake on proliferation enough to cause tumors"
  answer: 1
  explanation: "This is the core of Knudson's two-hit hypothesis. Tumor suppressors require inactivation of BOTH copies before their protective function is lost (loss-of-function is recessive). In sporadic retinoblastoma, two independent somatic mutations must hit the same cell — a statistically rare double event. Inherited cases start with one hit already in every retinal cell at birth; only one additional somatic event is needed, making tumor formation far more likely and occurring earlier. Option D is wrong: heterozygous loss is typically insufficient because the remaining normal copy maintains function."

- question: "An oncologist discovers that a cancer carries a point mutation in KRAS that locks its protein product in the GTP-bound (active) state. How many mutant copies of KRAS are needed to drive tumor growth?"
  type: multiple-choice
  options:
    - "Both copies must be mutated, since one normal copy would suppress the mutant signal"
    - "Only one mutant copy is sufficient, because the constitutively active protein overrides the normal regulatory system"
    - "Four copies are required because KRAS has multiple isoforms"
    - "Neither copy matters; KRAS mutations are always passenger mutations with no functional effect"
  answer: 1
  explanation: "Oncogenic mutations are dominant gain-of-function: one mutant copy is sufficient to drive excessive signaling because the activated protein (stuck in the 'on' state) floods the cell with growth signals regardless of what the second copy does. This is the gas pedal analogy — one stuck accelerator pushes the car forward even if the other pedal works normally. This distinguishes oncogenes fundamentally from tumor suppressors: oncogenes need ONE hit; tumor suppressors need TWO."

- question: "Oncogene mutations are dominant because a single mutant copy can drive excessive proliferation even when the other copy of the gene is normal and functional."
  type: true-false
  answer: true
  explanation: "This is the defining feature of oncogenes. The mutant protein product produces a gain of function — constitutive growth signaling, locked receptor activation, or unregulated transcription factor activity — that operates independently of the normal copy. One stuck accelerator is enough to keep the car moving. This contrasts sharply with tumor suppressors, where the remaining normal copy maintains function until it too is inactivated."

- question: "A person who inherits one mutant copy of TP53 (as in Li-Fraumeni syndrome) has already lost p53 function in all their cells, so cancer development is inevitable from birth."
  type: true-false
  answer: false
  explanation: "This is the key misconception about the two-hit model. Tumor suppressors require BOTH copies to be inactivated before protective function is lost — one normal allele is sufficient to maintain function. Li-Fraumeni syndrome patients have one normal TP53 copy in every cell, which continues to function. Cancer requires a second somatic mutation (the 'second hit') that eliminates that remaining copy in a particular cell. This is why Li-Fraumeni carriers face dramatically elevated cancer risk but do not develop cancer at birth — they are one somatic event away per cell, not zero."

- question: "Why must both copies of a tumor suppressor gene be inactivated for cancer to result, while activation of only one copy of an oncogene is sufficient to drive tumor growth?"
  type: short-answer
  answer: "Tumor suppressors have a loss-of-function mechanism: their normal role is to restrain proliferation, and one working copy is enough to maintain that brake. Only when both copies are inactivated is the restraint completely removed. Oncogenes have a gain-of-function mechanism: the mutant protein actively drives proliferation regardless of what the other copy does — one constitutively active accelerator overrides the system."
  explanation: "This mechanistic asymmetry explains why the two gene classes behave so differently in hereditary cancer syndromes. Tumor suppressor syndromes (BRCA1/2, RB1, APC, TP53) follow the two-hit pattern: one inherited hit plus one somatic hit. Oncogene-driven hereditary syndromes are rarer because a single germline oncogenic mutation would drive proliferation throughout development. The dominant/recessive distinction here is about the protein-level mechanism, not allele-level genetics in the traditional sense."
```

## Explainer

Normal cell division is controlled by a balance between growth-promoting signals and growth-restraining checkpoints. You know from gene regulation that transcription factors, signal transduction proteins, and cell cycle regulators are encoded by genes that can be altered by mutation. Cancer results not from a single mutation but from the accumulation of mutations that tip this balance—turning up accelerators and disabling brakes simultaneously. **Oncogenes** are the accelerators; **tumor suppressor genes** are the brakes. Understanding both classes, and how they differ mechanistically, is the foundation for thinking about cancer genetics.

An **oncogene** is a mutated or overexpressed version of a normal growth-promoting gene (the normal version is called a **proto-oncogene**). Proto-oncogenes encode growth factors, growth factor receptors, signal transduction proteins (like RAS), and transcription factors that promote entry into the cell cycle. A mutation that locks one of these proteins in the "on" state creates an oncogene: the cell receives a permanent growth signal without needing external stimulation. Because one mutant copy is sufficient to override the normal copy, oncogene mutations are **dominant**—like a stuck gas pedal that pushes through even when the other pedal is working normally. Classic examples include *KRAS* mutations (found in roughly 25% of all human cancers), *HER2* amplification (breast cancer), and the *BCR-ABL* translocation in chronic myeloid leukemia that creates a constitutively active kinase.

**Tumor suppressor genes** work differently: their normal function is to restrain proliferation—halting the cell cycle at checkpoints, repairing DNA damage, or triggering apoptosis when damage is irreparable. Losing a tumor suppressor removes a brake. But because each cell carries two gene copies, both must be inactivated before protective function is lost. This is **Knudson's two-hit hypothesis**: one inherited or somatic mutation (first hit) plus a second somatic mutation or loss of heterozygosity (second hit) completes the inactivation. The germline-inheritance implication is powerful: individuals born with one mutant copy in every cell—as in Li-Fraumeni syndrome (*TP53*) or familial adenomatous polyposis (*APC*)—need only one additional somatic event per cell to lose function, dramatically accelerating cancer onset. Key tumor suppressors include *TP53* (mutated in over 50% of cancers, coordinates the DNA damage response), *RB1* (a core cell cycle brake at the G1/S checkpoint), and *APC* (restrains proliferative Wnt signaling in intestinal epithelium).

Together, these two gene classes underpin the **multi-step model of carcinogenesis**: cancer cells typically accumulate both oncogenic activation and tumor suppressor loss over years or decades, explaining why cancer incidence rises steeply with age. The framework also explains why targeted therapies can work: drugs like imatinib (targeting BCR-ABL in CML) exploit a cancer cell's dependence on a specific activated oncogene, selectively killing cells that rely on that signal while sparing normal cells whose growth is governed by intact regulatory systems.
