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
stage: formal-systems
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

## Questions

```yaml
- question: "Two pink snapdragon plants (each with genotype C^R C^W, produced by crossing red and white parents) are crossed together. If incomplete dominance were actually blending inheritance — meaning alleles genuinely mix — what would you expect, and what actually happens?"
  type: multiple-choice
  options:
    - "Blending predicts all pink offspring; actual result is also all pink — the predictions agree"
    - "Blending predicts all pink offspring (since both parents are pink and the blend is fixed); actual result is 1 red : 2 pink : 1 white — the alleles segregated intact and the originals reappear"
    - "Blending predicts 3:1 pink:white; actual result is 1:2:1 red:pink:white"
    - "Both models predict 1:2:1 ratios but disagree on which phenotypes appear"
  answer: 1
  explanation: "This is the definitive test distinguishing incomplete dominance from blending inheritance. If alleles truly blended, the pink phenotype would be permanent — you could never recover red or white offspring from two pink parents. But in incomplete dominance, the alleles remain discrete and segregate through meiosis just as Mendel described. Crossing C^R C^W × C^R C^W produces 1/4 C^R C^R (red), 1/2 C^R C^W (pink), and 1/4 C^W C^W (white). The reappearance of red and white in the F2 proves the alleles never mixed — they coexisted in the pink heterozygotes and were sorted out by meiosis."

- question: "A person with type AB blood has genotype I^A I^B. Which correctly describes their red blood cell surface, and why?"
  type: multiple-choice
  options:
    - "Only A antigens are displayed, because I^A is dominant over I^B in most contexts"
    - "A blended intermediate antigen that is neither A nor B is produced"
    - "Both A and B antigens are displayed simultaneously — I^A and I^B are codominant, each directing synthesis of a different surface antigen independently"
    - "No antigens are displayed because the two alleles cancel each other's enzymatic activity"
  answer: 2
  explanation: "Codominance means both alleles are fully and independently expressed in the heterozygote — not a blend and not one masking the other. The I^A allele encodes an enzyme that adds N-acetylgalactosamine to a cell-surface glycoprotein (producing the A antigen); the I^B allele encodes a different enzyme that adds galactose (producing the B antigen). Both enzymes function independently in the same cell, so both antigens appear simultaneously. This is why type AB individuals can receive blood from any ABO type (universal recipients) but can only donate to other AB individuals."

- question: "Epistasis modifies the phenotypic ratios expected from a dihybrid cross, but the underlying alleles at each locus still segregate according to standard Mendelian rules during meiosis."
  type: true-false
  answer: true
  explanation: "Epistasis operates at the level of phenotype expression, not allele transmission. When the E locus in Labrador retrievers masks the B locus, the 9:3:3:1 ratio becomes 9:3:4, but the alleles at both loci still assort independently according to Mendel's law of independent assortment (assuming the loci are on different chromosomes). Epistasis is a gene-gene interaction at the biochemical pathway level: one gene's product controls whether another gene's product is ever deployed. The mechanism of allele transmission — meiosis, segregation, independent assortment — is unchanged."

- question: "Incomplete dominance is a form of blending inheritance because the intermediate phenotype in heterozygotes proves the two alleles have chemically mixed with each other."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about incomplete dominance. The intermediate phenotype arises from gene dosage, not allele mixing. A C^R C^W snapdragon is pink because one copy of C^R produces only half the red pigment that two copies produce — the white allele doesn't contribute pigment, it simply means fewer pigment-producing alleles are present. The alleles themselves remain completely separate and intact. The proof: cross two pink plants and you recover red and white offspring — impossible if the alleles had truly blended. Blending inheritance predicts traits merge permanently; incomplete dominance predicts they recover."

- question: "How does incomplete dominance differ from true blending inheritance, and what experimental result demonstrates the difference?"
  type: short-answer
  answer: "In blending inheritance, the alleles of the two parents permanently merge in the offspring — the original phenotypes can never be recovered. In incomplete dominance, the alleles remain discrete but the heterozygote's phenotype is intermediate (due to gene dosage: fewer allele copies produce less gene product). The definitive experiment is crossing two F1 heterozygotes: if blending occurred, both parents are identical (pink × pink) and all offspring should be pink. Instead, the F2 generation shows a 1:2:1 ratio of red:pink:white — the original red and white phenotypes reappear because the alleles segregated intact through meiosis."
  explanation: "Mendel's actual discovery was that discrete factors (alleles) are transmitted unchanged through generations. Incomplete dominance can superficially resemble blending because F1 heterozygotes look intermediate, but the F2 ratio is the giveaway. This experiment was historically important because pre-Mendelian biologists widely believed in blending inheritance, which would predict that traits average out over generations and that variation should decrease toward the mean — a theory that could not explain the persistence of variation in populations. Mendelian discrete inheritance solved this problem."
```

## Explainer

Mendel's principles of dominance and recessiveness predict clean 3:1 ratios in monohybrid crosses because one allele completely masks the other. But many genes do not behave this way. **Incomplete dominance** occurs when the heterozygote displays a phenotype intermediate between the two homozygotes. The classic example is snapdragon flower color: a cross between red (C^R C^R) and white (C^W C^W) produces pink heterozygotes (C^R C^W), and the F2 generation shows a 1:2:1 ratio of red:pink:white instead of 3:1. Crucially, this is *not* blending inheritance — the alleles do not mix. If you cross two pink F1 plants, red and white offspring reappear in the F2 because the alleles segregated intact through meiosis. The intermediate phenotype arises because one copy of C^R produces only half the amount of red pigment that two copies produce.

**Codominance** takes this further: both alleles are fully expressed simultaneously in the heterozygote rather than producing a blend. The ABO blood group system illustrates this. The I^A and I^B alleles are codominant — a person with genotype I^A I^B has both A and B antigens on their red blood cells (type AB blood), not some intermediate antigen. Each allele encodes a different enzyme that adds a different sugar to the cell surface glycoprotein, and both enzymes function independently. Note that I^A and I^B are each dominant over the i allele (which encodes no functional enzyme), so the ABO system demonstrates codominance *and* simple dominance simultaneously, depending on which allele pair you examine.

**Polygenic inheritance** explains traits like human height, skin color, and blood pressure, which show continuous variation rather than discrete categories. These traits are influenced by many loci, each contributing a small additive effect. If two loci each have two alleles contributing to skin pigmentation, a cross between two heterozygous parents can produce five phenotypic classes in a 1:4:6:4:1 ratio (a binomial distribution), creating what looks like a smooth gradient as the number of contributing loci increases. Add environmental variation on top, and the result is the bell-shaped distribution typical of quantitative traits. The underlying genetics are still Mendelian at each individual locus — it is the summation across many loci that produces the continuous phenotype.

**Epistasis** occurs when the alleles at one gene modify or mask the expression of alleles at another gene. In Labrador retriever coat color, the E gene controls whether pigment is deposited at all: dogs homozygous for the recessive e allele (ee) are yellow regardless of their genotype at the B locus (which determines black vs. brown pigment). This gives a modified 9:3:4 ratio instead of the expected 9:3:3:1 in a dihybrid cross, because the 3 (bbE_) and 1 (bbee) classes are phenotypically merged. Epistasis reveals that genes do not act in isolation — they operate within pathways, and the output of one step constrains what downstream steps can do. **Pleiotropy**, the final pattern, flips this relationship: a single gene affects multiple traits. The sickle-cell allele of hemoglobin causes anemia, organ damage, and malaria resistance simultaneously — all traceable to a single amino acid change that alters red blood cell shape under low oxygen conditions. Together, these patterns demonstrate that the one-gene-one-trait model is a useful starting point but not the full picture of how genotype maps to phenotype.
