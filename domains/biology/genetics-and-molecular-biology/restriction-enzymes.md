---
id: restriction-enzymes
title: Restriction Enzymes and DNA Cutting
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-structure
  type: hard
builds-toward:
- pcr
- recombinant-dna-technology
tags:
- restriction enzyme
- restriction site
- sticky ends
- blunt ends
- palindrome
stage: formal-systems
status: validated
---

# Restriction Enzymes and DNA Cutting

## Core Idea
Restriction endonucleases (restriction enzymes) are bacterial proteins that cleave double-stranded DNA at specific recognition sequences, typically 4–8 bp palindromes. Type II restriction enzymes cut within or adjacent to their recognition sequence, producing either sticky (cohesive) ends with short single-stranded overhangs or blunt ends. Sticky ends from compatible enzymes can base-pair with complementary sequences and be joined by DNA ligase, enabling directed assembly of recombinant DNA molecules. Bacteria protect their own DNA from restriction cleavage through methylation of the recognition sites by companion methyltransferases.

## How It's Best Learned
Given a circular plasmid map with restriction sites, predict the number and sizes of fragments produced by single and double digests. Confirm predictions by calculating fragment sizes against the total plasmid length.

## Common Misconceptions
- Restriction enzymes do not cut randomly; they are exquisitely specific to their recognition sequence.
- Two sticky ends from different enzymes that happen to be compatible can be joined, even if the original recognition site is not regenerated.

## Questions

```yaml
- question: "Two DNA fragments are cut with two different restriction enzymes that happen to produce the same 4-nucleotide 5' overhang. They are mixed and ligated together. Which statement best describes the resulting junction?"
  type: multiple-choice
  options:
    - "Both original restriction sites are fully regenerated at the junction, so either enzyme can cut there again"
    - "The junction contains a hybrid sequence from both original sites; it may not be recognized by either enzyme"
    - "The ligation fails because compatible sticky ends from different enzymes cannot pair"
    - "The junction is blunt-ended because ligation removes the single-stranded overhangs"
  answer: 1
  explanation: "Compatible sticky ends base-pair and are sealed by ligase regardless of which enzyme produced them. However, the full recognition sequence of a restriction enzyme extends beyond the overhang into the flanking DNA. When two fragments from different enzyme sites are joined, the resulting junction sequence is a hybrid of both sites' flanking sequences — and this hybrid may not match the complete recognition sequence of either original enzyme. This is actually useful in cloning: you can join fragments without worrying about re-cutting by the original enzyme."

- question: "A restriction enzyme produces blunt-ended cuts. Compared to sticky-end-producing enzymes, blunt-end ligation in recombinant DNA work is..."
  type: multiple-choice
  options:
    - "More efficient, because blunt ends can join in any orientation without overhang constraints"
    - "Equally efficient, since DNA ligase seals phosphodiester bonds identically in both cases"
    - "Less efficient, because no single-stranded overhangs provide temporary base-pairing to bring the ends together"
    - "Impossible without a different class of ligase specialized for blunt-end joins"
  answer: 2
  explanation: "Sticky ends have complementary single-stranded overhangs that base-pair with each other, transiently holding the two DNA molecules in close proximity before ligase seals the backbone. This dramatically increases ligation efficiency. Blunt ends have no such stabilization — the two fragments must collide and be held together long enough for ligase to act. Blunt-end ligation is possible but far less efficient, often requiring higher DNA concentrations and longer reaction times. Directionality is also lost with blunt ends since either end can join to either other end."

- question: "A bacterium's own DNA is immune to cleavage by its restriction enzymes because its genome lacks the palindromic recognition sequences that restriction enzymes target."
  type: true-false
  answer: false
  explanation: "This is a common misconception. The bacterium's genome DOES contain restriction sites — the same palindromic sequences the enzyme recognizes. Protection comes from a companion methyltransferase that adds methyl groups to adenine or cytosine bases within those recognition sequences. Methylated DNA is not cut by the restriction enzyme. Invading phage DNA, which lacks the host's methylation pattern, is recognized as foreign and cleaved. This restriction-modification system is a molecular 'self vs. non-self' detection mechanism, not an absence of target sequences."

- question: "Restriction enzymes recognize palindromic DNA sequences, meaning the sequence reads identically on both strands in the 5' to 3' direction."
  type: true-false
  answer: true
  explanation: "A DNA palindrome is defined by reading both strands 5' to 3'. For EcoRI's site: the top strand 5'-GAATTC-3' and the bottom strand (complementary, antiparallel) also reads 5'-GAATTC-3'. This palindromic symmetry is what allows the enzyme to bind with identical contacts on both sides of the double helix — it sees the same sequence on each strand. The two-fold symmetry of the recognition site matches the two-fold symmetry of the homodimeric enzyme, which is why most restriction enzymes are dimers that cut both strands."

- question: "Explain why sticky ends — rather than blunt ends — are preferred for constructing recombinant DNA molecules, even though both can be ligated."
  type: short-answer
  answer: "Sticky ends have short single-stranded overhangs that base-pair specifically with complementary overhangs, providing temporary stabilization that dramatically increases ligation efficiency. They also confer directionality: a specific sticky end from one enzyme will only join with a compatible partner, not with any random blunt end. Blunt ends can join in any orientation and with any other blunt end, sacrificing specificity. The base-pairing of sticky ends also increases the local concentration of the two fragments relative to each other, making productive ligase encounters far more frequent."
  explanation: "In molecular cloning, efficiency and specificity both matter. Sticky-end ligation can be 10–100× more efficient than blunt-end ligation. The directional specificity ensures that an insert goes into a vector in the correct orientation — something blunt ends cannot guarantee. This control over orientation is critical when the insert must be expressed in a particular reading frame."
```

## Explainer

You already know that DNA is a double-stranded helix with complementary base pairing. Restriction enzymes are molecular scissors that exploit a specific feature of DNA sequence: **palindromic recognition sites**. A DNA palindrome reads the same on both strands in the 5' to 3' direction — for example, the sequence GAATTC on one strand is matched by GAATTC on the complementary strand (reading in the opposite direction). The enzyme EcoRI recognizes exactly this six-base palindrome and cuts between the G and A on each strand, every time, with extraordinary precision. This specificity is not approximate — a single base change in the recognition site prevents cutting entirely.

When a restriction enzyme cuts within a palindrome, it can produce two different types of ends depending on where the cuts fall. **Sticky ends** (also called cohesive ends) result when the enzyme makes staggered cuts on the two strands, leaving short single-stranded overhangs. These overhangs can base-pair with any other compatible sticky end through hydrogen bonding, just as the two strands of DNA pair during replication. **Blunt ends** result when the enzyme cuts both strands at the same position, leaving no overhang. Sticky ends are far more useful in molecular biology because their overhangs provide temporary, specific attachment points — DNA ligase can then seal the backbone permanently.

This cut-and-paste logic is what makes recombinant DNA technology possible. If you cut two different DNA molecules with the same restriction enzyme, both will have compatible sticky ends. Mix them together, and the overhangs will find each other through complementary base pairing. Ligase seals the joins, and you have a hybrid molecule combining sequences from two different sources. This is how genes are inserted into plasmid vectors, how DNA libraries are constructed, and how the first genetically engineered organisms were created.

Bacteria evolved restriction enzymes as a defense system against invading phage DNA. When a bacteriophage injects its DNA into a bacterial cell, restriction enzymes recognize and cut the foreign DNA at its palindromic sites. The bacterium protects its own DNA through a companion **methyltransferase** that adds methyl groups to the same recognition sequences, blocking the restriction enzyme from cutting. This restriction-modification system is essentially an immune system for bacteria — it distinguishes self from non-self at the molecular level. The discovery of these enzymes in the 1970s transformed biology from an observational science into an engineering discipline, giving researchers precise, programmable tools for cutting DNA at defined locations.
