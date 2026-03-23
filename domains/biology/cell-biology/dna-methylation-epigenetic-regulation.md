---
id: dna-methylation-epigenetic-regulation
title: DNA Methylation and Epigenetic Regulation
domain: biology
course: cell-biology
prerequisites:
- id: gene-regulation-eukaryotes
  type: hard
- id: histone-modifications-epigenetic
  type: soft
builds-toward:
- histone-post-translational-modifications-acetylation
tags:
- DNA-methylation
- epigenetics
- gene-regulation
stage: formal-systems
status: validated
---

# DNA Methylation and Epigenetic Regulation

## Core Idea
DNA methylation, primarily at cytosines in CpG dinucleotides, is a covalent epigenetic modification that silences genes by blocking transcription factor binding or recruiting methyl-binding proteins (MeCP2, MBD1). Maintenance methyltransferase (DNMT1) copies methylation patterns to newly synthesized DNA during replication, enabling heritable silencing across cell divisions independent of underlying DNA sequence. Aberrant methylation patterns (hypermethylation of CpG islands at gene promoters, hypomethylation of repetitive elements) characterize cancer and developmental diseases.

## How It's Best Learned
Map DNA methylation genome-wide using bisulfite sequencing; measure methyltransferase activity in vitro. Inhibit DNA methylation with 5-azacytidine and assess effects on gene expression and cell phenotype.

## Common Misconceptions
- DNA methylation always silences genes; unmethylated CpG islands at promoters are normally associated with transcription. - Methylation is erased and reset during differentiation; some patterns are remarkably stable.

## Questions

```yaml
- question: "After DNA replication, each daughter duplex is hemimethylated — the parental strand retains its methyl marks, but the newly synthesized strand does not. Which enzyme recognizes this state and what does it do?"
  type: multiple-choice
  options:
    - "DNMT3a and DNMT3b recognize hemimethylated DNA and establish entirely new methylation patterns de novo on both strands"
    - "DNMT1 recognizes hemimethylated CpG sites and methylates the corresponding cytosine on the newly synthesized strand, restoring the full symmetrical methylation pattern"
    - "TET enzymes recognize hemimethylated DNA and oxidize the methyl group on the parental strand, erasing the pattern to produce a clean demethylated state"
    - "MeCP2 recognizes hemimethylated sites and recruits histone acetyltransferases to activate the surrounding chromatin"
  answer: 1
  explanation: "DNMT1 has high substrate preference for hemimethylated over unmethylated DNA — this selectivity is precisely what makes it the maintenance methyltransferase. After replication, DNMT1 reads the existing methyl mark on the parental strand and deposits a methyl group at the symmetrical CpG on the new strand, restoring full methylation. DNMT3a and 3b are de novo methyltransferases that establish new patterns at previously unmethylated sites during development. TET enzymes oxidize 5mC to promote demethylation — the opposite function."

- question: "In many cancers, CpG islands at tumor suppressor gene promoters become hypermethylated. What is the most likely direct consequence for gene expression?"
  type: multiple-choice
  options:
    - "The tumor suppressor gene is constitutively overexpressed because methylation stabilizes the promoter-transcription factor complex"
    - "The tumor suppressor gene is silenced: methyl-binding proteins are recruited, which attract histone deacetylases that compact chromatin into a repressive state"
    - "The CpG sites mutate to non-CpG dinucleotides over time, permanently disrupting the promoter sequence"
    - "Transcription factors bind irreversibly to the methylated promoter, blocking all further regulatory changes"
  answer: 1
  explanation: "Normally, CpG islands at active gene promoters are unmethylated. When hypermethylated, methyl-CpG-binding domain proteins (MeCP2, MBD1) are recruited, which in turn recruit histone deacetylases and chromatin-remodeling complexes that compact the surrounding chromatin. This creates stable, long-term silencing of the tumor suppressor gene — functionally equivalent to a loss-of-function mutation but without altering the DNA sequence. Reactivating silenced tumor suppressors with DNMT inhibitors like 5-azacytidine is a therapeutic strategy in certain leukemias."

- question: "A differentiated liver cell can maintain its specific gene expression pattern across decades of cell division — with the same genes silenced and the same genes active as in the original liver cell — without any change to the DNA sequence itself."
  type: true-false
  answer: true
  explanation: "This heritability is the defining feature of epigenetic regulation. DNMT1 faithfully copies methylation patterns to daughter strands after every cell division, so the gene silencing established during differentiation is perpetuated in all cellular descendants. The liver cell's daughters are liver cells — they contain identical DNA sequences to all other cell types in the body, but a distinct methylation landscape that maintains cell identity. This is what 'epigenetic' means: heritable information about gene expression that is independent of the underlying DNA sequence."

- question: "All CpG dinucleotides in the human genome are methylated in differentiated cells, and this methylation uniformly silences nearby genes."
  type: true-false
  answer: false
  explanation: "Context matters enormously. CpG islands at gene promoters are normally *unmethylated* and are associated with active transcription — methylation at these sites silences the gene. Most CpG sites scattered throughout the genome (in repetitive elements, transposons, and gene bodies) are methylated even in transcriptionally active regions, and their methylation serves different functions: suppressing transposon activity, potentially modulating transcriptional elongation. 'DNA methylation silences genes' is a useful rule of thumb for promoter CpG islands but is an oversimplification for the genome as a whole."

- question: "Why is DNMT1 called the 'maintenance methyltransferase,' and how does it preserve a cell's epigenetic identity through cell division?"
  type: short-answer
  answer: "DNMT1 specifically recognizes hemimethylated CpG sites — where the parental strand is methylated but the newly synthesized strand is not — and methylates the complementary cytosine. This happens after every DNA replication cycle, perpetuating the inherited methylation pattern to daughter cells without requiring any new signal. Without this mechanism, methylation patterns would be diluted by half with each division."
  explanation: "De novo methyltransferases (DNMT3a/3b) establish methylation patterns during development; DNMT1 preserves them indefinitely. The selectivity for hemimethylated substrates is the key: DNMT1 copies what exists rather than creating new patterns. This allows differentiated cell identity to persist stably for decades — a liver cell's methylation landscape is replicated at every division, ensuring its daughters are also liver cells. When DNMT1 is disrupted experimentally, genome-wide demethylation leads to inappropriate gene activation, chromosomal instability, and cell death — demonstrating that methylation maintenance is essential for normal cell function."
```

## Explainer

You know from eukaryotic gene regulation that transcription depends on the accessibility of promoter and enhancer regions, and from histone modifications that chromatin structure is a major determinant of that accessibility. **DNA methylation** adds another layer to this regulatory system — one that operates directly on the DNA molecule itself rather than on the histone proteins around which it is wrapped. Together with histone modifications, methylation constitutes the cell's epigenetic memory: a system for recording gene expression states that persists across cell divisions without altering the underlying DNA sequence.

The chemistry is straightforward. **DNA methyltransferases (DNMTs)** transfer a methyl group from S-adenosylmethionine (SAM) to the 5-position of cytosine, producing **5-methylcytosine (5mC)**. In mammals, this modification occurs almost exclusively at **CpG dinucleotides** — a cytosine followed by a guanine on the same strand. CpG sites are relatively rare in the genome because 5mC spontaneously deaminates to thymine over evolutionary time, but they are concentrated in clusters called **CpG islands** near the promoters of roughly 60–70% of human genes. The key principle is: when CpG islands at a gene's promoter are methylated, that gene is typically silenced; when they are unmethylated, the gene can be expressed.

Methylation silences genes through two mechanisms. First, the methyl group physically protrudes into the major groove of DNA, directly blocking some transcription factors from binding their recognition sequences. Second, and more importantly, methylated CpG sites recruit **methyl-CpG-binding domain proteins** (MeCP2, MBD1, MBD2), which in turn recruit histone deacetylases and chromatin-remodeling complexes that compact the surrounding chromatin into a repressive state. This creates a self-reinforcing loop: DNA methylation recruits histone-modifying enzymes that close chromatin, and closed chromatin can attract additional methyltransferase activity. The result is stable, long-term silencing — exactly what the cell needs for permanently shutting down genes in differentiated tissues.

The heritability of methylation patterns is what makes this system truly epigenetic. After DNA replication, each daughter duplex is **hemimethylated** — the parental strand carries the methyl marks, but the newly synthesized strand does not. **DNMT1**, the **maintenance methyltransferase**, recognizes these hemimethylated CpG sites and methylates the corresponding cytosine on the new strand, faithfully copying the pattern. This is how a liver cell's methylation pattern is transmitted to its daughter cells for decades without any ongoing signal. When this system goes wrong — promoter **hypermethylation** silencing tumor suppressor genes, or genome-wide **hypomethylation** activating transposable elements — the consequences include cancer, developmental disorders, and genomic instability. The reversibility of methylation (via TET enzymes that oxidize 5mC) has also made it a therapeutic target: drugs like 5-azacytidine inhibit DNMTs, reactivating silenced genes in certain leukemias.
