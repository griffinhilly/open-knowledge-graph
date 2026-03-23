---
id: transcription
title: 'Transcription: DNA to RNA'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-structure
  type: hard
- id: gene-expression-overview
  type: hard
- id: enzyme-structure-and-function
  type: soft
builds-toward:
- rna-types-and-structure
- rna-processing
- gene-regulation-prokaryotes
tags:
- transcription
- RNA polymerase
- promoter
- mRNA
- template strand
stage: formal-systems
status: validated
---

# Transcription: DNA to RNA

## Core Idea
Transcription is the synthesis of an RNA molecule complementary to a DNA template, carried out by RNA polymerase. The enzyme binds to a promoter sequence upstream of the gene, unwinds the double helix, and synthesizes RNA in the 5'-to-3' direction using the template (antisense) strand. In prokaryotes, a single RNA polymerase handles all RNA types; eukaryotes use three specialized polymerases (RNA Pol I, II, III). The product is a primary transcript that in eukaryotes requires further processing before translation.

## How It's Best Learned
Map promoter elements (TATA box, -10/-35 boxes) and trace the polymerase through initiation, elongation, and termination. Compare prokaryotic and eukaryotic transcription side by side.

## Common Misconceptions
- The coding strand and the template strand are often confused; RNA sequence matches the coding strand (with U replacing T), not the template strand.
- Transcription and replication both involve strand separation but use different enzymes and have distinct purposes.

## Questions

```yaml
- question: "A DNA template strand reads 3'-ATCGTA-5'. What is the sequence of the RNA transcript produced from this strand?"
  type: multiple-choice
  options:
    - "3'-ATCGTA-5'"
    - "5'-TAGCTA-3'"
    - "5'-UAGCAU-3'"
    - "3'-UAGCAU-5'"
  answer: 2
  explanation: "RNA polymerase reads the template strand 3'→5' and synthesizes RNA 5'→3' by complementary base pairing (A→U, T→A, C→G, G→C). Reading 3'-ATCGTA-5' gives RNA 5'-UAGCAU-3'. Option B is incorrect because it uses T instead of U. Option D has the wrong directionality. The RNA matches the coding strand sequence (with U replacing T), which is why option C is correct."

- question: "The RNA sequence produced during transcription is identical to the coding (non-template) strand of DNA, except that uracil replaces thymine."
  type: true-false
  answer: true
  explanation: "RNA polymerase uses the template (antisense) strand as a guide, synthesizing RNA complementary to it. Since the coding strand and template strand are complementary to each other, the RNA produced is the same sequence as the coding strand — with U in place of T. This is why the coding strand is also called the 'sense strand': it has the same sequence as the mRNA (with T→U substitution). Many students confuse which strand is read, but the product always matches the coding strand."

- question: "Why can prokaryotes begin translating an mRNA while transcription is still in progress, but eukaryotes cannot?"
  type: short-answer
  answer: "In prokaryotes, there is no nuclear membrane separating transcription from translation — both occur in the same cytoplasmic compartment simultaneously. In eukaryotes, transcription occurs in the nucleus and the primary transcript must be processed (5' cap, poly-A tail, splicing of introns) before export to the cytoplasm, where translation occurs. The physical and processing separation makes concurrent transcription-translation impossible."
  explanation: "This structural difference has major consequences for gene regulation. Prokaryotes can respond to environmental signals almost instantly by beginning translation as soon as RNA synthesis starts. Eukaryotes pay a time and energy cost in RNA processing but gain regulatory opportunities: alternative splicing, nuclear export control, and RNA stability mechanisms all act between transcription and translation, enabling far more complex gene regulation."
```

## Explainer

Transcription is the first step in converting the genetic information stored in DNA into a functional product. The central idea is straightforward: one strand of the DNA double helix is used as a template to synthesize a complementary RNA molecule. But the details of how this happens — and how it differs between prokaryotes and eukaryotes — reveal a great deal about how cells control which genes are expressed.

The process begins with **initiation**. RNA polymerase must recognize where to start. It does this by binding to a specific DNA sequence called a *promoter*, located upstream (in the 5' direction of the coding strand) from the gene. In prokaryotes, promoters have conserved sequences around positions −10 and −35 relative to the transcription start site. In eukaryotes, promoters are more complex and often include a TATA box, and RNA Pol II requires a set of *transcription factors* to assemble at the promoter before the polymerase can bind. This added complexity is a major mechanism for differential gene expression in eukaryotes.

Once bound, RNA polymerase unwinds a short stretch of the double helix and begins **elongation**: reading the template strand in the 3'→5' direction and synthesizing the RNA strand in the 5'→3' direction. The base-pairing rules are the same as in DNA replication — A pairs with U (not T, since RNA uses uracil), T pairs with A, C with G, G with C. A key point worth emphasizing: the RNA produced is *not* complementary to the coding strand — it is *identical* to it (with U replacing T). Students often confuse this because the polymerase physically reads the template strand, but the product mirrors the coding strand. This is why the coding strand is sometimes called the "sense strand."

**Termination** occurs when the polymerase reaches a terminator sequence. In prokaryotes, this can be a hairpin loop in the nascent RNA that causes the polymerase to stall and dissociate. In eukaryotes, termination is coupled to cleavage and polyadenylation of the transcript. After termination, eukaryotic pre-mRNA undergoes extensive *processing* before it can be translated: a 5' cap (a modified guanosine) and a poly-A tail are added for stability and nuclear export, and *introns* — non-coding intervening sequences — are spliced out by the spliceosome, leaving only the coding exons joined together.

The contrast between prokaryotic and eukaryotic transcription illustrates a broader principle: complexity in gene regulation scales with organismal complexity. Prokaryotes sacrifice regulatory sophistication for speed — they can translate mRNA while it is still being transcribed because there is no nuclear membrane separating the two processes. Eukaryotes pay a time and energy cost in RNA processing but gain multiple checkpoints at which gene expression can be regulated, enabling the cell-type-specific gene expression that underlies development.
