---
id: dna-methylation-and-epigenetic-silencing
title: DNA Methylation and Epigenetic Gene Silencing
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: epigenetics-intro
  type: hard
- id: dna-structure
  type: soft
builds-toward:
- genomic-imprinting-and-parent-of-origin-effects
- x-inactivation-and-dosage-compensation
tags:
- dna-methylation
- cpg-islands
- methyl-binding-proteins
- dnmts
- silencing
stage: formal-systems
status: validated
---

# DNA Methylation and Epigenetic Gene Silencing

## Core Idea
DNA methylation—the covalent addition of methyl groups typically at cytosine residues in CpG dinucleotides—is a covalent modification that suppresses gene expression and is essential for normal development, X-inactivation, and genomic imprinting. DNA methyltransferases (DNMT1, DNMT3A, DNMT3B) catalyze methylation; DNMT1 maintains methylation patterns during DNA replication by recognizing hemimethylated DNA. Methyl-binding proteins (MeCP2, MBD1-MBD4) recognize 5-methylcytosine and recruit repressive chromatin complexes containing HDACs and histone methyltransferases. Methylation patterns are stably maintained through cell division, establishing a heritable but reversible epigenetic code. Aberrant methylation (hypermethylation of tumor suppressor genes, hypomethylation of oncogenes) is implicated in cancer and developmental disorders.

## Questions

```yaml
- question: "A tumor suppressor gene is silenced in cancer cells, but DNA sequencing confirms the gene's coding sequence is completely intact. Which mechanism most likely explains the silencing?"
  type: multiple-choice
  options:
    - "Deletion of DNMT1, which prevents maintenance methylation and thus activates silencing"
    - "Hypermethylation of the CpG island in the gene's promoter region, recruiting chromatin-condensing complexes"
    - "Hypomethylation of the gene body, which reduces transcription elongation efficiency"
    - "Loss of histone acetylation marks globally across all chromosomes"
  answer: 1
  explanation: "Aberrant hypermethylation of CpG islands at tumor suppressor promoters is one of the most common epigenetic events in cancer. In normal cells, CpG islands near gene promoters are typically unmethylated, keeping the gene accessible. When they become methylated, methyl-binding proteins (MeCP2, MBDs) recruit HDACs and histone methyltransferases, condensing chromatin and silencing the gene — functionally equivalent to deleting it, but without altering the DNA sequence. This is why the sequence is intact but the gene is off."

- question: "Which best describes how DNA methylation silences a gene — the primary mechanism of action?"
  type: multiple-choice
  options:
    - "The methyl group directly modifies the mRNA transcript, producing a truncated nonfunctional protein"
    - "Methylated cytosines spontaneously mutate to thymine over time, eventually destroying the gene permanently"
    - "The methyl group is large enough to sterically block RNA polymerase from binding the promoter directly"
    - "Methyl-binding proteins recognize methylated CpGs and recruit histone deacetylases and chromatin-remodeling complexes, compacting the chromatin into a transcriptionally silent state"
  answer: 3
  explanation: "The primary silencing cascade operates through methyl-binding proteins, not direct steric blockade. When CpGs are methylated, MeCP2 and MBD proteins bind the methyl groups and recruit HDACs (which strip activating acetyl groups from histones) and histone methyltransferases (which add repressive methyl marks to histones). The resulting compact, heterochromatic structure buries the promoter and prevents transcription initiation. Direct steric blockade by the methyl group itself is a secondary, less important effect."

- question: "DNA methylation patterns are heritable through cell division because DNMT1 recognizes hemimethylated DNA (one strand methylated, one not) after replication and methylates the new strand to restore the original pattern."
  type: true-false
  answer: true
  explanation: "This is the maintenance methylation mechanism — the key to epigenetic inheritance. When DNA replicates, the new strand is initially unmethylated, producing hemimethylated duplexes. DNMT1 has a strong preference for hemimethylated over unmethylated DNA and is recruited to replication forks, where it faithfully copies the parental methylation pattern onto the new strand. This is why a liver cell divides to produce liver cells: the methylation patterns silencing neuron-specific genes are propagated to every daughter cell."

- question: "DNA methylation is a permanent, irreversible epigenetic modification because it involves a covalent chemical change to the DNA molecule."
  type: true-false
  answer: false
  explanation: "Methylation is covalent but reversible. Active demethylation is carried out by TET enzymes (which oxidize 5-methylcytosine through intermediates that are removed by base excision repair), and passive demethylation occurs when DNMT1 is absent or inhibited during replication (new strands remain unmethylated and the pattern dilutes). Critically, methylation does NOT alter the DNA sequence — only a cytosine base modification is added or removed, leaving the sequence intact. This reversibility distinguishes epigenetic silencing from mutation and underlies the therapeutic strategy of DNMT inhibitors like azacitidine."

- question: "Explain how DNA methylation differs from a genetic mutation in terms of effect on DNA sequence, heritability, and reversibility — and why these differences matter for cancer therapy."
  type: short-answer
  answer: "A genetic mutation changes the DNA sequence itself — a permanent alteration to the bases that is inherited by all descendant cells and cannot be corrected without genome editing. DNA methylation adds a methyl group to cytosine without changing the underlying sequence; the information content of the DNA is unchanged. Like mutations, methylation patterns are heritable through cell division (via DNMT1 maintenance). Unlike mutations, they are reversible: DNMT inhibitors (azacitidine, decitabine) block DNMT1, causing passive loss of methylation during replication, which can reactivate silenced tumor suppressor genes. This is a clinically validated cancer therapy — targeting epigenetic silencing rather than the DNA sequence itself."
  explanation: "The reversibility of methylation makes it an attractive therapeutic target that mutation repair is not. It also underlies the distinction between epigenetics (heritable regulatory states not encoded in sequence) and genetics (heritable sequence information). Both are involved in cancer, but only epigenetic silencing can be reversed pharmacologically without genome editing."
```

## Explainer

From your introduction to epigenetics, you understand that cells can regulate gene expression through mechanisms that don't alter the DNA sequence itself. DNA methylation is the most chemically direct of these mechanisms: an enzyme physically attaches a **methyl group** (–CH₃) to the 5-carbon of cytosine, converting it to **5-methylcytosine**. This modification occurs almost exclusively at **CpG dinucleotides** — places where a cytosine is followed by a guanine on the same strand. The human genome contains roughly 28 million CpG sites, and about 70-80% of them are methylated in any given cell type. The critical exception is **CpG islands** — clusters of CpG sites near gene promoters that are typically unmethylated in normal cells, keeping those genes accessible for transcription.

The mechanism by which methylation silences genes operates through two complementary pathways. First, the methyl group itself can physically block transcription factors from binding to the promoter — it occupies space in the major groove of DNA where proteins need to make contact. Second, and more importantly, a family of **methyl-CpG-binding proteins** (MeCP2, MBD1-4) specifically recognizes methylated CpGs and recruits **histone deacetylases (HDACs)** and histone methyltransferases. These enzymes modify the histone proteins that DNA wraps around, compacting the chromatin into a tightly packed, transcriptionally inactive state. Methylation thus triggers a cascade: methylated DNA attracts proteins that restructure chromatin, which buries the gene and prevents the transcription machinery from accessing it.

What makes methylation an epigenetic mechanism — rather than just a regulatory one — is its **heritability through cell division**. When DNA replicates, each daughter strand is initially unmethylated, producing **hemimethylated** DNA (one strand methylated, one not). The maintenance methyltransferase **DNMT1** recognizes these hemimethylated sites and adds methyl groups to the new strand, faithfully copying the methylation pattern. This is why a liver cell's daughter cells are liver cells, not neurons: the methylation patterns that silence neuron-specific genes are propagated every time the cell divides. Meanwhile, **DNMT3A** and **DNMT3B** are *de novo* methyltransferases that establish new methylation patterns during embryonic development, setting up the tissue-specific gene expression programs that define each cell type.

When this system goes wrong, the consequences can be severe. **Hypermethylation** of CpG islands at tumor suppressor gene promoters silences genes that normally restrain cell growth — this is a common early event in many cancers and functionally equivalent to deleting the gene. Conversely, **hypomethylation** can activate oncogenes or repetitive elements that are normally kept silent, destabilizing the genome. The reversibility of methylation — unlike a DNA mutation, a methyl group can be actively or passively removed — makes it an attractive target for cancer therapy. Drugs like azacitidine and decitabine inhibit DNA methyltransferases, reactivating silenced tumor suppressor genes. Understanding methylation thus connects basic molecular biology to both normal development and disease.
