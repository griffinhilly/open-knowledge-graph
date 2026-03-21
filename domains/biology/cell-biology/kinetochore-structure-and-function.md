---
id: kinetochore-structure-and-function
title: Kinetochore Structure and Function
domain: biology
course: cell-biology
prerequisites:
- id: dna-structure
  type: hard
- id: mitotic-spindle-checkpoint
  type: hard
builds-toward:
- sister-chromatid-cohesion-cohesin-proteins
- anaphase-promoting-complex-cell-cycle-control
tags:
- kinetochore
- chromosome-segregation
- spindle-attachment
stage: advanced
status: draft
---

# Kinetochore Structure and Function

## Core Idea
The kinetochore is a megadalton protein assembly on centromeric chromatin serving as the attachment site for spindle microtubules during chromosome segregation. Over 100 proteins organized into distinct subcomplexes (KMN network: KNL1, MIS12, NDC80 complex) mediate dynamic interactions with kinetochore microtubules and transmit tension signals. The kinetochore also functions as a molecular checkpoint: it monitors biorientation (amphitelic attachment) and prevents anaphase until all sister chromatid pairs achieve proper attachment.

## How It's Best Learned
Visualize kinetochore structure by cryo-EM or immunofluorescence; measure kinetochore-microtubule dynamics using live-cell imaging. Use purified components to reconstitute kinetochore assembly and test force generation.

## Common Misconceptions
- Kinetochores are static; they dynamically remodel as microtubules polymerize and depolymerize. - One kinetochore attaches to many microtubules; tension is distributed across the attachment site.

## Questions

```yaml
- question: "A chromosome achieves syntelic attachment — both sister kinetochores connect to microtubules from the SAME pole. Why does this incorrect attachment fail to silence the spindle assembly checkpoint?"
  type: multiple-choice
  options:
    - "Because syntelic attachment leaves one kinetochore completely unattached, which the SAC directly detects"
    - "Because the KMN network cannot bind microtubules from the same pole simultaneously"
    - "Because syntelic attachment does not generate tension across the kinetochore pair — without opposing pole pulling, there is no stretch between sisters, so checkpoint kinases remain active"
    - "Because Mad1 and Mad2 are only released when both kinetochores are occupied by at least 10 microtubules each"
  answer: 2
  explanation: "The SAC monitors both attachment AND tension. Syntelic attachment means both sisters are occupied by microtubules, but they pull in the same direction — so the kinetochore pair experiences no opposing forces and generates no tension. Tension physically stretches the structure, separating kinase substrates from their phosphatases and stabilizing correct attachments. Without tension, checkpoint signaling continues even though microtubules are present. This is why 'attached' is not sufficient — only amphitelic (bi-oriented) attachment generates the mechanical force that satisfies the checkpoint."

- question: "Why do kinetochore proteins form low-affinity, rapidly exchanging contacts with microtubule plus-ends rather than forming a rigid, stable clamp?"
  type: multiple-choice
  options:
    - "Because high-affinity binding would trigger apoptosis pathways in the cell"
    - "Because the NDC80 complex lacks the structural domains needed for stable microtubule binding"
    - "Because chromosome movement depends on riding the energy of microtubule depolymerization, which requires the kinetochore to maintain attachment to a shrinking end without irreversibly clamping it"
    - "Because stable binding would prevent other chromosomes from attaching to the same microtubule"
  answer: 2
  explanation: "Spindle microtubules undergo dynamic instability — constant cycles of polymerization and depolymerization. Chromosomes congress toward the metaphase plate and ultimately segregate by coupling to these dynamics: kinetochores can be pulled poleward by a depolymerizing microtubule, using the energy released by tubulin GTP hydrolysis. For this to work, the NDC80 complex must maintain contact with a shrinking tubulin end without locking it in place. Low-affinity contacts that exchange rapidly allow the kinetochore to 'track' the end, staying attached while the microtubule shortens. A rigid clamp would detach the instant depolymerization began."

- question: "Kinetochores are static structures that serve as simple anchor points holding chromosomes to spindle microtubules — their primary role is mechanical stability."
  type: true-false
  answer: false
  explanation: "Kinetochores are highly dynamic and serve at least two critical functions. Mechanically, they actively track dynamic microtubule plus-ends through rapidly exchanging NDC80-tubulin contacts, generating force for chromosome movement. Biochemically, they serve as the scaffold for the spindle assembly checkpoint — assembling Mad1, Mad2, and BubR1 when unattached or under-tensioned, and dismantling this checkpoint signal once correct amphitelic attachment generates sufficient tension. Far from static anchors, kinetochores continuously remodel as microtubules polymerize and depolymerize, and they integrate mechanical and biochemical signals to coordinate chromosome segregation."

- question: "Correct (amphitelic) attachment of sister kinetochores to microtubules from opposite poles generates tension that physically stabilizes the attachment and contributes to silencing the spindle assembly checkpoint."
  type: true-false
  answer: true
  explanation: "Tension is the physical readout of correct bi-orientation. When sister kinetochores connect to opposite poles, the pulling forces stretch the kinetochore structure. This stretch physically separates kinase substrates from their phosphatases at the outer kinetochore — phosphatase access stabilizes the attachment by preventing premature detachment. At the same time, the tension-induced structural change reduces the scaffolding activity for Mad1/Mad2 checkpoint complex assembly, contributing to SAC silencing. Incorrect attachments (syntelic, merotelic) don't generate proper tension, maintaining the checkpoint signal and triggering error correction by Aurora B kinase."

- question: "Explain how the kinetochore distinguishes amphitelic (correct) from syntelic or merotelic (incorrect) attachment, and what molecular mechanism converts this physical distinction into a biochemical checkpoint signal."
  type: short-answer
  answer: "Correct amphitelic attachment pulls sister kinetochores toward opposite poles, generating tension that physically stretches the kinetochore. This stretch spatially separates kinase substrates (at the inner kinetochore, near centromeric DNA) from their phosphatases (concentrated toward the outer kinetochore), causing a net dephosphorylation state that stabilizes microtubule contacts. Incorrect attachments — syntelic (both sisters to same pole) or merotelic (one kinetochore to both poles) — generate little or incorrect tension, leaving the inner kinetochore in a phosphorylated state that destabilizes the attachment and maintains recruitment of Mad1/Mad2 checkpoint proteins. Aurora B kinase acts as the error-correction enzyme: it phosphorylates NDC80 and other outer kinetochore proteins to weaken microtubule binding, selectively destabilizing low-tension (incorrect) attachments while high-tension (correct) attachments resist its activity because their inner kinase substrates are shielded."
  explanation: "The elegance of this system is that tension converts a geometric property (which poles microtubules came from) into a structural change at the kinetochore (stretch), which then drives a biochemical change (kinase/phosphatase balance). The cell does not directly 'see' which pole a microtubule came from — it only senses whether the resulting attachment produces adequate tension. This mechanical read-out is what ultimately determines whether anaphase is permitted to proceed."
```

## Explainer

You already know that DNA is packaged into chromosomes and that the mitotic spindle checkpoint prevents cells from proceeding to anaphase until chromosomes are properly attached. The kinetochore is the molecular structure that connects these two systems — it is the physical bridge between a chromosome and the spindle microtubules that will pull it to one pole of the dividing cell. Think of it as a sophisticated coupling device: one face grips the centromeric DNA, while the other face grabs onto the dynamic plus-ends of spindle microtubules.

The **kinetochore** is not a single protein but a megadalton assembly of over 100 proteins organized into layers. The inner kinetochore sits directly on centromeric chromatin, built around specialized histone variants (CENP-A) that mark where the kinetochore should assemble. The outer kinetochore faces the cytoplasm and contains the **KMN network** — three subcomplexes called KNL1, MIS12, and NDC80. The NDC80 complex is the primary microtubule-binding component: its long, rod-shaped structure reaches out and directly contacts the tubulin subunits of kinetochore microtubules. Each kinetochore binds not just one microtubule but a bundle of them (around 20–25 in human cells), distributing the mechanical load of chromosome movement.

What makes the kinetochore remarkable is that it maintains attachment to microtubules that are constantly growing and shrinking. Microtubule plus-ends undergo **dynamic instability** — switching between polymerization and depolymerization — and the kinetochore rides these changes. During chromosome congression, the kinetochore tracks a depolymerizing microtubule end inward toward the pole and a polymerizing end outward. This requires the NDC80 complex and associated factors to form low-affinity, rapidly exchanging contacts with tubulin, rather than a rigid lock.

The kinetochore also serves as the platform for the **spindle assembly checkpoint** you studied earlier. When a kinetochore is unattached or incorrectly attached, checkpoint proteins (Mad1, Mad2, BubR1) accumulate there and generate a "wait" signal that inhibits the anaphase-promoting complex. The critical distinction is between **amphitelic attachment** — where sister kinetochores connect to microtubules from opposite poles, generating tension — and erroneous attachments like syntelic (both sisters to the same pole) or merotelic (one kinetochore to both poles). Tension across the kinetochore stretches the structure, physically separating kinase substrates from their phosphatases, which stabilizes correct attachments and destabilizes incorrect ones. Only when every chromosome achieves amphitelic attachment and sufficient tension does the checkpoint silence, allowing the cell to proceed into anaphase.
