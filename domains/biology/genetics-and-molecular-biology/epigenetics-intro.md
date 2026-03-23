---
id: epigenetics-intro
title: Epigenetics
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: gene-regulation-eukaryotes
  type: hard
- id: dna-structure
  type: soft
builds-toward:
- genomics-overview
tags:
- epigenetics
- methylation
- histone modification
- chromatin
- imprinting
stage: formal-systems
status: validated
---

# Epigenetics

## Core Idea
Epigenetics refers to heritable changes in gene expression that do not involve alterations to the DNA sequence. Key mechanisms include DNA methylation (addition of methyl groups to cytosine, typically silencing genes) and histone modification (acetylation, methylation, phosphorylation altering chromatin accessibility). These marks can be maintained through cell divisions and in some cases transmitted across generations. Genomic imprinting — where a gene is expressed from only one parental allele based on its epigenetic marks — is one striking example with clinical implications in disorders like Prader-Willi and Angelman syndrome.

## How It's Best Learned
Compare open (euchromatin) and closed (heterochromatin) chromatin states and the histone modifications associated with each. Trace how an epigenetic mark is copied to daughter strands after DNA replication.

## Common Misconceptions
- Epigenetic changes are not mutations; the DNA sequence is unchanged.
- Not all epigenetic marks are heritable across generations; most are reset during gametogenesis.

## Questions

```yaml
- question: "Identical twins are genetically identical at birth, but by age 50 they often show markedly different patterns of gene expression. What is the most plausible molecular explanation?"
  type: multiple-choice
  options:
    - "Accumulated DNA mutations in one twin altered protein-coding sequences"
    - "Divergent environmental exposures caused different DNA methylation and histone modification patterns to accumulate over time"
    - "One twin's ribosomes became less efficient, reducing overall transcription rates"
    - "Meiotic recombination events occurred in somatic cells, reshuffling gene order"
  answer: 1
  explanation: "Epigenetic marks — particularly DNA methylation and histone modifications — accumulate in response to environmental factors like diet, stress, and toxins, and are maintained through cell divisions. Identical twins share the same DNA sequence, so diverging gene expression reflects epigenetic, not genetic, differences. Option A is wrong because the question specifies expression patterns, not sequence changes; and large-scale somatic mutations or ribosome inefficiency do not explain the systematic, heritable differences observed."

- question: "In a cell that has just undergone DNA replication, the newly synthesized strand lacks the methylation marks present on the original (template) strand. Which mechanism restores these marks?"
  type: multiple-choice
  options:
    - "De novo methyltransferases randomly methylate all cytosines on the new strand"
    - "Maintenance methyltransferase (DNMT1) recognizes the half-methylated CpG sites and methylates the new strand to match the template"
    - "RNA interference machinery detects unmethylated CpG sites and adds methyl groups"
    - "The cell does not restore methylation — daughter cells begin with blank epigenomes"
  answer: 1
  explanation: "DNMT1 is a maintenance methyltransferase that recognizes hemi-methylated CpG sites — where one strand is methylated and the newly synthesized strand is not — and methylates the new strand to match. This is the key mechanism by which epigenetic marks are faithfully propagated through cell division. De novo methyltransferases (DNMT3a/3b) establish new marks but do not maintain existing ones, and the cell absolutely does restore methylation patterns to preserve cell identity."

- question: "Epigenetic modifications alter gene expression by changing the nucleotide sequence of DNA."
  type: true-false
  answer: false
  explanation: "This is the central misconception about epigenetics. Epigenetic changes — DNA methylation, histone acetylation, histone methylation — modify how DNA is packaged and accessed without altering the underlying nucleotide sequence (A, T, G, C). The DNA sequence remains identical; what changes is whether and how that sequence is read. This is what makes epigenetics distinct from mutation."

- question: "Most epigenetic marks in mammals are erased during gametogenesis, which is why true transgenerational epigenetic inheritance (marks passing from grandparent to grandchild) is the exception rather than the rule."
  type: true-false
  answer: true
  explanation: "During gametogenesis (the formation of eggs and sperm), the genome undergoes extensive epigenetic reprogramming — most methylation marks are stripped and re-established. This prevents the faithful transmission of somatic epigenetic states across generations. Genuine transgenerational inheritance does occur in some cases (certain imprinted loci, for instance), but these are exceptions to a general pattern of epigenetic resetting, not the norm."

- question: "A deletion in the chromosomal region 15q11-13 causes Prader-Willi syndrome when inherited from the father, but Angelman syndrome when inherited from the mother — even though the deleted region is the same. Why does the parent of origin matter?"
  type: short-answer
  answer: "This is because of genomic imprinting. In the 15q11-13 region, different genes are imprinted (silenced) depending on which parental chromosome they're on. Some genes are only expressed from the paternal copy (the maternal copy is epigenetically silenced), while others are only expressed from the maternal copy. If the paternal copy is deleted, the maternally-imprinted genes have no functional copy — causing Prader-Willi. If the maternal copy is deleted, the paternally-imprinted genes lack a functional copy — causing Angelman. The same deletion has opposite consequences because epigenetic marks, not DNA sequence, determine which parental allele is active."
  explanation: "Imprinting means cells have already silenced one parental allele via methylation, so the remaining allele cannot compensate for a deletion on the other chromosome. This powerfully illustrates that epigenetic marks carry functional information beyond the DNA sequence — information that is parent-of-origin specific and established during gamete formation."
```

## Explainer

From your study of eukaryotic gene regulation, you know that cells control which genes are expressed through transcription factors, enhancers, and chromatin structure. **Epigenetics** extends this picture by revealing that some of these regulatory states can be locked in and faithfully copied when a cell divides — even passed to daughter cells that never see the original signal. The DNA sequence itself is unchanged, but chemical modifications to the DNA and its associated histone proteins create a second layer of heritable information sitting "on top of" the genetic code.

The two best-understood epigenetic mechanisms work through distinct chemistry but converge on the same outcome: controlling whether chromatin is open (accessible for transcription) or closed (silent). **DNA methylation** involves adding a methyl group (–CH₃) to cytosine bases, predominantly at CpG dinucleotides. When a gene's promoter region is heavily methylated, transcription factors generally cannot bind, and the gene is silenced. After DNA replication, the newly synthesized strand is initially unmethylated, but **maintenance methyltransferase (DNMT1)** recognizes the half-methylated CpG sites and methylates the new strand to match the old one — this is how the mark is copied through cell divisions. **Histone modifications** are more diverse: acetylation of histone tails generally opens chromatin (by neutralizing positive charges, loosening DNA-histone contacts), while certain methylation patterns on histones (like H3K9me3) recruit proteins that compact chromatin into silent heterochromatin. The interplay between DNA methylation and histone modifications creates stable, self-reinforcing chromatin states.

A striking demonstration of epigenetics in action is **genomic imprinting**. In most genes, both the maternal and paternal copies are expressed. But for ~100 imprinted genes in humans, only one parental copy is active — the other is silenced by epigenetic marks established during egg or sperm development. The IGF2 gene, for example, is expressed only from the paternal allele; the maternal copy is methylated and silent. If you inherit a defective paternal copy, you cannot compensate with the maternal one because it is epigenetically shut off. This explains why deletions of the same chromosomal region cause completely different diseases depending on which parent contributed it: loss of the paternal copy at 15q11-13 causes Prader-Willi syndrome (obesity, intellectual disability), while loss of the maternal copy causes Angelman syndrome (seizures, movement disorder) — same deletion, opposite parent, different imprinted genes affected.

The scope of epigenetics extends well beyond imprinting. Every cell in your body has the same DNA, yet a neuron and a liver cell express radically different gene sets. Epigenetic marks established during development lock in cell-type-specific expression patterns, which is why a skin cell stays a skin cell through thousands of divisions. Environmental factors — nutrition, stress, toxins — can alter epigenetic marks, providing a molecular mechanism for how experience can modify gene expression without mutating DNA. However, most epigenetic marks are erased and reset during gametogenesis (the production of eggs and sperm), which limits true transgenerational epigenetic inheritance in mammals. The cases where marks do escape this reprogramming are fascinating exceptions, not the rule.
