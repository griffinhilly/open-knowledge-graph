---
id: mismatch-repair-mlh-msh
title: Mismatch Repair and MLH/MSH Proteins
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-repair-mechanisms
  type: hard
- id: dna-replication-primers-helicase-synthesis
  type: soft
builds-toward:
- homologous-recombination-rad51-complex
tags:
- dna-repair
- mismatch-repair
- mlh
- msh
- replication
stage: advanced
status: draft
---

# Mismatch Repair and MLH/MSH Proteins

## Core Idea
Mismatch repair (MMR) corrects base mismatches that escape polymerase proofreading and mismatch due to slippage in repetitive sequences. MSH2/MSH6 (eukaryotes) or MutS (prokaryotes) recognize mismatches; MLH1/PMS2 (eukaryotes) or MutL (prokaryotes) coordinate the removal of the mismatch-containing strand. Defects in MMR cause Lynch syndrome and microsatellite instability in cancers.

## How It's Best Learned
Study the prokaryotic paradigm (MutS/MutL/MutH) where hemimethylated DNA distinguishes the newly synthesized strand. Understand how eukaryotes lack MutH and instead use a different discrimination system (PCNA orientation or strand discontinuities).

## Common Misconceptions
- Assuming MMR works equally well on both strands; it preferentially corrects the new strand in prokaryotes.
- Not recognizing that slippage in microsatellites and homopolymeric runs is a major source of mismatches.
- Thinking MMR deficiency causes mutations only during replication; it also affects meiotic recombination and homologous recombination.

## Questions

```yaml
- question: "Why is strand discrimination the most critical step in mismatch repair — the step without which the entire pathway could cause net harm?"
  type: multiple-choice
  options:
    - "Because mismatches only occur on the newly synthesized strand, so only one strand needs to be scanned"
    - "Because without knowing which strand contains the error, the repair system might correct the template strand, converting the replication mistake into a permanent mutation"
    - "Because strand discrimination determines which exonuclease is recruited to remove the mismatch"
    - "Because discrimination prevents the repair machinery from processing legitimate base modifications as mismatches"
  answer: 1
  explanation: "A mismatch is structurally ambiguous — both strands look normal except for the non-Watson-Crick pairing. The system cannot tell from the mismatch alone which base is wrong. If it corrects the template strand (the correct one), it converts the correct sequence to the error — a permanent mutation worse than the original replication mistake. Strand discrimination (hemimethylation in bacteria, strand discontinuities in eukaryotes) is what allows consistent targeting of the newly synthesized strand, achieving the 100- to 1000-fold fidelity improvement."

- question: "A patient with Lynch syndrome has a germline mutation inactivating one copy of MLH1. Decades later they develop colorectal cancer with microsatellite instability (MSI). What sequence of molecular events best explains this?"
  type: multiple-choice
  options:
    - "The single inherited MLH1 mutation directly activates oncogenes, initiating cancer immediately"
    - "Loss of the second MLH1 allele somatically (two-hit model) eliminates MMR, creating a mutator phenotype that accelerates mutation accumulation in tumor suppressors and oncogenes"
    - "MSI caused by the inherited mutation directly kills normal cells, allowing cancer cells to proliferate unopposed"
    - "Microsatellite instability in Lynch syndrome is present in all cells from birth and gradually causes cancer"
  answer: 1
  explanation: "Lynch syndrome follows the two-hit model: the inherited MLH1 mutation is heterozygous — the second allele still provides sufficient MMR function. When the second allele is somatically inactivated (the 'second hit'), MMR is completely eliminated in that cell lineage. Polymerase slippage at microsatellites goes uncorrected (producing MSI), and the mutator phenotype dramatically accelerates accumulation of mutations throughout the genome, including in tumor suppressor genes, driving cancer development."

- question: "A mismatch repair system that cannot distinguish the new strand from the template strand would be approximately as likely to cause permanent mutations as to prevent them."
  type: true-false
  answer: true
  explanation: "If the system randomly selects which strand to correct, it will fix the template strand in ~50% of cases — replacing the correct base with the error, permanently embedding the replication mistake as a heritable mutation. Proper strand discrimination ensures the system corrects the new strand in every case, achieving its full fidelity improvement. Without discrimination, the repair system would be no more useful than random mutagenesis, undermining its entire biological purpose."

- question: "Eukaryotic mismatch repair uses the same GATC hemimethylation mechanism as bacteria to identify the newly synthesized strand."
  type: true-false
  answer: false
  explanation: "This is a critical mechanistic difference. Bacteria use GATC methylation: the parental strand is methylated at GATC sites; the newly synthesized strand is transiently unmethylated, allowing MutH to nick the new strand specifically. Eukaryotes lack MutH and do not use methylation for strand discrimination. Instead, they exploit structural features of ongoing replication — nicks at Okazaki fragment junctions on the lagging strand, the 3' terminus on the leading strand, and the orientation of the PCNA sliding clamp — to identify the new strand."

- question: "Why are microsatellite sequences (short tandem repeats like CACACACA) particularly vulnerable when mismatch repair is defective, and why is microsatellite instability (MSI) used as a diagnostic marker for MMR dysfunction?"
  type: short-answer
  answer: "DNA polymerase slips frequently on repetitive sequences — the template or new strand can loop out during synthesis, creating insertion/deletion loops of one or more repeat units. MMR normally corrects these loops before they are permanently incorporated. Without MMR, each slippage event changes the repeat count in that cell, producing measurable length variation at microsatellite loci across the genome. Since slippage at microsatellites is frequent and the length changes accumulate in every cell division, MMR-deficient tumors show MSI at multiple loci simultaneously. Comparing tumor DNA to matched normal DNA from the same patient detects this variation, making MSI a sensitive and specific diagnostic marker for MMR dysfunction."
  explanation: "MSI testing is used both to screen for Lynch syndrome (where inherited MMR gene mutations predispose to colorectal and other cancers) and to identify sporadic MMR-deficient cancers. The latter are clinically important because MMR-deficient tumors accumulate many mutations throughout the genome, generating neoantigens that make them highly responsive to immune checkpoint blockade therapy — a major advance in cancer treatment that depends on this molecular distinction."
```

## Explainer

DNA polymerase is remarkably accurate, but it still makes roughly one error per 10⁷ nucleotides even with its built-in 3'→5' proofreading exonuclease. For a human genome of 6 billion base pairs, that means hundreds of mismatches per cell division would persist without a backup system. **Mismatch repair (MMR)** is that backup — a post-replicative surveillance pathway that scans newly synthesized DNA, finds mismatches the polymerase missed, and fixes them, improving overall replication fidelity by 100- to 1000-fold.

The system works in three steps: **recognition**, **strand discrimination**, and **excision/resynthesis**. In bacteria, the best-understood system uses **MutS** to patrol the DNA, recognizing mismatches and small insertion/deletion loops by detecting the distortion they create in the double helix. MutS then recruits **MutL**, which acts as a coordinator, and together they activate **MutH**. MutH's job is critical: it nicks the unmethylated strand at nearby GATC sequences. Since the parental (template) strand is methylated and the newly synthesized strand is transiently unmethylated, this asymmetry tells the system *which strand has the error*. An exonuclease then degrades the nicked strand past the mismatch, and DNA polymerase III resynthesizes the gap using the correct parental strand as template.

Eukaryotes use homologous proteins — **MSH2/MSH6** (called MutSα, recognizes single-base mismatches) and **MSH2/MSH3** (MutSβ, recognizes larger insertion/deletion loops) for recognition, and **MLH1/PMS2** (MutLα) for coordination. The critical difference is that eukaryotes lack MutH and don't use methylation for strand discrimination. Instead, they exploit the discontinuous nature of the newly synthesized strand — the nicks at Okazaki fragment junctions on the lagging strand, and the 3' terminus on the leading strand, along with the PCNA sliding clamp's orientation, signal which strand is new. This is why understanding replication machinery from your prerequisites matters: the repair system literally uses the structural features of ongoing replication to identify its target.

When MMR fails, the consequences are severe. **Microsatellites** — short tandem repeats like (CA)₁₅ — are especially vulnerable because DNA polymerase frequently slips on these sequences, producing insertion/deletion loops that only MMR can correct. Cells with defective MMR accumulate changes in microsatellite length, a phenotype called **microsatellite instability (MSI)**. In humans, inherited mutations in *MLH1* or *MSH2* cause **Lynch syndrome** (hereditary nonpolyposis colorectal cancer), which accounts for about 3% of all colorectal cancers. The two-hit model applies: one defective allele is inherited, and somatic loss of the remaining functional copy unleashes a mutator phenotype that accelerates the accumulation of mutations in tumor suppressor genes and oncogenes.
