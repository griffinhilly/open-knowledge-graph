---
id: homologous-recombination-rad51-complex
title: Homologous Recombination and the RAD51 Complex
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: meiotic-recombination-crossing-over
  type: soft
- id: dna-repair-mechanisms
  type: soft
builds-toward:
- non-homologous-end-joining-nhej
- genetic-mapping-recombination-frequency
tags:
- homologous-recombination
- rad51
- double-strand-break-repair
- dna-repair
stage: formal-systems
status: validated
---

# Homologous Recombination and the RAD51 Complex

## Core Idea
Homologous recombination repairs double-strand breaks and facilitates meiotic recombination. RAD51 protein replaces RPA on single-stranded DNA, forming a nucleoprotein filament. The filament invades homologous duplex DNA, forming a D-loop. DNA polymerase extends the invading 3' end, and resolution of the double Holiday junction completes recombination.

## How It's Best Learned
Follow the biochemical steps of homologous recombination: end resection by MRN/EXO1, RPA coating, RAD51 loading and filament formation, strand invasion, DNA synthesis, and resolution. Use electron microscopy or cryo-EM images to visualize D-loops and Holiday junctions.

## Common Misconceptions
- Assuming recombination always uses homologous template when some is ectopic or between non-allelic sequences.
- Not recognizing that the same machinery (RAD51, MRN) functions in both mitotic DSB repair and meiotic recombination.
- Thinking recombination is purely generative (creating new combinations) when it also serves a repair function.

## Questions

```yaml
- question: "A mutation prevents RAD51 from displacing RPA on the resected single-stranded DNA tails at a double-strand break. Which consequence would you most directly predict?"
  type: multiple-choice
  options:
    - "DSB repair proceeds normally, but meiotic crossover frequency is reduced because RAD51 is only required for meiosis"
    - "Homologous recombination fails because strand invasion cannot occur without a functional RAD51 nucleoprotein filament"
    - "DSB repair is slowed but not abolished, because RPA can directly mediate strand invasion at lower efficiency"
    - "Recombination frequency increases, because RPA normally suppresses RAD51-independent recombination pathways"
  answer: 1
  explanation: "RAD51 filament formation on the ssDNA tail is the essential step that enables strand invasion. Without RAD51 displacing RPA, the ssDNA remains bound by a protein that protects it but cannot catalyze homology search. The RAD51 filament actively scans the genome for a homologous duplex and catalyzes the D-loop formation that initiates repair. No RAD51 filament = no strand invasion = no HR. This is why BRCA2 mutations (which disrupt RAD51 loading) are so clinically significant."

- question: "Why is homologous recombination considered a high-fidelity repair pathway compared to non-homologous end joining (NHEJ)?"
  type: multiple-choice
  options:
    - "HR uses multiple redundant repair proteins that cross-check each other, reducing the probability that any single error is incorporated"
    - "HR uses a homologous DNA template to copy the original sequence across the break, restoring information rather than simply re-ligating broken ends"
    - "HR is restricted to the nucleus, where the higher chromatin density protects the repair intermediates from further damage"
    - "HR's nuclease activities degrade damaged DNA around the break before synthesizing a completely new replacement strand"
  answer: 1
  explanation: "The high fidelity of HR comes directly from template use. During strand invasion, the RAD51 filament invades a homologous duplex — typically the sister chromatid — and DNA polymerase copies the intact sequence across the break. This is information recovery, not just break sealing. NHEJ, by contrast, ligates the broken ends with minimal processing; if nucleotides were lost or modified during the break, NHEJ incorporates those errors. The template-dependent nature of HR is the mechanistic reason it is used preferentially in S and G2 phases, when the replicated sister chromatid is available as a template."

- question: "The RAD51 protein is the eukaryotic functional equivalent of bacterial RecA — it forms a nucleoprotein filament on single-stranded DNA and catalyzes the strand invasion step of homologous recombination."
  type: true-false
  answer: true
  explanation: "RAD51 and RecA are structural and functional homologs. Both form a right-handed helical filament around ssDNA, both use ATP hydrolysis to power conformational changes that facilitate homology search, and both catalyze the same fundamental step: strand invasion of a homologous duplex to form a displacement loop. RAD51 is part of a broader RecA/RAD51 superfamily that also includes DMC1, the meiosis-specific recombinase that performs analogous functions during meiotic recombination using the homologous chromosome rather than the sister chromatid."

- question: "Meiotic recombination and mitotic double-strand break repair use largely different molecular machinery, which is why mutations in repair genes like BRCA2 primarily affect cancer risk but do not impair meiosis."
  type: true-false
  answer: false
  explanation: "Both meiotic recombination and mitotic DSB repair use the same core RAD51 machinery (RAD51, MRN complex, BRCA2 as a mediator). The difference is not in the core proteins but in which sub-pathway is favored: meiotic cells use the double Holliday junction pathway to generate crossovers, while mitotic cells favor SDSA to produce non-crossovers and avoid loss of heterozygosity. BRCA2 mutations impair both — individuals with BRCA2 mutations have both elevated cancer risk (defective mitotic DSB repair) and can show reduced fertility (defective meiotic recombination)."

- question: "Explain why mitotic cells favor the synthesis-dependent strand annealing (SDSA) sub-pathway over the classical double Holliday junction pathway, and what would go wrong if they used the dHJ pathway instead."
  type: short-answer
  answer: "SDSA always produces non-crossovers: the newly synthesized strand is displaced from the template and anneals back to the other broken end, restoring the original sequence without exchanging flanking sequences. The dHJ pathway produces crossovers approximately half the time. In mitotic cells, crossovers between homologous chromosomes (rather than sister chromatids) would cause loss of heterozygosity — if one chromosome carries a tumor-suppressor mutation, a crossover could produce a daughter cell homozygous for that mutation, contributing to cancer. SDSA avoids this risk by ensuring repair is completed without exchange."
  explanation: "The cell-cycle regulation of sub-pathway choice reflects the different consequences of crossovers in meiosis versus mitosis. In meiosis, crossovers are essential for proper homolog segregation and genetic diversity, so the dHJ pathway is actively promoted (by proteins like MutLγ that stabilize dHJs). In mitotic cells, crossovers create genetic instability risk, so SDSA is favored. This is why the same core HR machinery produces different outcomes in the two cell types — the difference is in the regulatory proteins that channel the reaction, not the core recombinase itself."
```

## Explainer

From your study of meiotic recombination, you know that crossing over shuffles alleles between homologous chromosomes, generating genetic diversity. From DNA repair mechanisms, you know that double-strand breaks (DSBs) are among the most dangerous forms of DNA damage — a single unrepaired DSB can kill a cell. **Homologous recombination** (HR) is the molecular process that serves both purposes: it is the engine behind meiotic crossovers *and* the primary high-fidelity repair pathway for DSBs in somatic cells. The **RAD51 protein** is the central player in this process.

The pathway begins when a DSB is detected and processed. The MRN complex (Mre11-Rad50-Nbs1) recognizes the broken ends and, together with nucleases like EXO1, resects the 5' ends to generate long 3' single-stranded DNA (ssDNA) tails. These ssDNA tails are immediately coated by **RPA** (Replication Protein A), which prevents them from forming secondary structures and protects them from degradation. But RPA must be displaced before recombination can proceed — this is where RAD51 enters.

With the help of mediator proteins (BRCA2 in humans, Rad52 in yeast), **RAD51 replaces RPA** on the ssDNA, forming a helical nucleoprotein filament — a structure that looks like a stretched-out spring of protein wrapped around DNA. This RAD51 filament is the active search-and-invasion machine. It scans the genome for a homologous duplex DNA sequence (typically the sister chromatid in mitotic cells, or the homologous chromosome in meiosis), and when it finds a match, the filament catalyzes **strand invasion**: the ssDNA tail physically displaces one strand of the homologous duplex and pairs with the complementary strand, forming a structure called a **D-loop** (displacement loop). This is the step that gives HR its name — it requires a homologous template, which is what makes the repair accurate rather than error-prone.

Once the D-loop forms, DNA polymerase extends the invading 3' end using the homologous strand as a template, effectively copying the missing information across the break. The subsequent steps depend on the sub-pathway: in the classical **double Holliday junction** (dHJ) pathway, the second broken end is captured, two four-way junctions form, and their resolution by specialized nucleases produces either crossover or non-crossover products. In the **synthesis-dependent strand annealing** (SDSA) pathway — the predominant pathway in mitotic cells — the extended strand is displaced and re-anneals to the other broken end, always producing non-crossovers. The choice between these pathways is tightly regulated: meiotic cells favor dHJ resolution to generate the crossovers essential for chromosome segregation, while mitotic cells favor SDSA to avoid the loss of heterozygosity that crossovers would cause. Understanding RAD51-mediated HR provides the mechanistic foundation for topics ranging from genetic mapping to cancer biology, since mutations in HR genes (BRCA1, BRCA2, RAD51) are among the most clinically significant in human genetics.
