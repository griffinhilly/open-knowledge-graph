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

## Explainer

DNA polymerase is remarkably accurate, but it still makes roughly one error per 10⁷ nucleotides even with its built-in 3'→5' proofreading exonuclease. For a human genome of 6 billion base pairs, that means hundreds of mismatches per cell division would persist without a backup system. **Mismatch repair (MMR)** is that backup — a post-replicative surveillance pathway that scans newly synthesized DNA, finds mismatches the polymerase missed, and fixes them, improving overall replication fidelity by 100- to 1000-fold.

The system works in three steps: **recognition**, **strand discrimination**, and **excision/resynthesis**. In bacteria, the best-understood system uses **MutS** to patrol the DNA, recognizing mismatches and small insertion/deletion loops by detecting the distortion they create in the double helix. MutS then recruits **MutL**, which acts as a coordinator, and together they activate **MutH**. MutH's job is critical: it nicks the unmethylated strand at nearby GATC sequences. Since the parental (template) strand is methylated and the newly synthesized strand is transiently unmethylated, this asymmetry tells the system *which strand has the error*. An exonuclease then degrades the nicked strand past the mismatch, and DNA polymerase III resynthesizes the gap using the correct parental strand as template.

Eukaryotes use homologous proteins — **MSH2/MSH6** (called MutSα, recognizes single-base mismatches) and **MSH2/MSH3** (MutSβ, recognizes larger insertion/deletion loops) for recognition, and **MLH1/PMS2** (MutLα) for coordination. The critical difference is that eukaryotes lack MutH and don't use methylation for strand discrimination. Instead, they exploit the discontinuous nature of the newly synthesized strand — the nicks at Okazaki fragment junctions on the lagging strand, and the 3' terminus on the leading strand, along with the PCNA sliding clamp's orientation, signal which strand is new. This is why understanding replication machinery from your prerequisites matters: the repair system literally uses the structural features of ongoing replication to identify its target.

When MMR fails, the consequences are severe. **Microsatellites** — short tandem repeats like (CA)₁₅ — are especially vulnerable because DNA polymerase frequently slips on these sequences, producing insertion/deletion loops that only MMR can correct. Cells with defective MMR accumulate changes in microsatellite length, a phenotype called **microsatellite instability (MSI)**. In humans, inherited mutations in *MLH1* or *MSH2* cause **Lynch syndrome** (hereditary nonpolyposis colorectal cancer), which accounts for about 3% of all colorectal cancers. The two-hit model applies: one defective allele is inherited, and somatic loss of the remaining functional copy unleashes a mutator phenotype that accelerates the accumulation of mutations in tumor suppressor genes and oncogenes.
