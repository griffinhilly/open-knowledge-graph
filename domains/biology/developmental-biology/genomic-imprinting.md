---
id: genomic-imprinting
title: Genomic Imprinting
domain: biology
course: developmental-biology
prerequisites:
- id: chromatin-in-development
  type: hard
- id: gene-expression-overview
  type: hard
builds-toward: []
tags:
- genomic-imprinting
- parent-of-origin
- DNA-methylation
- Igf2
- H19
- Prader-Willi
- Angelman
stage: expert
status: validated
---
# Genomic Imprinting

## Core Idea
Genomic imprinting is an epigenetic phenomenon in which certain genes are expressed from only one parental allele — either the maternal or paternal copy — while the other is silenced through DNA methylation established in the parental germline. Approximately 100-200 imprinted genes have been identified in mammals, many clustered in imprinting control regions. Imprinting is established during gametogenesis (differently in sperm versus eggs), maintained through development, and erased and re-established each generation in the germline. Many imprinted genes regulate growth: paternally expressed genes (like Igf2) tend to promote growth, while maternally expressed genes (like H19, Igf2r) tend to restrict it — consistent with the parental conflict hypothesis. Imprinting disorders (Prader-Willi, Angelman, Beckwith-Wiedemann syndromes) demonstrate the clinical consequences of disrupted mono-allelic expression.

## Questions

```yaml
- question: "The paternal allele of Igf2 (insulin-like growth factor 2) is expressed, while the maternal allele is silenced. If a child inherits a deletion of Igf2 from their father, what is the expected growth phenotype?"
  type: multiple-choice
  options:
    - "Normal growth, because the maternal allele compensates"
    - "Growth restriction, because the only active copy (paternal) is deleted, and the intact maternal copy is silenced by imprinting and cannot compensate"
    - "Overgrowth, because loss of Igf2 removes growth inhibition"
    - "No effect, because Igf2 is not important for growth"
  answer: 1
  explanation: "This is the key clinical consequence of imprinting: for imprinted genes, cells are functionally hemizygous — they rely on only one allele. The maternal Igf2 allele is present but epigenetically silenced (methylated), so it cannot compensate for loss of the paternal copy. A paternal deletion effectively eliminates Igf2 expression entirely, causing growth restriction. Conversely, inheriting the same deletion from the mother would have no effect (the maternal allele is already silent). This parent-of-origin-dependent inheritance pattern is the diagnostic hallmark of imprinting disorders."

- question: "Genomic imprinting is caused by differences in DNA sequence between the maternal and paternal alleles."
  type: true-false
  answer: false
  explanation: "Imprinting is epigenetic, not genetic — the DNA sequence of the maternal and paternal alleles is identical. The difference is in the DNA methylation pattern, established during gametogenesis. In sperm, certain imprinting control regions are methylated; in eggs, different regions are methylated. After fertilization, these differential methylation marks are maintained through DNA replication by maintenance methyltransferase (DNMT1), ensuring that the parental identity of each allele is preserved. The imprinting marks are erased in primordial germ cells and re-established according to the sex of the developing individual, resetting the cycle each generation."

- question: "Explain why deletion of the same chromosomal region (15q11-q13) causes Prader-Willi syndrome when inherited from the father but Angelman syndrome when inherited from the mother."
  type: short-answer
  answer: "The 15q11-q13 region contains both paternally expressed genes (whose loss causes Prader-Willi syndrome — obesity, intellectual disability, hypotonia) and maternally expressed genes (specifically UBE3A, whose loss causes Angelman syndrome — severe intellectual disability, seizures, happy demeanor). When the paternal copy is deleted, the paternally expressed genes are lost and the (silenced) maternal copies cannot compensate — causing Prader-Willi. When the maternal copy is deleted, the maternally expressed UBE3A gene is lost and the (silenced) paternal copy cannot compensate — causing Angelman. The same deletion produces different syndromes depending on parent of origin because different genes in the region are active on each parental chromosome."
  explanation: "These reciprocal syndromes from the same deletion were key evidence for genomic imprinting in humans. They also demonstrate a practical clinical concern: genetic counseling for imprinting disorders must account for which parent carries the mutation, not just whether the mutation is present."
```

## Explainer

In standard Mendelian genetics, it does not matter whether an allele comes from the mother or the father — both are expected to function equally. **Genomic imprinting** violates this assumption. For imprinted genes, only one parental allele is active; the other is silenced by epigenetic modifications (primarily DNA methylation) established during gamete formation. This means cells are functionally hemizygous at imprinted loci — a loss-of-function mutation or deletion of the active allele cannot be compensated by the silent allele from the other parent.

The molecular mechanism involves **differentially methylated regions** (DMRs) — DNA sequences that are methylated on one parental allele but not the other. These methylation differences are established during **gametogenesis**: oocytes and sperm methylate different imprinting control regions. After fertilization, the differential methylation is faithfully maintained through development by DNMT1 (maintenance methyltransferase), which copies methylation patterns to the newly synthesized DNA strand during replication. The methylation state of the imprinting control region determines which allele's genes are expressed — through mechanisms including blocking CTCF insulator binding (Igf2/H19 locus), directing antisense RNA expression that silences nearby genes, or directly recruiting repressive chromatin complexes.

The **parental conflict hypothesis** (Haig, 1993) provides an evolutionary explanation for why imprinting exists. In mammals, the mother invests heavily in each offspring through pregnancy and lactation, and her evolutionary interest is to distribute resources among all her offspring (present and future). The father's evolutionary interest is to maximize resource extraction for his offspring specifically (since future offspring may have a different father). Consistent with this prediction, many paternally expressed imprinted genes promote fetal growth (Igf2 — insulin-like growth factor 2), while many maternally expressed genes restrict growth (Igf2r, H19, p57). Imprinting thus represents a molecular tug-of-war between parental genomes over resource allocation to offspring.

Imprinting disorders illustrate the clinical consequences. **Prader-Willi syndrome** (loss of paternally expressed genes at 15q11-q13) causes insatiable appetite, obesity, and intellectual disability. **Angelman syndrome** (loss of the maternally expressed UBE3A gene at the same locus) causes severe intellectual disability, seizures, and characteristic happy demeanor. **Beckwith-Wiedemann syndrome** (overexpression of Igf2 due to imprinting defects at 11p15) causes overgrowth and increased cancer risk. These disorders demonstrate that normal development requires precisely one active copy of imprinted genes — neither zero (when the active allele is lost) nor two (when the silent allele is inappropriately activated). Imprinting adds a layer of regulation beyond the DNA sequence, making the parental history of each chromosome developmentally relevant.
