---
id: specialized-transduction-excision
title: Specialized Transduction and Prophage Excision
domain: biology
course: microbiology
prerequisites:
- id: viral-replication-cycle
  type: hard
- id: generalized-transduction-phage
  type: soft
builds-toward:
- temperate-phage-lysogeny
tags:
- transduction
- prophage
- excision
stage: advanced
status: draft
---

# Specialized Transduction and Prophage Excision

## Core Idea
Temperate phages integrate at specific chromosomal attachment (att) sites. Inaccurate excision of a prophage from the chromosome can transfer adjacent bacterial genes while leaving behind phage genes, creating defective phages that carry bacterial DNA. This specialized transduction is limited to genes near the att site but can efficiently move these genes between cells.

## Explainer

You already know from studying the viral replication cycle that temperate phages can integrate their DNA into the host chromosome rather than immediately lysing the cell. The integrated phage DNA — the **prophage** — sits quietly within the bacterial genome, flanked by specific attachment sites called **attL** and **attR** (left and right). These att sites are hybrids: each contains sequences from both the original phage att site and the bacterial att site, created during the recombination event that inserted the phage. The prophage is replicated passively along with the chromosome, sometimes for hundreds of bacterial generations.

The interesting biology begins when the prophage excises. Normal excision is the precise reverse of integration: recombination between attL and attR regenerates the intact circular phage genome and restores the bacterial chromosome. But occasionally — roughly once per 10⁵ to 10⁶ excision events — the recombination machinery cuts at the wrong position. Instead of cutting exactly at the att boundaries, it cuts asymmetrically, grabbing a stretch of adjacent bacterial DNA on one side while leaving behind a corresponding stretch of phage DNA. The result is a **defective transducing phage** particle: it carries some bacterial genes but has lost some of its own genes and typically cannot complete a lytic cycle on its own.

This is what distinguishes **specialized transduction** from the generalized transduction you studied earlier. In generalized transduction, any bacterial gene can be accidentally packaged because the phage headful-packaging mechanism occasionally grabs random chromosomal fragments. In specialized transduction, only genes immediately flanking the prophage integration site can be transferred. For the classic example of phage lambda in *E. coli*, the att site sits between the **gal** operon (galactose metabolism) and the **bio** operon (biotin synthesis), so lambda can only transduce gal or bio genes — never genes from distant parts of the chromosome.

When a defective transducing phage injects its hybrid DNA into a new recipient cell, the bacterial genes it carries can recombine into the recipient's chromosome, giving the recipient new genetic capabilities. Because the transducing particle delivers the same flanking genes every time (not random fragments), specialized transduction is highly efficient for those specific genes — far more so than generalized transduction for any single gene. This reliability made specialized transduction a powerful early tool for fine-structure genetic mapping near phage attachment sites, and it remains a vivid illustration of how imprecise molecular machinery can drive horizontal gene transfer in bacterial populations.
