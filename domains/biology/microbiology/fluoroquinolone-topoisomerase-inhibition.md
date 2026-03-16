---
id: fluoroquinolone-topoisomerase-inhibition
title: Fluoroquinolone Antibiotics and DNA Topoisomerase Inhibition
domain: biology
course: microbiology
prerequisites:
- id: dna-replication
  type: hard
- id: enzyme-structure-and-function
  type: soft
builds-toward:
- antibiotic-resistance-mutations-downregulation
tags:
- fluoroquinolones
- topoisomerase
- dna-gyrase
stage: formal-systems
status: draft
---

# Fluoroquinolone Antibiotics and DNA Topoisomerase Inhibition

## Core Idea
Fluoroquinolones inhibit bacterial DNA gyrase and topoisomerase IV, enzymes that manage DNA supercoiling during replication and transcription. By stabilizing the enzyme-DNA cleavage complex, fluoroquinolones prevent DNA relaxation, causing DNA breaks and cell death. Their broad spectrum and excellent bioavailability make them widely used despite rapid resistance development.

## Explainer

From your understanding of DNA replication, you know that the double helix must be unwound for the replication fork to advance. But unwinding creates a problem: as helicase separates the two strands ahead of the fork, the DNA downstream becomes overwound, accumulating **positive supercoils** that, if left unchecked, would physically halt replication by making it impossible to separate the strands further. Imagine unzipping a twisted rope from one end — the twist tightens ahead of your fingers. Bacteria solve this problem with **topoisomerases**, enzymes that cut, pass, and reseal DNA strands to relieve torsional stress.

Two topoisomerases are critical in bacteria. **DNA gyrase** (a type II topoisomerase) introduces negative supercoils by cutting both strands of DNA, passing a segment of the double helix through the break, and resealing it. This counteracts the positive supercoiling generated during replication and transcription. **Topoisomerase IV** performs a related function: it decatenates (unlinks) the two daughter chromosomes after replication is complete, allowing them to segregate into daughter cells. Without these enzymes, replication stalls, transcription grinds to a halt, and the cell cannot divide.

**Fluoroquinolones** — drugs like ciprofloxacin, levofloxacin, and moxifloxacin — exploit this dependency with a clever mechanism. They do not simply block the enzyme's active site like a traditional inhibitor. Instead, they bind to the topoisomerase while it is in the middle of its catalytic cycle — specifically, after the enzyme has cut both DNA strands but before it has resealed them. The drug **stabilizes the cleavage complex**, trapping the enzyme covalently attached to the broken DNA ends. The result is not merely an inactive enzyme but an active source of damage: the stabilized breaks become permanent double-strand breaks when the replication fork collides with the trapped complex, or when cellular processes attempt to remove the stalled enzyme. These double-strand breaks overwhelm the bacterial DNA repair machinery, triggering the SOS response and ultimately cell death.

This mechanism — converting an essential enzyme into a DNA-damaging agent — is why fluoroquinolones are bactericidal rather than merely bacteriostatic. It also explains why resistance develops: mutations in the **quinolone resistance-determining region (QRDR)** of the gyrase or topoisomerase IV genes alter the drug-binding site just enough to prevent fluoroquinolone binding while preserving enzymatic function. In Gram-negative bacteria, gyrase is typically the primary target, and resistance mutations appear there first; in Gram-positive bacteria, topoisomerase IV is usually the primary target. High-level resistance often requires mutations in both targets, which is why fluoroquinolone resistance typically evolves in a stepwise fashion through sequential mutations.
