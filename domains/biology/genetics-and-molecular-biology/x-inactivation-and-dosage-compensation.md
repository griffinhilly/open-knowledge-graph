---
id: x-inactivation-and-dosage-compensation
title: X-Inactivation and Dosage Compensation
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: sex-linked-inheritance
  type: hard
- id: epigenetics-intro
  type: soft
- id: dna-methylation-and-epigenetic-silencing
  type: soft
tags:
- x-inactivation
- lyonization
- xist
- dosage-compensation
- barr-body
stage: formal-systems
status: draft
---

# X-Inactivation and Dosage Compensation

## Core Idea
X-inactivation (lyonization) is the epigenetic silencing of one X chromosome in female mammals, equalizing X-linked gene dosage between XX females and XY males. The process is initiated by Xist RNA, transcribed from the X-inactivation center (Xic), which coats the chromosome in cis and recruits chromatin-silencing complexes. Methylation of promoter CpG islands and repressive histone marks establish and maintain the heterochromatic inactive X (Xi). X-inactivation is random—either the maternal or paternal X is silenced in each cell—creating a mosaic phenotype in females. Early X-inactivation patterns establish developmental cell lineages, and reactivation of the inactivated X occurs in germ cells. Some disorders (e.g., Rett syndrome from MECP2 mutations) show variable severity in heterozygous females due to unequal X-inactivation patterns.

## Explainer

From sex-linked inheritance, you know that females carry two X chromosomes while males carry one X and one Y. This creates a potential dosage problem: without compensation, females would produce twice the amount of every X-linked gene product compared to males. **Dosage compensation** solves this by transcriptionally silencing nearly an entire X chromosome in every female cell, a process discovered by Mary Lyon in 1961 and accordingly called **lyonization**. The result is that both sexes effectively operate with a single active X.

The molecular trigger is a long non-coding RNA called **Xist** (X-inactive specific transcript), produced from a region called the **X-inactivation center (Xic)** on the X chromosome chosen for silencing. Early in embryonic development, one X in each cell begins to upregulate Xist expression. The Xist RNA does something remarkable — it physically coats the chromosome from which it is transcribed, spreading outward from the Xic in cis (meaning it stays on its chromosome of origin rather than drifting to the other X). As Xist accumulates, it recruits chromatin-silencing complexes: Polycomb repressive complexes deposit the repressive histone mark H3K27me3, histone deacetylases remove activating acetyl marks, and DNA methyltransferases methylate CpG islands at gene promoters. Layer by layer, the chromosome is converted into a densely compacted, transcriptionally inert structure visible under the microscope as the **Barr body**.

The choice of which X to inactivate is **random** — in each cell of the early embryo, either the maternal or paternal X is silenced with roughly equal probability. Once made, the choice is **heritable**: all daughter cells maintain the same inactive X through DNA methylation and histone modification patterns that are faithfully copied during cell division. Because the decision is made independently in each cell, the adult female is a **mosaic** of two cell populations — some expressing genes from the maternal X, others from the paternal X. The classic visible example is the calico cat: the patchy orange and black fur pattern arises because the gene for coat color is X-linked, and random inactivation produces patches of cells expressing one allele or the other.

This mosaicism has medical significance. A female heterozygous for an X-linked disease mutation will have some cells expressing the normal allele and others expressing the mutant allele. If inactivation happens to skew — silencing the normal X in a disproportionate number of cells — symptoms can be more severe. This explains the variable expressivity of conditions like **Rett syndrome**, where MECP2 mutations on one X can range from asymptomatic to severe depending on the inactivation pattern. Notably, X-inactivation is reversed in germ cells during oogenesis, so both X chromosomes are reactivated before meiosis, ensuring that each egg carries a fully functional X regardless of which was silenced in the somatic lineage.
