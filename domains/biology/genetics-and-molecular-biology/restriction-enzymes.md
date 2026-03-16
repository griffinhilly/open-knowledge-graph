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

## Explainer

You already know that DNA is a double-stranded helix with complementary base pairing. Restriction enzymes are molecular scissors that exploit a specific feature of DNA sequence: **palindromic recognition sites**. A DNA palindrome reads the same on both strands in the 5' to 3' direction — for example, the sequence GAATTC on one strand is matched by GAATTC on the complementary strand (reading in the opposite direction). The enzyme EcoRI recognizes exactly this six-base palindrome and cuts between the G and A on each strand, every time, with extraordinary precision. This specificity is not approximate — a single base change in the recognition site prevents cutting entirely.

When a restriction enzyme cuts within a palindrome, it can produce two different types of ends depending on where the cuts fall. **Sticky ends** (also called cohesive ends) result when the enzyme makes staggered cuts on the two strands, leaving short single-stranded overhangs. These overhangs can base-pair with any other compatible sticky end through hydrogen bonding, just as the two strands of DNA pair during replication. **Blunt ends** result when the enzyme cuts both strands at the same position, leaving no overhang. Sticky ends are far more useful in molecular biology because their overhangs provide temporary, specific attachment points — DNA ligase can then seal the backbone permanently.

This cut-and-paste logic is what makes recombinant DNA technology possible. If you cut two different DNA molecules with the same restriction enzyme, both will have compatible sticky ends. Mix them together, and the overhangs will find each other through complementary base pairing. Ligase seals the joins, and you have a hybrid molecule combining sequences from two different sources. This is how genes are inserted into plasmid vectors, how DNA libraries are constructed, and how the first genetically engineered organisms were created.

Bacteria evolved restriction enzymes as a defense system against invading phage DNA. When a bacteriophage injects its DNA into a bacterial cell, restriction enzymes recognize and cut the foreign DNA at its palindromic sites. The bacterium protects its own DNA through a companion **methyltransferase** that adds methyl groups to the same recognition sequences, blocking the restriction enzyme from cutting. This restriction-modification system is essentially an immune system for bacteria — it distinguishes self from non-self at the molecular level. The discovery of these enzymes in the 1970s transformed biology from an observational science into an engineering discipline, giving researchers precise, programmable tools for cutting DNA at defined locations.
