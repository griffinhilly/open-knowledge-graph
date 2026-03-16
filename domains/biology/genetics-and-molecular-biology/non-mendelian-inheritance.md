---
id: non-mendelian-inheritance
title: Non-Mendelian Inheritance Patterns
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dominance-and-recessiveness
  type: hard
- id: sex-linked-inheritance
  type: soft
builds-toward:
- population-genetics-intro
tags:
- incomplete dominance
- codominance
- polygenic traits
- pleiotropy
- epistasis
stage: abstract-reasoning
status: validated
---
# Non-Mendelian Inheritance Patterns

## Core Idea
Many traits do not follow strict Mendelian dominance patterns. Incomplete dominance produces a blended phenotype in heterozygotes (e.g., red × white flowers → pink). Codominance results in simultaneous expression of both alleles (e.g., AB blood type). Polygenic traits such as height are controlled by many loci, producing continuous variation. Epistasis occurs when alleles at one locus mask or modify the expression of alleles at another locus, producing unexpected phenotypic ratios. Pleiotropy describes a single gene affecting multiple phenotypic traits, illustrating that genes rarely act in isolation.

## How It's Best Learned
Classify each pattern by its F2 phenotypic ratios and the molecular logic behind each. Practice modified Punnett squares for epistatic interactions and predict offspring ratios.

## Common Misconceptions
- Incomplete dominance is not blending inheritance; the alleles themselves remain unchanged in the offspring.
- Epistasis modifies Mendelian ratios but still involves discrete alleles and meiotic segregation.

## Explainer

Mendel's principles of dominance and recessiveness predict clean 3:1 ratios in monohybrid crosses because one allele completely masks the other. But many genes do not behave this way. **Incomplete dominance** occurs when the heterozygote displays a phenotype intermediate between the two homozygotes. The classic example is snapdragon flower color: a cross between red (C^R C^R) and white (C^W C^W) produces pink heterozygotes (C^R C^W), and the F2 generation shows a 1:2:1 ratio of red:pink:white instead of 3:1. Crucially, this is *not* blending inheritance — the alleles do not mix. If you cross two pink F1 plants, red and white offspring reappear in the F2 because the alleles segregated intact through meiosis. The intermediate phenotype arises because one copy of C^R produces only half the amount of red pigment that two copies produce.

**Codominance** takes this further: both alleles are fully expressed simultaneously in the heterozygote rather than producing a blend. The ABO blood group system illustrates this. The I^A and I^B alleles are codominant — a person with genotype I^A I^B has both A and B antigens on their red blood cells (type AB blood), not some intermediate antigen. Each allele encodes a different enzyme that adds a different sugar to the cell surface glycoprotein, and both enzymes function independently. Note that I^A and I^B are each dominant over the i allele (which encodes no functional enzyme), so the ABO system demonstrates codominance *and* simple dominance simultaneously, depending on which allele pair you examine.

**Polygenic inheritance** explains traits like human height, skin color, and blood pressure, which show continuous variation rather than discrete categories. These traits are influenced by many loci, each contributing a small additive effect. If two loci each have two alleles contributing to skin pigmentation, a cross between two heterozygous parents can produce five phenotypic classes in a 1:4:6:4:1 ratio (a binomial distribution), creating what looks like a smooth gradient as the number of contributing loci increases. Add environmental variation on top, and the result is the bell-shaped distribution typical of quantitative traits. The underlying genetics are still Mendelian at each individual locus — it is the summation across many loci that produces the continuous phenotype.

**Epistasis** occurs when the alleles at one gene modify or mask the expression of alleles at another gene. In Labrador retriever coat color, the E gene controls whether pigment is deposited at all: dogs homozygous for the recessive e allele (ee) are yellow regardless of their genotype at the B locus (which determines black vs. brown pigment). This gives a modified 9:3:4 ratio instead of the expected 9:3:3:1 in a dihybrid cross, because the 3 (bbE_) and 1 (bbee) classes are phenotypically merged. Epistasis reveals that genes do not act in isolation — they operate within pathways, and the output of one step constrains what downstream steps can do. **Pleiotropy**, the final pattern, flips this relationship: a single gene affects multiple traits. The sickle-cell allele of hemoglobin causes anemia, organ damage, and malaria resistance simultaneously — all traceable to a single amino acid change that alters red blood cell shape under low oxygen conditions. Together, these patterns demonstrate that the one-gene-one-trait model is a useful starting point but not the full picture of how genotype maps to phenotype.
