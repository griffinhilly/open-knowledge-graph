---
id: non-homologous-end-joining-nhej
title: Non-Homologous End Joining (NHEJ) and DSB Repair
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-repair-mechanisms
  type: hard
builds-toward:
- crispr-gene-editing
tags:
- dna-repair
- non-homologous-end-joining
- nhej
- double-strand-break
stage: advanced
status: draft
---

# Non-Homologous End Joining (NHEJ) and DSB Repair

## Core Idea
NHEJ is a major pathway for double-strand break repair that directly ligates DNA ends without requiring homologous sequence. Ku70/Ku80 recognize and protect DNA ends; DNA-PK catalyzes processing; Ligase IV seals the nick. NHEJ is error-prone (may cause small insertions or deletions) but is rapid and active throughout the cell cycle.

## How It's Best Learned
Compare NHEJ and homologous recombination in terms of template requirement, accuracy, cell-cycle timing, and consequences of repair. Understand why NHEJ predominates at telomeres and in non-coding regions.

## Common Misconceptions
- Assuming NHEJ is the primary DSB repair pathway; HR may be preferred when homologs are available.
- Not recognizing that NHEJ can result in loss or gain of a few nucleotides at the break site.
- Thinking NHEJ is bad because it is error-prone; it provides a rapid repair option when accuracy is less critical than speed.

## Questions

```yaml
- question: "A cell sustains a double-strand break during G1 phase of the cell cycle. Which repair pathway predominantly handles this break, and why?"
  type: multiple-choice
  options:
    - "Homologous recombination, because it is more accurate and preferred whenever possible"
    - "NHEJ, because no sister chromatid template is available in G1, and NHEJ operates throughout the cell cycle"
    - "Base excision repair, because it is the primary pathway for all single- and double-strand damage"
    - "Mismatch repair, because G1 is the main window for post-replication proofreading"
  answer: 1
  explanation: "Homologous recombination requires a sister chromatid as a repair template and therefore operates primarily in S and G2 phases, after DNA replication when the sister is available. In G1, no sister chromatid exists, so NHEJ — which requires no template — is the dominant pathway. NHEJ is active throughout the entire cell cycle, making it the default repair mechanism for DSBs in most mammalian cells. Options C and D describe completely different repair pathways that do not address double-strand breaks."

- question: "When CRISPR-Cas9 is used to knock out a gene, the most common outcome is a frameshift mutation that disrupts the reading frame. What directly produces this frameshift?"
  type: multiple-choice
  options:
    - "Homologous recombination mistakenly repairs the Cas9-induced cut using a mismatched template"
    - "The Cas9 nuclease itself removes several base pairs from the coding sequence as it cuts"
    - "NHEJ repair of the double-strand break introduces small insertions or deletions (indels) at the cut site"
    - "The guide RNA integrates into the coding sequence at the cleavage site"
  answer: 2
  explanation: "When Cas9 introduces a DSB, the cell's NHEJ pathway repairs it rapidly. During repair, the end-processing step (trimming damaged bases or filling gaps) introduces small indels — typically 1–20 bp. If these indels occur in a coding exon, they shift the reading frame for all downstream codons, usually introducing premature stop codons and destroying protein function. This is the standard CRISPR knockout strategy. Option B is wrong: Cas9 makes a blunt cut at a specific site without removing bases; the indels arise from NHEJ processing."

- question: "NHEJ is essential for V(D)J recombination, the process by which the immune system generates the diversity of antibody and T-cell receptor sequences."
  type: true-false
  answer: true
  explanation: "V(D)J recombination deliberately introduces DSBs at recombination signal sequences to rearrange gene segments. After RAG recombinase cuts the DNA, NHEJ is required to rejoin the coding ends. Crucially, the imprecision of NHEJ — the insertion or deletion of a few nucleotides at the junctions — is not a bug but a feature: it generates additional sequence diversity at the junctions (junctional diversity), enormously expanding the repertoire of possible receptor sequences. Patients with NHEJ defects show severe combined immunodeficiency precisely because V(D)J recombination cannot complete."

- question: "NHEJ is a backup or last-resort DSB repair pathway, used only when homologous recombination is unavailable."
  type: true-false
  answer: false
  explanation: "NHEJ is the dominant DSB repair pathway in mammalian cells, not a backup. It operates throughout the cell cycle, including G1 when HR cannot function. It is also faster than HR — completing within minutes. The characterization as 'backup' likely arises from its error-prone nature compared to HR, but error-prone does not mean secondary. In many contexts — telomere maintenance, V(D)J recombination, CRISPR knockouts — NHEJ is the primary and essential pathway, not an alternative."

- question: "Why is NHEJ described as 'error-prone,' and under what circumstances does this imprecision become advantageous or even essential?"
  type: short-answer
  answer: "NHEJ is error-prone because the end-processing step, which trims or fills broken ends to make them ligatable, often removes or adds a few base pairs. These indels alter the local DNA sequence at the repair junction. This imprecision is a disadvantage when NHEJ repairs a coding sequence — the indel may frameshift the reading frame and destroy gene function. However, the same imprecision is advantageous or essential in two contexts: (1) V(D)J recombination, where NHEJ-introduced junctional diversity vastly expands immune receptor repertoire diversity, and (2) CRISPR gene knockouts, where researchers deliberately exploit NHEJ indels to disrupt genes they want to silence."
  explanation: "The broader principle is that 'error-prone' must be evaluated relative to context. NHEJ's imprecision is a serious liability at critical coding sequences but a productive feature wherever sequence diversity is the goal. Speed and cell-cycle independence are NHEJ's other key properties: it can act immediately after a break in any phase of the cell cycle, which is often more important for cell survival than whether the repair is perfectly accurate."
```

## Explainer

From your study of DNA repair mechanisms, you know that double-strand breaks (DSBs) are the most dangerous form of DNA damage — a single unrepaired DSB can trigger cell death or chromosomal rearrangements. Cells have two main strategies for fixing DSBs: homologous recombination (HR), which uses a sister chromatid as a template for accurate repair, and **non-homologous end joining (NHEJ)**, which directly glues the broken ends back together without any template. NHEJ trades accuracy for speed and availability — it works in any phase of the cell cycle, including G1 when no sister chromatid exists, making it the default DSB repair pathway in most mammalian cells.

The NHEJ pathway proceeds through a series of steps, each handled by a dedicated protein complex. First, the **Ku70/Ku80 heterodimer** — a ring-shaped protein — threads onto each broken DNA end and acts as a scaffold, protecting the ends from degradation by nucleases and recruiting downstream repair factors. Think of Ku as a molecular clamp that stabilizes the break site. Next, Ku recruits **DNA-PKcs** (DNA-dependent protein kinase catalytic subunit), which bridges the two ends and phosphorylates itself and other repair factors to activate processing. If the broken ends are not directly compatible (which they usually are not — DSBs often leave damaged or mismatched bases), processing enzymes like Artemis trim the ends to create ligatable termini.

The final step is ligation by the **XRCC4–Ligase IV complex**, which seals the nick and restores the phosphodiester backbone. The entire process can be completed within minutes — far faster than HR, which requires extensive strand invasion and DNA synthesis. However, the processing step is where errors creep in. Trimming damaged nucleotides from the break ends before ligation often removes a few base pairs, creating small **deletions**. Sometimes the polymerases μ and λ add a few nucleotides to fill gaps, creating small **insertions**. These insertions and deletions (collectively called **indels**) are the hallmark of NHEJ repair and the reason the pathway is described as error-prone.

Despite its imprecision, NHEJ is not a backup mechanism — it is essential. Cells that lack NHEJ components are hypersensitive to ionizing radiation (which causes DSBs) and show severe immunodeficiency because V(D)J recombination, the process that generates antibody diversity, relies on NHEJ to rejoin the programmed DSBs made during immune receptor gene rearrangement. NHEJ is also the pathway exploited by CRISPR-Cas9 gene editing: when Cas9 cuts a target site, NHEJ repair introduces indels that disrupt the reading frame, effectively knocking out the gene. Understanding NHEJ — its speed, its error profile, and its cell-cycle independence — is therefore crucial not only for understanding genome stability but also for designing and interpreting modern genome engineering experiments.
