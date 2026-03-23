---
id: transposable-elements
title: Transposable Elements and Evolution
domain: biology
course: evolutionary-biology
prerequisites:
- id: dna-mutations
  type: hard
builds-toward:
- genomic-reorganization
tags:
- molecular-evolution
- mobile-elements
- genomics
stage: advanced
status: validated
---

# Transposable Elements and Evolution

## Core Idea
Transposable elements (TEs) are mobile DNA sequences that can copy themselves throughout genomes, sometimes comprising >45% of mammalian genomes. Though mostly silenced, TEs contribute to evolution through insertional mutagenesis, recombination, and exaptation (co-option of TE sequences for new functions). TE activity varies across species and lineages.

## Questions

```yaml
- question: "Which of the following is the best example of TE exaptation — the co-option of a transposable element sequence for a new host function?"
  type: multiple-choice
  options:
    - "A LINE element inserting into an exon and disrupting the encoded protein"
    - "The RAG1 and RAG2 recombinase enzymes, which drive V(D)J recombination in the vertebrate immune system and evolved from an ancient transposase"
    - "DNA methylation silencing active TEs throughout the genome"
    - "A retrotransposon increasing from 10 to 10,000 copies across generations"
  answer: 1
  explanation: "Exaptation is the evolutionary co-option of an existing structure or sequence for a new function different from its original one. The RAG1/RAG2 system is a canonical example: what was once a transposase — an enzyme that mobilized a DNA transposon — was co-opted to perform the site-specific recombination that generates antibody and T-cell receptor diversity in jawed vertebrates. This illustrates the key insight that TEs are not merely parasites but a major source of evolutionary novelty. Options A and C represent host-TE conflict; option D illustrates TE replication, not exaptation."

- question: "A researcher observes that a mobile element in a plant genome has increased from approximately 50 copies to over 5,000 copies over the course of 50 generations. Which mechanism most likely explains this copy number increase?"
  type: multiple-choice
  options:
    - "Cut-and-paste transposition by a Class II DNA transposon, where the element excises and reinserts elsewhere"
    - "Copy-and-paste retrotransposition: the element is transcribed to RNA, reverse-transcribed to DNA, and the new copy integrates while the original remains"
    - "Ectopic recombination between existing copies amplifying them through tandem duplication"
    - "The transposase enzyme replicating independently of the host genome"
  answer: 1
  explanation: "Class I retrotransposons use a copy-and-paste mechanism: the element is transcribed into RNA, then reverse-transcribed back into DNA by a reverse transcriptase encoded by the element itself, and the new DNA copy integrates at a new genomic location — leaving the original intact. This inherently increases copy number with each successful transposition event, explaining how retrotransposons can reach hundreds of thousands of copies (e.g., human Alu elements: ~1 million copies). Class II DNA transposons (cut-and-paste) do not inherently increase copy number because the original is excised; the only way they gain copies is if the donor site is replicated before transposition."

- question: "Class II DNA transposons increase their copy number with each transposition event because the original element remains in place while a new copy is inserted at a different location."
  type: true-false
  answer: false
  explanation: "This description actually applies to Class I retrotransposons (copy-and-paste). Class II DNA transposons use a cut-and-paste mechanism: the transposase enzyme excises the element from its current location and inserts it elsewhere. The original copy does not remain — it is moved, not copied. Copy number stays the same (or can actually decrease if excision is imprecise). DNA transposons can occasionally achieve net copy number gains if transposition happens during S phase after the donor site has been replicated but before the target site has been, but this is not inherent to the mechanism."

- question: "Although most TE copies in mammalian genomes are inactive or silenced, TEs have been a significant source of regulatory sequences, novel proteins, and evolutionary innovations over deep evolutionary time."
  type: true-false
  answer: true
  explanation: "Despite the fact that most TE copies are mutated into silence or actively suppressed by DNA methylation and small RNA pathways, the sheer abundance of TE sequences (~45% of the human genome, >80% of maize) means that even a tiny fraction of exaptation events produces enormous numbers of new regulatory elements and functional sequences. Documented examples include RAG1/RAG2 (adaptive immunity), syncytin proteins (placental development from retroviral envelope genes), and thousands of enhancers and promoters derived from TE sequences. TEs are a primary driver of regulatory evolution and genomic novelty."

- question: "Why does the host genome evolve mechanisms to suppress TE activity, and how can TEs nonetheless contribute to evolutionary novelty despite this suppression?"
  type: short-answer
  answer: "TEs are suppressed because they are primarily harmful in the short term: insertions into genes disrupt function, and ectopic recombination between dispersed TE copies causes chromosomal rearrangements (deletions, inversions, duplications). The host genome and its TEs exist in an evolutionary arms race, with TEs 'seeking' to replicate and the host evolving DNA methylation, piRNA pathways, and other silencing mechanisms to keep them in check. Despite this suppression, TEs contribute to novelty over deep evolutionary time in two ways: first, occasional insertions in regulatory regions can fortuitously improve fitness and be preserved by natural selection; second, TE-derived sequences can be exapted — their coding or regulatory potential repurposed entirely — as occurred with the RAG recombinase and syncytin. The critical insight is that a mechanism that is harmful on average can still be a net source of innovation across millions of years of evolution."
  explanation: "The host-TE relationship is often called 'genomic parasitism,' but this framing is incomplete. TEs are more accurately understood as an ongoing source of mutational variation — mostly neutral or deleterious, occasionally beneficial — at a scale that single-nucleotide mutations cannot match."
```

## Explainer

From your study of DNA mutations, you know that changes to the genome — substitutions, insertions, deletions — provide the raw material for evolution. **Transposable elements** (TEs) represent an entirely different scale of genomic change: rather than single-nucleotide alterations, TEs are sequences hundreds to thousands of base pairs long that can move or copy themselves to new locations within the genome. They are sometimes called "jumping genes," a term coined by Barbara McClintock, who first discovered them in maize in the 1940s. Far from being rare curiosities, TEs make up roughly 45% of the human genome and over 80% of some plant genomes like maize.

TEs fall into two major classes based on their mechanism of movement. **Class I elements** (retrotransposons) use a "copy-and-paste" mechanism: they are transcribed into RNA, reverse-transcribed back into DNA, and the new DNA copy inserts at a new genomic location. The original copy stays put, so retrotransposons increase in copy number over time. LINEs (Long Interspersed Nuclear Elements) and SINEs (Short Interspersed Nuclear Elements, including the human Alu element) are the most abundant retrotransposons in mammalian genomes. **Class II elements** (DNA transposons) use a "cut-and-paste" mechanism: the element is excised from one location and inserted into another by a transposase enzyme. DNA transposons do not inherently increase in copy number, though replication timing can sometimes produce a net gain.

Most TE copies in any genome are inactive — mutated into silence over millions of years, or actively repressed by the host through DNA methylation and small RNA pathways. This is because TE insertions are usually neutral or harmful: an element landing inside a gene can disrupt its function, and ectopic recombination between dispersed TE copies can cause chromosomal rearrangements like deletions, duplications, and inversions. The genome and its TEs exist in a kind of evolutionary tension, with TEs "seeking" to replicate and the host genome evolving mechanisms to suppress them.

Yet TEs are far more than genomic parasites. Over evolutionary time, TE sequences have been **exapted** — co-opted for host functions — in remarkable ways. Regulatory sequences derived from TEs have been repurposed as enhancers, promoters, and insulators controlling host gene expression. The RAG1 and RAG2 enzymes that drive V(D)J recombination in the vertebrate adaptive immune system evolved from a transposase. Syncytin proteins, essential for placental development in mammals, derive from retroviral envelope genes. These examples illustrate a broader principle: TEs are a major source of evolutionary novelty, seeding genomes with raw material that natural selection can occasionally reshape into new functions.
